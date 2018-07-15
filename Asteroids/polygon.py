
import rotatable
import pygame
import math

class Polygon(rotatable.Rotatable):

	def __init__(self, x , y, dx, dy, rotation, world_width,world_height):

		rotatable.Rotatable.__init__(self, x, y, dx, dy, rotation, world_width, world_height )
		self.mOriginalPolygon = []
		self.mColor = (255,255,255)

	def getPolygon(self):
		return self.mOriginalPolygon
	def getColor(self):
		return self.mColor
	def getRadius(self):
		distance = []
		if len(self.mOriginalPolygon) != 0:
			for point in self.mOriginalPolygon:
				dx = point[0] 
				dy = point[1] 
				point_distance = math.sqrt(dx * dx + dy * dy)
				distance.append(point_distance)
			average = sum(distance)/len(distance)
			return average
		else:
			return 0
	def setPolygon(self, point_list):
		self.mOriginalPolygon = point_list
	def setColor(self, color):
		self.mColor = color
	def draw(self, surface):
		new_polygon = self.rotateAndTranslatePointList(self.mOriginalPolygon)
		pygame.draw.polygon(surface, self.mColor, new_polygon, 1)
