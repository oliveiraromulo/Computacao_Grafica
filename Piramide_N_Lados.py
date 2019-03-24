from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

lados = 25

# vertices = (
#     (-1, 0, 1), #0
#     (-1, 0,-1), #1
#     ( 1, 0,-1), #2
#     ( 1, 0, 1), #3
#     ( 0, 1, 0), #BICO_PIRAMIDE = 4
# )

# linhas = (
#     (0,1),
#     (0,3),
#     (2,1),
#     (2,3),
#     (0,4),
#     (1,4),
#     (2,4),
#     (3,4),
# )

# faces = (
#     (0, 1, 2, 3)
# )

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )


def Piramide():
    #Base da Piramide
    glBegin(GL_LINE_LOOP)
    for l in range(lados):
        glVertex3f(math.cos((2*math.pi*l)/lados), 0, math.sin((2*math.pi*l)/lados))
    glEnd()


    glBegin(GL_LINE_LOOP)
    for l in range(lados):
        if l > 6:
            glColor3fv((1,0.5,0.5))
        else:
            glColor3fv(cores[l])
        glVertex3f(math.cos((2*math.pi*l)/lados), 0, math.sin((2*math.pi*l)/lados))
        glVertex3f(0, 2, 0)

    glEnd()

def melancia():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    Piramide()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)


# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("PIRAMIDE_N LADOS")
glutDisplayFunc(melancia)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()