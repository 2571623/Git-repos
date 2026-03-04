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

jacques = {"parent": {"nom": "Jacques", "age": 18, "travail": "TUTEUR", "se_presenter": se_presenter, "est_majeur": est_majeur}, "ecole": "College de Maisonneuve", "moyenne": 82}

def appelle_methode_ou_attribut(obj, nom):
    if nom in obj:
        methode = obj[nom]
        print(methode)
    elif "parent" in obj and nom in obj["parent"]:
        methode = obj["parent"][nom]
        print(methode)
    else:
        print(f"Erreur : la méthode {nom} n'existe pas dans l'objet.")

appelle_methode_ou_attribut(jacques, "nom")

# Polymorphisme

chien = {"nom": "Rex"}

appelle_methode_ou_attribut(chien, "nom")