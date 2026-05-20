from django.contrib import admin
from .models import Customer, Department
# Register your models here.
admin.site.register(Department)
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'age', 'joined_date')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('joined_date','first_name')
    readonly_fields = ('joined_date',)



