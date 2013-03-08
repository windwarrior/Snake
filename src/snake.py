from entity import Entity, Point

from pygame.color import Color
import math

class Snake(Entity):
    def __init__(self, location, pixels, color, game):
        super(Snake, self).__init__(location, pixels, game)
        self.color = color
        self.prevDirection = (0,0)
        self.spawnTicks = 0

        self.speed = 7
        self.player = None
        self.directive = (0,0)

    def tick(self, ticks):
        if self.spawnTicks < 50:
            self.spawnTicks += 1
        elif (ticks % self.speed == 0):
            self.move(self.directive)



    def move(self, direction):
        (xDiff, yDiff) = direction
        (xPrev, yPrev) = self.prevDirection
        if not (xDiff == 0 and yDiff == 0):     
            if (-1 * xPrev == xDiff and -1 * yPrev == yDiff):
                (xDiff, yDiff) = (xPrev, yPrev)

            (xHead, yHead, headCol) = self.pixels[-1]

            self.pixels[-1] = (xHead, yHead, self.color)
            newPos = ((xHead + xDiff) % self.game.level.width, (yHead + yDiff) % self.game.level.height, Color("yellow"))
            self.pixels.append(newPos)
            col = self.game.level.isOnOtherEntity(self, (newPos[0], newPos[1]))
            isColWithSelf = (newPos[0], newPos[1], self.color) in self.pixels[0:-1]

            if isColWithSelf:
                print (xDiff, yDiff), newPos
                self.game.level.killEntity(self)

                

                if self.player:
                    self.player.addScore(int(-1 * math.floor((self.player.score) / 2)))
                    self.player.respawn()

            if col and isinstance(col,Point):
                self.game.level.killEntity(col)
                if self.player:
                    self.player.addScore(1)
            elif col and isinstance(col, Snake):
                (xOtherHead, yOtherHead, colorOtherHead) = col.getPixels()[-1]
                if (xOtherHead == newPos[0]) and (yOtherHead == newPos[1]):
                    self.game.level.killEntity(col)

                    if col.player:
                        col.player.addScore(int(-1 * math.floor((self.player.score) / 2)))
                        col.player.respawn()
                self.game.level.killEntity(self)



                self.game.level.killEntity(self)

                if self.player:
                    self.player.addScore(int(-1 * math.floor((self.player.score) / 2)))
                    self.player.respawn()

            else:
                self.pixels.remove(self.pixels[0])

            self.prevDirection = (xDiff, yDiff)

            
