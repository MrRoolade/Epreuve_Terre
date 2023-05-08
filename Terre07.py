## Taille d'une chaîne
## affiche le nombre de caractère de la chaîne de caractères donnée en argument.

## Variables et Import
import sys
Bad_Answer = "Erreur"

try :	
	# Variables
	Saisie = sys.argv[1]
	nbre_car = int(len(Saisie)) #Recuperation de la longueur du string + transforme en integer
	Saisie = list(Saisie) #conversion de la chaine de caractère en list
	num = ('0','1','2','3','4','5','6','7','8','9')
	verif_num = False

	# Test
	for x in num : # check si la chaine contient un element de la list num 
		if x in Saisie :
			verif_num = True
			break
	
	if len(sys.argv)>= 3 : #si il n'y a pas trop d'arguments
		print(Bad_Answer)

	elif verif_num == True: # contient un chiffre
		print(Bad_Answer)  

	else :
		print(nbre_car)

except IndexError : #si l'argument est absent
	print(Bad_Answer)

#FIN