## Pair ou impair
## détermine si l'argument donné est un entier pair ou impair..

## Variables et Import
import sys
Bad_Answer = "Tu ne me la mettras pas à l’envers."

try :	
	Saisie = abs(int(sys.argv[1]))

	if len(sys.argv)>= 3 : #si il n'y a pas trop d'arguments
		print(Bad_Answer)
	
	elif Saisie % 2 == 1 : 			
		print("impair")
	else:	
		print("pair")
	
except ValueError : #si l'argument autre chose qu'un integer
	print(Bad_Answer)

except IndexError : #si l'argument est absent
	print(Bad_Answer)

#FIN