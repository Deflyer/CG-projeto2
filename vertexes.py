# File contaning functions that colect the vertexes used to created a object. It 
# is a simpler way to modularize our objects without using a bunch of files.

from geometric_transf import *
from PIL import Image
from OpenGL.GL import *
import random

def load_texture_from_file(texture_id, img_textura):
    '''
    Load texture files (from the code developed by our professor Jean Roberto Ponciano).
    '''
    
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    img = Image.open(img_textura)
    img_width = img.size[0]
    img_height = img.size[1]

    image_data = img.convert("RGBA").tobytes("raw", "RGBA",0,-1)

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, img_width, img_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)

def load_model_from_file(filename):
    '''
    Load Wavefront OBJ files (from the code developed by our professor Jean Roberto Ponciano).
    '''

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
    Responsible for loading house vertexes and textures.    
    '''
    
    vertexes = []
    size = []
    textures_coord_list = []

    modelo = load_model_from_file('objects/house/house.obj')

    # Allows more than one texture.
    faces_visited = []
    for face in modelo['faces']:
        if face[2] not in faces_visited:
            size.append(len(vertexes))
            faces_visited.append(face[2])
        for vertice_id in face[0]:
            vertexes.append( modelo['vertices'][vertice_id-1] )
        for texture_id in face[1]:
            textures_coord_list.append( modelo['texture'][texture_id-1] )

    load_texture_from_file(2,'objects/house/house.jpg')
    size.append(len(vertexes))
    return vertexes, size, textures_coord_list

def get_vertexes_drawer():
    '''
    Responsible for loading drawer vertexes and textures.
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

def get_vertexes_ground():
    '''
    Responsible for loading ground vertexes and textures.
    '''

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

def get_vertexes_vase():
    '''
    Responsible for loading vase vertexes and textures.
    '''

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

def get_vertexes_rose():
    '''
    Responsible for loading rose vertexes and textures.
    '''

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

def get_vertexes_bed():
    '''
    Responsible for loading bed vertexes and textures.
    '''

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
    Responsible for loading bathroom vertexes and textures.
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
    load_texture_from_file(3,'objects/bathroom/bathroom.png')
    return vertexes, size, textures_coord_list

