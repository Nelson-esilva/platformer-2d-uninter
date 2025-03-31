from code.Const import ENTITY_SPEED, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, WIN_HEIGHT, WIN_WIDTH
from code.Entity import Entity
import pygame as pg

class Player(Entity):
    
    def __init__(self, name, position):
        super().__init__(name, position)
          
    
    def move(self):
        pressed_key = pg.key.get_pressed()
        #if pressed_key[pg.K_UP] and self.rect.top > 0:
        #    self.rect.centery -= ENTITY_SPEED['Player1']
            
        #if pressed_key[pg.K_DOWN] and self.rect.bottom < WIN_HEIGHT:
        #    self.rect.centery += ENTITY_SPEED['Player1']
        
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right > WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
