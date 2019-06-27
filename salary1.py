class Salary:
    def __init__(self, pay):
        self.pay = pay

    def getTotal(self):
        return (self.pay * 12)


class Employee:
    def __init__(self, name, pay, bonus):
        self.name = name
        self.bonus = bonus
        self.salary = Salary(pay)

    def annualSalary(self):
        print(f"{self.name}\'s total: {self.salary.getTotal() + self.bonus}")

if __name__ == '__main__':
    employee = Employee('Ben', 100, 10)
    employee.annualSalary()