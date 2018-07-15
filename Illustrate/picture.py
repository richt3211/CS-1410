import pygame
import sun
import rect
import tree
import person
import cloud
import blanket

class Picture:

	def __init__(self, width, height):
		self.mWidth = width
		self.mHeight = height

		self.mSun = sun.Sun( (247, 238, 101), 175, 125, 50)
		self.mSky = rect.Rect((101, 233, 247), 0, 0, 900, 450)
		self.mGrass = rect.Rect((86, 219, 110), 0, 450, 900, 350)
		self.mTree1 = tree.Tree((143, 102, 26), (71, 153, 17), 650, 325, 75, 125)
		self.mTree2 = tree.Tree((168, 141, 50), (168, 50, 100), 800, 375, 50, 75)
		adult = 'adult'
		child = 'child'
		self.mParent1 = person.Person(adult, 225, 300 )
		self.mParent2 = person.Person(adult, 100, 300)
		self.mChild1 = person.Person(child, 350, 350)
		self.mChild2 = person.Person(child, 450, 350)
		self.mChild3 = person.Person(child, 550, 350)
		self.mCloud1 = cloud.Cloud(400, 50, 150, 100)
		self.mCloud2 = cloud.Cloud(650, 70, 200, 100)
		self.mBlanket = blanket.Blanket((219, 50, 107), 100, 500, 350, 150)
		return
	def draw (self,surface):

		self.mSky.draw(surface)
		self.mGrass.draw(surface)
		self.mSun.draw(surface)
		self.mTree1.draw(surface)
		self.mTree2.draw(surface)
		self.mParent1.draw(surface)
		self.mParent2.draw(surface)
		self.mChild1.draw(surface)
		self.mChild2.draw(surface)
		self.mChild3.draw(surface)
		self.mCloud1.draw(surface)
		self.mCloud2.draw(surface)
		self.mBlanket.draw(surface)

		