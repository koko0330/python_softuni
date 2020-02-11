import unittest

'''
Write a function strToInt, that can transform a string into a number..

strToInt("1234") == 1234
strToInt("605" ) == 605
strToInt("1405") == 1405
strToInt("-7"  ) == -7
'''

# return int
def strToInt(inputString):
    # Write your code here...
    pass







# Tests
class TestStrToIntMethods(unittest.TestCase):
    def __handler(self, cases):
        for case in cases:
            inStr = case
            outStr = strToInt(case)
            print("Input->|%s| Output->|%s| Excpected->|%s|" % (inStr, outStr, cases[case]))
            self.assertEqual(outStr, cases[case])

    def testStrToInt(self):
                # "input":"excpectedOut"
        cases =[{"1234567":1234567,  "12":12, "2":2, "-12": -12}]

        for case in cases:
            self.__handler(case)


if __name__ == '__main__':
    unittest.main()
