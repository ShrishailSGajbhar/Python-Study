from typing import Any
from sys import getsizeof

def get_size(user_input: Any):
    print(f"{user_input} -> {getsizeof(user_input)} bytes")

get_size([1,2,3])
get_size("Hello World!")
get_size(None)

from typing import Final
CONSTANT: Final[str] = "I am a string constant"
PI: Final[float] = 3.14

print(CONSTANT)
print(PI)

CONSTANT = "Hello World"
PI = 4.44

print(CONSTANT)
print(PI)

# Iterables
from typing import Iterable

def print_names(names:Iterable[str]):
    for i, name in enumerate(names, start=1):
        print(i, name)

print_names(["Shrishail","Sharad","Gajbhar"])

sample_list: list[int] = [1,2,3]
sample_set: set[int] = {1,2,3}

from typing import Sequence

def get_first_element(sequence: Sequence[int]) -> int:
    return sequence[0] if sequence else -1

print(get_first_element(sample_list))
# get_first_element(sample_set)