
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

