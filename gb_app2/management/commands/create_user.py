from django.core.management.base import BaseCommand
from gb_app2.models import User
from datetime import date

current_date = date.today()

class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        date = current_date
        user = User(name='Vladimir',
                    email='vovar@example.com',
                    phone_number='+79503423542',
                    password='Istina',
                    address='Severomorsk, Severnaya zastava, h.22',
                    date=date.today(),
                    )
        user.save()
        self.stdout.write(f'{user}')
