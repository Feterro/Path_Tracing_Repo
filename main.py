import threading
import time
from GUI.Window import Window
from Model.Ray import *
import Model.PathTracing as PT
import Model.Funtions as FN
from numpy import arange
from collections import deque
def MAINLOOP():
    samples = 1
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

        Segmento(False, [Point(0, 155), Point(68, 155)]),
        Segmento(False, [Point(68, 155), Point(68, 183)]),
        Segmento(False, [Point(68, 183), Point(0, 183)]),
        Segmento(False, [Point(0, 13), Point(200, 13)]),
        Segmento(False, [Point(200, 13), Point(200, 155)]),
        Segmento(False, [Point(200, 155), Point(134, 155)]),
        Segmento(False, [Point(134, 155), Point(134, 182)]),
        Segmento(True, [Point(134, 182), Point(200, 182)]),
        Segmento(False, [Point(200, 182), Point(300, 182)]),
        Segmento(False, [Point(300, 182), Point(300, 155)]),
        Segmento(False, [Point(300, 155), Point(233, 155)]),
        Segmento(False, [Point(233, 155), Point(233, 13)]),
        Segmento(False, [Point(233, 13), Point(465, 13)]),
        Segmento(False, [Point(465, 13), Point(465, 155)]),
        Segmento(False, [Point(465, 155), Point(398, 155)]),
        Segmento(False, [Point(398, 155), Point(398, 182)]),
        Segmento(False, [Point(398, 182), Point(500, 182)]),
        Segmento(False, [Point(0, 328), Point(35, 328)]),
        Segmento(False, [Point(35, 328), Point(35, 386)]),
        Segmento(False, [Point(35, 386), Point(167, 386)]),
        Segmento(False, [Point(167, 386), Point(167, 328)]),
        Segmento(False, [Point(167, 328), Point(299, 328)]),
        Segmento(False, [Point(299, 328), Point(299, 357)]),
        Segmento(False, [Point(299, 357), Point(200, 357)]),
        Segmento(False, [Point(200, 357), Point(200, 416)]),
        Segmento(False, [Point(200, 416), Point(0, 416)]),
    ]
    luces = []
    reflejos=[]

    display.screen.fill((0, 0, 0))
    for i in arange(0,360,0.2):
        ray1 = Ray(pPosicion=Point(117, 339))
        ray2 = Ray(pPosicion=Point(84, 339))
        ray2.setDirectionFromAngle(i)
        ray1.setDirectionFromAngle(i)

        luces.append(ray1)
        luces.append(ray2)

        for i in range(samples):
            point = PT.intersectPoint(ray1, paredes)
            if point is not None:
                ray1.setFinal(point)
                reflejos += ray1.rebotar(paredes)
                ray1.setFinal(point)
                reflejos += ray1.rebotar(paredes)

            point2 = PT.intersectPoint(ray2, paredes)
            if point2 is not None:
                ray2.setFinal(point)
                reflejos += ray2.rebotar(paredes)
                ray2.setFinal(point)
                reflejos += ray2.rebotar(paredes)

    test_list = deque(reflejos)
    test_list.rotate(len(reflejos)//2)
    reflejos = list(test_list)
    img = FN.getImageBlank()
    global t, Img, Reflejos, Luces, Paredes
    Luces = luces
    Reflejos = reflejos
    Paredes = paredes
    Img = img

    print("Rayos generados")

    t.start()

    for pared in paredes:
        display.drawSegment((0, 0, 255), pared)

    while True:
        display.drawImage(Img)
        time.sleep(0.01)


Luces = Reflejos = Paredes = []
lucesEfectivas = [[0]*500]*500
Img = None

def threadPathTrace():
    PT.pathTrace(Luces, Reflejos, Paredes, Img, lucesEfectivas)


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








