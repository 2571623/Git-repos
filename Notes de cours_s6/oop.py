age = 30
nom = "Alice"
travail = "Exploratrice"

def se_presenter(nom, age, travail):
    return f"Bonjour, je m'appelle {nom}, j'ai {age} ans et je suis {travail}."

def est_majeur(age):
    return age >= 18

#print(se_presenter)

# Version avec une liste

AGE = 0 
NOM = 1
TRAVAIL = 2
SE_PRESENTER = 3
EST_MAJEUR = 4

alice = [None,30, "Alice", "Exploratrice", se_presenter, est_majeur]
bob = [None,17, "Bob", "Apprenti", se_presenter, est_majeur]
henry = [None,25, "Henry", "Scientifique", se_presenter, est_majeur]

# Heritage avec une liste
PARENT = 0


# Une autre "classe" sous forme de liste : etudiant
ECOLE = 1
MOYENNE = 2

jacques = [[None,18, "Jacques", "TUTEUR", se_presenter, est_majeur], "College de Maisonneuve", 82]

print(jacques[PARENT][NOM])

# Version avec une classe

class Personne:
    def __init__(self, nom, age, travail):
        self.nom = nom
        self.age = age
        self.travail = travail

    def se_presenter(self):
        return f"Bonjour, je m'appelle {self.nom}, j'ai {self.age} ans et je suis {self.travail}."

    def est_majeur(self):
        return self.age >= 18
    
alice_class = Personne("Alice", 30, "Exploratrice")
print(dir(alice_class))
classe_de_alice = alice_class.__class__

#possede_methode_se_presenter = "se_presenter" in dir(alice_class)
possede_methode_se_presenter = hasattr(alice_class, "se_presenter")
print(possede_methode_se_presenter)
