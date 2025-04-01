#!/usr/bin/python
import sys
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
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        
        EntityFactory.set_level(1 if name == 'Level1' else 2)
        
        player = EntityFactory.get_entity('Player1')
        player.score = player_score[0]
        self.entity_list.append(player)
        
        if game_mode == MENU_OPTION[1]:
            player = EntityFactory.get_entity('Player2')
            player.score = player_score[1]
            self.entity_list.append(player)
            
        pg.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pg.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)
    
    def run(self, player_score: list[int]):
        clock = pg.time.Clock()
        while True:
            clock.tick(FPS)
            
            # Event handling
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == EVENT_ENEMY:
                    enemy = EntityFactory.get_entity('Enemy1' if self.name == 'Level1' else 'Enemy2')
                    if enemy:
                        self.entity_list.append(enemy)
                elif event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout <= 0:
                        self.update_scores(player_score)
                        return True
            
            # Game logic
            self.update_entities()
            self.check_game_over()
            
            # Rendering
            self.render()
            pg.display.flip()
    
    def update_entities(self):
        for ent in self.entity_list:
            ent.move()
            if isinstance(ent, Player):
                shoot = ent.shoot()
                if shoot:
                    self.entity_list.append(shoot)
    
    def check_game_over(self):
        if not any(isinstance(ent, Player) for ent in self.entity_list):
            return False
    
    def render(self):
        self.window.fill((0, 0, 0))
        for ent in self.entity_list:
            self.window.blit(ent.surf, ent.rect)
        
        # UI Rendering
        self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
    
    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        font = pg.font.SysFont("Lucida Sans Typewriter", text_size)
        text_surf = font.render(text, True, text_color)
        self.window.blit(text_surf, text_pos)
    
    def update_scores(self, player_score):
        for ent in self.entity_list:
            if isinstance(ent, Player):
                if ent.name == 'Player1':
                    player_score[0] = ent.score
                elif ent.name == 'Player2':
                    player_score[1] = ent.score