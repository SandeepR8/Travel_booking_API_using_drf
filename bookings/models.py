from django.db import models
from django.contrib.auth.models import User



# Bus Model

class Bus(models.Model):
    bus_name = models.CharField(max_length=255)
    bus_code = models.CharField(max_length=20,unique=True)
    origin = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    features = models.TextField()
    start_time = models.TimeField()
    reach_time = models.TimeField()
    seat_count = models.PositiveBigIntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=20,decimal_places=2)

    class Meta:
        verbose_name = 'Bus'
        verbose_name_plural = 'Buses'

    def __str__(self):
        return f'{self.bus_name} bus travels from {self.origin} to {self.destination}'

# Seat model 
class Seat(models.Model):
    bus = models.ForeignKey('Bus', on_delete=models.CASCADE, related_name='seats')
    seat_no = models.CharField(max_length=10)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f'seat number {self.seat_no} booked in {self.bus.bus_name}'


# Bookings model

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    booking_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} booked {self.bus.bus_name} of seat {self.seat.seat_no} at {self.booking_at}'
