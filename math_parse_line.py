class MathParser:

    nums = '0123456789.'
    signs = '()*/^+-'

    def __init__(self, lines):
        self.lines = lines
        self.results = []

    def parse(self):
        for line in self.lines:
            print(line)
            line2 = self.clear_line(line)
            print(line2)
            line3 = self.get_line_with_dividers(line2)
            a = self.get_list(line3)
#            print(a)
            b = self.reduce_arr(a)
            print(b)
            self.results.append(b[0])
            print('-' * 30)

    @staticmethod
    def clear_line(string):
        return ''.join([c for c in string if c in MathParser.nums + MathParser.signs])

    @staticmethod
    def get_line_with_dividers(string):
        for n in MathParser.nums:
            for s in MathParser.signs:
                if n + s in string:
                    string = string.replace(n + s, n + '|' + s)
                if s + n in string:
                    string = string.replace(s + n, s + '|' + n)
        for s1 in MathParser.signs:
            for s2 in MathParser.signs:
                if s1 + s2 in string:
                    string = string.replace(s1 + s2, s1 + '|' + s2)
        return string

    @staticmethod
    def get_list(string):
        res = string.split('|')
        for i in range(len(res)):
            if res[i] not in MathParser.signs:
                res[i] = float(res[i])
        return res

    @staticmethod
    def rindex(mylist, myvalue):
        return len(mylist) - mylist[::-1].index(myvalue) - 1

    def reduce_arr(self, arr: list):
        print(arr)
        if '(' in arr:
            i1 = arr.index('(')
            i2 = MathParser.rindex(arr, ')')
            #print(arr[:i1-1], arr[i1+1:i2], arr[i2+1:])
            return self.reduce_arr(arr[:i1] + self.reduce_arr(arr[i1+1:i2]) + arr[i2+1:])
        else:
            while '^' in arr:
                i = arr.index('^')
                res = arr[i-1] ** arr[i + 1]
                print('^', res)
                arr[i-1:i+2] = [res]
                print(arr)
            while self.is_there_unar_minus(arr):
                i = arr.index('-')
                res = -arr[i + 1]
                print('unar-', res)
                #print(i, arr[i:i+2])
                arr[i:i+2] = [res]
                print(arr)
            while '*' in arr:
                i = arr.index('*')
                res = arr[i - 1] * arr[i + 1]
                print('*', res)
                arr[i - 1:i + 2] = [res]
                print(arr)
            while '/' in arr:
                i = arr.index('/')
                res = arr[i - 1] / arr[i + 1]
                print('/', res)
                arr[i - 1:i + 2] = [res]
                print(arr)
            while '+' in arr:
                i = arr.index('+')
                res = arr[i - 1] + arr[i + 1]
                print('+', res)
                arr[i - 1:i + 2] = [res]
                print(arr)
            while '-' in arr:
                i = arr.index('-')
                res = arr[i - 1] - arr[i + 1]
                print('usual-', res)
                arr[i - 1:i + 2] = [res]
                print(arr)

            return arr

    def is_there_unar_minus(self, arr):
        return arr[0]=='-' or \
               any([not(isinstance(arr[i-1], float)) and arr[i]=='-' and \
                    isinstance(arr[i+1], float) for i in range(1, len(arr)-1)])


if __name__ == '__main__':
    lines = ['1+ 2.7',
             '2  *  (3 - 4),',
             '((2+3)*4)^2 - 11.1 / 2',
             '-3 + 4',
             '(11 - 3 * 3) * 7']

    parser = MathParser(lines)
    parser.parse()
    print(parser.results)
