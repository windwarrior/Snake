class Entity(object):
    def __init__(self, location, sketch, game):
        self.pixels = []

        (xLoc, yLoc) = location
        for (x,y,color) in sketch:
            self.pixels.append((x + xLoc, y + yLoc, color))

        self.game = game
        self.score = 0

    def getPixels(self):
        return self.pixels

    def update(self):
        pass

    def onKill(self):
        pass

    def score(self, points):
        self.score = self.score + points

class Point(Entity):
    def __init__(self, location, pixels, game):
        super(Point, self).__init__(location, pixels, game)

    def onKill(self):
        self.game.spawnNewPoint()

        
