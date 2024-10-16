# File contating functions that draw each one of our composed objects.

from OpenGL.GL import *
from geometric_transf import *
import keyboard as kb

def draw_dragon(loc_model, loc_color, size):    
    # rotate
    angle = 0.0
    r_x = 0.0; r_y = 0.0; r_z = 1.0
    
    # translade
    t_x = 0.0; t_y = 10.0; t_z = -20.0
    
    # scale
    s_x = 1.0; s_y = 1.0; s_z = 1.0
    
    mat_model = get_mat_model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)
       
    # draws the dragon
    glBindTexture(GL_TEXTURE_2D, 0)
    glDrawArrays(GL_TRIANGLES, size['dragon'][0], size['dragon'][1] - size['dragon'][0]) ## renderizando

def draw_house(loc_model, loc_color, size):    
    # rotate
    angle = 0.0
    r_x = 0.0; r_y = 0.0; r_z = 1.0
    
    # translade
    t_x = 0.0; t_y = 1.0; t_z = -20.0
    
    # scale
    s_x = 1.0; s_y = 1.0; s_z = 1.0
    
    mat_model = get_mat_model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)
    
    # draws each house face with a texture
    for i in range(len(size['house']) - 1):
        glBindTexture(GL_TEXTURE_2D, (i + 1) % 3)
        glDrawArrays(GL_TRIANGLES, size['house'][i], size['house'][i +1] - size['house'][i]) ## renderizando
        

def draw_tree2(loc_model, loc_color, size):
    # rotate
    
    angle = 0.0
    r_x = 0.0; r_y = 0.0; r_z = 1.0
    
    # translade
    t_x = -10.0; t_y = -1.0; t_z = 15.0
    
    # scale
    s_x = 7.0; s_y = 7.0; s_z = 7.0
    
    mat_model = get_mat_model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)

    ### desenho o wood log
    #define id da textura do modelo
    glBindTexture(GL_TEXTURE_2D, 0)
    glDrawArrays(GL_TRIANGLES, size['tree2'][0], size['tree2'][1] - size['tree2'][0]) ## renderizando
    
    ### draws the leaves
    #define id da textura do modelo
    glBindTexture(GL_TEXTURE_2D, 1)

    glDrawArrays(GL_TRIANGLES, size['tree2'][1], size['tree2'][2] - size['tree2'][1]) ## renderizando    
    
def draws_mario(loc_model, loc_color, size):
    # translade
    t_x = 0.0; t_y = 0.0; t_z = -50.0
    
    # rotate
    angle = 0
    r_x = 0.0; r_y = 0.0; r_z = 1.0
    
    # scale
    s_x = 0.1; s_y = 0.1; s_z = 0.1
    
    mat_model = get_mat_model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)
       
    glUniform4f(loc_color, 0.4, 0.2, 0, 1.0)
    glDrawArrays(GL_TRIANGLES, size['mario'][0], size['mario'][1] - size['mario'][0]) ## renderizando