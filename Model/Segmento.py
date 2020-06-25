from Model.Point import Point
class Segmento:

    seccion = [Point(), Point()]
    especularidad=False
    lado=""

    def __init__(self, espec=False, puntos=[Point(), Point()], lad="abaj"):
        self.especularidad=espec
        self.seccion=puntos
        self.lado=lad

    def setEspecularidad(self, cambioEspec):
        self.especularidad=cambioEspec

    def getEspecularidad(self):
        return self.especularidad

    def getSeccion(self):
        return self.seccion

    def getLado(self):
        return self.lado

