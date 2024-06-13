import pygame

from const import *
# Данный класс отвечает за перетаскивание фигуры
class Dragger:
    def __init__(self):
        self.piece = None
        self.dragging = False
        self.mouse_X = 0
        self.mouse_Y = 0
        self.init_row = 0
        self.init_col = 0

    # Метод перетаскивания (blit) фигур курсором
    def upadate_blit(self, surface): # Рисуем фигуру на месте курсора
        #texture 
        self.piece.set_texture(size=128)
        texture = self.piece.texture
        #img
        img = pygame.image.load(texture)
        # rectа
        img_center = (self.mouse_X, self.mouse_Y)
        self.piece.texture_rect = img.get_rect(center=img_center)
        #Проецируем
        surface.blit(img, self.piece.texture_rect)
     
    # Остальные методы

    def update_mouse_position(self, pos): # pos - переменная с координатами курсора в которой есть (X_координата, Y_координата)
        self.mouse_X, self.mouse_Y = pos

    def save_initial(self, pos): # Сохраняем первоночальную позицию, для отката.
          self.init_row = pos[1] // SQsize
          self.init_col = pos[0] // SQsize

    def drag_piece(self, piecee): # Получаем данные о перетаскиваемой фигуре
         self.piece = piecee
         self.dragging = True
        
    def undrag_piece(self): # выключаем перетаскивание
         self.piece = None
         self.dragging = False

