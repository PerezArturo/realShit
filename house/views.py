from rest_framework import permissions, generics
from .serializers import HousePubSerializer
from .models import HousePub


class HousePubList(generics.ListCreateAPIView):
    queryset = HousePub.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = HousePubSerializer


class HousePubDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = HousePub.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = HousePubSerializer
