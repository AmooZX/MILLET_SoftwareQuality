import operator


# Fonction pour parser les nombres entrées par l'utilisateur d'un string à son type
def stringToNum(s):
    # Si ça ne fonctionne pas pour mettre en int
    try:
        return int(s)
    # Alors c'est mit en float
    except ValueError:
        return float(s)


def main():
    # Dictionnaire de correspondance pour les opérateurs
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '%': operator.mod,
        '^': operator.xor,
    }

    # Récupérations des entrées de l'utilisateur
    firstNb = stringToNum(input("Entrer le premier nombre : "))
    operatorInput = input("Entrer l'opérateur : ")
    secondNb = stringToNum(input("Entrer le deuxième nombre : "))

    # Dans une variable, le résultat de l'opération
    result = operators[operatorInput](firstNb, secondNb)

    try:
        # Enlève la virgule si le résultat est un integer
        if result.is_integer():
            result = int(result)
    except AttributeError:
        result = result

    # Nom du fichier où le résultat sera enregistré
    nameOfFile = input("Nom du fichier : ")

    # ouverture du fichier en mode overwrite, écriture du résultat en string dedans et fermeture du dit fichier
    file = open(nameOfFile + ".txt", "w")
    file.write(str(result))
    file.close()


if __name__ == "__main__":
    main()
