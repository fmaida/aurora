import os

from aurora.core.pagine import Pagina, Pagine
from aurora.core.tema import Tema
from aurora.core.permalink import Permalink
from aurora.core.preferenze import Preferenze, PreferenzaNonTrovataEx

# crea_pagine()
#a = Pagina("_pages/prova.md")
#print(a)
preferenze = Preferenze("_config.yml")
lista = Pagine("_pages")

try:
	nome_tema = preferenze.get("theme")
except PreferenzaNonTrovataEx:
	nome_tema = "default"

percorso_tema = os.path.join("_themes", nome_tema)
tema = Tema(percorso_tema)
tema.set_preferenze_sito(preferenze)
permy = Permalink("_site")
permy.set_tema(tema)
permy.render(lista, "page")
