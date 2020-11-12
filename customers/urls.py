from django.urls import path

from customers import views
from customers.views import CustomersApi, CustomerDetails, CustomerDetailGenericApi, CustomerListGenericApi

urlpatterns = [
    path('',views.home),
    path('customers',CustomerListGenericApi.as_view()),
    path('details/<int:id>/',CustomerDetailGenericApi.as_view()),
]