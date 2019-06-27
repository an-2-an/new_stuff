class Salary:
    def __init__(self, pay):
        self.pay = pay

    def getTotal(self):
        return (self.pay * 12)


class Employee:
    def __init__(self, name, salary, bonus):
        self.name = name
        self.bonus = bonus
        self.salary = salary

    def annualSalary(self):
        print(f"{self.name}\'s total: {self.salary.getTotal() + self.bonus}")

if __name__ == '__main__':
    salary = Salary(100)
    employee = Employee('Ben', salary, 10)
    employee.annualSalary()