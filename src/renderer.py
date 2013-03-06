import abc

import pygame
from pygame.locals import *
from time import sleep

from pygame.color import Color

from gamestate import GameState

class Renderer():
    def __init__(self, game):
        self.game = game
        self.disp = pygame.display.set_mode((800,600), pygame.HWSURFACE)
        self.widthUnit = 0
        self.heightUnit = 0

    def drawScores(self):
        pass

    def drawFields(self):
        lvl = self.game.level.bake_level()
        for i in range(len(lvl)):
            for j in range(len(lvl[i])):
                if not (lvl[i][j] == None):
                    pygame.draw.rect(self.disp, lvl[i][j], ((j) * self.widthUnit + 0.025 * self.widthUnit + 25.0, (i) * self.heightUnit + 0.025 * self.heightUnit + 25.0, 0.95 * self.widthUnit, 0.95 * self.heightUnit), 0)
                pygame.draw.rect(self.disp, Color(20,20,20,255), ((j) * self.widthUnit + 0.025 * self.widthUnit + 25.0, (i) * self.heightUnit + 0.025 * self.heightUnit + 25.0, 0.95 * self.widthUnit, 0.95 * self.heightUnit), 1)


    def _drawTransparentOverlay(self):
        s = pygame.Surface((self.disp.get_width(), self.disp.get_height()))
        s.set_alpha(128)
        s.fill(Color("black"))
        self.disp.blit(s, (0,0))

    def drawPauseScreen(self):
        self._drawTransparentOverlay()        

        font = pygame.font.SysFont("Dejavu Sans Extralight", 50)
        game_pauzed_label = font.render(u"Game paused", 1, Color("white"))
        
        font2 = pygame.font.SysFont("Dejavu Sans Extralight", 16)
        continue_label = font2.render(u"Press [P] to continue", 1, Color("white"))

        xLoc = (self.disp.get_width() - game_pauzed_label.get_width()) / 2
        yLoc = (self.disp.get_height() - (game_pauzed_label.get_height() + continue_label.get_height())) / 2

        self.disp.blit(game_pauzed_label, (xLoc, yLoc))

        xLoc2 = (self.disp.get_width() - continue_label.get_width()) / 2
        yLoc2 = (self.disp.get_height() + game_pauzed_label.get_height() )/ 2 
        self.disp.blit(continue_label, (xLoc2, yLoc2))
    
    def drawGameOver(self):
        self._drawTransparentOverlay()

        font = pygame.font.SysFont("Dejavu Sans Extralight", 50)
        label = font.render(u"Game Over", 1, Color("white"))
        xLoc = (self.disp.get_width() - label.get_width()) / 2
        yLoc = (self.disp.get_height() - label.get_height()) / 2
        self.disp.blit(label, (xLoc, yLoc))

    def drawScores(self):
        font = pygame.font.SysFont("Dejavu Sans Extralight", 16) 
        string = ""
        for player in self.game.level.players:
            string = string + "Player {0}: {1} ".format(player.color, player.score)

        label = font.render(string, 1, Color(200,200,200,255))
        xLoc = 10
        yLoc = (25 - label.get_height()) / 2
        self.disp.blit(label, (xLoc, yLoc))

    def tick(self, delay):
        field = self.game.level

        self.widthUnit = (self.disp.get_width() - 50.0) / field.width
        self.heightUnit = (self.disp.get_height() - 50.0) / field.height

        self.disp.fill(Color("black"))

        self.drawFields()     

        self.drawScores()  

        if self.game.gameState == GameState.PauzeState:
            self.drawPauseScreen()
        elif self.game.gameState == GameState.GameOverState:
            self.drawGameOver()
            
        pygame.display.update()

class AbstractRenderer(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, game, disp):
        self.game = game
        self.disp = disp

    @abc.abstractmethod
    def render(self):
        return

class StartScreenRenderer(AbstractRenderer):
    def __init__(self, game, disp):
        super(StartScreenRenderer, self).__init__(game, disp)

    def render(self):
        width = self.disp.get_width()
        height = self.disp.get_height()
        spacing = 12

        singleWidth = (width - 2 * spacing) / 2
        singleHeight = (height - 2 * spacing) / 2

        for i in [spacing, (width + spacing)/ 2]:
            for j in [spacing, (height + spacing)/ 2]:
                pygame.draw.rect(self.disp, Color(32,32,32,255), (i, j, (width / 2) - 1.5 * spacing, (height / 2) - 1.5 * spacing), 0)
                pygame.draw.rect(self.disp, Color(64,64,64,255), (i, j, (width / 2) - 1.5 * spacing, (height / 2) - 1.5 * spacing), 3)
                pygame.draw.rect(self.disp, Color(92,92,92,255), (i, j, (width / 2) - 1.5 * spacing, (height / 2) - 1.5 * spacing), 2)
                #pygame.draw.rect(self.disp, Color(64,64,64,255), ((i * width / 2), (j * height / 2), (width / 2), (height / 2)), 3)
                #pygame.draw.rect(self.disp, Color(92,92,92,255), ((i * width / 2), (j * height / 2), (width / 2), (height / 2)), 1)

        pygame.display.update()

def test_renderer():
    disp = pygame.display.set_mode((800,600), pygame.HWSURFACE)
    sr = StartScreenRenderer(None, disp)
    sr.render()

    sleep(5)

test_renderer()
        
        
