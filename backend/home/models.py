from django.conf import settings
from django.db import models
class M1(models.Model):
    'Generated Model'
    key = models.ForeignKey("users.User",on_delete=models.CASCADE,related_name="m1_key",)
