from skimage.draw import line

from Model.Ray import *
from Model.Segmento import *
from Model.Funtions import *
from numpy import *
#TODO ColorBlind

def intersectPoint(light=Ray(), walls=[Segmento()], devolucion=False):
    paredes=[]
    dictPoints = {}
    for wall in walls:
        point = raySegmentIntersect(light, wall)
        # if wall.transparencia==True:
        #      point=None
        if point is not None:
            dist=pointsDistance(point, light.posicion)
            dictPoints[dist] = point
            paredes.append([point, wall])

    if len(dictPoints) > 0:
        point = dictPoints[min(dictPoints.keys())]
        if point.x == light.posicion.x and point.y == light.posicion.y:
            del dictPoints[min(dictPoints.keys())]

        if len(dictPoints) > 0:
            minimo=dictPoints[min(dictPoints.keys())]
            if devolucion:
                for pard in paredes:
                    if pard[0]==minimo:
                        return pard[1]
            else:
                return minimo
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

def pathTrace(luces, reflejos, paredes, blankImage, lucesEfectivas):
    from time import time
    pixelesIndirecta = getImageBlank()
    pixelesDirecta = getImageBlank()
    matrizIntensidadDirecta = [[0] * 500] * 500
    matrizIntensidadIndirecta = [[0] * 500] * 500
    img = getArrayImage()
    # Start counting.
    start_time = time()

    luzDirecta(luces, blankImage, img, pixelesDirecta, matrizIntensidadDirecta)
    luzIndirecta(reflejos, blankImage, img, lucesEfectivas, pixelesIndirecta, matrizIntensidadIndirecta)
    luzGlobal(blankImage, lucesEfectivas, pixelesDirecta, pixelesIndirecta, luces, reflejos,
              matrizIntensidadDirecta, matrizIntensidadIndirecta)

    # Calculate the elapsed time.
    elapsed_time = time() - start_time
    elapsed_time = "Elapsed time: %0.2f seconds." % elapsed_time
    print(elapsed_time)

def luzIndirecta(reflejos, blankImage, img, lucesEfectivas, pixelesIndirecta, matrizIntensidad):
    for reflejo in reflejos:
        puntosx, puntosy = line( reflejo.posicion.x, reflejo.posicion.y, reflejo.final.x, reflejo.final.y)
        for i in range(len(puntosx)):
            px = puntosx[i] - 1
            py = puntosy[i] - 1

            try:
                lucesEfectivas[px][py] += 1
            except IndexError:
                print(px, py)
            distanciaReflejo = pointsDistance(reflejo.posicion, Point(px, py))
            distanciaLuzDirecta = reflejo.distancia
            distanciaTotal = distanciaReflejo + distanciaLuzDirecta

            intensity = (1 - (distanciaTotal / 500)) ** 2

            try:
                matrizIntensidad[px][py] = max(matrizIntensidad[px][py], intensity)
            except IndexError:
                print(px, py)
            color = (img[int(py)][int(px)])[:3]
            colorWall2 = array([color / 100 for color in img[reflejo.posicion.y-1][reflejo.posicion.x-1][:3]])
            #color = color * intensity * colorWall2
            color = color * colorWall2  * math.acos(radians(reflejo.direccion.x))
            pixelesIndirecta[px][py] =  add(blankImage[px][py], color//2)// 2
            blankImage[px][py] = pixelesIndirecta[px][py]


    print("Luz indirecta calculada")

def luzDirecta(luces, blankImage, img, pixelesDirecta, matrizIntensidad):

    numeroRayos = 0
    for luz in luces:
        numeroRayos += 1
        puntosx, puntosy = line(luz.posicion.x, luz.posicion.y, luz.final.x, luz.final.y)
        for i in range(len(puntosx)-1):

            px = puntosx[i]
            py = puntosy[i]

            intensity = (1 - (pointsDistance(luz.posicion, Point(px, py)) / 500)) ** 2
            matrizIntensidad[px][py] = max(matrizIntensidad[px][py], intensity)
            color = (img[int(py)][int(px)])[:3]

            color = color * math.acos(radians(luz.direccion.x)) * matrizIntensidad[px][py]
            blankImage[px][py] = add(blankImage[px][py], color//2)  // 2
            pixelesDirecta[px][py] = blankImage[px][py]

    print("Luz directa calculada")

def luzGlobal(blankImage, lucesEfectivas, pixelesDirecta, pixelesIndirecta, luces, reflejos,
              matrizIntensidadDirecta, matrizIntensidadIndirecta):

    print("Luz global")
    for reflejo in (reflejos+luces):
        puntosx, puntosy = line(reflejo.posicion.x, reflejo.posicion.y, reflejo.final.x, reflejo.final.y)
        for i in range(len(puntosx)):
            px = puntosx[i]
            py = puntosy[i]
            blankImage[px-1][py-1] = (pixelesDirecta[px-1][py-1]*1.5 + pixelesIndirecta[px-1][py-1]*0.5) // 2
    print("Luz global terminada")

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