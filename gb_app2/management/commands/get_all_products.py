from django.core.management.base import BaseCommand
from gb_app2.models import Product


class Command(BaseCommand):
    help = "Get all products."

    def handle(self, *args, **kwargs):
        users = Product.objects.all()
        for user in users:
            self.stdout.write(f'{user}')


