from code.Const import ENTITY_SPEED, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, WIN_HEIGHT, WIN_WIDTH
from code.Entity import Entity
import pygame as pg

class Enemy(Entity):
    
    def __init__(self, name, position):
        super().__init__(name, position)
          
    
    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]