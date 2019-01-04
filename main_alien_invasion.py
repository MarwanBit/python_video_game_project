import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
	#Initialize game, settings, and create a screen object!
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption(ai_settings.screen_caption)

	#This creates a ship
	ship = Ship(screen)

	#This sets the background color
	bg_color = (230, 230, 230)

	#The main game loop
	while True:

		#Look for keyboard and mouse events/ inputs
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		#This draws the ship
		ship.blitme()

		#This line redraws the screen for each iteration in the loop
		screen.fill(ai_settings.bg_color)

		#Make the most recently drawn screen visible
		pygame.display.flip()

run_game()
