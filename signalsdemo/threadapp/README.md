## How Django Signals Work with Threading
    Django signals, by default, execute synchronously in the same thread as the view that triggers them. This means that both the view and the signal receiver run in the same thread, and their execution is sequential.

In the context of threading, if we log the thread IDs of both the view and the signal handler, we can observe that they share the same thread. This demonstrates that signals are processed in the same thread as the caller, rather than spawning a new thread for the signal handling.

## Console Output
    When a signal is triggered, we can observe the following sample output in console:
        View started in thread: 140570292090688 at 1726134820.3592165
        Signal received in thread: 140570292090688 at 1726134820.3707514
        Signal processing finished in thread: 140570292090688 at 1726134822.3717377
        View finished in thread: 140570292090688 at 1726134822.3717377

    As we can see:
    Both the view and the signal handler are executed in the same thread (the thread ID is the same: 140570292090688).
    The view and the signal handler share the same lifecycle, confirming that the signal is processed synchronously within the same thread.

## Description (Proof)
    If Django signals were executed in a different thread, the thread ID for the signal handler would be different from the view. However, as seen in the console output, both share the same thread ID, proving that they run within the same thread.
