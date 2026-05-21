from django import forms
from .models import Courier

class CourierForm(forms.ModelForm):
    class Meta:
        model = Courier
        fields = ['name', 'phone', 'vehicle_type']