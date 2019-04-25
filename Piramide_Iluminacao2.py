from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *

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
    (1, 2, 0),
    (3, 0, 2),
    (0, 1, 4),
    (0, 3, 4),
    (2, 1, 4),
    (2, 3, 4)
)

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )

def calculaNormalFace(v0, v1, v2):
    x = 0
    y = 1
    z = 2    
    U = ( v2[x]-v0[x], v2[y]-v0[y], v2[z]-v0[z] )
    V = ( v1[x]-v0[x], v1[y]-v0[y], v1[z]-v0[z] )
    N = ( (U[y]*V[z]-U[z]*V[y]),(U[z]*V[x]-U[x]*V[z]),(U[x]*V[y]-U[y]*V[x]))
    NLength = sqrt(N[x]*N[x]+N[y]*N[y]+N[z]*N[z])
    return ( N[x]/NLength, N[y]/NLength, N[z]/NLength)

def Piramide():
    glColor3fv((1,0,0))
    glBegin(GL_QUADS)
    glVertex3f(-1, 0, 1)
    glVertex3f(-1, 0,-1)
    glVertex3f( 1, 0,-1)
    glVertex3f( 1, 0, 1)
    glEnd()

    glBegin(GL_TRIANGLES)
    glNormal3fv(calculaNormalFace((-1, 0, 1),(-1, 0,-1),( 0, 2, 0)))
    glVertex3f(-1, 0, 1)#0
    glVertex3f(-1, 0,-1)#1
    glVertex3f( 0, 2, 0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glNormal3fv(calculaNormalFace((-1, 0, 1),( 1, 0, 1),( 0, 2, 0)))
    glVertex3f(-1, 0, 1)#0
    glVertex3f( 1, 0, 1)#3
    glVertex3f( 0, 2, 0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glNormal3fv(calculaNormalFace(( 1, 0,-1),(-1, 0,-1),( 0, 2, 0)))
    glVertex3f( 1, 0,-1)#2
    glVertex3f(-1, 0,-1)#1
    glVertex3f( 0, 2, 0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glNormal3fv(calculaNormalFace(( 1, 0,-1),( 1, 0, 1),( 0, 2, 0)))
    glVertex3f( 1, 0,-1)#2
    glVertex3f( 1, 0, 1)#3
    glVertex3f( 0, 2, 0)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    Piramide()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)


def reshape(w,h):
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45,float(w)/float(h),0.1,50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,1,10,0,0,0,0,1,0)

def init():
    mat_ambient = (0.4, 0.0, 0.0, 1.0)
    mat_diffuse = (1.0, 0.0, 0.0, 1.0)
    mat_specular = (0.0, 1.0, 0.0, 1.0)
    mat_shininess = (50,)
    light_position = (3, 3, 6)
    glClearColor(0.0,0.0,0.0,0.0)
    glShadeModel(GL_FLAT)
 
    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_MULTISAMPLE)
 
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(800,600)
    glutCreateWindow("Piramide")
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutTimerFunc(50,timer,1)
    init()
    glutMainLoop()
 
main()