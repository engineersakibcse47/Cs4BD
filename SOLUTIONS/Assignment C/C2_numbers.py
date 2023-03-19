"""
Write single-line expressions to initialize member variables `a) - k)`
such that they yield the results shown in comments.
Only use [built-in functions](https://docs.python.org/3/library/functions.html)
or Python's powerful expressions
[ternary operators](https://book.pythontips.com/en/latest/ternary_operators.html),
[list comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp)
Don't write own functions.
"""
class C2_numbers:

    def __init__(self, numbers=[4, 12, 3, 8, 17, 12, 1, 8, 7]):
        """
        Constructor.
        """
        if numbers != None and type(numbers==list):
            self.numbers = numbers

        # a) initialize with number of numbers: 9
        self.a = len(numbers)    

        # b) initialize with first three numbers: [4, 12, 3]
        self.b = numbers[0:3]       

        # c) initialize with last three numbers: [1, 8, 7]
        self.c = numbers[-3:]

        # d) initialize with last three numbers reverse: [7, 8, 1]
        self.d = numbers[:-4:-1]

        # e) initialize with odd numbers: [3, 17, 1, 7]
        self.e = [num for num in numbers if num % 2 != 0]

        # f) initialize with number of odd numbers: 4
        self.f = len(list(filter(lambda x: (x%2 != 0) , numbers)))

        # g) initialize with sum_ of odd numbers: 28
        self.g = sum(num for num in numbers if num % 2 != 0) 

        # h) duplicate numbers removed: [4, 12, 3, 8, 17, 1, 7]
        self.h = list( dict.fromkeys(numbers))

        # i) number of duplicate numbers: 2
        self.i = len(numbers)- len(set(numbers))

        # j) ascending list of squared numbers with no duplicates: [1, 9, 16, 49, 64, 144, 289]
        self.j = sorted(x * x for x in dict.fromkeys(numbers))

        # k) initialize with "ODD_LIST", "EVEN_LIST" or "EMPTY_LIST" depending on numbers length
        self.k = 'EMPTY_LIST' if (len(numbers) <= 0) else 'ODD_LIST' if (len(numbers) % 2) else 'EVEN_LIST'


    def print_results(self):
        print(f'numbers: {self.numbers}\n#')
        fmt = {
            # key: (value, output string)
            'a': (self.a, 'number of numbers'),
            'b': (self.b, 'first three numbers'),
            'c': (self.c, 'last three numbers'),
            'd': (self.d, 'last three numbers reverse'),
            'e': (self.e, 'odd numbers'),
            'f': (self.f, 'number of odd numbers'),
            'g': (self.g, 'sum of odd numbers'),
            'h': (self.h, 'duplicate numbers removed'),
            'i': (self.i, 'number of duplicate numbers'),
            'j': (self.j, 'ascending, de-dup (n^2) numbers'),
            'k': (self.k, 'length'),
        }
        # format output, e.g.: "b) first three numbers: [1, 4, 6]"
        for k in sorted(fmt.keys()):
            print(f'{k}) {fmt[k][1]}: {fmt[k][0]}')



if __name__ == '__main__':
    """
    Main driver that starts program when called from command line.
    """
    #
    n1 = C2_numbers()   # use default list in C2_numbers
    #
    n2 = C2_numbers([1, 4, 6, 67, 6, 8, 23, 8, 34, 49, 67, 6, 8, 23, 37, 67, 6, 34, 19, 67, 6, 8])
    #
    n1.print_results()
    n2.print_results()     # try also other list