from django.contrib.auth import login
from django.http import Http404
from rest_framework import status, permissions
from rest_framework.authtoken.admin import User
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

from customers.models import Customers
from customers.serializers import CustomerSerializer, UserSerializer


class Login(APIView):
    permission_classes = (permissions.AllowAny)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response({'message': 'welcome'}, status=status.HTTP_200_OK)


class CreateUser(APIView):

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data,many=True)
        if serializer.is_valid():
            user = serializer.save()
            print("User is Valid"+str(user))
            #
            # if user:
            #     Customers.objects.create(user=user)
            #
            #     token = Token.objects.create(user=user)
            #     json = serializer.data
            #     # json['token'] = token.key
            #     # json['customer'] = customer
            #     json = user.customers_set.all()
            return Response({'message':'Successfully Created User'}, status=status.HTTP_201_CREATED)

            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        print('invalid user')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


class GetUser(APIView):

    def get_object(self, pk):
        try:
            user = User.objects.get(id=pk)
            return user.customers_set.all()
        except User.DOESNotExist:
            raise Http404

    def get(self, request, pk):
        data = self.get_object(pk)
        serializer = CustomerSerializer(data)
        return Response(serializer.data)


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
