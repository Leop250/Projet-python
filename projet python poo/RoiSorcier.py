from magicien import *
from personage import *
import random

class RoiSorcier(Personnage):
    FORCE_FRAPPE_1 = 5
    FORCE_FRAPPE_2 = 20

    def __init__(self, nom, vie, force, degats, tour="jouerre1"):
        # Appel du constructeur de la classe parent (Personnage)
        super().__init__(nom, vie, force, degats, tour)
        
    def rappeAvecSonEpee(self, adversaire):
        adversaire.recoitDegat(self, self.FORCE_FRAPPE_1)
        self.FORCE_FRAPPE_1 +=1
        print("l'attaque rappeAvecSonEpee à augmnté de 1 est ", self.FORCE_FRAPPE_1)

    

    def attaqueAvecSonNazgul(self, adversaire):
        adversaire.recoitDegat(self, self.FORCE_FRAPPE_2)
        self.FORCE_FRAPPE_2 +=1
        print("lattaque son Nazghul à augmenté de 1",self.FORCE_FRAPPE_2)
    
    def attaque(self, adversaire):
        attaque_possible = ["rappeAvecSonEpee", "attaqueAvecSonNazgul"]
        choix = random.choice(attaque_possible)
        if choix == "rappeAvecSonEpee":
            self.rappeAvecSonEpee(adversaire)
            print("jutilise l'attaque rappeAvecSonEpee")
        elif choix == "attaqueAvecSonNazgul":
            self.attaqueAvecSonNazgul(adversaire)
            print("jutilise l'attaque  attaqueAvecSonNazgul")


        

