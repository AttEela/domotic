from .pyviera.pyviera import VieraFinder


class TvController():
    def __init__(self):
        self.device = VieraFinder().get_viera()

    def power_off(self):
        self.device.power()

    def mute(self):
        self.device.mute()

    def pause(self):
        self.device.pause()

    def netflix(self):
        self.device.netflix()

    def get_volume(self):
        return self.device.get_volume()


if __name__ == '__main__':
    tv_controller = TvController()
    tv_controller.netflix()
