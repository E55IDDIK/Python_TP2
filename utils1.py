# Json manup ,Décorateurs et générateurs 
import json
import os
from gestion_examens import *
from datetime import datetime

# Décorateur 

def logger(fonction):
    def wrapper(*args, **kwargs):
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Debut de {fonction.__name__}")
        try :
            resultat = fonction(*args, **kwargs)

            if resultat is None:
                print(f"[INFO] {fonction.__name__} exécutée avec succès.")
            else:
                print(f"[INFO] Résultat de {fonction.__name__} : {resultat}")

            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Fin de {fonction.__name__}")
            print("-" * 40)
            return resultat
        
        except Exception as e:
            print(f"[ERREUR] La fonction {fonction.__name__} a échoué : {e}")
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Fin de {fonction.__name__}")
            print("-" * 40)
    return wrapper

def verifier_json(fonction):
    def wrapper(fichier="data.json"):
        if not os.path.exists(fichier):
            print("[ERREUR] Le fichier data.json n'existe pas.")
            return CentreExamens()
        return fonction(fichier)
    return wrapper

@logger
def sauvegarder_donnees(centre, fichier="data.json"):
    data = {
        "etudiants": [],
        "examens": []
    }

    for e in centre.etudiants:
        data["etudiants"].append(e.to_dict())

    for ex in centre.examens:
        data["examens"].append(ex.to_dict())

    with open(fichier, "w") as f:
        json.dump(data, f, indent=4)
    
@verifier_json
def charger_donnees(fichier="data.json"):
    centre = CentreExamens()
    try:
        with open(fichier,"r") as f:
            data = json.load(f)
    
        # charger les etudiants et les examens
        for e in data["etudiants"]:
            etudiant = Etudiant(
                e["nom"],
                e["numero"],
                e["filiere"]
            )
            centre.ajouter_etudiant(etudiant)

        for ex in data["examens"]:
            examen = Examen( 
                ex["matiere"],
                ex["date"],
                ex["surveillant"]
            )
            centre.ajouter_examen(examen)
        
        print("Données chargées avec succès.")

    except FileNotFoundError:
        print("Fichier inexistant. Aucune donnée chargée.")

    except json.JSONDecodeError:
        print("Fichier JSON vide ou corrompu.")

    except Exception as e:
        print("Erreur lors du chargement :", e)

    return centre

def examens_par_date(examens,date):
    for ex in examens:
        if ex.date == date :
            yield ex

def examens_par_surveillant(examens,surveillant):
    for ex in examens:
        if ex.surveillant == surveillant :
            yield ex


def etudiants_par_filiere(etudiants, filiere):
    for e in etudiants:
        if e.filiere == filiere:
            yield e