# TP et projets

<p class="sous-titre">Recherche textuelle</p>

## <span class="etiquette">TP</span> La course des algorithmes de recherche

*compter, chronométrer et comparer naïf, Horspool et `str.find`*

<p class="infos-activite">Durée : 2 h 30 à 3 h (deux séances) · Sur machine, par deux</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/12-tp-recherche-textuelle){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-12-tp-recherche-textuelle.zip){ .md-button }

!!! consignes "Consignes"

    - Fichier à télécharger (lien ci-dessus) : `tp_recherche_depart.py` (outils, squelettes et tests). Le lancer affiche l’état des tests.

    - Texte d’étude : *Le Tour du monde en quatre-vingts jours* de Jules Verne (1872), **domaine public**. Le télécharger sur `gutenberg.org` (chercher le titre, choisir le format « Plain Text UTF-8 ») et l’enregistrer sous le nom `verne.txt`, dans le dossier du fichier Python. *Sans connexion : faire les parties C à E sur le génome seul.*

    - Niveau : ★ échauffement, ★★ classique (niveau bac), ★★★ défi ; les *coups de pouce* et les *corrigés* se déplient sous chaque exercice. Le symbole <span class="run" title="À programmer et tester sur machine">▶</span>  signale ce qui est à programmer et tester.

    - Usage de l’IA, indiqué sur chaque exercice : <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> aucune ; <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> en appui (déboguer, reformuler, vérifier ; la réponse finale est écrite et comprise par vous) ; <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> l’exercice s’appuie sur une réponse d’IA. Voir la [charte d’usage de l’IA](../charte.md).

!!! encadre "But du TP"

    Transformer les algorithmes du cours en **instruments de mesure** : chaque recherche renverra, en plus des positions trouvées, le **nombre de comparaisons de caractères** effectuées. On fera ensuite courir la méthode naïve et Boyer-Moore-Horspool sur un **vrai roman** et sur un **génome** d’un million de bases, on étudiera l’effet de la **longueur du motif** et de la **taille de l’alphabet**, on construira des **cas défavorables**, et on se mesurera à la méthode `find` de Python. *Produit final* : des tableaux de mesures et un bilan argumenté sur le coût de la recherche textuelle.

**Convention de comptage.** On compte **une comparaison** chaque fois qu’un caractère du texte est comparé à un caractère du motif, que la comparaison réussisse ou échoue.

## Partie A — Compter le travail

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 1</span> — La méthode naïve, avec compteur <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-recherche-textuelle-tp-1-1 }

1.  À la main : combien de comparaisons la méthode naïve fait-elle pour chercher `ACG` dans `CAAGACG` ? (Reprendre le schéma du cours : $5$ alignements.)

2.  <span class="run" title="À programmer et tester sur machine">▶</span>  Compléter `naive_compte(motif, texte)`, qui renvoie le couple `(positions, comparaisons)`. Pour compter aussi la comparaison qui échoue, on peut écrire la boucle intérieure ainsi :

    ```python
            j = 0
            while j < m and texte[i + j] == motif[j]:
                comp += 1                   # comparaison reussie
                j += 1
            if j < m:
                comp += 1                   # la comparaison qui a echoue
    ```

    Vérifier : `naive_compte("ACG", "CAAGACG")` vaut `([4], 9)`.

??? corrige "Corrigé"

    - Texte ordinaire : naïf $\approx n$ comparaisons ($1{,}0$ à $1{,}1\,n$ en français, $1{,}33\,n$ sur l’ADN) ; Horspool $\approx n/m$ (sous-linéaire). Pire cas : les deux en $n \times m$ (tableau de la partie D).

    - Plus le motif est long, plus les sauts (jusqu’à $m$) sont grands. Sur l’ADN, les quatre lettres sont toutes près de la fin du motif : les sauts restent petits et le gain plafonne vers $0{,}4\,n$.

    - Le prétraitement (la table) coûte une seule passe sur le motif ($m$ opérations), négligeable devant la recherche dans un texte de $n \gg m$ caractères : on dépense un peu de mémoire pour gagner beaucoup de temps.

    - `find` est compilé et optimisé : on l’utilise en pratique. Programmer Horspool sert à **comprendre** pourquoi il est rapide, et quand il ne l’est pas.

    **1.** $i=0$ : $1$ (`A`$\neq$`C`) ; $i=1$ : $2$ ; $i=2$ : $2$ ; $i=3$ : $1$ ; $i=4$ : $3$ (trouvé). Total : **9 comparaisons**.

    **2.**

    ```python
    def naive_compte(motif, texte):
        n = len(texte)
        m = len(motif)
        positions = []
        comp = 0
        for i in range(n - m + 1):
            j = 0
            while j < m and texte[i + j] == motif[j]:
                comp += 1                   # comparaison reussie
                j += 1
            if j < m:
                comp += 1                   # la comparaison qui a echoue
            else:
                positions.append(i)
        return positions, comp
    ```

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 2</span> — Horspool, avec compteur <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-recherche-textuelle-tp-1-2 }

