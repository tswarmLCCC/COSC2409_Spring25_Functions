# Abstraction with Functions

Abstraction is a fundamental concept in programming that helps manage complexity by hiding unnecessary details and exposing only the essential features of a module or function. In Python, functions are a primary tool for achieving abstraction.

## Using Functions for Abstraction

Functions allow you to encapsulate code into reusable blocks. This makes your code more modular, easier to read, and maintain.

### Example

```python
def calculate_area(radius):
    """Calculate the area of a circle given its radius."""
    import math
    return math.pi * (radius ** 2)
```

## Organizing Code in Separate Files

To further enhance abstraction and maintainability, you can organize your code into separate files. For example, you might have a `math_functions.py` file for mathematical operations and a `main.py` file for the main execution logic.

### Example Structure

```
/C:/homework/COSC2409/COSC2409_Spring25_Functions/
│
├── math_functions.py
├── main.py
└── tests/
    └── test_math_functions.py
```

### `math_functions.py`

```python
def calculate_area(radius):
    """Calculate the area of a circle given its radius."""
    import math
    return math.pi * (radius ** 2)
```

### `main.py`

```python
from math_functions import calculate_area

def main():
    radius = 5
    area = calculate_area(radius)
    print(f"The area of the circle with radius {radius} is {area}")

if __name__ == "__main__":
    main()
```

## Unit Testing

Unit tests help ensure that your functions work as expected. You can use the `unittest` module in Python to write and run tests.

### `tests/test_math_functions.py`

```python
import unittest
from math_functions import calculate_area

class TestMathFunctions(unittest.TestCase):

    def test_calculate_area(self):
        self.assertAlmostEqual(calculate_area(1), 3.141592653589793)
        self.assertAlmostEqual(calculate_area(0), 0)
        self.assertAlmostEqual(calculate_area(2.5), 19.634954084936208)

if __name__ == "__main__":
    unittest.main()
```

By organizing your code into functions, separate files, and using unit tests, you can achieve a higher level of abstraction and maintainability in your projects.