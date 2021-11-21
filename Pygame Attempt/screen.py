import pygame
import doctest


class Display():
	'''
	Creates a Screen object which everything will
	be drawn onto, we setup this screen with size=(width,height),
	a caption, and icon.....

	This Screen Object will manage everything that we display...
	'''


	def __init__(self, size, color=(255,255,255), caption='Clear Skies', icon='assets/images/red_facing_south.png'):
		'''
		Initializes our Screen object, creating a screen with the following
		params...

		inputs:
			size: a width, height tuple,
			caption: the caption on the screen
			icon: the image icon on the screen
		'''

		#Initialize the Display's screen, get its height, width, color and set the 
		#caption.....
		self.screen = pygame.display.set_mode(size)
		self.height = size[0]
		self.width = size[1]
		self.color = color
		self.caption = caption
		self.icon = pygame.image.load(icon)


	def init_screen(self):
		'''
		Initializes our screen using pygames functiosn for creating screens...
		'''
		
		pygame.display.set_caption(self.caption)
		pygame.display.set_icon(self.icon)


	def flip(self):
		'''
		Updates the screen, updating the screen....
		'''

		pygame.display.flip()


