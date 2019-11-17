from django.urls import re_path
from core.views import (
    queryable_customer_view,
    customer_view,
)


urlpatterns = [
    re_path(
        r'^api/v1/customers/(?P<pk>[0-9]+)$',
        queryable_customer_view.QueryableCustomerView.as_view(),
        name = "queryable-customer-api"),
    re_path(
        r'^api/v1/customers/$',
        customer_view.CustomerView.as_view(),
        name = "customer-api"),
        

    # re_path(
    #    r'^api/v1/customers/(?P<pk>[0-9]+)$',
    #    customer_view.CustomerView.get_delete_update_customer,
    #    name='get_delete_update_customer'
    # ),
    # re_path(
    #    r'^api/v1/customers/$',
    #    customer_view.CustomerView.get_post_customers,
    #    name='get_post_customers'
    # )
]
