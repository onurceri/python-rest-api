from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from core.models.customer_model import Customer
from core.serializers import CustomerSerializer


class CustomerView(APIView):
    def get(self, request, *args, **kwargs):
        # get all customers
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        # insert a new record for a customer
        data = {
            'first_name': request.data.get('first_name'),
            'age': int(request.data.get('age')),
            'last_name': request.data.get('last_name'),
            'mail_address': request.data.get('mail_address')
        }
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
