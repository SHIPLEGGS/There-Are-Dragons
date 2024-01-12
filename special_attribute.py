import random

import environment
from trainer import Miraak, Isildur, all_trainers


def bend_will_convert(enemy):
    for i in all_trainers:
        if i != Miraak:
            i.dragons.remove(enemy)


def toothless(dragon, trainer, attack_type):
    dragon.health -= dragon.attack_types[attack_type]
    dragon.attack_types[attack_type] = 0
    dragon.attack_modify(dragon, 1)
    dragon.magic_damage *= 0.25 * trainer.cunning
    print("Critical Strike!")
    if environment.environment.visibility == "Bad" or environment.environment.visibility == "Blind":
        dragon.speed += 5
    if environment.environment.weather == "Storm" or environment.environment.weather == "Invisible":
        dragon.magic_damage += 5


def bend_will(trainer, enemy):
    chance_to_bend_will_1 = random.randint(0, 4)
    chance_to_bend_will_2 = random.randint(0, 4)
    if chance_to_bend_will_1 == chance_to_bend_will_2:
        print("Gol Hah Dov!")
        trainer.dragons.append(enemy)
        trainer.bend_will_convert(enemy)


def zii_los_dii_du(trainer, dragon, attack_type):
    if trainer.lives <= 0 and Miraak.resurrection_count != 1:
        print("Zii Los Dii Du")
        trainer.lives += 1
        dragon.attack_types[attack_type] = 10000
        Miraak.resurrection_count = 1
    else:
        print("Miraak Slain")


def flight_of_the_valkyrie(dragon, attack_type, enemy):
    if enemy.speed < dragon.speed:
        print("I shall run you in circles!")
        dragon.speed += 5
    else:
        print("So you have chosen violence...")
        dragon.attack_types[attack_type] += 2


def angmars_dominion(dragon, attack_type, enemy):
    for _ in Isildur.dragons_slain:
        dragon.attack_types[attack_type] += 10
        print("The foul kingdom should rise again!")
    if (enemy.health - dragon.attack_types[attack_type]) <= 0:
        Isildur.dragons_slain.append(enemy)


def the_dragonborn_king(trainer, dragon, enemy):
    if dragon.health > enemy.health:
        dragon.health += 300
        print("Lord of the Dragonguard")
    else:
        trainer.attribute_add()
        print("Legends of Akavir empower me...")


def founder_of_the_first_empire(trainer):
    for j in range(trainer.rounds_played):
        trainer.dragon_level_up_choice()


def chimarmavidium(trainer, attack_type):
    if trainer.lives <= 0:
        trainer.lives += 1
        print("The Heart of Lorkhan Prevails")
        for dragons in trainer.dragons:
            dragons.health += 100
            dragons.attack_types[attack_type] += 5
            dragons.attack_speed += 5
            dragons.size += 5
            dragons.eyesight.replace(dragons.eyesight, "All-Seeing")
            dragons.camouflage.replace(dragons.camouflage, "Invisible")
            dragons.intelligence.replace(dragons.intelligence, "All-Knowing")


def saint_nerevar_moon_and_star(trainer):
    stars = 0
    print("Nerevar at Red MOUNTAIN!!!")
    for items in all_trainers:
        for _ in items.dragons:
            stars += 5
    for my_dragons in range(stars):
        for my_dragon in trainer.dragons:
            trainer.level_up_dragon(my_dragon)


def special_attributes_unique_run(dragon, trainer, attack_type, enemy):
    if trainer.name == "Hiccup":
        toothless(dragon, trainer, attack_type)
    elif trainer.name == "Miraak":
        bend_will(dragon, trainer)
        zii_los_dii_du(trainer, dragon, attack_type)
    elif trainer.name == "Astrid":
        flight_of_the_valkyrie(dragon, attack_type, enemy)
    elif trainer.name == "Isildur":
        angmars_dominion(dragon, attack_type, enemy)
    elif trainer.name == "Reman Cyrodiil":
        the_dragonborn_king(trainer, dragon, enemy)
    elif trainer.name == "Tiber Septim":
        founder_of_the_first_empire(trainer)
        chimarmavidium(trainer, attack_type)
    elif trainer.name == "Indoril Nerevar":
        saint_nerevar_moon_and_star(trainer)
