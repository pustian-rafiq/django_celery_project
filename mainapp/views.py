from django.http import HttpResponse
from django.shortcuts import render
from .tasks import test_func
from django.http import JsonResponse
import json
import pandas as pd
from .utils import prepare_invoice_data_for_csv, prepare_order_status_for_csv
import paramiko

# Create your views here.
def test(request):
    test_func.delay()
    return HttpResponse("Done")

def create_invoice_csv(request):
    # SFTP configuration
    sftp_host = '127.0.0.1'
    sftp_port = 21
    sftp_username = 'sgc'
    sftp_password = 'sgc123'
    # remote_file_path = '/'
    sftp_path = 'E:\Python Django Project\django-celery\django-celery\sales_order'

    #Request to API for invoice data
    # response = requests.get('https://api.example.com/invoices')
    
    #open json file
    with open('sales_order.json') as response:
        sales_orders = json.load(response)

    #read json file
    # data = json.load(response)
    
    # Prepare API response data for invoice CSV
    invoice_list = []
    for sales_order in sales_orders:
        for invoice in sales_order["Invoices"]:
            for line_index, line in enumerate(invoice["Lines"]):
                invoice_dict = prepare_invoice_data_for_csv(sales_order,invoice,line,line_index)
                invoice_list.append(invoice_dict)
                # print(line_index,line)
    
    #convert invoice list to dataframe
    df = pd.DataFrame(invoice_list)
    
    #create csv file
    invoice_csv = df.to_csv(index=False)

    # Upload the invoice CSV to SFTP
    transport = paramiko.Transport((sftp_host, sftp_port))
    transport.connect(username=sftp_username, password=sftp_password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    # sftp.put(invoice_local_file_path, '/path/to/invoice.csv')
    # sftp = paramiko.SFTPClient.from_transport(transport)
    # with sftp.file('811.csv', 'w') as f:
    #     f.write(invoice_csv)
    # sftp.close()
    # transport.close()

    return 'Sales order processed and invoice CSV uploaded successfully'
    # return JsonResponse(invoice_list, safe=False)

def create_order_status_csv(request):
     #open json file
    with open('order_status.json') as response:
        sales_orders = json.load(response)

    #read json file
    # data = json.load(response)
    
    # Prepare API response data for invoice CSV
    order_stat_list = []
    for order_status in sales_orders:
        for line_index, line in enumerate(order_status["Order"]["Lines"]):
            order_stat_dict = prepare_order_status_for_csv(order_status,line,line_index)
            order_stat_list.append(order_stat_dict)
            # print(line_index,line)
    
    #convert invoice list to dataframe
    df = pd.DataFrame(order_stat_list)
    
    #create csv file
    invoice_csv = df.to_csv('870.csv',index=False)
    return JsonResponse(order_stat_list, safe=False)

def get_850_csv(request):
     #open json file
    with open('850.json') as response:
        po_data = json.load(response)
    
    payload = []
    data_dic = {
            "SaleID": "",
            "Memo": "",
            "Status": "",
            "AutoPickPackShipMode": "",
            "Lines": [],
            "AdditionalCharges": [],
            "TotalBeforeTax": 0,
            "Tax": 0,
            "Total": 0
        }
    for data in po_data:
        payloadd_item_index = []
        po_number = data["Purchase Order Number"]
        if len(payload) > 0:
            for index, item in enumerate(payload):
                if item["Purchase Order Number"] == po_number:
                    payload_item_index = index
                else:
                     item = {
                        "ProductID": "",
                        "SKU": data["Buyer Part #"],
                        "Name": data["Description"],
                        "Quantity": data["Quantity"],
                        "Price": data["Unit Price"],
                        "Discount": 0,
                        "Tax": 0,
                        "AverageCost": 0,
                        "TaxRule": "",
                        "Comment": data["Note"],
                        "DropShip": False,
                        "BackorderQuantity": 0,
                        "Total": 0
                    }  

        data_dic["Lines"].append(item)
        payload.append(data_dic)
    return JsonResponse(po_data, safe=False)