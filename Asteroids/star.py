import circle
import random
class Star(circle.Circle):

	def __init__(self, x, y, world_width, world_height):
		circle.Circle.__init__(self,x, y, 0 , 0, 0, 2, world_width, world_height)
		brightness = random.randrange(0, 255)
		self.mBrightness = brightness
		self.mColor = (self.mBrightness, self.mBrightness, self.mBrightness)
	def getBrightness(self):
		return self.mBrightness
	def setBrightness(self, brightness):
		test_brightness = self.mBrightness + brightness
		if test_brightness <= 255 and test_brightness >=0:
			self.mBrightness = test_brightness
			self.mColor = (self.mBrightness, self.mBrightness, self.mBrightness)
	def evolve(self, dt):
		brightness = random.randrange(0,2)
		if brightness == 0:
			self.setBrightness(10)
		elif brightness == 1:
			self.setBrightness(-10)
		else:
			return