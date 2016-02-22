from aurora.core.pagine.pagina import Pagina


class Pagine:

	def __init__(self):
		self.elenco = []

	def aggiungi(self, p_pagina):
		self.elenco.append(Pagina(p_pagina))
