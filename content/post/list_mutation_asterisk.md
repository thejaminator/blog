+++
title = 'Accidental list mutation with asterisk'
date = "2024-03-15"
tags = [
    "python",
    "gotchas",
]
draft = true
+++

Let's say you want to create a list, which has another 10 empty lists. 
Meaning that you want to create a list that looks like this:
```python
[[], [], [], [], [], [], [], [], [], []]
```
You might be tempted to do this:

```python
lists = [[]] * 10
print(lists)
# Output: [[], [], [], [], [], [], [], [], [], []]
```
That looks ok! But this will not work as expected. This will create a list with 10 references to the same empty list. This means that if you modify one of the lists, all of the other lists will also be modified (because they are all the same list).
Let's see it in action:
```python
first_list = lists[0]
# Mutate the first list
first_list.append(1)
print(lists)
# Output: [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1]]
```
To create a list of 10 empty lists, you should use the range function:
```python
lists_v2 = [[] for _ in range(10)]
first_list_v2 = lists_v2[0]
# Mutate the first list
first_list_v2.append(1)
print(lists_v2)
# Output: [[1], [], [], [], [], [], [], [], [], []]
```
Why does this work? The range function creates a new empty list for each iteration. This means that each list is a separate object, and modifying one list will not affect the other lists.

