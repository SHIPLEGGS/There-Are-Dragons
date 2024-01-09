class Dragon:
    def __init__(self, name, speed, attack_speed, attack_damage, eyesight, size, camouflage, intelligence):
        self.name = name
        self.speed = speed
        self.attack_speed = attack_speed
        self.attack_damage = attack_damage
        self.magic_damage = attack_damage
        self.eyesight = eyesight
        self.size = size
        self.camouflage = camouflage
        self.intelligence = intelligence
        self.health = 300
        self.attack_modifiers = [self.size, self.attack_damage]
        self.speed_modifiers = [self.size, self.speed, self.attack_speed]


Rongwield = Dragon("Rongwield", 1, 2, 4, "Good", 5, "Black", "Average")
Gerhardt = Dragon("Gerhardt", 1, 2, 2, "Bad", 4, "Black", "Dumb")
Wunduniik = Dragon("Wuunduniik", 3, 4, 2, "Good", 3, "Grey", "Smart")
Vesper = Dragon("Vesper", 4, 3, 1, "Moderate", 1, "White", "Smart")
Sahlokaniir = Dragon("Sahlokaniir", 1, 2, 2, "Good", 2, "Grey", "All-Knowing")
Fenriir = Dragon("Fenriir", 3, 3, 2, "Blind", 1, "Invisible", "Average")
Aarensfjior = Dragon("Aarensfjior", 2, 1, 3, "All-Seeing", 3, "Grey", "Average")
Haelgir = Dragon("Haelgir", 2, 1, 3, "Moderate", 2, "White", "Dumb")
Ilkriim = Dragon("Ilkriim", 3, 3, 2, "Moderate", 2, "Black", "Dumb")
Norghar = Dragon("Norghar", 2, 1, 3, "Bad", 2, "White", "Idiot")
Thoralde = Dragon("Thoralde", 1, 2, 2, "Bad", 4, "Grey", "Average")
Ywennen = Dragon("Ywennen", 2, 1, 3, "Good", 3, "Grey", "Smart")
