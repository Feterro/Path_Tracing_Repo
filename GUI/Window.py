import pygame
from PIL import Image
import numpy as np
class Window:
    def __init__(self, pHeight, pWidth, pNombre):
        self.h = pHeight
        self.w = pWidth
        self.nombre = pNombre
        self.running = True
        self.border = 50

        self.w = self.w + (2 * self.border)
        self.h = self.h + (2 * self.border)

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