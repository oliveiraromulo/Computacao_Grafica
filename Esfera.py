from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *
import numpy
import sys
import png

raio = 5
pontos = 20

thetaI = -(pi/2)
thetaF = (pi/2)
deltaTheta = (thetaF - thetaI)/pontos

phiI = 0
phiF = 2*pi
deltaPhi = (phiF - phiI)/pontos

theta = thetaI

# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = '\033'

# Number of the glut window.
window = 0

# Rotations for cube. 
xrot = yrot = zrot = 0.0
dx = 0.1
dy = 0
dz = 0

texture = []

def LoadTextures():
    global texture
    texture = glGenTextures(2)

    ################################################################################
    glBindTexture(GL_TEXTURE_2D, texture[0])
    reader = png.Reader(filename='terra_baixa.png')
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    ################################################################################

def InitGL(Width, Height):             
    LoadTextures()
    glEnable(GL_TEXTURE_2D)
    glClearColor(0.0, 0.0, 0.0, 0.0)    
    glClearDepth(1.0)                  
    glDepthFunc(GL_LESS)               
    glEnable(GL_DEPTH_TEST)            
    glShadeModel(GL_SMOOTH)            
    
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)

def ReSizeGLScene(Width, Height):
    if Height == 0:                        
        Height = 1

    glViewport(0, 0, Width, Height)      
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def DrawGLScene():
    global xrot, yrot, zrot, texture

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
    glLoadIdentity()                   

    glClearColor(0.5,0.5,0.5,1.0)            
    
    glTranslatef(0.0,0.0, -25.0)            

    glRotatef(xrot,1.0,0.0,0.0)          
    glRotatef(yrot,0.0,1.0,0.0)           
    glRotatef(zrot,0.0,0.0,1.0) 
    
    glBindTexture(GL_TEXTURE_2D, texture[0])

    glBegin(GL_TRIANGLE_STRIP)

    for t in numpy.arange(thetaI, thetaF, deltaTheta):
        for p in numpy.arange(phiI, phiF, deltaPhi):
            #Ponto P
            x = raio * cos(t) * cos(p)
            y = raio * sin(t)
            z = raio * cos(t) * sin(p)
            glTexCoord2f(p/(2*pi), ((t - (pi/2))/pi))
            glVertex3f(x, y, z)
            
            #glColor3fv((1, 1, 1))
            #Ponto Q
            x = raio * cos(t) * cos(p + deltaPhi)
            y = raio * sin(t)
            z = raio * cos(t) * sin(p + deltaPhi)
            glTexCoord2f((p + deltaPhi)/(2*pi), (t - (pi/2))/pi)
            glVertex3f(x, y, z)
            #glColor3fv((1, 1, 1))
            #Ponto R
            x = raio * cos(t + deltaTheta) * cos(p)
            y = raio * sin(t + deltaTheta)
            z = raio * cos(t + deltaTheta) * sin(p)
            glTexCoord2f(p/(2*pi), (((t + deltaTheta) - (pi/2))/pi))
            glVertex3f(x, y, z)
            #glColor3fv((0, 1, 0))
            #Ponto S
            x = raio * cos(t + deltaTheta) * cos(p + deltaPhi)
            y = raio * sin(t + deltaTheta)
            z = raio * cos(t + deltaTheta) * sin(p + deltaPhi)
            glTexCoord2f((p + deltaPhi)/(2*pi), (((t + deltaTheta) - (pi/2))/pi))
            glVertex3f(x, y, z)
            #glColor3fv((0, 0, 1))
    glEnd()              # Done Drawing The Cube
    
    xrot  = xrot + 0.9                # X rotation
    yrot = yrot + 0.9                 # Y rotation
    zrot = zrot + 0.5                 # Z rotation


    glutSwapBuffers()


# def keyPressed(tecla, x, y):
#     global dx, dy, dz
#     if tecla == ESCAPE:
#         glutLeaveMainLoop()
#     elif tecla == 'x' or tecla == 'X':
#         dx = 0.5
#         dy = 0
#         dz = 0   
#     elif tecla == 'y' or tecla == 'Y':
#         dx = 0
#         dy = 0.5
#         dz = 0   
#     elif tecla == 'z' or tecla == 'Z':
#         dx = 0
#         dy = 0
#         dz = 0.5

# def teclaEspecialPressionada(tecla, x, y):
#     global xrot, yrot, zrot, dx, dy, dz
#     if tecla == GLUT_KEY_LEFT:
#         print ("ESQUERDA")
#         xrot -= dx                # X rotation
#         yrot -= dy                 # Y rotation
#         zrot -= dz                     
#     elif tecla == GLUT_KEY_RIGHT:
#         print ("DIREITA")
#         xrot += dx                # X rotation
#         yrot += dy                 # Y rotation
#         zrot += dz                     
#     elif tecla == GLUT_KEY_UP:
#         print ("CIMA")
#     elif tecla == GLUT_KEY_DOWN:
#         print ("BAIXO")

def main():
    global window
    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    
    # get a 640 x 480 window 
    glutInitWindowSize(640, 480)
    
    # the window starts at the upper left corner of the screen 
    glutInitWindowPosition(0, 0)
    
    window = glutCreateWindow("Textura")

    glutDisplayFunc(DrawGLScene)
    
    # When we are doing nothing, redraw the scene.
    glutIdleFunc(DrawGLScene)
    
    # Register the function called when our window is resized.
    glutReshapeFunc(ReSizeGLScene)
    
    # # Register the function called when the keyboard is pressed.  
    # glutKeyboardFunc(keyPressed)

    # glutSpecialFunc(teclaEspecialPressionada)

    # Initialize our window. 
    InitGL(640, 480)

    # Start Event Processing Engine    
    glutMainLoop()

# Print message to console, and kick off the main to get it rolling.
if __name__ == "__main__":
    #print ("Hit ESC key to quit.")
    main()