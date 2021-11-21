import pyglet
from pyglet.window import key
from pyglet.window import mouse


#We create a window object where everything's displayed.
window = pyglet.window.Window()
#creates image obj, searching local directory.
image = pyglet.resource.image('charizard.jpg')
#creates a label object.. with certain args..
label = pyglet.text.Label('hello, world',
	font_name = 'Times New Roman',
	font_size =36,
	x=window.width//2,
	y=window.width//2,
	anchor_x='center',
	anchor_y='center')


#Note that key has the attributes key.A, key.LEFT, the key module contains all
#keyboard keys information... corresponding to the keys ASCII representation (i.e. key.A=35 [if that
#is its ASCII representation])


#Detects keyboard events
@window.event
def on_key_press(symbol, modifiers):
	'''
	symbol is the symbol of the key pressed and modifier is something like...
	CTRL,SHIFT,CAPs that is tacked on...
	'''
	print(f'The {modifiers} {symbol} key was pressed.')


#creates an event
@window.event
def on_draw():
	#clears our window obj...
	window.clear()
	#displays our image object
	image.blit(0,0)
	#draws our label...
	label.draw()


@window.event
def on_mouse_press(x,y, button, modifiers):
	#(x,y) is the pos clicked, button is the button used, modifiers is....
	#
	if button == mouse.LEFT:
		print(f'The coord ({x},{y}) was pressed.')
	elif button == mouse.RIGHT:
		print(f'The coord ({x},{y}) was right-clicked.')


#These track all possible events...
event_logger = pyglet.window.event.WindowEventLogger()
window.push_handlers(event_logger)

#creates the app mainloop
pyglet.app.run()