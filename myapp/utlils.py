from django.core.mail import send_mail
from auth_system.settings import EMAIL_HOST_USER


def _send_mail_to_users(email, token):
    subject = 'Hello'
    message = f'Click on the link to verify your account http://127.0.0.1:8000/verify/{token} '
    # message = f'Hello Test Email'
    from_email = EMAIL_HOST_USER
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list, fail_silently=False)