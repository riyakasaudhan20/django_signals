from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import threading
import time

class ComplexModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=ComplexModel)
def complex_callback(sender, instance, created, **kwargs):
    print(f"Signal received in thread: {threading.get_ident()} at {time.time()}")
    time.sleep(2)
    print(f"Signal processing finished in thread: {threading.get_ident()} at {time.time()}")
