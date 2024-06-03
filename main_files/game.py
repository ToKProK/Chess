import pygame
from board import Board
from const import *

class Game:

    def __init__(self):
        self.board = Board()


    # Рисуем доску

    def show_bg(self, surface): 
        for row in range(Rows):
            for col in range(Cols):
                if (row + col) % 2 == 0:
                    color = (234, 235, 200) #зелённый
                else: 
                    color = (119, 154, 88) #тёмно-зелённый
                    rect = ()

                rect = (col * SQsize, row * SQsize, SQsize, SQsize) #так сказать рисуем квадрат (1 параметр x, потом y, далее длина и ширина)

                pygame.draw.rect(surface, color, rect)
    
    # Рисуем фигуры
    def show_pieces(self, surface):
        for row in range(Rows):
            for col in range(Cols):
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece
                    img = pygame.image.load(piece.texture)
                    img_center = col * SQsize + SQsize // 2, row * SQsize + SQsize // 2
                    piece.texture_rect = img.get_rect(center = img_center)
                    surface.blit(img, piece.texture_rect)