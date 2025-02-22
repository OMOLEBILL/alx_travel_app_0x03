from django.shortcuts import render
from rest_framework import viewsets
from listings.models import Listing, Booking
from listings.serializers import ListingSerializer, BookingSerializer
from listings.tasks import send_booking_confirmation_email

class ListingViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Listing instances.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Booking instances.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        # Save the booking instance
        booking = serializer.save()
        # Trigger the task asynchronously
        send_booking_confirmation_email.delay(booking.id, booking.email)

