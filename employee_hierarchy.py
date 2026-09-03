class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(self.name, "is doing regular work.")

    def describe(self):
        print(self.name, "- Salary:", self.salary)


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def work(self):
        super().work()
        print(self.name, "is also managing", self.team_size, "people.")

    def describe(self):
        print(self.name, "- Salary:", self.salary, "- Team Size:", self.team_size)


e = Employee("James", 5000)
m = Manager("Ana", 8000, 5)

e.work()
e.describe()

m.work()
m.describe()

print(isinstance(m, Employee))