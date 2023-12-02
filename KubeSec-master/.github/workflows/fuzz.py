# fuzz.py

import logging
logging.basicConfig(filename="fuzzlog.log", filemode='a', format='%(asctime)s %(message)s')
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
        inputs = f"{a} and {b}"
        print(f"Bug discovered in divide_numbers with inputs ({a}, {b}): {e}")
        logging.info("Error dividing inputs: %s", inputs)

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
        logging.info("Error finding maximum with : %s", lst)

# Fuzz square_root with positive integers
@given(integers(min_value=0))
def test_square_root(n):
    try:
        square_root(n)
    except Exception as e:
        print(f"Bug discovered in square_root with input {n}: {e}")

if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    test_multiply_numbers()
    test_divide_numbers()
    test_concatenate_strings()
    test_find_maximum()
    test_square_root()
