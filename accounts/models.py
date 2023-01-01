import json

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.
from books.models import Book


class CustomUserManager(BaseUserManager):
    def get_manager_queryset(self):
        return super(CustomUserManager, self).get_queryset().filter(is_manager=True)

    def get_user_queryset(self):
        return super(CustomUserManager, self).get_queryset().filter(is_manager=False)

    def get_queryset(self):
        return super(CustomUserManager, self).get_queryset().all()


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=250, db_index=True, null=True)
    is_manager = models.BooleanField(default=False)
    obtained = models.ManyToManyField('books.Book', related_name="obtained_books", blank=True)
    mass_fundraise = models.ManyToManyField('books.Book', related_name="fundraised_books", blank=True)
    user_manager = CustomUserManager()

    def __str__(self):
        return self.username


class UserAddress(models.Model):
    default = models.BooleanField(default=False)
    name = models.CharField(max_length=250, db_index=True)
    province = models.CharField(max_length=250, db_index=True)
    district = models.CharField(max_length=250, db_index=True)
    street = models.CharField(max_length=250, db_index=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def to_json(self):
        return AddressSerializer(self).data


class Report(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField()


class Favorites(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    books = models.ForeignKey(Book, on_delete=models.CASCADE)


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_owner = models.IntegerField(11)


class Orders(models.Model):
    receiver = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    address = models.TextField()


class Sales(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    sender = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    shipping_key = models.CharField(max_length=11)


class OrderDetail(models.Model):
    sale = models.ForeignKey(Sales, on_delete=models.CASCADE)
    book = models.TextField()

