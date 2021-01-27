#!/usr/bin/env python3



#Créer une calculatrice simple.
#Il faut demander à l’utilisateur un premier nombre.
#Puis un opérateur
#Puis un deuxième nombre.
#Ensuite il faut écrire le résultat dans un fichier dont l'utilisateur choisit le nom.

import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

def operation(a, b, c):
    result = 0
    if a == "+":
        result = b + c
    elif a =="-":
        result = b - c
    elif a =="*":
        result = b * c
    elif a =="/":
        result = b / c
    return(result)

def main():

    #Récupération entrées utilisateur
    firstInt = int(input("Veuillez entrer un chiffre \n"))
    operator = input("Veuillez entrer un opérateur \n")
    secondInt = int(input("veuillez choisir un deuxieme chiffre \n"))
    nameFile = input("dans quel fichier voulez vous écrire le resultat ?\n")

    #Calcul en fonction de l'opérateur choisis
    result = operation(operator, firstInt, secondInt)
    #Création, écriture et fermeture du fichier
    print(result)

    #fileToWrite =  open(nameFile + ".txt", "w")
    #fileToWrite.write(str(firstInt) + operator + str(secondInt) + " =" + str(result))
    #fileToWrite.close()


if __name__== "__main__":
    unittest.main()