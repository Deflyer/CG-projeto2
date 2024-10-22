# File contating functions that draw each one of our composed objects.

from OpenGL.GL import *
from geometric_transf import *
import keyboard as kb

def draw_bathroom(loc_model, loc_color, size):    
    # rotate
    angle = 0.0
    r_x = 0.0; r_y = 0.0; r_z = 1.0
    
    # translade
    t_x = 15.0; t_y = 10.0; t_z = -20.0
    
    # scale
    s_x = 0.005; s_y = 0.005; s_z = 0.005
    
    mat_model = get_mat_model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)
       
    # draws the bathroom
    glBindTexture(GL_TEXTURE_2D, 3)
    glDrawArrays(GL_TRIANGLES, size['bathroom'][0], size['bathroom'][1] - size['bathroom'][0]) ## renderizando

def draw_drawer(loc_model, loc_color, size):    
    # rotate
    angle = 0.0
    r_x = 0.0; r_y = 0.0; r_z = 1.0
    
    # translade
    t_x = 3.0; t_y = -1.0; t_z = -22.25
    
    # scale
    s_x = 0.75; s_y = 0.75; s_z = 0.75
    
    mat_model = get_mat_model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)

    # draws the drawer
    glBindTexture(GL_TEXTURE_2D, 5)
    glDrawArrays(GL_TRIANGLES, size['drawer'][0], size['drawer'][1] - size['drawer'][0]) ## renderizando

def draw_sky(loc_model, loc_color, size):    
    # rotate
    angle = 0.0
    r_x = 0.0; r_y = 0.0; r_z = 1.0
    
    # translade
    t_x = 0.0; t_y = -35; t_z = 0.0
    
    # scale
    s_x = 1; s_y = 1; s_z = 1
    
    mat_model = get_mat_model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)
       
    # draws the sky
    glBindTexture(GL_TEXTURE_2D, 4)
    glDrawArrays(GL_TRIANGLES, size['sky'][0], size['sky'][1] - size['sky'][0]) ## renderizando

def draw_ground(loc_model, loc_color, size):    
    # rotate
    angle = 0.0
    r_x = 0.0; r_y = 0.0; r_z = 1.0
    
    # translade
    t_x = 0.0; t_y = -0.5; t_z = 0.0
    
    # scale
    s_x = 1; s_y = 1; s_z = 1
    
    mat_model = get_mat_model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)
       
    # draws the ground
    glBindTexture(GL_TEXTURE_2D, 5)
    glDrawArrays(GL_TRIANGLES, size['ground'][0], size['ground'][1] - size['ground'][0])

def draw_house(loc_model, loc_color, size):    
    # rotate
    angle = 0.0
    r_x = 0.0; r_y = 0.0; r_z = 1.0
    
    # translade
    t_x = 0.0; t_y = -1.0; t_z = -20.0
    
    # scale
    s_x = 0.5; s_y = 0.5; s_z = 0.5
    
    mat_model = get_mat_model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)
    
    # draws each house face with a texture  
    for i in range(len(size['house']) - 1):
        glBindTexture(GL_TEXTURE_2D, 2)
        glDrawArrays(GL_TRIANGLES, size['house'][i], size['house'][i +1] - size['house'][i]) ## renderizando
        

def draw_shrek(loc_model, loc_color, size):
    # rotate
    
    angle = 0.0
    r_x = 0.0; r_y = 0.0; r_z = 1.0
    
    # translade
    t_x = 0.0; t_y = 0.0; t_z = 0.0
    
    # scale
    s_x = 6; s_y = 6; s_z = 6
    
    mat_model = get_mat_model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)

    ### desenho o wood log
    #define id da textura do modelo
    glBindTexture(GL_TEXTURE_2D, 0)
    glDrawArrays(GL_TRIANGLES, size['shrek'][0], size['shrek'][1] - size['shrek'][0]) ## renderizando
    
    ### draws the leaves
    #define id da textura do modelo
    glBindTexture(GL_TEXTURE_2D, 1)

    glDrawArrays(GL_TRIANGLES, size['shrek'][1], size['shrek'][2] - size['shrek'][1]) ## renderizando    