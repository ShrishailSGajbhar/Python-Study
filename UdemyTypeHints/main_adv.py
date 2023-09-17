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

from typing import Callable
from datetime import datetime

def get_time() -> str:
    return f"{datetime.now():%H:%M:%S}"

def repeat(func:Callable, amount:int):
    for i in range(amount):
        print(f"{i+1}: {func()}")

repeat(get_time, 3)

def print_it(text:str, print_func:Callable[[str], None])->None:
    print_func(text)

def print_loud(text:str)->None:
    print(f"{text.upper()}!")

print_it('hello', print_func=print_loud)

# Protocols
from typing import Protocol
class Printer(Protocol):
    def print(self, magazine:str)->None:
        ...
    def copy(self, magazine:str, copies:int)->None:
        ...

class LazerPrinter:
    def __init__(self, name:str, version:int) -> None:
        self.name = name
        self.version = version
    
    def print(self, magazine:str) -> None:
        print(f"The printer {self.name} with version {self.version} is printing magazine {magazine}")
    def copy(self, magazine:str, copies:int)->None:
        print(f"The printer {self.name} with version {self.version} is printing {copies} copies of the magazine {magazine}")

lp:Printer = LazerPrinter("LazerPrinter",10)
lp.print("Python Grail")
lp.copy("Python Grail", 5)

class InkJetPrinter:
    def __init__(self, name:str, version:int) -> None:
        self.name = name
        self.version = version
    
    def print(self, magazine:str) -> None:
        print(f"The printer {self.name} with version {self.version} is printing magazine {magazine}")
    def copy(self, magazine:str, copies:int)->None:
        print(f"The printer {self.name} with version {self.version} is printing {copies} copies of the magazine {magazine}")

ijp:Printer = InkJetPrinter("InkJetPrintet", 11)
ijp.print("Python Adventures")
ijp.copy("Python Adventures", 11)