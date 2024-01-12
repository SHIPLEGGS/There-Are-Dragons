import random

import dragon


class Environment:
    def __init__(self):
        weather_choice_1 = random.randint(0, 4)
        weather_choice_2 = random.randint(0, 2)
        weather_choice_3 = random.randint(0, 5)

        if weather_choice_1 == 1:
            self.weather = "Black"
        elif weather_choice_1 == 2:
            self.weather = "Grey"
        elif weather_choice_1 == 3:
            self.weather = "White"
        else:
            self.weather = "Invisible"

        if weather_choice_2 == 1:
            self.temperature = "warm"
        else:
            self.temperature = "cold"

        if weather_choice_3 == 1:
            print(weather_choice_3)
            self.visibility = "Good"
        elif weather_choice_3 == 2:
            self.visibility = "Moderate"
        elif weather_choice_3 == 3:
            self.visibility = "Bad"
        elif weather_choice_3 == 4:
            self.visibility = "Blind"
        elif weather_choice_3 == 5:
            self.visibility = "All-Seeing"

    def apply_weather_factors(self):
        for i in dragon.all_dragons:
            if i.eyesight == self.visibility:
                i.attack_speed += 2
            if i.camouflage == self.weather:
                i.size += 2
            if self.temperature == "warm":
                i.attack_damage += 2
            else:
                i.magic_damage += 2


environment = Environment()
print(environment.visibility, environment.temperature, environment.weather)
