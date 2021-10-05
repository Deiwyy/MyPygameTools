import pygame
from window import Window
from game import Game
import sys

class Mainloop:
	def __init__(self):
		self.clock = pygame.time.Clock()
		self.FPS = 60
		self.window = Window(800, 600)
		self.game = Game(self)
		self.running = True

	def main(self):
		while self.running:
			self.clock.tick(self.FPS)
			events = pygame.event.get()
			keys_pressed = pygame.key.get_pressed()
			self.game.update(events, keys_pressed)
			self.game.draw(self.window)

		pygame.quit()
		sys.exit(0)



	def stop(self):
		self.running = False


if __name__ == '__main__':
	ml = Mainloop()
	ml.main()