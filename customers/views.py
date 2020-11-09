from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from customers.models import Customers
from customers.serializers import CustomerSerializer

@csrf_exempt
def customer(request):

    if request.method == 'GET':
        customers = Customers.objects.all()
        serializer = CustomerSerializer(customers,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)


@csrf_exempt
def customer_detail(request, pk):
    try:
        customer = Customers.objects.get(pk=pk)
    except Customers.DoesNotExist:
        return HttpResponse(status=400)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return  JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CustomerSerializer(customer, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return  JsonResponse(serializer.errors,status=400)

    elif request.method == 'DELETE':
        customer.delete()
        return HttpResponse(status=200)





def home(request):
    return render(request,'customers/test.html')
