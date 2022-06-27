from django.db import models
from helpers.models import TrackingModel
from authentication.models import User


class License(TrackingModel):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)
    duration = models.IntegerField()
    readable_duration = models.CharField(max_length=16)
    amount_of_children = models.IntegerField()
    parent_license_id = models.IntegerField(null=True)
    is_active = models.BooleanField(default=False)
    price = models.FloatField()

    class Meta:
        db_table = 'license'


class Payment(TrackingModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    license = models.ForeignKey(License, on_delete=models.CASCADE)
    verified_pay = models.BooleanField(default=False)

    class Meta:
        db_table = 'payment'
