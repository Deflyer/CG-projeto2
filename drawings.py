# File contating functions that draw each one of our composed objects.

from OpenGL.GL import *
from geometric_transf import *
import keyboard as kb

def draw_dragon(loc_model, loc_color, size):    
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
    glBindTexture(GL_TEXTURE_2D, 1)
    glDrawArrays(GL_TRIANGLES, size['dragon'][0], size['dragon'][1] - size['dragon'][0]) ## renderizando

def draw_tree2(loc_model, loc_color, size):
    # rotacao
    
    angle = 0.0
    r_x = 0.0; r_y = 0.0; r_z = 1.0
    
    # translacao
    t_x = -10.0; t_y = -1.0; t_z = 15.0
    
    # escala
    s_x = 7.0; s_y = 7.0; s_z = 7.0
    
    mat_model = model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)

    ### desenho o tronco da arvore
    #define id da textura do modelo
    glBindTexture(GL_TEXTURE_2D, 0)
    # desenha o modelo
    glDrawArrays(GL_TRIANGLES, size['tree2'][0], size['tree2'][1] - size['tree2'][0]) ## renderizando
    
    ### desenho as folhas
    #define id da textura do modelo
    glBindTexture(GL_TEXTURE_2D, 1)
    # desenha o modelo
    glDrawArrays(GL_TRIANGLES, size['tree2'][1], size['tree2'][2] - size['tree2'][1]) ## renderizando    

def desenha_mario(loc_model, loc_color, size):
    # translacao
    t_x = 0.0; t_y = 0.0; t_z = -50.0
    
    # rotacao
    angle = 0
    r_x = 0.0; r_y = 0.0; r_z = 1.0
    
    # escala
    s_x = 0.1; s_y = 0.1; s_z = 0.1
    
    mat_model = model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)
       
    glUniform4f(loc_color, 0.4, 0.2, 0, 1.0)
    glDrawArrays(GL_TRIANGLES, size['mario'][0], size['mario'][1] - size['mario'][0]) ## renderizando

def desenha_Container(loc_model, loc_color, size = 0):
    
    
    # aplica a matriz model
    
    # rotacao
    angle = 210.0
    r_x = 0.0; r_y = 1.0; r_z = 0.0
    
    # translacao
    t_x = 0.0; t_y = 0.0; t_z = 15.0
    
    # escala
    s_x = 0.015; s_y = 0.015; s_z = 0.015
    
    mat_model = model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    glUniformMatrix4fv(loc_model, 1, GL_FALSE, mat_model)

    #desenha container
    #define id da textura do modelo
    glBindTexture(GL_TEXTURE_2D, 2)
    # desenha o modelo
    glDrawArrays(GL_TRIANGLES, 41172, 91248-41172) ## renderizando

    #desenha o ar condicionado
    #define id da textura do modelo
    glBindTexture(GL_TEXTURE_2D, 3)
    # desenha o modelo
    glDrawArrays(GL_TRIANGLES, 91248, 118005-91248) ## renderizando
    

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

    
    
