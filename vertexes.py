# File contaning functions that have the vertexes used to created a object. It 
# is a simpler way to modularize our objects without using a bunch of files.

import numpy as np
from geometric_transf import *
from PIL import Image
from OpenGL.GL import *
import random

def load_texture_from_file(texture_id, img_textura):
    '''
    Load files from the code developed by our professor.
    '''
    
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    img = Image.open(img_textura)
    print(img_textura,img.mode)
    img_width = img.size[0]
    img_height = img.size[1]

    image_data = img.convert("RGBA").tobytes("raw", "RGBA",0,-1)

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, img_width, img_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)


def load_model_from_file(filename):
    '''
    Loads a Wavefront OBJ file.    
    '''

    objects = {}
    vertices = []
    texture_coords = []
    faces = []

    material = None

    # abre o arquivo obj para leitura
    for line in open(filename, "r"): # para cada linha do arquivo .obj
        if line.startswith('#'): continue # ignora comentarios
        values = line.split() # quebra a linha por espaço
        if not values: continue

        # recuperando vertices
        if values[0] == 'v':
            vertices.append(values[1:4])

        # recuperando coordenadas de textura
        elif values[0] == 'vt':
            texture_coords.append(values[1:3])

        # recuperando faces 
        elif values[0] in ('usemtl', 'usemat'):
            material = values[1]
        elif values[0] == 'f':
            face = []
            face_texture = []
            for v in values[1:]:
                w = v.split('/')
                face.append(int(w[0]))
                if len(w) >= 2 and len(w[1]) > 0:
                    face_texture.append(int(w[1]))
                else:
                    face_texture.append(0)

            faces.append((face, face_texture, material))

    model = {}
    model['vertices'] = vertices
    model['texture'] = texture_coords
    model['faces'] = faces

    return model

def get_vertexes_house():
    '''
    Responsible for loading the house vertexes and textures.    
    '''
    
    vertexes = []
    size = []
    textures_coord_list = []

    modelo = load_model_from_file('objects/casa/house.obj')

    # Allow for more the one texture.
    faces_visited = []
    for face in modelo['faces']:
        if face[2] not in faces_visited:
            size.append(len(vertexes))
            faces_visited.append(face[2])
        for vertice_id in face[0]:
            vertexes.append( modelo['vertices'][vertice_id-1] )
        for texture_id in face[1]:
            textures_coord_list.append( modelo['texture'][texture_id-1] )

    load_texture_from_file(2,'objects/casa/house.jpg')
    size.append(len(vertexes))
    return vertexes, size, textures_coord_list

def get_vertexes_drawer():
    '''
    Responsible for loading the bathroom vertexes and textures.
    '''

    vertexes = []
    size = []
    textures_coord_list = []

    modelo = load_model_from_file('objects/drawer/drawer.obj')

    # Allows only one texture.
    for face in modelo['faces']:
        for vertice_id in face[0]: vertexes.append( modelo['vertices'][vertice_id-1] )
        for texture_id in face[1]:
            textures_coord_list.append( modelo['texture'][texture_id-1] )

    size.append(len(vertexes))
    load_texture_from_file(5,'objects/drawer/drawer_texture.png')
    return vertexes, size, textures_coord_list

def get_textures_ground():
    vertexes = []
    size = []
    textures_coord_list = []

    modelo = load_model_from_file('objects/ground/ground.obj')

    # Allows only one texture.
    for face in modelo['faces']:
        for vertice_id in face[0]: vertexes.append( modelo['vertices'][vertice_id-1] )
        for texture_id in face[1]:
            textures_coord_list.append( modelo['texture'][texture_id-1] )

    size.append(len(vertexes))
    load_texture_from_file(9,'objects/ground/ground_texture.jpg')
    return vertexes, size, textures_coord_list

def get_textures_vase():
    vertexes = []
    size = []
    textures_coord_list = []

    modelo = load_model_from_file('objects/vase/vase.obj')

    # Allows only one texture.
    for face in modelo['faces']:
        for vertice_id in face[0]: vertexes.append( modelo['vertices'][vertice_id-1] )
        for texture_id in face[1]:
            textures_coord_list.append( modelo['texture'][texture_id-1] )

    size.append(len(vertexes))
    load_texture_from_file(6,'objects/vase/vase_texture.png')
    return vertexes, size, textures_coord_list

