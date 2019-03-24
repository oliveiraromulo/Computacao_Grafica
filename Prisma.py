from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

vertices_base = 5

# vertices = (
#     ( 1,-1,-1),
#     ( 1, 1,-1),
#     (-1, 1,-1),
#     (-1,-1,-1),
#     ( 1,-1, 1),
#     ( 1, 1, 1),
#     (-1,-1, 1),
#     (-1, 1, 1),
#     )

# linhas = (
#     (0,1),
#     (0,3),
#     (0,4),
#     (2,1),
#     (2,3),
#     (2,7),
#     (6,3),
#     (6,4),
#     (6,7),
#     (5,1),
#     (5,4),
#     (5,7),
#     )

# faces = (
#     (0,1,2,3),
#     (3,2,7,6),
#     (6,7,5,4),
#     (4,5,1,0),
#     (1,5,7,2),
#     (4,0,3,6)
#     )

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )

def Prisma():
     #Base Superior
    glBegin(GL_LINE_LOOP)
    for l in range(vertices_base):
        glVertex3f(math.cos((2*math.pi*l)/vertices_base), 0, math.sin((2*math.pi*l)/vertices_base))
    glEnd()

    #Base Inferior
    glBegin(GL_LINE_LOOP)
    for l in range(vertices_base):
        glVertex3f(math.cos((2*math.pi*l)/vertices_base), 2, math.sin((2*math.pi*l)/vertices_base))
    glEnd()


    glBegin(GL_LINES)
    for l in range(vertices_base):
        glVertex3f(math.cos((2*math.pi*l)/vertices_base), 0, math.sin((2*math.pi*l)/vertices_base))
        glVertex3f(math.cos((2*math.pi*l)/vertices_base), 2, math.sin((2*math.pi*l)/vertices_base))
    glEnd()
    
def melancia():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    Prisma()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("CUBO N VERTICES")
glutDisplayFunc(melancia)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-25)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()


