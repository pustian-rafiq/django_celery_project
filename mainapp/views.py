from django.http import HttpResponse
from django.shortcuts import render
from .tasks import test_func
from django.http import JsonResponse
import json
import pandas as pd
from .utils import prepare_invoice_data_for_csv

# Create your views here.
def test(request):
    test_func.delay()
    return HttpResponse("Done")

def create_invoice_csv(request):
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
    df.to_csv('810.csv',index=False)

    return JsonResponse(invoice_list, safe=False)