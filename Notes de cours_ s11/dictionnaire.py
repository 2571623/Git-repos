liste = [("cle1", "toto"), ("cle2", 2.78), ("cle3", 42), ("cle4", True)]

class Foo:
    def __init__(self, x: int, nom: str):
        self._x = x
        self._nom = nom

    @property
    def nom(self):
        return self._nom
    
    def __hash__(self):
        return hash((self._x, self._nom))
    
    
class DictListeTuple:
    def __init__(self):
        self._liste_tuples = []

    def __len__(self):
        return len(self._liste_tuples)
    
    def __str__(self):
        return "{" + ", ".join(f"{cle}: {valeur}" for cle, valeur in self._liste_tuples) + "}"
    
    def ajouter(self, cle, valeur):
        for i, (c ,v) in enumerate(self._liste_tuples):
            if c == cle:
                self._liste_tuples[i] = (cle, valeur)
                return

        self._liste_tuples.append((cle, valeur))

dico = DictListeTuple()
dico.ajouter("cle1", "toto")
dico.ajouter("cle1", "toto")

print(dico)