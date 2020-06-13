from Model.Segmento import*
import random

class Ray:
    def __init__(self, pPosicion=Point(10, 10), pDireccion=Point(20,10)):
        self.direccion = pDireccion
        self.posicion = pPosicion

    def getDireccion(self):
        return self.direccion

    def getPosicion(self):
        return self.posicion

    def generarDir(self):
        coor=random.randint(0,1)
        num=random.randint(0,1)
        self.direccion.x=500
        self.direccion.y=500
        if coor==0:
            self.direccion.y=0
            self.direccion.x=0
        if num==0:
            self.direccion.x=random.randint(0,500)
        else:
            self.direccion.y = random.randint(0, 500)
        print(self.direccion.x)
        print(self.direccion.y)