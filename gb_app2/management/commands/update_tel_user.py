from django.core.management.base import BaseCommand
from gb_app2.models import User, Product, Order


class Command(BaseCommand):
    class Command(BaseCommand):
        help = "Update user telephone by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')
        parser.add_argument('tel', type=str, help='User telephone')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        tel = kwargs.get('tel')
        user = User.objects.filter(pk=pk).first()
        user.phone_number = tel
        user.save()
        self.stdout.write(f'{user}')
