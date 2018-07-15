# Richard Timpson
# Tuesday Thursday 9:00 - 10:15 AM
# CS 1410




import caloric_balance
import sys
def formatMenu():
	list = ['What would you like to do?', '[f] Record Food Consumption', '[a] Record Physical Activity', '[q] Quit']
	return list
def formatMenuPrompt():
	string = 'Enter an option: '
	return string
def formatActivityMenu():
	list =['Choose an activity to record', '[j] Jump Rope', '[r] Running', '[s] Sitting', '[w] Walking']
	return list
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
def createCaloricBalance():
	gender = getUserString('What is your gender?: ')
	age = getUserFloat("What is your age?: ")
	height = getUserFloat('What is your height?: ')
	weight = getUserFloat('What is your weight?: ')
	cb = caloric_balance.CaloricBalance(gender, age, height, weight)
	return cb
def recordActivityAction(caloricBalance):
	menu = formatActivityMenu()
	prompt = formatMenuPrompt()
	for x in menu:
		print (x)
	option = getUserString(prompt)
	if option == 'j':
		number = .08
	elif option == 'r':
		number = .095
	elif option == 's':
		number = 0.009
	elif option == 'w':
		number = 0.36
	else:
		print ("Please enter a valid option: ")
		return 0 
	minutes = getUserFloat("How many minutes did you exercise?: ")
	caloricBalance.recordActivity(number,minutes)
	string = 'Congratulations, your caloric balance is now ' + str(caloricBalance.getBalance())
	print (string)
	return
def eatFoodAction(caloricBalance):
	calories = getUserFloat("How many calories did you eat?: ")
	caloricBalance.eatFood(calories)
	string = 'Congratulations, your caloris balance is now ' + str(caloricBalance.getBalance())
	print (string)
def quitAction(caloricBalance):
	print ('The program is now ending')
	sys.exit( 0 )
def applyAction(caloricBalance, choice):
	if choice == 'f':
		eatFoodAction(caloricBalance)
	elif choice == 'a':
		recordActivityAction(caloricBalance)
	elif choice == 'q':
		quitAction(caloricBalance)
	else:
		print ("please enter a valid option: ")
def main():
	cb = createCaloricBalance()
	menu = formatMenu()
	prompt = formatMenuPrompt()
	while True:
		for x in menu:
			print (x)
		choice = getUserString(prompt)
		applyAction(cb, choice)
if __name__ == '__main__':
	main()







