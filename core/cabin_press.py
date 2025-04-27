import random

class CabinPressureSystem:
    def __init__(self):
        self.cabin_altitude = 0 #Cabin Altitude (feet)
        self.delta_pressure = 0 #Differential Pressure (PSI)
        self.vertical_speed = 0 #Vertical Speed ft/m
    
    def update(self):
        """Simulating with data for real time updates on cabin pressurizartion"""
        self.cabin_altitude = random.uniform(0,8000) #Simulation of altitude params upto 8000ft
        self.delta_pressure = random.uniform(7,9) #Simulation of PSI @ 7/9
        self.vertical_speed = random.uniform(-1000, 1100) #Verical speed limits of descent and climb perf

    def get_data(self):
        return{
            "Cabin Altitude": self.cabin_altitude,
            "Delta Pressure PSI": self.delta_pressure,
            "Verical Speed":self.vertical_speed
        }