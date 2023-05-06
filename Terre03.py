##L’alphabet à partir de 
## affiche les lettres de l'alphabet à partir d'un argument puis revient à la ligne

## Variables et Import
Lettre = ""
Alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
Nbre_Lettre = len(Alphabet)
import sys

# passe l'argument saisi en minuscule
if len(sys.argv) == 1 : #si l'argument est absent
	print ("veuillez saisir une Lettre de l'alphabet")
	
else:
	Saisie = sys.argv[1].lower()

	# Test 
	if len(sys.argv)>= 3 : #si il n'y a pas trop d'arguments
		print ("Veuillez saisir une seule Lettre svp")

	elif len(sys.argv[1])>= 2 : #si l'argument contient plusieurs charactères
		print ("Veuillez saisir une seule Lettre svp")

	elif Alphabet.count(Saisie) == 0: #si l'argument fait partie de la liste
		print("votre saisie ne fait pas partie de l'alphabet")

	else:
		for Lettre in range(Alphabet.index(Saisie), Nbre_Lettre) : #affiche les lettres de l'alphabet à partir d'un argument puis revient à la ligne
			print (Alphabet[Lettre] , end = '')
		print("")

#FIN