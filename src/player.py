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
    def __init__(self, location, pixels, color, game, directive, controlscheme):
        super(Player, self).__init__(location, pixels, color, game)
        self.controlscheme = controlscheme
        self.directive = directive

    def move(self):
        super(Player, self).move(self.directive)

    def setDirective(self, key):
        self.directive = self.controlscheme.keyActions[key]

    def onKill(self):
        print "I'm dead {0} {1}".format(self.color, self.score)

ControlArrows = ControlScheme(K_UP, K_DOWN, K_RIGHT, K_LEFT)
ControlWASD = ControlScheme(K_w, K_s, K_d, K_a)
