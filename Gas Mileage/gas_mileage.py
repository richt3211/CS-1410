import sys
def milesPerGallon(miles, gallons):
	if miles == 0 or gallons == 0:
		return 0.0
	else:
		mileage = (float(miles) / float(gallons))
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
		date = x['date']
		mileage =  milesPerGallon(miles, gallons)
		string = 'On ' + date + ': ' + str(miles) + ' miles traveled using using' + str(gallons) + ' gallons. Gas mileage: ' +  str(mileage) + " mpg"
		strings.append(string)
	return strings
	if not strings:
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
	string = 'Enter an option: '
	return string
def getUserString(string):
	input1 = input(string)
	input1 = input1.strip()
	while not input1:
		input1 = input(string)
		input1 = input1.strip()
	return input1
def getUserFloat(string):
	while True:
		try:
			float1 = input(string)
			float1 = float(float1)
			if float1 > 0.0:
				return float1
			else:
				print ("Enter a valid float number greater than or equal to 0")
		except:
			print ("Enter a valid float number greater than or equal to 0")
def getDate():
	date = getUserString('Date: ')
	return date
def getMiles():
	miles = getUserFloat('Miles : ')
	return miles
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
	trips = listTrips(noteBook)
	if not trips:
		print ("There are no trips")
	for x in trips:
		print (x)

def calculateMPGAction(noteBook):
	if not noteBook:
		print ("There is no trip date")
	else:
		mpg = calculateMPG(noteBook)
		print("Average MPG" + str(mpg))
def quitAction(noteBook):
	print ('The program is now ending')
	sys.exit( 0 )
def applyAction(noteBook,string):
	if string == 'r':
		recordTripAction(noteBook)
	elif string == 'l':
		listTripsAction(noteBook)
	elif string == 'c':
		calculateMPGAction(noteBook)
	elif string == 'q':
		quitAction(noteBook)
	elif string:
		print ("Sorry. Not a valid option")
def main():
	noteBook = createNotebook()
	menu = formatMenu()
	while True:
		for x in menu:
			print (x)
		input1 = getUserString(formatMenuPrompt())
		applyAction(noteBook, input1)
	return

if __name__ == '__main__':
	main()



