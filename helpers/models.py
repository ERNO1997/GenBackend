from django.db import models


class TrackingModel(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        abstract = True
        ordering = ('-created_at',)
