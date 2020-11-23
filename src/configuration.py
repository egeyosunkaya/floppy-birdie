import os

def __str_to_bool(val):
    return str(val).capitalize() == "TRUE"

class Configuration:

    @staticmethod
    def is_debug_mode_enabled():
        return os.environ.get("FLAPPY_DEBUG_ENABLED", "False")