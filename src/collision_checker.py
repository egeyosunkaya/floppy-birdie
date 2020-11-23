import pygame
from global_vars import GlobalVars


class CollisionChecker: 

    def __init__(self, background_state, bird_state):
        self.background_state = background_state
        self.bird_state = bird_state

    def check_collision(self):

        # Pipe - Bird Collision
        for pipe_tuple in self.background_state.pipe_list:
            for pipe in pipe_tuple:
                if pipe.get_collision_box().colliderect(self.bird_state.get_collision_box()):
                    print("Collision detected")
                    return True
        
        # Bird Out of bounds check 
        out_of_bounds_pixel_tolerance = 10
        bird_coll_box = self.bird_state.get_collision_box()
        if bird_coll_box.bottom > GlobalVars.get_screen_size().y + out_of_bounds_pixel_tolerance \
            or bird_coll_box.top < 0 - out_of_bounds_pixel_tolerance:
            print("Out of bounds deteced")
            return True

        return False 