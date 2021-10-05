import pygame

class Window:
	def __init__(self, width, height, title='My Game'):
		self.width = width
		self.height = height
		self.title = title
		self.window = pygame.display.set_mode((width, height))

	def get_height(self):
		return self.height

	def get_width(self):
		return self.height

	def get_size(self):
		return (self.width, self.height)

	def get(self):
		return self.window

	def draw(self, surfaces):
		if surfaces:
			if type(surfaces) == dict:
				surfaces = surfaces.values()
			elif type(surfaces) == pygame.Surface:
				surfaces = [surfaces]
			for s in surfaces:
				self.window.blit(s, (s.get_rect().x, s.get_rect().y))

	def clear(self, color):
		self.window.fill(color)
		pygame.display.update()