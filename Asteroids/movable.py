import pygame
import math
class Movable:

	def __init__(self, x, y, dx, dy, world_width, world_height):

		self.mX = x
		self.mY = y
		self.mDX = dx
		self.mDY = dy
		self.mWorldWidth = world_width
		self.mWorldHeight = world_height
		self.mActive = True

	def getX(self):
		return self.mX
	def getY(self):
		return self.mY
	def getDX(self):
		return self.mDX
	def getDY(self):
		return self.mDY
	def getWorldWidth(self):
		return self.mWorldWidth
	def getWorldHeight(self):
		return self.mWorldHeight
	def getActive(self):
		return self.mActive
	def setActive(self, active):
		self.mActive = active
	def move(self, dt):
		testX = self.mX + self.mDX * dt
		testY = self.mY + self.mDY * dt
		if testX >= self.mWorldWidth: 
			self.mX = testX - self.mWorldWidth
		elif testX < 0:
			self.mX = self.mWorldWidth + testX
		else:
			self.mX = testX

		if testY >= self.mWorldHeight: 
			self.mY = testY - self.mWorldHeight
		elif testY < 0:
			self.mY = self.mWorldHeight + testY
		else:
			self.mY = testY
	def hits(self, other):
		dx = self.mX - other.mX
		dy = self.mY - other.mY
		distance = math.sqrt(dx** 2 + dy **2)
		col_distance = self.getRadius() + other.getRadius()
		if distance <= col_distance:
			return True 
		else:
			return False
	def getRadius(self):
		raise NotImplementedError
	def accelerate (self, delta_velocity):
		raise NotImplementedError
	def evolve (self, dt):
		raise NotImplementedError
	def draw (self, surface):
		raise NotImplementedError
	
				