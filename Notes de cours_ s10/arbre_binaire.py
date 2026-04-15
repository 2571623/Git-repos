class Eleve:
    def __init__(self, nom, prenom, matricule):
        self.nom = nom
        self.prenom = prenom
        self.matricule = matricule

    def __lt__(self, other):
        print(self.nom)
        return self.matricule < other.matricule
    
    def __eq__(self, other):
        return self.matricule == other.matricule

    
class NoeudABR:
    def __init__(self, valeur):
        self.valeur = valeur
        self.gauche = None
        self.droite = None