from typing import Union

# type annotations for basic data types
text:str = "hello"
number:int = 10
percent:float = 0.50
is_connected:bool = False

# if we give type hints explicitly, it helps editor to provide hints
def format_input_str(user_input:str):
    return user_input.capitalize()

print(format_input_str("hello world"))

# add the union operator for adding more than one type hints to the variable
def format_input(user_input:Union[int, str]):
    print(user_input)

format_input(10)

# install and use mypy package to caught some uncaught exceptions
uncaught_list: list[str] = [10, None, "hello"]
'''
 mypy main.py
main.py:22: error: List item 0 has incompatible type "int"; expected "str"  [list-item]
main.py:22: error: List item 1 has incompatible type "None"; expected "str"  [list-item]
Found 2 errors in 1 file (checked 1 source file)
'''

# Tuple
coordinates: tuple[int, str, bool] = (10, "hello", True)

# Set
set1: set[int] = {1,2,3}
set2: set[int|str] = {"a", 1, "b", 2}

# dictionary
dict1:dict[int,int] = {1:1, 2:2}
dict2:dict[int|str, int] = {"a":1, 2:2}

# optional
person: str | None = "Shri"

def greet(name: str | None = None):
    if name is None:
        print("No one to greet!")
    else:
        print(f"Hello, {name}")

greet()

# Classes
class Fruit:
    def __init__(self, name:str, weight:int) -> None:
        self.name = name
        self.weight = weight
    
    def describe(self):
        print(f"The {self.name} weighs {self.weight} grams..")

orange:Fruit = Fruit(name="Orange", weight=300)
orange.describe()
    
    