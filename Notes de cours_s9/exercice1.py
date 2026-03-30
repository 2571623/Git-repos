with open("Notes de cours_s9/poeme.txt", "r", encoding="utf-8") as mon_fichier:

    caractere = mon_fichier.read()
    lignes = caractere.splitlines()
    n_mots = caractere.split()

    print(f"Le poème contient {len(lignes)} lignes.")
    print(f"Le poème contient {len(caractere)} caractères.")
    print(f"Le poème contient {len(n_mots)} mots.")