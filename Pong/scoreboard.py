import pygame

class ScoreBoard:

	def __init__(self, x, y, width, height):

		self.mX = x
		self.mY = y
		self.mWidth = width
		self.mHeight = height
		self.mLeftScore = 0
		self.mRightScore = 0
		self.mServeStatus

	def getX(self):
		return self.mX
	def getY(self):
		return self.mY
	def getWidth(self):
		return self.mWidth
	def getHeight(self):
		return self.mHeight
	def getLeftScore(self):
		return self.mLeftScore
	def getRightScore(self):
		return self.mRightScore
	def getServeStatus(self):
		return self.mServeStatus
	def isGameOver(self):

	def scoreLeft(self):

	def scoreRight(self):

	def swapServe(self):

	def draw(self, surface):
		