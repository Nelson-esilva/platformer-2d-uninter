#!/usr/bin/python
import pygame as pg
from code.Level import Level
from code.Const import MENU_OPTION
from code.Menu import Menu


class Game:

    def __init__(self):

        pg.init()
        self.window = pg.display.set_mode(size=(1200, 800))

    def run(self, ):
        
        print('Loop Start')
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()
            
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1]]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION[4]:
                pg.quit()
                quit()
            else:
                pass
        
            





