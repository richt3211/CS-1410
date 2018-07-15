"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
"""

import unittest

import main

class TestEatFoodAction(unittest.TestCase):
    def input_replacement(self, prompt):
        self.assertFalse(self.too_many_inputs)
        self.input_given_prompt = prompt
        r = self.input_response_list[self.input_response_index]
        self.input_response_index += 1
        if self.input_response_index >= len(self.input_response_list):
            self.input_response_index = 0
            self.too_many_inputs = True
        return r

    def print_replacement(self, *text, **kwargs):
        line = " ".join(text) + "\n"
        self.printed_lines.append(line)

    def setUp(self):
        self.too_many_inputs = False
        self.input_given_prompt = None
        self.input_response_index = 0
        self.input_response_list = [""]
        main.input = self.input_replacement

        self.printed_lines = []
        main.print = self.print_replacement

    def test001_eatFoodActionExists(self):
        self.assertTrue('eatFoodAction' in dir(main),
                        'Function "eatFoodAction" is not defined, check your spelling')

    def test002_eatFoodAction_updatesBalance(self):
        from main import eatFoodAction
        from caloric_balance import CaloricBalance

        cb = CaloricBalance('f', 23.0, 65.0, 130.0)
        expected = -1417.9
        actual = cb.getBalance()
        self.assertAlmostEqual(actual, expected, 2,
                               'Your result (%s) is not close enough to (%s)' % (actual, expected))

        self.input_response_list = ["400"]
        eatFoodAction(cb)

        actual_response = self.input_response_list[self.input_response_index]
        self.assertEqual("400", actual_response)

        actual2 = cb.getBalance()
        self.assertNotEqual(actual, actual2,
                            'Your eatFoodAction did not update the caloric balance.')

    def test003_eatFoodAction_updatesBalance(self):
        from main import eatFoodAction
        from caloric_balance import CaloricBalance

        cb = CaloricBalance('f', 23.0, 65.0, 130.0)
        expected = -1417.9
        actual = cb.getBalance()
        self.assertAlmostEqual(actual, expected, 2,
                               'Your result (%s) is not close enough to (%s)' % (actual, expected))

        expected_response = "400"
        self.input_response_list = ["0", "-1.7", "-20", "zero", "twleve", "", "\n", expected_response]
        eatFoodAction(cb)

        actual2 = cb.getBalance()
        self.assertNotEqual(actual, actual2,
                            'Your eatFoodAction did not update the caloric balance.')

        expected = actual + float(expected_response)
        actual  = actual2
        self.assertAlmostEqual(expected, actual, 2,
                               'Your result (%s) is not close enough to (%s). Did you use getUserFloat?' % (actual, expected))


    def test004_eatFoodAction_updatesBalance(self):
        from main import eatFoodAction
        from caloric_balance import CaloricBalance

        cb = CaloricBalance('f', 23.0, 65.0, 130.0)
        expected = -1417.9
        actual = cb.getBalance()
        self.assertAlmostEqual(actual, expected, 2,
                               'Your result (%s) is not close enough to (%s)' % (actual, expected))

        expected_response = "998"
        self.input_response_list = ["0", "-1.7", "-20", "zero", "twleve", "", "\n", expected_response, "500", "600", "700"]
        eatFoodAction(cb)

        actual2 = cb.getBalance()
        self.assertNotEqual(actual, actual2,
                            'Your eatFoodAction did not update the caloric balance.')

        expected = actual + float(expected_response)
        actual  = actual2
        self.assertAlmostEqual(expected, actual, 2,
                               'Your result (%s) is not close enough to (%s). Did you use getUserFloat?' % (actual, expected))

if __name__ == '__main__':
    unittest.main()