1.  À la main : dérouler Horspool pour `ACG` dans `CAAGACG` (table : `A`$\to 2$, `C`$\to 1$, autres $\to 3$). Combien d’alignements ? Combien de comparaisons ?

2.  <span class="run" title="À programmer et tester sur machine">▶</span>  Compléter `horspool_compte(motif, texte)` (même principe, comparaison de **droite à gauche** ; la fonction `table_decalage` est fournie). Vérifier les tests, dont l’exemple `MOTIF` du cours : combien de comparaisons pour Horspool ? et pour la méthode naïve ?

??? corrige "Corrigé"

    **1.** $i=0$ : fenêtre `CAA`, `G`$\neq$`A` ($1$ comparaison), fin `A` $\to$ saut $2$ ; $i=2$ : fenêtre `AGA`, $1$ comparaison, fin `A` $\to$ saut $2$ ; $i=4$ : `ACG`, $3$ comparaisons, trouvé ; fin `G` (absente de la table) $\to$ saut $3$, $i=7$ : fin. **3 alignements, 5 comparaisons**.

    **2.**

    ```python
    def horspool_compte(motif, texte):
        n = len(texte)
        m = len(motif)
        dec = table_decalage(motif)
        positions = []
        comp = 0
        i = 0
        while i <= n - m:
            j = m - 1
            while j >= 0 and texte[i + j] == motif[j]:
                comp += 1                   # comparaison reussie
                j -= 1
            if j >= 0:
                comp += 1                   # la comparaison qui a echoue
            else:
                positions.append(i)
            i += dec.get(texte[i + m - 1], m)
        return positions, comp
    ```

    Exemple `MOTIF` du cours : **9** comparaisons pour Horspool ($4$ échecs immédiats puis $5$), **26** pour la méthode naïve.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 3</span> — Une référence, et mille tests <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-recherche-textuelle-tp-1-3 }

1.  <span class="run" title="À programmer et tester sur machine">▶</span>  Compléter `toutes_positions(motif, texte)` à l’aide de `texte.find(motif, debut)`, qui renvoie la première position du motif à partir de l’indice `debut`, ou $-1$ s’il est absent. Attention : les occurrences peuvent se **chevaucher** (`AA` est trois fois dans `AAAA`).

    ??? pouce "Coup de pouce"

        Chercher une première fois à partir de $0$ ; tant que le résultat `p` n’est pas $-1$, l’ajouter à la liste et relancer la recherche à partir de `p + 1` (et non `p + len(motif)`, à cause des chevauchements).

2.  <span class="run" title="À programmer et tester sur machine">▶</span>  Écrire une boucle de **$1\,000$ tests aléatoires** : texte de longueur $0$ à $30$ et motif de longueur $1$ à $5$, tous deux sur l’alphabet `"AB"` (avec `random.choice` et `random.randint`). À chaque tour, vérifier par un `assert` que les trois fonctions renvoient les mêmes positions. Pourquoi un alphabet de deux lettres est-il un bon choix pour ces tests ?

??? corrige "Corrigé"

    ```python
    def toutes_positions(motif, texte):
        positions = []
        p = texte.find(motif)
        while p != -1:
            positions.append(p)
            p = texte.find(motif, p + 1)     # p + 1 : chevauchements permis
        return positions

    def mot_aleatoire(longueur):
        mot = ""
        for k in range(longueur):
            mot = mot + random.choice("AB")
        return mot

    for k in range(1000):
        texte = mot_aleatoire(random.randint(0, 30))
        motif = mot_aleatoire(random.randint(1, 5))
        ref = toutes_positions(motif, texte)
        assert naive_compte(motif, texte)[0] == ref
        assert horspool_compte(motif, texte)[0] == ref
    ```

    Avec deux lettres seulement, le motif apparaît **souvent**, avec beaucoup de correspondances partielles et de chevauchements : ce sont les situations délicates, celles où se cachent les erreurs d’indice. Sur un alphabet de $26$ lettres, presque tous les tests seraient des « absent » sans intérêt. (Les tests passent sans erreur.)

