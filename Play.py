import random

def shifumi():
    print("Choisissez :")
    print("1. Pierre")
    print("2. Feuille")
    print("3. Ciseaux")

    choix = int(input("Votre choix (1/2/3) : "))

    if choix not in [1, 2, 3]:
        print("Choix invalide. Veuillez choisir 1, 2 ou 3.")
        return

    options = {1: "Pierre", 2: "Feuille", 3: "Ciseaux"}
    choix_joueur = options[choix]
    choix_ordi = options[random.randint(1, 3)]

    print(f"Vous avez choisi : {choix_joueur}")
    print(f"L'ordinateur a choisi : {choix_ordi}")

    if choix_joueur == choix_ordi:
        print("Égalité !")
    elif (choix_joueur == "Pierre" and choix_ordi == "Ciseaux") or \
         (choix_joueur == "Feuille" and choix_ordi == "Pierre") or \
         (choix_joueur == "Ciseaux" and choix_ordi == "Feuille"):
        print("Vous avez gagné !")
    else:
        print("L'ordinateur a gagné !")

# Appel de la fonction pour jouer
shifumi()
