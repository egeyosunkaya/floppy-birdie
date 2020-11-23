import pygame
import logging
from pygame.math import Vector2
from pygame import Rect
from pygame.transform import flip
from global_vars import GlobalVars
import random

class BackgroundState:

    def __init__(self): 
        self.pipe_list = []
        self.pipe_factory = PipeFactory()
        self.pipe_list.append(self.pipe_factory.create_pipe())
        self.velocity_scale = 0.05
        self.pipe_offset_x = 6

        self.background_image = BackgroundImage()

        


    def update(self):
        for pipe_tuple in self.pipe_list:
            for pipe in pipe_tuple:
                pipe.location += Vector2(-1,0).elementwise() * self.velocity_scale
        
        if self.pipe_list[-1][0].location.x < GlobalVars.get_world_size().x - self.pipe_offset_x:
            self.pipe_list.append(
                self.pipe_factory.create_pipe()
            )
        
        if self.pipe_list[0][0].location.x < - 4:
            self.pipe_list.pop(0)
        


class PipeFactory:

    def __init__(self):
        self.image = pygame.image.load("assets/Pipe.png")
        self.last_created = 0
        self.texture_size = Vector2(280, 280)
        self.texture_offset = Vector2(0, 0)
        self.difficulty = 1
    def create_pipe(self):

        opennig_size_scale = random.randint(3, 6) * 0.40 * self.difficulty
        openning_y_middle =  random.normalvariate(GlobalVars.get_world_size().y / 2, sigma= 0.4)
        openning_y_upper = openning_y_middle - opennig_size_scale
        opennig_y_lower = openning_y_middle + opennig_size_scale
        self.last_created = (self.last_created + 1 ) % 2
        
        print("Middle: " + str(openning_y_middle), "Upper: " + str(openning_y_upper), "Lower:" + str(opennig_y_lower) )
        
        bottom_pipe =  Pipe(
                self.image,
                Vector2(
                    GlobalVars.get_world_size().x , 
                    opennig_y_lower),
                Rect(self.texture_offset, self.texture_size)
            ) 
            
        up_pipe =  Pipe(
                flip(self.image, False, True),
                Vector2(GlobalVars.get_world_size().x , openning_y_upper - (GlobalVars.get_world_size().y / 2)),
                Rect(self.texture_offset, self.texture_size)
            )

        return (up_pipe, bottom_pipe)
        

class BackgroundImage:

    def __init__(self):
        self.sprite = pygame.transform.scale(pygame.image.load("assets/background.jpg"),
            (int(GlobalVars.get_screen_size().x), int(GlobalVars.get_screen_size().y)),
         )
        self.location = Vector2(0,0)
        self.texture_rect = Rect(0, 0, 768, 512)

class Pipe:

    def __init__(self, sprite, location, texture_rect):
        self.sprite = sprite
        self.location = location 
        self.texture_rect = texture_rect
        self.bitmask = pygame.mask.from_surface(self.sprite)

    def get_collision_box(self):

        return self.sprite.get_bounding_rect(min_alpha=1).move(self.location.elementwise() * GlobalVars.get_cell_size())
        # return Rect(
        #     (self.location + Vector2(1.3, 0)).elementwise() * GlobalVars.get_cell_size(),
        #     (self.texture_rect.size[0] * 0.375, self.texture_rect.size[1] * 0.9)
        # )