class Typemateriel(object):
	"""Classe représentant un type de materiel.

	Attributs:
		nom : nom du type de salle
	"""

	def __init__(self,nom):
		self.nom = nom
	
	def __str__(self):
		return "{nom}".format()

	def __repr__(self):
		return self._nom

	@property
	def nom(self):
	    return self._nom

	@nom.setter
	def nom(self, val):
		self._nom = val