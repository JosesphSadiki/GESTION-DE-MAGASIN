
from enregistrer_vente import*
import json
def filtrer_vente():
  fichiers_vente=charger_donnees_vente()
  if fichiers_vente==[]:
    print("il n'y a aucune vente enregistrée !!")
    return
  else:
    date_debut=input(" entrez la date de debut DD-MM-YY: ")
    date_fin=input("entrez la date de la fin DD-MM-YY: ")
    if date_debut=="" or date_fin=="":
       print("tous les champs sont obligatoires !")
       return
    else:
       ventes_filtrees=[]
       compte=0
       for ventes in fichiers_vente:
            if ventes['date']>=date_debut and ventes['date']<=date_fin:
                compte+=1
                ventes_filtrees.append(ventes)
            else:
               continue
            if compte==0:
                print(f"il n y a aucune vente comprise entre {date_debut} et {date_fin} ")
            else:
                print(f"¨\`les ventes filtrées\`n")
            for ventes in ventes_filtrees:
                print(f"{ventes['qte']} {ventes['prix']} {ventes['nom_client']} {ventes['article']}")
             
           
       

    


    
    ventes_filtrees=[]

    date_debut=input("saisissez la date de debut de filtrage: ")
    try:
        from datetime import datetime
        date_debut=datetime.strftime(date_debut,"%d/%m/%y")
    except ValueError:
        print("format de date invalide !")
        return None
    ventes_filtrees=filtrer_vente()
    return ventes_filtrees


    
    


