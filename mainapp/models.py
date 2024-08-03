from django.db import models

from base.models import BaseModel

# Create your models here.
class SalesOrder(models.Model):
    order_id = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.CharField(max_length=100)

    def __str__(self):
        return self.order_id

class Invoice(models.Model):
    order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=10, decimal_places=2)