from django.urls import path
from . import views

urlpatterns = [
    path('thread-test/', views.thread_test_view, name='thread_test_view'),
    path('', views.thread_home_view, name='thread_home_view'),
]
