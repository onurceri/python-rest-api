from core.models import (
    customer_model,
    customer_mailaddress_model,
    customer_type_model,
    customer_type_map_model,
)

from rest_framework.serializers import (
    ModelSerializer,
    RelatedField
)


class MailAddressSerializer(ModelSerializer):
    class Meta:
        model = customer_mailaddress_model.CustomerMailAddress
        fields = [
            'customer_id',
            'mail_address', ]


class CustomerMailAddressSerializer(RelatedField):
    def to_representation(self, value):
        mail_address = value.mail_address
        return mail_address


class CustomerSerializer(ModelSerializer):
    mail_addresses = CustomerMailAddressSerializer(
        many=True, read_only=True)

    class Meta:
        model = customer_model.Customer
        fields = ['name', 'mail_addresses']
