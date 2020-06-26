import math
import random
from Model.Segmento import Segmento
def length(v1):
    #Assumes v1 starts at (0,0)
    return math.sqrt(v1.x * v1.x + v1.y * v1.y)

def pointsDistance(v1, source):

    return math.sqrt((source.x - v1.x)**2 + (source.y - v1.y)**2)

def normalize(v1):
    #assumes v1 starts at (0,0)
    v1 = v1 / length(v1)
    return v1

def getArrayImage():

    from PIL import Image
    import numpy as np
    imgName = "C:/Users/edfsedf/Documents/GitHub/Path_Tracing_Repo/Model/roomBleed2.png"
    # reference image for background color
    im_file = Image.open(imgName)
    ref = np.array(im_file)
    return ref

def getImageBlank():
    from PIL import Image
    import numpy as np
    i = Image.new("RGB", (500, 500), (0, 0, 0))
    px = np.array(i)
    return px

def getDireccionLuz(ray, segmento):
    if segmento.seccion[0].x == segmento.seccion[1].x:
        if segmento.seccion[0].x > ray.posicion.x:
            return "der"
        else:
            return "izq"
    else:
        if segmento.seccion[0].y > ray.posicion.y:
            return "aba"
        else:
            return "arr"

def pendiente(puntoIni,puntoFin):
    return puntoFin.y-puntoIni.y/puntoFin.x-puntoIni.x


def anguloIncidencia(ray, auxiliar):
    rayoAuxiliar = auxiliar
    longOpue = rayoAuxiliar.final.y-rayoAuxiliar.posicion.y
    longAdya = ray.final.x-rayoAuxiliar.final.x
    angRad = math.atan(longOpue/longAdya)
    return abs(math.degrees(angRad))