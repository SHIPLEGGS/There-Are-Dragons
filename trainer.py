import special_attribute


class Trainer:
    def __init__(self, name, strength, speed, cunning):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.cunning = cunning
        self.special_attributes = []
        self.lives = 3
        self.trainer_attack_modifiers = [self.strength, self.speed]
        self.trainer_speed_modifiers = self.speed
        self.dragons = []
        self.rounds_played = 0

    def attack_modify(self, dragon, attack_type):
        if attack_type == 0:
            trainer_modified_attack = 0
            for i in range(len(dragon.attack_modifiers)):
                trainer_modified_attack = self.trainer_attack_modifiers[i] * dragon.attack_modifiers[i]
            dragon.attack_damage = dragon.size + (dragon.attack_speed * dragon.attack_damage) + trainer_modified_attack
            dragon.magic_damage = 0
            print(dragon.attack_damage)
        elif attack_type == 1:
            dragon.magic_damage = dragon.magic_damage ** 2 * dragon.intelligence / dragon.size
            dragon.attack_damage = 0
            print(dragon.magic_damage)

    def speed_modify(self, dragon):
        trainer_modified_speed = 0
        for i in range(len(dragon.speed_modifiers)):
            trainer_modified_speed += self.trainer_speed_modifiers * dragon.speed_modifiers[i]
        dragon.speed = dragon.speed + trainer_modified_speed - (dragon.size / 2)
        dragon.attack_speed = dragon.attack_speed + trainer_modified_speed
        print(dragon.attack_speed, dragon.speed)

    def bend_will_convert(self, enemy):
        for i in special_attribute.all_trainers:
            if i != special_attribute.Miraak:
                i.dragons.remove(enemy)

    def level_up_dragon(self, dragon):
        print(dragon, " has levelled up... ")
        magic_or_attack = input("Level up fire breath, or level up physical attack: ")
        smaller_or_bigger = input("Starve your dragon, or overfeed your dragon: ")
        dragon.health += 50
        dragon.speed += 1
        if magic_or_attack == 0:
            dragon.attack_damage += 2
        else:
            dragon.magic_damage += 2
        if self.name == "Tiber Septim":
            dragon.size += 1

    def attack_bite(self, dragon, enemy):
        special_attribute.special_attribute_check(self, dragon, enemy, 0)
        enemy.health -= dragon.attack_damage

    def attack_breath_fire(self, dragon, enemy):
        special_attribute.special_attribute_check(self, dragon, enemy, 1)
        enemy.health -= dragon.magic_damage

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

    def dragon_level_up_choice(self):
        choice = input("Choose a dragon to level up: ")
        for i in range(len(self.dragons)):
            print(str(self.dragons[i].name) + ": " + str(i))
            if choice == str(i):
                choice_to_level_up = self.dragons[i]
            break
        self.level_up_dragon(choice_to_level_up)
