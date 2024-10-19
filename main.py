from OpenGL.GL import *
from config_screen import *
from drawings import *
from vertexes import *
from vertexes import *
import keyboard as kb
import glm

# Configuring the screen used to show the objects with textures.
window = init_window()
program = create_program()

glHint(GL_LINE_SMOOTH_HINT, GL_DONT_CARE)
glEnable( GL_BLEND )
glBlendFunc( GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA )
glEnable(GL_LINE_SMOOTH)
glEnable(GL_TEXTURE_2D)
qtt_textures = 50
textures = glGenTextures(qtt_textures)

# Getting all the vertexes and textures used in our project.
index_vertexes = {}
textures_coord_list = []
start = 0

# Creating the shrek.
shrek, coords_shrek, textures_shrek = get_vertexes_shrek()
print(start)
index_vertexes['shrek'] = [start]
# We use a different method to read from an obj file, so different save
for value in coords_shrek:
    index_vertexes['shrek'].append(start + value)
start = len(shrek) + start

# Creating the bathroom.
bathroom, coords_bathroom, textures_bathroom = get_vertexes_bathroom()
index_vertexes['bathroom'] = [start]
for value in coords_bathroom:
    index_vertexes['bathroom'].append(index_vertexes['bathroom'][-1] + value)
start = len(bathroom) + start

# Creating the house.
house, coords_house, textures_house = get_vertexes_house()
index_vertexes['house'] = [start]
for value in coords_house:
    index_vertexes['house'].append(index_vertexes['house'][-1] + value)
start = len(house) + start

# Creating the sky.
sky, coords_sky, textures_sky = get_vertexes_sky()
index_vertexes['sky'] = [start]
for value in coords_sky:
    index_vertexes['sky'].append(index_vertexes['sky'][-1] + value)
start = len(sky) + start

# Creating the ground.
ground, coords_ground, textures_ground = get_vertexes_ground()
index_vertexes['ground'] = [start]
for value in coords_ground:
    index_vertexes['ground'].append(index_vertexes['ground'][-1] + value)
start = len(ground) + start

# Joining everyone
vertexes_temp = np.concatenate((shrek, bathroom))
vertexes_temp = np.concatenate((vertexes_temp, house))
vertexes_temp = np.concatenate((vertexes_temp, sky))
vertexes_temp = np.concatenate((vertexes_temp, ground))
vertexes = np.zeros(len(vertexes_temp), [("position", np.float32, 3)])
vertexes['position'] = vertexes_temp

textures_temp = textures_shrek + textures_bathroom + textures_house + textures_sky + textures_ground
textures = np.zeros(len(textures_temp), [("position", np.float32, 2)])
textures['position'] = textures_temp

#-----------------------------------------------------------------------------------

# Sending and rendering the objects.
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
    draw_bathroom(loc_model, loc_color,index_vertexes)
    draw_house(loc_model, loc_color, index_vertexes)
    draw_shrek(loc_model, loc_color,index_vertexes)
    draw_sky(loc_model, loc_color,index_vertexes)
    draw_ground(loc_model, loc_color,index_vertexes)

    mat_view, loc_view = get_view(program)
    glUniformMatrix4fv(loc_view, 1, GL_TRUE, mat_view)

    mat_projection, loc_projection = get_projection(program)
    glUniformMatrix4fv(loc_projection, 1, GL_TRUE, mat_projection)    

    # Displaying the next frame.
    glfw.swap_buffers(window)

glfw.terminate()