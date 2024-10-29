# File used to handle keyboard events.
# Most of the logic is from the code of our professor Jean Roberto Ponciano.

import math
import glfw
import glm

# Handles polyMode changing using 'p' key.
polyMode = False

# Handles camera movements.
cameraPos = glm.vec3(0.0,  0.0,  1.0)
cameraFront = glm.vec3(0.0,  0.0, -1.0)
cameraUp = glm.vec3(0.0,  1.0,  0.0)
skyfix = glm.vec3(0.0,  -72.0,  0.0) # used to make camera not surpass skybox sphere.

# Handles mouse events.
firstMouse = True
yaw = -90.0 
pitch = 0.0
lastX = 700/2
lastY = 700/2

# Handles Shrek translation.
shrek_step = 0
shrek_side_step = 0

# Handles rose scale.
rose_scale_y = 0.05

# Handles bird rotation.
bird_speed = 0.00
bird_radius = 80.0
bird_angle = 0.0

def key_event(window,key,scancode,action,mods):
    '''
    Handles inputs from the keyboard.
    '''
    
    global polyMode
    global cameraPos
    global cameraFront
    global cameraUp
    global shrek_step
    global shrek_side_step
    global rose_scale_y
    global bird_speed

    cameraSpeed = 0.4

    # Where Shrek shouldn't go.
    exclusion_zones = [
        (-8, -30, 6, 1),
        (5, -9, 25, -2),             
        ]
    
    # Camera forward movent ('w' key).
    if key == 87 and (action==1 or action==2):
        valid = True
        nova_pos = cameraPos + cameraSpeed * cameraFront
        if glm.length(nova_pos + skyfix) >= 96 or nova_pos[1] < -0.5:
             valid = False
        if valid:
            cameraPos = nova_pos
    
    # Camera backward movement ('s' key).
    if key == 83 and (action==1 or action==2):
        valid = True
        nova_pos = cameraPos - cameraSpeed * cameraFront
        if glm.length(nova_pos +skyfix) >= 96 or nova_pos[1] < -0.5:
             valid = False
        if valid:
            cameraPos = nova_pos
    
    # Camera left movement ('a' key).
    if key == 65 and (action==1 or action==2):
        valid = True
        nova_pos = cameraPos - glm.normalize(glm.cross(cameraFront, cameraUp)) * cameraSpeed
        if glm.length(nova_pos + skyfix) >= 96 or nova_pos[1] < -0.5:
             valid = False
        if valid:
            cameraPos = nova_pos
        
    # Camera right movement ('d' key).
    if key == 68 and (action==1 or action==2):
        valid = True
        nova_pos = cameraPos + glm.normalize(glm.cross(cameraFront, cameraUp)) * cameraSpeed
        if glm.length(nova_pos +skyfix) >= 96 or nova_pos[1] < -0.5:
             valid = False
        if valid:
            cameraPos = nova_pos

    # Shrek forward movement ('i' key).
    if key == 73 and (action==1 or action==2):
        valid = True
        for zone in exclusion_zones:
                x_min, z_min, x_max, z_max = zone
                if (x_min <= shrek_side_step <= x_max) and (z_min <= shrek_step + 1.9 <= z_max):
                    valid = False
        if(shrek_side_step **2  + (shrek_step - 0.5) ** 2 >= 3600):
             valid = False
        if valid:
            shrek_step -= 0.5 
        
    # Shrek backward movement ('k' key).
    if key == 75 and (action==1 or action==2):
        valid = True
        for zone in exclusion_zones:
                x_min, z_min, x_max, z_max = zone
                if (x_min <= shrek_side_step <= x_max) and (z_min <= shrek_step + 2.1 <= z_max):
                    valid = False
        if(shrek_side_step **2  + (shrek_step + 0.5) ** 2 >= 3600):
             valid = False
        if valid:
            shrek_step += 0.5 

    # Shrek left movement ('j' key).
    if key == 74 and (action==1 or action==2):
        valid = True
        for zone in exclusion_zones:
                x_min, z_min, x_max, z_max = zone
                if (x_min <= shrek_side_step -0.5 <= x_max) and (z_min <= shrek_step + 2 <= z_max):
                    valid = False
        if((shrek_side_step - 0.5) **2  + (shrek_step) ** 2 >= 3600):
             valid = False
        if valid:
            shrek_side_step -= 0.5 

    # Shrek right movement ('l' key).
    if key == 76 and (action==1 or action==2):
        valid = True
        for zone in exclusion_zones:
                x_min, z_min, x_max, z_max = zone
                if (x_min <= shrek_side_step +0.5 <= x_max) and (z_min <= shrek_step + 2 <= z_max):
                    valid = False
        if((shrek_side_step + 0.5) **2  + (shrek_step) ** 2 >= 3600):
             valid = False
        if valid:
            shrek_side_step += 0.5 

    # Change visual mode (polymode).)
    if key == 80 and action == glfw.PRESS: 
        polyMode = not polyMode

    # Grows rose ('↑' key).
    if key == 265 and action == glfw.PRESS:
        aux = rose_scale_y + 0.01
        rose_scale_y = min(aux, 0.13)

    # Decreses rose ('↓' key).
    if key == 264 and action == glfw.PRESS:
        aux = rose_scale_y - 0.01
        rose_scale_y = max(aux,0.05)

    # Speed up bird ('→' key).
    if key == 262 and action == glfw.PRESS:
        aux = bird_speed + 0.01
        bird_speed = min(aux, 0.05)

    # Speed down bird ('←' key).
    if key == 263 and action == glfw.PRESS:
        aux = bird_speed - 0.01
        bird_speed = max(aux, 0.0)

def mouse_event(window, xpos, ypos):
    '''
    Handles inputs from the keyboard.
    '''

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