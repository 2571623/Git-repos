import csv

#with open("Notes de cours_s9/data.csv", "r", encoding="utf-8") as mon_fichier:
#    texte = csv.reader(mon_fichier)
#    en_tete = next(texte)
#    position_planetes = en_tete.index("Nom planète")
#    for ligne in texte:
#        #print(ligne)
#        print(f"Planète : {ligne[position_planetes]}")

with open("Notes de cours_s9/data.csv", "r", encoding="utf-8") as mon_fichier:
    texte = csv.DictReader(mon_fichier)
    for ligne in texte:
        #print(ligne)
        print(f"Planète : {ligne['Nom planète']}")