import unittest

'''
Given two integers a and b, which can be positive or negative,
find the sum of all the numbers between including them too and return it.
If the two numbers are equal return a or b.

Note: a and b are not ordered!

getSum(1, 0) == 1   // 1 + 0 = 1
getSum(1, 2) == 3   // 1 + 2 = 3
getSum(0, 1) == 1   // 0 + 1 = 1
getSum(1, 1) == 1   // 1 Since both are same
getSum(-1, 0) == -1 // -1 + 0 = -1
getSum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2
'''

# return int
def getSum(a, b):
    # Write your code here
    pass

# Tests
class getSumMethods(unittest.TestCase):
    def getSumDiff(self):
        self.assertEqual(getSum(10, 10), 10)
        self.assertEqual(getSum(0, 1), 1)
        self.assertEqual(getSum(0, -1), -1)
        self.assertEqual(getSum(-1, 2), 2)


if __name__ == '__main__':
    unittest.main()
