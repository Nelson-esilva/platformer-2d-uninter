import pygame as pg

#C
COLOR_ORANGE = (182,57,16)
COLOR_WHITE = (255,255,255)
COLOR_YELLOW = (255,255,0)
COLOR_GREEN = (0,128,0)
COLOR_CIANO = (0,128,128)

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
    'Level2Bg0': 0,
    'Level2Bg1': 1,
    'Level2Bg2': 2,
    'Level2Bg3': 3,
    'Level2Bg4': 4,
    'Level2Bg5': 5,
    'Level2Bg6': 6,
    'Level2Bg7': 7,
    'Level2Bg8': 7,
    'Player1'  : 3,
    'Player2'  : 3,
    'Enemy1'   : 4,
    'Enemy2'   : 4,
    'Player1Shot'  : 2,
    'Player2Shot'  : 2,
}

EVENT_ENEMY = pg.USEREVENT + 1
EVENT_TIMEOUT = pg.USEREVENT + 2

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level1Bg7': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level2Bg5': 0,
    'Level2Bg6': 0,
    'Level2Bg7': 0,
    'Level2Bg8': 0,
    'Player1'  : 1,
    'Player2'  : 1,
    'Enemy1'    : 3,
    'Enemy2'    : 3,
    'Player1Shot': 30,
    'Player2Shot': 30,
}

ENTITY_HEALT = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Level1Bg7': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Level2Bg5': 999,
    'Level2Bg6': 999,
    'Level2Bg7': 999,
    'Level2Bg8': 999,
    'Player1'  : 300,
    'Player2'  : 300,
    'Enemy1'    : 70,
    'Enemy2'    : 100,
    'Player1Shot': 1,
    'Player2Shot': 1,
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level1Bg7': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level2Bg5': 0,
    'Level2Bg6': 0,
    'Level2Bg7': 0,
    'Level2Bg8': 0,
    'Player1'  : 0,
    'Player2'  : 0,
    'Enemy1'    :1,
    'Enemy2'    :2,
    'Player1Shot': 0,
    'Player2Shot': 0,
}

ENTITY_SHOT_DELAY = {
    'Player1' : 35,
    'Player2' : 35,
}

#F
FPS = 60
    
#M
MENU_OPTION = ('NEW GAME',
               'COOPERATIVE MODE',
               'HOW TO PLAY',
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

#S
SPAWN_TIME = 2000

#T
TIMEOUT_LEVEL = 30000
TIMEOUT_STEP = 100

#W
WIN_WIDTH = 600
WIN_HEIGHT = 400