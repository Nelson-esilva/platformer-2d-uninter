from tkinter.font import Font
import pygame as pg

from code.Const import COLOR_ORANGE, COLOR_WHITE, COLOR_YELLOW, MENU_OPTION

class Menu:

    def __init__(self, window):

        self.window = window
        self.surf = pg.image.load('./assets/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        
    def run(self, ):
        menu_option = 0
        pg.mixer_music.load('./assets/Menu.mp3')
        pg.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "The Scientist's Hunt", COLOR_ORANGE, (600,130))
            
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(30, MENU_OPTION[i], COLOR_YELLOW, (200,400 + 30*i))
                else:
                    self.menu_text(30, MENU_OPTION[i], COLOR_WHITE, (200,400 + 30*i))
        
            
            #Check for all events
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()   #close window
                    quit()      #end pygame
                    
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_DOWN:
                        if menu_option < len(MENU_OPTION) -1:
                            menu_option += 1
                        else:
                            menu_option = 0
                
                    if event.key == pg.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) -1
                
                    if event.key == pg.K_RETURN: #ENTER
                            return MENU_OPTION[menu_option]
                
                
            
            pg.display.flip()
                    
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pg.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: pg.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pg.Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)