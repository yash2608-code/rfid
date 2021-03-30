from django.db import models

# Create your models here.
class Admin(models.Model):
    Card_id = models.CharField(max_length=50)