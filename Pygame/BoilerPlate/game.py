import pygame



class Game:
	def __init__(self, loop):
		self.loop = loop

	def update(self, events, keys_pressed):
		for e in events:
			if e.type == pygame.QUIT:
				self.loop.stop()

	def draw(self, window):
		pass