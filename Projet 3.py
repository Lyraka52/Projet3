class Voiture:
    def __init__(self, immatriculation:str, marque:str, nom_prop:str,abonne:bool):
        self.immatriculation = immatriculation
        self.marque = marque
        self.nom_prop = nom_prop
        self.abonne = abonne

    def place(self):
        if self.abonne == False:
            return None
        else:
            return