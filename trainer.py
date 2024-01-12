class Trainer:
    def __init__(self, name, strength, speed, cunning):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.cunning = cunning
        self.lives = 3
        self.trainer_attack_modifiers = [self.strength, self.speed]
        self.trainer_speed_modifiers = self.speed
        self.dragons = []
        self.opponent = None
        self.rounds_played = 0

    # Can modify a dragons attacks
    def attack_modify(self, dragon, attack_type):
        if attack_type == 0:
            trainer_modified_attack = 0
            for i in range(len(dragon.attack_modifiers)):
                trainer_modified_attack = self.trainer_attack_modifiers[i] * dragon.attack_modifiers[i]
            dragon.attack_damage = (dragon.size +
                                    (dragon.attack_speed * dragon.attack_damage) + trainer_modified_attack)
            dragon.magic_damage = 0
            print(dragon.attack_damage, " Attack Damage! ")
        elif attack_type == 1:
            dragon.magic_damage = dragon.magic_damage ** 2 * dragon.intelligence / dragon.size
            dragon.magic_damage += self.cunning * 1 / self.strength
            dragon.attack_damage = 0
            print(dragon.magic_damage, " Magic Damage")

    # Can modify a dragons speed
    def speed_modify(self, dragon):
        trainer_modified_speed = 0
        for i in range(len(dragon.speed_modifiers)):
            trainer_modified_speed += self.trainer_speed_modifiers * dragon.speed_modifiers[i]
        dragon.speed = dragon.speed + trainer_modified_speed - (
                dragon.size / 2)
        dragon.attack_speed = dragon.attack_speed + trainer_modified_speed

    # Can level up a dragon
    def level_up_dragon(self, dragon):
        print(dragon, " has levelled up... ")
        magic_or_attack = input("Level up fire breath, or level up physical attack: ")
        smaller_or_bigger = input("Starve your dragon, or overfeed your dragon: ")
        self.dragons[dragon].health += 50
        self.dragons[dragon].speed += 1
        if magic_or_attack == 0:
            self.dragons[dragon].attack_damage += 2
        else:
            self.dragons[dragon].magic_damage += 2
        if self.name == "Tiber Septim":
            self.dragons[dragon].size += 1
        if smaller_or_bigger == 0:
            self.dragons[dragon].size += 1
        else:
            self.dragons[dragon].size -= 1

    # Can allow their user to level up a dragon
    def dragon_level_up_choice(self):
        choice = input("Choose a dragon to level up: ")
        for i in range(len(self.dragons)):
            print(str(self.dragons[i].name) + ": " + str(i))
            if choice == str(i):
                choice_to_level_up = self.dragons[i]
                self.level_up_dragon(choice_to_level_up)

    # Can increase their attributes
    def attribute_add(self):
        attribute_to_add = input("Choose a trainer attribute to increase: ")
        print("Strength: 1")
        print("Speed: 2")
        print("Cunning: 3")
        if attribute_to_add == 1:
            self.strength += 1
        elif attribute_to_add == 2:
            self.speed += 1
        elif attribute_to_add == 3:
            self.cunning += 1


Tiber_Septim = Trainer("Tiber Septim   ", 12, 10, 12)
Reman_Cyrodiil = Trainer("Reman Cyrodiil ", 7, 7, 7)
Isildur = Trainer("Isildur        ", 8, 6, 6)
Isildur.dragons_slain = []
Astrid = Trainer("Astrid         ", 4, 10, 6)
Miraak = Trainer("Miraak         ", 4, 3, 8)
Miraak.resurrection_count = 0
Hiccup = Trainer("Hiccup         ", 0, 4, 15)
Nerevar = Trainer("Indoril Nerevar", 0, 0, 0)
Arthur = Trainer("Arthur         ", 6, 5, 4)
Farren = Trainer("Farren         ", 4, 4, 7)
Vyrthr = Trainer("Vyrthr         ", 3, 9, 3)
Reddah_Aaltus = Trainer("Reddah Aaltus  ", 5, 5, 5)
Anna_Regalia = Trainer("Anna Regalia   ", 3, 3, 3)

all_trainers = [Hiccup, Miraak, Astrid, Isildur, Reman_Cyrodiil, Tiber_Septim, Nerevar, Arthur, Farren, Reddah_Aaltus,
                Anna_Regalia, Vyrthr]
beginner_trainers = [Arthur, Farren, Reddah_Aaltus, Anna_Regalia, Vyrthr]
