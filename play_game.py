import random

import dragon
import trainer


def tutorial_run():
    choice = 0
    print("                          Welcome to the tutorial milk drinker\n")
    print("The game is controlled entirely by the number keys unless otherwise explicitly specified\n")
    print("You begin the game by choosing a trainer, you will receive a random selection of 3 from 5\n")
    print(" starter trainers. Each trainer comes with 3 dragons to begin the game, your dragons are\n")
    print("  essentially your lives, run out of dragons and the game is over. To win, be the last\n")
    print("                                dragon trainer standing.\n")
    print("                                    I understand: 1\n")
    while choice == 0:
        move_on = input(" ==> ")
        if move_on == "1":
            choice = 1
            pass
        elif move_on == "0":
            print("Your a slow bugger aren't you!")
        else:
            print("THAT IS NOT AN OPTION, READ THE TUTORIAL!")


class User:

    def __init__(self):
        self.user_name = None
        self.choice = -1
        self.trainer = trainer.Trainer(name="", strength=0, speed=0, cunning=0)
        self.friendly_intro = 0
        self.round_number = 1
        self.dragons = []
        self.failed_inputs = 0
        self.chosen_dragon = None

    def choice_increment(self):
        self.choice += 1
        return self.choice

    def game_setup(self):
        options = []
        choice = 0
        numbers = [0, 1, 2, 3, 4]
        random_numbers = random.sample(numbers, 3)
        dragon.assign_dragons()
        print("Choose one of the following trainers: \n")
        for i in random_numbers:
            options.append(trainer.beginner_trainers[i])
            print(trainer.beginner_trainers[i].name, " : ", self.choice_increment())
            for j in trainer.beginner_trainers[i].dragons:
                print("  " + "Dragons: ")
                print("  " + j.name + "\n")
                j.get_dragon_attributes()
                print("")
        self.choice = -1
        while choice == 0:
            print("Your choice: ")
            your_choice = input(" ==> ")
            for j in range(len(options)):
                if your_choice == str(j):
                    self.trainer.strength = options[j].strength
                    self.trainer.speed = options[j].speed
                    self.trainer.cunning = options[j].cunning
                    self.trainer.name = self.trainer.name.replace("", options[j].name)
                    self.trainer.dragons = options[j].dragons
                    trainer.beginner_trainers.remove(options[j])
                    trainer.all_trainers.remove(options[j])
                    choice = 1
            if choice == 1:
                print("You Chose: " + self.trainer.name)
            else:
                print("That is not a valid option, try again.")
                self.failed_inputs += 1

    def define_username(self):
        choice_input = 0
        while True:
            if choice_input == 0:
                choice_input = 1
                self.user_name = input("To begin, please enter a Username\n ==> ")
                if len(self.user_name) < 2 or len(self.user_name) > 8:
                    print("Usernames must be 2 to 8 characters long.")
                else:
                    choice_input = 2
            if choice_input == 1:
                self.user_name = input("Please enter a valid Username\n ==> ")
                if len(self.user_name) < 2 or len(self.user_name) > 8:
                    print("Usernames must be 2 to 8 characters long.")
                else:
                    choice_input = 2
            if choice_input == 2 or choice_input == 3:
                if choice_input == 2:
                    print("You have chosen: " + self.user_name)
                    print("To continue press \'1\'. To choose a different name press \'0\'.")
                username_confirm = input(" ==> ")
                if username_confirm == "1":
                    break
                elif username_confirm == "0":
                    choice_input = 1
                else:
                    print("Not a valid confirmation, \'0\' or \'1\', their is no \'3\'.")
                    choice_input = 3
                    self.failed_inputs += 1

    def run_round(self):
        if self.failed_inputs >= 3:
            print("Invalid inputs have exceeded the 3 idiot maximum. Terminating stupidity, get hands noob")
            exit()
        first_or_second = random.randint(0, 1)
        first_or_second_attack = random.randint(0, 1)
        choice = random.randint(0, len(trainer.all_trainers))
        choice_1 = random.randint(0, len(trainer.beginner_trainers))
        print("Round -- " + str(self.round_number))
        if self.friendly_intro < 2:
            opponent = trainer.beginner_trainers[choice_1]
            dragon_choice = random.randint(0, len(opponent.dragons))
            print(dragon_choice)
        else:
            opponent = trainer.all_trainers[choice]
            dragon_choice = random.randint(0, len(opponent.dragons))
        print("Your opponent is: " + opponent.name)
        if first_or_second == 0:
            print("They have chosen: " + opponent.dragons[dragon_choice].name)
            opponent.opponent = opponent.dragons[dragon_choice]
            opponent.dragons[dragon_choice].get_dragon_attributes()
        else:
            print("Which dragon would you like to pick: ")
            for i in self.dragons:
                print(i.name + str(self.choice_increment()))
                while True:
                    chose_dragon = input(" ==> ")
                    if i == self.dragons[int(chose_dragon)]:
                        self.chosen_dragon = i
                        print("You chose: " + self.dragons[int(chose_dragon)].name)
                        break
                    else:
                        print("You have not selected a valid option.")
                        self.failed_inputs += 1
        if first_or_second == 0:
            print("Which dragon would you like to pick: ")
            for i in self.dragons:
                print(i.name + str(self.choice_increment()))
                while True:
                    chose_dragon = input(" ==> ")
                    if i == self.dragons[int(chose_dragon)]:
                        self.chosen_dragon = i
                        print("You chose: " + self.dragons[int(chose_dragon)].name)
                        break
                    else:
                        print("You have not selected a valid option.")
                        self.failed_inputs += 1
        else:
            print("They have chosen: " + opponent.dragons[dragon_choice].name)
            opponent.opponent = opponent.dragons[dragon_choice]
            opponent.dragons[dragon_choice].get_dragon_attributes()

        if first_or_second_attack == 0:
            opponent_action = random.randint(0, 2)
            print("Your opponent engages!")
            if opponent_action == 0:
                print("Your opponents dragon has bitten " + self.chosen_dragon.name)
                opponent.speed_modify(opponent.opponent)
                opponent.attack_modify(opponent.opponent, 0)
                opponent.opponent.attack_bite(opponent, self.chosen_dragon)
            elif opponent_action == 1:
                print("Your oppents dragon challenges " + self.chosen_dragon.name + "s Thu'um")
                opponent.speed_modify(opponent.opponent)
                opponent.attack_modify(opponent.opponent, 1)
                opponent.opponent.attack_breath_fire(opponent, self.chosen_dragon)

            elif opponent_action == 2:
                print("You opponets strafes evasively ")
        else:
            print("Command your dragon!")
            print("Bite: 0\nVerbal Assault: 1\nDodge: 2")
            while True:
                action = input(" ==> ")
                if action == "0":
                    self.trainer.speed_modify(self.chosen_dragon)
                    self.trainer.attack_modify(self.chosen_dragon, 0)
                    self.chosen_dragon.attack_bite(self, opponent)
                    break
                elif action == "1":
                    self.trainer.speed_modify(self.chosen_dragon)
                    self.trainer.attack_modify(self.chosen_dragon, 1)
                    self.chosen_dragon.attack_breath_fire(self, opponent)
                    break
                elif action == "2":
                    break
                else:
                    print("Invalid option!")

    def launch_game(self):
        print("Welcome... to \'The Skies of Keizhal\'.")
        self.define_username()
        print("                  " +
              "Hello " + str(self.user_name) + "\n" +
              "     Would you like to play the Tutorial?\n" +
              "(0 for no I've got this, 1 for yes im a bitch).\n")
        tutorial_yes_no = input(" ==> ")
        if tutorial_yes_no == "1":
            tutorial_run()
        elif tutorial_yes_no == "0":
            print("That's what I like to hear! HAVE AT \'EM.")
            pass
        else:
            print("STOP TROLLING, I asked for 0 or 1\n Initiating punishment tutorial...\n")
            tutorial_run()
        self.game_setup()
        self.run_round()


user = User()
user.launch_game()
