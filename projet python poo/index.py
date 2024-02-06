from combat import demarrerCombat
from personage import *
from magicien import  *
from RoiSorcier import *


roi_sorcier = RoiSorcier(nom="Roi Sorcier", vie=1500, force=25, degats=12)
magicien = Magicien(nom="Mag", vie=100, force=20, degats=5)

# Lancement du combat
demarrerCombat(magicien, roi_sorcier)


