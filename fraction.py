class Fraction:
    def __init__(self, numerator: int, denominator: int = 1):
        self.numerator, self.denominator = numerator, denominator
        self.reduce()

    def reduce(self):
        for i in range(min(self.denominator, self.numerator), 0, -1):
            if self.numerator % i == 0 and self.denominator % i == 0:
                self.numerator //= i
                self.denominator //= i
                break

    def __str__(self):
        if self.numerator == 0:
            return '0'
        else:
            integer_part = self.numerator // self.denominator
            if integer_part == 0:
                return f'{self.numerator}/{self.denominator}'
            else:
                fraction_part = self.numerator - integer_part * self.denominator
                if fraction_part == 0:
                    return f'{integer_part}'
                else:
                    return f'{integer_part} {fraction_part}/{self.denominator}'

    def __add__(self, other):
        return Fraction(self.numerator * other.denominator + self.denominator * other.numerator,
                        self.denominator * other.denominator)
    def __sub__(self, other):
        return Fraction(self.numerator * other.denominator - self.denominator * other.numerator,
                        self.denominator * other.denominator)

    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __pow__(self, power, modulo=None):
        return Fraction(self.numerator**power, self.denominator**power)

    def __float__(self):
        return self.numerator / self.denominator

    def __lt__(self, other):
        return float(self) < float(other)

    def __eq__(self, other):
        return float(self) == float(other)

if __name__ == '__main__':
    f1 = Fraction(25,10)
    print(f1)
    d = {'numerator': 75, 'denominator': 30}
    f2 = Fraction(**d)
    print(f2)
    f3 = f1 - f2
    print(f3)
    f = [Fraction(i, 12) for i in range(1, 12)]
    print(', '.join([str(fr) for fr in f]))
    import random
    random.shuffle(f)
    print(', '.join([str(fr) for fr in f]))
    f.sort(key=lambda x: float(x))
    print(', '.join([str(fr) for fr in f]))
    random.shuffle(f)
    print(', '.join([str(fr) for fr in f]))
    f.sort()
    print(', '.join([str(fr) for fr in f]))

    f4 = f1 / f2
    print(f4)