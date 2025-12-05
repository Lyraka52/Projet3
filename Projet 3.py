import random

marques = ["Renault", "Peugeot", "Citroën", "Opel", "Volkswagen","Toyota", 
           "BMW", "Mercedes", "Audi", "Ford","Nissan", "Hyundai", "Fiat", 
           "Dacia","Honda", "Mazda", "Volvo", "Tesla"]


class Voiture:
    """Créer une classe voiture"""
    def __init__(self, immatriculation, marque, proprietaire, abonne):
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
        voiture.abonne = True
        voiture.place = numero_place
        self.abonnes.append(voiture)
        self.places[numero_place - 1] = voiture

    def annuler_abonnement(self, voiture):
        """Annule l’abonnement d’une voiture."""
        if voiture in self.abonnes:
            # libérer la place réservée
            if voiture.place is not None:
                self.places[voiture.place - 1] = None
            voiture.abonne = False
            voiture.place = None
            self.abonnes.remove(voiture)

    def place_libre(self, numero_place):
        return self.places[numero_place - 1] is None

    def garer(self, voiture, numero_place):
        """Gare une voiture sur une place normale."""
        if self.place_libre(numero_place):
            self.places[numero_place - 1] = voiture
        else:
            print("La place est déjà prise.")

    def voiture_a_la_place(self, numero_place):
        return self.places[numero_place - 1]

    def places_abonnes_occupees_par_autres(self):
        """Renvoie la liste des places réservées à des abonnés mais occupées par une autre voiture."""
        res = []
        for v in self.abonnes:
            if v.place is not None:
                place = v.place
                # la place existe mais n’a pas la bonne voiture
                if self.places[place - 1] != v:
                    res.append(place)
        return res

    def nb_places_libres_sans_abonnes(self):
        """Nombre de places libres en excluant les places réservées aux abonnés."""
        places_reservees = {v.place for v in self.abonnes if v.place is not None}

        compteur = 0
        for i in range(1, 481):
            if i not in places_reservees and self.place_libre(i):
                compteur += 1
        return compteur

    def afficher_niveau(self, niveau):
        """Affiche un niveau sous forme graphique : 
        - 80 places par niveau
        - '-' = place libre
        - '*' = place occupée"""
        print(f"\n=== Niveau {niveau} ===")

        debut = (niveau - 1) * 80
        fin = debut + 80
        ligne = ""
        for i in range(debut, fin):
            if self.places[i] is None:
                symbole = "."
            else:
                symbole = "X"
            ligne += symbole + " | "

        print(ligne)

p = Parking()

v1 = Voiture("AA-111-AA", random.choice(marques), "Alice", False)
v2 = Voiture("BB-222-BB", random.choice(marques), "Bob", False)
v3 = Voiture("CC-333-CC", random.choice(marques), "Chris", False)

# Abonner une voiture (v1 à la place 120)
print("\n--- Abonnement ---")
p.abonner(v1, 120)
v1.afficher()

# Garer v2 sur une place normale
print("\n--- Garer une voiture ---")
p.garer(v2, 50)

# Garer v3 sur la place d’un abonné pour tester la fonction
p.garer(v3, 120)

# Afficher niveau 2 (places 81 à 160)
print("\n--- Niveau 2 ---")
p.afficher_niveau(2)
p.afficher_niveau(5)

# Vérifier les places d'abonnés occupées par d'autres voitures
print("\n--- Places abonnés occupées par d'autres voitures ---")
print(p.places_abonnes_occupees_par_autres())

# Nombre de places libres hors abonnés
print("\n--- Nombre de places libres (hors abonnés) ---")
print(p.nb_places_libres_sans_abonnes())
