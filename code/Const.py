import pygame as pg

#C
COLOR_ORANGE = (182,57,16)
COLOR_WHITE = (255,255,255)
COLOR_YELLOW = (255,255,0)

#E
ENTITY_SPEED ={
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'Level1Bg7': 7,
    'Player1'  : 3,
    'Player2'  : 3,
    'Enemy1'   : 4,
    'Enemy2'   : 4,
}

EVENT_ENEMY = pg.USEREVENT + 1


ENTITY_HEALT = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Level1Bg7': 999,
    'Player1'  : 300,
    'Player2'  : 300,
    'Enemy1'    : 60,
    'Enemy2'    : 90,
}
    
#M
MENU_OPTION = ('NEW GAME',
               'COOPERATIVE MODE',
               'CARACTER SELECT',
               'SCORE',
               'EXIT')

#P
PLAYER_KEY_UP = {'Player1' : pg.K_UP,
                 'Player2' : pg.K_w}

PLAYER_KEY_DOWN = {'Player1' : pg.K_DOWN,
                 'Player2' : pg.K_s}

PLAYER_KEY_LEFT = {'Player1' : pg.K_LEFT,
                 'Player2' : pg.K_a}

PLAYER_KEY_RIGHT = {'Player1' : pg.K_RIGHT,
                 'Player2' : pg.K_d}

PLAYER_KEY_SHOOT = {'Player1' : pg.K_RCTRL,
                 'Player2' : pg.K_LCTRL}



#W
WIN_WIDTH = 1200
WIN_HEIGHT = 800