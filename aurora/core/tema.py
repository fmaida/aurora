import os
from jinja2 import FileSystemLoader, Environment
from jinja2.exceptions import TemplateNotFound

from aurora.core.preferenze \
	import Preferenze, PreferenzaNonTrovataEx, FilePreferenzeNonTrovatoEx
from aurora.core.pagine import Pagine


class Tema:
	"""
	Questa classe fa da wrapper a Jinja2 e consente di
	creare dei file HTML a partire da un template in formato HTML e dei
	parametri passati sotto forma di dizionario/oggetto
	"""

	# TODO: Cambiare il nome alla classe Pagina... dovrebbe avere un nome tipo "Convertitore" o roba simile

	def __init__(self, p_percorso_tema: str):
		"""
		Inizializza la classe passandogli subito i parametri generali
		da utilizzare per creare le pagine (roba come il nome del sito,
		il disclaimer da scrivere in ogni piè di pagina, ...)

		Args:
			p_percorso_tema (str):
				Percorso alla cartella che contiene i layout e gli asset
				per renderizzare le pagine e gli articoli con il tema

		Returns:
			None
		"""

		self._preferenze_sito = Preferenze()

		# Carica le eventuali preferenze del tema
		percorso_config = os.path.join(p_percorso_tema, "_config.yml")
		try:
			# Carica (o perlomeno tenta) il file delle preferenze _config.yml
			self._preferenze_tema = Preferenze(percorso_config)
		except FilePreferenzeNonTrovatoEx:
			# Non esiste un file _config.yml con le preferenze del tema
			# Usa quelle di default
			self._preferenze_tema = Preferenze()

		# Chiama in causa Jinja2 e gli spiega da quale
		# cartella dovrà tirarsi su i template/layout da utilizzare
		# per creare le pagine HTML
		self.jinja2 = Environment(
			loader=FileSystemLoader(p_percorso_tema),
			trim_blocks=True)

	def set_preferenze_sito(self, p_preferenze):
		self._preferenze_sito = p_preferenze

	def render(self, p_pagine: Pagine, p_layout_default: str = "default") -> str:
		"""
		Crea un file HTML a partire da un template/layout
		indicato ed utilizzando i parametri globali e
		quelli passati dall'utente.

		Args:
			p_pagine (Pagine):
				Un'istanza della classe Pagine che conterrà le pagine da convertire
			p_layout_default (String):
				Se non viene indicato nelle preferenze di una pagina,
				per il rendering utilizza questo layout

		Returns (String):
			Una stringa contenente il codice HTML della pagina
			appena costruita dal metodo
		"""

		for pagina in p_pagine:

			# Decide quale layout deve utilizzare
			# per fare il rendering della pagina
			try:
				# La pagina in questione ha nella parte YAML
				# un parametro "layout" che specifica come
				# l'utente vuole renderizzarla ?
				layout = pagina.preferenze.get("layout")
			except PreferenzaNonTrovataEx:
				# No. Allora decide il programma per l'utente.
				layout = p_layout_default

			# Fa caricare il template in memoria a Jinja2
			try:
				template = self.jinja2.get_template(layout + ".html")
			except TemplateNotFound:
				template = self.jinja2.get_template(p_layout_default + ".html")

			# Prepara il dizionario con i parametri da passare a Jinja2,
			# unendo quelli globali del sito a quelli del tema ed
			# aggiunge quelli della pagina che sta renderizzando
			preferenze = Preferenze()
			preferenze.aggiungi("site", self._preferenze_sito.get())
			preferenze.aggiungi("theme", self._preferenze_tema.get())
			preferenze.aggiungi("page", pagina.preferenze.get())
			preferenze.aggiungi("content", pagina.contenuto)

			# Renderizza la pagina e la restituisce
			yield pagina, template.render(preferenze.get())
