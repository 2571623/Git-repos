class Personne:
    def __init__(self, prenom, nom, age):
        print("Initialisation de la classe Personne")
        self.prenom = prenom
        self.nom = nom
        self.age = age

    def dire_bonjour(self):
        return f"Bonjour, je m'appelle {self.prenom} {self.nom} et j'ai {self.age} ans."
