#!/usr/bin/python
import sys
from tkinter.font import Font
import pygame as pg

from code.Const import COLOR_WHITE, EVENT_ENEMY, MENU_OPTION, WIN_HEIGHT
from code.Entity import Entity
from code.EntityFactory import EntityFactory

class Level:

    def __init__(self, window, name, game_mode):
        self.timeout = 20000 #20 segundos
        self.window = window
        self.name = name
        self.game_mode = game_mode #modo de jogo
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        if game_mode in [MENU_OPTION[1]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pg.time.set_timer(EVENT_ENEMY, 3000)
        
        
        
    def run(self):
        pg.mixer_music.load(f'./assets/Menu.mp3')
        pg.mixer_music.play(-1)
        clock = pg.time.Clock()
        while True:
            clock.tick(40)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                
                if event.type == EVENT_ENEMY:
                    self.entity_list.append(EntityFactory.get_entity('Enemy1'))
                    
            #printed text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps() :.0f}', COLOR_WHITE, (10, WIN_HEIGHT-35))        
            self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT-20))
            pg.display.flip()
                    
                    
                    
    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
            text_font: Font = pg.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
            text_surf: pg.Surface = text_font.render(text, True, text_color).convert_alpha()
            text_rect: pg.Rect = text_surf.get_rect(top=text_pos[1])
            self.window.blit(source=text_surf, dest=text_rect)