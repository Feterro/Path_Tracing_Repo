import threading

from GUI.Window import Window
import time
from Model.Ray import *
import Model.PathTracing as PT
import Model.Funtions as FN
from numpy import arange
def MAINLOOP():

    global boolean

    bordes=[
        Segmento(False, [Point(0, 500), Point(500, 500)]),
        Segmento(False, [Point(500, 500), Point(500, 0)]),
        Segmento(False, [Point(500, 0), Point(0, 0)]),
        Segmento(False, [Point(0, 0), Point(0, 500)])
    ]

    paredes = bordes + [

        #Segmento(False, [Point(200, 200), Point(400, 200)]),#arriba
        #Segmento(False, [Point(400, 300), Point(400, 400)]),# der
        #Segmento(False, [Point(200, 400), Point(300, 400)]),#abajo
        #Segmento(False, [Point(100, 200), Point(100, 350)]),#izq
        Segmento(False,[Point(180, 135), Point(215, 135)]),
        Segmento(False, [Point(285, 135), Point(320, 135)]),
        Segmento(False, [Point(320, 135), Point(320, 280)]),
        Segmento(False, [Point(320, 320), Point(320, 355)]),
        Segmento(False, [Point(320, 355), Point(215, 355)]),
        Segmento(False, [Point(180, 390), Point(180, 286)]),
        Segmento(False, [Point(180, 286), Point(140, 286)]),
        Segmento(False, [Point(320, 320), Point(360, 320)]),
        Segmento(False, [Point(180, 250), Point(180, 135)]),
        Segmento(False, [Point(215, 135), Point(215, 107)]),
        Segmento(False, [Point(285, 135), Point(285, 107)])
    ]
    luces = []
    reflejos=[]

    display.screen.fill((0, 0, 0))

    for i in arange(0,360,0.1):
        ray1 = Ray(pPosicion=Point(190, 145))
        ray2 = Ray(pPosicion=Point(310, 145))
        ray1.generarDir()
        ray2.generarDir()
        #ray2.setDirectionFromAngle(i)
        #ray1.setDirectionFromAngle(i)
        point = PT.intersectPoint(ray1, paredes)
        point2 = PT.intersectPoint(ray2, paredes)
        luces.append(ray1)
        luces.append(ray2)
        if point is not None:
            ray1.setFinal(point)
            reflejos += ray1.rebotar(bordes, paredes)
        if point2 is not None:
            ray2.setFinal(point2)
            reflejos += ray2.rebotar(bordes, paredes)

    img = FN.getImageBlank()
    global t, Img, Reflejos, Luces, Paredes
    Luces = luces
    Reflejos = reflejos
    Paredes = paredes
    Img = img

    print("Rayos generados")

    t.start()
    while True:
        #display.screen.fill((255, 255, 255))
        display.drawImage(Img)
        time.sleep(0.01)


Luces = Reflejos = Paredes = []
Pixeles = {}
Img = None

def threadPathTrace():
    PT.pathTrace(Luces, Reflejos, Paredes, Img, Pixeles)
t = threading.Thread(target = threadPathTrace) # f being the function that tells how the ball should move
t.setDaemon(True) # Alternatively, you can use "t.daemon = True"


if __name__ == '__main__':
    display = None
    Thread = threading.Thread(target=MAINLOOP)
    Thread.setDaemon(True)
    boolean = True
    display = Window(500, 500, "Path Tracing")
    Thread.start()
    display.run()








