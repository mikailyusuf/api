from django.urls import path

from customers import views
from customers.views import Login, CustomerDetails, CustomersApi, GetUser, CreateUser

urlpatterns = [
    # path('', views.home),
    path('customers', CustomersApi.as_view()),
    path('details/<int:pk>/', CustomerDetails.as_view()),
    path('create', CreateUser.as_view(), name='create'),
    path('login/', Login.as_view(), name='login'),
    path('user/<int:pk>/', GetUser.as_view(), name='user'),

]
