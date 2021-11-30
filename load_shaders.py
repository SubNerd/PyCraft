# imports
import os
from logger import *
import time
from OpenGL.GL import *

# configure logging
logging.basicConfig(level=logging.DEBUG)

# dictionary of shaders
shaders = {}

# function to load shaders
def load_shaders():
    for i in os.listdir("./shaders"):
        if not "." in i:
            try:
                log("load_shaders", f"Loading shader: {i}")
                frag = None
                vert = None
                with open("./shaders/" + i + "/"+f'{i}.frag', "r") as f:
                    frag = f.read()
                with open("./shaders/" + i + "/"+f'{i}.vert', "r") as f:
                    vert = f.read()
                shader = compile_shader(vert, frag)
                shaders[i] = shader
            except:
                logging.warn(f"load_shaders: Failed to load shader: {i}")

# function to compile shaders
def compile_shader(vert, frag):
    shader = glCreateProgram()
    vs = glCreateShader(GL_VERTEX_SHADER)
    fs = glCreateShader(GL_FRAGMENT_SHADER)
    glShaderSource(vs, vert)
    glShaderSource(fs, frag)
    glCompileShader(vs)
    glCompileShader(fs)
    glAttachShader(shader, vs)
    glAttachShader(shader, fs)
    glLinkProgram(shader)
    return shader
