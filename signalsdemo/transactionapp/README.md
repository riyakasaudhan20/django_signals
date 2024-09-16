## How Django Signals Work with Database Transactions (TransactionApp)
By default, Django signals are triggered within the same database transaction as the caller. This means if the caller (typically the view or model operation) is wrapped in a transaction, the signal will also execute within that same transaction.

If the transaction is rolled back, the changes made in the signal handler (such as saving to the database) will also be rolled back.

## Console Output (TransactionApp)
When we access the /transactionapp/transaction-test/ URL, the following sample output is displayed in the console:

    View started at 1726134820.3592165, in transaction: True
    Signal triggered in the transaction: True
    View finished at 1726134822.3717377, in transaction: True
    As seen from the output:

    The view is wrapped in an atomic transaction (in_atomic_block: True).
    The signal handler is executed within the same transaction, as indicated by in_atomic_block: True in both the view and the signal handler.

## Description (Proof with Database Transactions)
If Django signals were executed outside of the transaction, the in_atomic_block flag inside the signal handler would be False. However, in this case, both the view and the signal handler have in_atomic_block set to True, proving that they are part of the same transaction.
