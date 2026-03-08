# Classes et logique métier (POO)

#class etudiant
class Etudiant:
    def __init__(self, nom, numero, filiere):
        self.__nom = nom
        self.__numero = numero
        self.__filiere = filiere
    #getters et setters pour etudiant
    @property
    def nom(self):
        return self.__nom
    @property
    def numero(self):
        return self.__numero
    
    @property
    def filiere(self):
        return self.__filiere

    @nom.setter
    def nom(self, nom):
        self.__nom = nom
    
    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @filiere.setter
    def filiere(self, filiere):
        self.__filiere = filiere

    def to_dict(self):
        return {
            "nom" : self.__nom,
            "numero" : self.__numero,
            "filiere" : self.__filiere
        }

#class Examen
class Examen:
    def __init__(self,matiere,date,surveillant):
        self.__matiere = matiere
        self.__date = date
        self.__surveillant = surveillant
    # getter et setters pour examen
    @property
    def matiere(self):
        return self.__matiere
    
    @property
    def date(self):
        return self.__date
    
    @property
    def surveillant(self):
        return self.__surveillant

    @matiere.setter
    def matiere(self, matiere):
        self.__matiere = matiere

    @date.setter
    def date(self, date):
        self.__date = date

    @surveillant.setter
    def surveillant(self, surveillant):
        self.__surveillant = surveillant

    
    def to_dict(self):
        return {
            "matiere" : self.__matiere,
            "date" : self.__date,
            "surveillant" : self.__surveillant
        }

#class CentreExamens
class CentreExamens:
    def __init__(self):
        self.__etudiants = []
        self.__examens = []
    
    # getters et setters pour centre d'examens
    @property
    def etudiants(self):
        return self.__etudiants
    @property
    def examens(self):
        return self.__examens

    # les methodes

    # ajouter les etudiants
    def ajouter_etudiant(self, etudiant):
        self.__etudiants.append(etudiant)

    # ajouter les examens
    def ajouter_examen(self,examen):
        self.__examens.append(examen)
    
    # afficher les examens
    def afficher_examens(self):
        for e in self.__examens:
            print(e.to_dict())
    
    # compter le nombre d'examens
    def compter_examens(self):
        return len(self.__examens)

    # statistiques
    def statistiques(self):
        matieres_unique = set()
        for ex in self.__examens:
            matieres_unique.add(ex.matiere)
        
        return {
            "total_examens" : self.compter_examens(),
            "total_etudiants" : len(self.__etudiants),
            "matieres_uniques" : len(matieres_unique)
        }