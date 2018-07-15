import pygame

class Person:

	def __init__(self,  age, x, y):

		self.mAge = age
		self.mX = x
		self.mY = y

	def draw(self, surface):

		if self.mAge == 'adult':
			radius = 30
			white = (255, 255, 
				255)
			#head
			circlePosition = (self.mX, self.mY)
			#body
			bodyPositionStart = (self.mX, self.mY + radius)
			bodyPositionEnd = (self.mX, self.mY + radius + 75)
			#arm
			armPositionStart = (self.mX - 40, self.mY + radius + 37)
			armPositionEnd = (self.mX + 40, self.mY + radius + 37)
			#legs
			leg1Position = (self.mX - 30, self.mY + radius + 120)
			leg2Position = (self.mX + 30, self.mY + radius + 120)
			#eyes
			eye1Position = (self.mX - 10, self.mY - 10)
			eye2Position = (self.mX + 10, self.mY - 10)
			#mouth
			mouth = pygame.Rect(self.mX - 10, self.mY, 20, 10)


			#head
			pygame.draw.circle(surface, white, (circlePosition) , 30, 3 )

			#body
			pygame.draw.line(surface, white, bodyPositionStart, bodyPositionEnd, 2)

			#arm
			pygame.draw.line(surface, white, armPositionStart, armPositionEnd, 2)

			#legs
			pygame.draw.line(surface, white, bodyPositionEnd, leg1Position, 2)
			pygame.draw.line(surface, white, bodyPositionEnd, leg2Position, 2)

			#eyes
			pygame.draw.circle(surface, white, eye1Position, 5, 1)
			pygame.draw.circle(surface, white, eye2Position, 5, 1)

			#mouth
			pygame.draw.arc(surface, white, mouth, 3.5, 6.3)

		elif self.mAge == 'child':
			radius = 20
			white = (255, 255, 
				255)
			#head
			circlePosition = (self.mX, self.mY)
			#body
			bodyPositionStart = (self.mX, self.mY + radius)
			bodyPositionEnd = (self.mX, self.mY + radius + 37)
			#arm
			armPositionStart = (self.mX - 30, self.mY + radius + 20)
			armPositionEnd = (self.mX + 30, self.mY + radius + 20)
			#legs
			leg1Position = (self.mX - 30, self.mY + radius + 80)
			leg2Position = (self.mX + 30, self.mY + radius + 80)
			#eyes
			eye1Position = (self.mX - 5, self.mY - 7)
			eye2Position = (self.mX + 5, self.mY - 7)
			#mouth
			mouth = pygame.Rect(self.mX - 7, self.mY, 15, 7)


			#head
			pygame.draw.circle(surface, white, circlePosition , radius, 3 )

			#body
			pygame.draw.line(surface, white, bodyPositionStart, bodyPositionEnd, 2)

			#arm
			pygame.draw.line(surface, white, armPositionStart, armPositionEnd, 2)

			#legs
			pygame.draw.line(surface, white, bodyPositionEnd, leg1Position, 2)
			pygame.draw.line(surface, white, bodyPositionEnd, leg2Position, 2)

			#eyes
			pygame.draw.circle(surface, white, eye1Position, 3, 1)
			pygame.draw.circle(surface, white, eye2Position, 3, 1)

			#mouth
			pygame.draw.arc(surface, white, mouth, 3.5, 6.3)

			return
