import pygame


class CollisionChecker: 

    def __init__(self, background_state, bird_state):
        self.background_state = background_state
        self.bird_state = bird_state

    def check_collision(self):
        for pipe_tuple in self.background_state.pipe_list:
            for pipe in pipe_tuple:
                if pipe.get_collision_box().colliderect(self.bird_state.get_collision_box()):
                    print("Collision detected")
                    return True

        return False 