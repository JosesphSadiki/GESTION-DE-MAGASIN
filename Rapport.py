from datetime import datetime
from Charger_donnees import *
import json

#Cette focntion permet a générer un rapport journalier pour tout activité
def rapport ():

    # chargement des fichiers
    LISTE_VENTE = charger_donnees_vente()
    LISTE_ACHAT = charger_donnees_produit()
    LISTE_RAPPORT_SUP = rapport_suppresion()

    COMPTEUR = 0
    COMPTEUR2 = 0
    COMPTEUR3 = 0
    date = datetime.today().strftime('%d/%m/%Y')

    print("\n \t\t\t\tRAPPORT JOURNALIER:")
    print("\n \t\t\t\tACHAT\n")

    for ACHAT in LISTE_ACHAT: # parcours le fichier pour les ACHAT
                if ACHAT[4] == date:   # compare si la date l'achat est égale à la date actuelle
                    COMPTEUR +=1
                    print(f"\t\t ID PRODUIT : {ACHAT[0]} | NOM PRODUIT : {ACHAT[1]} | PRIX : {ACHAT[2]} | QUANTITE : {ACHAT[3]} | DATE : {ACHAT[4]} | HEURE {ACHAT[5]}")
                    print("\t\t ================================================================================")
    if COMPTEUR == 0:
         print("\n \t\t\t\tAUCUN ACHAT A ETE FAIT AUJOURD'HUI\n")

    print("\n \t\t\t\tVENTES \n")
          
    for VENTE in LISTE_VENTE:   # parcours le fichier pour les VENTES
        if VENTE[6] == date:   # compare si la date l'achat est égale à la date actuelle
            COMPTEUR2 +=1
            print(f"\tID VENTE {VENTE[0]}  |NOM PRODUIT {VENTE[2]} |QUANTITE {VENTE[3]} |PRIX UNITAIRE {VENTE[4]} |PRIX TOTAL A PAYER {VENTE[5]} |DATE {VENTE[6]} |HEURE {VENTE[7]} ")
            print("\t=========================================================================================================================")
    if COMPTEUR2 == 0:
         print("\n \t\t\t\tAUCUNNE VENTE A ETE FAITE AUJOURD'HUI\n")

    print("\n \t\t\t\tSUPPRESSION \n")

    for RAPPORT_SUPP in LISTE_RAPPORT_SUP:  # parcours le fichier suppressions
        if RAPPORT_SUPP[1] == date:  # compare si la date de l'evenement de suppression est égale à la date actuelle
            COMPTEUR3 +=1
            print(f"\tTACHE : {RAPPORT_SUPP[0]}  | DATE : {RAPPORT_SUPP[1]} | HEURE : {RAPPORT_SUPP[2]} ")
            print("\t===================================================================================================")
    if COMPTEUR3 == 0:
         print("\n \t\t\t\tAUCUNNE SUPPRESSION A ETE FAITE AUJOURD'HUI\n")
    