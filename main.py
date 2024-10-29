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

# Configuring ambient variables.
glHint(GL_LINE_SMOOTH_HINT, GL_DONT_CARE)
glEnable( GL_BLEND )
glBlendFunc( GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA )
glEnable(GL_LINE_SMOOTH)
glEnable(GL_TEXTURE_2D)
qtt_textures = 12
textures = glGenTextures(qtt_textures)

# Getting all the vertexes and textures used in our project.
index_vertexes = {}
textures_coord_list = []
start = 0

# Creating the shrek.
shrek, coords_shrek, textures_shrek = get_vertexes_shrek()
index_vertexes, start = create_object(index_vertexes, shrek, coords_shrek, 'shrek', start)

# Creating the bathroom.
bathroom, coords_bathroom, textures_bathroom = get_vertexes_bathroom()
index_vertexes, start = create_object(index_vertexes, bathroom, coords_bathroom, 'bathroom', start)

# Creating the house.
house, coords_house, textures_house = get_vertexes_house()
index_vertexes, start = create_object(index_vertexes, house, coords_house, 'house', start)

# Creating the sky.
sky, coords_sky, textures_sky = get_vertexes_sky()
index_vertexes, start = create_object(index_vertexes, sky, coords_sky, 'sky', start)

# Creating the drawer.
drawer, coords_drawer, textures_drawer = get_vertexes_drawer()
index_vertexes, start = create_object(index_vertexes, drawer, coords_drawer, 'drawer', start)

# Creating the vase.
vase, coords_vase, textures_vase = get_textures_vase()
index_vertexes, start = create_object(index_vertexes, vase, coords_vase, 'vase', start)

# Creating the rose.
rose, coords_rose, textures_rose = get_textures_rose()
index_vertexes, start = create_object(index_vertexes, rose, coords_rose, 'rose', start)

# Creating the bed.
bed, coords_bed, textures_bed = get_textures_bed()
index_vertexes, start = create_object(index_vertexes, bed, coords_bed, 'bed', start)

# Creating the ground.
ground, coords_ground, textures_ground = get_textures_ground()
index_vertexes, start = create_object(index_vertexes, ground, coords_ground, 'ground', start)

# Creating the plant1.
plant1, coords_plant1, textures_plant1, positions1 = get_vertexes_plant1()
index_vertexes, start = create_object(index_vertexes, plant1, coords_plant1, 'plant1', start)

# Creating the plant2.
plant2, coords_plant2, textures_plant2, positions2 = get_vertexes_plant2()
index_vertexes, start = create_object(index_vertexes, plant2, coords_plant2, 'plant2', start)

# Creating the bird.
bird, coords_bird, textures_bird = get_vertexes_bird()
index_vertexes, start = create_object(index_vertexes, bird, coords_bird, 'bird', start)

# Joining everyone
vertexes_temp = np.concatenate((shrek, bathroom))
vertexes_temp = np.concatenate((vertexes_temp, house))
vertexes_temp = np.concatenate((vertexes_temp, sky))
vertexes_temp = np.concatenate((vertexes_temp, drawer))
vertexes_temp = np.concatenate((vertexes_temp, vase))
vertexes_temp = np.concatenate((vertexes_temp, rose))
vertexes_temp = np.concatenate((vertexes_temp, bed))
vertexes_temp = np.concatenate((vertexes_temp, ground))
vertexes_temp = np.concatenate((vertexes_temp, plant1))
vertexes_temp = np.concatenate((vertexes_temp, plant2))
vertexes_temp = np.concatenate((vertexes_temp, bird))

vertexes = np.zeros(len(vertexes_temp), [("position", np.float32, 3)])
vertexes['position'] = vertexes_temp

textures_temp = textures_shrek + textures_bathroom + textures_house + textures_sky + textures_drawer + textures_vase + textures_rose + textures_bed + textures_ground + textures_plant1 + textures_plant2 + textures_bird
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

sky_rotation_angle = 0.0

# Code main loop.
while not glfw.window_should_close(window):
    # Reading user interactions.
    glfw.poll_events()

    kb.bird_angle = (kb.bird_angle + kb.bird_speed) % 360
    sky_rotation_angle = (sky_rotation_angle + 0.1) % 360

    # Activating the polygon view mode.
    if kb.polyMode:
        glPolygonMode(GL_FRONT_AND_BACK,GL_LINE)
    else:
        glPolygonMode(GL_FRONT_AND_BACK,GL_FILL)

    # Clearing screen and loading a new solid background.
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
    glClearColor(1.0, 1.0, 1.0, 1.0)

    # Drawing the objects.
    draw_bathroom(loc_model, loc_color, index_vertexes)
    draw_plant1(loc_model, loc_color,index_vertexes, positions1)
    draw_plant2(loc_model, loc_color,index_vertexes, positions2)
    draw_house(loc_model, loc_color, index_vertexes)
    draw_shrek(loc_model, loc_color, index_vertexes)
    draw_sky(loc_model, loc_color, index_vertexes, sky_rotation_angle)
    draw_drawer(loc_model, loc_color, index_vertexes)
    draw_vase(loc_model, loc_color, index_vertexes)
    draw_rose(loc_model, loc_color, index_vertexes)
    draw_bed(loc_model, loc_color, index_vertexes)
    draw_ground(loc_model, loc_color, index_vertexes)
    draw_bird(loc_model, loc_color, index_vertexes)

    mat_view, loc_view = get_view(program)
    glUniformMatrix4fv(loc_view, 1, GL_TRUE, mat_view)

    mat_projection, loc_projection = get_projection(program)
    glUniformMatrix4fv(loc_projection, 1, GL_TRUE, mat_projection)    

    # Displaying the next frame.
    glfw.swap_buffers(window)

glfw.terminate()