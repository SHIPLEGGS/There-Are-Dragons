The Game is simply run by creating a new user object (user = User()) and then calling launch game (user.launch_game()),
its that easy, it is entirely scalable so any number of dragons and or trainers can be added without rewrites, all calculation algorithms for damage, leveling etc. are modular and can 
be edited easily from the trainer or dragon class.
The run_round() method in play_game.py is intentionally unoptimized as is much other code, the project is intended to showcase what can be achieved solely with the fundamentals of python
and OOP design.
