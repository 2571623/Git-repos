from arbre import Node
class Fichier:
    def __init__(self,)

class Dossier:
    def __init__(self, nom):
        self.nom = nom
        self.children = []

    def add_child(self, nom):
        node = Dossier(nom)
        self.children.append(node)
        return node
    
    def add_file(self, nom):
        node = Fichier(nom)
        self.children.append(node)
        return node