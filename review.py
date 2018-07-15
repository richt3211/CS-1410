import math

def createEmptyDictionary():
	return {}
def addItem(dict, key, value):
	dict[key] = value
	return
def delItem(dict, key):
	del dict[key]
	return
def keysOf(dict):
	list = []
	for x in dict:
		list.append(x)
	return list
def valuesOf(dict):
	list = []
	for x in dict:
		list.append(dict[x])
	return list
def unzip (dict):

def existsP(dict, key):
	if key in dict:
		return True
	else:
		return False

class C:

	def __init__(self, x , y):
		self.mX = 0
		self.mY = 0
		self.setX(x)
		self.setY(y)

		return
	def setX(self, x):
		if x <= 0:
			self.mX = x
		else:
			print ("Please enter a valid point")
		return
	def setY (self, y):
		if y >= 0:
			self.mY = y
		else:
			print ("Please enter a valid point")
		return
	def getX(self):
		return self.mX
	def getY(self):
		return self.mY
	def getDist(self):
		distance = math.sqrt(self.mX ** 2 + self.mY ** 2 )
		return distance