import pyglet
from pyglet.window import Window
import pyglet.resource


class StartScreen(Window):
	'''
	This class defines the start screen for the "clear skies" game...
	'''


	def __init__(self, scene_control):
		'''
		Constructs the start_screen class given a default height and width
		for the screen given by the params height and width

		inputs:
			height: height of the screen in pixels
			width: width of the screen in pixels.
		'''

		#Inherit from the Window class.....
		super().__init__(resizable=True)
		#Make scene control an attribute
		self.scene_control = scene_control
		#Set the Window Caption....
		self.set_caption("Clear Skies")
		#Set Icon of Window...
		self.icon = pyglet.image.load('icon.JPG')
		self.set_icon(self.icon)
		#the start screen image if saved in this attribute
		self.background = pyglet.image.load('start_screen.jpg')
		#Set the Window size to fit the image...
		self.set_size(self.background.width, self.background.height)
		#Start Button Label..
		self.start_button_text = pyglet.text.Label(
			'Start!', font_name = 'Times New Roman',
			font_size=36, x=self.width//2, y=self.height//(2.5), 
			anchor_x = 'center', anchor_y='center'
			)
		#Finally we have the music for the start screen....
		self.start_screen_music = pyglet.media.load('start_screen.mp3')
		#Music player loads music and plays it..
		self.music_player = pyglet.media.Player()
		self.music_player.queue(self.start_screen_music)
		self.music_player.play()
		


	
	def on_draw(self):
		'''
		Draws the start_screen using its attributes...

		inputs:
			self (a start screen object..)
		'''

		#if the start_screen is supposed to be drawn...
		if self.scene_control.start_screen == True:
			self.clear()
			self.background.blit(
				0,0
				)
			self.start_button_text.draw()


			
		



