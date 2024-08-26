from django.db import models

# Create your models here.

class People(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    phone = models.CharField(max_length=20)
    birth = models.DateField()
    member_rccg = models.CharField(max_length=3)
    whatsapp_no = models.CharField(max_length=20)
    referee = models.TextField()
    attended_prev = models.CharField(max_length=3)
    suggestions = models.TextField()
