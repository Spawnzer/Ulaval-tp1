import math

#Custom fn to deal with pesky edge cases like "--50",wrapping it up in a try/catch seems to do it
def is_digit(n):
     try:
          float(n)
          return True
     except ValueError:
          return False

def conversion_celsius():
    temp = input("Entrez la temperature en Farhenheit:")
    while (is_digit(temp) == False):
          temp = input("Entrez une temperature en Farhenheit valide:")
    print(f"La temperature en Celcius est: " + str(((float(temp) - 32)* (5/9))))

def calculer_aire():
    radius = input("Entrez le rayon du cercle:")
    while (is_digit(radius) == False or float(radius) <= 0):
          radius = input("Entrez un rayon valide:")
    print("L'aire du cercle est de " + str(float(radius) ** 2 * math.pi))  

def validate_note(note):
    return True if is_digit(note) and 0 <= float(note) <= 100 else False

def calculate_final_note(notes):
    return ((notes[0] * 0.15) + (notes[1] * 0.30) + (notes[2] * 0.55))

def calculer_note():
    notes = []
    i = 0
    while (i < 3):
        note = input("Entrez une note sur 100:")
        while (not validate_note(note)):
            note = input("Entrez une note valide sur 100:")
        notes.append(float(note))
        i = i + 1
    print(f"{float(calculate_final_note(notes)):4.1f}%")  

def calculer_stationnement():
    cout = 0
    heure = input("Entrez votre temps d'utilisation du stationnement: ")
    while (heure.isnumeric() == False or int(heure) < 0):
        heure = input("Entrez un temps de stationnement valide: ")
    cout = int((int(heure) / 24)) * 12
    restant = int(heure) % 24
    cout = (cout + 5) if restant >= 3 else 0
    if restant >= 3:
        restant = restant - 3
    cout = cout + restant if restant < 7 else cout + 7
    print(f"{cout}$") 
    
def validate_input_int(datum):
     return True if datum.isnumeric() and int(datum) >= 0 else False

def validate_input_float(datum):
     return True if is_digit(datum) and float(datum) >= 0 else False

def calculer_cout(conso, passager, distance, prix):
     return (((distance/100) * conso) * (1+(passager * 0.05)) * prix)

def calculer_cout_voyage():
     conso = input("Veuillez entrer la consommation du vehicule en L/100Km.")
     while (not validate_input_float(conso)):
          conso = input("Veuillez entrer une consommation en L/100Km valide (>=0)")
     passager = input("Veuillez entrer le nombre de passagers (excluant le chauffeur).")
     while (not validate_input_int(passager)):
          passager = input("Veuillez entrer un nombre de passagers (excluant le chauffeur) valide (>=0).")
     distance = input("Veuillez entrer la distance de la destination.")
     while (not validate_input_float(distance)):
          distance = input("Veuillez entrer une distance en Km valide (>=0).")
     prix = input("Veuillez entrer le prix d'un litre d'essence en dollars.")
     while (not validate_input_float(prix)):
          prix = input("Veuillez entrer un prix au litre valide (>=0)")
     coutAller = calculer_cout(float(conso), int(passager), float(distance), float(prix))
     coutRetour = coutAller * 2
     print(f"Distance :   {distance} KM \n"
               f"Nombre de passager :   {passager} \n"
               f"Consommation du vehicule :   {conso}L/100Km \n"
               f"Prix de l'essence :   {prix}$/L \n\n"
               "--Pour l'aller--\n"
               f"Litre d'essence consommes :   {((float(distance)/100) * float(conso)) * (1+(int(passager) * 0.05)):1.2f}L\n"
               f"Cout :   {coutAller:1.2f} $\n"
               "--Pour l'aller retour--\n"
               f"Litre d'essence consommes :   {(((float(distance)/100) * float(conso)) * (1+(int(passager) * 0.05))*2):1.2f}L\n"
               f"Cout :   {coutRetour:1.2f} $\n"
            )

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
