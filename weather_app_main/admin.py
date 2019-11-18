from django.contrib import admin

# Register your models here.
from .models import City

admin.site.register(City)

admin.site.site_header = "Weather Application Admin"
admin.site.site_title = "Weather Application Admin Area"
admin.site.index_title = "Welcome to Weather Application Admin Area"
