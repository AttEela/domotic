from .sound_bar_controller import SoundBarController
from .tv_controller import TvController


class DomoticManager():

    def __init__(self):
        self.sound_bar_controller = SoundBarController()
        self.tv_controller = TvController()

    def execute_command(self, normalized_command):

        if ("action" in normalized_command.keys()) & ("object" in normalized_command.keys()):

            if normalized_command["object"] == "SOUND":
                if normalized_command["action"] == "TURN_OFF":
                    self.sound_bar_controller.volume_set(0)
                elif normalized_command["action"] == "INCREASE":
                    self.sound_bar_controller.volume_up()
                elif normalized_command["action"] == "DECREASE":
                    self.sound_bar_controller.volume_down()
                elif normalized_command["action"] in ["PUT", "PLAY"]:
                    self.sound_bar_controller.play_music()

            elif normalized_command["object"] == "VOLUME":
                if normalized_command["action"] == "INCREASE":
                    self.sound_bar_controller.volume_up()
                elif normalized_command["action"] == "DECREASE":
                    self.sound_bar_controller.volume_down()

            elif normalized_command["object"] == "TV":
                if normalized_command["action"] == "TURN_OFF":
                    self.tv_controller.power_off()

            elif normalized_command["object"] == "MUSIC":
                if normalized_command["action"] == "TURN_OFF":
                    self.sound_bar_controller.volume_set(0)
                elif normalized_command["action"] in ["PUT", "PLAY"]:
                    self.sound_bar_controller.play_music()
                elif normalized_command["action"] == "INCREASE":
                    self.sound_bar_controller.volume_up()
                elif normalized_command["action"] == "DECREASE":
                    self.sound_bar_controller.volume_down()
                elif normalized_command["action"] == "CHANGE":
                    self.sound_bar_controller.next_track()

            elif normalized_command["object"] == "PAUSE":
                if normalized_command["action"] == "PUT":
                    self.tv_controller.pause()

            elif normalized_command["object"] == "PLAY":
                if normalized_command["action"] == "PUT":
                    self.tv_controller.play()

            elif normalized_command["object"] == "DAMSO":
                if normalized_command["action"] in ["PUT", "PLAY"]:
                    self.sound_bar_controller.play_damso()

        elif ("action" in normalized_command.keys()) & ("quantity" in normalized_command.keys()):
            if normalized_command["action"] == "PUT":
                if normalized_command["quantity"] == "LOUDER":
                    self.sound_bar_controller.volume_up()
                elif normalized_command["quantity"] == "LOWER":
                    self.sound_bar_controller.volume_down()


if __name__ == "__main__":
    domotic_manager = DomoticManager()

    # Check the sound bar controller
    print(domotic_manager.sound_bar_controller.get_status())

    # Check the TV controller
    domotic_manager.tv_controller.netflix()
