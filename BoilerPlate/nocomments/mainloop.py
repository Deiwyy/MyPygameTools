import pygame
from window import Window
import sys
from scene import Scene



class Mainloop:
	def __init__(self):
		self.clock = pygame.time.Clock()
		self.FPS = 60
		self.window = Window(800, 600)
		self.running = True
		self.current_scene_name = 'main'
		self.scenes = {'main': Scene(self)}

	def main(self):
		while self.running:
			delta = self.clock.tick(self.FPS) * 0.001
			events = pygame.event.get()
			keys_pressed = pygame.key.get_pressed()
			self.scenes[self.current_scene_name].update(events, keys_pressed, delta)
			self.scenes[self.current_scene_name].draw()
			self.window.clear([255, 255, 255])
			self.window.draw(self.scenes[self.current_scene_name].get_surfaces())
		pygame.quit()
		sys.exit(0)

	def stop(self):
		self.running = False

	def change_scene(self, scene):
		self.current_scene_name = scene

	def get_window(self):
		return self.window


if __name__ == '__main__':
	ml = Mainloop()
	ml.main()