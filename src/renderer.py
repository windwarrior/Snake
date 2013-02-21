import pygame
from pygame.locals import *

from pygame.color import Color

class Renderer():
    def __init__(self, game):
        self.game = game
        self.disp = pygame.display.set_mode((800,600), pygame.HWSURFACE)
        self.widthUnit = 0
        self.heightUnit = 0

    def drawScores(self):
        pass

    def drawFields(self):
        field = self.game.field

        for i in range(len(field.fields)):
            for j in range(len(field.fields[i])):
                pygame.draw.rect(self.disp, Color(50,50,50,255), ((j) * self.widthUnit + 0.025 * self.widthUnit + 25.0, (i) * self.heightUnit + 0.025 * self.heightUnit + 25.0, 0.95 * self.widthUnit, 0.95 * self.heightUnit), 1)

    def drawEntities(self):
        field = self.game.field

        for entity in (self.game.entities + self.game.players):
            for (x,y,color) in entity.getPixels():
                if x >= 0 and x < field.width and y >= 0 and y < field.height:
                    xLoc = x * self.widthUnit + 0.025 * self.widthUnit + 25.0
                    yLoc = y * self.heightUnit + 0.025 * self.heightUnit + 25.0
                    pygame.draw.rect(self.disp, color, (xLoc,yLoc, 0.95 * self.widthUnit, 0.95 * self.heightUnit), 0)

    def drawPauseScreen(self):
        s = pygame.Surface((self.disp.get_width(), self.disp.get_height()))
        s.set_alpha(128)
        s.fill(Color("black"))
        self.disp.blit(s, (0,0))

        font = pygame.font.SysFont("Dejavu Sans Extralight", 50)
        label = font.render(u"Game paused\u2026", 1, Color("white"))
        xLoc = (self.disp.get_width() - label.get_width()) / 2
        yLoc = (self.disp.get_height() - label.get_height()) / 2
        self.disp.blit(label, (xLoc, yLoc))

    def tick(self, delay):
        field = self.game.field

        self.widthUnit = (800.0 - 50.0) / field.width
        self.heightUnit = (600.0 - 50.0) / field.height

        self.disp.fill(Color("black"))

        self.drawFields()
        self.drawEntities()        

        if self.game.pauze:
            self.drawPauseScreen()
            
        pygame.display.update()
        
