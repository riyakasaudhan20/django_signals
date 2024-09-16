# Rectangle Class

## Overview
This project contains a Python class `Rectangle` that demonstrates how to work with custom classes and iteration in Python.

## Rectangle Class
The `Rectangle` class has the following features:
1. **Initialization**:
   - Requires `length` and `width` as integers.

2. **Iteration**:
   - Supports iteration to access `length` and `width` in the specified format.

### Usage

1. **Implementation**:
   ```python
   from rectangle import Rectangle

   # Create a Rectangle instance
   rectangle = Rectangle(10, 5)

   # Iterate over the instance
   for value in rectangle:
       print(value)

Output:
    {'length': 10}
    {'width': 5}

2. **Running the Example**:
    python rectangle.py

3. **Installation**:
    No additional packages are required. Ensure you have Python 3.x installed.
