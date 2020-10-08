import pytest
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

from house.serializers import HousePubSerializer
from house.models import HousePub


class DummyClient:
    def __init__(self, data):
        self.data = data

    def expected_result(self, user):
        return {
            'id': self.data.get('id', None),
            'title': self.data.get('title', None),
            'description': self.data.get('description', None),
            'price': self.data.get('price', None),
            'currency': self.data.get('currency', None),
            'phone': self.data.get('phone', None),
            'email': self.data.get('email', None),
            'no_Bedroom': self.data.get('no_Bedroom', None),
            'no_Bathroom': self.data.get('no_Bathroom', None),
            'house_Size': self.data.get('house_Size', None),
            'user': user.id,
        }


class TestClientSerializer:
    @pytest.mark.django_db
    def test_all_fields(self):
        user = User.objects.create(username='arturo')

        data = {
            "id": 1,
            "title": "House Test",
            "description": "This is a test",
            "price": 2500,
            "currency": 1,
            "phone": "6641710528",
            "email": "exmaple@mail.com",
            "no_Bedroom": 4,
            "no_Bathroom": 2,
            "house_Size": 15000,
            "user": user
        }

        client = HousePub(**data)
        exp_results = DummyClient(data).expected_result(user)
        results = HousePubSerializer(client).data

        assert results == exp_results

    @pytest.mark.django_db
    def test_required_fields(self):
        user = User.objects.create(username='arturo')

        data = {
            "id": 1,
            "title": "House Test",
            "description": "This is a test",
            "price": 2500,
            "currency": 1,
            "phone": "6641710528",
            "no_Bedroom": 4,
            "no_Bathroom": 2,
            "house_Size": 15000,
            "user": user
        }

        client = HousePub(**data)
        exp_results = DummyClient(data).expected_result(user)
        results = HousePubSerializer(client).data

        assert results == exp_results

    @pytest.mark.django_db
    def test_error_title_fields(self):
        user = User.objects.create(username='arturo')

        incomplete_data = {
            "id": 1,
            "description": "This is a test",
            "price": 2500,
            "currency": 1,
            "phone": "6641710528",
            "no_Bedroom": 4,
            "no_Bathroom": 2,
            "house_Size": 15000,
            "user": user
        }

        serializer = HousePubSerializer(data=incomplete_data)

        with pytest.raises(ValidationError):
            serializer.is_valid(raise_exception=True)
