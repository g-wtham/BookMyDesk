from django.db import models
from django.contrib.auth.models import User

class scanHistory(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    barcode_data = models.CharField(max_length=255)