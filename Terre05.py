## Division
## Affiche le résultat et le reste d’une division entre deux nombres.

## Variables et Import
import sys
Bad_Answer = "Erreur"

try :	
	# Variables
	Saisie1 = int(sys.argv[1]) 
	Saisie2 = int(sys.argv[2])
	Resultat = Saisie1 // Saisie2
	Reste = Saisie1 % Saisie2

	# Test
	if len(sys.argv)>= 4 : #si il n'y a pas trop d'arguments
		print(Bad_Answer)

	elif len(sys.argv)< 3 : # si il manque un argument
		print(Bad_Answer)

	elif Resultat != 0 : # test si le resultat n'est pas zero	
		print("Resulat :", Resultat )
		print("Reste :", Reste )
	else:	
		print(Bad_Answer)
	
except ValueError : #si l'argument autre chose qu'un integer
	print(Bad_Answer)

except IndexError : #si l'argument est absent
	print(Bad_Answer)

except ZeroDivisionError : # si le dividande est 0
	print(Bad_Answer)

#FIN