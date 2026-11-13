"""HW11 Question 3: Tracing a recursive function

Below is a recursive function called `flatten()`. It takes a nested list and returns a flat list 
containing all the elements.

Your task is to write a non-recursive version of the `flatten()` function. You may use for loops,
while loops, and auxiliary data structures (like lists or dicts). Your non-recursive version should 
be called `flatten_non_recursive()` and produce the same output as the recursive `flatten()` 
function.

Make sure to write tests for `flatten_non_recursive()` in the tests directory.
The autograder has tests to ensure that `flatten_non_recursive()` does not use recursion, but you
do not need to test that.
"""

from typing import Any

def flatten(items: list[Any]) -> list[int]:
    """Return a flat list containing all the elements from the nested list.
    
    
    Args:
        items: A nested list of integers.

    Returns:
        A flat list containing all the integers from the nested list.
    """
    result: list[int] = []
    for item in items:
        if isinstance(item, int):
            result.append(item)
        else:
            result.extend(flatten(item))
    return result
