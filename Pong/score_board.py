import pygame
import text

class ScoreBoard:

	def __init__(self, x, y, width, height):

		self.mX = x
		self.mY = y
		self.mWidth = width
		self.mHeight = height
		self.mLeftScore = 0
		self.mRightScore = 0
		self.mServeStatus = 1

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
		if self.mServeStatus == 3 or self.mServeStatus == 4:
			return True
		else:
			return False
	def scoreLeft(self):
		game = self.isGameOver()
		if game == False:
			self.mLeftScore += 1
			if self.mLeftScore == 9:
				self.mServeStatus = 3
	def scoreRight(self):
		game = self.isGameOver()
		if game == False:
			self.mRightScore += 1
			if self.mRightScore == 9:
				self.mServeStatus = 4
	def swapServe(self):
		game = self.isGameOver()
		if game == False:
			if self.mServeStatus == 2:
				self.mServeStatus = 1
			elif self.mServeStatus == 1:
				self.mServeStatus = 2
	def draw(self, surface):
		leftscore = str(self.getLeftScore())
		rightscore = str(self.getRightScore())
		leftText = text.Text(leftscore, self.mX, self.mY)
		leftText.setColor((255,255,255))
		leftText.draw(surface)
		rightText = text.Text(rightscore, self.mX + self.mWidth , self.mY)	
		rightText.setColor((255,255,255))
		rightText.draw(surface)
