from tkinter.font import Font
import pygame as pg

from code.Const import COLOR_ORANGE, COLOR_WHITE, MENU_OPTION

class Menu:

    def __init__(self, window):

        self.window = window
        self.surf = pg.image.load('./assets/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)
        
    def run(self, ):
        pg.mixer_music.load('./assets/Menu.mp3')
        pg.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "The Scientist's Hunt", COLOR_WHITE, (600,130))
            
            for i in range(len(MENU_OPTION)):
                self.menu_text(30, MENU_OPTION[i], COLOR_WHITE, (200,400 + 30*i))
            
            pg.display.flip()
            
            #Check for all events
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()   #close window
                    quit()      #end pygame
                    
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pg.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: pg.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pg.Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)