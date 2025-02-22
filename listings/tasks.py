from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from listings.models import Booking

@shared_task
def send_booking_confirmation_email(booking_id, user_email):
    """
    Task to send a booking confirmation email including the listing title and checkout date.
    """
    try:
        booking = Booking.objects.get(pk=booking_id)
    except Booking.DoesNotExist:
        return

    listing_title = booking.listing.title
    checkout_date = booking.check_out_date.strftime('%Y-%m-%d')

    subject = 'Booking Confirmation'
    message = (
        f"Your booking for '{listing_title}' has been confirmed.\n"
        f"Checkout Date: {checkout_date}\n\n"
        "Thank you for choosing us!"
    )
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]

    send_mail(subject, message, from_email, recipient_list)