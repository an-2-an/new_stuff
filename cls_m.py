class Boy:
    ID = 0
    def __init__(self, name, age):
        self.name, self.age = name, age
        Boy.ID += 1
        self.id = Boy.ID
    def __str__(self):
        return f'Boy {self.name}, age={self.age}, id={self.id}'
    @classmethod
    def from_str(cls, line):
        return cls(line.split()[0], int(line.split()[1]))

    @classmethod
    def from_arr_str(cls, lines):
        return [Boy.from_str(line) for line in lines]

    @classmethod
    def show_ID(cls):
        print(f'next ID will be {cls.ID + 1}')

if __name__ == '__main__':
    boy1 = Boy.from_str('Johnny 12')
    print(boy1)

    s = ['Billy 10', 'Sammy 11']
    boys = Boy.from_arr_str(s)
    for boy in boys:
        print(boy)

    Boy.show_ID()

