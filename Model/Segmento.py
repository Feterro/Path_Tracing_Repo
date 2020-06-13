from Model.Point import Point
class Segmento:

    seccion = [Point(), Point()]
    especularidad=False

    def __init__(self,espec=False,puntos=[Point(), Point()]):
        self.especularidad=espec
        self.seccion=puntos

    def setEspecularidad(self, cambioEspec):
        self.especularidad=cambioEspec

    def getEspecularidad(self):
        return self.especularidad

    def getSeccion(self):
        return self.seccion

