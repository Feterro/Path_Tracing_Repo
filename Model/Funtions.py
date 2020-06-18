import math
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


def anguloEntreRectas(light, wall):
    numerador = light.posicion.y - light.final.y
    denominador = light.posicion.x - light.final.x
    m1 = 0
    if denominador != 0:
        pendiente = numerador / denominador

    numerador = wall.seccion[0].y - wall.seccion[1].y
    denominador = wall.seccion[0].x - wall.seccion[1].x
    m2 = 0
    if denominador != 0:
        m2 = numerador / denominador
    if(1 + m1 *m2) != 0:
        angulo = math.atan(m1 - m2 / 1 + m1 * m2)
        return angulo
    else:
        return False