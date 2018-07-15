import pygame

class Cloud:

	def __init__(self,  x, y, width, height):

		self.mX = x
		self.mY = y
		self.mWidth = width
		self.mHeight = height

	def draw(self, surface):

		cloudRect = (self.mX, self.mY, self.mWidth, self.mHeight)
		pygame.draw.ellipse(surface, (255, 255, 255), cloudRect, 0)