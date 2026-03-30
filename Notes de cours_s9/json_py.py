import json

with open("Notes de cours_s9/json.json", "r", encoding="utf-8") as mon_fichier:
    data = json.load(mon_fichier)

print(data)