from .sound_bar_controller import SoundBarController
from .tv_controller import TvController

class DomoticManager():

    def __init__(self):
        self.sound_bar_controller = SoundBarController()
        self.tv_controller = TvController()

if __name__ == "__main__":
    domotic_manager = DomoticManager()

    # Check the sound bar controller
    print(domotic_manager.sound_bar_controller.get_status())

    # Check the TV controller
    domotic_manager.tv_controller.netflix()
