#import HTML5

class CodiceHTML():

    def __init__(self, p_contenuto = None):
        self.riga = []
        if not p_contenuto is None:
            self.__add__(p_contenuto)

    def __add__(self, p_aggiunta):
        if isinstance(p_aggiunta, CodiceHTML):
            for elemento in p_aggiunta.riga:
                self.riga.append((1 + elemento[0], elemento[1]))
        else:
            self.riga.append((0, p_aggiunta))
        return self

    def read(self, p_file):
        doc_file = open(p_file, "r")
        testo = doc_file.read()
        doc_file.close()
        self += testo

    def __str__(self):
        temp = ""
        for elemento in self.riga:
            temp += "\t" * elemento[0]
            temp += str(elemento[1])
            temp += "\n"
        return temp


class Tag(CodiceHTML):

    def __init__(self, p_tag, p_classi = None, p_id = None, p_contenuto = None):
        super(Tag, self).__init__()
        self.apertura = "<{0}".format(p_tag)
        if not p_classi is None:
            self.apertura += " class=\"{0}\"".format(p_classi)
        if not p_id is None:
            self.apertura += " id=\"{0}\"".format(p_id)
        self.apertura += ">"
        if not p_contenuto is None:
            self += p_contenuto
        self.chiusura = "</{0}>".format(p_tag)

    def __add__(self, p_aggiunta):
        if isinstance(p_aggiunta, Tag):
            self.riga.append((1, p_aggiunta.apertura))
            super(Tag, self).__add__(p_aggiunta)
            self.riga.append((1, p_aggiunta.chiusura))
        else:
            self.riga.append((1, p_aggiunta))
        return self

    def __str__(self):
        temp = ""
        #temp += "\t" * elemento[0]
        temp += self.apertura
        temp += "\n"
        temp += super(Tag, self).__str__()
        temp += self.chiusura
        temp += "\n"
        return temp

class Div(Tag):

    def __init__(self, p_classi = None):
        super(Div, self).__init__("div", p_classi)

class Head(Tag):

    def __init__(self, p_titolo = None):
        super(Head, self).__init__("head")
        if not p_titolo is None:
            titolo = Tag("title")
            titolo += p_titolo
            self += titolo
        self += "<meta charset=\"utf-8\"></meta>"
        self += "<link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css\">"
        self += "<link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap-theme.min.css\">"
        self += "<script src=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js\"></script>"


class Body(Tag):

    def __init__(self):
        super(Body, self).__init__("body")


class Document(Tag):

    def __init__(self, p_titolo = None):
        super(Document, self).__init__("html")
        self += Head(p_titolo)

    def export(self, p_nome_file = "index.html"):
        doc_file = open(p_nome_file, "w")
        doc_file.write(str(self))
        doc_file.close()


'''
container = Linea()
row = Linea()
col1 = Linea()
col2 = Linea()
testo1 = Linea()
testo2 = Linea()

testo1 += "Testo a sinistra"
testo2 += "testo a destra"

col1 += "<div class=\"col-md-8\">"
col1 += testo1
col1 += "</div>"

col2 += "<div class=\"col-md-4\">"
col2 += testo2
col2 += "</div>"

row += "<div class=\"row\">"
row += col1
row += col2
row += "</div>"

container += "<div class=\"container\">"
container += row
container += "</div>"

print (container)

head = Linea()
head += "<head>"
head += "\t<title>Prova</title>"
head += "\t<meta charset=\"utf-8\">"
head += "</head>"

body = Linea()
body += "<body>"
body += container
body += "</body>"

doc = Linea()
doc += "<html>"
doc += head
doc += body
doc += "</html>"

print(doc)
'''

container = Div("container")
row1 = Div("row")
row2 = Div("row")
col1 = Div("col-md-8")
col2 = Div("col-md-4")

col1 += "Testo a sinistra. "
col1.read("loremipsum.txt")
col2.read("cicerone.txt")

intestazione = Div("col-md-12")
intestazione += Tag("h1", None, None, "Ciao a tutti belli e brutti")

pie = Div("col-md-12")
pie += Tag("h4", None, None, "&copy; Francesco Maida")

row1 += intestazione

row2 += col1
row2 += col2

row3 = Div("row")
row3 += pie

container += row1
container += row2
container += row3

doc = Document()

body = Body()
body += container

doc += body
#doc += container

doc.export("index.html")

print (doc)