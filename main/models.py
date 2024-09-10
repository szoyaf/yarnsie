from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    rating = models.FloatField(null=True, blank=True)
    stock = models.IntegerField()
    # image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name
