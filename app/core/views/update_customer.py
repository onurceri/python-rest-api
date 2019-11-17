from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from core.models.customer_model import Customer
from core.serializers import CustomerSerializer

class UpdateCustomerView(APIView):
    def put(self, request, *args, **kwargs):
        if request.method == 'PUT':
            serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)