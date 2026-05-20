from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomerRegistrationForm
from .models import Customer
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    context = {
        'title': 'Home Page',
        'message': 'Welcome to the Customers Application'
    }
    return render(request, 'customers/home.html', context)

def about(request):
    context = {
        'title': 'About Page',
        'description': 'This store application is built using Django.'
    }
    return render(request, 'customers/about.html', context)

def contactus(request):
    context = {
        'title': 'Contact Page',
        'description': 'Developed by Store Manager. E-mail: admin@store.com'
    }
    return render(request, 'customers/contactus.html', context)

@login_required(login_url='login')
def register_customer(request):
   
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():  # التحقق من صحة البيانات
            form.save()      # حفظ البيانات في قاعدة البيانات
            return redirect('customers_home') # إعادة توجيه للصفحة الرئيسية بعد النجاح
    else:
        # إذا كان المستخدم يزور الصفحة لأول مرة (عرض نموذج فارغ)
        form = CustomerRegistrationForm()
        
    return render(request, 'customers/register.html', {'form': form})

@login_required(login_url='login')
def customer_list(request):
    # جلب جميع سجلات العملاء من قاعدة البيانات
    customers = Customer.objects.all()
    return render(request, 'customers/customer_list.html', {'customers': customers})

@login_required(login_url='login')
def customer_update(request, id):
    # جلب العميل المطلوب بناءً على المعرف (ID) أو إظهار خطأ 404 إذا لم يوجد
    customer = get_object_or_404(Customer, id=id)
    
    if request.method == 'POST':
        # تمرير البيانات الجديدة مع الحفاظ على الكائن الأصلي (instance)
        form = CustomerRegistrationForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        # عرض النموذج وبداخله بيانات العميل الحالية
        form = CustomerRegistrationForm(instance=customer)
        
    return render(request, 'customers/register.html', {'form': form})

@login_required(login_url='login')
def customer_delete(request, id):
    customer = get_object_or_404(Customer, id=id)
    
    if request.method == 'POST':
        customer.delete() # تنفيذ أمر الحذف من قاعدة البيانات
        return redirect('customer_list')
        
    return render(request, 'customers/customer_confirm_delete.html', {'customer': customer})

def register_account(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() # حفظ المستخدم وتشفير كلمة المرور تلقائياً
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'customers/register_account.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('customer_list') # التوجه للقائمة بعد الدخول
    else:
        form = AuthenticationForm()
    return render(request, 'customers/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')