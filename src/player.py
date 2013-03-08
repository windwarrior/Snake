from pygame.locals import *

from snake import Snake

class Direction():
    RIGHT = (1,0)
    LEFT = (-1,0)
    UP = (0,-1) #inverted y axis
    DOWN = (0,1)

class ControlScheme(object):
    def __init__(self, up, down, right, left):
        self.up = up
        self.down = down
        self.right = right
        self.left = left

        self.keyActions = {self.up: Direction.UP, self.down: Direction.DOWN, self.left: Direction.LEFT, self.right: Direction.RIGHT}

    def getAllKeys(self):
        return self.keyActions.keys()

class Player():
    def __init__(self, color, game, name, controlscheme):
        self.game = game
        self.name = name
        self.controlscheme = controlscheme
        self.color = color
        self.alive = True
        self.score = 0
        (self.entity, directive) = self.game.level.spawnSnake(color, game)

        self.entity.player = self
        self.entity.directive = directive

    def setDirective(self, key):
        self.entity.directive = self.controlscheme.keyActions[key]

    def addScore(self, score):
        print "Prev: {0}, New: {1}".format(self.score, self.score - score)
        self.score = self.score + score

    def respawn(self):
        (self.entity, directive) = self.game.level.spawnSnake(self.color, self.game)
        self.entity.player = self
        self.entity.directive = directive

    def onKill(self):
        self.alive = False
        self.game.level.entities.remove(self.entity)
        self.entity = None
        print "I'm dead {0} {1}".format(self.color, self.score)

ControlArrows = ControlScheme(K_UP, K_DOWN, K_RIGHT, K_LEFT)
ControlWASD = ControlScheme(K_w, K_s, K_d, K_a)
ControlJIKL = ControlScheme(K_i, K_k, K_l, K_j)
ControlNum = ControlScheme(K_KP8, K_KP5, K_KP6, K_KP4)
