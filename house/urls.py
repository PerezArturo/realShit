from django.urls import path
from .views import HousePubList, HousePubDetails

urlpatterns = [
    path('', HousePubList.as_view()),
    path('<int:pk>/', HousePubDetails.as_view()),
]
