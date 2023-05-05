## Afficheur d’arguments
## affiche tous les arguments identifié lors de la saisie de la commande
## Import Variables

import sys

# effectue une boucle suivant le nbre d'argument saisie et les affiche un par un avec retour à la ligne 
for arg in sys.argv:
    #exclue le premier argument (nom de ficher) grace à un test
    if arg != sys.argv[0]:
        print (arg)

 #FIN