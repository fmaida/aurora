import os

from aurora.core.pagine import Pagina, Pagine
from aurora.core.tema import Tema
from aurora.core.output import Output
from aurora.core.attributi import Attributi, TagNonTrovato

# Carica le preferenze del sito
preferenze = Attributi("_config.yml")

# Carica le pagine da convertire
lista = Pagine("_pages")

# Carica il tema da utilizzare
try:
	nome_tema = preferenze.theme
except TagNonTrovato:
	nome_tema = "default"
percorso_tema = os.path.join("_themes", nome_tema)
tema = Tema(percorso_tema)
tema.set_preferenze_sito(preferenze)

# Crea i file di output
out = Output("_site")
out.set_tema(tema)
out.render(lista, "page")
