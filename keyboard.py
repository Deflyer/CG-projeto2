# File used to handle keyboard events.
# Most of the logic is from the code of our professor

import math
import glfw
import glm

polyMode = False
tree_scale = 1
sun_rot = 0
sun_speed = 0
person_step = 0
person_speed = 0
cameraPos   = glm.vec3(0.0,  0.0,  1.0)
cameraFront = glm.vec3(0.0,  0.0, -1.0)
cameraUp    = glm.vec3(0.0,  1.0,  0.0)
firstMouse = True
yaw = -90.0 
pitch = 0.0
lastX =  700/2
lastY =  700/2

# Geometric transformations auxiliar variables.
rose_scale_y = 0.05
bird_speed = 0.00
bird_radius = 80.0
bird_angle = 0.0

def key_event(window,key,scancode,action,mods):
    global polyMode
    global cameraPos
    global cameraFront
    global cameraUp
    global rose_scale_y
    global bird_speed

    cameraSpeed = 0.4
    
    if key == 87 and (action==1 or action==2): # tecla W
        cameraPos += cameraSpeed * cameraFront
    
    if key == 83 and (action==1 or action==2): # tecla S
        cameraPos -= cameraSpeed * cameraFront
    
    if key == 65 and (action==1 or action==2): # tecla A
        cameraPos -= glm.normalize(glm.cross(cameraFront, cameraUp)) * cameraSpeed
        
    if key == 68 and (action==1 or action==2): # tecla D
        cameraPos += glm.normalize(glm.cross(cameraFront, cameraUp)) * cameraSpeed

    if key == 80 and action == glfw.PRESS: 
        polyMode = not polyMode

    if key == 265 and action == glfw.PRESS: # tecla seta pra cima (rosa cresce).
        aux = rose_scale_y + 0.01
        rose_scale_y = min(aux, 0.13)

    if key == 262 and action == glfw.PRESS: # tecla seta pra direita.
        aux = bird_speed + 0.01
        bird_speed = min(aux, 0.05)

    if key == 263 and action == glfw.PRESS: # tecla seta pra baixo.
        aux = bird_speed - 0.01
        bird_speed = max(aux, 0.0)

def mouse_event(window, xpos, ypos):
    global firstMouse, cameraFront, yaw, pitch, lastX, lastY
    if firstMouse:
        lastX = xpos
        lastY = ypos
        firstMouse = False

    xoffset = xpos - lastX
    yoffset = lastY - ypos
    lastX = xpos
    lastY = ypos

    sensitivity = 0.5
    xoffset *= sensitivity
    yoffset *= sensitivity

    yaw += xoffset
    pitch += yoffset

    
    if pitch >= 90.0: pitch = 90.0
    if pitch <= -90.0: pitch = -90.0

    front = glm.vec3()
    front.x = math.cos(glm.radians(yaw)) * math.cos(glm.radians(pitch))
    front.y = math.sin(glm.radians(pitch))
    front.z = math.sin(glm.radians(yaw)) * math.cos(glm.radians(pitch))
    cameraFront = glm.normalize(front)