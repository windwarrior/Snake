from entity import Entity, Point
from pygame.color import Color

class Snake(Entity):
    def __init__(self, location, pixels, color, game):
        super(Snake, self).__init__(location, pixels, game)
        self.color = color
        self.prevDirection = (0,0)

    def move(self, direction):
        (xDiff, yDiff) = direction
        (xPrev, yPrev) = self.prevDirection
        if not (xDiff == 0 and yDiff == 0):     
            if (-1 * xPrev == xDiff and -1 * yPrev == yDiff):
                (xDiff, yDiff) = (xPrev, yPrev)

            (xHead, yHead, headCol) = self.pixels[-1]

            self.pixels[-1] = (xHead, yHead, self.color)
            newPos = ((xHead + xDiff) % self.game.field.width, (yHead + yDiff) % self.game.field.height, Color("yellow"))
            self.pixels.append(newPos)
            col = self.game.isOnOtherEntity(self, (newPos[0], newPos[1]))
            isColWithSelf = (newPos[0], newPos[1], self.color) in self.pixels[0:-1]

            if isColWithSelf:
                print (xDiff, yDiff), newPos
                print "You lost!"
                self.game.killEntity(self)

                self.game.stop()

            if col and isinstance(col,Point):
                print "Colliding!"
                self.game.killEntity(col)
                super(Snake, self).score(1)
            elif col and isinstance(col, Snake):
                (xOtherHead, yOtherHead, colorOtherHead) = col.getPixels()[-1]
                if (xOtherHead == newPos[0]) and (yOtherHead == newPos[1]):
                    print "headon!"                    
                    self.game.killEntity(col)
                self.game.killEntity(self)
            else:
                self.pixels.remove(self.pixels[0])

            self.prevDirection = (xDiff, yDiff)

            
