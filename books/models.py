import base64
import time
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.db import models
# Create your models here.
from django.urls import reverse
import random


class Author(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Author_detail", kwargs={"pk": self.pk})


class Publisher(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Publisher_detail", kwargs={"pk": self.pk})


class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})


class BookManager(models.Manager):
    def get_queryset(self):
        return super(BookManager, self).get_queryset().filter(available=True)

    def available_books(self):
        return self.get_queryset().count()


def save_image(data):
    format, imgstr = data.split(';base64,')
    ext = format.split('/')[-1]
    timestr = round(time.time() * 1000)
    rand_num = random.randrange(1000000, 9999999)
    data = ContentFile(base64.b64decode(imgstr), name=str(timestr) + str(rand_num) + '.' + ext)
    file_name = default_storage.save('frontend/public/images/books/'+data.name, data)
    #file_url = default_storage.url(file_name)
    return '/static/images/books/'+data.name


class Book(models.Model):

    SHIPMENT_CHOICES = (
        ('R', 'Receiver'),
        ('D', 'Donor'),
    )
    donor = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, null=True, default=None)
    name = models.CharField(max_length=250, db_index=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    abstract = models.TextField(blank=True)
    page_count = models.IntegerField(default=200, blank=False)
    shipment_type = models.CharField(max_length=1, choices=SHIPMENT_CHOICES, default='R')
    image = models.TextField(blank=True)
    image2 = models.TextField(blank=True)
    image3 = models.TextField(blank=True)

    objects = models.Manager()
    books_manager = BookManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Book_detail", kwargs={"pk": self.pk})

    def save(
        self, *args, **kwargs
    ):
        self.image = save_image(self.image)

        super(Book, self).save(*args, **kwargs)
