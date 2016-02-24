import yaml
import mistune


class Pagina:
	"""
	Questa classe gestisce una pagina
	"""

	def __init__(self, p_file):

		parte_yaml, parte_testo = self.metodo1(p_file)

		print("PARTE YAML:\n{0}".format(str(parte_yaml)))
		print()
		print(parte_testo)

	def metodo1(self, p_file):
		with open(p_file) as f:
			leggi_yaml = False
			parte_yaml = ""
			parte_testo = ""
			for riga in f:
				if riga == "---\n":
					leggi_yaml = not leggi_yaml
				else:
					if leggi_yaml:
						parte_yaml += riga
					else:
						parte_testo += riga
			f.close()
		return yaml.load(parte_yaml), mistune.markdown(parte_testo)

	def metodo2(self, p_file):
		with open(p_file) as f:
			testo = f.read()

		import re
		pattern = re.compile("([\-]{3,}[.\s\S]*[\-]{3,})([.\s\S]*)")  # /gm
		ricerca = re.match(pattern, testo)
		parte_yaml = ricerca.group(1)
		parte_testo = ricerca.group(2)
		f.close()
		return parte_yaml, parte_testo