## Partie B — Un vrai roman

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 4</span> — À la recherche de Phileas Fogg <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-recherche-textuelle-tp-1-4 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Charger le roman avec `texte = lire_texte("verne.txt")` et afficher sa longueur $n$.

1.  <span class="run" title="À programmer et tester sur machine">▶</span>  Recopier et compléter le tableau ($n$ est le nombre de caractères du texte) :

| **Motif** | **Occurrences** | **Comp. naïf** | **Comp. Horspool** | **Rapport naïf / Horspool** |
|:---|:--:|:--:|:--:|:--:|
| `Fix` |  |  |  |  |
| `Fogg` |  |  |  |  |
| `Aouda` |  |  |  |  |
| `Passepartout` |  |  |  |  |
| `quatre-vingts jours` |  |  |  |  |

1.  Le nombre de comparaisons de la méthode naïve dépend-il beaucoup du motif ? Comparer à $n$. Et celui de Horspool ?

2.  Pourquoi Horspool fait-il **moins de comparaisons qu’il n’y a de caractères** dans le texte ? Quels caractères n’a-t-il jamais lus ?

3.  <span class="run" title="À programmer et tester sur machine">▶</span>  Chercher `fogg` (sans majuscule). Que se passe-t-il ? Comment chercher un mot « sans tenir compte des majuscules » ? (Penser à `lower()`.)

??? corrige "Corrigé"

    **1.** Mesures sur `verne.txt` ($n = 440\,824$ caractères, fichier Gutenberg complet) :

    | **Motif ($m$)** | **Occ.** | **Comp. naïf** | **Comp. Horspool** | **Rapport** |
    |:---|:--:|:--:|:--:|:--:|
    | `Fix` ($3$) | $275$ | $1{,}00\,n$ | $0{,}35\,n$ | $2{,}9$ |
    | `Fogg` ($4$) | $655$ | $1{,}01\,n$ | $0{,}27\,n$ | $3{,}8$ |
    | `Aouda` ($5$) | $136$ | $1{,}00\,n$ | $0{,}23\,n$ | $4{,}4$ |
    | `Passepartout` ($12$) | $423$ | $1{,}01\,n$ | $0{,}13\,n$ | $7{,}6$ |
    | `quatre-vingts jours` ($19$) | $18$ | $1{,}02\,n$ | $0{,}10\,n$ | $10{,}3$ |

    **2.** Le naïf fait toujours un peu plus de $n$ comparaisons, quel que soit le motif : presque toutes les positions échouent dès la première lettre (ici une majuscule ou une lettre peu fréquente), quelques-unes à la deuxième. Horspool en fait de moins en moins quand le motif s’allonge (de l’ordre de $n/m$, un peu plus pour les motifs courts).

    **3.** À chaque échec, il saute souvent de $m$ caractères (ou presque) : les caractères **survolés** lors des sauts ne sont jamais comparés.

    **4.** `fogg` n’est pas trouvé (ou presque pas) : la recherche distingue majuscules et minuscules (`"F" != "f"`). On cherche `"fogg"` dans `texte.lower()` (et on met aussi le motif en minuscules). Dans le roman : `fogg` $0$ fois, `Fogg` $655$ fois, et $685$ fois dans `texte.lower()` (les $30$ de plus sont écrits en capitales, `FOGG`, dans les titres de chapitres).

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 5</span> — Un mini-`grep` <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-recherche-textuelle-tp-1-5 }

La commande `grep` des systèmes Unix affiche les **lignes** d’un fichier qui contiennent un motif. On en écrit une version Python, fondée sur Horspool.

1.  <span class="run" title="À programmer et tester sur machine">▶</span>  Écrire `grep(motif, texte)`, qui découpe le texte en lignes (`texte.split("\n")`) et renvoie la liste des couples `(numéro de ligne, ligne)` des lignes contenant le motif (la première ligne porte le numéro $1$). Afficher les cinq premières lignes du roman qui contiennent `Passepartout`.

