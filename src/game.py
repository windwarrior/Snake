import pygame
import random
from time import sleep

from pygame.locals import *
from pygame.color import Color

from renderer import Renderer
from level import Level
from entity import Entity, Point, PowerUp
from snake import Snake
from player import Direction, ControlScheme, Player, ControlWASD, ControlArrows

from gamestate import GameState
    
class Game():
    def __init__(self):
        self.gameState = GameState.InitState

        self.level = Level(24,18, self)
        self.renderer = Renderer(self)
        self.ticks = 0

        self.initialize()

    def initialize(self):
        pygame.init()

    def event(self, event):
        if event.type == pygame.QUIT:
            self.gameState = GameState.QuitState
        elif event.type == KEYDOWN:
            if event.key == K_p:
                self.gameState = GameState.PauzeState
            else:
                for player in self.level.players:
                    if event.key in player.controlscheme.getAllKeys():
                        player.setDirective(event.key)

    def setGameOver(self):
        print "game over"
        self.gameState = GameState.GameOverState

    def gameTick(self):
        for entity in self.level.entities + self.level.players:
            entity.tick()

    def frameTick(self):
        self.renderer.tick(0)

    def startScreen(self):
        pass

    def gameRun(self):
        gameticks = 0
        frameticks = 0
        while(self.gameState == GameState.RunState):
            for event in pygame.event.get():
                self.event(event)

            if(self.ticks % 3 == 0):
                gameticks += 1
                self.gameTick()

            self.frameTick()
            frameticks += 1
            self.ticks += 1

            sleep(1.0/60.0)

    def gameInit(self):
        self.level.players = [
                Player((4,0), [(0,0,Color("red")), (1,0,Color("red")), (2,0,Color("Yellow"))], Color("red"), self, (1,0), ControlArrows),
                Player((4,4), [(0,0,Color("blue")), (1,0,Color("blue")), (2,0,Color("Yellow"))], Color("blue"), self, (1,0), ControlWASD)
                ]

        self.level.entities = [
            #PowerUp((10,10), self)
        ]
        self.level.spawnNewPoint()
        self.level.spawnNewPoint()
        self.gameState = GameState.RunState 
      
    def gamePauze(self):
        while(self.gameState == GameState.PauzeState):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameState = GameState.QuitState    
                elif event.type == KEYDOWN:
                    if event.key == K_p:
                        self.gameState = GameState.RunState
            sleep(0.1)

    def gameOver(self):
        while(self.gameState == GameState.GameOverState):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameState = GameState.QuitState
                elif event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        self.gameState = GameState.InitState        

    def run_forever(self):
        running = True
        while(running):
            if   self.gameState == GameState.InitState:
                self.gameInit()
            elif self.gameState == GameState.RunState:
                self.gameRun()
            elif self.gameState == GameState.PauzeState:
                self.gamePauze()
            elif self.gameState == GameState.GameOverState:
                self.gameOver()
            elif self.gameState == GameState.QuitState:
                running = False

        self.gameState = GameState.QuitState
                
        pygame.quit()

if __name__ == "__main__":
    r = Game()
    r.run_forever()
        
