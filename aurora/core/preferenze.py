import os
import yaml


class TagNonTrovato(Exception):
    pass


class FilePreferenzeNonTrovato(Exception):
    pass


class FilePreferenzeCorrotto(Exception):
    pass


class Preferenze:
    """
    Questa classe gestisce il file di configurazione del sito (_config.yml)
    """

    def __init__(self, p_file_yaml: str = None, p_crea_se_inesistente: bool = False):
        """
        Costruttore della classe

        Args:
            p_file_yaml: Il file in formato YAML
                         con la configurazione da aprire
        """

        self._preferenze = dict()
        # Se il file di configurazione è stato passato..
        if p_file_yaml is not None:
            # ..verifica se il suddetto file esiste
            try:
                self.importa(p_file_yaml)
            except (FileNotFoundError, FilePreferenzeCorrotto) as e:
                if p_crea_se_inesistente:
                    # Il file non esiste. Lo crea
                    f = open(p_file_yaml, "w")
                    f.write()
                    f.close()
                    # Riprova
                    self.importa(p_file_yaml)
                else:
                    raise FilePreferenzeNonTrovato

    def importa(self, p_file_yaml: str):
        """
        Importa un file di configurazione (_config.yml)

        Args:
            p_file_yaml: Il percorso al file da aprire

        Returns:
            None
        """
        try:
            if os.path.exists(p_file_yaml):
                f = open(p_file_yaml, "r")
                testo_yaml = f.read()
                f.close()
                self.importa_da_testo(testo_yaml)
            else:
                raise FileNotFoundError
        except:
            raise FilePreferenzeCorrotto

    def importa_da_testo(self, p_testo_yaml):
        self._preferenze = yaml.load(p_testo_yaml)

    def __getattr__(self, p_elemento: str):
        """
        Restituisce un elemento quando richiesto come preferenze.elemento

        Args:
            p_elemento:
                Il nome dell'elemento richiesto
        Returns:
            Il valore dell'elemento richiesto
        """

        try:
            return self._preferenze[p_elemento]
        except KeyError:
            raise TagNonTrovato
        except TypeError:
            raise TagNonTrovato

    def __setattr__(self, p_elemento: str, p_valore):
        if p_elemento != "_preferenze":
            self._preferenze[p_elemento] = p_valore
        else:
            super().__setattr__(p_elemento, p_valore)

    def esporta(self):
        return self._preferenze

    def __getitem__(self, p_elemento):
        return self._preferenze[p_elemento]

    def __setitem__(self, p_elemento, p_valore):
        self._preferenze[p_elemento] = p_valore

    def __str__(self) -> str:
        temp = "---\n"
        for elemento in self._preferenze:
            temp += elemento + ": " + str(self._preferenze[elemento]) + "\n"
        temp += "---"
        return temp
