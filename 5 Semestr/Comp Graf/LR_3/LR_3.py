from PIL import Image
from math import *

width = 900
height = 600

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
pink = (255, 0, 255)
color = (102, 102, 102)

pattern_width = 4
pattern_height = 4
colors = [red, green, blue, pink, color]
pattern = [
    [red, red, red, green],
    [red, blue, green, pink],
    [red, green, blue, pink],
    [green, pink, pink, pink]
    ]


white = (255, 255, 255)
black = (0, 0, 0)


img = Image.new(mode = "RGB", size = (width, height), color=white) 

def lineSimple(x0, y0, x1, y1): #Простой алгоритм построения линии
    if x1 != x0 and y1 != y0:
        a = (y1 - y0) / (x1 - x0)
        b = y0 - x0 * a
        if abs(x1 - x0) > abs(y1 - x0):
            for x in range(min(x0, x1), max(x0, x1)):
                img.putpixel((x, a * x + b), black)
        else:
            for y in range(min(y0, y1), max(y0, y1)):
                img.putpixel((round((y - b) / a), y), black)
    elif x1 == x0:
        for y in range(min(y0, y1), max(y0, y1)):
            img.putpixel((x0, y), black)
    else:
        for x in range(min(x0, x1), max(x0, x1)):
            img.putpixel((x, y0), black)

def lineBresenham(x0, y0, x1, y1): #Инкрементный алгоритм Брезенхама для линии
    if abs(x0 - x1) >= abs(y0 - y1):
        if x1 == x0:    
            for y in range(min(y0, y1), max(y0, y1)):
                img.putpixel((x0, y), black)
            
        else:
            if x0 < x1:
                x = x0
                y = y0
                dx = x1 - x0
                dy = y1 - y0
            else:
                x = x1
                y = y1
                dx = x0 - x1
                dy = y0 - y1

            m = abs(dy / dx)
            e = m - 1 / 2
            i = 0

            img.putpixel((x, y), black)

            while i < dx:
                if e >= 0:
                    if dy >= 0:
                        y += 1
                    else:
                        y -= 1
                    e += m - 1
                else:
                    e +=m
                x += 1
                img.putpixel((x, y), black)
                i+=1
    else:
        if y0 < y1:
            x = x0
            y = y0
            dy = y1 - y0
            dx = x1 - x0
            
        else:
            x = x1
            y = y1
            dy = y0 - y1
            dx = x0 - x1
            

        m = abs(dx / dy)
        e = m - 1 / 2
        i = 0

        img.putpixel((x, y), black)

        while i < dy:
            if e >= 0:
                if dx >= 0:
                    x += 1
                else:
                    x -= 1
                e += m - 1
            else:
                e +=m
            y += 1
            img.putpixel((x, y), black)
            i+=1



def circleSimple(x0, y0, R): #Простой метод построения окружности
    xstart = x0 - R
    y1start = y0
    y2start = y0
    
    for i in range(x0 - R, x0 + R + 1):
        x = i 
        y1 = round(y0 + sqrt(R * R - pow(x - x0, 2)))
        y2 = round(y0 - sqrt(R * R - pow(x - x0, 2)))
        lineBresenham(xstart, y1start, x, y1)
        lineBresenham(xstart, y2start, x, y2)
        xstart = x
        y1start = y1
        y2start = y2

def circleParametric(x0, y0, R, c1, c2): #Параметрический метод построения окружности
    x1 = x0 + R
    y1 = y0

    for alfa in range(1, 360):
        radian = alfa * pi / 180
        x2 = x0 + R * cos(c1 * radian)
        y2 = y0 + R * sin(c2 * radian)
        lineBresenham(round(x1), round(y1), round(x2), round(y2))
        x1 = x2
        y1 = y2

def circleBresenham(x, y, R):
    x0 = x
    y0 = y
    x = 0
    y = R
    delta = 1 - 2 * R
    error = 0
    while y >= 0:
        img.putpixel((x0 + x, y0 + y), black)
        img.putpixel((x0 + x, y0 - y), black)
        img.putpixel((x0 - x, y0 + y), black)
        img.putpixel((x0 - x, y0 - y), black)

        error = 2 * (delta + y) - 1
        if delta < 0 and error <= 0:
            x += 1
            delta += (2 * x + 1)
            continue
        error = error = 2 * (delta - x) - 1
        if delta > 0 and error > 0:
            y -= 1
            delta += 1 - 2 * y 
            continue
        x += 1
        delta += 2 * (x - y)
        y -= 1

def paintSimple(x0, y0, color):
    img.putpixel((x0, y0), color)

    if  not(img.getpixel((x0 + 1, y0)) in colors) and img.getpixel((x0 + 1, y0)) != black:
        paintSimple(x0 + 1, y0, color)

    if not(img.getpixel((x0 - 1, y0)) in colors) and img.getpixel((x0 - 1, y0)) != black:
        paintSimple(x0 - 1, y0, color)

    if not(img.getpixel((x0, y0 + 1)) in colors) and img.getpixel((x0, y0 + 1)) != black:
        paintSimple(x0, y0 + 1, color)

    if not(img.getpixel((x0, y0 - 1)) in colors) and img.getpixel((x0, y0 - 1)) != black:
        paintSimple(x0, y0 - 1, color)

