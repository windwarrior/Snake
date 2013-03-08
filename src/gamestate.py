import abc

from renderer import *
from entity import Entity, Point, PowerUp
from snake import Snake
from player import *


class BaseState(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, game):
        self.game = game

    @abc.abstractmethod
    def on_state_changed(self):
        # the method called on changing the state to this state
        pass

    @abc.abstractmethod
    def render(self):
        pass

    @abc.abstractmethod
    def process_events(self, events):     
        pass

    @abc.abstractmethod
    def update(self):
        pass

class InitState(BaseState):
    def __init__(self, game):
        super(InitState, self).__init__(game)

    def on_state_changed(self):
        colors = [Color("red"), Color("blue"), Color("purple"), Color("brown")]
        names = ["Jack", "Harry", "Franz", "DeeDee"]
        controls = [ControlArrows, ControlWASD, ControlJIKL, ControlNum]
        for i in range(0,4):

            self.game.level.players.append(Player(colors[i], self.game, names[i], controls[i]))
            
        #self.game.level.players = [
        #    Player((4,0), [(0,0,Color("red")), (1,0,Color("red")), (2,0,Color("Yellow"))], Color("red"), self.game, (1,0), "Red", ControlArrows),
        #    Player((4,4), [(0,0,Color("blue")), (1,0,Color("blue")), (2,0,Color("Yellow"))], Color("blue"), self.game, (1,0), "Blue", ControlWASD),
        #    Player((4,8), [(0,0,Color("purple")), (1,0,Color("purple")), (2,0,Color("yellow"))], Color("purple"), self.game, (1,0), "Purple", ControlJIKL),
        #    Player((4,12), [(0,0,Color("brown")), (1,0,Color("brown")), (2,0,Color("yellow"))], Color("brown"), self.game, (1,0), "Brown", ControlNum),
        #]

        
        for i in range(len(self.game.level.players)):
            self.game.level.spawnNewPoint()

        self.game.changeState(self.game.runState)

    def render(self):
        pass

    def process_events(self, events):
        pass

    def update(self):
        pass

class RunState(BaseState):
    def __init__(self, game):
        super(RunState, self).__init__(game)
        self.renderer = GameRenderer(game)
        self.ticks = 0

    def on_state_changed(self):
        pass

    def render(self):
        self.renderer.render()

    def process_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.game.changeState(self.game.quitState) #somestate
            elif event.type == pygame.VIDEORESIZE:
                self.game.screen = pygame.display.set_mode(event.dict['size'], pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)
            elif event.type == KEYDOWN:
                if event.key == K_p:
                    self.game.changeState(self.game.pauzeState) #somestate
                else:
                    for player in self.game.level.players:
                        if event.key in player.controlscheme.getAllKeys():
                            player.setDirective(event.key)

    def update(self):
        self.game.ticks += 1

        if self.game.ticks > self.game.maxTicks:
            self.game.changeState(self.game.gameOverState)

        for entity in self.game.level.entities:
            entity.tick(self.game.ticks)


class PauzeState(BaseState):
    def __init__(self, game):
        super(PauzeState, self).__init__(game)
        self.renderer = PauzeOverlayRenderer(game)

    def on_state_changed(self):
        pass

    def render(self):
        self.renderer.render()

    def process_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.game.changeState(self.game.quitState) 
            elif event.type == KEYDOWN:
               if event.key == K_p:
                  self.game.changeState(self.game.runState) 

    def update(self):
        pass


class GameOverState(BaseState):
    def __init__(self, game):
        super(GameOverState, self).__init__(game)
        self.renderer = GameOverOverlayRenderer(game)

    def on_state_changed(self):
        pass

    def render(self):
        self.renderer.render()

    def process_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.game.changeState(self.game.quitState) 
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    self.game.changeState(self.game.initState)   

    def update(self):
        pass

class QuitState(BaseState):
    def __init__(self, game):
        super(QuitState, self).__init__(game)

    def on_state_changed(self):
        self.game.quit()

    def render(self):
        pass

    def process_events(self, events):
        pass

    def update(self):
        pass   
