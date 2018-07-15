import rock
import ship
import pygame
import random
import star

class Asteroids:

	def __init__(self, world_width, world_height):
		self.mWorldWidth = world_width
		self.mWorldHeight = world_height
		shipX = self.mWorldWidth / 2
		shipY = self.mWorldHeight / 2
		self.mShip = ship.Ship(shipX, shipY, self.mWorldWidth, self.mWorldHeight)
		self.mRocks = []
		self.mObjects = [self.mShip]
		# rocks
		for x in range(10):
			rockX = random.randrange(0, self.mWorldWidth)
			rockY = random.randrange(0 , self.mWorldHeight)
			rock1 = rock.Rock(rockX, rockY, world_width, world_height)
			self.mRocks.append(rock1)
			self.mObjects.append(rock1)
		#stars
		self.mStars = []
		for x in range(20):
			starX = random.randrange(0, self.mWorldWidth)
			starY = random.randrange(0, self.mWorldHeight)
			star1 = star.Star(starX, starY, self.mWorldWidth, self.mWorldHeight )
			self.mStars.append(star1)
			self.mObjects.append(star1)
		self.mBullets = []
		self.mGameLost = False
		self.mGameWon = False

	def getShip(self):
		return self.mShip
	def getRocks(self):
		return self.mRocks
	def getStars(self):
		return self.mStars
	def getBullets(self):
		return self.mBullets
	def getObjects(self):
		return self.mObjects
	def getWorldWidth(self):
		return self.mWorldWidth
	def getWorldHeight(self):
		return self.mWorldHeight
	def turnShipLeft(self, delta_rotation):
		self.mShip.rotate( - delta_rotation)
	def turnShipRight(self, delta_rotation):
		self.mShip.rotate(delta_rotation)
	def accelerateShip(self, delta_velocity):
		self.mShip.accelerate(delta_velocity)
	def fire(self):
		if len(self.mBullets) < 3:
			bullet = self.mShip.fire()
			self.mBullets.append(bullet)
			self.mObjects.append(bullet)
	def evolveAllObjects(self,dt):
		for x in self.mObjects:
			x.evolve(dt)
	def collideShipAndBullets(self):
		for bullet in self.mBullets:
			if self.mShip.hits(bullet):
				bullet.setActive(False)
				self.mShip.setActive(False)
				self.mGameLost = True
		return
	def collideShipAndRocks(self):
		for rock in self.mRocks:
			if self.mShip.hits(rock):
				self.mShip.setActive(False)
				# self.mRocks.remove(rock)
				self.mGameLost = True
		return
	def collideRocksAndBullets(self):
		for rock in self.mRocks:
			for bullet in self.mBullets:
				if rock.hits(bullet):
					rock.setActive(False)
					bullet.setActive(False)
					self.mBullets.remove(bullet)
					self.mRocks.remove(rock)

		return
	def removeInactiveObjects(self):
		for bullet in self.mBullets:
			if bullet.getAge() > 6:
				self.mBullets.remove(bullet)
		for object1 in self.mObjects:
			if object1.getActive() == False:
				self.mObjects.remove(object1)
		return
	def evolve(self,dt):
		self.evolveAllObjects(dt)
		self.collideShipAndBullets()
		self.collideShipAndRocks()
		self.collideRocksAndBullets()
		self.removeInactiveObjects()
	def draw(self, surface):
		surface.fill((0,0,0))
		for x in self.mObjects:
			if x.getActive():
				x.draw(surface)
		if self.mGameLost:
			print('You lost the game')
			pygame.font.init()
			font = pygame.font.SysFont('Comic Cans MS', 30)
			textsurface = font.render("You Lost", False, (255,255,255))
			surface.blit(textsurface, (self.mWorldWidth / 2,self.mWorldHeight / 2))
		if len(self.mRocks) == 0:
			pygame.font.init()
			font = pygame.font.SysFont('Comic Cans MS', 30)
			textsurface = font.render("You Won", False, (255,255,255))
			surface.blit(textsurface, (self.mWorldWidth /2, self.mWorldHeight/ 2))