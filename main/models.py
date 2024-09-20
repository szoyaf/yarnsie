from django.db import models
from django.contrib.auth.models import User
import uuid

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    rating = models.FloatField(null=True, blank=True)
    stock = models.IntegerField()
    # image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name
