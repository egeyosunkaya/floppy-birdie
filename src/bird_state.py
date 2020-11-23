import logging
from pygame.math import Vector2
from pygame import Rect, image
from global_vars import GlobalVars
import pygame

class BirdState:

    def __init__(self):
        self.scale = 1.0 / 16
        self.Vx = 0
        self.Vy = -1 * self.scale 
        self.Ax = 0
        self.Ay = 0
        self.time_step = 0.01
        self.gravity = 0.3
        self.Vx_limit_upper = 2 * self.scale
        self.Vy_limit_upper = -2 * self.scale
        self.Vx_limit_lower = -2 * self.scale
        self.Vy_limit_lower = 2 * self.scale 
        self.bird_position = Vector2(2,3)
        self.bird_sprite = image.load("assets/Bird2.png")
        self.texture_rect = Rect(0,0, 96, 96)
        self.bitmask = pygame.mask.from_surface(self.bird_sprite)

    def update(self, move_command):

        if move_command != None:
            self.Vx += move_command.get_move_vector().x * self.scale
            self.Vy += move_command.get_move_vector().y * self.scale

        self.Vx = min(
            self.Vx_limit_upper, 
            self.Vx + (self.Ax * self.time_step)
            )

        self.Vy = max(
            min(
                self.Vy_limit_lower, 
                self.Vy + self.gravity * self.time_step
            ),
            self.Vy_limit_upper
            )
    
        self.bird_position += Vector2(self.Vx, self.Vy)

    def get_move_vector(self):
        return Vector2(self.Vx, self.Vy)

    def get_collision_box(self):

        return self.bird_sprite.get_bounding_rect(min_alpha=1).move(self.bird_position.elementwise() * GlobalVars.get_cell_size())

            