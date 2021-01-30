from django.db import models
from django.contrib.auth.models import AbstractUser

VACCINATION_CHOICES = [
    ('NV', 'Not Vaccinated'),
    ('SL', 'On Short List'),
    ('V', 'Vaccinated'),
]


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(primary_key=True)
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=32)
    vaccination_info = models.CharField(choices=VACCINATION_CHOICES, max_length=2)


class Store(models.Model):
    # pk is already defined and is the primary key for the store
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=32)
    safety_policy = models.TextField()
    location = models.CharField(max_length=256)
    store_hours = models.TextField()
    

class Code(models.Model):
    uuid = models.UUIDField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
        
class Favourites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
