import os
from aurora.core.pagine import Pagina, Pagine
from aurora.core.tema import Tema
from aurora.core.preferenze import Preferenze, TagNonTrovato
from aurora.core.output import Output


class Progetto:
    """
    Questa classe gestisce un progetto creato con Aurora
    """

    def __init__(self, p_percorso):
        self.basedir = p_percorso

        # Carica le preferenze del sito
        preferenze = Preferenze(os.path.join(self.basedir, "_config.yml"))

        # Carica le pagine da convertire
        self.lista = Pagine(os.path.join(self.basedir, "_pages"))

        # Carica il tema da utilizzare
        try:
            nome_tema = preferenze.theme
        except TagNonTrovato:
            nome_tema = "default"

        percorso_cartella_temi = os.path.join(self.basedir, "_themes")

        if not os.path.exists(percorso_cartella_temi):
            os.mkdir(percorso_cartella_temi)

        percorso_tema = os.path.join(percorso_cartella_temi, nome_tema)

        if not os.path.exists(percorso_tema):
            os.mkdir(percorso_tema)

        self.tema = Tema(percorso_tema)
        self.tema.set_preferenze_sito(preferenze)

    def render(self):

        # Crea i file di output
        percorso_output = os.path.join(self.basedir, "_site")
        if not os.path.exists(percorso_output):
            os.mkdir(percorso_output)
        out = Output(percorso_output)

        out.set_tema(self.tema)
        out.render(self.lista, "page")
