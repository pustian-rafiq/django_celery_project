import json

def process_api_response(data):
    """
    Process the API response and prepare data for CSV.
    """
    
    #mapping api response data for creating invoice(810) csv file
    data_list = []
    for index,item in enumerate(data['Invoices'][0]['Lines']):
        data_dict = {
            'Transaction ID': 810,
            'Accounting ID': '',
            'Purchase Order Number': '',
            'PO Date': '',
            'Invoice Number': data['Invoices'][0]['InvoiceNumber'],
            'Invoice Date':  data['Invoices'][0]['InvoiceDate'],
            'Ship To Name':  data['Customer'],
            'Ship To Address - Line One': data['ShippingAddress']['DisplayAddressLine1'],
            'Ship To Address - Line Two': data['ShippingAddress']['DisplayAddressLine2'],
            'Ship To City': data['ShippingAddress']['City'],
            'Ship To State': data['ShippingAddress']['State'],
            'Ship To Zip code': data['ShippingAddress']['Postcode'],
            'Ship To Country': data['ShippingAddress']['Country'],
            'Store #':  '',
            'Bill To Name':  data['Customer'],
            'Ship To Address - Line One': data['BillingAddress']['DisplayAddressLine1'],
            'Ship To Address - Line Two': data['BillingAddress']['DisplayAddressLine2'],
            'Ship To City': data['BillingAddress']['City'],
            'Ship To State': data['BillingAddress']['State'],
            'Ship To Zip code': data['BillingAddress']['Postcode'],
            'Ship To Country': data['BillingAddress']['Country'],
            'Bill To Code':  '',
            'Ship Via':  '',
            'Ship Date':  '',
            'Terms':   data['Terms'],
            'Note':   data['Note'],
            'Department Number':  '',
            'Do Not Ship Before':  '',
            'Do Not Ship After':  '',
            'Allowance Percent1':  '',
            'Allowance Amount1':  '',
            'Allowance Percent2':  '',
            'Allowance Amount2':  '',
            'Line #':  index + 1,
            'Vendor Part #':  '',
            'Buyer Part #':  '',
            'UPC #':  item['SKU'],
            'Description':   item['Name'],
            'Quantity':   item['Quantity'],
            'UOM':  '',
            'Unit Price':   item['Price'],
            'Pack Size':  '',
            '# of Inner Packs':  '',
            'Item Allowance Percent1':  '',
            'Item Allowance Amount1':  '',
        }
        data_list.append(data_dict)
    return data_list