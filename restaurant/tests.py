from restaurant.models import TableBooking , Order , Menu , Table
from django.urls import include, path, reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.test import TestCase
from .serializers import OrderSerializer


class TestView(APITestCase):
    def test_get_menu(self):
        url = reverse('get_menu')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TestView1(APITestCase):
    def test_get_tabledetails(self):
        url = reverse('table-details')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TestView2(APITestCase):
    def test_order(self):
        obj= Menu()
        obj1= TableBooking()
        obj.items='chicken'
        obj.price=50
        obj.time_to_prepare=10
        obj.save(self)
        obj1.name='Akash'
        obj1.people=4
        obj1.save(self)
        url = reverse('book-order')
        data = {'items': [1],
                'table_no':1}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TestView3(APITestCase):
    def test_tabledetails(self):
        obj = Table()
        obj.total_table = 20
        obj.available_table=14
        obj.booked_table = 6
        obj.save(self)
        url = reverse('book-table')
        data = {'name': "Akash",
                'people':4}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
