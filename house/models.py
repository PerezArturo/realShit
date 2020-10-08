from django.contrib.auth.models import User
from django.db import models


class HousePub(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    currency = models.CharField(choices=[(1, 'MX'), (2, 'USD')], max_length=1)
    phone = models.CharField(max_length=10)
    email = models.EmailField(null=True, blank=True)
    no_Bedroom = models.IntegerField()
    no_Bathroom = models.IntegerField()
    house_Size = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
