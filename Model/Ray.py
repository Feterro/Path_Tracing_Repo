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
        self.lucesIndirectas = 2

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

    def rebotar(self, bordes, paredes):
        from Model.PathTracing import intersectPoint
        lucesIndirectas = []

        for i in range(self.lucesIndirectas):
            luzIndirecta = reboteRayos(self, bordes)
            final = intersectPoint(luzIndirecta, paredes)
            if final is not None:
                luzIndirecta.setFinal(final)

                lucesIndirectas.append(luzIndirecta)

        return  lucesIndirectas

def reboteRayos(light, bordes):
    import Model.PathTracing as PT
    #Reflexion
    puntoRef = PT.intersectPoint(light, bordes)
    luzIndirecta = Ray(pPosicion=light.final)

    if puntoRef.y == 0:
        luzIndirecta.setDirectionFromAngle(random.randint(181, 359))

    elif puntoRef.y == 500:
        luzIndirecta.setDirectionFromAngle(random.randint(1, 179))

    elif puntoRef.x == 0:
        if random.randint(0, 1) == 0:
            luzIndirecta.setDirectionFromAngle(random.randint(1, 89))

        else:
            luzIndirecta.setDirectionFromAngle(random.randint(271, 359))

    elif puntoRef.x == 500:
        luzIndirecta.setDirectionFromAngle(random.randint(89, 269))

    return luzIndirecta

