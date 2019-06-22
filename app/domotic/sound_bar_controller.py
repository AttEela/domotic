from libsoundtouch import discover_devices


class SoundBarController():
    """
        Class to control the sound bar.
    """
    def __init__(self):
        self.device = discover_devices(timeout=2)[0]

    def get_status(self):
        return self.device.status()

    def mute(self):
        """Mute and un-mute."""
        self.device.mute()

    def volume_up(self):
        """Volume up."""
        self.device.volume_up()

    def volume_down(self):
        """Volume down."""
        self.device.volume_down()

    def volume_set(self, level):
        """Set volume level: from 0 to 100."""
        self.device.set_volume(level)


if __name__ == "__main__":
    sound_controller = SoundBarController()
    print(sound_controller.get_status())
    # sound_controller.mute()
