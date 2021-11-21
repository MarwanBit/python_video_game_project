import pyglet
from start_screen import StartScreen
from scene_control import SceneControl


#Creates the SceneControl obj uses to keep track of current events,
#locations, etc....
scene_control = SceneControl()
#Creates the startScreen object uses to start the game...
start_screen = StartScreen(scene_control)

#Starts the event loop..
pyglet.app.run()