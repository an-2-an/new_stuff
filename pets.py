class Kitty:
    def __init__(self, name, age):
        self.name, self.age = name, age
    def __str__(self):
        return f'Kitty {self.name}, age: {self.age}'
    def __lt__(self, other):
        if self.name == other.name:
            return self.age < other.age
        else:
            return self.name < other.name

if __name__ == '__main__':
    names = ['Mimy', 'Angus', 'Mimy', 'Barsik', 'Angus']
    ages = [5, 3, 4, 2, 2]
    cats = [Kitty(name, age) for name, age in zip(names, ages)]
    for cat in sorted(cats, key=lambda x: (x.name, x.age)):
        print(cat)
    for cat in sorted(cats):
        print(cat)
