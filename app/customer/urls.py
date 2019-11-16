from django.urls import re_path
from core.views import (
    customer_view
)


urlpatterns = [
    re_path(
        r'^api/v1/customers/(?P<pk>[0-9]+)$',
        customer_view.get_delete_update_customer,
        name='get_delete_update_customer'
    ),
    re_path(
        r'^api/v1/customers/$',
        customer_view.get_post_customers,
        name='get_post_customers'
    )
]
