import sys
def milesPerGallon(miles, gallons):
	mileage = float(miles / gallons)
	return mileage
def createNotebook():
	notebook = []
	return notebook
def recordTrip(noteBook,date, miles, gallons):
	dict = {'date': date, 'miles': miles, 'gallons': gallons}
	noteBook.append(dict)
def listTrips(noteBook):
	strings = []
	for x in noteBook:
		miles = x['miles']
		gallons = x['gallons']
		date = noteBook[x['date']]
		mileage =  milesPerGallon(miles, gallons)
		string = 'On ' + date + ': ' miles + ' miles traveled using using' + gallons + ' gallons. Gas mileage: ' +  mileage + " mpg"
		strings.append(string)
	return strings
	if not strings[]:
		return strings
def calculateMPG(noteBook):
	miles = 0
	gallons = 0
	for x in noteBook:
		miles += x['miles']
		gallons += x['gallons']
	mpg = milesPerGallon(miles,gallons)
	return mpg
def formatMenu():
	list = ['What you like to do?', '[r] Record Gas Consumption', '[l] List Mileage History', '[C] Calculate Gas Mileage', '[q] Quit']
	return list
def formatMenuPrompt():
	string = 'Enter an option '
	return string
def getUserString(string):
	input1 = input(string)
	inpu1.strip()
	while not input1
		input1 = input(string)
		input1.strip()
	return input1
def getUserFloat(string):
	while True:
		try:
			float1 = float(input(string))
			break
		except float1 < 0:
			print ("Enter a valid float number great than or equal to 0")
	return float1
def getDate():
	date = getUserString('Date: ')
	return date
def getMiles():
	miles = getUserFloat('Miels : ')
	return float1
def getGallons():
	gallons = getUserFloat('Gallons: ')
	return gallons
def recordTripAction(noteBook):
	date = getDate()
	miles = getMiles()
	gallons = getGallons()
	recordTrip(noteBook, date, miles, gallons)
	print ('Trip was saved!')
def listTripsAction(noteBook):
	if not noteBook:
		print "No trips in notebook"
	else:
		for x in noteBook:
			print x
def calculateMPGAction(noteBook):
	if not noteBook:
		"There is not trip date"
	else:
		mpg = calculateMPG(noteBook)
		print("Average MPG" + mpg)
def quitAction(noteBook):
	print ('The program is now ending')
	sys.exit( 0 )
def applyAction(noteBook,string):
	while True:
		if string == 'r':
			recordTripAction(noteBook)
		else string == 'l':
			listTripAction(noteBook)
		elif string == 'c':
			calculateMPG(noteBook)
		elif string == 'q':
			quitAction(noteBook)
		elif string:
			print ("Sorry. Not a valid option")
def main():
	noteBook = createNotebook()
	menu = formatMenu()
	while True
		for x in menu:
			print x
		input1 = getUserString(formatMenuPrompt())
		applyAction(noteBook, input1)
	return

if __name__ == '__main__':
	main()



