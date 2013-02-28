from pygame.color import Color

import random

from entity import Point
class Level():
    def __init__(self, width, height, game):
        self.width = width
        self.height = height
        self.players = []
        self.entities = []
        self.game = game
    
    def killEntity(self, entity):
        if entity in self.entities:
            self.entities.remove(entity)
            entity.onKill()
        elif entity in self.players:
            self.players.remove(entity)
            entity.onKill()

        if len(self.players) == 0:
            print "players op?"
            self.game.setGameOver()

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
            (newX, newY) = (random.randint(0, self.width-1), random.randint(0, self.height-1))

            if not((newX, newY) in pixelList):
                found = True

        self.entities.append(Point((newX, newY), [(0,0,Color("Green"))], self.game))   

    def bake_level(self):
        empty = [[None for i in range(0,self.width)] for i in range(0, self.height)]

        for ent in self.entities + self.players:
            for (x,y,col) in ent.getPixels():
                empty[y][x] = col

        return empty           

