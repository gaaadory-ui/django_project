#from django.urls import path
#from . import views
#
#urlpatterns = [
#    # مسار القائمة
#    path('', views.courier_list, name='courier_list'),
#    
#    # مسار الإضافة
#    path('register/', views.courier_create, name='courier_register'),
#    
#    # مسارات التعديل والحذف
#    path('<int:id>/update/', views.courier_update, name='courier_update'),
#    path('<int:id>/delete/', views.courier_delete, name='courier_delete'),
#]
from django.urls import path
from . import views

urlpatterns = [
    # مسار القائمة
    path('', views.CourierListView.as_view(), name='courier_list'),
    
    # مسار الإضافة
    path('register/', views.CourierCreateView.as_view(), name='courier_register'),
    
    # مسارات التعديل والحذف (✅ تم تغيير id إلى pk)
    path('<int:pk>/update/', views.CourierUpdateView.as_view(), name='courier_update'),
    path('<int:pk>/delete/', views.CourierDeleteView.as_view(), name='courier_delete'),
]