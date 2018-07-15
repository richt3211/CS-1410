# Richard Timpson
# Tuesday Thursday 9:00 - 10:15 AM
# CS 1410


class CaloricBalance:
	
	def __init__(self, gender, age, height, weight):
		self.mWeight = weight
		self.mBalance = - (self.getBMR(gender,age,height,weight))
	def getBMR(self, gender, age, height, weight):
		if gender == 'm':
			bmr = 66 + (12.7 * height) + (6.23 * weight) - (6.8 * age)
			return bmr
		elif gender == 'f':
			bmr = 655 + (4.7 * height) + (4.35 * weight) - (4.7 * age)
			return bmr
		else:
			return 0
	def getBalance(self):
		return self.mBalance
	def recordActivity(self, caloric_burn, minutes):
		caloric_bpm = (caloric_burn * self.mWeight) * minutes
		self.mBalance -= caloric_bpm
	def eatFood(self, calories):
		self.mBalance += calories

