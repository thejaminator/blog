+++
title = 'Mutable Defaults and How to Fix them'
date = 2024-03-19T18:48:19+08:00
draft = false
tags = [
    "python",
    "gotchas",
    "typing",
    "pydantic",
]
+++

Most people know the issue with mutable defaults in Python. But what's the best way to fix it?

## The issue
```python
class User:
    def __init__(self, name: str, emails: list[str] = []) -> None:
        self.name = name
        self.emails = emails

    def add_email(self, email: str) -> None:
        self.emails.append(email)

james = User(name="James")
james.add_email("james@gmail.com")
john = User(name="John")
# John will have the emails ['james@gmail.com'], even though we never added that email to John's list.
# That's a bug!!
print(john.emails)
```

In tools such as ruff, you'll see
```
B006 Do not use mutable data structures for argument defaults
Found 1 error.
```

The issue is that the default value for `strings` is a mutable list. This means that if you modify the list, the default value will be modified subsequently.

## Suggested fix - type annotate the list as a Sequence

```python
from typing import Sequence

class User:
    def __init__(self, name: str, emails: Sequence[str] = []) -> None:
        self.name = name
        self.emails: list[str] = list(emails)

    def add_email(self, email: str) -> None:
        self.emails.append(email)
```

Typing emails as `Sequence[str]` promises to users and your type checker that you won't modify the list.
This allows you to use `[]` as a default, because you won't ever mutate it.
For example, when we assign `self.email`, we call `list(emai)` to create a new list, which is a new object.

## Other possible fix - Use None as the default value

```python
class User:
    def __init__(self, name: str, emails: list[str] | None = None) -> None:
        self.name = name
        self.emails = emails or []

    def add_email(self, email: str) -> None:
        self.emails.append(email)

```


This solves the problem by using None as a default. Since None is immutable, it won't be modified when you modify the list.
However, I don't really like this solution because it is confusing to me what the difference is when you pass [] or None.
In this case, there is no difference between `[]` or None, but it requires the user to read the code to understand that.
Furthermore, since the type signature may be list[str], it is not clear where the User class would mutate the list that you pass in.
The `add_email` method for instance, may mutate the list that you pass in, which leads to future bugs.



## Sidenotes and fun facts - dataclasses vs pydantic's approach
Mutable defaults is the reason why dataclasses ban mutable defaults.
If you do this, you'll get the error `mutable default <class 'list'> for field emails is not allowed: use default_factory`.
```
from dataclasses import dataclass

@dataclass
class UserDataclass:
    emails: list[str] = [] # kaboom


So you need to do this instead:
@dataclass
class UserDataclass2:
    emails: list[str] = field(default_factory=list) # OK
```

Unfortunately, dataclasses still throw an error even if you typed it as a Sequence, which is annoying.

Pydantic's approach on the other hand, does a smart deepcopy trick, where they copy the default value whenever you create a new instance of the class.
This copying avoids the mutable defaults problem, and allows you to use mutable defaults without any issues.

```python
from pydantic import BaseModel

class UserPydantic(BaseModel):
    name: str
    emails: list[str] = [] # OK, although I would still type this as a Sequence[str] to avoid other mutation bugs

    def add_email(self, email: str) -> None:
        self.emails.append(email)

james = UserPydantic(name="James")
james.add_email("james@gmail.com")
print(james.emails)
john = UserPydantic(name="John")
print(john.emails) # [] instead of ['james@gmail.com'] that we got with the User class. So no bugs here
```






