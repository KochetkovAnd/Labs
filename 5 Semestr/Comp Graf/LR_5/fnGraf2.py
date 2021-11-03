from math import pi
from PyQt5.QtGui import QPixmap
from PIL import Image
from PIL.ImageQt import ImageQt

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

def showImage(image, picture):
    image.hide()
    qim = ImageQt(picture)
    pixmapImage = QPixmap.fromImage(qim)
    w, h = image.width(), image.height()
    pixmapImage = pixmapImage.scaled(w, h)
    #pixmapImage = pixmapImage.scaled(w, h, Qt.KeepAspectRatio)
    image.setPixmap(pixmapImage)
    image.show()

def lineBresenham(img, color, x0, y0, x1, y1): #Инкрементный алгоритм Брезенхама для линии
    if abs(x0 - x1) >= abs(y0 - y1):
        if x1 == x0:    
            for y in range(min(y0, y1), max(y0, y1)):
                img.putpixel((x0, y), color)
            
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

            img.putpixel((x, y), color)

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
                img.putpixel((x, y), color)
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

        img.putpixel((x, y), color)

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
            img.putpixel((x, y), color)
            i+=1
