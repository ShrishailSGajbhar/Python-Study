def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

plus = add
print(plus(2,3))
print(plus)
print(add)

operations = [add, subtract]
print(operations[1](2,3))