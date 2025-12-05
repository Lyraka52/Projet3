import random

marques = ["Renault", "Peugeot", "Citroën", "Opel", "Volkswagen","Toyota", "BMW", "Mercedes", "Audi", "Ford","Nissan", "Hyundai", "Fiat", "Dacia","Honda", "Mazda", "Volvo", "Tesla"]


class Voiture:
    """Créer une classe voiture"""
    def init(self, immatriculation, marque, proprietaire, abonne):
        """Le constructeur prend en argument l'immatriculation, la marque, le proproétaire de la voiture et si il est abonné ou non"""
        self.immatriculation = immatriculation
        self.marque = marque
        self.proprietaire = proprietaire
        self.abonne = abonne
        self.place = None

    def afficher(self):
        """Affiche les informations de la voiture"""
        print("Immatriculation :", self.immatriculation)
        print("Marque :", self.marque)
        print("Propriétaire :", self.proprietaire)
        print("Abonné :", self.abonne)
        print("Place attribuée :", self.place)

class Parking:
    """Créer une classe parking"""
    def __init__(self):
        self.places = [None] * 480
        self.abonnes = []

    def abonner(self, voiture, numero_place):
        """Regarde si le propriétaire est abonné ou non pour lui attributer une place"""
        if voiture.abonne == False:
            print("Le propriétaire n'est pas abonné.")
        elif voiture.abonne == True:
            voiture.place = numero_place
            self.abonnes.append(voiture)

    def place_libre(self, numero_place):
        """Vérifie si la place est libre ou non"""
        return self.places[numero_place - 1] is None

    def garer(self, voiture, numero_place):
        """Place une voiture à une place donnée"""
        if self.place_libre(numero_place):
            self.places[numero_place - 1] = voiture
        else:
            print("La place est déjà prise.")

    def voiture_a_la_place(self, numero_place):
        return self.places[numero_place - 1]

marque_aleatoire2 = random.choice(marques)
v2 = Voiture("XY-987-ZT", marque_aleatoire2, "Bob", False)
