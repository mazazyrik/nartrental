from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Product


class OrderAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.product = Product.objects.create(
            title='Тестовый товар',
            slug='test-product',
            description='Описание тестового товара',
            price=1000000,
            is_active=True
        )

    def test_create_order_valid(self):
        url = reverse('order-list')
        data = {
            'product': self.product.id,
            'customer_name': 'Иван Иванов',
            'customer_phone': '+79991234567',
            'comment': 'Тестовый комментарий'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'Заявка успешно создана')

    def test_create_order_invalid_missing_fields(self):
        url = reverse('order-list')
        data = {
            'product': self.product.id,
            'customer_name': '',
            'customer_phone': '+79991234567'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
