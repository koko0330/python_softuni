import unittest

'''
Write a function maskify, which changes all but the last four characters into '*'.

maskify("4556364607935616") == "************5616"
maskify("64607935616") ==  "*******5616"
maskify("1") == "1"
maskify("") ==  ""

Useful: https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3
'''

# return masked string
def maskify(inputString):
    # Write your code here...

    pass


# Tests
class TestMaskifyMethods(unittest.TestCase):
    def __handler(self, cases):
        for case in cases:
            inStr = case
            outStr = maskify(case)
            print("Input->|%s| Output->|%s| Excpected->|%s|" % (inStr, outStr, cases[case]))
            self.assertEqual(outStr, cases[case])

    def testMaskify(self):
                # "input":"excpectedOut"
        cases =[{"1234567":"***4567",  "1234567891011":"*********1011"},
                {"":"",  "1":"1",  "   a  2":"***a  2", "       ":"***    "},
                {"abcDeF1232":"******1232",  "abcDeF1AA2":"******1AA2"},
                {"Revane!": "***ane!",  "sUhoto$Ko!":"******$Ko!"}]

        for case in cases:
            self.__handler(case)


if __name__ == '__main__':
    unittest.main()
