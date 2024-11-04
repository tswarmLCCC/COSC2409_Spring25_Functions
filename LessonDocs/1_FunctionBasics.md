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

## Parameters and Arguments
- **Parameters** are variables listed inside the parentheses in the function definition.
- **Arguments** are the values passed to the function when it is called.

## Return Statement
The `return` statement is used to exit a function and return a value.

```python
def square(x):
    """Returns the square of a number."""
    return x * x
```

## Docstrings
Docstrings are string literals that appear right after the function definition and are used to describe the function's purpose.

```python
def greet(name):
    """This function greets the person whose name is passed as an argument."""
    print(f"Hello, {name}!")
```

## Conclusion
Functions are a fundamental aspect of Python programming, enabling code reuse and better organization. Understanding how to define and use functions is essential for writing efficient and maintainable code.