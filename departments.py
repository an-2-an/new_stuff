class Worker:
    def __init__(self, name, salary):
        self.name, self.salary = name, salary
    def __str__(self):
        return f'Worker {self.name}, salary={self.salary}'

class Manager(Worker):
    def __init__(self, name, salary, education):
        Worker.__init__(self, name, salary)
        self.education = education
    def __str__(self):
        return f'Manager {self.name}, salary={self.salary}, educ.={self.education}'

class Department:
    def __init__(self, head, *staff):
        self.head = head
        self.staff = list(staff)
    def show_info(self):
        print(f'Department Head: {self.head.name}, staff={[s.name for s in self.staff]}')
    def show_personal_alphabetical_order(self):
        for p in sorted(self.staff + [self.head], key=lambda x: x.name):
            print(f'|{p.name:^16}|{type(p).__name__:^10}|{float(p.salary):^10.2f}|')


if __name__ == '__main__':
    w1 = Worker('Jones', 2000)
    w2 = Worker('Benson', 1900)
    w3 = Worker('Dembrose', 1700)
    m1 = Manager('Ivanov', 2900, 'ZNTU')
    d1 = Department(m1, w1, w2, w3)
    d1.show_info()
    d1.show_personal_alphabetical_order()
