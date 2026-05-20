# customers/serializers.py
from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        # تحديد الحقول التي نريد إرسالها لتطبيق الموبايل (أو الـ Frontend)
        fields = ['id', 'first_name', 'last_name', 'email', 'age', 'department']