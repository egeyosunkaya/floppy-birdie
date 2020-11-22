
from pygame.math import Vector2

class JumpCommand:

    def get_move_vector(self):
        return Vector2(0,-1.5)