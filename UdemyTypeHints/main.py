# type annotations for basic data types
text:str = "hello"
number:int = 10
percent:float = 0.50
is_connected:bool = False

# if we give type hints explicitly, it helps editor to provide hints
def format_input(user_input:str):
    return user_input.capitalize()

print(format_input("hello world"))
