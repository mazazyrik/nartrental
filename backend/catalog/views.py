from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.conf import settings
import requests
import hmac
import hashlib
import json
from .models import Product, Order
from .serializers import (
    ProductListSerializer,
    ProductDetailSerializer,
    OrderCreateSerializer
)


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.filter(is_active=True)
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductDetailSerializer
        return ProductListSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        section = self.request.query_params.get('section')
        if section:
            qs = qs.filter(section=section)
        return qs


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()

        self.notify_bot(order)

        return Response(
            {'message': 'Заявка успешно создана'},
            status=status.HTTP_201_CREATED
        )

    def notify_bot(self, order):
        try:
            payload = {
                'order_id': order.id,
                'product': order.product.title,
                'section': order.product.section,
                'price': order.price_locked,
                'customer_name': order.customer_name,
                'customer_phone': order.customer_phone,
                'comment': order.comment,
                'created_at': order.created_at.isoformat()
            }

            signature = hmac.new(
                settings.NOTIFY_SECRET.encode(),
                json.dumps(payload, separators=(',', ':')).encode(),
                hashlib.sha256
            ).hexdigest()

            headers = {'X-Signature': signature}

            requests.post(
                settings.BOT_NOTIFY_URL,
                json=payload,
                headers=headers,
                timeout=5
            )
        except Exception as e:
            print(f'Ошибка уведомления бота: {e}')
