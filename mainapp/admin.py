from django.contrib import admin
from .models import SalesOrder, Invoice
# Register your models here.
admin.site.register(SalesOrder)
admin.site.register(Invoice)