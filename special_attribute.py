import random
from Main import all_trainers


class Special_Attribute:
    def __init__(self, name):
        self.name = name


Toothless = Special_Attribute("Toothless")
Bend_Will = Special_Attribute("Bend Will")
Miraak_Shout = Special_Attribute("Zii Los Dii Du")
Miraak_Shout.ResurrectCount = 1
Valkyrie = Special_Attribute("Flight of the Valkyrie")
Nazgul = Special_Attribute("Angmar's Dominion")
Nazgul.Dragons_Slain = []
Dragonborn_King = Special_Attribute("The Dragonborn King")
Tiber_1 = Special_Attribute("Founder of the First Empire")
Tiber_2 = Special_Attribute("Chimarmavidium: The Last Miracle of Kagrenac")
Indoril = Special_Attribute("Saint Nerevar, Moon-and-star")


def special_attribute_check(trainer, dragon, enemy):
    for i in trainer.special_attributes:
        if i.name == "Toothless":
            dragon.attack_damage = 0
            if dragon.health < (dragon.health / 100) * 20:
                dragon.attack_modify(dragon)
                dragon.attack_damage = dragon.attack_damage * 3
                print("Critical Strike")
        elif i.name == "Bend Will":
            chance_to_bend_will_1 = random.randint(0, 4)
            chance_to_bend_will_2 = random.randint(0, 4)
            if chance_to_bend_will_1 == chance_to_bend_will_2:
                print("Gol Hah Dov!")
                trainer.dragons.append(enemy)
                trainer.bend_will_convert(enemy)
        elif i.name == "Zii Los Dii Du":
            if trainer.lives <= 0 and Miraak_Shout.ResurrectCount != 0:
                print("Zii Los Dii Du")
                trainer.lives += 1
                dragon.attack_damage = 10000
            else:
                print("Miraak Slain")
        elif i.name == "Flight of the Valkyrie":
            if enemy.speed < dragon.speed:
                print("I shall run you in circles!")
                dragon.speed += 5
            else:
                print("So you have chosen violence...")
                dragon.attack_damage += 2
        elif i.name == "Angmar's Dominion":
            for souls in Nazgul.Dragons_Slain:
                dragon.attack_damage += 10
                print("The foul kingdom should rise again!")
            if (enemy.health - dragon.attack_damage) <= 0:
                Nazgul.Dragons_Slain.append(enemy)
        elif i.name == "The Dragonborn King":
            if dragon.health > enemy.health:
                dragon.health += 300
                print("Lord of the Dragonguard")
            else:
                trainer.attribute_add()
                print("Legends of Akavir empower me...")
        elif i.name == "Founder of the First Empire":
            for j in range(trainer.rounds_played):
                trainer.dragon_level_up_choice()
        elif i.name == "Chimarmavidium: The Last Miracle of Kagrenac":
            if trainer.lives <= 0:
                trainer.lives += 1
                print("The Heart of Lorkhan Prevails")
                for dragons in trainer.dragons:
                    dragons.health += 100
                    dragons.attack_damage += 5
                    dragons.attack_speed += 5
                    dragons.size += 5
                    dragons.eyesight.replace(dragons.eyesight, "All-Seeing")
                    dragons.camouflage.replace(dragons.camouflage, "Invisible")
                    dragons.intelligence.replace(dragons.intelligence, "All-Knowing")
        elif i.name == "Saint Nerevar, Moon-and-star":
            stars = 0
            print("Nerevar at Red MOUNTAIN!!!")
            for items in all_trainers:
                for item in items.dragons:
                    stars += 5
            for my_dragons in range(stars):
                for my_dragon in trainer.dragons:
                    trainer.level_up_dragon(my_dragon)
