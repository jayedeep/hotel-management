from django.contrib import admin
from .models import User,Restaurants,Foods
# Register your models here.

admin.site.register(Restaurants)
admin.site.register(Foods)