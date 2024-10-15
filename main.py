from OpenGL.GL import *
from config_screen import *
from drawings import *
from vertexes import *
from vertexes import *
import keyboard as kb
import glm

window = init_window()
program = create_program()

glHint(GL_LINE_SMOOTH_HINT, GL_DONT_CARE)
glEnable( GL_BLEND )
glBlendFunc( GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA )
glEnable(GL_LINE_SMOOTH)
glEnable(GL_TEXTURE_2D)
qtd_texturas = 4
textures = glGenTextures(qtd_texturas)
# Getting all the vertexes used in our project.

# Creating the house.
index_vertexes = {}
textures_coord_list = []
start = 0
# Creating the tree2.
tree2, coords_tree2, textures_tree2 = get_vertexes_tree2()
print(start)
index_vertexes['tree2'] = [start]
for value in coords_tree2:
    index_vertexes['tree2'].append(index_vertexes['tree2'][-1] + value)
start = len(tree2) + start

# Creating the dragon.
dragon, coords_dragon, textures_dragon = get_vertexes_dragon()
index_vertexes['dragon'] = [start]
for value in coords_dragon:
    index_vertexes['dragon'].append(index_vertexes['dragon'][-1] + value)
start = len(dragon) + start

# Creating the mario.
mario, coords_mario = get_vertexes_mario()
index_vertexes['mario'] = [start]
for value in coords_mario:
    index_vertexes['mario'].append(index_vertexes['mario'][-1] + value)
start = len(mario) + start



# Joining everyone
vertexes_temp = np.concatenate((tree2, dragon))
vertexes_temp = np.concatenate((vertexes_temp, mario))
vertexes = np.zeros(len(vertexes_temp), [("position", np.float32, 3)])
vertexes['position'] = vertexes_temp

textures_temp = textures_tree2 + textures_dragon
textures = np.zeros(len(textures_temp), [("position", np.float32, 2)]) # duas coordenadas
textures['position'] = textures_temp

#-----------------------------------------------------------------------------------
# Configuring the screen used to show the objects.
send_data_to_gpu(program, vertexes, textures)
render_window(window)

# Activating the keyboard and mouse handler function and initializing an auxiliar variable.
glfw.set_key_callback(window,kb.key_event)
glfw.set_cursor_pos_callback(window, kb.mouse_event)

#-----------------------------------------------------------------------------------
# Getting GPU variables.

loc_color = get_loc_color(program)
mat_view, loc_view = get_view(program)
mat_projection, loc_projection = get_projection(program)
loc_model = glGetUniformLocation(program, "model")
#-----------------------------------------------------------------------------------
# Code main loop.
while not glfw.window_should_close(window):
    # Reading user interactions.
    glfw.poll_events()
    kb.sun_rot += kb.sun_speed
    kb.person_step += kb.person_speed

    # Activating the polygon view mode.
    if kb.polyMode:
        glPolygonMode(GL_FRONT_AND_BACK,GL_LINE)
    else:
        glPolygonMode(GL_FRONT_AND_BACK,GL_FILL)

    # Clearing screen and loading a new solid background.
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
    glClearColor(1.0, 1.0, 1.0, 1.0)

    # Drawing the objects.
    #draw_dragon(loc_model, loc_color,index_vertexes)
    draw_tree2(loc_model, loc_color,index_vertexes)

    mat_view, loc_view = get_view(program)
    glUniformMatrix4fv(loc_view, 1, GL_TRUE, mat_view)

    mat_projection, loc_projection = get_projection(program)
    glUniformMatrix4fv(loc_projection, 1, GL_TRUE, mat_projection)    

    # Displaying the next frame.
    glfw.swap_buffers(window)

glfw.terminate()