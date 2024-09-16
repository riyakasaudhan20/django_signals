from django.http import HttpResponse
from django.shortcuts import render
from .models import SimpleModel
import time

def test_view(request):
    start_time = time.time()
    print(f"View started at {start_time}")
    
    SimpleModel.objects.create(name="Test")
    
    end_time = time.time()
    print(f"View finished at {end_time}")
    return HttpResponse(f"Total time: {end_time - start_time} seconds")

def home_view(request):
    return render(request, 'signalapp/home.html')