from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import time

class SimpleModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=SimpleModel)
def my_callback(sender, instance, created, **kwargs):
    print(f"Signal received at {time.time()}")
    time.sleep(2)  # delay to observe signals pattern
    print(f"Signal processing finished at {time.time()}")