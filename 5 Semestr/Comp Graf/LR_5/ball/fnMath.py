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

def divisionIntoPolygons(ball3D):

    polygons = []

    for i in range(len(ball3D) - 1):
        for j in range(len(ball3D[0]) - 1):
            M1 = ball3D[i][j]
            M2 = ball3D[i][j + 1]
            M3 = ball3D[i + 1][j + 1]
            M4 = ball3D[i + 1][j]
            if not(round(M1[0]) == round(M2[0]) and round(M1[1]) == round(M2[1]) and round(M1[1]) == round(M2[1]) and round(M1[2]) == round(M2[2]) and round(M1[0]) == round(M2[0]) and round(M3[1]) == round(M4[1]) and round(M3[1]) == round(M4[1]) and round(M3[2]) == round(M4[2])):
                polygons.append((M1, M2, M3, M4))

    return polygons

def getXY(dot):
    xOld = dot[0]
    yOld = dot[1]
    zOld = dot[2]

    x =  - xOld * cos(pi / 4) + yOld * cos(pi / 4)
    y = zOld - xOld * sin(pi / 4)  - yOld * sin(pi / 4)

    return round(x), round(y)

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

def normalVector(dots):

    M1 = dots[0]
    M2 = dots[1]
    M3 = dots[2]
    M4 = dots[3]

    if round(M1[0]) == round(M2[0]) and round(M1[1]) == round(M2[1]) and round(M1[2]) == round(M2[2]):
        x1, y1, z1 = M1[0], M1[1], M1[2] 
        x2, y2, z2 = M3[0], M3[1], M3[2] 
        x3, y3, z3 = M4[0], M4[1], M4[2]
    else:
        x1, y1, z1 = M1[0], M1[1], M1[2] 
        x2, y2, z2 = M2[0], M2[1], M2[2] 
        x3, y3, z3 = M3[0], M3[1], M3[2]    

    xN = (y2 - y1) * (z3 - z1) - (z2 - z1) * (y3 - y1)
    yN = (z2 - z1) * (x3 - x1) - (x2 - x1) * (z3 - z1)
    zN = (y3 - y1) * (x2 - x1) - (y2 - y1) * (x3 - x1)

    return xN, yN, zN
