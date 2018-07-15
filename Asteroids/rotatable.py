import movable
import pygame
import math

class Rotatable(movable.Movable):

	def __init__(self, x, y, dx, dy, rotation, world_width, world_height):
		movable.Movable.__init__(self, x, y, dx, dy, world_width, world_height)
		self.mRotation = rotation
	def getRotation(self):
		return self.mRotation
	def rotate(self, delta_rotation):
		if delta_rotation >= 360:
			delta_rotation -= 360
		testRotation = self.mRotation + delta_rotation
		if testRotation >= 360:
			self.mRotation = testRotation - 360
		elif testRotation < 0:
			self.mRotation = testRotation + 360
		else:
			self.mRotation = testRotation
	def splitDeltaVIntoXAndY(self, rotation, delta_velocity):
		radian_rotation = math.radians(rotation)
		x = delta_velocity * math.cos(radian_rotation)
		y = delta_velocity * math.sin(radian_rotation)
		return x , y
	def accelerate(self, delta_velocity):
		dx, dy = self.splitDeltaVIntoXAndY(self.mRotation, delta_velocity)
		self.mDX += dx
		self.mDY += dy
		return
	def rotatePoint(self, x,y):
		d = math.sqrt( x * x + y * y)
		gamma = math.atan2( y, x)
		gamma += math.radians(self.mRotation)
		newX = d * math.cos(gamma)
		newY = d * math.sin(gamma)
		return newX, newY
	def translatePoint(self, x,y):
		newX = x + self.mX
		newY = y + self.mY
		return newX, newY
	def rotateAndTranslatePoint(self, x ,y):
		testX, testY = self.rotatePoint(x,y)
		newX, newY = self.translatePoint(testX, testY)
		return newX, newY
	def rotateAndTranslatePointList(self, point_list):
		newList = []
		for point in point_list:
			newPoint = self.rotateAndTranslatePoint(point[0], point[1])
			newList.append(newPoint)
		return newList