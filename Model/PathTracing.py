from skimage.draw import line

from Model.Ray import *
from Model.Segmento import *
from Model.Funtions import *
from numpy import *

#TODO ColorBlind
#TODO Especularidad

def intersectPoint(light=Ray(), walls=[Segmento()]):

    dictPoints = {}
    for wall in walls:

        point = raySegmentIntersect(light, wall)
        if point is not None:
            dictPoints[pointsDistance(point, light.posicion)] = point

    if len(dictPoints) > 0:
        point = dictPoints[min(dictPoints.keys())]
        if point.x == light.posicion.x and point.y == light.posicion.y:
            del dictPoints[min(dictPoints.keys())]

        if len(dictPoints) > 0:
            return dictPoints[min(dictPoints.keys())]
        else:
            return None
    else:
        return None

def raySegmentIntersect(ray, wall):
    # ori (x1, y1)
    # dir (x2, y2)
    # segInicio (x3, y3)
    # segFinal (x4, y4)

    # calculate vectors
    v1 = ray.getPosicion() - wall.seccion[0]
    v2 = wall.seccion[1] - wall.seccion[0]
    v3 = Point(-ray.getDireccion().y, ray.getDireccion().x)

    dot = v2.dot(v3)

    if abs(dot) < 0.000001:
        return None

    t = v2.cross(v1) / dot
    u = v1.dot(v3) / dot
    #print("[ {}, {}, {}, {}]".format(t, u, ray.posicion, ray.direccion))
    if t >= 0.0 and (0.0 <= u <= 1.0):
        # X de P: x1 + t(x2 - x1)
        # Y de P: y1 + t(y2 - y1)
        #ori(x1, y1) => dir(x2, y2)
        pointInt = makePoint(ray.posicion, t, ray.direccion)

        return pointInt

    return None

def raySegmentIntersect2(ori, dir, p1, p2):
    # ori (x1, y1)
    # dir (x2, y2)
    # segInicio (x3, y3)
    # segFinal (x4, y4)

    det = (ori.x - dir.x) * (p1.y - p2.y) - (ori.y - dir.y) * (p1.x - p2.x)

    if det is 0:
        return None

    t = (ori.x - p1.x) * (p1.y - p2.y) - (ori.y - p1.y) * (p1.x - p2.x) / det
    u = -((ori.x - dir.x) * (p1.y - p2.y) - (ori.y - dir.y) * (p1.y - p2.y)) / det
    print("[ {}, {}, {}, {}]".format(t, u, ori, dir))
    if t >= 0.0 and (0.0 <= u <= 1.0):
        # X de P: x1 + t(x2 - x1)
        # Y de P: y1 + t(y2 - y1)
        # ori(x1, y1) => dir(x2, y2)
        pointInt = ori.makePoint(t, dir)

        return pointInt

    return None

    pass

def makePoint(posicion, t, direccion):
    normalizeDirection = normalize(direccion)
    x = posicion.x + normalizeDirection.x * t
    y = posicion.y + normalizeDirection.y * t
    point = Point(int(x), int(y))
    return point

def pathTrace(luces, reflejos, paredes, blankImage, pixeles):

    img = getArrayImage()
    luzIndirecta(reflejos, blankImage, img, pixeles)
    luzDirecta(luces, blankImage, img, pixeles)

def luzIndirecta(reflejos, blankImage, img, pixeles):

    for reflejo in reflejos:
        puntosx, puntosy = line( reflejo.posicion.x, reflejo.posicion.y, reflejo.final.x, reflejo.final.y)
        for i in range(len(puntosx)):
            px = puntosx[i]
            py = puntosy[i]

            if str(px) + str(py) in pixeles:
                pixeles[str(px) + str(py)] += 1
            else:
                pixeles[str(px) + str(py)] = 1

            intensity =  (reflejo.intensidad - (pointsDistance(reflejo.posicion, Point(px, py)) / 500)) ** 2
            values = (img[int(py) - 1][int(px) - 1])[:3]
            colorDominante = max(values.tolist())
            colorPorcen = values / array([colorDominante,colorDominante,colorDominante])
            luzTemporal = array([1, 1, 0.75])
            luzTemporal = luzTemporal + (luzTemporal*colorPorcen)

            values = values * intensity * luzTemporal
            values = add(blankImage[px - 1][py - 1], values) / pixeles[str(px) + str(py)]
            blankImage[px - 1][py - 1] = values

def luzDirecta(luces, blankImage, img, pixeles={}):

    for luz in luces:
        luzTemporal = array([1, 1, 0.75])
        puntosx, puntosy = line(luz.posicion.x, luz.posicion.y, luz.final.x, luz.final.y)

        for i in range(len(puntosx)):
            px = puntosx[i]
            py = puntosy[i]
            intensity = (1 - (pointsDistance(luz.posicion, Point(px, py)) / 500)) ** 2
            values = (img[int(py) - 1][int(px) - 1])[:3]
            values = values * intensity * luzTemporal
            values = add(blankImage[px - 1][py - 1], values) / 2
            blankImage[px - 1][py - 1] = values

def functionRay(Ray, x):
    #esta funcion retorna un y dado un x
    #calcular la pendiente
    x1 = Ray.posicion.x
    y1 = Ray.posicion.y
    x2 = Ray.final.x
    y2 = Ray.final.y

    if x2 - x1 == 0:
        return False
    m = (y2 - y1) / (x2 - x1)

    y = m*(x -x1) + y1

    return y