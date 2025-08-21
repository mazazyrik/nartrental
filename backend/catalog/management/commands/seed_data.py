from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from catalog.models import Product
import os


class Command(BaseCommand):
    help = 'Заполняет базу демо-товарами'

    def handle(self, *args, **options):
        products_data = [
            {
                'title': 'Светобаза - Mercedes Atego 2011 года',
                'slug': 'svetobaza-mercedes-atego',
                'description': 'Профессиональная светобаза на базе Mercedes Atego для съемок и мероприятий',
                'price': 9900000,
            },
            {
                'title': 'Генератор Honda EU30i',
                'slug': 'generator-honda-eu30i',
                'description': 'Бензиновый генератор мощностью 3 кВт, идеален для выездных съемок',
                'price': 1500000,
            },
            {
                'title': 'Светильник ARRI L7-C',
                'slug': 'svetilnik-arri-l7-c',
                'description': 'Светодиодный светильник с переменной цветовой температурой',
                'price': 4500000,
            },
            {
                'title': 'Камера Sony FX6',
                'slug': 'kamera-sony-fx6',
                'description': 'Кинокамера с полнокадровым сенсором и профессиональными функциями',
                'price': 12000000,
            },
            {
                'title': 'Микрофон Sennheiser MKH 416',
                'slug': 'mikrofon-sennheiser-mkh416',
                'description': 'Направленный конденсаторный микрофон для профессиональной записи',
                'price': 1800000,
            }
        ]

        for product_data in products_data:
            product, created = Product.objects.get_or_create(
                slug=product_data['slug'],
                defaults=product_data
            )

            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Создан товар: {product.title}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f'Товар уже существует: {product.title}')
                )

        self.stdout.write(
            self.style.SUCCESS('Демо-данные успешно добавлены!')
        )
