from jinja2 import FileSystemLoader, Environment


class Convertitore:
	"""
	Questa classe fa da wrapper a Jinja2 e consente di
	creare dei file HTML a partire da un template in formato HTML e dei
	parametri passati sotto forma di dizionario/oggetto
	"""
	# TODO: Cambiare il nome alla classe Pagina... dovrebbe avere un nome tipo "Convertitore" o roba simile

	def __init__(self, p_parametri):
		"""
		Inizializza la classe passandogli subito i parametri generali
		da utilizzare per creare le pagine (roba come il nome del sito,
		il disclaimer da scrivere in ogni piè di pagina, ...)

		Args:
		    p_parametri (Parametri):
		    	istanza della classe Parametri

		Returns:
		    None
		"""

		# Imposta i parametri generali
		self.parametri = p_parametri

		# Chiama in causa Jinja2 e gli spiega da quale
		# cartella dovrà tirarsi su i template/layout da utilizzare
		# per creare le pagine HTML
		self.jinja2 = Environment(
			loader=FileSystemLoader(self.parametri.cartella["layout"].get()),
			trim_blocks=True)

	def get_parametri(self):
		"""
		Restituisce un'instanza della classe Parametri

		Returns:
		    Parametri
		"""
		return self.parametri

	def set_parametri(self, p_parametri):
		"""
		Imposta i parametri globali, sostituendo l'istanza
		della classe Parametri che mantiene al proprio
		interno con una nuova

		Args:
		    p_parametri (Parametri):
		    	La nuova istanza di Parametri da utilizzare
		    	per i parametri globali di funzionamento
		"""

		self.parametri = p_parametri

	def render(self, p_parametri, p_template=None):
		"""
		Crea un file HTML a partire da un template/layout
		indicato ed utilizzando i parametri globali e
		quelli passati dall'utente.

		Args:
		    p_parametri (Dict):
		    	Dizionario contenente tutti i parametri necessari
		    	alla creazione di una pagina HTML (ad esempio
		    	il titolo dell'intestazione della pagina ed il testo
		    	da scrivere all'interno della pagina). Questi parametri
		    	verranno aggiunti ai parametri generali memorizzati in
		    	self.parametri
		    p_template (String):
		    	Stringa che contiene il nome del template da utilizzare
		    	per renderizzare la pagina, senza estensione ".html".
		    	Ad esempio "default.html" -> "default"

		Returns (String):
		    Una stringa contenente il codice HTML della pagina
		    appena costruita dal metodo
		"""

		# Pigliati su il layout indicato dall'utente
		if p_template is None:
			# Se l'utente non ha voluto indicare nulla,
			# piglia quello di default
			p_template = "default"

		# Fa caricare il template in memoria a Jinja2
		template = self.jinja2.get_template(p_template + ".html")

		# Prepara il dizionario con i parametri da passare a Jinja2,
		# unendo quelli base per fare il sito (contenuti in
		# self.parametri) con quelli passati in p_parametri
		parametri = self.parametri.render()
		parametri.update(p_parametri)

		# Renderizza la pagina e la restituisce
		return template.render(parametri)
