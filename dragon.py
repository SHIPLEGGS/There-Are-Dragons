import special_attribute
import trainer


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

    def attack_bite(self, user_trainer, dragon, enemy):
        special_attribute.special_attributes_unique_run(dragon, user_trainer, 0, enemy)
        enemy.health -= self.attack_damage

    def attack_breath_fire(self, user_trainer, dragon, enemy):
        special_attribute.special_attributes_unique_run(dragon, user_trainer, 1, enemy)
        enemy.health -= self.magic_damage

    def get_dragon_attributes(self):
        print(str(self.name) + "s Attributes: ")
        print("Attack Damage: " + str(self.attack_damage) + " Magic Damage: " + str(self.magic_damage))
        print("Speed: " + str(self.speed) + " Size: " + str(self.size))
        print("Colour: " + str(self.camouflage) + " Vision: " + str(self.eyesight))
        print("Health: " + str(self.health) + " Intelligence: " + str(self.intelligence))


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
