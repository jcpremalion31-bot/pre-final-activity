class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(self.name, "is doing regular work.")

    def describe(self):
        print("Employee:", self.name, "- Salary:", self.salary)


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def work(self):
        super().work()
        print(self.name, "is also managing", self.team_size, "people.")


    def describe(self):
        print("Manager:", self.name)
        print("Salary:", self.salary)
        print("Team Size:", self.team_size)


m = Manager("Ana", 80000, 5)
e = Employee("John", 30000)


print("MANAGER:")
m.work()
m.describe()

print("\nEMPLOYEE:")
e.work()
e.describe()