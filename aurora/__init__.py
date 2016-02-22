from aurora.core.convertitore import Convertitore
from aurora.core.parametri import Parametri
from aurora.core.strumenti import prepara_per_url
from aurora.ext.database import Software


def crea_pagine():

	parametri = Parametri()
	parametri.aggiungi("title", "MSX Legends")
	parametri.aggiungi("footer", "&copy; 2016 Francesco Maida")

	convertitore = Convertitore(parametri)

	elenco = {"elenco": []}

	# Per ogni software nel database..
	for elemento in Software.get():

		# Prepara il nome della cartella che ospiterà la scheda
		elemento["cartella"] = prepara_per_url(elemento["titolo"])

		# Vede se il software indicato ha una schermata da mostrare
		# Per farlo vede se l'immagine è vuota o meno
		if elemento["immagine"] is not None:
			elemento["file_immagine"] = "/" + elemento["cartella"] + "/" + elemento["hash"] + ".png"
		else:
			elemento["file_immagine"] = "/img/not_found.png"

		# Ora, prepara innanzitutto una cartella per ospitare il file html

		output = convertitore.render(elemento, "default")

		# Scrive il risultato in un file "index.html" in un'altra cartella

		elenco["elenco"].append({"cartella": elemento["cartella"], "nome": elemento["titolo"]})

		cartella = parametri.cartella["output"] + elemento["cartella"]
		if not cartella.esiste():
			cartella.crea()

		# Scrive il file HTML nella cartella
		file_output = cartella.get("index.html")
		stream = open(file_output, "w")
		stream.write(output)
		stream.close()

		# Scrive l'immagine nella cartella (se necessario)
		if elemento["immagine"] is not None:
			file_output = cartella.get(elemento["hash"] + ".png")
			stream = open(file_output, "wb")
			stream.write(elemento["immagine"])
			stream.close()

	# Ed infine scrive il file index.html
	output = convertitore.render(elenco, "index")

	file_output = parametri.cartella["output"].get("index.html")
	stream = open(file_output, "w")
	stream.write(output)
	stream.close()
