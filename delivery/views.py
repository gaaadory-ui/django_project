from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Courier

# 1. عرض البيانات (Read)
class CourierListView(ListView):
    model = Courier
    template_name = 'delivery/courier_list.html'
    context_object_name = 'couriers'

# 2. تعديل البيانات (Update)
class CourierUpdateView(UpdateView):
    model = Courier
    template_name = 'delivery/courier_form.html'
    fields = ['name', 'phone', 'vehicle_type']
    success_url = reverse_lazy('courier_list')

# 3. حذف البيانات (Delete)
class CourierDeleteView(DeleteView):
    model = Courier
    template_name = 'delivery/courier_confirm_delete.html'
    success_url = reverse_lazy('courier_list')

class CourierCreateView(LoginRequiredMixin, CreateView):
    model = Courier
    template_name = 'dlivery/courier_form.html' # يعيد استخدام نفس قالب النموذج الذي أنشأناه سابقاً
    fields = ['name', 'phone', 'vehicle_type'] # الحقول المطلوبة للإدخال
    success_url = reverse_lazy('courier_list') # التوجيه لقائمة المناديب تلقائياً بعد الحفظ
    login_url = 'login' # حماية الصفحة ومنع الزوار غير المسجلين من الدخول