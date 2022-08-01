from django.db import models
from helpers.models import TrackingModel
from authentication.models import User
from datetime import datetime, timedelta
import pytz


class License(TrackingModel):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)
    duration = models.IntegerField()
    readable_duration = models.CharField(max_length=16)
    amount_of_children = models.IntegerField()
    parent_license_id = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=False, blank=False)
    price = models.FloatField()

    class Meta:
        db_table = 'license'

    def __str__(self):
        return self.name + ' (' + self.readable_duration + ')'


class Payment(TrackingModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    license = models.ForeignKey(License, on_delete=models.CASCADE)
    verified_pay = models.BooleanField(default=False)

    class Meta:
        db_table = 'payment'

    @property
    def expire_date(self):
        return self.updated_at + timedelta(days=self.license.duration)

    def has_expired(self):
        utc = pytz.UTC
        return not self.verified_pay or utc.localize(datetime.now()) > self.expire_date

    def __str__(self):
        if self.verified_pay:
            return 'OK {} -> {} ({})'.format(self.user.email, self.license.name, self.updated_at)
        else:
            return 'PENDING {} -> {} ({})'.format(self.user.email, self.license.name, self.created_at)
