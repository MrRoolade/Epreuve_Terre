## Nombre Premier
## affiche si le nombre saisie est un nombre premier ou non

## Variables Import et Fonction
import sys 

def message_erreur(): 
    print("Erreur!")

if len(sys.argv) >=3 : # si trop d'arguments
    message_erreur()

else :

    try :
        Saisie = int(sys.argv[1]) 
        reste_division = [] #creation d'une liste du resulat de l'opératin '%'

        if sys.argv[1].isdigit() != True or Saisie < 0: # teste si l'arguement est valide ou négatif
            message_erreur() 
            
        else :                      
            for x in range(2,Saisie-1) : # boucle sur l'interval de nombre entre 2 et la saisie -1
                reste = Saisie % x          #affecte le résulat de l'opération '%' dans la variable 'reste'
                reste_division.append(reste) #enregistre reste dans la liste reste_division

            if reste_division.count(0) != 0 or Saisie == 0 or Saisie == 1:  
            # teste la presence du chiffre zero dans la liste ou si la saisie est 0 ou 1
                print(f'NON, {Saisie} n\'est pas un nombre premier')
                
            else :
                print(f'OUI, {Saisie} est un nombre premier')
                    
    except ValueError : #si erreur de type de variable
        message_erreur()

    except IndexError : # si absence d'arguments
        message_erreur()
#FIN