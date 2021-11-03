from fm

def start(R, step, img):  

    image = Image.new(mode = "RGB", size = (frameSize, frameSize), color=white)
    addAxles(image)
    figure = getBall3D(R, step)
    polygons = divisionIntoPolygons(figure)
    printPolygons(polygons, image)
    showImage(img, image)

    return figure  