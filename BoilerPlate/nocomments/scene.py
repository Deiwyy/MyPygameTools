import pygame


class Scene:
	def __init__(self, loop):
		self.loop = loop
		self.surfaces = [pygame.Surface((800, 600))]

	def update(self, events, keys_pressed, delta):
		for e in events:
			if e.type == pygame.QUIT:
				self.loop.stop()

	def get_surfaces(self):
		return self.surfaces

	def draw(self):
		pass