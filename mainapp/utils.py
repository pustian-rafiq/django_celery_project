import json
import datetime

def prepare_invoice_data_for_csv(sales_order,invoice,line,line_index):
    """
    Process the API response and prepare data for CSV.
    """
    #mapping api response data for creating invoice(810) csv file
    data_dict = {
        'Transaction ID': 810,
        'Accounting ID': '',
        'Purchase Order Number': '',
        'PO Date': '',
        'Invoice Number': invoice['InvoiceNumber'],
        'Invoice Date':  invoice['InvoiceDate'],
        'Ship To Name':  sales_order['Customer'],
        'Ship To Address - Line One': sales_order['ShippingAddress']['DisplayAddressLine1'],
        'Ship To Address - Line Two': sales_order['ShippingAddress']['DisplayAddressLine2'],
        'Ship To City': sales_order['ShippingAddress']['City'],
        'Ship To State': sales_order['ShippingAddress']['State'],
        'Ship To Zip code': sales_order['ShippingAddress']['Postcode'],
        'Ship To Country': sales_order['ShippingAddress']['Country'],
        'Store #':  '',
        'Bill To Name':  sales_order['Customer'],
        'Ship To Address - Line One': sales_order['BillingAddress']['DisplayAddressLine1'],
        'Ship To Address - Line Two': sales_order['BillingAddress']['DisplayAddressLine2'],
        'Ship To City': sales_order['BillingAddress']['City'],
        'Ship To State': sales_order['BillingAddress']['State'],
        'Ship To Zip code': sales_order['BillingAddress']['Postcode'],
        'Ship To Country': sales_order['BillingAddress']['Country'],
        'Bill To Code':  '',
        'Ship Via':  '',
        'Ship Date':  '',
        'Terms':   sales_order['Terms'],
        'Note':   sales_order['Note'],
        'Department Number':  '',
        'Do Not Ship Before':  '',
        'Do Not Ship After':  '',
        'Allowance Percent1':  '',
        'Allowance Amount1':  '',
        'Allowance Percent2':  '',
        'Allowance Amount2':  '',
        'Line #':  line_index + 1,
        'Vendor Part #':  '',
        'Buyer Part #':  '',
        'UPC #':  line['SKU'],
        'Description':   line['Name'],
        'Quantity':   line['Quantity'],
        'UOM':  '',
        'Unit Price':   line['Price'],
        'Pack Size':  '',
        '# of Inner Packs':  '',
        'Item Allowance Percent1':  '',
        'Item Allowance Amount1':  '',
    }
    return data_dict

def prepare_order_status_for_csv(order_status,line,line_index):
    data_dict = {
        'Status': order_status["FulFilmentStatus"],
        'Reference #': '',
        'Status Report Date': datetime.datetime.now().strftime ("%Y%m%d"),
        'Order/Item Code': order_status["Order"]["SaleOrderNumber"],
        'Purpose': '',
        'Total':  line['Total'],
        'PO #':  '',
        'PO Date': '',
        'Vendor Order #': '',
        'Item Sequence #': line_index + 1,
        'UPC #': line['SKU'],
        'Buyer Part #': '',
        'Vendor Item #': '',
        "Manufacturer's Part #": '',
        'Quantity':  line['Quantity'],
        'UOM':  '',
        'Price': line['Price'],
        # 'Status': '',
        'Expected Ship Date': '',
        'Store #': '',
        'DC #': '',
        }
    return data_dict