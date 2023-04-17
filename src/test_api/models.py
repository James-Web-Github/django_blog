from django.db import models

# Create your models here.
class test_api1(models.Model):

    api_name = models.CharField(max_length=10)
    