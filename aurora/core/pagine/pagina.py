import os
import markdown2
import unicodedata

from aurora.core.preferenze import Preferenze, TagNonTrovato


class Pagina:
    """
    Questa classe gestisce una pagina
    """

    def __init__(self, p_file):
        self.meta = Preferenze()
        self.contenuto = ""
        self.importa(p_file)

    def importa(self, p_file):
        with open(p_file) as f:
            leggi_yaml = False
            parte_yaml = ""
            parte_testo = ""
            for riga in f:
                if riga[:3] == "---" and riga[-1:] == "\n":
                    leggi_yaml = not leggi_yaml
                else:
                    if leggi_yaml:
                        parte_yaml += riga
                    else:
                        parte_testo += riga
            f.close()

        self.meta.importa_da_testo(parte_yaml)
        self.contenuto = markdown2.markdown(parte_testo)
        try:
            # Se l'articolo / pagina ha una proprietà "title" da usare..
            titolo = self.meta.title
            self.meta.url = self.decidi_url(titolo)
        except TagNonTrovato:
            # Altrimenti come nome usa quello del file senza estensione
            nome, estensione = os.path.splitext(os.path.basename(p_file))
            self.meta.url = self.decidi_url(nome)

    @staticmethod
    def decidi_url(p_nome):
        # Rimuove tutte le accentate e le sostituisce con caratteri ASCII
        nfkd_form = unicodedata.normalize('NFKD', p_nome)
        temp = u"".join([c for c in nfkd_form if not unicodedata.combining(c)])
        # Sostituisce gli spazi e altri caratteri con delle lineette
        temp = temp.lower().replace(chr(32), "-") \
            .replace(".", "-").replace(",", "-") \
            .replace(";", "-").replace(":", "-") \
            .replace("'", "-").replace(chr(34), "-")
        # Elimina i casi in cui ci sono due o tre lineette di seguito
        temp = temp.replace("---", "-").replace("--", "-")
        # Restituisce la stringa modificata
        return temp

    def __str__(self) -> str:
        temp = "FILE: {0}\n".format(self.url)
        temp += str(self.meta)
        temp += self.meta.content
        return temp

    # def metodo2(self, p_file):
    # 	with open(p_file) as f:
    # 		testo = f.read()
    #
    #	import re
    #	pattern = re.compile("([\-]{3,}[.\s\S]*[\-]{3,})([.\s\S]*)")  # /gm
    #	ricerca = re.match(pattern, testo)
    #	parte_yaml = ricerca.group(1)
    #	parte_testo = ricerca.group(2)
    #	f.close()
    #	return parte_yaml, parte_testo
