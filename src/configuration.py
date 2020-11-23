import os


class Configuration:

    @staticmethod
    def __str_to_bool(val):
        return str(val).capitalize() == "TRUE"


    @staticmethod
    def is_debug_mode_enabled():
        return Configuration.__str_to_bool(os.environ.get("FLAPPY_DEBUG_ENABLED", "False"))