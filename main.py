import threading
import time
from GUI.Window import Window
from Model.Segmento import *
from Model.Ray import *
import Model.PathTracing as PT
def MAINLOOP():

    global boolean

    paredes = [
        Segmento(False, [Point(400, 300), Point(400, 400)]),
        Segmento(False, [Point(200, 200), Point(400, 200)]),
        Segmento(False, [Point(100, 200), Point(100, 450)]),
        Segmento(False, [Point(100, 500), Point(400, 500)])
    ]
    luces = [

    ]

    display.screen.fill((0, 0, 0))

    for i in range(0,360,1):
        newRay = Ray(pPosicion=Point(250, 350))
        newRay.generarDir()

        point = PT.intersectPoint(newRay, paredes)
        luces.append(newRay)
        if point is not None:
            newRay.setFinal(point)

    for pared in paredes:

        display.drawSegment((0,0,255),pared)

    for luz in luces:
        display.drawLight(luz)

    '''while True:
        #display.screen.fill((255, 255, 255))
        if boolean:
            display.drawLine(display.screen, (0, 0, 255), (0, 0), (display.w, display.h), 5)
        else:
            display.drawLine(display.screen, (255, 0, 255), (display.w, 0), (0, display.h), 5)
        boolean = not boolean
        time.sleep(1)'''



if __name__ == '__main__':
    display = None
    Thread = threading.Thread(target=MAINLOOP)
    Thread.setDaemon(True)
    boolean = True
    display = Window(550, 550, "Path Tracing")
    Thread.start()
    display.run()








