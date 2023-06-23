## 24 to 12
## affiche la transformation d'une heure affichée en format 24h en une heure affichée en format 12h

## Variables Import et Fonction
import sys

def message_erreur(): # Fonction ERREUR
    print("Erreur!")
    sys.exit()

if len(sys.argv) >=3 : # si trop d'arguments
    message_erreur()

else :
        
    try :
        H_Saisie = sys.argv[1]
        hh = int(H_Saisie[0:2])
        mm = int(H_Saisie[3:-2])
        pp = H_Saisie[-2:]

        if hh == 00 :
            message_erreur()

        elif pp.upper() != "AM" and pp.upper() != "PM":
            message_erreur()

        elif hh > 12 or mm > 59:
            message_erreur()
        
        else :
            hh = { pp.upper() == "AM" and hh == 12  : "00",
                    hh == 12 and pp.upper() == "PM" : 12,
                    hh < 12 and pp.upper() == "PM" : hh + 12,
                    hh <10 and pp.upper() == "AM" : f"0{hh}",
                    12 > hh >= 10 and pp.upper() == "AM" : hh 
            }[True]
        
        print(f'{hh}:{mm}')
      
    except ValueError : #si erreur de type de variable
        message_erreur()

    except IndexError : # si absence d'arguments
        message_erreur()
#FIN