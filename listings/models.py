from django.db import models

class Listing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Booking(models.Model):
    email = models.EmailField()
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bookings")
    user_name = models.CharField(max_length=255)
    check_in_date = models.DateTimeField(auto_now_add=True)
    check_out_date = models.DateTimeField()

    def __str__(self):
        return f"Booking for {self.listing.title} by {self.user_name}"

class Review(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="reviews")
    user_name = models.CharField(max_length=255)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"Review for {self.listing.title} by {self.user_name}"
