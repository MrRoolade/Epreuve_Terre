##L’alphabet à partir de 
## affiche les lettres de l'alphabet à partir d'un argument puis revient à la ligne

## Variables et Import
Lettre = ""
Alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
Nbre_Lettre = len(Alphabet)
import sys

# passe l'argument saisi en minuscule
Saisie = sys.argv[1].lower()

# Test 
if len(sys.argv)>= 3 : #si il n'y a pas trop d'arguments
	print ("trop d'arg")
elif len(sys.argv[1])>= 2 : #si l'argument contient plusieurs charactères
	print ("arg trop long")
elif Alphabet.count(Saisie) == 0: #si l'argument fait partie de la liste
	print("votre saisie ne fait pas partie de l'alphabet")
else:
	for Lettre in range(Alphabet.index(Saisie), Nbre_Lettre) : #affiche les lettres de l'alphabet à partir d'un argument puis revient à la ligne
		print (Alphabet[Lettre] , end = '')
	print("")

#FIN