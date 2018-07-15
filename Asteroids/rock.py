import polygon
import random
import math
class Rock(polygon.Polygon):

	def __init__(self, x, y, world_width, world_height):
		rotation = random.uniform( 0, 359.9)
		polygon.Polygon.__init__(self, x, y, 0, 0, rotation, world_width, world_height)
		self.mSpinRate = random.uniform( -90, 90)
		velocity = random.randrange( 10,20)
		self.accelerate(velocity)
		self.setPolygon(self.createRandomPolygon(30, 6))

	def createRandomPolygon(self, radius, number_of_points):
		list = []
		dtheta = 360 / number_of_points
		theta = dtheta
		for x in range(number_of_points):
			side_len = random.uniform(.7, 1.3) * radius
			point = math.cos(math.radians(theta)) * side_len, math.sin(math.radians(theta)) * side_len
			theta += dtheta
			list.append(point)
		return list
	def getSpinRate(self):
		return self.mSpinRate
	def setSpinRate(self, spin_rate):
		self.mSpinRate = spin_rate
	def evolve(self, dt):
		self.rotateAndTranslatePointList(self.mOriginalPolygon)
		self.move(dt)
		self.rotate(self.mSpinRate * dt)
