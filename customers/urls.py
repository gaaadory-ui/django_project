from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='customers_home'),
    path('about/', views.about, name='customers_about'),
    path('contactus/', views.contactus, name='contactus'),
    path('register/', views.register_customer, name='register_customer'),
    path('customers/', views.customer_list, name='customer_list'),
    path('customer/edit/<int:id>/', views.customer_update, name='customer_update'),
    path('customer/delete/<int:id>/', views.customer_delete, name='customer_delete'),
    path('register_account/', views.register_account, name='register_account'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]