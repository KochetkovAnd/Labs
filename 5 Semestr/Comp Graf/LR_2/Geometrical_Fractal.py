from math import *
from tkinter import *
from time import *

N = 40
H = 3
PAUSE = 0.001

ANGLE = pi / 4
str = "F++F++F++F"
rule = "-F++F-"

Height = 800
Width = 1200

def step(str):
    res = ""
    for s in str:
        if s == 'F':
            res += rule
        else:
            res += s
    #print(res)
    return res

class my_turtle:
    def __init__(self,x,y,angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.data = []
    def centr(self):
        self.x = Width / 2
        self.y = Height / 2
    def forward(self):
        canvas.create_line(self.x, self.y, self.x + H * cos(self.angle), self.y - H * sin(self.angle))
        self.x += H * cos(self.angle)
        self.y -= H * sin(self.angle)
    def left(self):
        self.angle -= ANGLE
    def right(self):
        self.angle += ANGLE
    def safe(self):
        self.data.append([self.x, self.y, self.angle])
    def get(self):
        info = self.data.pop()
        self.x = info[0]
        self.y = info[1]
        self.angle = info[2]



root = Tk()
canvas = Canvas(root, width=Width, height=Height)
canvas.pack()

tr = my_turtle(Width / 2, Height / 2, pi / 2)



for i in range(N):    
    canvas.delete("all")
    tr.centr()
    for s in str:
        if s == "F":
            tr.forward()
        elif s == "-":
            tr.left()
        elif s == "+":
            tr.right()
        elif s == "[":
            tr.safe()
        elif s == "]":
            tr.get()
        #sleep(PAUSE)
        root.update()
    str = step(str) 
    sleep(1)