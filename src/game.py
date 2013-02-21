import pygame
import random
from time import sleep

from pygame.locals import *
from pygame.color import Color

from renderer import Renderer
from field import Field
from entity import Entity, Point
from snake import Snake
from player import Direction, ControlScheme, Player, ControlWASD, ControlArrows

class Game():
    def __init__(self):
        self.running = True
        self.alive = False
        self.renderer = Renderer(self)
        self.field = Field(24,18)
        self.players = []
        self.entities = []
        self.i = 0
        self.initialize()
        self.pauze = False
        self.direction = (0,0)

    def initialize(self):
        pygame.init()
        self.running = True

    def event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
            self.alive = False
            self.pauze = False
        elif event.type == KEYDOWN:
            if event.key == K_p:
                self.pauze = not self.pauze
            else:
                for player in self.players:
                    if event.key in player.controlscheme.getAllKeys():
                        player.setDirective(event.key)

    def stop(self):
        self.alive = False

    def gameTick(self):
        for player in self.players:
            player.move()

    def killEntity(self, entity):
        if entity in self.entities:
            self.entities.remove(entity)
            entity.onKill()
        elif entity in self.players:
            self.players.remove(entity)
            entity.onKill()

    def isOnOtherEntity(self, own_entity, location):
        (x,y) = location

        for et in (self.entities + self.players):
            for (xC,yC,col) in et.getPixels():
                if (x == xC and y == yC and not (et == own_entity)):
                    return et

        return None        

    def spawnNewPoint(self):
        found = False
        (newX, newY) = (None,None)
        pixelList = []

        for ent in self.entities + self.players:   
            for (x,y,col) in ent.getPixels():
                pixelList.append((x,y))

        while not found:
            (newX, newY) = (random.randint(0, self.field.width-1), random.randint(0, self.field.height-1))

            if not((newX, newY) in pixelList):
                found = True

        self.entities.append(Point((newX, newY), [(0,0,Color("Green"))], self))


            
    def frameTick(self):
        self.renderer.tick(0)

    def run_forever(self):
        while(self.running):
            self.entities = []
            self.players = [
                Player((4,0), [(0,0,Color("red")), (1,0,Color("red")), (2,0,Color("Yellow"))], Color("red"), self, (1,0), ControlArrows),
                Player((4,4), [(0,0,Color("blue")), (1,0,Color("blue")), (2,0,Color("Yellow"))], Color("blue"), self, (1,0), ControlWASD)
                ]
            self.spawnNewPoint()
            self.alive = True
            while(self.alive):
                for event in pygame.event.get():
                    self.event(event)

                self.gameTick()

                self.frameTick()

                while(self.pauze):
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            self.running = False
                            self.alive = False
                            self.pauze = False
                    sleep(0.3)

                sleep(0.3)
        pygame.quit()

if __name__ == "__main__":
    r = Game()
    r.run_forever()
        
