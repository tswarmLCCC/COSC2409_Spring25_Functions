# Python Functions

## Introduction
Functions are reusable blocks of code that perform a specific task. They help in organizing code, making it more readable and maintainable.

## Defining a Function
In Python, a function is defined using the `def` keyword followed by the function name and parentheses `()`.

```python
def function_name(parameters):
    """Docstring describing the function."""
    # Function body
    return result
```

## Example
Here is a simple example of a function that adds two numbers:

```python
def add_numbers(a, b):
    """This function returns the sum of two numbers."""
    return a + b
```

## Calling a Function
To call a function, use the function name followed by parentheses containing arguments.

```python
result = add_numbers(5, 3)
print(result)  # Output: 8
```

