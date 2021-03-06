"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
"""

import unittest
import main


class TestApplyAction(unittest.TestCase):
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

    def exit_replacement(self, value):
        self.exit_called = True
        self.exit_value = value

    def record_activity_replacement(self, index):
        self.record_activity_called = True

    def eat_food_replacement(self, index):
        self.eat_food_called = True

    def quit_replacement(self, index):
        self.quit_called = True

    def setUp(self):
        self.record_activity_called = False
        self.eat_food_called = False
        self.quit_called = False

        self.too_many_inputs = False
        self.input_given_prompt = None
        self.input_response_index = 0
        self.input_response_list = [""]
        main.input = self.input_replacement

        self.printed_lines = []
        main.print = self.print_replacement

        self.exit_called = False
        self.exit_value = -1

        main.recordActivityAction = self.record_activity_replacement
        main.eatFoodAction = self.eat_food_replacement
        main.quitAction = self.quit_replacement

    def tearDown(self):
        return

    def test001_applyActionExists(self):
        self.assertTrue('applyAction' in dir(main),
                        'Function "applyAction" is not defined, check your spelling')

    def test002_applyActionCallsEatFoodActivity(self):
        from main import applyAction
        from caloric_balance import CaloricBalance
        cb = CaloricBalance('f', 23.0, 65.0, 130.0)
        obal = cb.getBalance()
        applyAction(cb, "f")
        self.assertEqual(obal, cb.getBalance(), 'applyAction should not change the caloric balance.')
        self.assertTrue(self.eat_food_called, "Option 'f' was provided, eatFoodAction should have been called.")
        self.assertFalse(self.record_activity_called, "Option 'f' was provided, recordActivityAction should not have been called.")
        self.assertFalse(self.quit_called, "Option 'f' was provided, quitAction should not have been called.")
        self.assertEqual(len(self.printed_lines), 0, 'Nothing should be printed in the applyAction function.')

    def test003_applyActionCallsRecordActivityAction(self):
        from main import applyAction
        from caloric_balance import CaloricBalance
        cb = CaloricBalance('f', 23.0, 65.0, 130.0)
        obal = cb.getBalance()
        applyAction(cb, "a")
        self.assertEqual(obal, cb.getBalance(), 'applyAction should not change the caloric balance.')
        self.assertFalse(self.eat_food_called,  "Option 'a' was provided, eatFoodAction should not have been called.")
        self.assertTrue(self.record_activity_called, "Option 'a' was provided, recordActivity should have been called.")
        self.assertFalse(self.quit_called, "Option 'a' was provided, quitAction should not have been called.")
        self.assertEqual(len(self.printed_lines), 0, 'Nothing should be printed in the applyAction function.')

    def test004_applyActionCallsQuitAction(self):
        from main import applyAction
        from caloric_balance import CaloricBalance
        cb = CaloricBalance('f', 23.0, 65.0, 130.0)
        obal = cb.getBalance()
        applyAction(cb, "q")
        self.assertEqual(obal, cb.getBalance(), 'applyAction should not change the caloric balance.')
        self.assertFalse(self.eat_food_called, "Option 'q' was provided, eatFoodAction should not have been called.")
        self.assertFalse(self.record_activity_called,  "Option 'q' was provided, recordActivityAction should not have been called.")
        self.assertTrue(self.quit_called,  "Option 'q' was provided, quitAction should have been called.")
        self.assertEqual(len(self.printed_lines), 0, 'Nothing should be printed in the applyAction function.')

    def test005_applyActionDetectsIllegalAction(self):
        from main import applyAction
        from caloric_balance import CaloricBalance
        cb = CaloricBalance('f', 23.0, 65.0, 130.0)
        obal = cb.getBalance()
        applyAction(cb, "x")
        self.assertEqual(obal, cb.getBalance(), 'applyAction should not change the caloric balance.')
        self.assertFalse(self.eat_food_called, "An illegal option was provided, eatFoodActiion should not have been called.")
        self.assertFalse(self.record_activity_called,  "An illegal option was provided, recordActivityAction should not have been called.")
        self.assertFalse(self.quit_called,  "An illegal option was provided, quitAction should not have been called.")
        self.assertGreaterEqual(len(self.printed_lines), 0, 'Nothing should be printed in the applyAction function.')


if __name__ == '__main__':
    unittest.main()
