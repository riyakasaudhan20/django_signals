from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
import threading
import time

class TransactionModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=TransactionModel)
def transaction_callback(sender, instance, created, **kwargs):
    # Log the thread ID and database transaction status
    print(f"Signal received in thread: {threading.get_ident()} at {time.time()}")
    # Simulate a long-running process
    time.sleep(2)
    # Check if the database transaction is still active
    if transaction.get_connection().in_atomic_block:
        print(f"Database transaction is active at {time.time()}")
    else:
        print(f"Database transaction is not active at {time.time()}")
