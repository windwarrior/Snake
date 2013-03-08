from pygame.color import Color

import random

from entity import Point
from snake import Snake

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
            entity.onKill()

        if len([player for player in self.players if player.alive]) == 0:
            print "players op?"
            self.game.changeState(self.game.gameOverState)

    def isOnOtherEntity(self, own_entity, location):
        (x,y) = location

        for et in (self.entities):
            for (xC,yC,col) in et.getPixels():
                if (x == xC and y == yC and not (et == own_entity)):
                    return et

        return None     

    def spawnNewPoint(self):
        found = False
        (newX, newY) = (None,None)
        pixelList = []

        for ent in self.entities:   
            for (x,y,col) in ent.getPixels():
                pixelList.append((x,y))

        while not found:
            (newX, newY) = (random.randint(0, self.width-1), random.randint(0, self.height-1))

            if not((newX, newY) in pixelList):
                found = True

        self.entities.append(Point((newX, newY), [(0,0,Color("Green"))], self.game))   

    def bake_level(self):
        empty = [[None for i in range(0,self.width)] for i in range(0, self.height)]

        for ent in self.entities:
            for (x,y,col) in ent.getPixels():
                if x >= self.width or y >= self.height:
                    print "entity {0} is offending {1}".format(ent, ent.getPixels())
                    continue
                empty[y][x] = col

        return empty  


    def spawnSnake(self, color, game):
        direction = random.choice([(0,1), (0,-1), (1,0), (-1,0)])
        
        snakePix = [(0,0, color), (direction[0],direction[1], color), (direction[0]*2,direction[1]*2, Color("yellow"))]
    
        found = False

        candidate = None
            
        while not found:
            randX = random.randint(0, self.width - 3)
            randY = random.randint(0, self.height - 3)

            found = True
            location = (randX, randY)
            for pix in [(x + randX, y + randY) for (x,y, col) in snakePix]:
                if self.isOnOtherEntity(None, pix):
                    found = False

        snake = Snake(location, snakePix, color, game)
        self.entities.append(snake)

        return (snake, direction)
                    
            

    

                 


