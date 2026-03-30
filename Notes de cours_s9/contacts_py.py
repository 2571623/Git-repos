import json

with open("Notes de cours_s9/contacts.json", "r", encoding="utf-8") as mon_fichier:
    data = json.load(mon_fichier)

for contact in data:
    print(f"Nom : {contact['nom']}")
    print(f"Courriel : {contact['email']}")
    if len(contact["telephones"]) > 1:
        print(f"Plus de un numéro de téléphone : {contact['nom']}")