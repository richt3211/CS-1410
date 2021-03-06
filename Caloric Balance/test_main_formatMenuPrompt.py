"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
"""

import unittest

import main


class TestFormatMenuPrompt(unittest.TestCase):
    def test001_formatMenuPromptExists(self):
        self.assertTrue('formatMenuPrompt' in dir(main),
                        'Function "formatMenuPrompt" is not defined, check your spelling')
        return

    def test002_formatMenuPromptReturnsCorrectString(self):
        from main import formatMenuPrompt
        expected = "Enter an option: "
        actual = formatMenuPrompt()
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
