import threading
import time
from GUI.Window import Window
from Model.Segmento import *
from Model.Ray import *
import Model.PathTracing as PT
def MAINLOOP():

    global boolean

    bordes=[Segmento(False, [Point(0, 500), Point(500, 500)]),
        Segmento(False, [Point(500, 500), Point(500, 0)]),
        Segmento(False, [Point(500, 0), Point(0, 0)]),
        Segmento(False, [Point(0, 0), Point(0, 500)])]

    paredes = [

        #Segmento(False, [Point(200, 400), Point(300, 200)]),
        #Segmento(False, [Point(300, 200), Point(300, 400)]),
        #Segmento(False, [Point(200, 400), Point(300, 400)]),
        Segmento(False, [Point(200, 200), Point(400, 200)]),#arriba
        Segmento(False, [Point(400, 300), Point(400, 400)]),# der
        Segmento(False, [Point(200, 400), Point(300, 400)]),#abajo
        Segmento(False, [Point(100, 200), Point(100, 350)]),#izq
        Segmento(False, [Point(0, 500), Point(500, 500)]),
        Segmento(False, [Point(500, 500), Point(500, 0)]),
        Segmento(False, [Point(500, 0), Point(0, 0)]),
        Segmento(False, [Point(0, 0), Point(0, 500)])

    ]
    luces = []
    reflejos=[]

    display.screen.fill((0, 0, 0))

    for i in range(0,360,72):
        newRay = Ray(pPosicion=Point(250, 350))
        #newRay.generarDir()
        newRay.setDirectionFromAngle(i)

        point = PT.intersectPoint(newRay, paredes)
        luces.append(newRay)
        if point is not None:
            RayCopy=newRay;
            newRay.setFinal(point)
            puntoRef=PT.intersectPoint(RayCopy,bordes)
            Reflejo=Ray(pPosicion=point)
            if(puntoRef.y==0):
                Reflejo.setDirectionFromAngle(random.randint(181,359))
                final=PT.intersectPoint(Reflejo, bordes) #TEMPORAL SOLO PARA VISUALIZAR LAS INTERSECCIONES EN LOS IFS SE BORRAN
            elif(puntoRef.y==500):
                Reflejo.setDirectionFromAngle(random.randint(1, 179))
                final=PT.intersectPoint(Reflejo, bordes)

            elif(puntoRef.x==0):
                if(random.randint(0,1)==0):
                    Reflejo.setDirectionFromAngle(random.randint(1, 89))
                else:
                    Reflejo.setDirectionFromAngle(random.randint(271, 359))
                final=PT.intersectPoint(Reflejo, bordes)
            elif(puntoRef.x==500):
                    Reflejo.setDirectionFromAngle(random.randint(89, 269))
                    final = PT.intersectPoint(Reflejo, bordes)
            Reflejo.setFinal(final)
            reflejos.append(Reflejo);

    for pared in paredes:

        display.drawSegment((0,0,255),pared)

    for luz in luces:
        display.drawLight(luz)
    for reflejo in reflejos:
        display.drawLight(reflejo)

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
    display = Window(500, 500, "Path Tracing")
    Thread.start()
    display.run()








