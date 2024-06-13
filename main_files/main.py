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
        board = self.game.board
        dragger = self.game.dragger
        while True:
            game.show_bg(screen)
            game.show_moves(screen)
            game.show_pieces(screen)
            
            if dragger.dragging:
                dragger.upadate_blit(screen)

            for event in pygame.event.get():
                
                # Клик
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse_position(event.pos)
                    clicked_Col = dragger.mouse_X // SQsize # Номер, нажатой строки (начиная с нуля).
                    clicked_Row = dragger.mouse_Y // SQsize # Номер, нажатого столбца (начиная с нуля).
                    print(f"({dragger.mouse_X,dragger.mouse_Y}), ({clicked_Row,clicked_Col})")

                    if game.board.squares[clicked_Row][clicked_Col].has_piece():  # На выбранной клетке в массиве squares есть ли фигура?
                        piece = game.board.squares[clicked_Row][clicked_Col].piece
                        board.cal_moves(piece, clicked_Row, clicked_Col) # Просчитываем все вохможные ходы для выбранной фигуры
                        dragger.save_initial(event.pos) # Сохраняем первоночальную позицию, для отката.
                        dragger.drag_piece(piece) # Сохраняем выбранную фигуру
                
                # Передвижение мышки
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging == True: # Данное условие позволяет остеживать передвижение мыши, только при зажатой кнопке на фигуре.
                        dragger.update_mouse_position(event.pos) # Обнавляем позицию курсора
                        #dragger.upadate_blit(screen) # Рисуем фигуру на месте курсора

                # Отпускание клика
                elif event.type == pygame.MOUSEBUTTONUP:
                    dragger.undrag_piece()


                #Выход из приложения
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
main = Main()
main.mainloop()