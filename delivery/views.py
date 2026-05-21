from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Courier
from .forms import CourierForm

# 1. عرض قائمة المناديب
@login_required(login_url='login')
def courier_list(request):
    couriers = Courier.objects.all()
    return render(request, 'delivery/courier_list.html', {'couriers': couriers})

# 2. إضافة مندوب جديد
@login_required(login_url='login')
def courier_create(request):
    if request.method == 'POST':
        form = CourierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courier_list')
    else:
        form = CourierForm()
    return render(request, 'delivery/courier_register.html.html', {'form': form})

# 3. تعديل بيانات مندوب
@login_required(login_url='login')
def courier_update(request, id):
    courier = get_object_or_404(Courier, id=id)
    if request.method == 'POST':
        form = CourierForm(request.POST, instance=courier)
        if form.is_valid():
            form.save()
            return redirect('courier_list')
    else:
        form = CourierForm(instance=courier)
    return render(request, 'delivery/courier_form.html', {'form': form})

# 4. حذف مندوب
@login_required(login_url='login')
def courier_delete(request, id):
    courier = get_object_or_404(Courier, id=id)
    if request.method == 'POST':
        courier.delete()
        return redirect('courier_list')
    # مررنا المتغير باسم 'object' ليتطابق مع ما كتبناه في القالب سابقاً
    return render(request, 'delivery/courier_confirm_delete.html', {'object': courier})