2.  <span class="run" title="À programmer et tester sur machine">▶</span>  Écrire `surligner(motif, ligne)`, qui renvoie la ligne où chaque occurrence du motif est entourée de crochets. Exemple : `surligner("ab", "xxabyyab")` renvoie `"xx[ab]yy[ab]"`. Que choisir quand deux occurrences se chevauchent, comme pour `surligner("aa", "aaa")` ?

    ??? pouce "Coup de pouce"

        Parcourir les positions renvoyées par `horspool_compte` en gardant un indice `i` : la partie de la ligne déjà recopiée. On ajoute `ligne[i:p]`, puis le motif entre crochets, puis `i` devient `p + len(motif)` ; une position `p` inférieure à `i` (chevauchement) est ignorée.

3.  Le fichier de Gutenberg est coupé en lignes d’environ $70$ caractères. Pour le motif `Phileas Fogg`, comparer : le nombre de lignes renvoyées par `grep`, le nombre d’occurrences trouvées par `horspool_compte` dans le texte entier, puis dans `texte.replace("\n", " ")`. Expliquer les écarts.

??? corrige "Corrigé"

    `grep` *filtre* les lignes : on construit par compréhension la liste des couples `(numéro, ligne)` pour les seules lignes où Horspool trouve au moins une position (on peut aussi partir d’une liste vide et ajouter chaque couple avec `append`).

    ```python
    def grep(motif, texte):
        lignes = texte.split("\n")
        return [(k + 1, lignes[k]) for k in range(len(lignes))
                if horspool_compte(motif, lignes[k])[0] != []]

    def surligner(motif, ligne):
        positions = horspool_compte(motif, ligne)[0]
        resultat = ""
        i = 0
        for p in positions:
            if p >= i:              # on ignore une occurrence qui chevauche la precedente
                resultat = resultat + ligne[i:p] + "[" + motif + "]"
                i = p + len(motif)
        return resultat + ligne[i:]

    for numero, ligne in grep("Passepartout", texte)[:5]:
        print(numero, surligner("Passepartout", ligne))
    ```

    **2.** On ne peut pas mettre de crochets qui se chevauchent : on garde la première occurrence et on ignore celles qui la recouvrent, d’où `"[aa]a"` (c’est aussi le choix de `grep` et des éditeurs).

    **3.** Dans le roman : $282$ lignes, $282$ occurrences dans le texte entier, $301$ après le remplacement. `grep` compte des *lignes* : une ligne qui contient deux fois le motif ne compterait qu’une fois (ce n’est jamais le cas ici, d’où $282 = 282$). Surtout, quand `Phileas` est en fin de ligne et `Fogg` au début de la suivante, le texte contient `"Phileas\nFogg"` : ni `grep`, ni la recherche dans le texte entier ne trouvent le motif (le caractère de fin de ligne n’est pas une espace). En remplaçant les fins de ligne par des espaces, on retrouve ces occurrences coupées ($19$ ici), au prix de la perte des numéros de ligne. *(Vérifié sur un petit texte : `grep("Fogg voyage", "Phileas Fogg\nvoyage")` renvoie `[]`, mais le motif est trouvé après le remplacement.)*

## Partie C — La longueur du motif, et la taille de l’alphabet

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Plus le motif est long… <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-recherche-textuelle-tp-1-6 }

1.  <span class="run" title="À programmer et tester sur machine">▶</span>  Compléter `moyenne_comparaisons(algo, texte, m, essais=5, graine=1)` : elle choisit `essais` positions `p` au hasard (`random.randint(0, len(texte) - m)`), prend comme motif `texte[p:p + m]` (il est donc présent au moins une fois), et renvoie le nombre **moyen** de comparaisons de `algo`, divisé par la longueur du texte. Un résultat de $0{,}25$ signifie : « en moyenne, une comparaison pour quatre caractères du texte ».

2.  <span class="run" title="À programmer et tester sur machine">▶</span>  On crée un génome par `adn = genome(1_000_000)` (un million de bases `A`, `C`, `G`, `T`). Recopier et compléter le tableau (deux chiffres après la virgule) :

| **Longueur $m$ du motif** | **2** | **4** | **8** | **16** | **32** | **64** |
|:--------------------------|:-----:|:-----:|:-----:|:------:|:------:|:------:|
| Naïf, roman               |       |       |       |        |        |        |
| Horspool, roman           |       |       |       |        |        |        |
| Naïf, génome              |       |       |       |        |        |        |
| Horspool, génome          |       |       |       |        |        |        |

