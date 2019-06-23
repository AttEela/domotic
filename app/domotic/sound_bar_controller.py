import time
from libsoundtouch import discover_devices
from libsoundtouch.utils import Source


class SoundBarController():
    """
        Class to control the sound bar.
    """
    def __init__(self):
        self.device = discover_devices(timeout=2)[0]

    def get_status(self):
        return self.device.status()

    def get_volume(self):
        return self.device.volume()

    def mute(self):
        """Mute and un-mute."""
        self.device.mute()

    def volume_set(self, level):
        """Set volume level: from 0 to 100."""
        self.device.set_volume(level)

    def volume_up(self):
        """Volume up."""
        self.device.set_volume(min(self.device.volume().actual + 5, 100))

    def volume_down(self):
        """Volume down."""
        self.device.set_volume(max(self.device.volume().actual - 5, 0))

    def power_off(self):
        """Turn off the device."""
        self.device.power_off()

    def play_music(self):
        uri = "spotify:playlist:37i9dQZF1DWTwnEm1IYyoj"
        uri = "spotify:user:spotify:playlist:37i9dQZF1DWVuV87wUBNwc"
        spot_user_id = ""
        self.device.play_media(Source.SPOTIFY, uri, spot_user_id)
        time.sleep(0.2)
        self.device.shuffle(True)
        self.device.next_track()
        self.device.set_volume(20)
        print("I play some music")

    def next_track(self):
        self.device.next_track()

    def play_damso(self):
        uri = "spotify:artist:2UwqpfQtNuhBwviIC0f2ie"
        spot_user_id = ""
        self.device.play_media(Source.SPOTIFY, uri, spot_user_id)
        time.sleep(0.2)
        self.device.shuffle(True)
        self.device.next_track()
        self.device.set_volume(20)
        print("I play some music")


if __name__ == "__main__":
    sound_controller = SoundBarController()
    print(sound_controller.get_status())
    # sound_controller.mute()
