from celery import shared_task
import requests
from .models import SalesOrder, Invoice
import pandas as pd

@shared_task(bind=True)
def test_func(self):
    for i in range(10):
        print(i)
    return "Done"

@shared_task
def generate_invoice():
    # Call third-party API
    response = requests.get('https://fakestoreapi.com/products')
    products_data = response.json()
    print(products_data)
    # Generate sales invoice
    for sale in products_data:
        order = SalesOrder.objects.create(
            order_id=sale['id'],
            amount=sale['price'],
            customer=sale['title']
        )
        invoice = Invoice.objects.create(
            order=order,
            invoice_number=sale['id'],
            total=sale['price']
        )

    # Convert to CSV
    invoices = Invoice.objects.all()
    data = {
        'invoice_number': [],
        'order_id': [],
        'total': []
    }

    for invoice in invoices:
        data['invoice_number'].append(invoice.invoice_number)
        data['order_id'].append(invoice.order.order_id)
        data['total'].append(invoice.total)

    df = pd.DataFrame(data)
    print(df)