1.  Sur le roman, comment évolue le travail de Horspool quand $m$ double ? Comparer avec $1/m$. Retrouve-t-on le « miracle du sous-linéaire » du cours ?

2.  Sur le génome, Horspool cesse de s’améliorer au-delà de $m \approx 8$. Expliquer pourquoi : pour un long motif sur l’alphabet `ACGT`, que valent à peu près les décalages de la table ?

    ??? pouce "Coup de pouce"

        Afficher `table_decalage(adn[1000:1032])` : où se trouvent les dernières occurrences de `A`, `C`, `G` et `T` dans un motif de 32 bases ? Un saut ne peut pas dépasser ces distances.

3.  Le naïf fait environ $1{,}33\,n$ comparaisons sur le génome. Justifier ce nombre : à une position donnée, quelle est la probabilité que la première comparaison réussisse ? les deux premières ?

4.  *(Facultatif.)* <span class="run" title="À programmer et tester sur machine">▶</span>  Tracer les quatre courbes avec `matplotlib` (`plt.plot`, `plt.xscale("log")`).

??? corrige "Corrigé"

    **1.**

    ```python
    def moyenne_comparaisons(algo, texte, m, essais=5, graine=1):
        random.seed(graine)
        total = 0
        for k in range(essais):
            p = random.randint(0, len(texte) - m)
            total += algo(texte[p:p + m], texte)[1]
        return total / essais / len(texte)

    adn = genome(1_000_000)
    for m in (2, 4, 8, 16, 32, 64):
        print(m, moyenne_comparaisons(naive_compte, adn, m),
                 moyenne_comparaisons(horspool_compte, adn, m))
    ```

    **2.** Valeurs obtenues (graines fixées : exactes et reproductibles) :

    | **$m$**          |  **2**   |  **4**   |  **8**   |  **16**  |  **32**  |  **64**  |
    |:-----------------|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|
    | Naïf, roman      | $1{,}08$ | $1{,}10$ | $1{,}10$ | $1{,}10$ | $1{,}10$ | $1{,}10$ |
    | Horspool, roman  | $0{,}56$ | $0{,}30$ | $0{,}16$ | $0{,}10$ | $0{,}07$ | $0{,}05$ |
    | Naïf, génome     | $1{,}25$ | $1{,}33$ | $1{,}33$ | $1{,}33$ | $1{,}33$ | $1{,}33$ |
    | Horspool, génome | $0{,}71$ | $0{,}54$ | $0{,}40$ | $0{,}41$ | $0{,}35$ | $0{,}45$ |

    **3.** Sur le roman, le travail de Horspool est à peu près **divisé par deux** quand $m$ double ($0{,}30 \to 0{,}16 \to 0{,}10$), comme $1/m$ (un peu au-dessus) : c’est bien le comportement **sous-linéaire** en $n/m$ du cours. Pour $m = 64$, on ne compare qu’environ $1$ caractère sur $20$.

    **4.** Dans un motif de $32$ bases, chacune des quatre lettres apparaît presque à coup sûr **près de la fin**. Par exemple, `table_decalage(adn[1000:1032])` vaut :  
    `{’T’: 9, ’A’: 1, ’C’: 2, ’G’: 4}`. Le saut est donc toujours petit (ici au plus $9$, souvent $1$ à $4$), quelle que soit la longueur du motif : le gain plafonne. Plus l’alphabet est **petit**, moins Horspool est efficace.

    **5.** À une position quelconque, la première comparaison est toujours faite ; elle réussit avec probabilité $1/4$, et l’on fait alors une deuxième comparaison, qui réussit avec probabilité $1/4$… En moyenne : $1 + \frac14 + \frac1{16} + \dots \approx \frac43 \approx 1{,}33$ comparaison par position. Sur un texte français, la première lettre du motif est plus rare (alphabet plus grand), d’où $\approx 1{,}1$.

    **6.** Avec `matplotlib` : pour chaque ligne,  
    `plt.plot(longueurs, valeurs, label=...)` ; puis `plt.xscale("log")`, `plt.legend()`, `plt.show()`.

## Partie D — Les cas défavorables

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Construire le pire <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-recherche-textuelle-tp-1-7 }

On prend un texte de $n = 20\,000$ lettres `A` : `texte = "A" * 20000`.

