import doctest


class Tracker():
	'''
	This class saves progress, keeps track of what event needs to occur,
	what is occuring currently, the current scene, etc, and a whole bunch of 
	conditionals...
	'''


	def __init__(self):
		'''
		Initializes the object and starts with a bunch of flags/conditionals
		needed for the game logic such as..... Game_Active, Inventory_Open, etc...

		inputs:
			None as of now........
		'''

		self.game_active = True
		#list of scenes 
		self.scene_list = []
		#Give the current scene 
		self.current_scene = ''
		#Make the player invisible initially....
		self.player_visible = False



	def append_scene_list(self, scene):
		'''
		puts the scene taken as input and puts it into our scene_list....
		'''

		self.scene_list.append(scene)


	def update_current_scene(self, scene_name):
		'''
		Given a scene_name this updates the current scene name of Tracker which we can use later on...
		'''

		self.current_scene = scene_name