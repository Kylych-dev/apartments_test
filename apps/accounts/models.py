from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin

ROLE_CHOICES = [
    ('manager', 'Manager'),
    ('client', 'Client')
]


class CustomUser(AbstractUser, PermissionsMixin):
    role = models.CharField(max_length=15, choices=ROLE_CHOICES)
    

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


    class Meta:
        verbose_name = ("user")
        verbose_name_plural = ("users")


    def __str__(self):
        return f'{self.username} role: {self.role}'


class Client(models.Model):
    first_name = models.CharField(max_length=30, blank=True, verbose_name="First Name")
    last_name = models.CharField(max_length=30, blank=True, verbose_name="Last Name")
    phone_number = models.CharField(max_length=15, verbose_name="Phone Number")
    contract_number = models.CharField(max_length=100)
    user = models.OneToOneField(
        CustomUser, 
        on_delete=models.CASCADE, 
        primary_key=True
        )

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"    

    def __str__(self):
        return self.user.username


class Manager(models.Model):
    first_name = models.CharField(max_length=30, blank=True, verbose_name="First Name")
    last_name = models.CharField(max_length=30, blank=True, verbose_name="Last Name")
    phone_number = models.CharField(max_length=15, verbose_name="Phone Number")
    email = models.EmailField(unique=True, max_length=60, verbose_name="Email")
    successful_deals = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(
        CustomUser, 
        on_delete=models.CASCADE, 
        primary_key=True
        )        


    class Meta:
        verbose_name = "manager"
        verbose_name_plural = "managers"

    def __str__(self):
        return self.user.username