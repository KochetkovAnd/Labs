from math import *

def getBall3D(R, numberOfSteps):    
    ball3D = []

    z = - R
    stepZ = 2 * R / (numberOfSteps - 1)
    
    for i in range(numberOfSteps):
        temp1 = []
        temp2 = []
        Rz = sqrt(abs(pow(R, 2) - pow(z, 2)))
        x = - Rz
        stepX = 2 * Rz / (numberOfSteps - 1)
        for j in range(numberOfSteps):            
            y1 = sqrt(abs(pow(Rz, 2) - pow(x, 2)))
            y2 = -sqrt(abs(pow(Rz, 2) - pow(x, 2)))
            temp1.append((x, y1, z))
            temp2.append((x, y2, z))
            x += stepX
        temp2.reverse()
        ball3D.append(temp1 + temp2)
        z += stepZ
    return ball3D

def affinProjection(ball3D, a, b):
    
    projection = []

    for i in range(len(ball3D)):
        temp = []
        for j in range(len(ball3D[0])):
            dot = ball3D[i][j]
            xOld = dot[0]
            yOld = dot[1]
            zOld = dot[2]
            xNew = xOld * cos(a) + yOld * sin(a)
            yNew = - xOld * sin(a) * cos(b) + yOld * cos(a) * cos(b) + zOld * sin(b)
            zNew = xOld * sin(a) * sin(b) - yOld * cos(a) * sin(b) + zOld * cos(b)
            temp.append((xNew, yNew, zNew))
        projection.append(temp)

    return projection

def projectionToPrint(ball3D):
    ball2D = []
    for i in range(len(ball3D)):
        temp = []
        for j in range(len(ball3D[0])):
            dot = ball3D[i][j]
            xOld = dot[0]
            yOld = dot[1]
            zOld = dot[2]
            x =  - xOld * cos(pi / 4) + yOld * cos(pi / 4)
            y = zOld - xOld * sin(pi / 4)  - yOld * sin(pi / 4)
            temp.append((x, y))
        ball2D.append(temp)    
    return ball2D


def affin1(figure, kx, ky, kz):
    figureafter = []

    for i in range(len(figure)):
        temp = []
        for j in range(len(figure[0])):
            dot = figure[i][j]
            xOld = dot[0]
            yOld = dot[1]
            zOld = dot[2]
            xNew = xOld * kx
            yNew = yOld * ky
            zNew = zOld * kz
            temp.append((xNew, yNew, zNew))
        figureafter.append(temp)

    return figureafter 

def affin2(figure, a):
    figureafter = []

    for i in range(len(figure)):
        temp = []
        for j in range(len(figure[0])):
            dot = figure[i][j]
            xOld = dot[0]
            yOld = dot[1]
            zOld = dot[2]
            xNew = xOld
            yNew = yOld * cos(a) - zOld * sin(a)
            zNew = yOld * sin(a) + zOld * cos(a)
            temp.append((xNew, yNew, zNew))
        figureafter.append(temp)

    return figureafter 

def affin3(figure, a):
    figureafter = []

    for i in range(len(figure)):
        temp = []
        for j in range(len(figure[0])):
            dot = figure[i][j]
            xOld = dot[0]
            yOld = dot[1]
            zOld = dot[2]
            xNew = xOld + a 
            yNew = yOld 
            zNew = zOld 
            temp.append((xNew, yNew, zNew))
        figureafter.append(temp)

    return figureafter 