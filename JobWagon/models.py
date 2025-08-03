from django.db import models

class Bookings(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Verified', 'Verified'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    PARTNER_STATUS_CHOICES = [
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
        ('Pending', 'Pending'),
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=200)
    purpose = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    hours = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    partner_status = models.CharField(max_length=10, choices=PARTNER_STATUS_CHOICES, default='Pending')  # Partner's decision
    reason = models.TextField(blank=True, null=True,default='Verifying Your Details')  # Field for status update reason

    def __str__(self):
        return f"{self.name} - {self.purpose} ({self.date} at {self.time}) "

class Partner(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=128)
    adhaar = models.CharField(max_length=20)
    city = models.CharField(max_length=50)


