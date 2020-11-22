import pygame
import logging
from pygame import init
from pygame.math import Vector2
from pygame import Rect
import random
from commands import JumpCommand
from background_state import BackgroundState
from bird_state import BirdState
from global_vars import GlobalVars


    
class GameState:


    def __init__(self):
        self.world_size = GlobalVars.get_world_size()
        self.bird_state = BirdState()
        self.background_state = BackgroundState()

    def update(self, move_command):
        self.bird_state.update(move_command)
        self.background_state.update()

    def get_bird_position(self):
        return self.bird_state.bird_position



class Game:


    def __init__(self):
        pygame.init()
        
        pygame.display.set_caption("Floppy Birdie")
        self.clock = pygame.time.Clock()
        self.game_state = GameState()
        self.move_command =  None
        self.cell_size = GlobalVars.get_cell_size()
        self.game_window = pygame.display.set_mode(
            (int(self.cell_size.x * self.game_state.world_size.x), 
            int(self.cell_size.y * self.game_state.world_size.y))
            )
        self.window_size = self.game_state.world_size.elementwise() * self.cell_size
        self.running = True
        self.score = 0

    def processInput(self): 

        self.move_command = None
        for event in pygame.event.get():

            if event.type == pygame.constants.QUIT:
                self.running = False
                break
            elif event.type == pygame.constants.KEYDOWN:
                if event.key == pygame.constants.K_ESCAPE:
                    self.running = False
                    break
                
                elif event.key == pygame.constants.K_SPACE or event.key == pygame.constants.K_w:
                    self.move_command = JumpCommand()
    
    def update(self):
        self.game_state.update(self.move_command)
   
    def render(self): 
        #self.game_window.fill((0,0,0))

        

        # Draw Background

        self.game_window.blit(
            self.game_state.background_state.background_image.sprite,
            Vector2(0,0),
            self.game_state.background_state.background_image.texture_rect
        ) 


        # Draw Bird
        self.game_window.blit(
            self.game_state.bird_state.bird_sprite, 
            self.game_state.get_bird_position().elementwise() * self.cell_size,
            self.game_state.bird_state.texture_rect
            )

        
        # Draw Pipes

        for pipe_tuple in self.game_state.background_state.pipe_list:
            for pipe in pipe_tuple:
                self.game_window.blit(
                    pipe.sprite,
                    pipe.location.elementwise() * self.cell_size,
                    pipe.texture_rect
                )

        pygame.display.update()

    def run(self):

        while self.running:
            self.processInput()
            self.update()
            self.render()
            self.clock.tick(60)
