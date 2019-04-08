from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *
import numpy

raio = 2
pontos = 20

thetaI = -(pi/2)
thetaF = (pi/2)
deltaTheta = (thetaF - thetaI)/pontos

phiI = 0
phiF = 2*pi
deltaPhi = (phiF - phiI)/pontos


theta = thetaI

def Esfera():  
    # #Base para a rotação no eixo Y. Angulo Theta
    # for pc in range(pontosCirculo):
    #     #Base para circunferencia da esfera. Angulo Fi
    #     for p in range(pontos):
    #         x = raio*(math.cos((2*math.pi*p)/pontos)*math.cos((2*math.pi*pc)/pontosCirculo))
    #         y = raio*(math.cos((2*math.pi*p)/pontos))
    #         z = raio*(math.cos((2*math.pi*p)/pontos)*math.sin((math.pi*pc)/pontosCirculo))
    #          glVertex3f(x, y, z)
    # glColor3fv((1,0.5,0.5))

    glBegin(GL_LINES)
    for t in numpy.arange(thetaI, thetaF, deltaTheta):
        for p in numpy.arange(phiI, phiF, deltaPhi):
            x = raio * cos(t) * cos(p)
            y = raio * sin(t)
            z = raio * cos(t) * sin(p)
            glVertex3f(x, y, z)
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
