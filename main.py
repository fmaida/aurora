import os
import pathlib


def verifica_dipendenze():

    # Installa pyjade se è necessario
    try:
        import pyjade
    except ImportError:
        import pip
        pip.main(["install", "pyjade", "-q"])

    # Installa pyyaml se è necessario
    try:
        import pyyaml
    except ImportError:
        import pip
        pip.main(["install", "pyyaml", "-q"])

def inizializza():

    def crea_cartella(p_cartella):
        path = pathlib.Path(p_cartella)
        if not path.is_dir():
            os.mkdir(p_cartella)

    crea_cartella("_includes")
    crea_cartella("_layouts")
    crea_cartella("_posts")
    crea_cartella("_pages")
    crea_cartella("_site")





print(os.getcwd())
# inizializza()