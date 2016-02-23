import yaml
import mistune


class Pagina:
	"""
	Questa classe gestisce una pagina
	"""

	def __init__(self, p_file):

		parte_yaml, parte_testo = self.metodo2(p_file)

		# print(list(yaml.load_all(parte_yaml))[0])
		# print("\n\n")
		# print(mistune.markdown(parte_testo))

	def metodo1(self, p_file):
		with open(p_file) as f:
			leggi_yaml = False
			parte_yaml = ""
			parte_testo = ""
			testo = f.readline()
			while testo != "":
				if testo == "---\n":
					if not leggi_yaml:
						parte_yaml += testo
						leggi_yaml = True
					else:
						parte_yaml += testo
						leggi_yaml = False
				else:
					if leggi_yaml:
						parte_yaml += testo
					else:
						parte_testo += testo
				testo = f.readline()
			f.close()
		return parte_yaml, parte_testo

	def metodo2(self, p_file):
		with open(p_file) as f:
			testo = f.read()

		import re
		pattern = re.compile("[\-]{3,}(.|[\r\n])+[\-]{3,}")  # /gm
		parte_yaml = re.match(pattern, testo)
		print(str(parte_yaml.group(2)))
		f.close()
		return parte_yaml, None  # parte_testo
