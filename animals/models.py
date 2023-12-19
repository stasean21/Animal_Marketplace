from django.db import models
from django.contrib.auth.models import User


class Animal(models.Model):
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='animal_images/', blank=True, null=True)
    city = models.CharField(max_length=100, default='Unknown')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name