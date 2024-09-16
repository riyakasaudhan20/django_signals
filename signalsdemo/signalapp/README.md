## How Django Signals Work
    Django signals are executed synchronously by default. This means that when a signal is sent, the code in the receiver function is executed immediately, before the next line of code after the signal dispatch is run.

## Console Output
    When a signal is triggered, we can observe the following sample output in console:
        View started at 1726134810.3592165
        Signal received at 1726134810.3707514
        Signal processing finished at 1726134812.3717377
        View finished at 1726134812.3717377
    As we can see, the view doesn't end until after the signal receiver has finished, demonstrating that the signal is processed synchronously.

## Description (Proof)
    If signals were asynchronous, the view would finish almost immediately, and the total time would be close to 0 seconds.
    However, when we run this code and access the /test/ URL, we'll see that the total time is over 5 seconds. This proves that the view waits for the signal receiver to finish before completing.
    Hence,The output demonstrates that the view doesn't end until after the signal receiver has finished processing. This shows that the signal is processed synchronously, meaning the signal's processing is completed before the view finishes.

## References
    https://python.plainenglish.io/django-signals-sync-async-c2bd3294e403

