import random

class SmartBin:
    def __init__(self, initial_level=0):
        self.bin_level = initial_level
        self.motion_detected = False

    def set_level(self, level):
        if not (0 <= level <= 100):
            raise ValueError("Bin level must be between 0 and 100.")
        self.bin_level = level

    def simulate_level_change(self):
        # Replaces manual input() - randomly increases level to simulate real use
        self.bin_level = min(100, self.bin_level + random.randint(0, 10))

    def simulate_motion(self):
        self.motion_detected = random.choice([True, False])

    def get_notification(self):
        if self.bin_level == 100:
            return "The bin is full! Sending notification..."
        elif self.bin_level >= 80:
            return "The bin is almost full! Sending notification..."
        elif self.bin_level >= 50:
            return "Past halfway! Sending notification..."
        else:
            return "The bin is not full yet. No notification sent."

    def get_status(self):
        return {
            "device": "smart_bin",
            "bin_level": self.bin_level,
            "notification": self.get_notification(),
            "lid_open": self.motion_detected
        }


# Only runs when you test this file directly - won't interfere when imported
if __name__ == "__main__":
    bin = SmartBin()
    bin.set_level(85)
    bin.simulate_motion()
    print(bin.get_status())