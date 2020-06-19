import pygame
from PIL import Image
import numpy as np
from Model.Segmento import *
from Model.Ray import *
class Window:

    def __init__(self, pHeight, pWidth, pNombre):
        self.h = pHeight
        self.w = pWidth
        self.nombre = pNombre
        self.running = True
        self.border = 50

        self.w = self.w #+ (1 * self.border)
        self.h = self.h #+ (1 * self.border)

        self.screen = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption(self.nombre)

    def run(self):
        pygame.init()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


    def drawLine(self, Surface, color, start_pos, end_pos, width):
        pygame.draw.line(Surface, color, start_pos, end_pos, width)
        pygame.display.flip()

    def drawSegment(self, color=(0,0,0), pSegmento=Segmento(False,[Point(50,50), Point(50,100)])):
        pygame.draw.line(self.screen, color, pSegmento.getSeccion()[0].getTuple(),
        pSegmento.getSeccion()[1].getTuple(), 5)
        pygame.display.flip()

    def drawLight(self, pRay=Ray()):
        posicion = pRay.getPosicion().getTuple()
        direccion = pRay.getFinal().getTuple()

        color = (255,255,255)
        pygame.draw.line(self.screen, color, posicion, direccion, 1)
        pygame.display.flip()

    def drawImage(self, bmp):
        self.screen.fill((255, 255, 255))
        surface = pygame.surfarray.make_surface(bmp)
        self.screen.blit(surface, (0, 0))
        pygame.display.flip()