def get_vertexes_sky():
    '''
    Responsible for loading sky vertexes and textures.
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
    
    load_texture_from_file(4,'objects/sky/sky.jpg')
    return vertexes, size, textures_coord_list


def get_vertexes_plant1():
    '''
    Responsible for loading plant1 vertexes and textures.    
    '''
    
    vertexes = []
    size = []
    textures_coord_list = []

    modelo = load_model_from_file('objects/plant/plant1.obj')

    # Allows more than one texture.
    faces_visited = []
    for face in modelo['faces']:
        if face[2] not in faces_visited:
            size.append(len(vertexes))
            faces_visited.append(face[2])
        for vertice_id in face[0]:
            vertexes.append( modelo['vertices'][vertice_id-1] )
        for texture_id in face[1]:
            textures_coord_list.append( modelo['texture'][texture_id-1] )

    load_texture_from_file(10,'objects/plant/plant1.png')
    size.append(len(vertexes))

    positions = []
  
    # Where plants shouldn't grow.
    exclusion_zones = [
    (-8, -30, 6, 60),
    (5, -9, 25, -2),             
    ]
    
    # Randomizes plants positions.
    for i in range(3):
        min_radius = 14 * (i + 1)
        max_radius = 14 * (i + 2)
        num_plants = 120 + 50 * i
        angle_step = 360 / num_plants
        for j in range(num_plants):
            angle_rad = math.radians(j * angle_step + random.uniform(-10, 10)) # Small angle variation.
            radius = random.uniform(min_radius, max_radius) # Random radius between min_radius and max_radius.
            t_x = radius * math.cos(angle_rad) # X-coordinate through the circle.
            t_y = -1.0 # Keeps y-coordinate in -1.
            t_z = radius * math.sin(angle_rad) # Z-coordinate through the circle.
            angle = random.uniform(0, 360) # Randomizes plant rotation.
            s_x = random.uniform(0.5, 0.7) + 0.2*i # Random scale between 0.3 and 0.7.
            s_y = s_x # Keeps a uniform scale.
            s_z = random.uniform(0.5, 0.7) + 0.2*i # Random scale to depth.
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
    Responsible for loading plant2 vertexes and textures.    
    '''
    
    vertexes = []
    size = []
    textures_coord_list = []

    modelo = load_model_from_file('objects/plant/plant2.obj')

    # Allows more than one texture.
    faces_visited = []
    for face in modelo['faces']:
        if face[2] not in faces_visited:
            size.append(len(vertexes))
            faces_visited.append(face[2])
        for vertice_id in face[0]:
            vertexes.append( modelo['vertices'][vertice_id-1] )
        for texture_id in face[1]:
            textures_coord_list.append( modelo['texture'][texture_id-1] )

    load_texture_from_file(11,'objects/plant/plant2.png')
    size.append(len(vertexes))

    positions = []
  
    # Where plants shouldn't grow.
    exclusion_zones = [
    (-8, -30, 6, 0),
    (5, -9, 25, -2),             
    ]
    
    # Randomizes plants positions.
    for i in range(3):
        min_radius = 3 * (i + 1)
        max_radius = 3 * (i + 2)
        num_plants = 10
        angle_step = (360 / num_plants) + random.uniform(0, 45)
        for j in range(num_plants):
            angle_rad = math.radians(j * angle_step + random.uniform(-10, 10)) # Small angle variation.
            radius = random.uniform(min_radius, max_radius) # Random radius between min_radius and max_radius.
            t_x = radius * math.cos(angle_rad) # X-coordinate through the circle.
            t_y = -1.0 # Keeps y-coordinate in -1.
            t_z = radius * math.sin(angle_rad) # Z-coordinate through the circle.
            angle = random.uniform(0, 360) # Randomizes plant rotation.
            s_x = random.uniform(0.01, 0.02) + 0.005*i # Random scale between 0.3 and 0.7.
            s_y = s_x # Keeps a uniform scale.
            s_z = random.uniform(0.01, 0.02) + 0.005*i # Random scale to depth.
            valid = True
            for zone in exclusion_zones:
                x_min, z_min, x_max, z_max = zone
                if (x_min <= t_x <= x_max) and (z_min <= t_z <= z_max):
                    valid = False
            if valid:
                positions.append((t_x, t_y, t_z, angle, s_x, s_y, s_z))

    return vertexes, size, textures_coord_list, positions

def get_vertexes_bird():
    '''
    Responsible for loading bird vertexes and textures.    
    '''
    
    vertexes = []
    size = []
    textures_coord_list = []

    modelo = load_model_from_file('objects/bird/bird.obj')

    # Allows more than one texture.
    faces_visited = []
    for face in modelo['faces']:
        if face[2] not in faces_visited:
            size.append(len(vertexes))
            faces_visited.append(face[2])
        for vertice_id in face[0]:
            vertexes.append( modelo['vertices'][vertice_id-1] )
        for texture_id in face[1]:
            textures_coord_list.append( modelo['texture'][texture_id-1] )

    load_texture_from_file(12,'objects/bird/bird.jpg')
    size.append(len(vertexes))
    return vertexes, size, textures_coord_list

def get_vertexes_shrek():
    '''
    Responsible for loading Shrek vertexes and textures.
    '''
    
    vertexes = []
    size = []
    textures_coord_list = []
    
    modelo = load_model_from_file('objects/shrek/shrek.obj')

    # Allows more than one textures.
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
    load_texture_from_file(0,'objects/shrek/shrek.jpg')
    load_texture_from_file(1,'objects/shrek/leather.jpg')
    return vertexes, size[1:], textures_coord_list

def create_object(index_vertexes, vertexes_object, coords_object, name, start):
    '''
    Fills the 'index_vertexes' dictionary with the specified object vertexes and
    updates the start point variable counter ('start').
    '''
    
    index_vertexes[name] = [start]

    # We use a different method to read from an obj file, so different save.
    for value in coords_object:
        index_vertexes[name].append(start + value)
    start = len(vertexes_object) + start

    return index_vertexes, start