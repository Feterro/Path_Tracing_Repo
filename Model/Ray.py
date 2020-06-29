
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
        self.lucesIndirectas = 1
        self.angle = 0

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
        self.angle = angle
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
        if coor == 0:
            pDireccion.y = 0
            pDireccion.x = 0
        if num == 0:
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

    def rebotar(self, paredes):
        from Model.PathTracing import intersectPoint
        lucesIndirectas = []
        for i in range(self.lucesIndirectas):
            paredChoque=intersectPoint(self,paredes,True)
            if paredChoque.especularidad:
                reflejo=reboteEspecular(self,paredes)
            else:
                reflejo = reboteRayos(self, paredes)
            final = intersectPoint(reflejo, paredes)
            if final is not None:
                reflejo.setFinal(final)
                reflejo.setIntensidad(self)
                lucesIndirectas.append(reflejo)

        return lucesIndirectas

class Reflejo(Ray):
    #TODO agregar atributo
    def __init__(self,  pPosicion=Point(10, 10), pDireccion=Point(20,10)):
        Ray.__init__(self, pPosicion, pDireccion)
        self.distancia = 1

    def setIntensidad(self, Ray):
        self.distancia = fun.pointsDistance(Ray.posicion, self.posicion)

import Model.PathTracing as PT

def reboteRayos(light, paredes):

    paredChoque= PT.intersectPoint(light, paredes, True)
    puntoRef = fun.getDireccionLuz(light,paredChoque)
    luzIndirecta = Reflejo(pPosicion=light.final)

    if puntoRef == "arr":
        luzIndirecta.setDirectionFromAngle(random.randint(189, 340))
    elif puntoRef == "aba":
        luzIndirecta.setDirectionFromAngle(random.randint(10, 170))

    elif puntoRef == "izq":
        if random.randint(0, 1) == 0:
            luzIndirecta.setDirectionFromAngle(random.randint(1, 85))

        else:
            luzIndirecta.setDirectionFromAngle(random.randint(280, 360))
    elif puntoRef == "der":
        luzIndirecta.setDirectionFromAngle(random.randint(95, 260))
    return luzIndirecta

def reboteEspecular(ray1, paredes):
    # BUG punto de interseccion es apenas mayor al de salida
    import Model.PathTracing as PT
    auxiliar = Reflejo(pPosicion=ray1.posicion)
    auxiliar.final.x = ray1.posicion.x
    auxiliar.final.y = ray1.final.y
    paredChoque = PT.intersectPoint(ray1, paredes, True)
    direccion=fun.getDireccionLuz(ray1, paredChoque)
    cambioAng = 0
    if ray1.posicion.x == ray1.final.x or ray1.final.y==ray1.posicion.y:
        return None
    ang = fun.anguloIncidencia(ray1, auxiliar)
    anguloInvertido = 0
    if direccion == "arr":
        cambioAng = 180
        if ray1.final.x > ray1.posicion.x:
            anguloInvertido=-((90-ang) * 2)
    elif direccion == "aba":
        if ray1.final.x < ray1.posicion.x:
            anguloInvertido=(90 - ang) * 2
    elif direccion == "izq":
        cambioAng = 270
        if ray1.final.y < ray1.posicion.y:
            anguloInvertido=(90 - ang) * 2
    elif direccion == "der":
        cambioAng = 90
        if ray1.final.y > ray1.posicion.y:
            anguloInvertido = (90 - ang) * 2
    reb = Reflejo(pPosicion=ray1.final)
    reb.setDirectionFromAngle(ang+cambioAng+anguloInvertido)
    pointPrue = PT.intersectPoint(reb, paredes, False)
    reb.setFinal(pointPrue)
    reb.setIntensidad(ray1)
    return reb

