from django.http import HttpResponse
from django.shortcuts import render
from .models import ComplexModel
import threading
import time

def thread_test_view(request):
    start_time = time.time()
    print(f"View started in thread: {threading.get_ident()} at {start_time}")
    
    ComplexModel.objects.create(name="Thread Test")
    
    end_time = time.time()
    print(f"View finished in thread: {threading.get_ident()} at {end_time}")
    return HttpResponse(f"Total time: {end_time - start_time} seconds")

def thread_home_view(request):
    return render(request, 'threadapp/home.html')
