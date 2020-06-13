from Model.Ray import *
import math

def intersectPoint(light=Ray(), walls=[Segmento()]):

    dictPoints = {}
    for wall in walls:

        point = raySegmentIntersect(light.getPosicion(), light.getDireccion()
                ,wall.getSeccion()[0], wall.getSeccion()[1])
        if point is not None:
            dictPoints[length(point)] = point


    return dictPoints[min(dictPoints.keys())]


def raySegmentIntersect(ori, dir, p1, p2):
    # calculate vectors
    v1 = ori - p1
    v2 = p2 - p1
    v3 = Point(-dir.y, dir.x)

    dot = v2.dot(v3)
    if abs(dot) < 0.000001:
        return -1.0

    t = v2.cross(v1) / dot
    u = v1.dot(v3) / dot

    if t >= 0.0 and (0.0 <= u <= 1.0):
        # X de P: x1 + t(x2 - x1)
        # Y de P: y1 + t(y2 - y1)
        #ori(x1, y1) => dir(x2, y2)
        pointInt = ori.makePoint(t, dir)
        return pointInt

    return None

def length(v1):
    #assumes v1 starts at (0,0)
    return math.sqrt(v1.x*v1.x + v1.y*v1.y)