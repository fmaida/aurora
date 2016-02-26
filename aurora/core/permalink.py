import os

from aurora.core.preferenze import Preferenze, PreferenzaNonTrovataEx
from aurora.core.tema import Tema
from aurora.core.pagine import Pagine, Pagina


class Permalink:

	def __init__(self, p_cartella_output: str):
		self._cartella_output = p_cartella_output
		self.tema = None

	def set_tema(self, p_tema: Tema):
		self.tema = p_tema

	def set_output_su_file(self):
		pass

	def set_output_su_cartelle(self):
		pass

	def _get_percorso_file_output(self, p_nome_file):
		return os.path.join(self._cartella_output, p_nome_file)

	def render(self, p_pagine: Pagine, p_layout_default: str = "default"):

		output = ""
		for pagina in p_pagine:
			output = self.tema.render(pagina, p_layout_default)
			with open(self._get_percorso_file_output(pagina.url + ".html"), "w") as f:
				f.write(output)
				f.close()
