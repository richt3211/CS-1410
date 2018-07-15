import polygon
import bullet

class Ship(polygon.Polygon):

	def __init__(self, x, y, world_width, world_height):

		polygon.Polygon.__init__(self, x, y, 0, 0, 0, world_width, world_height)
		self.setPolygon([(10,0), (-10,-10), (-10,10)])

	def evolve(self, dt):
		self.move(dt)
	def fire(self):
		pointx, pointy = self.mOriginalPolygon[0]
		print(pointx, pointy)
		tip = self.rotateAndTranslatePoint(pointx, pointy)
		print(tip[0], tip[1])
		bullet1 = bullet.Bullet(tip[0]	, tip[1], self.getDX(), self.getDY(), self.getRotation(), self.mWorldHeight, self.mWorldWidth)
		return bullet1

