from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

flag = True
xRotated, yRotated, zRotated = 0.0, 0.0, 0.0

def check(value):
    global flag
    flag = not flag
    print(flag)
    glutPostRedisplay()
    glutTimerFunc(1000, check, 0)

def highlight_lines(x, y, z, live_transparency_line):
    for a in np.arange(0, 0.2, 0.1):
        for b in np.arange(0, 0.2, 0.1):
            for c in np.arange(0, 0.2, 0.1):
                # First Hidden Layer Plane 1
                glPointSize(3.0)
                glBegin(GL_POINTS)
                glColor4f(1.0, 1.0, 1.0, 0.05)
                glVertex3f(0.1 + b, 0.1 + c, 0.4)
                glVertex3f(0.1 + b, 0.1 + c, 0.4)
                glEnd()
                glBegin(GL_LINE_LOOP)
                glColor4f(1.0, 1.0, 1.0, live_transparency_line)
                glVertex3f(x, y, z)
                glVertex3f(0.1 + b, 0.1 + c, 0.4)
                glVertex3f(0.1 + b, 0.1 + c, 0.4)
                glEnd()

                # First Hidden Layer Plane 4
                if c < .44:
                    glPointSize(3.0)
                    glBegin(GL_POINTS)
                    glVertex3f(x, y, z)
                    glVertex3f(0.17 + b, 0.16 + c, 0.44)
                    glVertex3f(0.17 + b, 0.16 + c, 0.44)
                    glEnd()
                    glBegin(GL_LINE_LOOP)
                    glColor4f(1.0, 1.0, 1.0, live_transparency_line)
                    glVertex3f(x, y, z)
                    glVertex3f(0.17 + b, 0.16 + c, 0.44)
                    glVertex3f(0.17 + b, 0.16 + c, 0.44)
                    glEnd()

                # Second Hidden Layer Plane 1
                glPointSize(3.0)
                glBegin(GL_POINTS)
                glColor4f(1.0, 1.0, 1.0, 0.05)
                glVertex3f(0.1 + b, 0.1 + c, 0.8)
                glVertex3f(0.1 + b, 0.1 + c, 0.8)
                glEnd()
                glBegin(GL_LINE_LOOP)
                glColor4f(1.0, 1.0, 1.0, live_transparency_line)
                glVertex3f(0.1 + b, 0.1 + a, 0.4)
                glVertex3f(0.1 + b, 0.1 + c, 0.8)
                glVertex3f(0.1 + b, 0.1 + c, 0.8)
                glEnd()

                # Output layer
                glPointSize(20.0)
                glBegin(GL_POINTS)
                glColor4f(0.0, 0.0, 1.0, 1.0)
                glVertex3f(0.2, 0.35, 1.2)
                glEnd()
                glBegin(GL_LINE_LOOP)
                glColor4f(1.0, 1.0, 1.0, live_transparency_line)
                glVertex3f(0.1 + b, 0.1 + a, 0.8)
                glVertex3f(0.2, 0.35, 1.2)
                glVertex3f(0.2, 0.35, 1.2)
                glEnd()

