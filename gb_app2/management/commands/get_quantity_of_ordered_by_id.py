from django.core.management.base import BaseCommand
from gb_app2.models import Order, Product


class Command(BaseCommand):
    help = "Get the quantity of ordered goods by ID."
    # python manage.py get_quantity_of_ordered_by_id 7

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        count = 0
        pk = kwargs.get('pk')
        for order in Order.objects.all():
            prods = order.products.filter(id=pk)
            count += len(prods)
        self.stdout.write(f'Заказано товаров с ID_{pk}: {count}')

