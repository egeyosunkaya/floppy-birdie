from pygame.math import Vector2


# __cell_size = Vector2(64,64)
# __world_size = Vector2(12,8)
class GlobalVars:


    @staticmethod
    def get_cell_size():
        return Vector2(64,64)

    @staticmethod
    def get_world_size():
        return Vector2(12,8)

    @staticmethod
    def get_screen_size():
        return Vector2 (
            int(GlobalVars.get_cell_size().x * GlobalVars.get_world_size().x), 
            int(GlobalVars.get_cell_size().y * GlobalVars.get_world_size().y),
        )
    