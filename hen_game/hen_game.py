import sys

import pygame

def run_game():
	# Initialize game and create a screen object.
	pygame.init()
	screen = pygame.display.set_mode((1200, 700))
	pygame.display.set_caption("Collect the Eggs!")

	# Set the background color.
	bg_color = (0, 70, 0)
	screen.fill(bg_color)

	while True:
		# Watch for keyboard and mouse events.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(0)
		# Redraw the screen during each pass through the loop.
				
		# Make the most recently drawn screen visible.
		pygame.display.flip()

		

		


run_game()		