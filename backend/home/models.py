from django.conf import settings
from django.db import models
class M1(models.Model):
    'Generated Model'
    key = models.ForeignKey("users.User",on_delete=models.CASCADE,related_name="m1_key",)
    int1 = models.BooleanField(null=True,blank=True,)
    data1 = models.DateField(auto_now=True,null=True,blank=True,)
    time1 = models.DateTimeField(null=True,blank=True,)
