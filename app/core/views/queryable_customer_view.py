from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from core.models.customer_model import Customer
from core.serializers import CustomerSerializer


class QueryableCustomerView(APIView):
    
    def __get_customer(self, kwargs):
        if kwargs is not None:
            arg = kwargs.get('pk')
            if arg is not None:
                try:
                    customer = Customer.objects.get(pk=arg)
                    return customer
                except Customer.DoesNotExist:
                    raise

    def get(self, request, *args, **kwargs):
        try:
            customer = self.__get_customer(kwargs)
            if customer is not None:
                # get details of a single customer
                serializer = CustomerSerializer(customer)
                return Response(serializer.data)
        except Customer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        try:
            customer = self.__get_customer(kwargs)
            if customer is not None:
                # delete a single customer
                customer.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
        except Customer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            customer = self.__get_customer(kwargs)
            if customer is not None:
               serializer = CustomerSerializer(customer, data=request.data)
            if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Customer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)