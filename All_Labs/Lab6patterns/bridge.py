class Appliance:
    """Base class for devices."""
    def start(self):
        raise NotImplementedError

    def stop(self):
        raise NotImplementedError


class RemoteController:
    """Controller for managing devices."""
    def __init__(self, appliance: Appliance):
        self.appliance = appliance

    def turn_on(self):
        return self.appliance.start()

    def turn_off(self):
        return self.appliance.stop()
