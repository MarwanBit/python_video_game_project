import pygame


'''
SOURCES FOR THINGS USED IN THIS PROJECT..............


Link for Music Used:
https://downloads.khinsider.com/game-soundtracks/album/pokemon-firered-leafgreen-enhanced-soundtrack/06%2520Pallet%2520Town.mp3

Link for Sprites Used:
'''


'''
This python file contains a bunch of global variables used throughout the 
game...
'''

'''
This section is for initializing things...
'''
pygame.font.init()

#Our Chosen physics constants....
delta_t = 0.1

#Sets the default size of the program to the size of the start_screen....
default_size = pygame.image.load('assets/images/start_screen.jpg').get_size()

'''
This Section of the condig file deals with all things start_screen_related
'''
font = pygame.font.Font(None, 36)
new_game_text = font.render('New Game', 1, (255,255,255))
load_game_text = font.render('Load Game', 1, (255,255,255))
title_font = font.render('Clear Skies', 1, (255,255,255))

start_screen_entity_dict = {
	'start_screen': (pygame.image.load('assets/images/start_screen.jpg'),(0,0)),
	'new_game_text': (new_game_text, (200,300)),
	'load_game_text' : (load_game_text, (200,200)),
	'title_font': (title_font, (200, 100)),
	}

start_screen_sound_dict = {'start_screen': 'assets/music/start_screen.wav'}


'''
This Section of the config file deals with all things test_field related...
'''
test_field_entity_dict = {
	'field_background' : (pygame.image.load('assets/images/fire_red_map.jpg'),(0,0))
}
test_field_sound_dict = {'idle_music': 'assets/music/pallet_town.wav'}


'''
This Section of the config file deals with all things player related......
'''
player_image_list_north = [
'assets/images/red_facing_north.png', 'assets/images/red_facing_north_2.png', 'assets/images/red_facing_north_3.png'
]
player_image_list_south = [
'assets/images/red_facing_south.png', 'assets/images/red_facing_south_2.png', 'assets/images/red_facing_south_3.png'
]
player_image_list_left = [
'assets/images/red_facing_left.png', 'assets/images/red_facing_left_2.png', 'assets/images/red_facing_left_3.png'
]
player_image_list_right = [
'assets/images/red_facing_right.png', 'assets/images/red_facing_right_2.png', 'assets/images/red_facing_right_3.png'

]
