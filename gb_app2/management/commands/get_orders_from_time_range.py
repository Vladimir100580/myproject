from django.core.management.base import BaseCommand
from gb_app2.models import Order
from datetime import datetime

class Command(BaseCommand):
    class Command(BaseCommand):
        help = "Get all orders located in the specified time period. Date format: %d.%m.%y"
        # пример ввода: python manage.py get_orders_from_time_range 01.01.20 31.12.22

    def add_arguments(self, parser):
        parser.add_argument('be', type=str, help='bottom edge')
        parser.add_argument('te', type=str, help='top edge')

    def handle(self, *args, **kwargs):
        be = datetime.strptime(kwargs.get('be'), '%d.%m.%y').date()
        te = datetime.strptime(kwargs.get('te'), '%d.%m.%y').date()

        for order in Order.objects.filter(date_ordered__gte=be, date_ordered__lte=te):
            self.stdout.write(f'{order}')
