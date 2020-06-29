from Model.Point import Point
class Segmento:

    seccion = [Point(), Point()]
    especularidad = False
    transparencia = False
    lado=""

    def __init__(self, espec=False, puntos=[Point(), Point()], trans=False):
        self.especularidad = espec
        self.seccion = puntos
        self.transparencia = trans

    def setEspecularidad(self, cambioEspec):
        self.especularidad = cambioEspec

    def getEspecularidad(self):
        return self.especularidad

    def getSeccion(self):
        return self.seccion


