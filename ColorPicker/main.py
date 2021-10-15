import pygame
import pyperclip
import tkinter as tk
import tkinter, tkinter.messagebox
pygame.init()

ALLOWED_FILE_TYPES = ('jpg', 'png')
CURRENT_SPRITE = None
WINDOW = pygame.display.set_mode((600, 600))
FONT = pygame.font.SysFont('Calibri', 32)
NO_SPRITE_MESSAGE = FONT.render('No image loaded. Drag and drop one here', True, (0, 0, 0))

def main():
	global CURRENT_SPRITE
	while True:
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				pygame.quit()
				exit(0)
			if e.type == pygame.DROPFILE:
				CURRENT_SPRITE = load_sprite(e.file)
			if e.type == pygame.MOUSEBUTTONDOWN:
				if e.button == 1:
					get_pixel_rgb()
		draw()

def draw():
	WINDOW.fill((255, 255, 255))
	try:
		WINDOW.blit(CURRENT_SPRITE, (0, 0))
	except TypeError:
		WINDOW.blit(NO_SPRITE_MESSAGE, (0, 0))		
	pygame.display.update()

def load_sprite(filename):
	sprite = None
	for i in ALLOWED_FILE_TYPES:
		if filename.lower().endswith(i):
			sprite = pygame.image.load(filename)
			set_window_to_sprite_size(sprite)
	return sprite

def set_window_to_sprite_size(sprite):
	WINDOW = pygame.display.set_mode((sprite.get_rect().width, sprite.get_rect().height))

def get_pixel_rgb():
	mp = pygame.mouse.get_pos()
	if CURRENT_SPRITE:
		pyperclip.copy(str(CURRENT_SPRITE.get_at((mp[0], mp[1]))[0:3]))
		showMsgBox(CURRENT_SPRITE.get_at((mp[0], mp[1]))[0:3])

def showMsgBox(text):
    root = tkinter.Tk()
    root.withdraw()
    tkinter.messagebox.showinfo('Copied', f'Color {text} copied')
    root.destroy()

if __name__ == '__main__':
	main()
