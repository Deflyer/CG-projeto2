# File containg functions that return all sort of transformation matrixes. Created to abstract the math in other codes.

import math
import numpy as np
import glm

def get_mat_model(angle, r_x, r_y, r_z, t_x, t_y, t_z, s_x, s_y, s_z):
    """
    Dealls with all the transformations of a object
    Equivalent to the model matrix
    """
    
    angle = math.radians(angle)
    
    matrix_transform = glm.mat4(1.0) # instanciando uma matriz identidade
       
    # aplicando translacao (terceira operação a ser executada)
    matrix_transform = glm.translate(matrix_transform, glm.vec3(t_x, t_y, t_z))    
    
    # aplicando rotacao (segunda operação a ser executada)
    if angle!=0:
        matrix_transform = glm.rotate(matrix_transform, angle, glm.vec3(r_x, r_y, r_z))
    
    # aplicando escala (primeira operação a ser executada)
    matrix_transform = glm.scale(matrix_transform, glm.vec3(s_x, s_y, s_z))
    
    matrix_transform = np.array(matrix_transform)
    
    return matrix_transform

def get_mat_translation(t_x, t_y, t_z):
    '''
    Returns a translation matrix according to the translation variables received.
    '''

    return np.array([[1.0, 0.0, 0.0, t_x], 
                     [0.0, 1.0, 0.0, t_y], 
                     [0.0, 0.0, 1.0, t_z],
                     [0.0, 0.0, 0.0, 1.0]], np.float32)

def get_mat_scale(s_x, s_y, s_z):
    '''
    Returns a scale matrix according to the scale variables received.
    '''

    return np.array([[s_x, 0.0, 0.0, 0.0], 
                     [0.0, s_y, 0.0, 0.0], 
                     [0.0, 0.0, s_z, 0.0], 
                     [0.0, 0.0, 0.0, 1.0]], np.float32)

def get_mat_rotation_x(angle):
    '''
    Returns a X axis rotation matrix according to the angle variable received.
    '''

    sin = math.sin(angle)
    cos = math.cos(angle)

    return np.array([[1.0, 0.0,  0.0, 0.0], 
                     [0.0, cos, -sin, 0.0], 
                     [0.0, sin,  cos, 0.0], 
                     [0.0, 0.0,  0.0, 1.0]], np.float32)

def get_mat_rotation_y(angle):
    '''
    Returns a Y axis rotation matrix according to the angle variable received.
    '''

    sin = math.sin(angle)
    cos = math.cos(angle)

    return np.array([[ cos, 0.0, sin, 0.0], 
                     [ 0.0, 1.0, 0.0, 0.0], 
                     [-sin, 0.0, cos, 0.0], 
                     [ 0.0, 0.0, 0.0, 1.0]], np.float32)

def get_mat_rotation_z(angle):
    '''
    Returns a Z axis rotation matrix according to the angle variable received.
    '''

    sin = math.sin(angle)
    cos = math.cos(angle)

    return np.array([[cos, -sin, 0.0, 0.0], 
                     [sin,  cos, 0.0, 0.0], 
                     [0.0,  0.0, 1.0, 0.0], 
                     [0.0,  0.0, 0.0, 1.0]], np.float32)