
class Personnage:
    def __init__(self, nom,vie,force, degats, tour="jouerre1",):
        self.__nom = nom
        self.__vie = 100
        self.__force= force
        self.__degats= degats
        Personnage.tour = "jouerre1"
        pass
    
    def frappe(perso, force_frapp):
        pass

    @ property
    def nom(self):
        return self.__nom

    @ nom.setter
    def set_nom(self, new_nom):
        if type(self.nom)== str:
            self.__nom= new_nom
        else:
            print("type imcompatible")
    
    @property
    def vie(self):
        return self.__vie
    
    @vie.setter
    def set_vie(self, new_vie):

        if type(self.vie)== int:
            self.__vie= new_vie
        else:
            print("type imcompatible")
    
    @property
    def degats(self):
        return self.__degats
    
    @ degats.setter
    def degat_setter(self, new_degats):
        if type(self.__degats) == float:
            self.__degats = new_degats
        else:
            print("type incompatible")
    
    @property
    def force(self):
        return self.__force
    @ force.setter
    def force_setter(self, new_force):
        if type(self.__force)== float:
            self.__force = new_force
        else:
            print("type incompatible")
        

        
    @property
    def degar(self):
        return self.__degats
    @ force.setter
    def force_setter(self, new_degats):
        if type(self.__degats)== float:
            self.__degats = new_degats
        else:
            print("type incompatible")

    """
        # Getters
    def get_nom(self):
        return self.__nom

    def get_vie(self):
        return self.__vie

    def get_force(self):
        return self.__force

    def get_experience(self):
        return self.__experience

    def get_degats(self):
        return self.__degats

    # Setters
    def set_nom(self, nom):
        self.__nom = nom

    def set_vie(self, vie):
        self.__vie = vie

    def set_force(self, force):
        self.__force = force

    def set_experience(self, experience):
        self.__experience = experience

    def set_degats(self, degats):
        self.__degats = degats
    """

    
    def frappe(self,jouerre1, degat):
        self.jouerre1.vie -= degat
    
    def esquive(self):
        print("vous avez esuivez bravo")
    
    def recoitDegat(self,adersaire, force):
        self.__degats += force
        self.__vie -= force

    
    """
        def set_degats(self, degats):
        self.__degats = degats

    # Méthodes
    def frappe(self, cible, force_frappe):
        cible.recoit_degat(self, force_frappe)

    def esquive(self):
        # Logique d'esquive
        print(f"{self.__nom} esquive l'attaque!")

    def recoit_degat(self, adversaire, force_frappe):
        self.__degats += force_frappe
        self.__vie -= force_frappe
    """
    


