from sound_bar_controller import SoundBarController

class DomoticManager():

    def __init__(self):
        self.sound_bar_controller = SoundBarController()


if __name__ == "__main__":
    domotic_manager = DomoticManager()
    print(domotic_manager.sound_bar_controller.get_status())
    #sound_controller.mute()
