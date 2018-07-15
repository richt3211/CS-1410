import pygame

class Rect:

	def __init__(self, color, x, y, width, height):

		self.mColor = color
		self.mX = x
		self.mY = y
		self.mWidth = width
		self.mHeight = height
	def draw(self, surface):

		rect = pygame.Rect(self.mX, self.mY, self.mWidth, self.mHeight )
		pygame.draw.rect(surface, self.mColor, rect, 0 )
