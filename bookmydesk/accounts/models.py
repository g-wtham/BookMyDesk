from django.db import models
from django.contrib.auth.models import User

class scanHistory(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    barcode_data = models.CharField(max_length=255)
    scanned_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.barcode_data}"