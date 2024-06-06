import pygame
import sys

from const import *
from game import Game

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Width, Height))
        pygame.display.set_caption("Шахматы")
        self.game = Game()
    def mainloop(self):
        screen = self.screen
        game = self.game
        dragger = self.game.dragger
        while True:
            game.show_bg(screen)
            game.show_pieces(screen)
            
            for event in pygame.event.get():
                
                # Клик
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse_position(event.pos)
                    clicked_Row = dragger.mouse_X // SQsize # Номер, нажатой строки (начиная с нуля).
                    clicked_Col = dragger.mouse_Y // SQsize # Номер, нажатого столбца (начиная с нуля).
                    print(f"({dragger.mouse_X,dragger.mouse_Y}), ({clicked_Row,clicked_Col})")
                    if game.board.squares[clicked_Col][clicked_Row].has_piece():  # На выбранной клетке в массиве squares есть ли фигура?
                        piece = game.board.squares[clicked_Row][clicked_Col].piece
                        dragger.save_initial(event.pos) # Сохраняем выбранную позицию
                        dragger.drag_piece(piece) # Сохраняем выбранную фигуру
                # Передвижение мышки
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging == True: # Данное условие позволяет остеживать передвижение мыши, только при зажатой кнопке на фигуре.
                        dragger.update_mouse_position(event.pos)
                        dragger.upadate_blit(screen)

                # Отпускание клика
                elif event.type == pygame.MOUSEBUTTONUP:
                    pass


                #Выход из приложения
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()



            pygame.display.update()
main = Main()
main.mainloop()