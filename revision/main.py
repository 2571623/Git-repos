from oop import Foo, MonException
from fichier import get_data

def main():
    print("Examen praitque, c'est bientôt les vacances !")
    try:
        f = Foo("Foo", 2)
        print(f)
    except Exception as e:
        print(e)
    except ValueError as e:
        print("Oups .....")
        print(e)
    except Exception as e:
        print("Ah bin là, ça va vraiment pas !")
        print(e)
    
    data = get_data("config/fichier1.json")
    print(data)

if __name__ == "__main__":
    main()