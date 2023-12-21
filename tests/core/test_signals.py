from django.core import mail

from core.models import Progress, Book
from core.signals import send_completion_email_after_seven_days

from userAuths.models import CustomUser

import pytest

@pytest.mark.django_db
@pytest.mark.celery
@pytest.mark.xfail
class TestEmailSignal:
    def test_send_completion_email_after_seven_days(celery_worker):
        user = CustomUser.objects.create(username='test', email='test@example.com')
        book = Book.objects.create(title='test-book')
        book = Book.objects.create(title='test-book')
        progress = Progress.objects.create(user=user, book=book)

        """
          Checking days remain is not equal to 0 since the send_completion_email_after_seven_days is yet
          to called with the countdown in the read function in the view.

        """
        assert progress.days_remaining != 0

        # Call the Celery task asynchronously
        send_completion_email_after_seven_days.apply_async(args=[str(progress.id)], countdown=2 * 60)

        # Check if the task was received by Celery
        tasks = celery_worker.app.control.inspect().active_queues()
        assert tasks is not None
        # assert 'send_completion_email_after_seven_days' in tasks
