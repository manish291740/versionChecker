from django.db import models

# Create your models here.
class checkDataModel(models.Model):

    IpAddress = models.CharField(max_length=20)