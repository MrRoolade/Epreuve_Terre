## 24 to 12
## affiche la transformation d'une heure affichée en format 24h en une heure affichée en format 12h

import sys 

#FONCTIONS
def convert_hour(hh): # convertit le format des heures 24 en 12
    hh = {hh == 12 or hh == 00: 12,
            0 < hh < 10 : f'0{hh}',
           10 <= hh < 12 : hh,
           12 < hh < 22 : f'0{hh-12}',
           22 <= hh < 24 : hh-12,
    }[True]
    return hh

def display_AM_PM(): # attribut le am ou le pm suivant l'heure
    pp = {hh == 12  or 12 < hh < 23: "PM",
          hh == 00 or 0 < hh < 12 :"AM",
    }[True]
    return pp

def is_int(hh,mm): # verifie si l'argument contient des chiffres
    if mm.isdigit() and hh.isdigit() :
        return True
    else :
        return False

#GESTIONS DES ERREURS / PARSING
try :
    if len(sys.argv) != 2 : # si mauvais format
         raise ValueError("Veuillez saisir une heure au format 'HH:MM'")

    H_Saisie = sys.argv[1]     

    if len(H_Saisie) != 5  or H_Saisie.count(':') != 1 : # si mauvais format
        raise ValueError("Veuillez saisir une heure au format 'HH:MM'")

    hh , mm = H_Saisie.split(":") # attribut des valeurs à hh et mm

    if is_int(hh,mm) is False : # si mauvais format (ne contient pas de chiffre)
        raise ValueError("Veuillez saisir une heure au format 'HH:MM'")
    else :
        hh =int(hh)
        mm = int(mm)

    if not (0 <= mm < 60 and 0 <= hh < 24 ):
         raise ValueError("Merci de saisir une heure valide")

except ValueError as e:
    print(f"Erreur : {e}")
    sys.exit(1)


#AFFICHAGE DU RESULTAT
print (f'{convert_hour(hh)}:{mm:02d}{display_AM_PM()}')

#FIN