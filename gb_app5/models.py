from django.db import models


class User(models.Model):
    name = models.CharField(max_length=128, blank=False)
    email = models.EmailField(default='')
    phone_number = models.CharField(max_length=16, default='')
    password = models.CharField(max_length=64, default='23571113')
    address = models.CharField(max_length=128, default='', blank=True)
    date = models.DateField()

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default='', blank=True)  # blank=True поле не обязательное для заполнения
    price = models.DecimalField(default=999999.99, max_digits=8, decimal_places=2)  # DecField т.к. Float - не точен
    quantity = models.PositiveSmallIntegerField(default=0)  # малое (до 2^15), положительное, целое число
    date_added = models.DateTimeField(auto_now_add=True)  # автозаполнение даты
    rating = models.DecimalField(default=4.0, max_digits=2, decimal_places=1)

    def __str__(self):
        return f'id: {self.pk}, name: {self.name}, price: {self.price}'

    def get_product(self):
        return f'{self.name}, {self.date_added}, {self.description[:20]}...'


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order_ID: {self.pk}'
