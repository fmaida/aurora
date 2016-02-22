from aurora.ext.database import schema


class Software:

	def __init__(self):
		pass

	@staticmethod
	def conto():
		return schema.Software.select().count()

	@staticmethod
	def get():
		"""
		Usato in un ciclo 'for elemento in Software.get() restituisce
		ogni volta un dizionario/oggetto contenente le seguenti informazioni:

		hash (hash calcolato del file)
		titolo (titolo del programma)
		sviluppatore (nome dello sviluppatore del programma)
		nazionalita (nazionalità dello sviluppatore)
		anno (anno di pubblicazione)
		descrizione (descrizione del programma)
		immagine (immagine del programma)
		"""

		query = schema.Software.select().limit(10)

		for risultato in query:

			output = {}
			output["hash"] = risultato.hash
			output["titolo"] = risultato.title
			output["sviluppatore"] = risultato.publisher
			output["nazionalita"] = risultato.country
			output["anno"] = risultato.year

			# Cerca di ottenere una descrizione
			try:
				sottoquery = schema.Manual.get(schema.Manual.base == output["hash"])
				output["descrizione"] = sottoquery.description
			except:
				output["descrizione"] = None

			# Cerca di ottenere un'immagine
			try:
				sottoquery = schema.Preview.get(schema.Preview.base == output["hash"])
				output["immagine"] = sottoquery.picture
			except:
				output["immagine"] = None

			yield output
