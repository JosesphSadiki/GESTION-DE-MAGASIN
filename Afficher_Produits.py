
from Charger_donnees import *

def Afficher_Produit(LISTE_PARAMETRE):
    
    LISTE_PARAMETRE = charger_donnees_produit()  # permet de charhé le fichier PRODUIT.json et d'affecté ses informations dans la liste LISTE_PARAMETRE
    print("""\n \t\t\t\t LE PRODUITS EN STOCK\n""")
    COMPTEUR = 0   # Cette variable permet de vérifier si le fichier ou bien la variable LISTE_PARAMETRE est vide ou pas
    for PRODUIT in LISTE_PARAMETRE:  # permet de parcourir les elements du fichier PRODUIT.JSON est de les affichés
        COMPTEUR +=1
        print(f"\t\t ID : {PRODUIT[0]} | NOM PRODUIT : {PRODUIT[1]}  | PRIX  : {PRODUIT[2]} | QUANTITE EN STOCK : {PRODUIT[3]}")
        print("\t\t ================================================================================")
    if COMPTEUR == 0:  # Si le compteur = 0 donc il y a pas les elements dans le fichier
            print("\n \t\t\t\tIl y a aucun produit dans le stock \n")
            return 
    return LISTE_PARAMETRE
