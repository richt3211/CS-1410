import pygame

class Tree:

	def __init__(self, barkColor, treeColor, x, y, width, height):

		self.mBarkColor = barkColor
		self.mTreeColor = treeColor
		self.mX = x
		self.mY = y
		self.mWidth = width
		self.mHeight = height

	def draw (self, surface):

		treeWidth = self.mWidth * 2
		treeHeight = self.mHeight + (self.mHeight /5)
		treeX = self.mX - self.mWidth / 2
		treeY = self.mY - self.mHeight

		barkRect = pygame.Rect(self.mX, self.mY, self.mWidth, self.mHeight)
		treeRect = pygame.Rect(treeX, treeY, treeWidth, treeHeight)
		pygame.draw.rect(surface, self.mBarkColor, barkRect, 0)
		pygame.draw.ellipse(surface, self.mTreeColor, treeRect, 0)