from rest_framework import serializers
from .models import HousePub


class HousePubSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousePub
        fields = ('id', 'title', 'description', 'price', 'currency', 'phone', 'email', 'no_Bedroom', 'no_Bathroom',
                  'house_Size', 'user')
