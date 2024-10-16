# File containing functions that configure the screen that will be used to show our project.

import glfw
from OpenGL.GL import *
import glm
import numpy as np
import keyboard as kb

HEIGHT = 1600
WIDTH = 1200
WINDOW_NAME = 'Project 2'
QTT_TEXTURES = 4

# Shaders' code.
vertex_code = """
        attribute vec3 position;
        attribute vec2 texture_coord;
        varying vec2 out_texture;
                
        uniform mat4 model;
        uniform mat4 view;
        uniform mat4 projection;        
        
        void main(){
            gl_Position = projection * view * model * vec4(position,1.0);
            out_texture = vec2(texture_coord);
        }
        """
fragment_code = """
        uniform vec4 color;
        varying vec2 out_texture;
        uniform sampler2D samplerTexture;

        void main(){
            vec4 texture = texture2D(samplerTexture, out_texture);
            gl_FragColor = texture;
        }
        """

def init_window():
    '''
    Instantiates a GLFW window.
    '''
    
    glfw.init()
    glfw.window_hint(glfw.VISIBLE, glfw.FALSE)
    window = glfw.create_window(WIDTH, HEIGHT, WINDOW_NAME, None, None)
    glfw.make_context_current(window)
    glfw.show_window(window)

    return window

def create_program():
    '''
    Requests GPU slots for the program and shaders to then compile and attach
    these shaders to this program slot.
    '''

    # Request a program and shader slots from GPU.
    program  = glCreateProgram()
    vertex   = glCreateShader(GL_VERTEX_SHADER)
    fragment = glCreateShader(GL_FRAGMENT_SHADER)

    # Set shaders source.
    glShaderSource(vertex, vertex_code)
    glShaderSource(fragment, fragment_code)

    # Compile shaders.
    glCompileShader(vertex)
    if not glGetShaderiv(vertex, GL_COMPILE_STATUS):
        error = glGetShaderInfoLog(vertex).decode()
        print(error)
        raise RuntimeError("Error compiling Vertex Shader.")
    glCompileShader(fragment)
    if not glGetShaderiv(fragment, GL_COMPILE_STATUS):
        error = glGetShaderInfoLog(fragment).decode()
        print(error)
        raise RuntimeError("Error compiling Fragment Shader.")

    # Attach shader objects to the program.
    glAttachShader(program, vertex)
    glAttachShader(program, fragment)

    # Build program.
    glLinkProgram(program)
    if not glGetProgramiv(program, GL_LINK_STATUS):
        print(glGetProgramInfoLog(program))
        raise RuntimeError('Error linking the program.')
        
    # Make program the default program.
    glUseProgram(program)

    return program

def send_data_to_gpu(program, vertexes, textures):
    '''
    Requests GPU slots to program data and then sends this data to this slot.
    '''

    # Request a buffer slot from GPU.
    buffer = glGenBuffers(2)


    # Sending vertexes data to this GPU variable.
    glBindBuffer(GL_ARRAY_BUFFER, buffer[0])
    glBufferData(GL_ARRAY_BUFFER, vertexes.nbytes, vertexes, GL_STATIC_DRAW)
    stride = vertexes.strides[0]
    offset = ctypes.c_void_p(0)

    # Localize the GPU variable (the one we defined in vertex shader) that represents each vertex.
    loc_vertex = glGetAttribLocation(program, "position")
    glEnableVertexAttribArray(loc_vertex)
    glVertexAttribPointer(loc_vertex, 3, GL_FLOAT, False, stride, offset)

    # Sending textures data to this GPU variable.
    glBindBuffer(GL_ARRAY_BUFFER, buffer[1])
    glBufferData(GL_ARRAY_BUFFER, textures.nbytes, textures, GL_STATIC_DRAW)
    stride = textures.strides[0]
    offset = ctypes.c_void_p(0)
    loc_texture_coord = glGetAttribLocation(program, "texture_coord")
    glEnableVertexAttribArray(loc_texture_coord)
    glVertexAttribPointer(loc_texture_coord, 2, GL_FLOAT, False, stride, offset)

def render_window(window):
    '''
    Render a already created window.
    '''

    glfw.show_window(window)
    glEnable(GL_DEPTH_TEST)

def get_loc_color(program):
    '''
    Returns the color variable localized in the GPU.
    '''

    return glGetUniformLocation(program, "color")

def get_view(program):
    '''
    Returns the transformation matrix variable localized in the GPU.
    '''

    return view_matrix(), glGetUniformLocation(program, "view")

def get_model(program):
    '''
    Returns the transformation matrix variable localized in the GPU.
    '''

    return glGetUniformLocation(program, "model")

def get_projection(program):
    '''
    Returns the transformation matrix variable localized in the GPU.
    '''

    return projection_matrix(), glGetUniformLocation(program, "projection")

def view_matrix():
    mat_view = glm.lookAt(kb.cameraPos, kb.cameraPos + kb.cameraFront, kb.cameraUp)
    mat_view = np.array(mat_view)
    return mat_view

def projection_matrix():
    # perspective parameters: fovy, aspect, near, far
    mat_projection = glm.perspective(glm.radians(45.0), WIDTH/HEIGHT, 0.1, 1000.0)
    
    mat_projection = np.array(mat_projection)    
    return mat_projection