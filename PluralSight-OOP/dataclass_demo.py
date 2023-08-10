from dataclasses import dataclass

@dataclass(slots=True) # enable memory optimization with slots parameter
class Project:
    name: str
    payment: int
    client: str

    def notify_client(self):
        print(f"Notifying the client about progress of the {self.name}")


class Employee:
    def __init__(self, name, age, salary, project) -> None:
        self.name = name
        self.age = age
        self.salary = salary
        self.project = project
    
    
p = Project("Django app", 20000, "Globomantics")
e = Employee("Ji-Soo", 38, 1000, p)
print(e.project)    
    

        