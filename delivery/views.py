from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Courier
from .forms import CourierForm

# ---- الاستدعاءات الجديدة الخاصة بالكلاسات المتقدمة ----
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

# ==========================================
# 🌟 الكلاسات المتقدمة الجديدة (CBVs) 🌟
# ==========================================

# 1. قائمة المناديب
class CourierListView(LoginRequiredMixin, ListView):
    model = Courier
    template_name = 'delivery/courier_list.html'
    context_object_name = 'couriers'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courier_count'] = Courier.objects.count()
        context['vehicle_types'] = (
            Courier.objects.order_by('vehicle_type')
            .values_list('vehicle_type', flat=True)
            .distinct()
        )
        return context

# 2. إضافة مندوب جديد
class CourierCreateView(LoginRequiredMixin,UserPassesTestMixin, CreateView):
    model = Courier
    template_name = 'delivery/courier_register.html' # ✅ تم توجيهها لصفحة التسجيل الجديدة
    fields = ['name', 'phone', 'vehicle_type']
    success_url = reverse_lazy('courier_list')
    login_url = 'login'
    def test_func(self):
        return self.request.user.is_superuser

# 3. تعديل مندوب
class CourierUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Courier
    template_name = 'delivery/courier_form.html' # تستخدم صفحة الفورم العادية
    fields = ['name', 'phone', 'vehicle_type']
    success_url = reverse_lazy('courier_list')
    login_url = 'login'
    def test_func(self):
        return self.request.user.is_superuser

# 4. حذف مندوب
class CourierDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Courier
    template_name = 'delivery/courier_confirm_delete.html'
    success_url = reverse_lazy('courier_list')
    login_url = 'login'
    def test_func(self):
        return self.request.user.is_superuser

# ==========================================
# 🌟 واجهات برمجة التطبيقات (APIs - REST Framework) 🌟
# ==========================================
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import Serializer
from .serializers import CourierSerializer
from rest_framework.permissions import BasePermission

class IsSuperUser(BasePermission):
    """
    يسمح فقط للمستخدمين الـ Superusers بالوصول.
    """
    def has_permission(self, request, view):
        # نتحقق إذا كان المستخدم مسجل الدخول وهو "سوبر يوزر"
        return bool(request.user and request.user.is_superuser)
        # 1. عرض جميع المناديب (GET) وإضافة مندوب جديد (POST)


class CourierListCreateAPI(generics.ListCreateAPIView):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer
    permission_classes = [IsSuperUser]   

# 2. عرض، تعديل، وحذف مندوب واحد بناءً على رقم الـ ID
class CourierDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer
    permission_classes = [IsSuperUser]


# ==========================================
# 🛑 الدوال العادية (الطريقة التقليدية - معطلة كمرجع) 🛑
# ==========================================

# @login_required(login_url='login')
# def courier_list(request):
#     couriers = Courier.objects.all()
#     return render(request, 'delivery/courier_list.html', {'couriers': couriers})

# @login_required(login_url='login')
# def courier_create(request):
#     if request.method == 'POST':
#         form = CourierForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('courier_list')
#     else:
#         form = CourierForm()
#     return render(request, 'delivery/courier_register.html', {'form': form})

# @login_required(login_url='login')
# def courier_update(request, id):
#     courier = get_object_or_404(Courier, id=id)
#     if request.method == 'POST':
#         form = CourierForm(request.POST, instance=courier)
#         if form.is_valid():
#             form.save()
#             return redirect('courier_list')
#     else:
#         form = CourierForm(instance=courier)
#     return render(request, 'delivery/courier_form.html', {'form': form})

# @login_required(login_url='login')
# def courier_delete(request, id):
#     courier = get_object_or_404(Courier, id=id)
#     if request.method == 'POST':
#         courier.delete()
#         return redirect('courier_list')
#     return render(request, 'delivery/courier_confirm_delete.html', {'object': courier})