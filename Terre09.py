## racine carré d'un nombre
## affiche la racine carré d'un nombre suivant les arguments donnés

## Variables et Import
import sys
from  math import *

def message_erreur(): 
    print("Erreur!")

if len(sys.argv) >=3 : # si trop d'arguments
    message_erreur()
    
else :

    try :
        nb1 = int(sys.argv[1])            

        if sys.argv[1].isdigit() != True or nb1 < 0 :
            message_erreur()

        else :
            racine = nb1 ** 0.5
            print(f'{racine : .3f} solution calculée avec la puissance 1/2') # solution classique
            racine = sqrt(nb1)
            print(f'{racine : .3f} solution calculée avec la fonction sqrt()') # solution avec fonction importées de "math"

                
    except ValueError : #si erreur de type de variable
        message_erreur()

    except IndexError : # si absence d'arguments
        message_erreur()
#FIN