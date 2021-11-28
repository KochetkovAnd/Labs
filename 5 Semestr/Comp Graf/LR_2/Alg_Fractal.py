from tkinter import *
from math import *
from time import *

xMin = -2
xMax = 2
yMin = -2
yMax = 2

Side = 50
Width = int(Side * (xMax - xMin))
Height = int(Side * (yMax - yMin))
N = 49
#sfgsdfsdf

Colors = ["#9b2226","#ae2012","#bb3e03","#ca6702","#ee9b00","#e9d8a6","#94d2bd","#0a9396","#005f73","#001219"]

root = Tk()
canvas = Canvas(root, width=Width, height=Height)
canvas.pack()

for i in range(Width):
    for j in range(Height):

        n = 0
        z0 = complex (i / Side - abs(xMin), j / Side - abs(yMin) )
        z = complex (i / Side - abs(xMin), j / Side - abs(yMin) )

        while(abs(z) <= 2) and (n < N):
            z = z * z * z+ z0
            n += 1
        if(n > 50):
            print (n)

        
        n = n // 5
        
        canvas.create_rectangle((z0.real + abs(xMin)) * Side, (z0.imag + abs(yMin)) * Side,(z0.real + abs(xMin)) * Side + 1,(z0.imag + abs(yMin)) * Side  + 1, fill=Colors[n], width=0)

        root.update()
sleep(10)