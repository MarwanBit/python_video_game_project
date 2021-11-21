import pygame

import sys

from screen import Display

from tracker import Tracker

from scene import Scene, Background

import config

from player import Player


#This Block of Code Initializes all objects used in our game...
tracker = Tracker() #Create the obj which tracks everything...	
display = Display(config.default_size) #Initialize our Display...
display.init_screen() #initialize the screen...
#Initialize Mixer...
pygame.mixer.init()
#Creates our background object...
background = Background(display)
#fills our background with the wanted color...
background.fill(background.display.color)
#Create our Initial Scene....
start_scene = Scene(
	background, display, config.start_screen_entity_dict, config.start_screen_sound_dict)
#Adds the start_scene flag to tracker....
tracker.append_scene_list(start_scene)

#Adds the test_field_scene
test_scene = Scene(
	background,display, config.test_field_entity_dict, config.test_field_sound_dict)
tracker.append_scene_list(test_scene)

#Player object....
player = Player(
	config.player_image_list_north, config.player_image_list_south,
	config.player_image_list_left, config.player_image_list_right,
	background
	)


#Set start_scenes flag to true since this is just the start of the game...
start_scene.activate_scene()


'''
Below we create the event loop which manages the game....
'''
while tracker.game_active:

	#Iterate through all game events and update stuff frame by frame...
	for event in pygame.event.get():
		
		#If they click the exit button exit...
		if event.type == pygame.QUIT:
			tracker.game_active = False #Redundant but want to take adv of tracker
		elif event.type == pygame.KEYDOWN:

			if event.key == pygame.K_SPACE:
				if start_scene.flag == True:
					test_scene.flag = True 
					tracker.player_visible = True
					start_scene.flag = False
					start_scene.stop_sounds()

			elif event.key == pygame.K_UP:
				player.set_vel(0,-player.character_speed)
				player.moving_up = True	
				player.moving_down = False 
				player.moving_right = False 
				player.moving_left = False
				player.update_direction('north')
			elif event.key == pygame.K_DOWN:
				player.set_vel(0,player.character_speed)
				player.moving_down = True
				player.moving_up = False 
				player.moving_right = False 
				player.moving_left = False
				player.update_direction('south')	
			elif event.key == pygame.K_RIGHT:
				player.set_vel(player.character_speed, 0)
				player.moving_right = True
				player.moving_up = False 
				player.moving_down = False 
				player.moving_left = False
				player.update_direction('right')	
			elif event.key == pygame.K_LEFT:
				player.set_vel(-player.character_speed, 0)
				player.moving_left = True
				player.moving_up = False 
				player.moving_right = False 
				player.moving_down = False	
				player.update_direction('left')


		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_UP and player.moving_up:
				player.set_vel(0,0)
			elif event.key == pygame.K_DOWN and player.moving_down:
				player.set_vel(0,0)
			elif event.key == pygame.K_LEFT and player.moving_left:
				player.set_vel(0,0) 
			elif event.key == pygame.K_RIGHT and player.moving_right:
				player.set_vel(0,0)


		
		






	#iterates through the scene flags and update whichever one is true...
	for scene in tracker.scene_list:
		#if this scene flag is the one that is on....
		if scene.flag:
			scene.show()

	#After this we'll unclude the logic for updating our character/trainer....
	if tracker.player_visible:
		player.update_pos(config.delta_t)
		player.draw()


	#Update the Screen with all changes...
	display.screen.blit(background,(0,0))
	display.flip()