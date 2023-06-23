## 
## affiche la transformation d'une heure affichée en format 24h en une heure affichée en format 12h

## Variables Import et Fonction
import sys 

def message_erreur(): 
    print("Erreur!")

if len(sys.argv) >=5 : # si trop d'arguments
    message_erreur()

else :
    try :
        Arg1 = int(sys.argv[1])
        Arg2 = int(sys.argv[2])
        Arg3 = int(sys.argv[3])
        Verif_Tri = { Arg1 < Arg2 < Arg3 : True,  # création d'un dictionnaire (clé: valeur) qui répertorie les différents cas
                    Arg1 == Arg2 : False,
                    Arg1 == Arg3 : False,
                    Arg2 == Arg3 : False,
                    Arg1 == Arg2 ==Arg3 : False
    } [True]
        if Verif_Tri == True :
            print("Trié") 
        elif Verif_Tri == False :
            print('Erreur!')
        else:
            print('Pas trié')

    except KeyError : #si autre saisie de integer non triée
        print('Pas trié')

    except ValueError : #si erreur de type de variable
        message_erreur()

    except IndexError : # si absence d'arguments
        message_erreur()
#FIN