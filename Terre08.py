## puissance d'un nombre
## affiche la puissance d'un nombre suivant les arguments donnés

## Variables et Import
import sys

def message_erreur():
    print("Erreur!")

if len(sys.argv) >=4 : # si trop d'arguments
    message_erreur()
    
else :

    try :
       
        nb1 = int(sys.argv[1])            
        nb2 = int(sys.argv[2])

        if sys.argv[1].isdigit() != True or nb1 < 0 : # verifie si arg n°1 est un chiffre ou négatif
            message_erreur()

        elif sys.argv[2].isdigit() != True  or nb2 < 0 : # verifie si arg n°2 est un chiffre ou négatif
            message_erreur()

        else :
            print(nb1 ** nb2)
                
    except ValueError : #si erreur de type de variable
        message_erreur()

    except IndexError : # si absence d'arguments
        message_erreur()
#FIN