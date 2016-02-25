import yaml


class PreferenzaNonTrovataEx(Exception):
	pass


class FilePreferenzeNonTrovatoEx(Exception):
	pass


class Preferenze:

	def __init__(self, p_file_yaml: str = None):
		self._preferenze = dict()
		if p_file_yaml is not None:
			try:
				with open(p_file_yaml) as f:
					self.importa(f.read())
				f.close()
			except FileNotFoundError:
				raise FilePreferenzeNonTrovatoEx

	def importa(self, p_testo_yaml: str):
		self._preferenze = yaml.load(p_testo_yaml)

	def get(self, p_elemento: str = None):
		if p_elemento is None:
			return self._preferenze
		else:
			try:
				return self._preferenze[p_elemento]
			except KeyError:
				raise PreferenzaNonTrovataEx

	def aggiungi(self, p_elemento: str, p_valore):
		self._preferenze[p_elemento] = p_valore

	def __str__(self) -> str:
		temp = "---\n"
		for elemento in self._preferenze:
			temp += elemento + ": " + str(self._preferenze[elemento]) + "\n"
		temp += "---"
		return temp
