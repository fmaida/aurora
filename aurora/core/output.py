import os

from aurora.core.preferenze import Preferenze, TagNonTrovato
from aurora.core.tema import Tema
from aurora.core.pagine import Pagine, Pagina


class Output:
    """
    Classe che gestisce l'output del sito in formato HTML e CSS
    """

    def __init__(self, p_cartella_output: str):
        """
        Costruttore della classe

        Args:
            p_cartella_output: Cartella in cui esportare i file HTML, CSS e JS
        """

        self._cartella_output = p_cartella_output
        self.tema = None

    def set_tema(self, p_tema: Tema):
        """
        Imposta il tema da utilizzare per esportare su file HTML, CSS e JS il sito

        Args:
            p_tema: Un'instanza della classe 'Tema' da utilizzare allo scopo

        Returns:
            None
        """
        self.tema = p_tema

    def set_output_su_file(self):
        pass

    def set_output_su_cartelle(self):
        pass

    def _get_percorso_file_output(self, p_nome_file):
        return os.path.join(self._cartella_output, p_nome_file)

    def render(self, p_pagine: Pagine, p_layout_default: str = "default"):
        """
        Esegue l'esportazione

        Args:
            p_pagine: Le pagine da esportare
            p_layout_default: Il layout da utilizzare per l'esportazione

        Returns:
            None
        """

        for pagina in p_pagine:
            output = self.tema.render(pagina, p_layout_default)
            with open(self._get_percorso_file_output(pagina.meta.url + ".html"), "w") as f:
                f.write(output)
                f.close()
