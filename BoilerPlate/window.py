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
		# Returns the window itself (Window) what pygame.display.set_mode returns 
		return self.window

	def draw(self, surfaces):
		if surfaces:
			if type(surfaces) == dict:
				surfaces = surfaces.values()
			elif type(surfaces) == pygame.Surface:
				surfaces = [surfaces]
			for s in surfaces:
				self.window.blit(s, (s.get_rect().x, s.get_rect().y))
		pygame.display.update()

	def clear(self, color):
		# Clears the window / fills the window with a color
		self.window.fill(color)
