# Benvenuti nella documentazione di Aurora

#### Cosa sarà un giorno Aurora ?
  
Aurora sarà un piccolo generatore di siti web statici (un static site generator per dirla all'inglese..) basato su python, pyjade e l'utilizzo di twitter bootstrap. L'idea di fondo è che sfruttando Bootstrap, il programma cercherà di creare dei siti internet e delle piccole pagine limitate *ma* con realizzabili con poco sforzo.

Non sarà mai un generatore con fiocchi e controfiocchi come [Jekyll](http://jekyllrb.com) o [Pelican](http://www.getpelican.com), ma nei miei desideri dovrebbe essere sufficiente a realizzare con poco sforzo molte belle cosucce e supporterà da subito Jade anzichè HTML.

#### Cosa dovrebbe implementare Aurora ?

* **Utilizzo dei file in formato .jade** al posto del formato .html per la generazione delle pagine
* **Supporto multilingua per le pagine** in modo che ogni pagina possa avere una o più traduzioni in altre lingue

#### Come dovrebbe venire implementato il supporto multilingua per le pagine ?

Io pensavo ad un sistema che sia una via di mezzo fra il Front Matter in formato YAML di Jekyll e le direttive usate da Pelican per gestire le traduzioni. In ogni file contenente i testi di una pagina ci dovrebbe essere una sezione iniziale in formato YAML Front Matter contenente dei meta-dati, fra cui:

* Titolo della pagina
* Nome dell'autore della pagina
* Data di creazione/ultima modifica
* Tags associati alla pagina
* Lingua in cui sono scritti i contenuti della pagina
* Ordine con cui dovrebbe essere processata la pagina (1 = Prima pagina da processare, 2 = Seconda, ...)
* Riferimento all'articolo originale, in modo che Aurora possa capire che un file contiene la traduzione di un'altro file. Per utilizzare lo stesso nome dato al campo da Pelican, io lo chiamerei "slug". Il campo "slug" fa riferimento al titolo della pagina, con gli spazi sostituiti da lineette.

Ovviamente l'inserimento di tutti questi meta-dati dovrebbe essere del tutto opzionale.

#### Puoi fare un'esempio di come dovrebbe essere scritta una pagina ?

Certo:

**File N.1 :** _pages/it/chi_sono.md
~~~~jade
---
title: Chi sono
date: 2016-02-16 16:36
language: it
slug: chi-sono
---

# Benvenuti

Questo è il mio sito ed il mio nome è Francesco!
~~~~

**File N.2 :** _pages/en/who_i_am.md
~~~~jade
---
title: Who I am
date: 2016-02-16 18:54
language: en
slug: chi-sono
---

# Welcome

This is my website and my name is Francesco!
~~~~

Nota che i campi slug sia nel file "italiano" che in quello "inglese" hanno lo stesso valore ("chi-sono"), ad indicare qual'è il file originale.

#### Quali sono le dipendenze per far funzionare Aurora ?

Aurora attualmente necessità di queste librerie esterne Python:

* Jinja2 (>= 2.9.4)
* PyYAML (>= 3.12)
* markdown2 (>= 2.3.2)
