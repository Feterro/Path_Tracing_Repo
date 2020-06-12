import threading
import time
from GUI.Window import Window

def MAINLOOP():

    global boolean
    while True:
        display.screen.fill((255, 255, 255))
        if boolean:
            display.drawLine(display.screen, (0, 0, 255), (0, 0), (display.w, display.h), 5)
        else:
            display.drawLine(display.screen, (255, 0, 255), (display.w, 0), (0, display.h), 5)
        boolean = not boolean
        time.sleep(1)



if __name__ == '__main__':
    display = None
    Thread = threading.Thread(target=MAINLOOP)
    Thread.setDaemon(True)
    boolean = True
    display = Window(550, 550, "Path Tracing")
    Thread.start()
    display.run()








