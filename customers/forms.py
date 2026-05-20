# customers/forms.py
from django import forms
from .models import Customer

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        # تحديد الحقول التي نريد أن تظهر للمستخدم ليعبئها
        fields = ['first_name', 'last_name', 'email', 'age','department']