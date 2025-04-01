import random
import pygame as pg

from code.Enemy import Enemy
from code.Player import Player
from code.Background import Background
from code.Const import WIN_WIDTH

class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(8):
                    list_bg.append(Background(f'Level1Bg{i}', position=(0,0)))
                    list_bg.append(Background(f'Level1Bg{i}', position=(WIN_WIDTH,0)))
                return list_bg
            case 'Level2Bg':
                list_bg = []
                for i in range(9):
                    list_bg.append(Background(f'Level2Bg{i}', position=(0,0)))
                    list_bg.append(Background(f'Level2Bg{i}', position=(WIN_WIDTH,0)))
                return list_bg
            case 'Player1':
                return Player('Player1', (WIN_WIDTH/2,200))
            
            case 'Player2':
                return Player('Player2', (WIN_WIDTH/3,200))
            
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 20, random.randint(200, 350)))
            
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 20, random.randint(400, 800)))