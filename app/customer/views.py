from rest_framework.generics import (
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView
)

from core.models import customer_model
from core.models import customer_mailaddress_model
from core.serializers import CustomerSerializer
from core.serializers import MailAddressSerializer


class ListCustomersView(ListAPIView):
    queryset = customer_model.Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDeleteView(DestroyAPIView):
    queryset = customer_model.Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerUpdateView(UpdateAPIView):
    queryset = customer_model.Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetailView(RetrieveAPIView):
    queryset = customer_model.Customer.objects.all()
    serializer_class = CustomerSerializer


class ListCustomersMailAddressesView(ListAPIView):
    queryset = customer_mailaddress_model.CustomerMailAddress.objects.all()
    serializer_class = MailAddressSerializer
