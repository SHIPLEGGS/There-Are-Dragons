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
        self.attack_types = [self.attack_damage, self.magic_damage]


Rongwield = Dragon("Rongwield", 1, 2, 4, "Good", 5, "Black", 3)
Gerhardt = Dragon("Gerhardt", 1, 2, 2, "Bad", 4, "Black", 2)
Wunduniik = Dragon("Wuunduniik", 3, 4, 2, "Good", 3, "Grey", 4)
Vesper = Dragon("Vesper", 4, 3, 1, "Moderate", 1, "White", 4)
Sahlokaniir = Dragon("Sahlokaniir", 1, 2, 2, "Good", 2, "Grey", 5)
Fenriir = Dragon("Fenriir", 3, 3, 2, "Blind", 1, "Invisible", 3)
Aarensfjior = Dragon("Aarensfjior", 2, 1, 3, "All-Seeing", 3, "Grey", 3)
Haelgir = Dragon("Haelgir", 2, 1, 3, "Moderate", 2, "White", 2)
Ilkriim = Dragon("Ilkriim", 3, 3, 2, "Moderate", 2, "Black", 2)
Norghar = Dragon("Norghar", 2, 1, 3, "Bad", 2, "White", 1)
Thoralde = Dragon("Thoralde", 1, 2, 2, "Bad", 4, "Grey", 3)
Ywennen = Dragon("Ywennen", 2, 1, 3, "Good", 3, "Grey", 4)
