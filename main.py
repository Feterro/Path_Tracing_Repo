import threading

from GUI.Window import Window
import time
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

        Segmento(False, [Point(0, 140), Point(500, 140)], False),


        Segmento(False, [Point(180, 135), Point(215, 135)], False),
        Segmento(False, [Point(285, 135), Point(320, 135)], False),
        Segmento(False, [Point(320, 135), Point(320, 277)], False),
        Segmento(False, [Point(320, 320), Point(320, 355)], True),
        Segmento(False, [Point(320, 355), Point(215, 355)], False),
        Segmento(False, [Point(180, 351), Point(180, 286)], False),
        Segmento(False, [Point(180, 286), Point(140, 286)], False),
        Segmento(False, [Point(320, 320), Point(360, 320)], False),
        Segmento(False, [Point(180, 206), Point(180, 135)], False),
        Segmento(False, [Point(215, 135), Point(215, 107)], False),
        Segmento(False, [Point(285, 135), Point(285, 107)], False),

        Segmento(False, [Point(180, 136), Point(215, 136)], False),
        Segmento(False, [Point(285, 136), Point(320, 136)], False),
        Segmento(False, [Point(319, 135), Point(319, 277)], False),
        Segmento(False, [Point(319, 320), Point(319, 355)], False),
        Segmento(False, [Point(320, 356), Point(215, 356)], False),
        Segmento(False, [Point(179, 351), Point(179, 286)], False),
        Segmento(False, [Point(180, 287), Point(140, 287)], False),
        Segmento(False, [Point(320, 321), Point(360, 321)], False),
        Segmento(False, [Point(181, 206), Point(181, 135)], False),
        Segmento(False, [Point(214, 135), Point(214, 107)], False),
        Segmento(False, [Point(284, 135), Point(284, 107)], False),


        #habitacion izquierda
        Segmento(False, [Point(145, 206), Point(180, 206)], False),
        Segmento(False, [Point(145, 206), Point(145, 135)], False),
        Segmento(False, [Point(106, 135), Point(145, 135)], False),
        Segmento(False, [Point(106, 135), Point(106, 170)], False),
        Segmento(False, [Point(106, 170), Point(69, 170)], False),
        Segmento(False, [Point(69, 205), Point(69, 170)], False),
        Segmento(False, [Point(69, 205), Point(33, 205)], False),
        Segmento(False, [Point(33, 322), Point(33, 205)], False),
        Segmento(False, [Point(33, 322), Point(71, 322)], False),
        Segmento(False, [Point(71, 300), Point(71, 322)], False),
        Segmento(False, [Point(71, 300), Point(80, 300)], False),
        Segmento(False, [Point(71, 300), Point(80, 300)], False),
        Segmento(False, [Point(80, 335), Point(80, 300)], False),
        Segmento(False, [Point(80, 335), Point(70, 335)], False),
        Segmento(False, [Point(70, 349), Point(70, 335)], False),
        Segmento(False, [Point(70, 349), Point(35, 349)], False),
        Segmento(False, [Point(35, 465), Point(35, 349)], False),
        Segmento(False, [Point(35, 465), Point(215, 465)], False),
        Segmento(False, [Point(215, 355), Point(215, 465)], False),

        Segmento(False, [Point(180, 351), Point(108, 351)], False),
        Segmento(False, [Point(108, 325), Point(108, 351)], False),
        Segmento(False, [Point(108, 325), Point(140, 325)], False),
        Segmento(False, [Point(140, 286), Point(140, 325)], False),

        #Arriba izq
        Segmento(False, [Point(107, 107), Point(215, 107)], False),
        Segmento(False, [Point(107, 107), Point(107, 74)], False),
        Segmento(False, [Point(35, 74), Point(107, 74)], False),
        Segmento(False, [Point(35, 74), Point(35, 0)], False),

        #Arriba Der
        Segmento(False, [Point(430, 107), Point(285, 107)], False),
        Segmento(False, [Point(430, 107), Point(430, 73)], False),
        Segmento(False, [Point(465, 73), Point(430, 73)], False),
        Segmento(False, [Point(465, 73), Point(465, 0)], False),

        #Habitacion der
        Segmento(False, [Point(360, 360), Point(360, 320)], False),
        Segmento(False, [Point(360, 360), Point(390, 360)], False),
        Segmento(False, [Point(390, 370), Point(390, 360)], False),
        Segmento(False, [Point(390, 370), Point(430, 370)], False),
        Segmento(False, [Point(430, 359), Point(430, 370)], False),
        Segmento(False, [Point(430, 359), Point(466, 359)], False),
        Segmento(False, [Point(466, 206), Point(466, 359)], False),
        Segmento(False, [Point(466, 206), Point(430, 206)], False),
        Segmento(False, [Point(430, 135), Point(430, 206)], False),
        Segmento(False, [Point(430, 135), Point(355, 135)], False),
        Segmento(False, [Point(355, 277), Point(355, 135)], False),
        Segmento(False, [Point(355, 277), Point(320, 277)], False),

        #puertas
        Segmento(False, [Point(160, 206), Point(160, 286)], False),
        Segmento(False, [Point(339, 277), Point(339, 320)], False),
    ]
    luces = []
    reflejos=[]

    display.screen.fill((0, 0, 0))
    for i in arange(0,360,0.1):
        ray1 = Ray(pPosicion=Point(182, 150))
        ray2 = Ray(pPosicion=Point(318, 150))
        #ray1.generarDir()
        #ray2.generarDir()
        ray2.setDirectionFromAngle(i)
        ray1.setDirectionFromAngle(i)

        luces.append(ray1)
        luces.append(ray2)

    for i in range(samples):
        for ray in luces:
            point = PT.intersectPoint(ray, paredes)
            if point is not None:
                ray.setFinal(point)
                reflejos += ray.rebotar(paredes)
                ray.setFinal(point)
                reflejos += ray.rebotar(paredes)

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
    #threadPathTrace()
    for pared in paredes:
        display.drawSegment((0, 0, 255), pared)
    '''for i in range(len(luces)):
        luz = luces[i]
        reflejo = reflejos[i]
        display.drawLight(luz)
        display.drawLight(reflejo)'''
    while True:
        #display.screen.fill((255, 255, 255))
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








