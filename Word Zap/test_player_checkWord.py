"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
"""

import sys
if sys.version_info.major != 3:
    print('You must use Python 3.x version to run this unit test')
    sys.exit(1)

import unittest

import player

class TestPlayerCheckWord(unittest.TestCase):
    def test001_exists(self):
        self.assertTrue('checkWord' in dir(player.Player),
            'Function "checkWord" is not defined, check your spelling')

    def test002_checkWordReturnBool(self):
        from player import Player
        p = Player('Luke')
        letters = p.getLetters()[:]
        r = p.checkWord('123456789')
        self.assertFalse(r, 'You should returned False')

        word = letters[0]
        r = p.checkWord(word)
        self.assertTrue(r, 'You should have returned true because "%s" is in %s' % (word, letters))

        newletters = p.getLetters()
        self.assertNotEqual(newletters, letters, "You should have updated the user's letters to remove the letter used")

    def test003_checkWordAllLetters(self):
        from player import Player
        from random import shuffle
        p = Player('Luke')
        letters = p.getLetters()[:]
        shuffle(letters)
        word = ''.join(letters)
        r = p.checkWord(word)
        self.assertTrue(r, 'You should have returned true because "%s" can be made out of %s' % (word, letters))

        newletters = p.getLetters()
        self.assertEqual(newletters, [], "The user should have no more letters after playing the last word.")

    def test004_checkWordExtraLetter(self):
        from player import Player
        from random import shuffle
        p = Player('Luke')
        letters = p.getLetters()[:]
        oletters = letters[:]
        shuffle(letters)

        word = ''.join(letters)
        extraletter = letters[0]
        word += extraletter
        r = p.checkWord(word)
        self.assertFalse(r,
            'You should have returned true because "%s" can not be made out of %s, it has one too many of the letter "%s"'
            % (word, letters, extraletter))

        newletters = p.getLetters()
        self.assertEqual(newletters, oletters, "The user should have the same letters after attempting the last word.")

if __name__ == '__main__':
    unittest.main()
