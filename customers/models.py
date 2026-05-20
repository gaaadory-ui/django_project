from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    # تعريف أعمدة الجدول
    first_name = models.CharField(max_length=100) # نص محدد الطول
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)       # بريد إلكتروني فريد
    age = models.IntegerField()                  # رقم صحيح
    joined_date = models.DateField(auto_now_add=True) # تاريخ يضاف تلقائياً عند الإنشاء
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    # للتحكم في كيفية ظهور الكائن عند طباعته (في لوحة التحكم مثلاً)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"