with open("Notes de cours_s9/poeme.txt", "r", encoding="utf-8") as mon_fichier:

    caractere = mon_fichier.read()
    lignes = caractere.splitlines()
    n_mots = len(caractere.split())

    print(len(lignes))
    print(len(caractere))
    print(n_mots)