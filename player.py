import random

class Player:

	def __init__(self, name):
		self.mName = name
		self.mLetters = []
		for x in range(7):
			self.drawLetter
	def getName(self):
		return self.mName
	def getLetters(self):
		return self.mLetters
	def drawLetter(self):
		letters = 'aaaaaaaaabbccddddeeeeeeeeeeeeffggghhiiiiiiiiijkllllmmnnnnnnooooooooppqrrrrrrssssttttttuuuuvvwwxyyz'
		random = random.randit(1, len(letters))
		letter = letters[random]
		self.mLetters.append(letter)
		return letter
	def printLetters(self):
		letters = self.getLetters()
		letters = letters.strip()
		for x in letters:
			print (x + ' ')
	def checkWord(self, word):
		string = ''
		for i in word:
			for j in self.mLetters:
				if i == j:
					string+= i
					self.mLetters.pop(j)
		if string == word:
			return True
		else:
			return False



