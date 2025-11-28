class Voiture:
    def __init__(self, immatriculation:str, marque:str, nom_prop:str,abonne:bool):
        self.immatriculation = immatriculation
        self.marque = marque
        self.nom_prop = nom_prop
        self.abonne = abonne 
    
class Parking:
    def __init__(self, abonnes:list):
        self.abonnes = abonnes
        places = []
