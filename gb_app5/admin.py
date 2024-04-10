from django.contrib import admin
from .models import User, Product, Order
import random


# для массовых операций
@admin.action(description="Задать случайные значения по количеству")  # Для эксперимента
def rand_quantity(modeladmin, request, queryset):
    queryset.update(quantity=random.randint(1, 100))


@admin.action(description="Сброс всех количеств на 0")  # не забыть добавить в action в ProductAdmin
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):  # Не забываем добавить в регистрацию
    """Список продуктов."""
    list_display = ['name', 'price', 'quantity', 'rating']
    ordering = ['price', '-quantity']  # сортировка по приоритету от порядка перечисления
    list_filter = ['date_added', 'price']  # фильтр
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description) '  # подсказка для search_fields
    actions = [rand_quantity, reset_quantity]

    """Отдельный продукт ."""
    fields = ['name', 'description', 'category', 'date_added', 'rating']  # не дружит с fieldsets
    readonly_fields = ['date_added', 'rating']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'total_price', 'date_ordered']
    ordering = ['-total_price']

    readonly_fields = ['customer', 'date_ordered', 'total_price']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['customer'],
            },
        ),
        (
            'Информация о заказе',
            {
                'classes': ['collapse'],
                'description': 'Сведения о заказанных товарах и стоимости',
                'fields': ['products', 'total_price'],
            },
        ),
        (
            'Дата и время заказа',
            {
                'fields': ['date_ordered'],
            }
        ),
    ]
# при таком подходе date_ordered должно быть обязательно указано в readonly_fields

admin.site.register(User)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
