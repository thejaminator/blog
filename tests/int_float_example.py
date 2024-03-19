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