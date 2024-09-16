from django.contrib import admin
from django.urls import path, include
from signalapp.views import test_view, home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test_view, name='test_view'),
    path('', home_view, name='home'),  # signalapp URLs
    path('threadapp/', include('threadapp.urls')),  # threadapp URLs
    path('transactionapp/', include('transactionapp.urls')), #transaction URLs
]
