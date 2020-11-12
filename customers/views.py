from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, mixins, generics
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from customers.models import Customers
from customers.serializers import CustomerSerializer


class CustomersApi(APIView):
    def get(self, request):
        customers = Customers.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerDetails(APIView):
    def get_object(self, pk):
        try:
            return Customers.objects.get(pk=pk)
        except Customers.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        data = self.get_object(pk)
        serializer = CustomerSerializer(data)
        return Response(serializer.data)

    def put(self, request, pk):
        data = self.get_object(pk)
        serializer = CustomerSerializer(data, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        data = self.get_object(pk)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomerListGenericApi(mixins.RetrieveModelMixin,
                             mixins.ListModelMixin,
                             mixins.CreateModelMixin,
                             mixins.UpdateModelMixin,
                             mixins.DestroyModelMixin,
                             generics.GenericAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class CustomerDetailGenericApi(mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin,generics.GenericAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'id'

    def get(self, request, id = None):

        if id:
            return self.retrieve(request)
        else:
            return  self.list(request)

    def delete(self, request, id):
        return self.destroy(request, id)

    def put(self, request, id):
        return self.update(request, id)


@api_view(['GET', 'POST'])
def customer(request):
    if request.method == 'GET':
        customers = Customers.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def customer_detail(request, pk):
    try:
        customer = Customers.objects.get(pk=pk)
    except Customers.DoesNotExist:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        customer.delete()
        return HttpResponse(status=status.HTTP_200_OK)


def home(request):
    return render(request, 'customers/test.html')