def get_textures_rose():
    vertexes = []
    size = []
    textures_coord_list = []

    modelo = load_model_from_file('objects/rose/rose.obj')

    # Allows only one texture.
    for face in modelo['faces']:
        for vertice_id in face[0]: vertexes.append( modelo['vertices'][vertice_id-1] )
        for texture_id in face[1]:
            textures_coord_list.append( modelo['texture'][texture_id-1] )

    size.append(len(vertexes))
    load_texture_from_file(7,'objects/rose/rose_texture.jpg')
    return vertexes, size, textures_coord_list

def get_textures_bed():
    vertexes = []
    size = []
    textures_coord_list = []

    modelo = load_model_from_file('objects/bed/bed.obj')

    # Allows only one texture.
    for face in modelo['faces']:
        for vertice_id in face[0]: vertexes.append( modelo['vertices'][vertice_id-1] )
        for texture_id in face[1]:
            textures_coord_list.append( modelo['texture'][texture_id-1] )

    size.append(len(vertexes))
    load_texture_from_file(8,'objects/bed/bed_texture.png')
    return vertexes, size, textures_coord_list

def get_vertexes_bathroom():
    '''
    Responsible for loading the bathroom vertexes and textures.
    '''

    vertexes = []
    size = []
    textures_coord_list = []

    modelo = load_model_from_file('objects/bathroom/bathroom.obj')

    # Allows only one texture.
    for face in modelo['faces']:
        for vertice_id in face[0]: vertexes.append( modelo['vertices'][vertice_id-1] )
        for texture_id in face[1]:
            textures_coord_list.append( modelo['texture'][texture_id-1] )

    size.append(len(vertexes))
    load_texture_from_file(3,'objects/bathroom/diffuse.png')
    return vertexes, size, textures_coord_list

def get_vertexes_sky():
    '''
    Responsible for loading the sky vertexes and textures.
    '''

    vertexes = []
    size = []
    textures_coord_list = []

    modelo = load_model_from_file('objects/sky/sky.obj')

    # Allows only one texture.
    for face in modelo['faces']:
        for vertice_id in face[0]: vertexes.append( modelo['vertices'][vertice_id-1] )
        for texture_id in face[1]:
            textures_coord_list.append( modelo['texture'][texture_id-1] )

    size.append(len(vertexes))
    
    load_texture_from_file(4,'objects/sky/ceu.jpg')
    return vertexes, size, textures_coord_list


def get_vertexes_plant1():
    '''
    Responsible for loading the plant1 vertexes and textures.    
    '''
    
    vertexes = []
    size = []
    textures_coord_list = []

    modelo = load_model_from_file('objects/plant/plant1.obj')

    # Allow for more the one texture.
    faces_visited = []
    for face in modelo['faces']:
        if face[2] not in faces_visited:
            size.append(len(vertexes))
            faces_visited.append(face[2])
        for vertice_id in face[0]:
            vertexes.append( modelo['vertices'][vertice_id-1] )
        for texture_id in face[1]:
            textures_coord_list.append( modelo['texture'][texture_id-1] )

    load_texture_from_file(11,'objects/plant/plant1.png')
    size.append(len(vertexes))

    positions = []
  
    exclusion_zones = [
    (-8, -30, 6, 60),
    (5, -9, 25, -2),             
    ]
    
    # Calcula posições fixas para as plantas
    for i in range(3):
        min_radius = 14 * (i + 1)
        max_radius = 14 * (i + 2)
        num_plants = 120 + 50 * i
        angle_step = 360 / num_plants
        for j in range(num_plants):
            angle_rad = math.radians(j * angle_step + random.uniform(-10, 10))  # Pequena variação de ângulo
            radius = random.uniform(min_radius, max_radius)  # Raio aleatório entre min_radius e max_radius
            t_x = radius * math.cos(angle_rad)  # Coordenada x ao longo do círculo
            t_y = -1.0                          # Mantém a altura y em -1
            t_z = radius * math.sin(angle_rad)  # Coordenada z ao longo do círculo
            angle = random.uniform(0, 360)  # Aleatoriza a rotação da planta
            s_x = random.uniform(0.5, 0.7) + 0.2*i   # Escala aleatória entre 0.3 e 0.7
            s_y = s_x                         # Mantém a escala uniforme
            s_z = random.uniform(0.5, 0.7) + 0.2*i   # Escala aleatória para a profundidade
            valid = True
            for zone in exclusion_zones:
                x_min, z_min, x_max, z_max = zone
                if (x_min <= t_x <= x_max) and (z_min <= t_z <= z_max):
                    valid = False
            if valid:
                positions.append((t_x, t_y, t_z, angle, s_x, s_y, s_z))

    return vertexes, size, textures_coord_list, positions

