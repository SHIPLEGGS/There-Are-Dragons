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

    def choice_increment(self, restart):
        self.choice -= restart
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
            print(trainer.beginner_trainers[i].name, " : ", self.choice_increment(0))
            for j in trainer.beginner_trainers[i].dragons:
                print("  " + "Dragons: ")
                print("  " + j.name + "\n")
                j.get_dragon_attributes()
                print("")
        while choice == 0:
            print("Your choice: ")
            your_choice = input(" ==> ")
            for j in range(len(options)):
                if your_choice == str(j):
                    self.trainer.strength = options[j].strength
                    self.trainer.speed = options[j].speed
                    self.trainer.cunning = options[j].cunning
                    self.trainer.name = self.trainer.name.replace("", options[j].name)
                    choice = 1
            if choice == 1:
                print("You Chose: " + self.trainer.name)
            else:
                print("That is not a valid option, try again.")

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
    def run_round(self):
        for i in range(len(trainer.all_trainers)):
            choice = random.randint(0, i)

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


user = User()
user.launch_game()
