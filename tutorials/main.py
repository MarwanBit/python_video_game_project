import pyglet

window = pyglet.window.Window()
image = pyglet.resource.image('charizard.jpg')

@window.event
def on_draw():
	window.clear()
	image.blit(0,0)


pyglet.app.run()