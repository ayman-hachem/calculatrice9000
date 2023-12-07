historique = []  # historique des opérations

def addition(chiffres):
    resultat = sum(chiffres)
    operation = f"{' + '.join(map(str, chiffres))} = {resultat}"
    historique.append(operation)
    print(resultat)
    return resultat

def soustraction(chiffres):
    resultat = chiffres[0]
    for i in range(1, len(chiffres)):
        resultat -= chiffres[i]
    operation = f"{chiffres[0]} - { ' - '.join(map(str, chiffres[1:]))} = {resultat}"
    historique.append(operation)
    print(resultat)
    return resultat

def division(chiffres):
    if len(chiffres) > 1:
        resultat = chiffres[0]
        for i in range(1, len(chiffres)):
            if chiffres[i] != 0:
                resultat /= chiffres[i]
            else:
                print("Impossible de diviser par zéro.")
                return None
        operation = f"{chiffres[0]} / { ' / '.join(map(str, chiffres[1:]))} = {resultat}"
        historique.append(operation)
        print(resultat)
        return resultat
    else:
        print("Au moins deux chiffres sont nécessaires pour effectuer une division.")
        return None

def multiplication(chiffres):
    resultat = 1
    for chiffre in chiffres:
        resultat *= chiffre
    operation = f"{chiffres[0]} * { ' * '.join(map(str, chiffres[1:]))} = {resultat}"
    historique.append(operation)
    print(resultat)
    return resultat

def puissance(chiffres):
    base, exponent = chiffres
    resultat = base ** exponent
    operation = f"{base} ^ {exponent} = {resultat}"
    historique.append(operation)
    print(resultat)
    return resultat

def racine_carree(chiffres):
    chiffre = chiffres[0]
    resultat = chiffre ** 0.5
    operation = f"{chiffres[0]} sqrt = {resultat}"
    historique.append(operation)
    print(resultat)
    return resultat

def trigonometrie(chiffres):
    operation = chiffres[0].lower()
    angle = chiffres[1]
    if operation == 'sin':
        print("Fonction sin non implémentée.")
    elif operation == 'cos':
        print("Fonction cos non implémentée.")
    elif operation == 'tan':
        print("Fonction tan non implémentée.")
    else:
        print("Opération trigonométrique non valide.")
        return None

def reset():
    historique.clear()
    print("L'historique des opérations a été réinitialisé.")

def afficher_historique():
    print("Historique des opérations :")
    for i, operation in enumerate(historique, 1):
        print(f"{i}. {operation}")

def calculatrice():
    resultats = []
    chiffres = []
    while True:
        operation = input("Choisissez une opération (+, -, *, /, ^, sqrt, sin, cos, tan, reset) ou '=' pour quitter : ")
        if operation.lower() == '=':
            break
        elif operation in ['+', '-', '*', '/']:
            chiffres = [float(input("Entrez un chiffre : "))]
            while True:
                chiffre = input("Entrez un chiffre (ou '=' pour terminer) : ")
                if chiffre.lower() == '=':
                    break
                chiffres.append(float(chiffre))
            if operation == '+':
                resultats.append(addition(chiffres))
            elif operation == '-':
                resultats.append(soustraction(chiffres))
            elif operation == '*':
                resultats.append(multiplication(chiffres))
            elif operation == '/':
                resultat = division(chiffres)
                if resultat is not None:
                    resultats.append(resultat)
        elif operation == '^':
            chiffres = [float(input("Entrez la base : ")), float(input("Entrez l'exposant : "))]
            resultats.append(puissance(chiffres))
        elif operation.lower() == 'sqrt':
            chiffres = [float(input("Entrez un chiffre : "))]
            resultats.append(racine_carree(chiffres))
        elif operation.lower() in ['sin', 'cos', 'tan']:
            chiffres = [input(f"Entrez l'opération trigonométrique ({operation}) : ").lower(), float(input("Entrez l'angle en degrés : "))]
            trigonometrie(chiffres)  # Ajouter le résultat à la liste des résultats si nécessaire
        elif operation.lower() == 'reset':
            reset()
        else:
            print("Opération non valide. Veuillez choisir parmi les opérations disponibles.")

# Appel de la fonction calculatrice
calculatrice()
afficher_historique()
