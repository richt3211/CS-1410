import pygame

class Sun:

	def __init__(self, color, x, y, radius):
		self.mColor = color
		self.mX = x
		self.mY = y
		self.mRadius = radius

	def draw(self, surface):

		pygame.draw.circle(surface, (self.mColor), (self.mX , self.mY), self.mRadius, 0)
