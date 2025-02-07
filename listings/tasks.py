from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_booking_confirmation_email(booking_id, user_email):
    """
    Task to send a booking confirmation email.
    """
    subject = 'Booking Confirmation'
    message = f'Your booking with ID {booking_id} has been confirmed. Thank you for choosing us!'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]

    send_mail(subject, message, from_email, recipient_list)