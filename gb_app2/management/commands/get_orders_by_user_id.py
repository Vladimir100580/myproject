from django.core.management.base import BaseCommand
from gb_app2.models import Order, Product


class Command(BaseCommand):
    help = "Get all orders by user id."
    # Пример ввода: get_orders_by_user_id 7

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        for order in Order.objects.filter(customer=pk):
            self.stdout.write(f'{order}')
            prods = order.products.all()
            self.stdout.write(f'Товары входящие в заказ:')
            for p in prods:
                self.stdout.write(f'{p}')
            self.stdout.write(f'\n')

