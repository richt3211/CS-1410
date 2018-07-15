#Richard Timpson
#Word Zap
#main.py
#CS 1410 TR: 9:00 - 10:15
#Curtis Larsen

import player
import sys
def getUserInt(string):
	while True:
		try:
			int1 = input(string)
			int1 = int(int1)
			if int1 > 0:
				return int1
			else:
				print ("Enter a int float number greater than or equal to 0")
		except:
			print ("Enter a valid int number greater than or equal to 0")
def getUserString(string):
	input1 = input(string)
	input1 = input1.strip()
	return input1
def getPlayers():
	playersList = []
	players = getUserInt('How many players would you like to have?')
	for x in range(players):
		name = getUserString("What is player " + str(x + 1) + "'s name?")
		player1 = player.Player(name)
		playersList.append(player1)
	return playersList
def convertToLower(word):
	word = word.lower()
	return word
def formatMenu():
	string = 'Time to play Word Zap!. See if you can use all of your letters. \n The first player to use all of their letters wins!\n'
	return string
def gameLoop(player, letters):
	name = player.getName()
	print ('\n' + str(name) + ', it is your turn')
	print ('Your letters are: ' + letters )
	string = getUserString('Enter a word to play or press enter to pass: ')
	if string == "":
		player.drawLetter()
		return True
	wordCheck = player.checkWord(string)
	if wordCheck == True:
		print ('Good Job\n')
		return True
	else:
		print ('Check your letters and try again')
		return False
def gameOver(player):
	letters = player.getLetters()
	if not letters:
		return True
	else:
		return False
def main():
	menu = formatMenu()
	print (menu)
	players = getPlayers()
	while True:
		for x in players:
			for i in range(7):
				letter = x.drawLetter
		for y in players:
			move = False
			while move == False:
				move = gameLoop(y,y.printLetters())
			if gameOver(y) == True:
				name = y.getName()
				print (name + " wins!")
				sys.exit ( 0 )
if __name__ == '__main__':
	main()


