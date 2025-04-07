#!/usr/bin/python
from abc import ABC, abstractmethod
import pygame as pg

from code.Const import ENTITY_DAMAGE, ENTITY_HEALT, ENTITY_SCORE

class Entity(ABC):

    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pg.image.load('./assets/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left = position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALT[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.last_dmg = 'None'
        self.score = ENTITY_SCORE[self.name]
        
    @abstractmethod    
    def move(self, ):
        pass