from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from core.models.customer_model import Customer
from core.serializers import CustomerSerializer


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_customer(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single customer
    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    # update details of a single customer
    if request.method == 'PUT':
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete a single customer
    if request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def get_post_customers(request):
    # get all customers
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
    # insert a new record for a customer
    if request.method == 'POST':
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
