from pygame.color import Color

class Entity(object):
    def __init__(self, location, sketch, game):
        self.pixels = []

        (xLoc, yLoc) = location
        for (x,y,color) in sketch:
            self.pixels.append((x + xLoc, y + yLoc, color))

        self.game = game
        self.alive = True

    def getPixels(self):
        return self.pixels

    def tick(self):
        pass

    def onKill(self):
        pass



class Point(Entity):
    def __init__(self, location, pixels, game):
        super(Point, self).__init__(location, pixels, game)

    def onKill(self):
        self.game.level.spawnNewPoint()

class PowerUp(Entity):
    def __init__(self, location, game):
        super(PowerUp, self).__init__(location, [(0,0,Color(0,255,255,255))], game)
