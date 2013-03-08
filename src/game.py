import pygame
import random
from time import sleep

from pygame.locals import *
from pygame.color import Color

from level import Level


from gamestate import *
    
class Game():
    def __init__(self):
        self.level = Level(34,28, self)
        self.ticks = 0

        self.initState = InitState(self)
        self.runState = RunState(self)
        self.pauzeState = PauzeState(self)
        self.gameOverState = GameOverState(self)
        self.quitState = QuitState(self)

        self.currentState = None


        self.ticks = 0
        self.maxTicks = 18000

        self.running = True
        
        self.disp = pygame.display.set_mode((1280,1024), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)

        self.initialize()
        self.changeState(self.initState)

    def initialize(self):
        pygame.init()

    def changeState(self, newState):
        print "changing state to {0}".format(newState)
        self.currentState = newState
        self.currentState.on_state_changed()

    def quit(self):
        self.running = False

    def run_forever(self):
        while(self.running):
            self.currentState.process_events(pygame.event.get())
            self.currentState.update()
            self.currentState.render()

            pygame.display.update()
            sleep(1.0/60.0) # update 20 keer per seconde
                
        pygame.quit()

if __name__ == "__main__":
    r = Game()
    r.run_forever()
        
