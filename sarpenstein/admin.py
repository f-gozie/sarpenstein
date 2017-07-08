from django.contrib import admin
from .models import Device, Customer, Sale
# Register your models here.
admin.site.register(Device)
admin.site.register(Customer)
admin.site.register(Sale)