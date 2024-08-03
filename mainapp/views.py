from django.http import HttpResponse
from django.shortcuts import render
from .tasks import test_func
from django.http import JsonResponse
import json
import pandas as pd
from .utils import process_api_response

# Create your views here.
def test(request):
    test_func.delay()
    return HttpResponse("Done")

def create_invoice_csv(request):
    #Request to API for invoice data
    # response = requests.get('https://api.example.com/invoices')
    
    #open json file
    response = open('invoice.json')
    #read json file
    data = json.load(response)
    
    # Prepare API response data for CSV
    data_list = process_api_response(data)
    
    #convert data to dataframe
    df = pd.DataFrame(data_list)
    
    #create csv file
    df.to_csv('810.csv')

    return JsonResponse(data)