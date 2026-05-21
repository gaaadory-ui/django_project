from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.CourierListView.as_view(), name='courier_list'),
    path('<int:pk>/update/', views.CourierUpdateView.as_view(), name='courier_update'),
    path('<int:pk>/delete/', views.CourierDeleteView.as_view(), name='courier_delete'),
]