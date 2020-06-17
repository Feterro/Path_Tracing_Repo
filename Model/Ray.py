from Model.Segmento import *
import random
import Model.Funtions as fun
import math as mt
class Ray:

    def __init__(self, pPosicion=Point(10, 10), pDireccion=Point(20,10)):
        self.direccion = Point()
        self.posicion = pPosicion
        self.setDireccion(pDireccion)
        self.final = Point(pPosicion.x, pPosicion.y)
        self.largo = 500

    def getDireccion(self):
        return self.direccion

    def getPosicion(self):
        return self.posicion

    def setDireccion(self, pDireccion):
        self.direccion.x = pDireccion.x - self.posicion.x
        self.direccion.y = pDireccion.y - self.posicion.y
        self.direccion = fun.normalize(self.direccion)

    def setRealDirection(self, pDirection):
        self.direccion = pDirection

    def setDirectionFromAngle(self, angle):

        x = mt.cos(mt.radians(-angle))
        y = mt.sin(mt.radians(-angle))
        if x > 1:
            x = 0
        if y > 1:
            y = 0

        self.direccion = Point(x, y)

    def setFinal(self, pFinal):

        self.final = pFinal
        largo = fun.pointsDistance(self.posicion, self.final)

        if (self.largo - largo) > 0:
            return True
        else:
            return False

    def getFinal(self):
        return self.final

    def generarDir(self):
        coor=random.randint(0,1)
        num=random.randint(0,1)
        pDireccion = Point()
        pDireccion.x = 500
        pDireccion.y = 500
        if coor==0:
            pDireccion.y = 0
            pDireccion.x = 0
        if num==0:
            pDireccion.x = random.randint(0,500)
        else:
            pDireccion.y = random.randint(0, 500)
        self.setDireccion(pDireccion)


    def generarRay(self):
        #Dado un rayo se genera otro por el choque con una pared

        pDireccion = self.direccion

        pPosicion = self.final


        print("{}, {}".format(pDireccion.x, pDireccion.y))
        ray = Ray(pPosicion=pPosicion)
        ray.setRealDirection(pDireccion)
        ray.largo = self.largo

        return ray

def reboteRayos(light=Ray(), wall=Segmento()):
    pass

