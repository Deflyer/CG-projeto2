# File contating functions that draw each one of our objects.

from OpenGL.GL import *
from geometric_transf import *
import keyboard as kb

def draw_bathroom(loc_model, loc_color, size):
    '''
    Draws a wooden bathroom using already loaded vertexes (they are referenced in 'size' parameter).
    '''
    
    # Rotating.
    angle = 200
    r_x = 0.0; r_y = 1; r_z = 0
    
    # Translading.
    t_x = 20.0; t_y = 2.2; t_z = -6.0
    
    # Scaling.
    s_x = 0.003; s_y = 0.003; s_z = 0.003
    
    # Composing all the movements in a single matrix.
    mat_model = get_mat_model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)
       
    # Finally drawing it.
    glBindTexture(GL_TEXTURE_2D, 3)
    glDrawArrays(GL_TRIANGLES, size['bathroom'][0], size['bathroom'][1] - size['bathroom'][0]) ## renderizando

def draw_drawer(loc_model, loc_color, size):  
    '''
    Draws a wooden drawer using already loaded vertexes (they are referenced in 'size' parameter).
    '''

    # Rotating.
    angle = 180.0
    r_x = 0.0; r_y = 1.0; r_z = 0.0
    
    # Translading.
    t_x = 2.7; t_y = -0.95; t_z = -7.8
    
    # Scaling.
    s_x = 0.75; s_y = 0.75; s_z = 0.75
    
    # Composing all the movements in a single matrix.
    mat_model = get_mat_model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)

    # Finally drawing it.
    glBindTexture(GL_TEXTURE_2D, 5)
    glDrawArrays(GL_TRIANGLES, size['drawer'][0], size['drawer'][1] - size['drawer'][0]) ## renderizando

def draw_vase(loc_model, loc_color, size):
    '''
    Draws a plant vase using already loaded vertexes (they are referenced in 'size' parameter).
    '''

    # Rotating.
    angle = 0.0
    r_x = 0.0; r_y = 0.0; r_z = 1.0
    
    # Translading.
    t_x = -2.8; t_y = -0.8; t_z = -6.8
    
    # Scaling.
    s_x = 0.005; s_y = 0.005; s_z = 0.005
    
    # Composing all the movements in a single matrix.
    mat_model = get_mat_model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)

    # Finaally drawing it.
    glBindTexture(GL_TEXTURE_2D, 6)
    glDrawArrays(GL_TRIANGLES, size['vase'][0], size['vase'][1] - size['vase'][0]) ## renderizando

def draw_rose(loc_model, loc_color, size):
    '''
    Draws a rose flower using already loaded vertexes (they are referenced in 'size' parameter).
    '''

    # Rotating.
    angle = 0.0
    r_x = 0.0; r_y = 0.0; r_z = 1.0
    
    # Translading.
    t_x = -2.8; t_y = -0.8; t_z = -6.8
    
    # Scaling.
    s_x = 0.05; s_y = kb.rose_scale_y; s_z = 0.05
    
    # Composing all the movements in a single matrix.
    mat_model = get_mat_model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)

    # Finally drawing it.
    glBindTexture(GL_TEXTURE_2D, 7)
    glDrawArrays(GL_TRIANGLES, size['rose'][0], size['rose'][1] - size['rose'][0]) ## renderizando

def draw_bed(loc_model, loc_color, size):
    '''
    Draws a wooden bed using already loaded vertexes (they are referenced in 'size' parameter).
    '''

    # Rotating.
    angle = 0.0
    r_x = 0.0; r_y = 1; r_z = 0.0
    
    # Translading.
    t_x = 2.7; t_y = -1.0; t_z = -20.0
    
    # Scaling.
    s_x = 0.035; s_y = 0.035; s_z = 0.035
    
    # Composing all the movements in a single matrix.
    mat_model = get_mat_model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)

    # Finally drawing it.
    glBindTexture(GL_TEXTURE_2D, 8)
    glDrawArrays(GL_TRIANGLES, size['bed'][0], size['bed'][1] - size['bed'][0]) ## renderizando

def draw_sky(loc_model, loc_color, size, angle):
    '''
    Draws a spherical 'skybox' using already loaded vertexes (they are referenced in 'size' parameter).
    '''

    # Rotating.
    r_x = 0.0; r_y = 1.0; r_z = 0
    
    # Translading.
    t_x = 0.0; t_y = -45; t_z = 0.0
    
    # Scaling.
    s_x = 1; s_y = 1; s_z = 1
    
    # Composing all the movements in a single matrix.
    mat_model = get_mat_model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)
       
    # Finally drawing it.
    glBindTexture(GL_TEXTURE_2D, 4)
    glDrawArrays(GL_TRIANGLES, size['sky'][0], size['sky'][1] - size['sky'][0]) ## renderizando

