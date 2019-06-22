from .sound_bar_controller import SoundBarController
from .tv_controller import TvController


class DomoticManager():

    def __init__(self):
        self.sound_bar_controller = SoundBarController()
        self.tv_controller = TvController()

    def execute_command(self, normalized_command):

        if normalized_command["object"] == "SOUND":
            if normalized_command["action"] == "TURN_OFF":
                self.sound_bar_controller.power_off()
            elif normalized_command["action"] == "INCREASE":
                self.sound_bar_controller.volume_up()
            elif normalized_command["action"] == "DECREASE":
                self.sound_bar_controller.volume_down()
            elif normalized_command["action"] == "PUT":
                self.sound_bar_controller.play_music()
            elif normalized_command["action"] == "PLAY":
                self.sound_bar_controller.play_music()
            elif normalized_command["action"] == "CHANGE":
                self.sound_bar_controller.next_track()

        elif normalized_command["object"] == "VOLUME":
            if normalized_command["action"] == "TURN_OFF":
                self.sound_bar_controller.power_off()
            elif normalized_command["action"] == "INCREASE":
                self.sound_bar_controller.volume_up()
            elif normalized_command["action"] == "DECREASE":
                self.sound_bar_controller.volume_down()

        elif normalized_command["object"] == "TV":
            if normalized_command["action"] == "TURN_OFF":
                self.tv_controller.power_off()

        elif normalized_command["object"] == "MUSIC":
            if normalized_command["action"] == "TURN_OFF":
                self.sound_bar_controller.power_off()
            if normalized_command["action"] == "PUT":
                self.sound_bar_controller.play_music()
            elif normalized_command["action"] == "INCREASE":
                self.sound_bar_controller.volume_up()
            elif normalized_command["action"] == "DECREASE":
                self.sound_bar_controller.volume_down()

        elif normalized_command["object"] == "PAUSE":
            if normalized_command["action"] == "PUT":
                self.tv_controller.pause()


if __name__ == "__main__":
    domotic_manager = DomoticManager()

    # Check the sound bar controller
    print(domotic_manager.sound_bar_controller.get_status())

    # Check the TV controller
    domotic_manager.tv_controller.netflix()
