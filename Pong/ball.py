import pygame
import random
class Ball:
	
	def __init__(self, size, min_x, max_x, min_y, max_y, left_paddle_x, right_paddle_x):
		self.mX = min_x
		self.mY = min_y
		self.mSize = size
		self.mDX = 0
		self.mDY = 0
		self.mMinX = min_x
		self.mMaxX = max_x
		self.mMinY = min_y
		self.mMaxY = max_y
		self.mLeftPaddleX = left_paddle_x
		self.mLeftPaddleMinY = min_y
		self.mLeftPaddleMaxY = max_y
		self.mRightPaddleX = right_paddle_x
		self.mRightPaddleMinY = min_y
		self.mRightPaddleMaxY = max_y

	# Getters
	def getX(self):
		return self.mX
	def getY(self):
		return self.mY
	def getSize(self):
		return self.mSize
	def getDX(self):
		return self.mDX
	def getDY(self):
		return self.mDY
	def getMinX(self):
		return self.mMinX
	def getMaxX(self):
		return self.mMaxX
	def getMinY(self):
		return self.mMinY
	def getMaxY(self):
		return self.mMaxY
	def getLeftPaddleX(self):
		return self.mLeftPaddleX
	def getLeftPaddleMinY(self):
		return self.mLeftPaddleMinY
	def getLeftPaddleMaxY(self):
		return self.mLeftPaddleMaxY
	def getRightPaddleX(self):
		return self.mRightPaddleX
	def getRightPaddleMinY(self):
		return self.mRightPaddleMinY
	def getRightPaddleMaxY(self):
		return self.mRightPaddleMaxY

	#setters
	def setPosition(self, x, y):
		if (x + self.mSize <= self.mMaxX and x >= self.mMinX) and (y + self.mSize <= self.mMaxY and y >= self.mMinY) :
			self.mX = x
			self.mY = y
	def setSpeed(self, dX, dY):
		self.mDX = dX
		self.mDY = dY
	def setLeftPaddleY(self, min_Y, max_Y):
		if min_Y >= self.mMinY and max_Y <= self.mMaxY and min_Y < max_Y:
			self.mLeftPaddleMinY = min_Y
			self.mLeftPaddleMaxY = max_Y
	def setRightPaddleY(self, minimum_Y, max_Y):
		if minimum_Y >= self.mMinY and max_Y <= self.mMaxY and minimum_Y < max_Y:
			self.mRightPaddleMinY = minimum_Y
			self.mRightPaddleMaxY = max_Y
	#checkers
	def checkTop(self, new_y):
		if new_y < self.mMinY:
			self.mDY = -self.mDY
			new_y = 2 * self.mMinY - new_y
			return new_y
		else:
			return new_y	
	def checkBottom(self, new_y):
		if new_y + self.mSize > self.mMaxY:
			self.mDY = -self.mDY
			new_y = 2 * self.mMaxY - new_y - 2 * self.mSize
			return new_y
		else:
			return new_y	
	def checkLeft(self, new_x):
		if new_x < self.mMinX:
			self.mDX = 0 
			self.mDY = 0
			new_x = self.mMinX
			return new_x
		else:
			return new_x
	def checkRight(self,new_x):
		if new_x + self.mSize > self.mMaxX:
			self.mDX = 0 
			self.mDY = 0
			new_x = self.mMaxX - self.mSize
		return new_x
	def checkLeftPaddle(self, new_x, new_y):
		mid_y = (new_y + self.mY) / 2
		if mid_y <= self.mLeftPaddleMaxY and mid_y >= self.mLeftPaddleMinY and new_x <= self.mLeftPaddleX and self.mX >= self.mLeftPaddleX:
			new_x = self.mLeftPaddleX + self.mLeftPaddleX - new_x
			self.mDX = -self.mDX
			return new_x
		else:
			return new_x
	def checkRightPaddle(self,new_x, new_y):
		mid_y = (new_y + self.mY) / 2
		if mid_y <= self.mRightPaddleMaxY and mid_y >= self.mRightPaddleMinY and new_x + self.mSize >= self.mRightPaddleX and self.mX + self.mSize <= self.mRightPaddleX:
			new_x = self.mRightPaddleX * 2 - new_x - self.mSize * 2
			self.mDX = -self.mDX
			return new_x
		else:
			return new_x

	#movers
	def move (self,dt):
		new_x = self.mX + (self.mDX * dt)
		new_y = self.mY + (self.mDY * dt)
		new_y = self.checkTop(new_y)
		new_y = self.checkBottom(new_y)
		new_x = self.checkRight(new_x)
		new_x = self.checkLeft(new_x)
		new_x = self.checkRightPaddle(new_x, new_y)
		new_x = self.checkLeftPaddle(new_x, new_y)
		self.mX = new_x
		self.mY = new_y
	def serveLeft(self,x,min_y,max_y, min_dx, max_dx, min_dy,max_dy):
		self.mX = x
		self.mY = random.uniform(min_y, max_y)
		self.mDX = random.uniform(min_dx, max_dx)
		self.mDY = random.uniform(min_dy, max_dy)
	def serveRight(self,x,min_y,max_y, min_dx, max_dx, min_dy,max_dy):
		self.mX = x 
		self.mY = random.uniform(min_y, max_y)
		self.mDX = random.uniform(-min_dx,-max_dx)
		self.mDY = random.uniform(min_dy, max_dy)
	def draw(self, surface):
		rect = pygame.Rect(self.mX, self.mY, self.mSize, self.mSize)
		pygame.draw.rect(surface, (255 , 255, 255), rect)