def paintCoroed(x0, y0):

    pixels = []
    pixels.append((x0, y0))
    while True:
        pixel = pixels.pop()
        if img.getpixel(pixel) != color and img.getpixel(pixel) != black:
            img.putpixel(pixel, pattern[pixel[0] % pattern_width][pixel[1] % pattern_height])
            if  not(img.getpixel((pixel[0] + 1, pixel[1])) in colors) and img.getpixel((pixel[0] + 1, pixel[1])) != black:
                pixels.append((pixel[0] + 1, pixel[1]))

            if not(img.getpixel((pixel[0] - 1, pixel[1])) in colors) and img.getpixel((pixel[0] - 1, pixel[1])) != black:
                pixels.append((pixel[0] - 1, pixel[1]))

            if not( img.getpixel((pixel[0], pixel[1] + 1)) in colors) and img.getpixel((pixel[0], pixel[1] + 1)) != black:
                pixels.append((pixel[0], pixel[1] + 1))

            if not(img.getpixel((pixel[0], pixel[1] - 1)) in colors) and img.getpixel((pixel[0], pixel[1] - 1)) != black:
                pixels.append((pixel[0], pixel[1] - 1))
        if len(pixels) == 0:
            break

def paintSimpleBetter(x0, y0, color):    

    
    pixels = []
    pixels.append((x0, y0))
    while len(pixels) != 0:        
        pixel = pixels.pop()
        x0 = pixel[0]
        y0 = pixel[1]    

        x = x0

        img.putpixel((x, y0), color)
        while img.getpixel((x, y0)) != black:
            img.putpixel((x, y0), color)
            x -= 1
        xLeft = x + 1

        x = x0

        img.putpixel((x, y0), color)
        while img.getpixel((x, y0)) != black:            
            img.putpixel((x, y0), color)
            x += 1
        xRight = x - 1

        if img.getpixel((xLeft, y0 + 1)) != black and img.getpixel((xLeft, y0 + 1)) != color:
            pixels.append((xLeft, y0 + 1))
        if img.getpixel((xLeft, y0 - 1)) != black and img.getpixel((xLeft, y0 - 1)) != color:
            pixels.append((xLeft, y0 - 1))


        for i in range (xLeft + 1, xRight):            

            if img.getpixel((i + 1, y0 + 1)) == black and img.getpixel((i, y0 + 1)) == white:
                pixels.append((i, y0 + 1))
            elif img.getpixel((i - 1, y0 + 1)) == black and img.getpixel((i, y0 + 1)) == white:
                pixels.append((i, y0 + 1)) 

            if img.getpixel((i + 1, y0 - 1)) == black and img.getpixel((i, y0 - 1)) == white:
                pixels.append((i, y0 - 1))
            elif img.getpixel((i - 1, y0 - 1)) == black and img.getpixel((i, y0 - 1)) == white:
                pixels.append((i, y0 -  1))

        if img.getpixel((xRight, y0 + 1)) != black and img.getpixel((xRight, y0 + 1)) != color:
            pixels.append((xRight, y0 + 1))
        if img.getpixel((xRight, y0 - 1)) != black and img.getpixel((xRight, y0 - 1)) != color:
            pixels.append((xRight, y0 - 1))

def Curve(dots):
    t = 0
    while t <= 1:
        x, y = findDot(dots, t)
        img.putpixel((round(x), round(y)), black)
        t += 0.001
        
def findDot(dots, t):
    while len(dots) != 1:
        curDots = []
        for i in range(0, len(dots) - 1):
            x = dots[i][0] + (dots[i + 1][0] - dots[i][0]) * t
            y = dots[i][1] + (dots[i + 1][1] - dots[i][1]) * t
            curDots.append((x, y))
        dots = curDots
    return dots[0]


lineBresenham(100, 100, 150, 140)
lineBresenham(150, 140, 200, 100)
lineBresenham(200, 100, 200, 120)
lineBresenham(200, 120, 160, 150)
lineBresenham(160, 150, 200, 180)
lineBresenham(200, 180, 200, 200)
lineBresenham(200, 200, 150, 160)
lineBresenham(150, 160, 100, 200)
lineBresenham(100, 200, 125, 150)
lineBresenham(125, 150, 100, 100)

paintSimpleBetter(130, 150, blue)

circleParametric(400, 100, 50, 1, 1)
paintCoroed(400, 100)

circleSimple(600, 100, 50)


lineSimple(595, 95, 605, 95)
lineSimple(605, 95, 605, 105)
lineSimple(605, 105, 595, 105)
lineSimple(595, 105, 595, 95)
paintCoroed(570, 100)
paintSimple(600, 100, red)

circleBresenham(500, 400, 50)

dots =[(200, 200), (300, 100), (400, 400), (500, 200)]
Curve(dots)

circleParametric(400, 300, 50, 10, 6)

img.show()