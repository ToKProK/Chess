import pygame
from board import Board
from const import *
from dragger import Dragger
class Game:

    def __init__(self):
        self.next_player = 'white' # Чей ход
        self.board = Board()
        self.dragger = Dragger()

    # Рисуем доску
    def show_bg(self, surface): 
        for row in range(Rows):
            for col in range(Cols):
                if (row + col) % 2 == 0:
                    color = (236,224,202) #светлый
                else: 
                    color = (127,96,75) #тёмный

                rect = (col * SQsize, row * SQsize, SQsize, SQsize) #так сказать рисуем квадрат (1 параметр x, потом y, далее длина и ширина)

                pygame.draw.rect(surface, color, rect)
    
    # Рисуем фигуры
    def show_pieces(self, surface):
        for row in range(Rows):
            for col in range(Cols):
                if self.board.squares[row][col].has_piece(): # На выбранной клетке в массиве squares есть ли фигура?
                    piece = self.board.squares[row][col].piece
                    if piece != self.dragger.piece: # Рисуем все фигуры, кроме перетаскиваемой
                        piece.set_texture(size=80)
                        img = pygame.image.load(piece.texture)
                        img_center = col * SQsize + SQsize // 2, row * SQsize + SQsize // 2 # Координаты центра клетки
                        piece.texture_rect = img.get_rect(center = img_center)
                        surface.blit(img, piece.texture_rect)

    def show_moves(self, surface):
        if self.dragger.dragging: # Проверка на перетаскивание курсора
            piece = self.dragger.piece
            for move in piece.moves:
                color = "#C86464" if (move.final.row + move.final.col) % 2 == 0 else "#C84646"

                rect = (move.final.col * SQsize, move.final.row * SQsize, SQsize, SQsize)

                pygame.draw.rect(surface, color, rect)

    def show_last_move(self, surface):  
        if self.board.last_move:
            initial = self.board.last_move.initial
            final = self.board.last_move.final
            for i in [initial, final]:
                color = (244, 247, 116) if (i.row + i.col) % 2 == 0 else (172, 195, 51)

                rect = (i.col * SQsize, i.row * SQsize, SQsize, SQsize)

                pygame.draw.rect(surface, color, rect)

    # другие методы
    def next_turn(self):
          self.next_player = "white" if self.next_player == 'black' else 'black'
