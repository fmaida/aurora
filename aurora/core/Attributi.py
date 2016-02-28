import yaml


class TagNonTrovato(Exception):
	pass


class FilePreferenzeNonTrovato(Exception):
	pass


class Attributi:

	def __init__(self, p_file_yaml: str = None):
		self._preferenze = dict()
		if p_file_yaml is not None:
			try:
				with open(p_file_yaml) as f:
					self.importa(f.read())
				f.close()
			except FileNotFoundError:
				raise FilePreferenzeNonTrovato

	def importa(self, p_testo_yaml: str):
		self._preferenze = yaml.load(p_testo_yaml)

	def __getattr__(self, p_elemento: str):
		try:
			return self._preferenze[p_elemento]
		except KeyError:
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
