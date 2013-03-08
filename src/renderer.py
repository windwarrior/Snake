import abc

import pygame
from pygame.locals import *
from time import sleep

from pygame.color import Color

from gamestate import *

class AbstractRenderer(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, game):
        self.game = game

    @abc.abstractmethod
    def render(self):
        return

    #Utility method to draw a black transparent overlay
    def _drawTransparentOverlay(self):
        s = pygame.Surface((self.game.disp.get_width(), self.game.disp.get_height()))
        s.set_alpha(128)
        s.fill(Color("black"))
        self.game.disp.blit(s, (0,0))

class StartScreenRenderer(AbstractRenderer):
    def __init__(self, game):
        super(StartScreenRenderer, self).__init__(game, disp)

    def render(self):
        width = self.game.disp.get_width()
        height = self.game.disp.get_height()
        spacing = 12

        singleWidth = (width - 2 * spacing) / 2
        singleHeight = (height - 2 * spacing) / 2

        for i in [spacing, (width + spacing)/ 2]:
            for j in [spacing, (height + spacing)/ 2]:
                pygame.draw.rect(self.game.disp, Color(32,32,32,255), (i, j, (width / 2) - 1.5 * spacing, (height / 2) - 1.5 * spacing), 0)
                pygame.draw.rect(self.game.disp, Color(64,64,64,255), (i, j, (width / 2) - 1.5 * spacing, (height / 2) - 1.5 * spacing), 3)
                pygame.draw.rect(self.game.disp, Color(92,92,92,255), (i, j, (width / 2) - 1.5 * spacing, (height / 2) - 1.5 * spacing), 2)
                #pygame.draw.rect(self.disp, Color(64,64,64,255), ((i * width / 2), (j * height / 2), (width / 2), (height / 2)), 3)
                #pygame.draw.rect(self.disp, Color(92,92,92,255), ((i * width / 2), (j * height / 2), (width / 2), (height / 2)), 1)


class GameRenderer(AbstractRenderer):
    def __init__(self, game):
        super(GameRenderer, self).__init__(game)
        self.widthUnit = 0
        self.heightUnit = 0

    def render(self):
        field = self.game.level

        self.widthUnit = (self.game.disp.get_width() - 50.0) / field.width
        self.heightUnit = (self.game.disp.get_height() - 50.0) / field.height

        self.game.disp.fill(Color("black"))

        self.drawFields()
        self.drawScores()
        self.drawTicks()

    def drawTicks(self):
        font = pygame.font.SysFont("Dejavu Sans Extralight", 16) 
        string = "Ticks done: {0}, Ticks left: {1}".format(self.game.ticks, self.game.maxTicks - self.game.ticks)

        label = font.render(string, 1, Color(200,200,200,255))

        xLoc = self.game.disp.get_width() - (label.get_width() + 10)
        yLoc = (25 - label.get_height()) / 2

        self.game.disp.blit(label, (xLoc, yLoc))

    def drawFields(self):
        lvl = self.game.level.bake_level()
        for i in range(len(lvl)):
            for j in range(len(lvl[i])):
                if not (lvl[i][j] == None):
                    pygame.draw.rect(self.game.disp, lvl[i][j], ((j) * self.widthUnit + 0.025 * self.widthUnit + 25.0, (i) * self.heightUnit + 0.025 * self.heightUnit + 25.0, 0.95 * self.widthUnit, 0.95 * self.heightUnit), 0)
                pygame.draw.rect(self.game.disp, Color(20,20,20,255), ((j) * self.widthUnit + 0.025 * self.widthUnit + 25.0, (i) * self.heightUnit + 0.025 * self.heightUnit + 25.0, 0.95 * self.widthUnit, 0.95 * self.heightUnit), 1)


    def drawScores(self):
        font = pygame.font.SysFont("Dejavu Sans Extralight", 16) 
        string = ""
        for player in self.game.level.players:
            string = string + "| Player {0}: {1} |".format(player.name, player.score)

        label = font.render(string, 1, Color(200,200,200,255))
        xLoc = 10
        yLoc = (25 - label.get_height()) / 2
        self.game.disp.blit(label, (xLoc, yLoc))

class PauzeOverlayRenderer(GameRenderer):
    def __init__(self, game):
        super(PauzeOverlayRenderer, self).__init__(game)

    def render(self):
        super(PauzeOverlayRenderer, self).render()
        self._drawTransparentOverlay()        

        font = pygame.font.SysFont("Dejavu Sans Extralight", 50)
        game_pauzed_label = font.render(u"Game paused", 1, Color("white"))
        
        font2 = pygame.font.SysFont("Dejavu Sans Extralight", 16)
        continue_label = font2.render(u"Press [P] to continue", 1, Color("white"))

        xLoc = (self.game.disp.get_width() - game_pauzed_label.get_width()) / 2
        yLoc = (self.game.disp.get_height() - (game_pauzed_label.get_height() + continue_label.get_height())) / 2

        self.game.disp.blit(game_pauzed_label, (xLoc, yLoc))

        xLoc2 = (self.game.disp.get_width() - continue_label.get_width()) / 2
        yLoc2 = (self.game.disp.get_height() + game_pauzed_label.get_height() )/ 2 
        self.game.disp.blit(continue_label, (xLoc2, yLoc2))


class GameOverOverlayRenderer(GameRenderer):

    def __init__(self, game):
        super(GameOverOverlayRenderer, self).__init__(game)

    def render(self):
        super(GameOverOverlayRenderer, self).render()
        self._drawTransparentOverlay()

        font = pygame.font.SysFont("Dejavu Sans Extralight", 50)
        label = font.render(u"Game Over", 1, Color("white"))
        xLoc = (self.game.disp.get_width() - label.get_width()) / 2
        yLoc = (self.game.disp.get_height() - label.get_height()) / 2
        self.game.disp.blit(label, (xLoc, yLoc)) 

        
        
