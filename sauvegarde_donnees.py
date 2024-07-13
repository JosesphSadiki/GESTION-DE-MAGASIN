import json

# ces focntions permettent la sauvegarde pour tout les fichiers
def sauvergade_donnees_vente(LISTE_PARAMETRE):
    with open('rapport_vente.json','w+') as FICHIER:
            json.dump(LISTE_PARAMETRE,FICHIER)
   
def sauvergade_donnees_achat(LISTE_PARAMETRE):
    with open('Produit.json','w+') as FICHIER:
            json.dump(LISTE_PARAMETRE,FICHIER)

def sauvergade_donnees_suppression(LISTE_PARAMETRE):
    with open('rapport_suppression.json','w+') as FICHIER:
            json.dump(LISTE_PARAMETRE,FICHIER)

def mot_de_passe_SAUVE(MOT_DE_PASSE_PARAMETRE):
      with open('MotDEpasse.json','w+') as FICHIER:
            json.dump(MOT_DE_PASSE_PARAMETRE,FICHIER)