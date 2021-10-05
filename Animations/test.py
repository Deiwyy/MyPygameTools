import pygame
from animation import Animation

SCREEN = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
FPS = 60

anim_delta_dependent = Animation(1)
anim_delta_dependent.load_frames_from_folder('testframes')

# anim_frame_dependant = Animation(60, True)
# anim_frame_dependant.load_frames_from_folder('testframes')

while True:
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			pygame.quit()
			exit(0)
	delta = clock.tick(FPS) * 0.001

	current_frame = anim_delta_dependent.update(delta)
	# current_frame = anim_frame_dependant.update()
	
	SCREEN.blit(pygame.transform.scale(current_frame, (600, 600)), (0, 0))
	pygame.display.update()