def display_network():
    glMatrixMode(GL_MODELVIEW)
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(-1.0, -0.75, -3.5)
    glColor3f(0.8, 0.2, 0.1)
    glRotatef(yRotated, 0.0, 1.0, 0.0)
    glScalef(2.0, 2.0, 2.0)
    
    dead_transparency_line = 0.08
    live_transparency_line = 0.15
    
    for a in np.arange(0, 0.6, 0.1):
        for b in np.arange(0, 0.6, 0.1):
            for c in np.arange(0, 0.6, 0.1):
                # Input layer
                glPointSize(15.0)
                glBegin(GL_POINTS)
                glColor4f(1.0, 1.0, 1.0, 0.05)
                glVertex3f(0.1 + b, 0.1 + a, 0.0)
                glEnd()
                
                # First Hiddeen Layer
                glPointSize(3.0)
                glBegin(GL_POINTS)
                glColor4f(1.0, 1.0, 1.0, 0.05)
                glVertex3f(0.1 + b, 0.1 + c, 0.4)
                glEnd()
                glBegin(GL_LINE_LOOP)
                glColor4f(1.0, 1.0, 1.0, dead_transparency_line)
                glVertex3f(0.1 + b, 0.1 + a, 0.0)
                glVertex3f(0.1 + b, 0.1 + c, 0.4)
                glVertex3f(0.1 + b, 0.1 + c, 0.4)
                glEnd()
                
                if c < 0.47:
                    glPointSize(3.0)
                    glBegin(GL_POINTS)
                    glVertex3f(0.1 + b, 0.1 + a, 0.0)
                    glVertex3f(0.13 + b, 0.13 + c, 0.42)
                    glEnd()
                    glBegin(GL_LINE_LOOP)
                    glColor4f(1.0, 1.0, 1.0, dead_transparency_line)
                    glVertex3f(0.1 + b, 0.1 + a, 0.0)
                    glVertex3f(0.13 + b, 0.13 + c, 0.42)
                    glVertex3f(0.13 + b, 0.13 + c, 0.42)
                    glEnd()
                
                glPointSize(3.0)
                glBegin(GL_POINTS)
                glVertex3f(0.1 + b, 0.1 + a, 0.0)
                glVertex3f(0.07 + b, 0.07 + c, 0.42)
                glVertex3f(0.07 + b, 0.07 + c, 0.42)
                glEnd()
                glBegin(GL_LINE_LOOP)
                glColor4f(1.0, 1.0, 1.0, dead_transparency_line)
                glVertex3f(0.1 + b, 0.1 + a, 0.0)
                glVertex3f(0.07 + b, 0.07 + c, 0.42)
                glVertex3f(0.07 + b, 0.07 + c, 0.42)
                glEnd()
                
                if c < 0.44:
                    glPointSize(3.0)
                    glBegin(GL_POINTS)
                    glVertex3f(0.1 + b, 0.1 + a, 0.0)
                    glVertex3f(0.17 + b, 0.16 + c, 0.44)
                    glVertex3f(0.17 + b, 0.16 + c, 0.44)
                    glEnd()
                    glBegin(GL_LINE_LOOP)
                    glColor4f(1.0, 1.0, 1.0, dead_transparency_line)
                    glVertex3f(0.1 + b, 0.1 + a, 0.0)
                    glVertex3f(0.17 + b, 0.16 + c, 0.44)
                    glVertex3f(0.17 + b, 0.16 + c, 0.44)
                    glEnd()
                
                glPointSize(3.0)
                glBegin(GL_POINTS)
                glColor4f(1.0, 1.0, 1.0, 0.05)
                glVertex3f(0.1 + b, 0.1 + c, 0.8)
                glVertex3f(0.1 + b, 0.1 + c, 0.8)
                glEnd()
                glBegin(GL_LINE_LOOP)
                glColor4f(1.0, 1.0, 1.0, dead_transparency_line)
                glVertex3f(0.1 + b, 0.1 + a, 0.4)
                glVertex3f(0.1 + b, 0.1 + c, 0.8)
                glVertex3f(0.1 + b, 0.1 + c, 0.8)
                glEnd()
                
                if c < 0.47:
                    glPointSize(3.0)
                    glBegin(GL_POINTS)
                    glVertex3f(0.1 + b, 0.1 + a, 0.42)
                    glVertex3f(0.13 + b, 0.13 + c, 0.82)
                    glVertex3f(0.13 + b, 0.13 + c, 0.82)
                    glEnd()
                    glBegin(GL_LINE_LOOP)
                    glColor4f(1.0, 1.0, 1.0, dead_transparency_line)
                    glVertex3f(0.1 + b, 0.1 + a, 0.0)
                    glVertex3f(0.13 + b, 0.13 + c, 0.82)
                    glVertex3f(0.13 + b, 0.13 + c, 0.82)
                    glEnd()
                
                glPointSize(3.0)
                glBegin(GL_POINTS)
                glColor4f(1.0, 1.0, 1.0, 0.05)
                glVertex3f(0.1 + b, 0.35, 1.2)
                glVertex3f(0.1 + b, 0.35, 1.2)
                glEnd()
                glBegin(GL_LINE_LOOP)
                glColor4f(1.0, 1.0, 1.0, dead_transparency_line)
                glVertex3f(0.1 + b, 0.1 + c, 0.8)
                glVertex3f(0.1 + a, 0.35, 1.2)
                glVertex3f(0.1 + a, 0.35, 1.2)
                glEnd()
                
                c += 0.1
            b += 0.1
        a += 0.1
    
    if flag:
        glPointSize(15.0)
        glBegin(GL_POINTS)
        glColor4f(0.0, 0.0, 1.0, 1.0)
        glVertex3f(0.3, 0.2, 0.0)
        glVertex3f(0.3, 0.3, 0.0)
        glVertex3f(0.3, 0.4, 0.0)
        glVertex3f(0.3, 0.5, 0.0)
        glVertex3f(0.3, 0.6, 0.0)
        glVertex3f(0.4, 0.5, 0.0)
        glVertex3f(0.2, 0.2, 0.0)
        glVertex3f(0.3, 0.2, 0.0)
        glVertex3f(0.4, 0.2, 0.0)
        glEnd()
        
        highlight_lines(0.3, 0.2, 0.0, live_transparency_line)
        highlight_lines(0.3, 0.3, 0.0, live_transparency_line)
        highlight_lines(0.3, 0.4, 0.0, live_transparency_line)
        highlight_lines(0.3, 0.5, 0.0, live_transparency_line)
        highlight_lines(0.3, 0.6, 0.0, live_transparency_line)
        highlight_lines(0.4, 0.5, 0.0, live_transparency_line)
        highlight_lines(0.2, 0.2, 0.0, live_transparency_line)
        highlight_lines(0.3, 0.2, 0.0, live_transparency_line)
        highlight_lines(0.4, 0.2, 0.0, live_transparency_line)
    
    glFlush()
    glutSwapBuffers()

# yRotated = 40


def reshape_network(x, y):
    if y == 0 or x == 0:
        return
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(40.0, float(x) / float(y), 0.5, 20.0)
    glViewport(0, 0, x, y)

def idle_network():
    global yRotated
    yRotated += 0.05
    display_network()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(1350, 1000)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"network Rotating Animation")
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    yRotated = 40
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    
    glutDisplayFunc(display_network)
    glutReshapeFunc(reshape_network)
    glutIdleFunc(idle_network)
    glutTimerFunc(100, check, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()