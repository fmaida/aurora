import os

from aurora.core.pagine.pagina import Pagina


class Pagine:

	def __init__(self, p_percorso: str):
		self._percorso = p_percorso
		self._elenco = []
		self._carica_tutti()

	def aggiungi(self, p_pagina: Pagina):
		self._elenco.append(p_pagina)

	def rimuovi(self, p_indice: int):
		self._elenco.remove(p_indice)

	def _carica_tutti(self):
		"""
		Carica tutti i files presenti nella cartella indicata
		"""
		for elemento in os.scandir(self._percorso):
			nome, estensione = os.path.splitext(elemento.name)
			estensione = estensione.lower()
			if estensione == ".md" or estensione == ".mkd" or estensione == ".markdown":
				self._elenco.append(Pagina(elemento.path))
		self._sostituzione_url_duplicati()

	def _sostituzione_url_duplicati(self):
		"""
		Controlla che fra tutte le pagine memorizzate
		non ce ne siano due con lo stesso URL. Se capita,
		cambia l'url di una delle due pagine
		"""

		modificato = False
		for indice1, pagina1 in enumerate(self._elenco):
			for indice2, pagina2 in enumerate(self._elenco):
				if indice2 != indice1 and pagina2.url == pagina1.url:
					pagina2.url += "-"
					modificato = True
				if modificato:
					break
			if modificato:
				break
		if modificato:
			self._sostituzione_url_duplicati()  # Ritenta da capo

	def __iter__(self) -> Pagina:
		"""
		Permette di eseguire un ciclo "for elemento in Pagine"
		"""

		for pagina in self._elenco:
			yield pagina

	def __str__(self):
		temp = "---\n"
		for indice, pagina in enumerate(self._elenco):
			temp += "{0:03.0f}: {1}\n".format(indice + 1, pagina.url)
		temp += "---"
		return temp
