import random

class EngineSystem:
    def __init__(self):
        self.n1 = 0 #Engine Speed N1
        self.n2 = 0 #Engine Speed N2
        self.oil_pressure = 0 #Oil pressure PSI
        self.oil_temperature = 0 #Oil temperature (°C)
        self.egt = 0 #Engine Exhaust Gas Temperature (°C)

    def update(self):
        '''Simulate real time updates for engine parameters'''
        self.n1 = random.uniform(20, 100)  # Simulate N1 between 20% and 100%
        self.n2 = random.uniform(50, 95)  # Simulate N2 between 50% and 95%
        self.oil_pressure = random.uniform(20, 60)  # Simulate oil pressure between 20 and 60 PSI
        self.oil_temperature = random.uniform(80, 120)  # Simulate oil temperature between 80 and 120°C
        self.egt = random.uniform(400, 900)  # Simulate EGT between 400°C and 900°C

    def get_data(self):
        '''Fetching current engine data'''
        return{
            "N1": self.n1,
            "N2": self.n2,
            "Oil Pressure": self.oil_pressure,
            "Oil Temperature": self.oil_temperature,
            "EGT": self.egt
        }