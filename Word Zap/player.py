#Richard Timpson
#Word Zap
#player.py
#CS 1410 TR: 9:00 - 10:15
#Curtis Larsen

import random
class Player:

	def __init__(self, name):
		self.mName = name
		self.mLetters = []
		for x in range(7):
			self.drawLetter()
	def getName(self):
		return self.mName
	def getLetters(self):
		return self.mLetters
	def drawLetter(self):
		letters = 'aaaaaaaaabbccddddeeeeeeeeeeeeffggghhiiiiiiiiijkllllmmnnnnnnooooooooppqrrrrrrssssttttttuuuuvvwwxyyz'
		random1 = random.randint(1, len(letters)-1)
		letter = letters[random1]
		self.mLetters.append(letter)
		return letter
	def printLetters(self):
		string = ''
		letters = self.getLetters()
		for x in range(len(letters)):
			if x != len(letters) - 1:
				string += letters[x] + ' '
			else:
				string += letters[x]
		return string
	def checkWord(self, word):
		string = ''
		list1 = self.getLetters()
		leng = len(list1)
		if len(word) > len(list1):
			return False
		for i in range(len(word)):
			for j in range(leng):
				if word[i] == list1[j]:
					string += word[i]
					list1.pop(j)
					leng -= 1
					break
		if string == word:
			self.mLetters = list1
			return True
		else:
			return False



