from Model.Segmento import  *
class Ray:
    def __init__(self, pPosicion=Point(10, 10), pDireccion=Point(0,1)):
        self.direccion = pDireccion
        self.posicion = pPosicion

    def getDireccion(self):
        return self.direccion

    def getPosicion(self):
        return self.posicion