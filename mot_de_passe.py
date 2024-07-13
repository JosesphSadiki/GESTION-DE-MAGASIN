
from Charger_donnees import * 
from Suppression_donnees import *
from sauvegarde_donnees import mot_de_passe_SAUVE 

#cette confion intervient lors de la connexion pour supprimer les données
def mot_de_passe():
    print("""\n \t\t\t\tPARTIE RESERVEE A L'ADMINISTRATEUR\n""")
    
    mot_de_passe_Ver = mot_de_passe_char()   # chargement  du fichier MotDEpasse.json et prend le mot de passe pour le stocker dans la (variable mot_de_passe_Ver)
    NBRE_ESSAIS = 4

    if mot_de_passe_Ver == "":
        print(f"\n \t\t\t\tACCÈS  LIBRE \n")
    else: 
        REPONSE_UTILISATEUR = input("\t\tEntrez le mot de passe : ")
        while mot_de_passe_Ver != REPONSE_UTILISATEUR and NBRE_ESSAIS > 1:   # permet de comprarer si le mot de passe saisi par l'utilisateur est egal au mot de passe qui est dans le fichier
            NBRE_ESSAIS -= 1
            print(f"\n \t\t\t\tMot de passe incorrect, il vous reste {NBRE_ESSAIS} d'essaies 🚨🚨\n")
            REPONSE_UTILISATEUR = input("\t\tEntrez le mot de passe (EXIT) pour quitter : ")

            if REPONSE_UTILISATEUR == "EXIT" or REPONSE_UTILISATEUR ==  "exit":
                print(f"\n \t\t\t\tVOUS VENEZ D'ANNULER L'OPERATION \n")
                return
        
    if NBRE_ESSAIS == 1:
         print(f"\n \t\t\t\tVous venez de dépasser le nombre d'éssaies,🚨🚨\n \t\t\t\tVEUILLEZ VOUS RAPPELEZ LE MOT DE PASSE ET REVENIR PLUS TARD")
         return
    else :
        print(f"\n \t\t\t\tMot de passe correct \n")
        print("\t\t1. supprimer le stock")
        print("\t\t2. supprimer les ventes")
        VEREIFICATEUR = 0

        while VEREIFICATEUR == 0:
            REP = input("\t\t❓ Votre choix (EXIT) pour quitter : ")
            if REP == "1":
                supprimer_stock()
            elif REP == "2":
                supprimer_vente()
            elif REP =="EXIT" or "exit":
                print(f"\n \t\t\t\tVOUS VENEZ D'ANNULER L'OPERATION \n")
                return
            else:
                print(f"\n \t\t\t\tMAUVAIS CHOIX \n")
                

#cette focnction permet la  sauvegarde d'un nouveau mot de passe
def sauvegarde_mot_de_passe():
    mot_de_passe_ver = mot_de_passe_char()  # chargement du fichier mot de passe.json
    ESSAIE = 4
    print("""\n \t\t\t\tPARTIE RESERVEE A L'ADMINISTRATEUR\n""")
    if mot_de_passe_ver == "":
        print(f"\n \t\t\t\tACCÈS  LIBRE \n")
    else :
        ANCIEN_mot_de_passe = input("\t\tENTRER L'ANCIEN MOT DE PASSE  : ")
        ESSAIE = 4
        while ANCIEN_mot_de_passe != mot_de_passe_ver and ESSAIE > 1 :   # vérification si le mot de passe pour la connexion est correct
                ESSAIE -= 1
                print(f"\n \t\t\t\tMot de passe incorrect \n")
                ANCIEN_mot_de_passe = input("\t\tENTRER L'ANCIEN MOT DE PASSE (EXIT) : ")
                if ANCIEN_mot_de_passe.lower() =="EXIT".lower():
                    print(f"\n \t\t\t\tVOUS VENEZ D'ANNULER L'OPERATION \n")
                    return
    if ESSAIE >=1 :
        VERIFICATEUR = 0
        VERIFICATEUR2 = 0

        while VERIFICATEUR == 0:
            VERIFICATEUR2 = 0
            Nouveau_mot_de_passe = input("\n\t\tENTREZ LE NOUVEAU MOT DE PASSE : ")
            confirmation_mot_de_passe = input("\t\tCONFIRMER VOTRE MOT DE PASSE : ")
            if confirmation_mot_de_passe != Nouveau_mot_de_passe:   # vérification du nouveau mot de passe et le mot de passe de confirmation
                  print(f"\n \t\t\t\tle mot de passe de confirmation ne pas égal au nouveau mot de passe \n") 
                        
            else:
                mot_de_passe_SAUVE(Nouveau_mot_de_passe)
                print(f"\n \t\t\t\tle Nouveau Mot de passe est enregistrer avec succès \n")
                return
            while VERIFICATEUR2 == 0 :
                REP_UTILISATEUR = input("\t\tVOULEZ-VOUS QUITTER (QUITTER) OU BIEN MODIFIER (CONTINUE) ?: ")
                if REP_UTILISATEUR.lower() == "QUITTER".lower():
                            print(f"\n \t\t\t\tVOUS VENEZ D'ANNULER L'OPERATION  \n") 
                            return
                elif REP_UTILISATEUR.lower() == "CONTINUE".lower():
                    VERIFICATEUR2 = 1
                else:
                     continue
    else :
        print(f"\n \t\t\t\tVOUS VENEZ DE DEPPASE LE NOMBRE D'ESSAIES \n")
        return
        