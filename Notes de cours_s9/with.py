with open("Notes de cours_s9/fichier_texte.txt", "r", encoding="utf-8") as mon_fichier:

    texte = mon_fichier.read()

    print(texte)

    boom = 1 / 0

#except FileNotFoundError as e:
#    print("Le fichier n'existe pas.")
#    x = input("Attendre vraiment longtemps pour continuer ? (o/n) ")
