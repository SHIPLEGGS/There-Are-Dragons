
import trainer
from special_attribute import special_attributes_unique_run


def assign_dragons():
    count = 0
    for i in all_dragons:
        trainer.all_trainers[count].dragons.append(i)
        count += 1


class Dragon:
    def __init__(self, name, speed, attack_damage, eyesight, size, camouflage, intelligence):
        self.name = name
        self.speed = speed
        self.attack_speed = speed * 1 / size
        self.attack_damage = attack_damage
        self.magic_damage = attack_damage
        self.eyesight = eyesight
        self.size = size
        self.camouflage = camouflage
        self.intelligence = intelligence
        self.health = 300
        self.attack_modifiers = [self.size, self.attack_damage]
        self.speed_modifiers = [self.size, self.speed, self.attack_speed]
        self.attack_types = [self.attack_damage, self.magic_damage]

    def attack_bite(self, user_trainer, enemy):
        special_attributes_unique_run(self, user_trainer, 0, enemy)
        enemy.health -= self.attack_damage

    def attack_breath_fire(self, user_trainer, enemy):
        special_attributes_unique_run(self, user_trainer, 1, enemy)
        enemy.health -= self.magic_damage

    def get_dragon_attributes(self):
        print(str(self.name) + "s Attributes: ")
        print("Attack Damage: " + str(self.attack_damage) + " Magic Damage: " + str(self.magic_damage))
        print("Speed: " + str(self.speed) + " Size: " + str(self.size))
        print("Colour: " + str(self.camouflage) + " Vision: " + str(self.eyesight))
        print("Health: " + str(self.health) + " Intelligence: " + str(self.intelligence))

    # Can level up a dragon
    def level_up_dragon(self):
        print(self.name, " has levelled up... ")
        print("Level up fire breath, or level up physical attack: 0 ; 1")
        print("Starve your dragon, or overfeed your dragon: 0 ; 1")
        magic_or_attack = input(" ==> ")
        smaller_or_bigger = input(" ==> ")
        self.health += 50
        self.speed += 1
        if magic_or_attack == "0":
            self.attack_damage += 2
            print(self.attack_damage)
        elif magic_or_attack == "1":
            self.magic_damage += 2
            print(self.magic_damage)
        else:
            print("Failed Input.")
            return "input_fail"
        if self.name == "Tiber Septim":
            self.size += 1
        if smaller_or_bigger == "0":
            self.size += 1
            print(self.size)
        elif smaller_or_bigger == "1":
            self.size -= 1
            print(self.size)
        else:
            print("Failed Input.")
            return "input_fail"


Rongwield = Dragon("Rongwield", 1, 2, "Good", 5, "Black", 3)
Gerhardt = Dragon("Gerhardt", 1, 2, "Bad", 4, "Black", 2)
Wunduniik = Dragon("Wuunduniik", 3, 4, "Good", 3, "Grey", 4)
Vesper = Dragon("Vesper", 4, 3, "Moderate", 1, "White", 4)
Sahlokaniir = Dragon("Sahlokaniir", 1, 2, "Good", 2, "Grey", 5)
Fenriir = Dragon("Fenriir", 3, 3, "Blind", 1, "Invisible", 3)
Aarensfjior = Dragon("Aarensfjior", 2, 1, "All-Seeing", 3, "Grey", 3)
Haelgir = Dragon("Haelgir", 2, 1, "Moderate", 2, "White", 2)
Ilkriim = Dragon("Ilkriim", 3, 3, "Moderate", 2, "Black", 2)
Norghar = Dragon("Norghar", 2, 1, "Bad", 2, "White", 1)
Thoralde = Dragon("Thoralde", 1, 2, "Bad", 4, "Grey", 3)
Ywennen = Dragon("Ywennen", 2, 1, "Good", 3, "Grey", 4)
all_dragons = [Rongwield, Gerhardt, Wunduniik, Vesper, Sahlokaniir, Fenriir, Aarensfjior, Haelgir,
               Ilkriim, Norghar, Thoralde, Ywennen]
