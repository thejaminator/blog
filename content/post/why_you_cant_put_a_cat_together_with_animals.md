+++
title = 'When my Cats are not Animals - an explanation of invariance and covariance'
date = 2024-03-19T15:44:15+08:00
draft = false
+++

Let's say you have a parent class `Animal` and a child class `Cat` that inherits from `Animal`. 
You might think that you can add a `Cat` to a list of `Animal`s. But then your pyright / vscode / mypy linter will complain that you can't do that. Why is that?

Let's start with a simple example:

```python
class Animal:
    def make_sound(self) -> None:
        print(f"animal!")

class Dog(Animal):
    ...

class Cat(Animal):
    ...

    def meow(self) -> None:
        print("meow!!")

def make_animal_sounds(animals: list[Animal]) -> None:
    for animal in animals:
        animal.make_sound()

def make_cat_sounds(cats: list[Cat]) -> None:
    for cat in cats:
        cat.meow()
def main():
    cats: list[Cat] = [Cat()]
    make_cat_sounds(cats=cats) # OK
    make_animal_sounds(animals=cats) # "Typeerror: list[Cat] is compatible with list[Animal]"
    
```

Why is `list[Cat]` incompatible with `list[Animal]`?
The reason is that `list[Cat]` is not a subclass of `list[Animal]`.
This is weird to us - because `Cat` is a subclass of `Animal`, so why isn't `list[Cat]` a subclass of `list[Animal]`?

The short answer is that the `list` is mutable and so you'll get into trouble if you allow `list[Cat]` to be a subclass of `list[Animal]`.

Let's see an example where `list[Cat]` is a subclass of `list[Animal]`, and things exploding.

```python
def main():
    cats: list[Cat] = [Cat()]
    animals: list[Animal] = cats # Normally, this would be flagged out as an error, but let's pretend that this is allowed
    animals.append(Dog()) # This is allowed a Dog can be added to a list of Animals
    make_cat_sounds(cats=cats) # Explodes at runtime because you'll call .meow() on a Dog
    make_animal_sounds(animals=animals) # OK
```

This is why `list[Cat]` is not a subclass of `list[Animal]`. If it were, you would be able to add a `Dog` to a list of `Cat`s, and that would be a disaster by causing make_cat_sounds(cats=cats) to explode at runtime.
In confusing-type-theory-speak, we say that `list` is *invariant* in its type parameter. This means that `list[Cat]` is not a subclass of `list[Animal]`.


## How do I fix it - Promise to never mutate the list
The real problem is mutability. Our `.append(Dog())` caused the explosion.
Now what happens if we promise to never mutate that list[Cat]?
We can promise by type hinting the cats in `make_cat_sounds` as a Sequence[Cat].



```python
from typing import Sequence
class Animal:
    def make_sound(self) -> None:
        print(f"animal!")

class Dog(Animal):
    ...

class Cat(Animal):
    ...

    def meow(self) -> None:
        print("meow!!")

def make_animal_sounds(animals: Sequence[Animal]) -> None:
    for animal in animals:
        animal.make_sound()

def make_cat_sounds(cats: Sequence[Cat]) -> None:
    for cat in cats:
        cat.meow()
def main():
    cats: Sequence[Cat] = [Cat()]
    animals: Sequence[Animal] = cats # Allowed, because a Sequence[Cat] is a subclass of Sequence[Animal].
    # animals.append(Dog()) # You can't do this - this will be flagged as an error. So we are forced to make a new list instead
    make_cat_sounds(cats=animals) # OK because you never mutated the list to add a dog
    new_animals = list(cats) + [Dog()] # OK
    make_animal_sounds(animals=new_animals) # OK
```

## What just happened?
By changing the type hint from `list` to `Sequence`, we are saying that we promise to never mutate the list. This is a good thing because it makes our code safer. We can't accidentally add a `Dog` to a list of `Cat`s.
By promising to never mutate the list, we are allowed to treat a `Sequence[Cat]` as a `Sequence[Animal]`. This is called *covariance* in confusing-type-theory-speak.


## In the wild
Where else do you see this?

Normally in python we say that an int can be treated as a float.

However when you try to pass a list[int] to a function that expects a list[float], this is not allowed because `list[int]` is not a subclass of `list[float]`. You can fix this by promising to never mutate the list, and changing the type hint to `Sequence[float]`.

Example
```python
from typing import Sequence

def print_float(f: float) -> None:
    print(f)

def print_floats(floats: list[float]) -> None:
    for f in floats:
        print_float(f)

def print_floats_seq(floats: Sequence[float]) -> None:
    for f in floats:
        print_float(f)


def main():
    single_int: int = 1
    print_float(f=single_int) # OK
    ints: list[int] = [1, 2, 3]
    print_floats(floats=ints) # "Typeerror: list[int] is not compatible with list[float]"
    ints_seq: Sequence[int] = [1, 2, 3] # OK
    print_floats_seq(ints_seq)
```

## What does this mean for library authors?
In general, you should use `Sequence` instead of `list` in your type hints. Two reasons
- The Sequence being covariant accepts a wider range of inputs. The Sequence[float] accepts a list[int] and a list[float]. But a list[float] only accepts a list[float].
- A Sequence is more general than a list. A Sequence can be a list, a tuple, or any other sequence type (like a tuple of floats..) This makes your library more flexible. In principle we want the most general type hint that we can get away with.

See [the excellent pyright best practices guide](https://github.com/microsoft/pyright/blob/main/docs/typed-libraries.md#best-practices-for-inlined-types).
