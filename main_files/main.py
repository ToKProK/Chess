import pygame
import sys

from const import *

class Main:

    def __init__(self):
        pygame.init()
        self.screnn = pygame.display.set_mode((Width, Height))
        pygame.display.set_caption("Шахматы")
    def mainloop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
main = Main()
main.mainloop()
