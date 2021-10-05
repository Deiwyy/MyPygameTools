import pygame

# Basic example scene

# Steps to how scenes work:
# 1. The scene is initialized (Aka the scene object is created in the mainloop)
# Every frame:
# 2. update() is called
# 3. draw() is called
# 4. get_surfaces() is called

class Scene:
	def __init__(self, loop):
		self.loop = loop

		# You don't directly draw to the screen, but on surfaces. They should be in a list or a dict, but you can have just one surface
		# You still can draw to the screen instead of drawing to a surface though. Get the screen (what pygame.display.set_mode returns) by doing self.loop.get_window().get()  
		# You could do something like this:
		# self.window = self.loop.get_window()
		self.surfaces = [pygame.Surface((800, 600))]

	def update(self, events, keys_pressed, delta):
		for e in events:
			if e.type == pygame.QUIT:
				self.loop.stop()
			# All of your logic goes here, called every frame
			# events arg is a list of events returned by pygame.event.get() called in the mainloop
			# keys_pressed is a list of keys that are being pressed returned by pygame.key.get_pressed()

	def get_surfaces(self):
		# This function is necessary, its called every frame and should return the list of the surfaces you want to draw
		return self.surfaces

	def draw(self):
		# This is where you draw to your surfaces
		pass