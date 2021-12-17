# imports
import pyglet
from pyglet.gl import *

# inbuilt imports
import Classes as pycraft
from logger import *

test = True

info('main', 'Initializing PyCraft...')
if __name__ == '__main__':
    # create window
    window = pycraft.PyCraftWindow(width = 800, height = 500, resizable = True)
    
    glClearColor(0.5, 0.7, 1, 1)
    # Run the app
    info('main', 'Running PyCraft...')
    pyglet.app.run()

info('main', 'Stopping!')
