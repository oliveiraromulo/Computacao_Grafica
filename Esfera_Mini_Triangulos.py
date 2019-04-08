from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *
import numpy

raio = 5
pontos = 20

thetaI = -(pi/2)
thetaF = (pi/2)
deltaTheta = (thetaF - thetaI)/pontos

phiI = 0
phiF = 2*pi
deltaPhi = (phiF - phiI)/pontos


theta = thetaI

def Esfera():  
    glBegin(GL_TRIANGLE_STRIP)
    for t in numpy.arange(thetaI, thetaF, deltaTheta):
        for p in numpy.arange(phiI, phiF, deltaPhi):
            #Ponto P
            x = raio * cos(t) * cos(p)
            y = raio * sin(t)
            z = raio * cos(t) * sin(p)
            glVertex3f(x, y, z)
            glColor3fv((1, 1, 1))
            #Ponto Q
            x = raio * cos(t) * cos(p + deltaPhi)
            y = raio * sin(t)
            z = raio * cos(t) * sin(p + deltaPhi)
            glVertex3f(x, y, z)
            glColor3fv((1, 1, 1))
            #Ponto R
            x = raio * cos(t + deltaTheta) * cos(p)
            y = raio * sin(t + deltaTheta)
            z = raio * cos(t + deltaTheta) * sin(p)
            glVertex3f(x, y, z)
            glColor3fv((0, 1, 0))
            #Ponto S
            x = raio * cos(t + deltaTheta) * cos(p + deltaPhi)
            y = raio * sin(t + deltaTheta)
            z = raio * cos(t + deltaTheta) * sin(p + deltaPhi)
            glVertex3f(x, y, z)
            glColor3fv((0, 0, 1))
    glEnd()

def melancia():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    Esfera()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("ESFERA")
glutDisplayFunc(melancia)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-25)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()
