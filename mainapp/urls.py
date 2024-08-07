from django.urls import path
from . import views
urlpatterns = [
    path('fgfg', views.test, name='test'),
    path('invoice', views.create_invoice_csv, name='create_invoice_csv'),
    path('order-status', views.create_order_status_csv, name='create_order_status_csv'),
    path('get-po', views.get_850_csv, name='get_850_csv'),
]
