from django.contrib import admin
from .models import Book, Publisher, Category, Author
from accounts.models import CustomUser, UserAddress, Report

# Register your models here.

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Publisher)
admin.site.register(CustomUser)
admin.site.register(UserAddress)
admin.site.register(Report)
