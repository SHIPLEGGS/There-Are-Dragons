import random


class Environment:
    def __init__(self):
        weather_choice_1 = random.randint(0, 4)
        weather_choice_2 = random.randint(0, 2)
        weather_choice_3 = random.randint(0, 3)

        if weather_choice_1 == 1:
            self.weather = "storm"
        elif weather_choice_1 == 2:
            self.weather = "fog"
        elif weather_choice_1 == 3:
            self.weather = "rain"
        else:
            self.weather = "sunshine"

        if weather_choice_2 == 1:
            self.temperature = "warm"
        else:
            self.temperature = "cold"

        if weather_choice_3 == 1:
            print(weather_choice_3)
            self.visibility = "poor"
        elif weather_choice_3 == 2:
            self.visibility = "moderate"
        else:
            self.visibility = "good"


environment = Environment()
print(environment.visibility, environment.temperature, environment.weather)
