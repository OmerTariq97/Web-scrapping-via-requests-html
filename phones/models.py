from django.db import models

# Create your models here.

class mobile(models.Model):
    name = models.CharField(max_length = 200)
    price = models.CharField(max_length = 50, blank = True)
    status = models.CharField(max_length = 50)
    camera = models.CharField(max_length = 250)
    processor = models.CharField(max_length = 250)
    storage = models.CharField(max_length = 250)
    battery = models.CharField(max_length = 150)
    ram = models.CharField(max_length = 200)
    display = models.CharField(max_length = 250)