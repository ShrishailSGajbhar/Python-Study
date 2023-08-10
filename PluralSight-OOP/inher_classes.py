class Employee:
    __slots__ = ("name", "age", "salary")

    def __init__(self, name, age, salary) -> None:
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

    def has_slots(self):
        return hasattr(self, "__slots__")

class SlotsInspectorMixin:
    __slots__ = ()
    
    def has_slots(self):
        return hasattr(self, "__slots__")

class Tester(Employee):
    def run_tests(self):
        print(f"Testing started by {self.name}")
        print(f"Testing over")


class Developer(SlotsInspectorMixin, Employee):
    __slots__ = ("framework",)

    def __init__(self, name, age, salary, framework) -> None:
        super().__init__(name, age, salary)
        self.framework = framework

    def increase_salary(self, percent, bonus=0):
        # Why not Employee.increase_salary(percent)?..super() makes it dynamic.
        super().increase_salary(percent)
        self.salary += bonus


t1 = Tester("SSG", 36, 1000)
t1.increase_salary(20)
print(t1.salary)

t2 = Developer("Ji-soo", 38, 1000, "Flask")
t2.increase_salary(20, 30)
print(t2.salary)

print(isinstance(t1, Tester))
print(isinstance(t2, Developer))
print(issubclass(Developer, Employee))
print(issubclass(Developer, object))

print(t2.framework)

# print(t1.__dict__) # should give an error as slots are used for memory optimization
# print(t2.__dict__) # should give an error as slots are used for memory optimization

print(t2.__slots__)

print(t2.has_slots())
print(t2.__dict__)