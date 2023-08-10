class Employee:
    def __init__(self, name, age, position, salary) -> None:
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self._annual_salary = None 

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old. Employee is a {self.position} with the salary of ${self.salary}"

    def __repr__(self) -> str:
        return (f"Employee(repr({self.name}), repr({self.age}), {self.position}, {self.salary})")
    
    @property
    def salary(self):
        return self._salary

    def get_salary(self):
        return self.salary
    
    @salary.setter
    def salary(self, salary):
        if salary<1000:
            raise ValueError("Minimum wage is $1000")
        else:
            self._salary=salary

    @property
    def annual_salary(self):
        if self._annual_salary is None:
            return self.salary * 12
        return self._annual_salary

e1 = Employee("Ji-Soo", 38, "developer", 1200)
e2 = Employee("Lauren", 44, "tester", 1000)
e2.increase_salary(percent=30)
print(repr(e1))

print(e1.get_salary())

e1.salary=1400
print(e1.annual_salary)