1.  <span class="run" title="À programmer et tester sur machine">▶</span>  Pour $m = 5,\ 10,\ 20,\ 40$, compter les comparaisons des deux algorithmes avec le motif `"A" * (m - 1) + "B"`, puis avec le motif `"B" + "A" * (m - 1)`. Présenter les résultats dans un tableau, avec une colonne $n \times m$.

2.  Pour chaque motif, expliquer *quel* algorithme est piégé, et pourquoi (dans quel sens compare-t-il ? de combien décale-t-il ?).

3.  Quel est donc le coût **dans le pire des cas** de chacun des deux algorithmes ? Ce pire cas est-il fréquent dans un texte en français ?

4.  À l’inverse, construire un motif de $10$ lettres pour lequel Horspool ne fait que $n/10$ comparaisons sur ce texte. Justifier.

??? corrige "Corrigé"

    **1.** Mesures ($n = 20\,000$) :

    ```python
    texte = "A" * 20000
    for m in (5, 10, 20, 40):
        m1 = "A" * (m - 1) + "B"
        m2 = "B" + "A" * (m - 1)
        print(m, naive_compte(m1, texte)[1], horspool_compte(m1, texte)[1],
                 naive_compte(m2, texte)[1], horspool_compte(m2, texte)[1], 20000 * m)
    ```

    | $m$ | **naïf, `A…AB`** | **Horspool, `A…AB`** | **naïf, `BA…A`** | **Horspool, `BA…A`** | $n \times m$ |
    |:--:|:--:|:--:|:--:|:--:|:--:|
    | $5$ | $99\,980$ | $19\,996$ | $19\,996$ | $99\,980$ | $100\,000$ |
    | $10$ | $199\,910$ | $19\,991$ | $19\,991$ | $199\,910$ | $200\,000$ |
    | $20$ | $399\,620$ | $19\,981$ | $19\,981$ | $399\,620$ | $400\,000$ |
    | $40$ | $798\,440$ | $19\,961$ | $19\,961$ | $798\,440$ | $800\,000$ |

    **2.** Motif `A…AB` : le **naïf** est piégé : il compare de gauche à droite, réussit $m-1$ fois et n’échoue que sur le `B`, puis ne décale que de $1$ : $m$ comparaisons à chacune des $n-m+1$ positions. Horspool commence par la fin : échec immédiat sur le `B` ($1$ comparaison)… mais il ne saute que de $1$ (la lettre de fin de fenêtre est `A`, à distance $1$ de la fin du motif) : $n - m + 1$ comparaisons. Motif `BA…A` : c’est l’inverse, **Horspool** est piégé ($m$ comparaisons de droite à gauche, puis saut de $1$), le naïf échoue tout de suite.

    **3.** Les deux sont en $O(n \times m)$ dans le pire des cas (coût **quadratique** si $m$ est de l’ordre de $n$). Ce pire cas exige un texte très répétitif (une seule lettre) : il n’arrive pratiquement jamais en français, mais il peut arriver sur des données binaires ou des séquences d’ADN très répétées.

    **4.** Un motif sans aucun `A`, par exemple `"B" * 10` : la lettre de fin de fenêtre est toujours `A`, absente de la table, donc saut de $10$ après une seule comparaison : $20\,000 / 10 = 2\,000$ comparaisons (mesuré : $2\,000$).

## Partie E — Face à Python

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — Contre la montre <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-recherche-textuelle-tp-1-8 }

La fonction fournie `chrono(f, a, b)` exécute `f(a, b)` et renvoie le couple (résultat, durée en secondes).

1.  <span class="run" title="À programmer et tester sur machine">▶</span>  Sur le génome et sur le roman, avec un motif de longueur $16$ pris dans le texte, mesurer la durée de `naive_compte`, `horspool_compte` et `toutes_positions`. Combien de fois `find` est-il plus rapide que votre Horspool ?

2.  La méthode `find` est écrite en langage C et compilée, et son algorithme s’inspire justement de Boyer-Moore-Horspool. Expliquer l’écart de temps. Le nombre de comparaisons et la durée mesurent-ils la même chose ?

3.  <span class="run" title="À programmer et tester sur machine">▶</span>  Comparer `toutes_positions("AA", "AAAA")` et `"AAAA".count("AA")`. Que compte exactement `count` ? Dans quel cas ce piège peut-il fausser une recherche dans l’ADN ?

