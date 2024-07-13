from Charger_donnees import *
from Verification_saisies import * 

# Cette focntion permet de cherger le vente par client
def vente_client ():
    
    LISTE_RAPPORT =  charger_donnees_vente()
    VERIFICATEUR  = 0
    while VERIFICATEUR == 0:
        REPONSE_UTILISATUER = input("\n \t\t\t\tEntrez le nom du client : ")
      
        VERIFICATEUR = verification_vente(REPONSE_UTILISATUER,VERIFICATEUR)
        
    COMPTEUR = 0
    print(f"\n \t\t\t\tINFOS SUR LE(s) VENTE (S) EFFECTUEE (S) PAR {REPONSE_UTILISATUER} \n")
    for CLIENT in LISTE_RAPPORT:
            if CLIENT[1].lower() == REPONSE_UTILISATUER.lower():
                COMPTEUR +=1
                print(f" ID VENTE : {CLIENT[0]}  |NOM PRODUIT : {CLIENT[2]} |QUANTITE : {CLIENT[3]} |PRIX UNITAIRE : {CLIENT[4]} |PRIX TOTAL A PAYER : {CLIENT[5]} |DATE : {CLIENT[6]} |HEURE : {CLIENT[7]}")
                print(" ===============================================================================================================================================")
    if COMPTEUR == 0: 
        print(f"\n \t\t\t\tAucun client porte le nom  {REPONSE_UTILISATUER} 😯\n")
