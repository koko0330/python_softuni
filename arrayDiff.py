import unittest

'''
Implement a difference function, which subtracts one list from another and returns the result.
It should remove all values from list a, which are present in list b

arrayDiff([1,2], [1]) == [2]
arrayDiff([1,2,2,2,3], [2]) == [1,3]
'''

# return list
def arrayDiff(a, b):
    # write your code here
    pass

# Tests
class arrayDiffMethods(unittest.TestCase):
    def testArrayDiff(self):
        self.assertEqual(arrayDiff([1,2], [1]), [2])
        self.assertEqual(arrayDiff([1,2,2,2,3], [2]), [1,3])
        self.assertEqual(arrayDiff([1,5,2,2,3], [2]), [1,5,3])

if __name__ == '__main__':
    unittest.main()