??? corrige "Corrigé"

    **1.** Durées mesurées (meilleure de trois exécutions, motif de longueur $16$) :

    |  | `naive_compte` | `horspool_compte` | `toutes_positions` (`find`) |
    |:---|:--:|:--:|:--:|
    | Génome ($10^6$ bases) | $198$ ms | $125$ ms | $4{,}6$ ms |
    | Roman ($4{,}4 \times 10^5$ car.) | $78$ ms | $11$ ms | $0{,}21$ ms |

    `find` est environ $25$ fois plus rapide que notre Horspool sur le génome, $50$ fois sur le roman.

    **2.** Notre Horspool est **interprété** : chaque tour de boucle Python coûte des dizaines d’instructions machine (et nous incrémentons en plus un compteur). `find` est compilé en langage machine, avec un algorithme du même type. Le nombre de comparaisons mesure le travail **de l’algorithme**, indépendamment de la machine et du langage ; la durée mesure aussi le coût de **l’implémentation**. Les deux mesures se complètent.

    **3.** `toutes_positions("AA", "AAAA")` vaut `[0, 1, 2]`, mais `"AAAA".count("AA")` vaut `2` : `count` compte les occurrences **sans chevauchement**. Dans l’ADN, où les répétitions (`ATATAT`…) sont fréquentes, on sous-estimerait le nombre d’occurrences d’un motif périodique.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 9</span> — Défi : le vrai Boyer-Moore (mauvais caractère) <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-recherche-textuelle-tp-1-9 }

Dans le Boyer-Moore du cours, on regarde le caractère `c = texte[i + j]` qui a **provoqué l’échec** (position `j` du motif), et on décale de `max(1, j - dernier.get(c, -1))`, où `dernier` associe à chaque lettre du motif sa **dernière** position. Après une occurrence trouvée, on décale de $1$.

1.  <span class="run" title="À programmer et tester sur machine">▶</span>  Écrire `table_dernier(motif)` et `boyer_moore_compte(motif, texte)`, et les ajouter aux $1\,000$ tests de l’exercice 3.

2.  <span class="run" title="À programmer et tester sur machine">▶</span>  Ajouter une ligne « Boyer-Moore » au tableau de l’exercice 6. Le vrai Boyer-Moore (réduit au mauvais caractère) fait-il mieux que Horspool ? Sur quel texte l’écart est-il le plus visible ?

??? corrige "Corrigé"

    ```python
    def table_dernier(motif):
        dernier = {}
        for k in range(len(motif)):
            dernier[motif[k]] = k
        return dernier

    def boyer_moore_compte(motif, texte):
        n = len(texte)
        m = len(motif)
        dernier = table_dernier(motif)
        positions = []
        comp = 0
        i = 0
        while i <= n - m:
            j = m - 1
            while j >= 0 and texte[i + j] == motif[j]:
                comp += 1                   # comparaison reussie
                j -= 1
            if j < 0:
                positions.append(i)
                i += 1
            else:
                comp += 1                   # la comparaison qui a echoue
                i += max(1, j - dernier.get(texte[i + j], -1))
        return positions, comp
    ```

    Moyennes obtenues (comparaisons divisées par $n$, $m = 2$ à $64$) : génome $0{,}83$ ; $0{,}58$ ; $0{,}50$ ; $0{,}53$ ; $0{,}33$ ; $0{,}49$ — roman $0{,}58$ ; $0{,}31$ ; $0{,}16$ ; $0{,}10$ ; $0{,}07$ ; $0{,}05$. Réduit au seul mauvais caractère, Boyer-Moore ne fait **pas mieux** que Horspool : quasi identique sur le roman, souvent un peu moins bon sur le génome (le caractère fautif est souvent une lettre présente juste à côté dans le motif, d’où des sauts de $1$). C’est ce qui justifie la simplification de Horspool ; le vrai gain de Boyer-Moore vient de la règle du bon suffixe <span class="horsprog">au-delà du programme</span>.

## Bilan du TP

!!! encadre "À rédiger (une dizaine de lignes, en citant vos mesures)"

    1.  Comparer le coût de la méthode naïve et de Horspool sur un texte « ordinaire », puis dans le pire des cas.

    2.  Expliquer pourquoi « plus le motif est long, plus la recherche est rapide », et pourquoi ce n’est plus vrai sur l’ADN.

    3.  À quoi sert le **prétraitement** du motif ? Combien coûte-t-il, comparé à la recherche elle-même ?

    4.  Pourquoi utiliser `find` (ou `in`) en pratique, et à quoi bon avoir programmé Horspool ?
