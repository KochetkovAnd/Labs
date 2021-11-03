#def addBall(R, step, image):
#    ball3D = getBall3D(R, step)
#    ball2D = projectionToPrint(ball3D)
#    printBall(ball2D, image)   
#
#    return ball3D

#def printBall(ball2D, image):
#
#    for i in range (len(ball2D)):
#        for j in range (len(ball2D[0]) - 1):            
#
#            x0 = round(ball2D[i][j][0]) + n
#            y0 = round(ball2D[i][j][1]) + n
#
#            x1 = round(ball2D[i][j + 1][0]) + n
#            y1 = round(ball2D[i][j + 1][1]) + n
#            
#            lineBresenham(image, black, x0, y0, x1, y1)
#
#    for i in range (len(ball2D) - 1):
#        for j in range (len(ball2D[0])):
#
#            x0 = round(ball2D[i][j][0]) + n
#            y0 = round(ball2D[i][j][1]) + n
#
#            x1 = round(ball2D[i + 1][j][0]) + n
#            y1 = round(ball2D[i + 1][j][1]) + n
#            
#            lineBresenham(image, black, x0, y0, x1, y1)