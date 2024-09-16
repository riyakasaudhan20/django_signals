# transactionapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('transaction-test/', views.transaction_test_view, name='transaction_test_view'),
    path('', views.transaction_home_view, name='transaction_home_view'),
]
