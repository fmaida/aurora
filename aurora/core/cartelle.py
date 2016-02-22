import os


class Cartella:
	"""
	Classe per gestire una cartella di sistema:
	per controllarla, cancellarla e crearla
	"""

	def __init__(self, p_percorso=None):
		self._percorso = None
		self.imposta(p_percorso)

	def imposta(self, p_percorso):
		self._percorso = p_percorso

	def get(self, p_percorso=None):
		if p_percorso is None:
			return self._percorso
		else:
			return os.path.join(self._percorso, p_percorso)

	def esiste(self):
		return os.path.exists(self._percorso)

	def crea(self, p_percorso=None):
		if p_percorso is None:
			os.mkdir(self.get())
		else:
			os.mkdir(self.get(p_percorso))

	def ricrea(self, p_percorso):
		pass

	def __add__(self, p_altro):
		nuovo_percorso = os.path.join(self._percorso, p_altro)
		return Cartella(nuovo_percorso)

	def __str__(self):
		return self._percorso
