# File contating functions that draw each one of our composed objects.

from OpenGL.GL import *
from geometric_transf import *
import keyboard as kb

def draw_dragon(loc_model, loc_color, size = 0):    
    # rotacao
    angle = 0.0
    r_x = 0.0; r_y = 0.0; r_z = 1.0
    
    # translacao
    t_x = 0.0; t_y = 0.0; t_z = -20.0
    
    # escala
    s_x = 1.0; s_y = 1.0; s_z = 1.0
    
    mat_model = model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)
       
    # desenha o dragao
    glUniform4f(loc_color, 0.4, 0.2, 0, 1.0)
    glDrawArrays(GL_TRIANGLES, 0, 113958) ## renderizando

def draw_tree(loc_transformation, loc_color, size):
    '''
    Draws a cylinder and a sphere above it to create a 3D tree.
    '''

    # Getting the transformation matrixes needed to move our tree.
    mat_rotation_x = get_mat_rotation_x(1.5)
    mat_rotation_z = get_mat_rotation_z(0)
    mat_scale      = get_mat_scale(kb.tree_scale, kb.tree_scale, kb.tree_scale)
    mat_translacao = get_mat_translation(-0.5, 0.3, -0.1)

    # Getting a final transformation matrix and then sending it to GPU.
    mat_transform = mat_translacao @ (mat_scale @ (mat_rotation_z @ mat_rotation_x))
    glUniformMatrix4fv(loc_transformation, 1, GL_TRUE, mat_transform) 
    
    # Drawing and painting the cylinder.
    glUniform4f(loc_color, 0.4, 0.2, 0, 1.0)
    glDrawArrays(GL_TRIANGLE_STRIP, size['tree'][0], size['tree'][1] - size['tree'][0])

    glUniform4f(loc_color, 0, 0.6, 0, 1.0)
    glDrawArrays(GL_TRIANGLE_STRIP, size['tree'][1], size['tree'][2] - size['tree'][1])    


def desenha_mario():
    
    global vertices
    
    # aplica a matriz model
    

    
    # translacao
    t_x = 0.0; t_y = 0.0; t_z = -50.0;
    
    # rotacao
    angle = 0;
    r_x = 0.0; r_y = 0.0; r_z = 1.0;
    
    # escala
    s_x = 0.1; s_y = 0.1; s_z = 0.1;
    
    mat_model = model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    loc_model = glGetUniformLocation(program, "model")
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)
       
    # desenha o mario
    glDrawArrays(GL_TRIANGLES, 113958, 148815 - 113958) ## renderizando
    
    
