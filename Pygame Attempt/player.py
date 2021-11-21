import pygame


class Player(pygame.sprite.Sprite):
	'''
	This class manages the player, the players inventory, pokemon,
	there level, where they've been on the game, how many badges they have, etc....
	'''


	def __init__(
		self, 
		image_list_north, image_list_south, image_list_left, image_list_right, 
		background):
		'''
		Initializes our player, taking no arguments but creates the data members needed to
		keep track of everything....

		inputs:
			image: the actual image of the character.... (a file path to the image....)
		'''

		#call the parent constructor
		super().__init__()
		self.image_list_north = [pygame.image.load(image) for image in image_list_north]
		self.image_list_south = [pygame.image.load(image) for image in image_list_south]
		self.image_list_left = [pygame.image.load(image) for image in image_list_left]
		self.image_list_right = [pygame.image.load(image) for image in image_list_right]
		self.direction_dict = {
		'north': self.image_list_north,
		'south': self.image_list_south,
		'left': self.image_list_left,
		'right': self.image_list_right
		}
		self.current_image_index = 0
		self.current_direction = 'south'
		self.pos = [0,0] #x,y coord of our image....
		self.x_vel = 0 #initialize with 0 vel
		self.y_vel = 0
		#the Background that we are drawing everything on...
		self.background = background

		#here are movement flags for the player.
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		self.character_speed = 3


	def update_pos(self, delta_t):
		'''
		Takes our object and updates the new position using its velocity, given some delta_t...
		'''

		#Updates the position of the object using its velocity....
		self.pos[0] = self.pos[0] + self.x_vel*delta_t 
		self.pos[1] = self.pos[1] + self.y_vel*delta_t


	def set_vel(self, v_x, v_y):
		'''
		Takes our player and lets us set the players velocity....
		'''

		self.x_vel = v_x
		self.y_vel = v_y


	def update_image_index(self, index):
		'''
		Takes our player list and updates the index
		'''

		self.current_image_index = index


	def update_direction(self, direction):
		'''
		Updates the direction that you are facing if you aren't in that same direction already...
		if not it merely updates your step....
		'''

		if self.current_direction != direction:
			self.current_direction = direction 
			self.current_image_index = 0
		else:
			self.current_image_index = (self.current_image_index + 1) % len(self.image_list_north)

	def draw(self):
		'''
		Draws our character onto the background if the player is visible....
		'''

		#Draws our player onto the background....
		self.background.blit(
			self.direction_dict[self.current_direction][self.current_image_index], self.pos)

