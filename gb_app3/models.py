from django.db import models


class User(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    phone_number = models.CharField(max_length=16)
    password = models.CharField(max_length=64)
    address = models.CharField(max_length=128)
    date = models.DateField()

    def __str__(self):
        return f'ID: {self.pk}, username: {self.name}, phone number: {self.phone_number}, date: {self.date}'


class Product(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    date_added = models.DateField()

    def __str__(self):
        return f'id: {self.pk}, name: {self.name}, price: {self.price}'

    def get_product(self):
        return f'{self.name}, {self.date_added}, {self.description[:20]}...'


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    date_ordered = models.DateField()

    def __str__(self):
        return f'Order_ID: {self.pk},' \
               f' Customer_ID: {self.customer.pk},' \
               f' Total_price: {self.total_price},' \
               f' Date_orders: {self.date_ordered}'
