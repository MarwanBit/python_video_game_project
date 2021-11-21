import pygame
import doctest
import config
import pygame.mixer


class Background(pygame.Surface):
	'''
	Creates the Background image which we then use to draw everything upon....
	'''


	def __init__(self, display):
		'''
		Instantantates a Background object which is the foundation for our pygame
		application....

		inputs:
			screen (the display/window/screen acting as the flooring for our program...)
		'''

		#Store a ref to the display in this class....
		self.display = display
		self.screen = self.display.screen
		#Create a Background class with the screen size the same as the one in the display....
		super().__init__(self.screen.get_size())


		


class Scene():
	'''
	Scene is a class which is a set of things to display to the screen
	given some conditional flag is true, for example the Start Screen is a 
	Scene which only displays when a flag is given...
	'''


	def __init__(self, background, display, entity_dict={}, sounds_dict={}):
		'''
		Creates our Scene object, taking in a entity list full of images with
		rects, colors, etc... which we can update so on and so forth... 
		'''

		#Automatically set the scene to false unless we update it...
		self.flag = False
		#create references to the background and displayes
		self.background = background
		self.display = display
		#Create a dict of entities... {entity_name, entity_obj}
		self.entity_dict = entity_dict
		#Create a dict of sounds... {sound_name: file_name...}
		self.sounds_dict = sounds_dict
		#A boolean telling if sound is playing or not...
		self.sound_playing = False


	def activate_scene(self):
		'''
		sets the Scene flag to true and thus displays the Scene when this is called...
		'''

		self.flag = True


	def deactivate_scene(self):
		'''
		sets the scene flag to false and thus undisplays the scene....
		'''

		self.flag = False


	def update_scene(self):
		'''
		Takes the scene and draws the updated version of the scene onto the display...
		'''

		for key in self.entity_dict.keys():
			#Draws each entity apart of the scene onto our screen object....
			self.background.blit(
				#This is the actual image obj...
				self.entity_dict[key][0],
				#This is the pos....
				self.entity_dict[key][1]				
				)


	def play_sounds(self, sound_name):
		'''
		Takes the scene and plays through the sounds_dict....
		'''

		#Plays a sound in the sound dict if no sound is currently playing...
		if self.sound_playing == False:
			self.player = pygame.mixer.Sound(self.sounds_dict[sound_name])
			self.player.play()
			self.sound_playing = True


	def stop_sounds(self):
		'''
		Stops playing a sound if any sound is currently playing
		'''
	
		#If any sound is currently playing...
		if self.sound_playing == True:
			self.player.stop()
			self.sound_playing = False


	def init_sound(self):
		'''
		Plays the first track off of the scenes sounds dict...
		'''
		self.play_sounds(list(self.sounds_dict.keys())[0])


	def show(self):
		'''
		Displaying the secne means just playing the music and updating the scene....

		Note: THIS STRUCTURE NEEDS TO REALLY BE THOUGHT OF BETTER......
		'''

		self.init_sound()
		self.update_scene()




