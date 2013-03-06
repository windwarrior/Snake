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

class Player(Snake):
    def __init__(self, location, pixels, color, game, directive, name, controlscheme):
        super(Player, self).__init__(location, pixels, color, game)
        self.name = name
        self.controlscheme = controlscheme
        self.directive = directive
        self.speed = 7

        self.alive = True

    def tick(self):
        self.ticks = self.ticks + 1
        if (self.ticks % self.speed == 0):
            self.move()
            self.ticks = 0

    def move(self):
        super(Player, self).move(self.directive)

    def setDirective(self, key):
        self.directive = self.controlscheme.keyActions[key]

    def onKill(self):
        self.alive = False
        print "I'm dead {0} {1}".format(self.color, self.score)

ControlArrows = ControlScheme(K_UP, K_DOWN, K_RIGHT, K_LEFT)
ControlWASD = ControlScheme(K_w, K_s, K_d, K_a)
ControlJIKL = ControlScheme(K_i, K_k, K_l, K_j)
ControlNum = ControlScheme(K_KP8, K_KP5, K_KP6, K_KP4)
