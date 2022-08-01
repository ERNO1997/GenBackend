from rest_framework import serializers
from licenses.models import License, Payment


class LicenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = License
        fields = ('id', 'name', 'description', 'duration', 'readable_duration', 'amount_of_children', 'price')


class PaymentSerializer(serializers.ModelSerializer):
    license = LicenseSerializer()

    class Meta:
        model = Payment
        fields = ('license', 'verified_pay', 'expire_date')
        read_only_fields = ('expire_date', )
