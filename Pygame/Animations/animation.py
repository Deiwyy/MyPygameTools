import pygame
import math
import os

class Animation:
	ACCEPTED_FILE_EXT = ['png', 'jpg']
	def __init__(self, delay, update_per_frame_amount=False, frames=[]):
		'''
			:param float delay: Delay between changing animation frames
			:param bool update_per_frame_amount: If set to True, the next animation frame will play every `delay` times animation.update() calls. Otherwise it will play every `delay` seconds.
			:param list frames: You can pass a list of frames on creating the object. You could also use `load_frames_from_folder()` or `load_frames_from_list()` instead
		'''
		self.frames = frames
		self.delay = delay
		self.update_per_frame_amount = update_per_frame_amount
		self.frames_passed = 0
		self.time_passed = 0
		self.current_frame_index = 0

	def load_frames_from_folder(self, path):
		'''
			:param string path: A path to the folder containing all the frames used in the said animation. Make sure that the files are named in an alphabetical order according to how the animation is structured. Accepts only 'png' and 'jpg' files. 
		'''
		files = os.listdir(path)
		files.sort()
		frames = []
		for file in files:
			ext = file.split('.')[-1]
			if ext in self.ACCEPTED_FILE_EXT:
				frames.append(pygame.image.load(os.path.join(path, file)).convert())
		self.frames = frames

	def load_frames_from_list(self, l):
		'''
			:param list l: The list containing all the frames. 
		'''
		self.frames = l

	def update(self, delta=0):
		'''
			:param int delta: The delta time (time from last frame in miliseconds (delta = clock.tick(FPS) * 0.001)). The default value is always 0. You dont have to pass anything in if update_per_frame_amount == True
			:return Surface frame: Returns the current frame. This should be what you blit out to the screen.
			:return None none: Returns None if no animation frames are given
		'''
		if self.frames:
			if self.update_per_frame_amount:
				self.frames_passed += 1
				if self.frames_passed == math.floor(self.delay):
					self.frames_passed = 0
					self.current_frame_index += 1
			else:
				self.time_passed += delta
				if self.time_passed >= self.delay:
					self.current_frame_index += 1
					self.time_passed = 0
			if self.current_frame_index > len(self.frames)-1:
				self.current_frame_index = 0
			return self.frames[self.current_frame_index]
		return None

	def get_frames(self):
		'''
			:return list frames: Returns the list of frames loaded.
		'''
		return self.frames

	def get_current_frame(self):
		'''
			:return Surface frame: Returns the current frame without updating the animation
		'''
		return self.frames[self.current_frame_index]