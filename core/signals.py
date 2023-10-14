from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from .models import Progress

import os

@receiver(post_save, sender=Progress)
def check_and_send_completion_email(sender, instance, **kwargs):
    if instance.days_remaining == 0:
        instance.mark_as_complete()
        instance.save()

        subject = 'Book Finished'
        from_email = os.environ.get('EMAIL_USER')
        recipient_list = [instance.user.email]
        
        text_content = strip_tags(f"Congratulations! You have finished the book '{instance.book.title}'. You can download it from here: {instance.book.pdf_file.url}.")

        template = 'core/email.html'
        html_content = render_to_string(template, {'book_title': instance.book.title, 'pdf_url': instance.book.pdf_file.url})
 
        email = EmailMultiAlternatives(subject, text_content, from_email, recipient_list)
        email.attach_alternative(html_content, "text/html")

        email.send()
