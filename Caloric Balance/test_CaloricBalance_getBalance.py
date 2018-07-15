"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
"""

import unittest

import caloric_balance


class TestCaloricBalanceGetBalance(unittest.TestCase):
    def test001_getBalanceExists(self):
        self.assertTrue('getBalance' in dir(caloric_balance.CaloricBalance),
                        'Function "getBalance" is not defined, check your spelling')

    def test002_f_getBalance(self):
        from caloric_balance import CaloricBalance
        cb = CaloricBalance('f', 23.0, 65.0, 130.0)

        balance = cb.getBalance()
        expected = -1417.9

        self.assertAlmostEqual(balance, expected, 2, 'Your result (%s) is not close enough to (%s)' % (balance, expected))

    def test003_f_getBalance(self):
        from caloric_balance import CaloricBalance
        cb = CaloricBalance('f', 27.0, 74.0, 155.0)

        balance = cb.getBalance()
        expected = -1550.15

        self.assertAlmostEqual(balance, expected, 2, 'Your result (%s) is not close enough to (%s)' % (balance, expected))

    def test004_m_getBalance(self):
        from caloric_balance import CaloricBalance
        cb = CaloricBalance('m', 26.0, 70.5, 185.0)

        balance = cb.getBalance()
        expected = -1937.1

        self.assertAlmostEqual(balance, expected, 2, 'Your result (%s) is not close enough to (%s)' % (balance, expected))

    def test005_m_getBalance(self):
        from caloric_balance import CaloricBalance
        cb = CaloricBalance('m', 35.0, 76.0, 275.0)

        balance = cb.getBalance()
        expected = -2506.45

        self.assertAlmostEqual(balance, expected, 2, 'Your result (%s) is not close enough to (%s)' % (balance, expected))

    def test006_x_getBalance(self):
        from caloric_balance import CaloricBalance
        cb = CaloricBalance('x', 26.0, 70.5, 185.0)

        balance = cb.getBalance()
        expected = 0.0

        self.assertEqual(balance, expected, 'Your result (%s) is not equal to (%s)' % (balance, expected))


if __name__ == '__main__':
    unittest.main()