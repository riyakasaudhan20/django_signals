from django.http import HttpResponse
from django.shortcuts import render
from .models import TransactionModel
from django.db import transaction
import time
import threading

@transaction.atomic
def transaction_test_view(request):
    start_time = time.time()
    print(f"View started in thread: {threading.get_ident()} at {start_time}")
    
    # Create an instance of the model to trigger the signal
    TransactionModel.objects.create(name="Transaction Test")
    
    end_time = time.time()
    print(f"View finished in thread: {threading.get_ident()} at {end_time}")
    return HttpResponse(f"Total time: {end_time - start_time} seconds")

def transaction_home_view(request):
    return render(request, 'transactionapp/home.html')
