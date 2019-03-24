from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

vertices = (
    (-1, 0, 1), #0
    (-1, 0,-1), #1
    ( 1, 0,-1), #2
    ( 1, 0, 1), #3
    ( 0, 1, 0), #BICO_PIRAMIDE = 4
)

linhas = (
    (0,1),
    (0,3),
    (2,1),
    (2,3),
    (0,4),
    (1,4),
    (2,4),
    (3,4),
)

faces = (
    (0, 1, 2, 3)
)

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )


def Piramide():
    glColor3fv((1,0,0))
    glBegin(GL_LINE_LOOP)
    glVertex3f(-1, 0, 1)
    glVertex3f(-1, 0,-1)
    glVertex3f( 1, 0,-1)
    glVertex3f( 1, 0, 1)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glVertex3f(-1, 0, 1)#0
    glVertex3f(-1, 0,-1)#1
    glVertex3f( 0, 2, 0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glVertex3f(-1, 0, 1)#0
    glVertex3f( 1, 0, 1)#3
    glVertex3f( 0, 2, 0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glVertex3f( 1, 0,-1)#2
    glVertex3f(-1, 0,-1)#1
    glVertex3f( 0, 2, 0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glVertex3f( 1, 0,-1)#2
    glVertex3f( 1, 0, 1)#3
    glVertex3f( 0, 2, 0)
    glEnd()

    # glColor3fv((0,1,0))
    # glBegin(GL_TRIANGLE_FAN)
    # glVertex3f( 0, 1, 0)
    # glVertex3f(-1, 0, 1)
    # glVertex3f(-1, 0,-1)
    # glVertex3f( 1, 0,-1)
    # glVertex3f( 1, 0, 1)
    # glVertex3f(-1, 0, 1)
    # glEnd()

def abacaxi():
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
glutCreateWindow("PIRAMIDE")
glutDisplayFunc(abacaxi)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()
