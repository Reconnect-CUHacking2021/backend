from django.db import models
from django.contrib.auth.models import AbstractUser

VACCINATION_CHOICES = [
    ('NV', 'Not Vaccinated'),
    ('V', 'Vaccinated'),
]

class Store(models.Model):
    # pk is already defined and is the primary key for the store
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=32)
    safety_policy = models.TextField()
    location = models.CharField(max_length=256)
    store_hours = models.TextField()
    
class Code(models.Model):
    uuid = models.UUIDField(primary_key=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='store')
    in_store = models.BooleanField(default=False)

class User(AbstractUser):
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=32)
    vaccination_info = models.CharField(choices=VACCINATION_CHOICES, max_length=2)
    favorites = models.ManyToManyField(Store)
    code = models.OneToOneField(Code, on_delete=models.CASCADE, null=True)

