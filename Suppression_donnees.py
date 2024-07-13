from Charger_donnees import * 
from sauvegarde_donnees import *
from Charger_donnees import *
from sauvegarde_donnees import *
from datetime import datetime
import time

# fonction pour la suppression de produit
def supprimer_stock():
    LISTE_PRODUITS = charger_donnees_produit()  # chargement du fichier PRODUIT.JSON
    REPONSE = input(f"\n \t\tÊTES-VOUS SUR DE VOULOIR VIDE LE STOCK (OUI/NON) ? : ")
    
    if REPONSE =="OUI" or "oui": 
        LISTE_INTERMEDIAIRE =[]

        if LISTE_PRODUITS == []:
            print(f"\n \t\tLE STOCK EST DEJA VIDE")
        else:
            LISTE_PRODUITS  = []
            sauvergade_donnees_achat(LISTE_PRODUITS)
            LISTE_SUPPR = rapport_suppresion()
            heure = time.strftime('%H:%M:%S')
            date = datetime.today().strftime('%d/%m/%Y')
            LISTE_INTERMEDIAIRE.append("Suppression de stock")
            LISTE_INTERMEDIAIRE.append(date)
            LISTE_INTERMEDIAIRE.append(heure)
            LISTE_SUPPR.append(LISTE_INTERMEDIAIRE)
            sauvergade_donnees_suppression(LISTE_SUPPR)  # enregistre une liste vide dans le fichier achat
            print(f"\n \t\t\t\t SUPPRESSION DE STOCK REUSSIE AVEC SUCCÈS\n")
        
    elif REPONSE =="NON" or "non":
        print(f"\n \t\tVous venez d'annuler l'operation de la suppression\n")
    else:
        print(f"\n \t\tVous venez d'inserer une réponse différente de (OUI ou NON)\n")
        supprimer_stock()
    return

# cette fonction permet de supprimer le vente
def supprimer_vente():

    LISTE_VENTE = charger_donnees_vente()  # chargement du fichier vent.json
    REPONSE = input(f"\n \t\tÊTES-VOUS SUR DE VOULOIR VIDE LES EVENEMENTS DE VENTE (OUI/NON) ? : ")

    if REPONSE =="OUI" or "oui": 
        LISTE_INTERMEDIAIRE = []
        if LISTE_VENTE == []:
            print(f"\n \t\tIL Y A AUCUNNE VENTE EFFECTUEE, DONC C'EST VIDE\n")
        else:

            LISTE_VENTE = []
            sauvergade_donnees_vente(LISTE_VENTE)
            LISTE_SUPPR = rapport_suppresion()
            heure = time.strftime('%H:%M:%S')
            date = datetime.today().strftime('%d/%m/%Y')
            LISTE_INTERMEDIAIRE.append("Suppression événement de vente")
            LISTE_INTERMEDIAIRE.append(date)
            LISTE_INTERMEDIAIRE.append(heure)
            LISTE_SUPPR.append(LISTE_INTERMEDIAIRE)
            sauvergade_donnees_suppression(LISTE_SUPPR)    # enregistre la liste vide dans le fichier VENTE.JSON
            print(f"\n \t\t\t\t SUPPRESSION REUSSIE AVEC SUCCÈS\n")
    elif REPONSE =="NON" or "non":
        print(f"\n \t\tVous venez d'annuler l'operation de la suppression\n")
    else:
        print(f"\n \t\tVous venez d'inserer une réponse différente de (OUI ou NON)\n")
        supprimer_vente()
    return

