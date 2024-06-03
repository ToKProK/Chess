import pygame

from const import *

class Game:

    def __init__(self):
        pass


    #показывает методы

    def show_bg(self, surface):
        pass
        for row in range(Rows):
            for col in range(Cols):
                if (row + col) % 2 == 0:
                    color = (234, 235, 200) #зелённый
                else: 
                    color = (119, 154, 88) #тёмно-зелённый

                rect = (col * SQsize, row * SQsize, SQsize, SQsize) #так сказать рисуем квадрат (1 параметр x, потом y, далее длина и ширина)

                pygame.draw.rect(surface, color, rect)