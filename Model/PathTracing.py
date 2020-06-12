from Model.Ray import *
import math
def intersectPoint(point, light=Ray(), walls=[Segmento()]):
    #Calcular la direccion de la luz al punto
    dir = light.getPosicion() - point
    #Calcular la distancia entre la luz y el punto
    lenght = Point.len(dir)

    #Se toma Point



def distancePointWall():
    pass