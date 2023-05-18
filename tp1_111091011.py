import math

#Custom fn to deal with pesky edge cases like "--50",wrapping it up in a try/catch seems to do it
def is_digit(n):
     try:
          int(n)
          return True
     except ValueError:
          return False

def conversion_celsius():
    temp = input("Entrez la temperature en Farhenheit:")
    while (is_digit(temp) == False):
          temp = input("Entrez une temperature en Farhenheit valide:")
    print("La temperature en Celcius est: " + str(((int(temp) - 32)* (5/9))))

def calculer_aire():
    radius = input("Entrez le rayon du cercle:")
    while (radius.isnumeric() == False or int(radius) <= 0):
          radius = input("Entrez un rayon valide:")
    print("L'aire du cercle est de " + str(int(radius) ** 2 * math.pi))  

def validate_note(note):
    return True if note.isnumeric() and 0 <= int(note) <= 100 else False

def calculate_final_note(notes):
    return ((notes[0] * 0.15) + (notes[1] * 0.30) + (notes[2] * 0.55))

def calculer_note():
    notes = []
    i = 0
    while (i < 3):
        note = input("Entrez une note sur 100:")
        while (not validate_note(note)):
            note = input("Entrez une note valide sur 100:")
        notes.append(int(note))
        i = i + 1
    print(int(calculate_final_note(notes)))  

def calculer_stationnement():
    cout = 0
    heure = input("Entrez votre temps d'utilisation du stationnement: ")
    while (heure.isnumeric() == False and int(heure) < 0):
        heure = input("Entrez un temps de stationnement valide: ")
    cout = int((int(heure) / 24)) * 12
    restant = int(heure) % 24
    cout = (cout + 5) if restant >= 3 else 0
    if restant >= 3:
        restant = restant - 3
    cout = cout + restant if restant < 7 else cout + 7
    print(f"{cout}$") 

def calculer_cout_voyage():
    answer = input("Votre choix: ")

def afficher_menu():
    print(  "Faites un choix parmi les options suivantes:\n\n"
            "A. Convertir Fahrenheit en Celsius\n"
            "B. Calculer Aire cercle\n"
            "C. Calculer et afficher note finale\n"
            "D. Calculer et afficher le montant pour le stationnement\n"
            "E. Calculer le cout d'un voyage\n"
            "M. Réafficher les options du menu.\n"
            "Q. Quitter le programme.\n\n"
            )
def main():
    afficher_menu()
    while True:
        answer = input("Votre choix: ").upper()
        if answer == "A":
            conversion_celsius()
        elif answer == "B":
            calculer_aire()
        elif answer == "C":
            calculer_note()
        elif answer == "D":
            calculer_stationnement()
        elif answer == "E":
            calculer_cout_voyage()
        elif answer == "M":
            afficher_menu()
        elif answer == "Q":
            break
        else:
            print("Ceci n'est pas un choix valide, reesayez\n")
            afficher_menu()

if __name__ == "__main__":
    main()