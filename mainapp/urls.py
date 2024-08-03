from django.urls import path
from . import views
urlpatterns = [
    path('fgfg', views.test, name='test'),
    path('invoice', views.create_invoice_csv, name='create_invoice_csv'),
]
