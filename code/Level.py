#!/usr/bin/python
import sys
from tkinter.font import Font
import pygame as pg

from code.Const import COLOR_CIANO, COLOR_GREEN, COLOR_WHITE, EVENT_ENEMY, EVENT_TIMEOUT, FPS, MENU_OPTION, SPAWN_TIME, TIMEOUT_LEVEL, TIMEOUT_STEP, WIN_HEIGHT
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player

class Level:

    def __init__(self, window, name, game_mode, player_score: list[int]):
        self.timeout = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.game_mode = game_mode #modo de jogo
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        player = EntityFactory.get_entity('Player1')
        player.score = player_score[0]
        self.entity_list.append(player)
        if game_mode in [MENU_OPTION[1]]:
            player = EntityFactory.get_entity('Player2')
            player.score = player_score[1]
            self.entity_list.append(player)
        pg.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pg.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)
        
        
        
    def run(self, player_score: list[int]):
        pg.mixer_music.load(f'./assets/Menu.mp3')
        pg.mixer_music.play(-1)
        clock = pg.time.Clock()
        while True:
            clock.tick(FPS)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent,Player):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name == 'Player1':
                    self.level_text(14, f'Player1 - Health: {ent.health} | Score: {ent.score}', COLOR_GREEN, (10, 25))
                if ent.name == 'Player2':
                    self.level_text(14, f'Player2 - Health: {ent.health} | Score: {ent.score}', COLOR_CIANO, (20, 45)) 
        
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                
                if event.type == EVENT_ENEMY:
                    self.entity_list.append(EntityFactory.get_entity('Enemy1'))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if ((isinstance(ent, Player)) and (ent.name == 'Player1')):
                                player_score[0] = ent.score # type: ignore
                            if ((isinstance(ent, Player)) and (ent.name == 'Player2')):
                                player_score[1] = ent.score # type: ignore
                        return True
                
            found_player = False
            for ent in self.entity_list:
                if isinstance(ent, Player):
                    found_player = True
            
            if not found_player:
                return False
                    
            #Collisions
            EntityMediator.verify_collision(entity_list=self.entity_list) 
            EntityMediator.verify_health(entity_list=self.entity_list)      
            
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