from dragon import Rongwield
from special_attribute import Toothless, Miraak_Shout, Bend_Will, Valkyrie, Nazgul, Dragonborn_King, Tiber_1, Tiber_2, \
    Indoril
from trainer import Trainer

Hiccup = Trainer("Hiccup", 0, 4, 15)
Hiccup.special_attributes.append(Toothless)

Miraak = Trainer("Miraak", 4, 3, 8)
Miraak.special_attributes.append(Miraak_Shout)
Miraak.special_attributes.append(Bend_Will)

Astrid = Trainer("Astrid", 4, 10, 6)
Astrid.special_attributes.append(Valkyrie)

Isildur = Trainer("Isildur", 8, 6, 6)
Isildur.special_attributes.append(Nazgul)

Reman_Cyrodiil = Trainer("Reman Cyrodiil", 7, 7, 7)
Reman_Cyrodiil.special_attributes.append(Dragonborn_King)

Tiber_Septim = Trainer("Tiber Septim", 12, 10, 12)
Tiber_Septim.special_attributes.append(Tiber_1)
Tiber_Septim.special_attributes.append(Tiber_2)

Nerevar = Trainer("Indoril Nerevar", 0, 0, 0)
Nerevar.special_attributes.append(Indoril)

all_trainers = [Hiccup, Miraak, Astrid, Isildur, Reman_Cyrodiil, Tiber_Septim, Nerevar]

print(Rongwield.speed)
Isildur.speed_modify(Rongwield)
Isildur.attack_modify(Rongwield)
