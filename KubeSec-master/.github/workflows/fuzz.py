# fuzz.py

from hypothesis import given
from hypothesis.strategies import text, integers, lists
from example_module import multiply_numbers, divide_numbers, concatenate_strings, find_maximum, square_root

# Fuzz multiply_numbers with integer inputs
@given(integers(), integers())
def test_multiply_numbers(a, b):
    try:
        multiply_numbers(a, b)
    except Exception as e:
        print(f"Bug discovered in multiply_numbers with inputs ({a}, {b}): {e}")

# Fuzz divide_numbers with integer inputs
@given(integers(), integers())
def test_divide_numbers(a, b):
    try:
        divide_numbers(a, b)
    except Exception as e:
        print(f"Bug discovered in divide_numbers with inputs ({a}, {b}): {e}")

# Fuzz concatenate_strings with text inputs
@given(text(), text())
def test_concatenate_strings(s1, s2):
    try:
        concatenate_strings(s1, s2)
    except Exception as e:
        print(f"Bug discovered in concatenate_strings with inputs ('{s1}', '{s2}'): {e}")

# Fuzz find_maximum with a list of integers
@given(lists(integers()))
def test_find_maximum(lst):
    try:
        find_maximum(lst)
    except Exception as e:
        print(f"Bug discovered in find_maximum with input {lst}: {e}")

# Fuzz square_root with positive integers
@given(integers(min_value=0))
def test_square_root(n):
    try:
        square_root(n)
    except Exception as e:
        print(f"Bug discovered in square_root with input {n}: {e}")

if __name__ == "__main__":
    test_multiply_numbers()
    test_divide_numbers()
    test_concatenate_strings()
    test_find_maximum()
    test_square_root()
