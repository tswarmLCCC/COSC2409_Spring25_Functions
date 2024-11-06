import nbformat as nbf

# Create a new notebook
nb = nbf.v4.new_notebook()

# Add markdown and code cells
cells = [
    nbf.v4.new_markdown_cell("# Functions and Default Arguments\n\nIn this notebook, we will explore how to use functions with default arguments in Python. Default arguments allow us to define functions that can be called with fewer arguments than they are defined to accept.\n\n## Defining a Function with Default Arguments\n\nLet's start by defining a simple function with default arguments."),
    nbf.v4.new_code_cell("def greet(name, greeting=\"Hello\"):\n    return f\"{greeting}, {name}!\"\n\n# Example usage\nprint(greet(\"Alice\"))\nprint(greet(\"Bob\", \"Hi\"))"),
    nbf.v4.new_markdown_cell("### Explanation\n\n1. **Function Definition**: We define a function `greet` that takes two arguments: `name` and `greeting`. The `greeting` argument has a default value of `\"Hello\"`.\n\n2. **Calling the Function**: \n    - When we call `greet(\"Alice\")`, it uses the default value for `greeting`, so the output is `\"Hello, Alice!\"`.\n    - When we call `greet(\"Bob\", \"Hi\")`, it uses the provided value for `greeting`, so the output is `\"Hi, Bob!\"`.\n\n## Using Default Arguments in More Complex Functions\n\nDefault arguments can be very useful in more complex functions. Let's see an example where we calculate the area of a rectangle, with a default value for the width."),
    nbf.v4.new_code_cell("def calculate_area(length, width=10):\n    return length * width\n\n# Example usage\nprint(calculate_area(5))\nprint(calculate_area(5, 20))"),
    nbf.v4.new_markdown_cell("### Explanation\n\n1. **Function Definition**: We define a function `calculate_area` that takes two arguments: `length` and `width`. The `width` argument has a default value of `10`.\n\n2. **Calling the Function**:\n    - When we call `calculate_area(5)`, it uses the default value for `width`, so the output is `5 * 10 = 50`.\n    - When we call `calculate_area(5, 20)`, it uses the provided value for `width`, so the output is `5 * 20 = 100`.\n\n## Important Considerations\n\nWhen using default arguments, it's important to remember that default values are evaluated only once. This can lead to unexpected behavior when using mutable default arguments like lists or dictionaries.\n\n### Example with Mutable Default Argument"),
    nbf.v4.new_code_cell("def append_to_list(value, my_list=[]):\n    my_list.append(value)\n    return my_list\n\n# Example usage\nprint(append_to_list(1))\nprint(append_to_list(2))\nprint(append_to_list(3))"),
    nbf.v4.new_markdown_cell("### Explanation\n\n1. **Function Definition**: We define a function `append_to_list` that takes two arguments: `value` and `my_list`. The `my_list` argument has a default value of an empty list `[]`.\n\n2. **Calling the Function**:\n    - When we call `append_to_list(1)`, it appends `1` to the default list, so the output is `[1]`.\n    - When we call `append_to_list(2)`, it appends `2` to the same list, so the output is `[1, 2]`.\n    - When we call `append_to_list(3)`, it appends `3` to the same list, so the output is `[1, 2, 3]`.\n\n### Solution\n\nTo avoid this issue, we can use `None` as the default value and initialize the list inside the function."),
    nbf.v4.new_code_cell("def append_to_list(value, my_list=None):\n    if my_list is None:\n        my_list = []\n    my_list.append(value)\n    return my_list\n\n# Example usage\nprint(append_to_list(1))\nprint(append_to_list(2))\nprint(append_to_list(3))"),
    nbf.v4.new_markdown_cell("### Explanation\n\n1. **Function Definition**: We define a function `append_to_list` that takes two arguments: `value` and `my_list`. The `my_list` argument has a default value of `None`.\n\n2. **Initializing the List**: Inside the function, we check if `my_list` is `None`. If it is, we initialize it to an empty list `[]`.\n\n3. **Calling the Function**:\n    - When we call `append_to_list(1)`, it appends `1` to a new list, so the output is `[1]`.\n    - When we call `append_to_list(2)`, it appends `2` to a new list, so the output is `[2]`.\n    - When we call `append_to_list(3)`, it appends `3` to a new list, so the output is `[3]`.\n\nBy using `None` as the default value, we ensure that a new list is created each time the function is called, avoiding the issue of shared mutable default arguments.")
]

# Add cells to the notebook
nb['cells'] = cells

# Write the notebook to a file
with open('test.ipynb', 'w') as f:
    nbf.write(nb, f)