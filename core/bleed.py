import random

class BleedSystem:
    def __init__(self):
        self.temperature_lo = 0  # Low temperature sensor reading (°C)
        self.temperature_hi = 0  # High temperature sensor reading (°C)
        self.pressure = 0        # Pressure reading (PSI)

    def update(self):
        """Simulate real-time updates for bleed parameters."""
        self.temperature_lo = random.uniform(20, 50)  # Simulate low temperature between 20°C and 50°C
        self.temperature_hi = random.uniform(40, 70)  # Simulate high temperature between 40°C and 70°C
        self.pressure = random.uniform(20, 60)       # Simulate pressure between 20 PSI and 60 PSI

    def get_data(self):
        """Return current bleed system data."""
        return {
            "Temperature LO": self.temperature_lo,
            "Temperature HI": self.temperature_hi,
            "Pressure": self.pressure,
        }