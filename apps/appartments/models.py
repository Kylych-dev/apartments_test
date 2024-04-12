from django.db import models
from apps.accounts.models import CustomUser

status_choices = [
        ('active', 'Активна'),
        ('barter', 'Бартер'),
        ('installment', 'Рассрочка'),
        ('reservation', 'Бронь'),
        ('purchased', 'Куплено'),
    ]

class Apartment(models.Model):
    # Поля для квартиры
    apartment_number = models.CharField(max_length=10, verbose_name="Номер квартиры")
    object_name = models.CharField(max_length=100, verbose_name="Название объекта")
    floor = models.PositiveIntegerField(verbose_name="Этаж")
    square_meters = models.PositiveIntegerField(verbose_name="Квадратные метры")
    status = models.CharField(max_length=20, choices=status_choices, default='active', verbose_name="Статус")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    client = models.ForeignKey(
        CustomUser, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        verbose_name="Клиент"
    )
    purchase_date = models.DateField(null=True, blank=True, verbose_name="Дата покупки")
    reservation_until = models.DateField(null=True, blank=True, verbose_name="Бронь до")

    class Meta:
        verbose_name = "Квартира"
        verbose_name_plural = "Квартиры"

    def __str__(self):
        return self.apartment_number