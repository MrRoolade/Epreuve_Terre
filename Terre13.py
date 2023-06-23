## trouver la Suisse
## programme qui prend en paramètre trois entiers et affiche la valeur du milieu.

## Variables Import et Fonction
import sys

def message_erreur(): # Fonction ERREUR
    print("Erreur!")

if  len(sys.argv) >=5 : # si trop d'arguments
    message_erreur()
    print(1)

else :
    try :
        Premier_arg = int(sys.argv[1])
        Deuxieme_arg = int(sys.argv[2])
        Troisieme_arg = int(sys.argv[3])

        # tableau = [ Premier_arg,Deuxieme_arg,Troisieme_arg]
        # tableau.sort(), print(tableau[1])

        Suisse = { Premier_arg > Deuxieme_arg > Troisieme_arg : Deuxieme_arg,
                  Deuxieme_arg > Troisieme_arg > Premier_arg : Troisieme_arg,
                  Troisieme_arg > Premier_arg > Deuxieme_arg : Premier_arg,
                  Troisieme_arg > Deuxieme_arg >  Premier_arg : Deuxieme_arg,
                  Premier_arg > Troisieme_arg >Deuxieme_arg : Troisieme_arg,
                  Deuxieme_arg > Premier_arg >Troisieme_arg  : Premier_arg,
                  Premier_arg==Troisieme_arg : f'Erreur!',
                  Premier_arg==Deuxieme_arg : f'Erreur!',
                  Deuxieme_arg==Troisieme_arg : f'Erreur!'
        }[True]
               
        print(f'{Suisse}')
        sys.exit()
      
    except ValueError : #si erreur de type de variable
        message_erreur()
        print(2)

    except IndexError : # si absence d'arguments
        message_erreur()
        print(3)
#FIN