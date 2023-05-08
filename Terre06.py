## Inverser une chaîne
## affiche l’inverse de la chaîne de caractères donnée en argument.

## Variables et Import
import sys
Bad_Answer = "Erreur"

try :	
	# Variables
	Saisie = sys.argv[1]
	nbre_car = int(len(Saisie)) #Recuperation de la longueur du string + transforme en integer
	Saisie = list(Saisie) #conversion de la chaine de caractère en list

	# Test
	if len(sys.argv)>= 3 : #si il n'y a pas trop d'arguments
		print(Bad_Answer+'_a')

	else :
		for i in range(nbre_car-1,-1,-1): # boucle à partir du dernier index de la list
			print(Saisie[i], end="")
		print("")

except IndexError : #si l'argument est absent
	print(Bad_Answer+'_e')

#FIN