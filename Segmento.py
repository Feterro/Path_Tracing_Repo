class Segmento:

    seccion=[]
    especularidad=False

    def __init__(self,espec,puntos):
        self.especularidad=espec
        self.seccion=puntos

    def setEspecularidad(self, cambioEspec):
        self.especularidad=cambioEspec

    def getEspecularidad(self):
        return self.especularidad

    def getSeccion(self):
        return self.seccion