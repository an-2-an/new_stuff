import unittest
from fraction import Fraction

class TestFraction(unittest.TestCase):

    def setUp(self):
        self.a = Fraction(2, 3)
        self.b = Fraction(1, 6)
        print(f'a = {self.a}')
        print(f'b = {self.b}')

    def test1(self):
        '''Тестируем сумму'''
        res = self.a + self.b
        mustbe = Fraction(5, 6)
        print(res)
        self.assertEqual(res, mustbe)

    def test2(self):
        '''Тестируем разность'''
        res = self.a - self.b
        mustbe = Fraction(1, 2)
        print(res)
        self.assertEqual(res, mustbe)

    def test3(self):
        '''Тестируем произведение, деление и степень'''
        res = self.a * self.b
        mustbe = Fraction(1, 9)
        print(res)
        self.assertEqual(res, mustbe)
        res = self.a / self.b
        mustbe = Fraction(4)
        print(res)
        self.assertEqual(res, mustbe)
        res = self.a ** 3
        mustbe = Fraction(8, 27)
        print(res)
        self.assertEqual(res, mustbe)

    def test4(self):
        '''тестируем равенство дробей'''
        self.assertTrue(self.b, Fraction(3, 18))

if __name__ == '__main__':
    unittest.main(verbosity=2)