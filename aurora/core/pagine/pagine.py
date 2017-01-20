import os

from aurora.core.pagine.pagina import Pagina
from aurora.core.preferenze import Preferenze, TagNonTrovato, FilePreferenzeNonTrovato


class Pagine:
    """
    Classe che gestisce una collezione di pagine di un sito
    """

    def __init__(self, p_percorso: str, p_crea_se_inesistente=True):
        """
        Costruttore della classe

        Args:
            p_percorso: Percorso alla cartella contenente le pagine (_pages)
        """

        self._percorso = p_percorso

        # Controlla se nel caso deve creare la cartella per le pagine
        if p_crea_se_inesistente:
            # Crea la cartella delle pagine se non esiste già
            if not os.path.exists(self._percorso):
                os.mkdir(self._percorso)

        self._preferenze = Preferenze()
        self._elenco = []
        self._carica_preferenze()
        self._carica_tutti()

    def aggiungi(self, p_pagina: Pagina):
        """
        Aggiunge una pagina all'elenco

        Args:
            p_pagina: Istanza di 'Pagina' da aggiungere

        Returns:
            None
        """
        self._elenco.append(p_pagina)

    def rimuovi(self, p_indice: int):
        """
        Rimuove una pagina dall'elenco

        Args:
            p_indice: Indice numerico della pagina da rimuovere

        Returns:
            None
        """
        self._elenco.remove(p_indice)

    def _carica_preferenze(self):
        """
        Verifica se esiste un file delle preferenze nella cartella indicata
        Se esiste, lo carica

        Returns:
            None
        """
        file_preferenze = os.path.join(self._percorso, "_config.yml")
        if os.path.exists(file_preferenze):
            self._preferenze = Preferenze(file_preferenze)

    def _carica_tutti(self):
        """
        Carica tutti i files presenti nella cartella indicata

        Returns:
            None
        """

        for elemento in os.scandir(self._percorso):
            nome, estensione = os.path.splitext(elemento.name)
            estensione = estensione.lower()
            if estensione == ".md" or estensione == ".mkd" \
                    or estensione == ".markdown" or estensione == ".txt":
                self._elenco.append(Pagina(elemento.path))
        self._sostituzione_url_duplicati()

    def _sostituzione_url_duplicati(self):
        """
        Controlla che fra tutte le pagine memorizzate
        non ce ne siano due con lo stesso URL. Se capita,
        cambia l'url di una delle due pagine

        Returns:
            None
        """

        modificato = False
        for indice1, pagina1 in enumerate(self._elenco):
            for indice2, pagina2 in enumerate(self._elenco):
                if indice2 != indice1 and pagina2.meta.url == pagina1.meta.url:
                    pagina2.meta.url += "-"
                    modificato = True
                if modificato:
                    break
            if modificato:
                break
        if modificato:
            self._sostituzione_url_duplicati()  # Ritenta da capo

    def __iter__(self) -> Pagina:
        """
        Permette di eseguire un ciclo "for elemento in Pagine"

        Returns:
            Un istanza della classe pagina ogni volta in cui viene richiamato
        """

        for pagina in self._elenco:
            yield pagina

    def __str__(self):
        """
        Restituisce la rappresentazione sotto forma di stringa dell'istanza

        Returns:
            str
        """
        temp = "---\n"
        for indice, pagina in enumerate(self._elenco):
            temp += "{0:03.0f}: {1}\n".format(indice + 1, pagina.url)
        temp += "---"
        return temp
