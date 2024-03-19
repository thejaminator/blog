+++
author = "James Chua"
title = "Native zip is evil"
date = "2024-03-16"
tags = [
    "python",
    "gotchas",
]
+++


The `zip` function is a built-in function in Python that allows you to combine two or more iterables into a single iterable. This is a useful function, but it has a very dangerous pitfall that can lead to very subtle bugs.
It does not raise an error when the two iterables have different lengths. Instead, it will silently ignore the extra elements of the longer iterable. This can lead to very hard to track bugs (and has hurt me in the past).

For example
    
```python
a = [1, 2, 3]
b = [4, 5, 6, 7]
zipped = zip(a, b)
print(list(zipped))
# Output: [(1, 4), (2, 5), (3, 6)]
# My 7 is gone!
```

I propose safe_zip, a function that raises an error when the two iterables have different lengths. This will make it easier to catch bugs early and avoid annoying bugs.

```python
from typing import Sequence, TypeVar

A = TypeVar('A')
B = TypeVar('B')
def safe_zip(first: Sequence[A], second: Sequence[B]) -> Sequence[tuple[A, B]]:
    if len(first) != len(second):
        raise ValueError(f"Length of first iterable ({len(first)=}) does not match length of second iterable ({len(second)=})")
    return zip(first, second)

test_list_1 = [1, 2, 3]
test_list_2 = [4, 5, 6, 7]
try:
    safe_zip(test_list_1, test_list_2)
except ValueError as e:
    print(f"Caught error: {e}")
```
