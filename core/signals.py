from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from .models import Progress

import os

from celery import shared_task


@shared_task
def send_completion_email_after_seven_days(progress_id):
    progress = Progress.objects.get(id=progress_id)
    if progress.days_remaining == 0:
        progress.mark_as_complete()
        progress.save()

        subject = 'Book Finished'
        from_email = os.environ.get('EMAIL_USER')
        recipient_list = [progress.user.email]

        text_content = strip_tags(f"Congratulations! You have finished the book '{progress.book.title}'. You can download it from here: {progress.book.pdf_file.url}.")

        template = 'core/email.html'
        html_content = render_to_string(template, {'book_title': progress.book.title, 'pdf_url': progress.book.pdf_file.url})

        email = EmailMultiAlternatives(subject, text_content, from_email, recipient_list)
        email.attach_alternative(html_content, "text/html")

        email.send()
