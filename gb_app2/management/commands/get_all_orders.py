from django.core.management.base import BaseCommand
from gb_app2.models import Order, Product


class Command(BaseCommand):
    help = "Detailed output of all orders."

    def handle(self, *args, **kwargs):
        for order in Order.objects.all():
            self.stdout.write(f'{order}')
            prods = order.products.all()  # c атрибутом many-to-many работаем, как с объектом (all(),get(),filter()...)
            self.stdout.write(f'Товары входящие в заказ:')
            for p in prods:
                self.stdout.write(f'{p}')
            self.stdout.write(f'\n')
