from django.urls import path
from .views import (
    ListCustomersView,
    CustomerDeleteView,
    CustomerUpdateView,
    CustomerDetailView,
    ListCustomersMailAddressesView
)


urlpatterns = [
    path('customers/', ListCustomersView.as_view(), name="list"),
    path('customer/<int:pk>/', CustomerDetailView.as_view(), "detail"),
    path('customer/edit/<int:pk>', CustomerUpdateView.as_view(), "update"),
    path('customer/delete/<int:pk>', CustomerDeleteView.as_view(), "delete"),

    path('customermailaddresses/', ListCustomersMailAddressesView.as_view(),
         name="customers-mail-addresses-all"),
]
