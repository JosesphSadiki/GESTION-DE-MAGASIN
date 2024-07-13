import json 
from Verification_saisies import *
from Charger_donnees import * 

# la focntion  pour la recherche d'un produit
def rechercher_produit():

    LISTE_PRODUIT = charger_donnees_produit()  # chargement fichier produit
    
    RESULTAT = []  # liste vide pour stocker les produit trouver
    COMPTEUR = 0
    VERIFICATEUR = 0

    while VERIFICATEUR == 0: 
        CHOIX_UTILISATEUR = input("\n \t\tEntrer le nom ou id du produit : ")
        VERIFICATEUR = recherche_produit (CHOIX_UTILISATEUR,VERIFICATEUR)   # verification de saisie

    for PRODUIT in LISTE_PRODUIT:  # permet de parcourir le produit
        if PRODUIT[1].lower() == CHOIX_UTILISATEUR.lower() or PRODUIT[0] == int(CHOIX_UTILISATEUR):   # pour comparer le nom du produit qui est saisi par l'utilisateur au nom de tout les produits pour trouver seul qui est égal
            COMPTEUR +=1
            RESULTAT.append(PRODUIT)
    if COMPTEUR == 0:
        print(f"\n \t\t\t\tAucun produit porte le nom OU id  {CHOIX_UTILISATEUR} 😯\n")
    else:
        print (f"\n \t\t\t\tLE PRODUIT A ETE TROUVE\n")
        
        for PRODIT_DISP in RESULTAT:
            print(f"\t\tID : {PRODIT_DISP[0]} | NOM PRODUIT : {PRODIT_DISP[1]} | PRIX : {PRODIT_DISP[2]} | QUANTITE EN STOCK :  {PRODIT_DISP[3]}")
            print("\t\t================================================================================")

