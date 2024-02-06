from personage import *
from magicien import  *
from RoiSorcier import *
import random
def demarrerCombat(Magicien, RoiSorcier):
    print("au debut du combat voici les  stats de vos personnages :")
    print("le magicien a ", Magicien.vie)
    print("le roi a  ", RoiSorcier.vie)
    qui_commence = random.choice(["roi", "mag"])
    print("le joueure qui commence est ", qui_commence)
    while Magicien.vie >=0 and RoiSorcier.vie > 0:
        #On commence par le tour du Magicien

        esquive= random.choice(["oui","oui","non","non","non","non","non","non"])


        if esquive == "oui":
            print("le roi à esquiver l'attque")
            pass
        else:
            Magicien.attaque(RoiSorcier)

        esquive1= random.choice(["oui","oui","non","non","non","non","non","non"])

        if esquive1 == "oui":
            print("le magicien à esquiver l'attaque")
            pass
        else:
            RoiSorcier.attaque(Magicien)




    

        print("le mag a ", Magicien.vie)
        print("le roi a ", RoiSorcier.vie)

    
    if  Magicien.vie < RoiSorcier.vie:
        print("le gaganat est ROI")
    else:
        print("le gagant est le magicien")

        



#pour gerer le tour pair roi impaire Magicien