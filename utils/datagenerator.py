import random

import numpy as np
import random


class DataGenerator:
    def __init__(self, min_temp=10.0, max_temp=30.0, min_hum=50.0, max_hum=70.0, min_heat=10.0, max_heat=30.0,
                 min_light=100, max_light=1100, min_gtemp=8.0,
                 max_gtemp=32.0, min_gmoist=10.0, max_gmoist=80.0):
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.min_hum = min_hum
        self.max_hum = max_hum
        self.min_heat = min_heat
        self.max_heat = max_heat
        self.min_light = min_light
        self.max_light = max_light
        self.min_gtemp = min_gtemp
        self.max_gtemp = max_gtemp
        self.min_gmoist = min_gmoist
        self.max_gmoist = max_gmoist

    def generate_temp(self):
        for x in np.arange(self.min_temp, self.max_temp, 0.01):
            yield round(x, 2)

    def generate_hum(self):
        pass

    def generate_heat(self):
        pass

    def generate_light(self):
        pass

    def generate_gtemp(self):
        pass

    def generate_gmoist(self):
        pass

    def generate_time(self):
        pass