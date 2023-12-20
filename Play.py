from random import choice

def shifumi():
    while True:
        choix = input("1. Pierre\n2. Feuille\n3. Ciseaux\nVotre choix (1/2/3) : ")
        if choix not in ["1", "2", "3"]:
            break
        
        joueur, ordi = ("Pierre", "Feuille", "Ciseaux")[int(choix) - 1], choice(("Pierre", "Feuille", "Ciseaux"))
        resultat = "Égalité !" if joueur == ordi else "Vous avez gagné !" if ((joueur, ordi) in [('Pierre', 'Ciseaux'), ('Feuille', 'Pierre'), ('Ciseaux', 'Feuille')]) else "L'ordinateur a gagné !"
        print(f"Vous avez choisi : {joueur}\nL'ordinateur a choisi : {ordi}\n{resultat}")

        if input("Rejouer ? (1 pour oui / autre pour non) : ") != '1':
            break

# Appel de la fonction pour jouer
shifumi()
