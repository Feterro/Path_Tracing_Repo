from Model.Ray import *
from Model.Segmento import *
from Model.Funtions import *


def intersectPoint(light=Ray(), walls=[Segmento()]):

    dictPoints = {}
    for wall in walls:

        point = raySegmentIntersect(light, wall)
        if point is not None:
            dictPoints[length(point)] = point

    if len(dictPoints) != 0:
        return dictPoints[min(dictPoints.keys())]
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
