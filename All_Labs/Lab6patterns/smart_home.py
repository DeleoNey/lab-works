class SingletonMeta(type):
    """A metaclass for implementing the Singleton pattern."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class SettingsManager(metaclass=SingletonMeta):
    """Global settings for a smart home."""
    def __init__(self):
        self.settings = {
            "temperature": 22,
            "lighting_mode": "warm",
        }

    def set_setting(self, key, value):
        self.settings[key] = value

    def get_setting(self, key):
        return self.settings.get(key)


class EnergyManager(metaclass=SingletonMeta):
    """Power consumption management."""
    def monitor_usage(self):
        return "Energy usage is being monitored."

    def optimize_energy(self):
        return "Energy usage has been optimized."


class LightingSystem:
    """Lighting system."""
    def start(self):
        return "Lighting system turned on."

    def stop(self):
        return "Lighting system turned off."

    def set_brightness(self, level):
        return f"Brightness set to {level}."


class ClimateControlSystem:
    """Climate control system."""
    def start(self):
        return "Climate control started."

    def stop(self):
        return "Climate control stopped."

    def set_temperature(self, target_temp):
        return f"Temperature set to {target_temp}°C."

class EntertainmentSystem:
    def play_music(self):
        return "Music is playing."

    def stop_music(self):
        return "Music stopped."

    def set_volume(self, level):
        return f"Volume set to {level}."


class SecuritySystem:
    """Security system."""
    def start(self):
        return "Security system armed."

    def stop(self):
        return "Security system disarmed."

class VoiceControl:
    def __init__(self, facade):
        self.facade = facade

    def execute_command(self, command):
        commands_map = {
            "turn on lights": self.facade.control_lighting,
            "arm security": self.facade.activate_security_system,
            "set temperature": lambda: self.facade.set_climate_control(22),
        }
        action = commands_map.get(command.lower(), lambda: "Command not recognized.")
        return action()



class SmartHomeFacade:
    """Facade for simplified access to subsystems."""
    def __init__(self):
        self.settings = SettingsManager()
        self.energy = EnergyManager()
        self.lighting = LightingSystem()
        self.climate = ClimateControlSystem()
        self.security = SecuritySystem()
        self.entertainment = EntertainmentSystem()
        self.voice_control = VoiceControl(self)



    def activate_lighting(self):
        return self.lighting.start()

    def deactivate_lighting(self):
        return self.lighting.stop()

    def set_brightness(self, level):
        return self.lighting.set_brightness(level)

    def activate_climate_control(self, temperature=None):
        response = self.climate.start()
        if temperature:
            response += f" {self.climate.set_temperature(temperature)}"
        return response

    def deactivate_climate_control(self):
        return self.climate.stop()

    def arm_security(self):
        return self.security.start()

    def disarm_security(self):
        return self.security.stop()
