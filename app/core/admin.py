from core.models import customer_model
from core.models import customer_mailaddress_model
from core.models import customer_type_model
from core.models import customer_type_map_model

from django.contrib import admin

admin.site.register(customer_model.Customer)
admin.site.register(customer_mailaddress_model.CustomerMailAddress)
admin.site.register(customer_type_model.CustomerType)
admin.site.register(customer_type_map_model.CustomerTypeMap)
