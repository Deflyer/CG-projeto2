# File contaning functions that have the vertexes used to created a object. It is a simpler way to modularize
# our objects without using a bunch of files.

import numpy as np
import random
from geometric_transf import *
from shapes import *

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

def get_vertexes_dragon():
    vertexes = []
    size = []

    modelo = load_model_from_file('objetos/uploads_files_4053544_house+creep.obj')

    for face in modelo['faces']:
        for vertice_id in face[0]: vertexes.append( modelo['vertices'][vertice_id-1] )
    size.append(len(vertexes))

    return vertexes, size

def get_vertexes_mario():
    vertexes = []
    size = []
    
    modelo = load_model_from_file('objetos/mario-model.obj')

    for face in modelo['faces']:
        for vertice_id in face[0]: vertexes.append( modelo['vertices'][vertice_id-1] )

    size.append(len(vertexes))

    return vertexes, size

def get_vertexes_tree():
    '''
    Returns an array containing all the vertexes of our tree object.

    The tree is created by positioning a sphere above a cylinder.
    '''

    # Generating the cylinder and sphere vertexes.
    cyl = cylinder(0.1,0.9)
    sph = sphere(0.3)
    vertexes = np.concatenate((cyl, sph))

    # Creating an array containing the amount of vertexes used in each shape.
    size = []
    size.append(len(cyl))
    size.append(len(sph))

    return vertexes, size

