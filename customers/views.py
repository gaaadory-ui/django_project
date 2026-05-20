from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomerRegistrationForm
from .models import Customer
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

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
# بدلاً من 4 أسطر، سطرين فقط!
class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'customers/customer_list.html'
    context_object_name = 'customers' # حتى لا نغير اسم المتغير في ملف HTML

class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    template_name = 'customers/register.html'
    fields = ['first_name', 'last_name', 'email', 'age', 'department'] # الحقول التي ستظهر للمستخدم
    success_url = reverse_lazy('customer_list') # أين يذهب بعد النجاح؟
    login_url = 'login' # أين يذهب إذا لم يكن مسجلاً للدخول؟

class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    template_name = 'customers/register.html'
    fields = ['first_name', 'last_name', 'email', 'age', 'department']
    success_url = reverse_lazy('customer_list')
    login_url = 'login'

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