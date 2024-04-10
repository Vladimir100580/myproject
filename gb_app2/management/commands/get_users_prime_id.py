from django.core.management.base import BaseCommand
from gb_app2.models import User, Product, Order


class Command(BaseCommand):
    help = "Get all users whose id number is a prime number."

    def handle(self, *args, **kwargs):
        for i in range(1, User.objects.latest('id').pk + 10):
            if prime_number(i):
                user = User.objects.filter(pk=i).first()  # filter лучше тем, что дает None (если id нет в БД)
                if user:
                    self.stdout.write(f'{user}')



def prime_number(n: int):
    """ Метод проверяет простое ли переданное в него число """
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
