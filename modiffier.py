import json
from Verification_saisies import *
from Charger_donnees import *
from sauvegarde_donnees import * 
from datetime import datetime
import time 

def modification ():
  
    LISTE_MODIFICATION = charger_donnees_produit() # chargement du fichier produit

    VERIFICATEUR = 0   # permet de déclancher la boucle while

    while VERIFICATEUR == 0:    # permet de bouclé si l'utilisateur laisse la case de nom du produit vide
        CHOIX_UTILISATEUR = input("\n \t\tEntrer le nom du produit à modifier : ")
        if CHOIX_UTILISATEUR == "":
            print(f"\n \t\t\t\tAttention  🚨🚨 le champs de nom du produit à modifier ne doit pas resté vide \n \t\t\t\t\t\t VEUILLEZ LE REMPLIR SVP  😯""")
        else:
            VERIFICATEUR = 1

    RESULTAT = []  # liste vide qui va contenir les informations qui vont modifier l'ancien
    COMPTEUR = 0
    indice = 0   # la variable qui va recuperer l'indice du produit a modifier
    for PRODUIT in LISTE_MODIFICATION:   # permet de parcourir liste de produit

        if PRODUIT[1].lower() == CHOIX_UTILISATEUR.lower():   # permet de verifier si le produit existe et de le récuperer
            COMPTEUR +=1 
            RESULTAT.append(PRODUIT)
            indice = PRODUIT [0] - 1  # recuperation de l'indice du produit
           
    

    if COMPTEUR == 0:
        print(f"\n \t\t\t\tAucun produit porte le nom  {CHOIX_UTILISATEUR} 😯\n")
    else:
        print("\n \t\t\t\t LES INFORMATIONS SUR LE PRODUIT QUE VOUS SOUHAITEZ MODIFIER \n")
        for PRODIT_DISP in RESULTAT:
            print(f"\t\t ID : {PRODIT_DISP[0]} | NOM PRODUIT : {PRODIT_DISP[1]} | PRIX : {PRODIT_DISP[2]} | QUANTITE EN STOCK :  {PRODIT_DISP[3]}")
            print("\t\t ================================================================================")

    print("\n \t\t\t\t ENTREZ LES NOUVELLES INFORMATIONS \n""")
    VERIFICATEUR = 0
    while VERIFICATEUR == 0:    
            NOM_PRODUIT  = input("\t\tEntrez le nom du produit : ")
            PRIX_PRODUIT  = input("\t\tEntrez le prix du produit : ")
            QUANTITE_PRODUIT = input("\t\tEntrez la quantité du produit : ")
            
            VERIFICATEUR = verification_modification(NOM_PRODUIT,PRIX_PRODUIT,QUANTITE_PRODUIT,VERIFICATEUR)   # verification de saisie
    
    LISTE_MODIFICATION[indice][1] = NOM_PRODUIT
    LISTE_MODIFICATION[indice][2] = float(PRIX_PRODUIT)
    LISTE_MODIFICATION[indice][3] =  int(QUANTITE_PRODUIT)
    heure = time.strftime('%H:%M:%S')
    date = datetime.today().strftime('%d/%m/%Y')
    LISTE_MODIFICATION [indice][4] = date
    LISTE_MODIFICATION [indice][5]= heure 

    sauvergade_donnees_achat(LISTE_MODIFICATION)  # sauvegarde des infos pour le produit modifier

    print(f"\n \t\t\t\tla modification du produit à été effectuée avec succès \n")