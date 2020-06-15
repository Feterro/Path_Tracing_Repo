from Model.Point import *
import random
import Model.Funtions as fun
class Ray:
    def __init__(self, pPosicion=Point(10, 10), pDireccion=Point(20,10)):
        self.direccion = Point()
        self.posicion = pPosicion
        self.setDireccion(pDireccion)
        self.final = Point()

    def getDireccion(self):
        return self.direccion

    def getPosicion(self):
        return self.posicion

    def setDireccion(self, pDireccion):
        self.direccion.x = pDireccion.x - self.posicion.x
        self.direccion.y = pDireccion.y - self.posicion.y
        self.direccion = fun.normalize(self.direccion)

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
        print(pDireccion.x)
        print(pDireccion.y)