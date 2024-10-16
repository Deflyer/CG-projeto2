# File contaning functions that have the vertexes used to created a object. It is a simpler way to modularize
# our objects without using a bunch of files.

import numpy as np
from geometric_transf import *
from PIL import Image
from OpenGL.GL import *

# Load files from the code developed by our professor
def load_texture_from_file(texture_id, img_textura):
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
    """Loads a Wavefront OBJ file. """
    objects = {}
    vertices = []
    texture_coords = []
    faces = []

    material = None

    # abre o arquivo obj para leitura
    for line in open(filename, "r"): ## para cada linha do arquivo .obj
        if line.startswith('#'): continue ## ignora comentarios
        values = line.split() # quebra a linha por espaço
        if not values: continue


        ### recuperando vertices
        if values[0] == 'v':
            vertices.append(values[1:4])


        ### recuperando coordenadas de textura
        elif values[0] == 'vt':
            texture_coords.append(values[1:3])

        ### recuperando faces 
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

# Responsible for loading the house vertexes and textures
def get_vertexes_house():
    vertexes = []
    size = []
    textures_coord_list = []


    modelo = load_model_from_file('objects/casa/casa.obj')

    # Allow for more the one texture
    faces_visited = []
    for face in modelo['faces']:
        if face[2] not in faces_visited:
            size.append(len(vertexes))
            faces_visited.append(face[2])
        for vertice_id in face[0]:
            vertexes.append( modelo['vertices'][vertice_id-1] )
        for texture_id in face[1]:
            textures_coord_list.append( modelo['texture'][texture_id-1] )

    load_texture_from_file(2,'objects/casa/grama.jpg')
    size.append(len(vertexes))
    print(size)
    return vertexes, size, textures_coord_list

# Responsible for loading the dragon vertexes and textures
def get_vertexes_dragon():
    vertexes = []
    size = []
    textures_coord_list = []


    modelo = load_model_from_file('objects/dragao.obj')

    # Allows only one texture
    for face in modelo['faces']:
        for vertice_id in face[0]: vertexes.append( modelo['vertices'][vertice_id-1] )
        for texture_id in face[1]:
            textures_coord_list.append( modelo['texture'][texture_id-1] )

    size.append(len(vertexes))
    print(size)
    return vertexes, size, textures_coord_list

# Responsible for loading the tree vertexes and textures
def get_vertexes_tree2():
    vertexes = []
    size = []
    textures_coord_list = []
    
    modelo = load_model_from_file('objects/arvore/arvore10.obj')

    # Allows more then one textures
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
    ### Loading textures, each with it's own id.
    load_texture_from_file(0,'objects/arvore/bark_0021.jpg')
    load_texture_from_file(1,'objects/arvore/DB2X2_L01.png')
    print(size)

    return vertexes, size[1:], textures_coord_list

# Responsible for loading the mario vertexes and textures
def get_vertexes_mario():
    vertexes = []
    size = []
    
    modelo = load_model_from_file('objects/mario-model.obj')
    # No texturesfor this one
    for face in modelo['faces']:
        for vertice_id in face[0]: vertexes.append( modelo['vertices'][vertice_id-1] )

    size.append(len(vertexes))

    return vertexes, size