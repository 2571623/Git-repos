from arbre import Node
class Fichier:
    def __init__(self, nom):
        self.nom = nom

    def __str__(self):
        return self.nom

class Dossier:
    def __init__(self, nom):
        self.nom = nom
        self.contenu : list[Fichier | Dossier] = []

    def ajouter(self, element):
        self.contenu.append(element)

    def __str__(self):
        return f"{self.nom}/"