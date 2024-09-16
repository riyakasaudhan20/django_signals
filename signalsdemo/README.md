# Signal Demo Project

This project demonstrates the use of Django signals and threading.

## Applications
- **signalapp**: A signal app that triggers a signal upon saving a model.
- **threadapp**: An app that demonstrates signal handling and threading behavior in Django.

## Setup
1. Clone the repository.
2. Install dependencies.
3. Run migrations.
4. Start the Django development server.

# SignalApp

This app demonstrates how Django signals work.

## Features
- A `SimpleModel` that triggers a `post_save` signal when an instance is created.
- A view that creates this model and logs signal handling.

## How to test
1. Visit `/test/` to trigger the signal.

# ThreadApp

This app demonstrates how signals are handled in the same thread as the view that triggers them.

## Features
- A `ComplexModel` that triggers a signal upon saving, with threading behavior being logged.
- A view that creates this model and logs the threading details.

## How to test
1. Visit `/threadapp/thread-test/` to trigger the thread signal.