def get_vertexes_plant2():
    '''
    Responsible for loading the plant2 vertexes and textures.    
    '''
    
    vertexes = []
    size = []
    textures_coord_list = []

    modelo = load_model_from_file('objects/plant/plant2.obj')

    # Allow for more the one texture.
    faces_visited = []
    for face in modelo['faces']:
        if face[2] not in faces_visited:
            size.append(len(vertexes))
            faces_visited.append(face[2])
        for vertice_id in face[0]:
            vertexes.append( modelo['vertices'][vertice_id-1] )
        for texture_id in face[1]:
            textures_coord_list.append( modelo['texture'][texture_id-1] )

    load_texture_from_file(12,'objects/plant/plant2.png')
    size.append(len(vertexes))

    positions = []
  
    exclusion_zones = [
    (-8, -30, 6, 0),
    (5, -9, 25, -2),             
    ]
    
    # Calcula posições fixas para as plantas
    for i in range(3):
        min_radius = 3 * (i + 1)
        max_radius = 3 * (i + 2)
        num_plants = 10
        angle_step = (360 / num_plants) + random.uniform(0, 45)
        for j in range(num_plants):
            angle_rad = math.radians(j * angle_step + random.uniform(-10, 10))  # Pequena variação de ângulo
            radius = random.uniform(min_radius, max_radius)  # Raio aleatório entre min_radius e max_radius
            t_x = radius * math.cos(angle_rad)  # Coordenada x ao longo do círculo
            t_y = -1.0                          # Mantém a altura y em -1
            t_z = radius * math.sin(angle_rad)  # Coordenada z ao longo do círculo
            angle = random.uniform(0, 360)  # Aleatoriza a rotação da planta
            s_x = random.uniform(0.01, 0.02) + 0.005*i   # Escala aleatória entre 0.3 e 0.7
            s_y = s_x                         # Mantém a escala uniforme
            s_z = random.uniform(0.01, 0.02) + 0.005*i   # Escala aleatória para a profundidade
            valid = True
            for zone in exclusion_zones:
                x_min, z_min, x_max, z_max = zone
                if (x_min <= t_x <= x_max) and (z_min <= t_z <= z_max):
                    valid = False
            if valid:
                positions.append((t_x, t_y, t_z, angle, s_x, s_y, s_z))

    return vertexes, size, textures_coord_list, positions

def get_vertexes_dino():
    '''
    Responsible for loading the dino vertexes and textures.    
    '''
    
    vertexes = []
    size = []
    textures_coord_list = []

    modelo = load_model_from_file('objects/dinosaur/dinosaur.obj')

    # Allow for more the one texture.
    faces_visited = []
    for face in modelo['faces']:
        if face[2] not in faces_visited:
            size.append(len(vertexes))
            faces_visited.append(face[2])
        for vertice_id in face[0]:
            vertexes.append( modelo['vertices'][vertice_id-1] )
        for texture_id in face[1]:
            textures_coord_list.append( modelo['texture'][texture_id-1] )

    load_texture_from_file(13,'objects/dinosaur/dino.jpg')
    size.append(len(vertexes))
    return vertexes, size, textures_coord_list

def get_vertexes_shrek():
    '''
    Responsible for loading the tree vertexes and textures.
    '''
    
    vertexes = []
    size = []
    textures_coord_list = []
    
    modelo = load_model_from_file('objects/jureg/jureg.obj')

    # Allows more then one textures.
    faces_visited = []
    for face in modelo['faces']:
        if face[2] not in faces_visited:
            size.append(len(vertexes))
            faces_visited.append(face[2])
        for vertice_id in face[0]:
            vertexes.append( modelo['vertices'][vertice_id-1] )
        for texture_id in face[1]:
            textures_coord_list.append( modelo['texture'][texture_id-1] )

    size.append(len(vertexes))

    # Loading textures, each with it's own id.
    load_texture_from_file(0,'objects/jureg/jureg.jpg')
    load_texture_from_file(1,'objects/jureg/leather.jpg')
    print(size)

    return vertexes, size[1:], textures_coord_list