import json
from Verification_saisies import * 
from Charger_donnees import * 
from sauvegarde_donnees import *
from datetime import datetime
import time 

# cette focntion permet  d'ajouter le produit
def ajouter_Produits(LISTE_PARAMETRE):
        LISTE_INTERMEDIAIRE = [] # liste vide qui va contenir les informations du nouveau produit avant de les inserer dans la liste LISTE_PARAMETRE
        id = len(LISTE_PARAMETRE)+1 # permet d'incrementer l'ID du produit à chaque enregistrement SA PRENDS LA TAILLE DU TABLEAU + 1

        VERIFICATEUR  = 0  # permet de déclancher la boucle WHILE pour faire la vérification de saisie
        print("""\n \t\t\t\t ENREGISTREMENT DU PRODUIT\n""")
        while VERIFICATEUR < 2:

            if VERIFICATEUR == 1 :   # permet d'afficher autrement le messages après une erreur lors de la saisie des informations
                REP_UTILISATEUR = input("\t\tVOULEZ-VOUS QUITTER (QUITTER) OU BIEN MODIFIER (CONTINUE) ?: ")
                if REP_UTILISATEUR.lower() == "QUITTER".lower():  # permet d'arreter l'opération si l'utilisateur tape EXIT
                            print(f"\n \t\t\t\tVOUS VENEZ D'ANNULER L'OPERATION  \n") 
                            return
                elif REP_UTILISATEUR.lower() == "CONTINUE".lower():   # permet de redémander à l'utilisateur les infos pour le produit
                    LISTE_PRODUITS = charger_donnees_produit()  # chargement du fichier PRODUIT.JSON et stocker les infos dans la variable LIESTE_PRODUITS
                    NOM_PRODUIT  = input("\t\tEntrez le nom du produit : ")
                    NOM_PRODUIT = NOM_PRODUIT.upper()
                    PRIX_PRODUIT  = input("\t\tEntrez le prix du produit : ")
                    QUANTITE_PRODUIT = input("\t\tEntrez la quantité du produit : ")

                    VERIFICATEUR = verification_ajout_produit(NOM_PRODUIT,PRIX_PRODUIT,QUANTITE_PRODUIT,LISTE_PRODUITS,VERIFICATEUR,id)
                else:
                      VERIFICATEUR = 1
            else:
                LISTE_PRODUITS = charger_donnees_produit()  # chargement du fichier PRODUIT.JSON et stocker les infos dans la variable LIESTE_PRODUITS
                NOM = input("\t\tEntrez le nom du produit : ")
                NOM_PRODUIT = NOM.upper()
                PRIX_PRODUIT  = input("\t\tEntrez le prix du produit : ")
                QUANTITE_PRODUIT = input("\t\tEntrez la quantité du produit : ")

                VERIFICATEUR = verification_ajout_produit(NOM_PRODUIT,PRIX_PRODUIT,QUANTITE_PRODUIT,LISTE_PRODUITS,VERIFICATEUR,id)

        PRIX_PRODUIT = float(PRIX_PRODUIT)    # conversion du type de la valeur PRIX_PRODUIT en (FLOAT)
        # la partie qui permet d'ajouter les informations dans la liste intermediaire
        LISTE_INTERMEDIAIRE.append(id)
        LISTE_INTERMEDIAIRE.append(NOM_PRODUIT)
        LISTE_INTERMEDIAIRE.append(PRIX_PRODUIT)
        LISTE_INTERMEDIAIRE.append(int(QUANTITE_PRODUIT))
        heure = time.strftime('%H:%M:%S')   # permet de stocker l'heure à la quelle on ajoute le produit
        date = datetime.today().strftime('%d/%m/%Y') # permet de stocker la date à la quelle on ajoute le produit
        LISTE_INTERMEDIAIRE.append(date)
        LISTE_INTERMEDIAIRE.append(heure)

        LISTE_PARAMETRE.append(LISTE_INTERMEDIAIRE)  # ajout de la liste intermediaire dans la liste parametre
        
        sauvergade_donnees_achat(LISTE_PARAMETRE)  # sauvegarde de la nouvelle liste qui contient l'element ajouter dans le fichier PRODUIT.JSON appartir de (la fonction sauvergade_donnees_achat) du module (sauvegarde_données)

        print("\n \t\t\t\tLe produit à été bien ajouter en stock \n")
        return LISTE_PARAMETRE

