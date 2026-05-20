import json

def get_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)
    return donnees

    """ 
    with remplace 
    f = open('donnees.json', 'r' , 'encoding=utf-8')
    try:
        donnees = json.load(fichier)
    finally:
        f.close
    """

