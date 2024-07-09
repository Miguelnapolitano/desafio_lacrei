import datetime
from urllib.parse import urlencode
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Visit
from professional.models import Professional

class TestVisitViewSet(APITestCase):

    def create_profesisonal(self):
        professional_data = {
                "first_name": "Miguel",
                "last_name": "Napolitano",
                "username": "Miguel2",
                "email": "miguel.napolitano2@mail.com",
                "password": "123",
                "profession": "Doctor",
            }
        
        new_prof = Professional.objects.create(**professional_data)
        return new_prof

    def test_get_by_professional_success(self):
        
        prof_uuid = self.create_profesisonal()
        visit_data = [
            {"professional": prof_uuid, "date": "2024-07-09 00:00:00"},
            {"professional": prof_uuid, "date": "2024-07-10 00:00:00"},
            {"professional": prof_uuid, "date": "2024-07-11 00:00:00"},
        ]
        Visit.objects.bulk_create([Visit(**data) for data in visit_data])

        url = f"/api/visit/get_by_professional?professional={str(prof_uuid.id)}"
        response = self.client.get(url, {}, follow=True)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_data = {
                        'schedule': [{
                            'date': datetime.datetime(2024, 7, 9, 0, 0, tzinfo = datetime.timezone.utc)
                        }, {
                            'date': datetime.datetime(2024, 7, 10, 0, 0, tzinfo = datetime.timezone.utc)
                        }, {
                            'date': datetime.datetime(2024, 7, 11, 0, 0, tzinfo = datetime.timezone.utc)
                        }]
                        }
        
        self.assertEqual(response.data, expected_data)

    def test_get_by_professional_without_param(self):
        url = f"/api/visit/get_by_professional"

        response = self.client.get(url, {}, follow=True)

        self.assertEqual(response.data, {"detail": "Url parameter prof is required."})
