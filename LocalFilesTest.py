#!/usr/bin/env python3
import LocalFilesCompetitionChecker, unitest

class TestStitchMethods(unittest.TestCase):

    # Original Files Stem from Margeaux
    path = 'INSERT PATH TO FILE'

    def testRegex(self):
        teststring1 = 'hello world, my name is qUadPay, and of course QUADPAY, quadpay, quadpay'
        teststring2 = 'nothing is here'
        test = regex(['quadpay', 'sezzle'])
        self.assertEqual(test.findall(teststring1), ['hello world, my name is qUadPay, and of course QUADPAY, quadpay, quadpay'])
        self.assertFalse(test.findall(teststring2), [])

    def testCountFiles(self):
        count = countFiles(path)
        self.assertEqual(count, 689)

if __name__ == "__main__":
    unitest.main()