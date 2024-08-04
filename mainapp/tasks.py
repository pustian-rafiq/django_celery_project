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
    
@shared_task
def fetch_and_process_sales_order():
    # Fetch sales order CSV from API
    response = requests.get('https://api.example.com/sales_order')
    sales_order_csv = response.text

    # Create payload for invoice API
    sales_order_df = pd.read_csv(StringIO(sales_order_csv))
    payload = sales_order_df.to_dict(orient='records')

    # Call invoice API
    invoice_response = requests.post('https://api.example.com/invoice', json=payload)
    invoice_data = invoice_response.json()

    # Create invoice CSV
    invoice_df = pd.DataFrame(invoice_data)
    invoice_csv = invoice_df.to_csv(index=False)

    # Upload invoice CSV to SFTP
    sftp_host = 'sftp.example.com'
    sftp_port = 22
    sftp_username = 'username'
    sftp_password = 'password'
    sftp_path = '/path/to/upload/invoice.csv'

    transport = paramiko.Transport((sftp_host, sftp_port))
    transport.connect(username=sftp_username, password=sftp_password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    with sftp.file(sftp_path, 'w') as f:
        f.write(invoice_csv)
    sftp.close()
    transport.close()