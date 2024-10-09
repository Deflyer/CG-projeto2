from OpenGL.GL import *
from config_screen import *
from drawings import *
from vertexes import *
from vertexes import *
import keyboard as kb
import glm

# Getting all the vertexes used in our project.

# Creating the house.
index_vertexes = {}
start = 0

# Creating the dragon.
dragon, coords_dragon = get_vertexes_dragon()
index_vertexes['dragon'] = [start]
for value in coords_dragon:
    index_vertexes['dragon'].append(index_vertexes['dragon'][-1] + value)

# Creating the mario.
mario, coords_mario = get_vertexes_mario()
index_vertexes['mario'] = [start]
for value in coords_mario:
    index_vertexes['mario'].append(index_vertexes['mario'][-1] + value)
start = len(mario) + start


# Joining everyone
vertexes_temp = np.concatenate((mario, dragon))
vertexes = np.zeros(len(vertexes_temp), [("position", np.float32, 3)])
vertexes['position'] = vertexes_temp


#-----------------------------------------------------------------------------------
# Configuring the screen used to show the objects.
window = init_window()
program = create_program()
send_data_to_gpu(program, vertexes)
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
    draw_dragon(loc_model, loc_color)

    mat_view, loc_view = get_view(program)
    glUniformMatrix4fv(loc_view, 1, GL_TRUE, mat_view)

    mat_projection, loc_projection = get_projection(program)
    glUniformMatrix4fv(loc_projection, 1, GL_TRUE, mat_projection)    

    # Displaying the next frame.
    glfw.swap_buffers(window)

glfw.terminate()