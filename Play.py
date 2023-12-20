import random

def shifumi():
    options = {1: "Pierre", 2: "Feuille", 3: "Ciseaux"}
    
    while True:
        print("Choisissez :")
        print("1. Pierre")
        print("2. Feuille")
        print("3. Ciseaux")

        choix = input("Votre choix (1/2/3) : ")

        if choix not in options:
            print("Choix invalide. Veuillez choisir 1, 2 ou 3.")
            continue

        choix_joueur = options[int(choix)]
        choix_ordi = options[random.randint(1, 3)]

        print(f"Vous avez choisi : {choix_joueur}")
        print(f"L'ordinateur a choisi : {choix_ordi}")

        if choix_joueur == choix_ordi:
            print("Égalité !")
        elif (choix_joueur, choix_ordi) in [("Pierre", "Ciseaux"), ("Feuille", "Pierre"), ("Ciseaux", "Feuille")]:
            print("Vous avez gagné !")
        else:
            print("L'ordinateur a gagné !")

        reponse = input("Voulez-vous rejouer ? (1 pour oui / 2 pour non) : ")
        if reponse != '1':
            break

# Appel de la fonction pour jouer
shifumi()
