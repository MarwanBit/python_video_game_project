class SceneControl():
	'''
	The class which tracks progress, controls transitions between
	scenes and locations, and generally keeps track of things...
	'''

	def __init__(self):
		'''
		Initializes our SceneControl class, which holds information
		on which scene, location, etc. is happening currently in game...
		'''

		#start_screen is on when initialized...
		self.start_screen = True