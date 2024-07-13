
import sys
from Ajout_Produits import *
from Afficher_Produits import *
from Rechercher_Produit import *
from enregistrer_vente import *
from Affiche_Ventes import *
from vente_client import *
from Rapport import *
from Charger_donnees import * 
from modiffier import * 
from mot_de_passe import *
from filtrage import*

LISTE_PRODUITS = []  #la liste vide pour les produits
LISTE_PRODUITS = charger_donnees_produit() # gargement de produit que j'affecte dans la liste produit depuis le fichier PRODUIT.json

#la variable MENU contient les différentes options, juste pour les affichées
MENU = """\n \t\t\t\t MENU PRINCIPAL\n""" """
                1.  Ajouter produit
                2.  Afficher produits
                3.  Rechercher produit
                4.  Enregistrer vente
                5.  Afficher ventes
                6.  Ventes par client
                7.  Générer rapport de ventes
                8.  Modification produit
                9.  Suppression des données
                10. Charger données
                11. Filtrage par date
                12. Quitter
                ❓ Votre choix : """

MENU_CHOICES = ["1","2","3","4","5","6","7","8","9","10","11","12"]   # la liste MENU_CHOIX contient les différents choix selon le menus dispo


while True:    
        CHOIX_UTILISATEUR = "" # la variable qui contiendrans le choix de l'utilisateurs pour les menus
        while CHOIX_UTILISATEUR not in MENU_CHOICES: # la boucle qui turne si le choix taper par l'utilisateur ne pas dans la liste de choix
            CHOIX_UTILISATEUR = input(MENU)
            if CHOIX_UTILISATEUR not in MENU_CHOICES:
                print("\t\tVeuillez Choisir une option valide...")
        if CHOIX_UTILISATEUR == "1":  # toutes les structures , permettentes de lancer un fonction précise selon le choix
            ajouter_Produits(LISTE_PRODUITS)
        elif CHOIX_UTILISATEUR =="2":
            Afficher_Produit(LISTE_PRODUITS)
        elif CHOIX_UTILISATEUR == "3":
            rechercher_produit()
        elif CHOIX_UTILISATEUR =="4":
            Enregistrer_vente(LISTE_PRODUITS)
        elif CHOIX_UTILISATEUR  == "5":
            afficher_vente()
        elif CHOIX_UTILISATEUR =="6":
            vente_client ()
        elif CHOIX_UTILISATEUR == "7":
            rapport()
        elif CHOIX_UTILISATEUR =="8":
            modification()
        elif CHOIX_UTILISATEUR == "9":
            mot_de_passe()
        elif CHOIX_UTILISATEUR =="10":
            charger_donnees_produit()
            charger_donnees_vente()
            print("\n \t\t\tchargement de données terminer\n")
        elif CHOIX_UTILISATEUR =="11":
            filtrer_vente()
        elif CHOIX_UTILISATEUR  == "12":
            print("\n \t\t\t\tÀ BIENTÔT...👐")
            sys.exit()  # une fonction de python importée depuis le module sys, qui permet d'arreter l'execution du code
        
