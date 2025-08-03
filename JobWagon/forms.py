# from django import forms
# from .models import Bookings

# class BookingStatusForm(forms.ModelForm):
#     class Meta:
#         model = Bookings
#         fields = ['status']

from django import forms
from .models import Bookings

class BookingStatusForm(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = ['status', 'reason']  # Include the reason field
        widgets = {
            'reason': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter reason for status change'}),
        }
