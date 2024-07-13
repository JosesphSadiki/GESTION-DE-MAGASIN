import json 
from Charger_donnees import * 
#cette focntion permet d'afficher le produits disponibles
def Afficher_Produit_dispo(LISTE_PARAMETRE):
    
    LISTE_PARAMETRE = charger_donnees_produit()   # chargement du fichier PRODUIT.JSON

    print("\n \t\t\t\tLES PRODUITS DISPONIBLES \n")
    COMPTEUR = 0
    for PRODUIT in LISTE_PARAMETRE:
        if PRODUIT[3] > 0 :  # cette condition permet de verifier si la quantité de chaque produit a affiché est supperieure à 0
            COMPTEUR +=1
            print(f"\t\t ID : {PRODUIT[0]} | NOM PRODUIT : {PRODUIT[1]}  | PRIX  : {PRODUIT[2]} | QUANTITE EN STOCK : {PRODUIT[3]}")
            print("\t\t ================================================================================")
    if COMPTEUR == 0:
        print("\n \t\t\t\tLE STOCK EST VIDE\n")
    #     return COMPTEUR,LISTE_PARAMETRE
    # else:
    return COMPTEUR,LISTE_PARAMETRE