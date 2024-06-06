import pygame

from const import *
# Данный класс отвечает за перетаскивание фигуры
class Dragger:
    def __init__(self):
        self.piec = None
        self.dragging = False
        self.mouse_X = 0
        self.mouse_Y = 0
        self.init_row = 0
        self.init_col = 0

    def update_mouse_position(self, pos): # pos - переменная с координатами курсора в которой есть (X_координата, Y_координата)
        self.mouse_X, self.mouse_Y = pos

    def save_initial(self, pos):
          self.init_row = pos[1] // SQsize
          self.init_col = pos[0] // SQsize

    def drag_piece(self, piece):
         self.piec = piece
         self.dragging = True
        
    def undrag_piece(self, piece):
         self.piec = None
         self.dragging = False

    def upadate_blit(self, surface):
        self.piec.set_texture(size=128)
        texture = self.piec.texture

        img = pygame.image.load(texture)

        img_center = (self.mouse_X, self.mouse_Y)

        self.piec.texture_rect = img.get_rect(center=img_center)

        surface.blit(img, self.piec.texture_rect)