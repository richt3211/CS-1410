import sys
def createIndex():
	index = {}
	return index
def recordBook(index, isbn,title):
	index[isbn] = title
def findBook(index, isbn):
	if isbn in index:
		return index[isbn]
	else:
		return ("")
def listBooks(index):
	list = []
	string = ''
	if not index:
		return list
	else:
		i = 1
		for key in index:
			string = str(i) + ") " + key + ": " + index[key] + ' \n'
			list.append(string)
			i += 1
	return list
index = {'0000-00000000': 'Book Title', '0000-12345678': 'War of the Worlds'}
def formatMenu():
	list = ['What would you like to do?', '[r] Record a Book' , '[f] Find a Book', '[l] List all Books' , '[q] Quit']
	return list
def formatMenuPrompt():
	string = "Enter an option: "
	return string
def getUserChoice(string):
	input1 = input(string)
	input1 = input1.strip()
	while not input1:
		input1 = input(string)
		input1 = input1.strip()
	return input1
def getISBN():
	isbn = getUserChoice('ISBN: ')
	return isbn
def getTitle():
	title = getUserChoice('title ')
	return title
def recordBookAction(index):
	isbn = getISBN()
	title = getTitle()
	recordBook(index,isbn,title)
def findBookAction(index):
	isbn = getISBN()
	display = findBook(index, isbn)
	print (display)
def listBooksAction(index):
	display = listBooks(index)
	if not display:
		print ("No books in index")
	else:
		for i in display:
			print (i)
def quitAction(index):
	display = "The program is now ending"
	print (display)
	sys.exit( 0 )
def applyAction(index, string):
	if string == 'r':
		recordBookAction(index)
	elif string == 'f':
		findBookAction(index)
	elif string == 'l':
		listBooksAction(index)
	elif string == 'q':
		quitAction(index)
	else:
		print ('Please enter a valid option')
def main():
	index = createIndex();
	display = formatMenu()
	prompt = formatMenuPrompt()
	while 1:
		print (display)
		input1 = getUserChoice(prompt)
		applyAction(index, input1)
if __name__ == '__main__':
	main()
	


