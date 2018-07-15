import pygame

class Blanket:

	def __init__(self, color, x, y, width, height):

		self.mColor = color
		self.mX = x
		self.mY = y
		self.mWidth = width
		self.mHeight = height

	def draw(self, surface):

		rect = pygame.Rect(self.mX, self.mY, self.mWidth, self.mHeight)

		pygame.draw.rect(surface, self.mColor, rect, 0)

		xRatio = self.mWidth // 5
		yRatio = self.mHeight // 5
		numCirc = self.mWidth // 5 + self.mHeight // 5

		for i in range(6):

			for x in range(6):

				pygame.draw.circle(surface, (255, 255, 255) , (self.mX + xRatio * i, self.mY + yRatio  * x), 2, 0)
