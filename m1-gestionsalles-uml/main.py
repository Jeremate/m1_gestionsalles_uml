from patrimoine import batiment
from patrimoine import typesalle
from patrimoine import materiel
from patrimoine import typemateriels
from patrimoine import salles
from patrimoine import typesalles

''' variables  '''
''' liste des batiment'''
batiments = {}
typesalles = []
materiels = []
typemateriels = []
salles = []
typesalles = []

''' fonctionnalitées batiment'''
def ajouter_batiment(no_bat,nom,adresse):
	nouveau_bat = batiment.batiment(nom,adresse)
	if no_bat not in batiments.keys():
		batiments[no_bat] = nouveau_bat


def rechercher_batiment(no_bat):
	print(no_bat," ",batiments[no_bat])


def modifier_batiment(no_bat,nom,adresse):
	nouveau_bat = batiment.batiment(nom,adresse)
	if no_bat in batiments.keys():
		batiments[no_bat] = nouveau_bat

def supprimer_batiment(no_bat):
	if no_bat not in batiments.keys():
		del batiments[no_bat]

'''fonctionnalitées typesalle'''
def ajouter_typesalle(nom):
	var_ajout = 1
	for ts in typesalles:
		if ts.getnom() == nom:
			var_ajout = 0
	if var_ajout:
		nouveau_typesalle = typesalle.typesalle(nom)
		typesalles.append(nouveau_typesalle)

def supprimer_typesalle(nom):
	for ts in typsalles:
		if ts.getnom() == nom:
			typesalle.remove(ts)

def consulter_typesalle(nom):
	for ts in typesalles:
		if ts.getnom() == nom:
			print(ts)

'''fonctionnalitées materiel'''
def ajouter_materiel(self,code_inv):


'''fonctionnalitées typemateriel'''
def ajouter_typemateriel(nom):
	var_ajout = 1
	for tm in typemateriels:
		if ts.getnom() == nom:
			var_ajout = 0
	if var_ajout:
		nouveau_typemateriel = typemateriel.typemateriel(nom)
		typemateriels.append(nouveau_typemateriel)

def supprimer_typemateriel(nom):
	for tm in typemateriels:
		if tm.getnom() == nom:
			typemateriels.remove(ts)

def consulter_typemateriel(nom):
	for tm in typemateriels:
		if tm.getnom() == nom:
			print(ts)


'''fonctionnalitées salle'''


def main():
	ajouter_batiment(1,"bat_1","adresse_1")
	'''ajouter_batiment(2,"bat_2","adresse_2")
	modifier_batiment(2,"bat_3","adresse_3")
	rechercher_batiment(2)'''
	ajouter_typemateriel("wow")
	supprimer_typemateriel("wow")
	supprimer_typesalle()
	print(typemateriels)
	print(batiments)

if __name__ == '__main__':
	main()
