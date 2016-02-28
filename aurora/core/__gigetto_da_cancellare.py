import os

from aurora.core.cartelle import Cartella


class Parametri:

	def __init__(self):
		self._opzioni = {}
		self.cartella = dict()
		self.cartella["base"] = Cartella(os.getcwd())
		self.cartella["layout"] = self.cartella["base"] + "_layout"
		self.cartella["output"] = self.cartella["base"] + "_site"

	def aggiungi(self, p_parametro, p_valore):


		self._opzioni[p_parametro] = p_valore

	def get(self, p_parametro):
		return self._opzioni[p_parametro]

	def render(self):
		out = dict()
		out["site"] = self._opzioni
		return out
