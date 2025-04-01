#!/usr/bin/python
import pygame as pg
from code.Level import Level
from code.Const import MENU_OPTION, WIN_HEIGHT, WIN_WIDTH
from code.Menu import Menu


class Game:

    def __init__(self):

        pg.init()
        self.window = pg.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        
        print('Loop Start')
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()
            
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1]]:
                player_score = [0, 0] #Player1, Player2
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level_return = level.run(player_score)
                    
            elif menu_return == MENU_OPTION[2]:  # HOW TO PLAY
                self.show_instructions()
                    
            elif menu_return == MENU_OPTION[4]:
                pg.quit()
                quit()
            else:
                pass
    
    def show_instructions(self):
        instructions = [
            "=== HOW TO PLAY ===",
            "",
            "Player 1 Controls:",
            "UP/DOWN/LEFT/RIGHT - Arrow Keys",
            "SHOOT - Right Ctrl",
            "",
            "Player 2 Controls:",
            "UP/DOWN/LEFT/RIGHT - W/A/S/D",
            "SHOOT - Left Ctrl",
            "",
            "Objective:",
            "- Defeat enemies before time runs out",
            "- Avoid getting hit",
            "- Cooperate in 2-player mode",
            "",
            "Press ESC to return"
        ]
        
        clock = pg.time.Clock()
        title_font = pg.font.SysFont("Lucida Sans Typewriter", 16, bold=True)  # Reduzido para 16
        section_font = pg.font.SysFont("Lucida Sans Typewriter", 12)  # Fonte para seções
        text_font = pg.font.SysFont("Lucida Sans Typewriter", 10)  # Fonte para texto normal
        
        while True:
            self.window.fill((0, 0, 0))  # Fundo preto
            
            # Título centralizado
            title = title_font.render("HOW TO PLAY", True, (255, 215, 0))
            self.window.blit(title, (600//2 - title.get_width()//2, 20))
            
            # Desenha instruções
            y_offset = 50  # Posição vertical inicial ajustada
            for line in instructions:
                if line.startswith("==="):
                    continue
                    
                if line.startswith("Player") or line.startswith("Objective"):
                    text = section_font.render(line, True, (255, 165, 0))
                    y_offset += 8  # Espaço extra reduzido
                else:
                    text = text_font.render(line, True, (200, 200, 200))
                
                self.window.blit(text, (50, y_offset))  # Margem esquerda de 50px
                y_offset += 18  # Espaçamento reduzido entre linhas
            
            pg.display.flip()
            
            # Controles
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        return

            clock.tick(60)

def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
    # Mantido igual ao original
    text_font = pg.font.SysFont("Lucida Sans Typewriter", text_size, bold=(text == "HOW TO PLAY"))
    text_surf = text_font.render(text, True, text_color).convert_alpha()
    text_rect = text_surf.get_rect(center=text_center_pos)
    self.window.blit(source=text_surf, dest=text_rect)





