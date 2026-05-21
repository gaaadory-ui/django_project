from django.db import models

class Courier(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    vehicle_type = models.CharField(max_length=50) # نوع المركبة (دباب، سيارة، إلخ)

    def __str__(self):
        return self.name