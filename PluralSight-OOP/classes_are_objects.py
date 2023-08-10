from datetime import date

class Employee:
    minimum_wage = 1000 # class attribute

    @classmethod
    def change_minimum_wage(cls, new_wage):
        if new_wage > 3000:
            raise ValueError("Company can't afford")
        cls.minimum_wage = new_wage

    @classmethod
    def new_employee(cls, name, dob):
        now = date.today()
        age = now.year - dob.year - ((now.month, now.day) < (dob.month, dob.day))
        return cls(name, age, cls.minimum_wage)
    
    def __init__(self, name, age, salary) -> None:
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary*(percent/100)

    @property
    def salary(self):
        return self.increase_salary
    
    @salary.setter
    def salary(self, salary):
        if salary < Employee.minimum_wage:
            raise ValueError(f"Mininum wage is ${Employee.minimum_wage}")
        self._salary = salary

print(Employee.minimum_wage)
Employee.change_minimum_wage(200)
print(Employee.minimum_wage)

e1 = Employee.new_employee("Shrishail", date(1987, 3, 5))
print(e1.__dict__)