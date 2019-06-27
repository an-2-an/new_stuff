import unittest
import sys

def get_sum(a, b):
    return a + b

def is_even(a):
    return a % 2 == 0

def get_list_from_a_to_b(a, b):
    return list(range(min(a, b), max(a, b)+1))

class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.data1 = [
            {'params': [2, 3], 'target': 5},
            {'params': [20, 35], 'target': 55},
            ]

    def test1(self):
        for d in self.data1:
            self.assertEqual(get_sum(*d['params']), d['target'])

    def test2(self):
        self.assertTrue(is_even(10))
        self.assertFalse(is_even(7))
        with self.assertRaises(TypeError):
            is_even('yyy')

    def test3(self):
        self.assertEqual(get_list_from_a_to_b(1, 4), [1, 2, 3, 4])
        self.assertEqual(get_list_from_a_to_b(8, 4), [4, 5, 6, 7, 8])

    @unittest.skip('demo skipping')
    def test_none(self):
        pass

    @unittest.skipIf((sys.platform.startswith('win')), 'not for windows')
    def test_if(self):
        pass

    def test_fail(self):
        self.fail('oooops...')

if __name__ == '__main__':
    unittest.main(verbosity=2)


