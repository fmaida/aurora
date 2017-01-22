### Inizialmente

La prima volta in cui lancio Aurora
voglio poter creare una cartella che
conterrà il mio progetto. Per farlo
digito il comando:

~~~~sh
aurora init <nome_del_progetto>
~~~~

Quando invio questo comando aurora dovrà
creare una cartella con il nome del progetto
che conterrà la seguente struttura:

~~~~sh
_config.yml
_pages/
_themes/
   +--- default/
          +--- css/
          +--- js/
          +--- default.html
_site/
~~~~

Cosa fanno questi files e queste cartelle:

* Il file `config.yml` è un file YAML che
  conterrà le impostazioni di funzionamento
  del mio sito web

* La cartella `_pages` conterrà le pagine
  in formato .md, .mkd, .markdown o .txt
  che dovranno essere convertite nelle
  rispettive pagine HTML da Aurora

* La cartella `_themes` conterrà un elenco
  di sottocartelle, ognuna delle quali avrà
  un tema applicabile al mio sito.
  Automaticamente viene generato il tema
  'default' da Aurora.

* La cartella `_site` conterrà il sito
  come esportato da Aurora.

### La conversione effettuata da Aurora

Aurora automaticamente cerca la cartella
`_pages` nella root del progetto e quindi
la scansiona alla ricerca di sottocartelle
o di file che terminano con l'estensione
.md, .mkd, .markdown e .txt. Se uno di questi
files viene trovati viene marcato per la
conversione in formato HTML.

Qualunque altro file trovato all'interno
della cartella _pages viene considerato come
fosse un file statico e viene copiato
automaticamente così com'è nella cartella di
output `_site` mantenendo la gerarchia:

Esempi di questo:

~~~~sh
logo.png --> _site/logo.png
cartella/musica.mp3 --> _site/cartella/musica.mp3
_pages/immagine.jpg --> _site/immagine.jpg
_pages/copertina/video.mov --> _site/copertina/video.mov
_pages/articolo01/foto1.jpg --> _site/articolo01/foto1.jpg
_pages/articolo02/foto1.jpg --> _site/articolo02/foto1.jpg
~~~~

Posso specificare nel file `_config.yml` che una
cartella presente nella root non deve essere considerata come
una collezione di file statici ma bensì come una cartella all'interno
della quale cercare gli articoli.

 Esempio:

 ~~~~yaml
 folders: ['_pages', 'collezione1', 'galleria']
 ~~~~


 ### Tema da usare per la conversione

 Posso indicare quale tema utilizzare per
 la conversione indicandolo nel file
 `_config.yml` in questo modo:

 ~~~~yaml
 theme: default
 ~~~~

 In questo caso Aurora durante la conversione
 andrà a prendersi i  files contenuti nella
 cartella `_themes/default/`.

  Ogni pagina può venire convertita con uno o più
  layout contenuti nella definizione della pagina.
  Ad esempio questo file `articolo.md` contiene:

  ~~~~yaml
  ----
  title: Il mio articolo
  layout: una_colonna
  ----

  # Lorem ipsum

  Lorem ipsum dolor sit amet...
  ~~~~

  In questo caso Aurora andrà a cercare il
  layout denominato `una_colonna` all'interno
  della cartella del tema indicata nel file `_config.yml`,
  e cioè 'default' nel nostro esempio precedente, e questo
  significa che andrà a cercarsi il file `_theme/default/una_colonna.html`

  Posso anche indicare l'autore di default all'interno del file `_config.yml`,
  e così in ogni articolo in cui manchi questa informazione Aurora la prenderebbe
  quedal file di configurazione.