def draw_ground(loc_model, loc_color, size):
    '''
    Draws a plane using already loaded vertexes (they are referenced in 'size' parameter).
    '''

    # Rotating.
    angle = 0.0
    r_x = 0.0; r_y = 0.0; r_z = 0.0
    
    # Translading.
    t_x = 0.0; t_y = -1.0; t_z = 0.0
    
    # Scaling.
    s_x = 70; s_y = 70; s_z = 70
    
    # Composing all the movements in a single matrix.
    mat_model = get_mat_model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)
    
    # Finally drawing it.
    glBindTexture(GL_TEXTURE_2D, 9)
    glDrawArrays(GL_TRIANGLE_STRIP, size['ground'][0], size['ground'][1] - size['ground'][0])

def draw_house(loc_model, loc_color, size):
    '''
    Draws a wooden house using already loaded vertexes (they are referenced in 'size' parameter).
    '''

    # Rotating.
    angle = 180
    r_x = 0.0; r_y = 1.0; r_z = 0
    
    # Translading.
    t_x = 0.0; t_y = -1.0; t_z = -10.0
    
    # Scaling.
    s_x = 0.5; s_y = 0.5; s_z = 0.5
    
    # Composing all the movements in a single matrix.
    mat_model = get_mat_model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)
    
    # Finally drawing it, using a texture in each house face.
    for i in range(len(size['house']) - 1):
        glBindTexture(GL_TEXTURE_2D, 2)
        glDrawArrays(GL_TRIANGLES, size['house'][i], size['house'][i +1] - size['house'][i]) ## renderizandoS 

def draw_plant1(loc_model, loc_color, size, positions):
    '''
    Draws our first plant sample using already loaded vertexes (they are referenced in 'size' parameter).
    '''

    for (t_x, t_y, t_z, angle, s_x, s_y, s_z) in positions:
        # Rotate the plant with the given random angle.
        r_x = 0.0; r_y = 1.0; r_z = 0
        
        # Generates the transformation matrix for each plant.
        mat_model = get_mat_model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
        glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)
        
        # Draw the plant with the texture.
        for j in range(len(size['plant1']) - 1):
            glBindTexture(GL_TEXTURE_2D, 10)
            glDrawArrays(GL_TRIANGLES, size['plant1'][j], size['plant1'][j + 1] - size['plant1'][j])

def draw_plant2(loc_model, loc_color, size, positions):
    '''
    Draws our second plant sample using already loaded vertexes (they are referenced in 'size' parameter).
    '''

    for (t_x, t_y, t_z, angle, s_x, s_y, s_z) in positions:
        # Rotate the plant with the given random angle.
        r_x = 0.0; r_y = 1.0; r_z = 0

        # Generates the transformation matrix for each plant.
        mat_model = get_mat_model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
        glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)
        
        # Draw the plant with the texture.
        for i in range(len(size['plant2']) - 1):
            glBindTexture(GL_TEXTURE_2D, 11)
            glDrawArrays(GL_TRIANGLES, size['plant2'][i], size['plant2'][i +1] - size['plant2'][i]) 

def draw_shrek(loc_model, loc_color, size):
    '''
    Draws Shrek using already loaded vertexes (they are referenced in 'size' parameter).
    '''

    # Rotating.
    angle = 180.0
    r_x = 0.0; r_y = 1.0; r_z = 0.0
    
    # Translading.
    t_x = 0.0 + kb.shrek_side_step; t_y = -1.0; t_z = 2.0 + kb.shrek_step
    
    # Scaling.
    s_x = 2.8; s_y = 2.8; s_z = 2.8
    
    # Composing all the movements in a single matrix.
    mat_model = get_mat_model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)

    # Drawing the Shrek character.
    glBindTexture(GL_TEXTURE_2D, 0)
    glDrawArrays(GL_TRIANGLES, size['shrek'][0], size['shrek'][1] - size['shrek'][0]) ## renderizando
    
    # Drawing the Shrek leather clothes.
    glBindTexture(GL_TEXTURE_2D, 1)
    glDrawArrays(GL_TRIANGLES, size['shrek'][1], size['shrek'][2] - size['shrek'][1]) ## renderizando    

def draw_bird(loc_model, loc_color, size):
    '''
    Draws a bird using already loaded vertexes (they are referenced in 'size' parameter).
    '''

    # Rotating.
    angle = - ( (360 * kb.bird_angle) / (2 * math.pi) )
    r_x = 0.0; r_y = 1.0; r_z = 0.0
    
    # Translading.
    t_x = kb.bird_radius * math.cos(kb.bird_angle); t_y = 50.0; t_z = kb.bird_radius * math.sin(kb.bird_angle)
    
    # Scaling.
    s_x = 0.05; s_y = 0.05; s_z = 0.05
    
    # Composing all the movements in a single matrix.
    mat_model = get_mat_model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z)
    glUniformMatrix4fv(loc_model, 1, GL_TRUE, mat_model)

    # Finally drawing it.
    for i in range(len(size['bird']) - 1):
        glBindTexture(GL_TEXTURE_2D, 12)
        glDrawArrays(GL_TRIANGLES, size['bird'][i], size['bird'][i +1] - size['bird'][i])