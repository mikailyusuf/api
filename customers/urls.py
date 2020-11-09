from django.urls import path

from customers import views

urlpatterns = [
    path('',views.home),
    path('customers',views.customer),
    path('details/<int:pk>/',views.customer_detail),
]