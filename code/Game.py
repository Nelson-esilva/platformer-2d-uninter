#!/usr/bin/python
import pygame as pg
from code.Menu import Menu


class Game:

    def __init__(self):

        pg.init()
        self.window = pg.display.set_mode(size=(1200, 800))

    def run(self, ):

        
        print('Loop Start')
        while True:
            menu = Menu(self.window)
            menu.run()
            pass
        
            





