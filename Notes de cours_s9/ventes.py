import csv

with open("Notes de cours_s9/ventes.csv", "r", encoding="utf-8") as mon_fichier:
    data = list(csv.DictReader(mon_fichier))

    nb_transaction = 0
    chiffre_affaires = 0.0
    chiffre_affaires_par_produit = {}
for row in data:
    nb_transaction += 1
    print(row)
    chiffre_affaires_courant = float(row['Quantité']) * float(row['PrixUnitaire'])
    chiffre_affaires += chiffre_affaires_courant
    
    if row["Produit"] in chiffre_affaires_par_produit:
        chiffre_affaires_par_produit[row["Produit"]] = 0.0
    chiffre_affaires_par_produit[row["Produit"]] += chiffre_affaires_courant

print(f"Nombre total de transactions : {nb_transaction}")
print(f"Chiffre d'affaires total : {chiffre_affaires}")