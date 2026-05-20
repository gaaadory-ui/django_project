from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='customers_home'),
    path('about/', views.about, name='customers_about'),
    path('contactus/', views.contactus, name='contactus'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register_account/', views.register_account, name='register_account'),
    
    # 🌟 الروابط الجديدة باستخدام CBV
    path('list/', views.CustomerListView.as_view(), name='customer_list'),
    path('register/', views.CustomerCreateView.as_view(), name='register_customer'),
    # ⚠️ مهم جداً: الـ CBV تستخدم <int:pk> وليس <int:id> للبحث عن السجل [cite: 1132, 1133]
    path('list/<int:pk>/update/', views.CustomerUpdateView.as_view(), name='customer_update'),
    path('list/<int:id>/delete/', views.customer_delete, name='customer_delete'), # (أبقينا الحذف بالدالة القديمة كمثال)
]