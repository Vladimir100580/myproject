from django.core.management.base import BaseCommand
from gb_app4.models import Product


class Command(BaseCommand):
    help = "Detailed output of all orders."

    def handle(self, *args, **kwargs):
        self.stdout.write(f'Список всех товаров:')
        for prod in Product.objects.all():
            self.stdout.write(f'{prod}')
