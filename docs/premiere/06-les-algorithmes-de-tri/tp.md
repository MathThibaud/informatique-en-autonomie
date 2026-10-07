# TP et projets

<p class="sous-titre">Les algorithmes de tri</p>

## <span class="etiquette">TP</span> Le banc d’essai des tris

*compter, chronométrer, comparer : sélection, insertion et `sorted`*

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/06-tp-banc-essai-tris){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/premiere-06-tp-banc-essai-tris.zip){ .md-button }

|  |  |
|:---|:---|
| **Durée** | 2 h à 2 h 30 (une à deux séances), en binôme, sur machine. |
| **Prérequis** | le cours *Les algorithmes de tri* (sélection, insertion, invariants, coût) et la notion de coût du chapitre *Algorithmique : le parcours séquentiel*. |
| **Fichier** | `tp_tris_depart.py` (à compléter : tout votre code s’y écrit). |

!!! encadre "But du TP"

    Le cours affirme que les tris par sélection et par insertion sont **quadratiques**, que l’insertion devient **linéaire** sur un tableau déjà trié, et que `sorted` est bien plus rapide. Vous allez construire un **banc d’essai** pour le vérifier vous-mêmes :

    1.  des tris **instrumentés** qui comptent leurs comparaisons et leurs mouvements ;

    2.  des **jeux d’essai** (listes aléatoires, triées, inversées, presque triées) ;

    3.  des **mesures** : nombres d’opérations, puis temps au chronomètre, tracés sur un graphique ;

    4.  une **visualisation** du tri pas à pas, et (défi) un **classement en direct**.

    **Produit final** : un programme qui imprime le tableau comparatif des deux tris, un graphique des temps, et un bilan rédigé qui confirme — ou nuance — le cours.

!!! consignes "Consignes"

    - Niveau : ★ échauffement, ★★ classique (niveau bac), ★★★ défi ; les *coups de pouce* et les *corrigés* se déplient sous chaque exercice. <span class="run" title="À programmer et tester sur machine">▶</span> *À programmer* dans `tp_tris_depart.py`.

    - **Règle du TP** : on écrit les tris soi-même ; `sort()` et `sorted()` ne servent que de **référence** (pour vérifier et pour la course de vitesse).

    - En bas du fichier, le programme principal contient des lignes en commentaire (`#`) : on les **décommente au fur et à mesure**. Des tests `assert` sont fournis.

    - Le compte rendu (tableaux, réponses, bilan) se fait sur le cahier (ou dans un fichier texte).

    - Usage de l’IA, indiqué sur chaque exercice : <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> aucune ; <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> en appui (déboguer, reformuler, vérifier ; la réponse finale est écrite et comprise par vous) ; <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> l’exercice s’appuie sur une réponse d’IA. Voir la [charte d’usage de l’IA](../charte.md).

## Les jeux d’essai

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 1</span> — Fabriquer des listes <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-les-algorithmes-de-tri-tp-1-1 }

Le fichier fournit `aleatoire(n)` (`n` entiers au hasard entre 0 et 1000), `est_trie(t)` et `presque_triee(n, k)` (une liste triée dans laquelle on a échangé `k` paires de voisins).

1.  <span class="run" title="À programmer et tester sur machine">▶</span> Exécuter le fichier, puis afficher dans la console `aleatoire(10)` et `presque_triee(10, 2)`.

2.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire `triee(n)`, qui renvoie `[0, 1, …, n-1]`, et `inversee(n)`, qui renvoie `[n, n-1, …, 1]`, chacune en une ligne, avec une compréhension sur `range(…)`.

    ```text
    >>> triee(4), inversee(4)
    ([0, 1, 2, 3], [4, 3, 2, 1])
    ```

3.  Pourquoi aura-t-on besoin de ces trois sortes de listes pour *tester* un tri, et pas seulement de listes au hasard ?

??? corrige "Corrigé"

    *Les deux tris sont quadratiques : quand la liste double, comparaisons et temps sont multipliés par 4 (nos mesures : $0{,}19$ s puis $0{,}75$ s pour $2\,000$ puis $4\,000$ valeurs). La sélection fait toujours $\frac{n(n-1)}{2}$ comparaisons ; l’insertion n’en fait que $n - 1$ sur une liste triée et reste presque linéaire sur une liste presque triée : c’est elle qu’il faut choisir quand les données sont déjà en ordre ou arrivent une à une. En revanche, la sélection déplace très peu les éléments. En pratique, `sorted` est des centaines à des milliers de fois plus rapide et l’écart grandit avec $n$ : on l’utilise toujours. Limite : un chronomètre mesure aussi ce que fait l’ordinateur à côté, et des tris de même coût peuvent avoir des temps différents ; ce sont les rapports qui comptent.*

    ```python
    def triee(n):
        return [i for i in range(n)]

    def inversee(n):
        return [i for i in range(n, 0, -1)]
    ```

    Question 3 : la liste triée est le **meilleur cas** de l’insertion, la liste inversée son **pire cas**, la liste aléatoire un cas « moyen ». Ce sont aussi des cas limites où se cachent les bugs (indice $-1$, boucle qui ne s’arrête pas…) : un tri qui ne marche que sur des listes au hasard n’est pas testé.

## Des tris qui comptent leur travail

On **instrumente** les deux tris du cours : ils trient le tableau **en place** comme d’habitude, et **renvoient en plus** un couple de compteurs.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 2</span> — Le tri par sélection instrumenté <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-les-algorithmes-de-tri-tp-1-2 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `tri_selection_compte(t)` qui trie `t` par sélection et renvoie le couple `(comparaisons, echanges)` :

- `comparaisons` compte les comparaisons `t[j] < t[i_min]` ;

- `echanges` compte les échanges **réellement utiles** : on n’échange que si `i_min != i`.

```text
>>> t = [5, 3, 8, 1, 9, 2]
>>> tri_selection_compte(t)
(15, 4)
>>> t
[1, 2, 3, 5, 8, 9]
```

??? pouce "Coup de pouce"

    Partir du tri par sélection du cours. Deux compteurs initialisés à `0` avant les boucles ; la comparaison à compter est dans la boucle interne, l’échange juste après elle.

??? corrige "Corrigé"

    ```python
    def tri_selection_compte(t):
        comparaisons = 0
        echanges = 0
        n = len(t)
        for i in range(n - 1):
            i_min = i
            for j in range(i + 1, n):
                comparaisons = comparaisons + 1
                if t[j] < t[i_min]:
                    i_min = j
            if i_min != i:               # on ne compte que les vrais echanges
                temp = t[i]
                t[i] = t[i_min]
                t[i_min] = temp
                echanges = echanges + 1
        return comparaisons, echanges
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 3</span> — Le tri par insertion instrumenté <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-les-algorithmes-de-tri-tp-1-3 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `tri_insertion_compte(t)` qui trie `t` par insertion et renvoie `(comparaisons, decalages)` : une **comparaison** est chaque test `t[j] > x` effectué, un **décalage** chaque affectation `t[j + 1] = t[j]`.

```text
>>> tri_insertion_compte([5, 3, 8, 1, 9, 2])
(11, 8)
>>> tri_insertion_compte([1, 2, 3, 4, 5])
(4, 0)
```

??? pouce "Coup de pouce"

    Garder la boucle `while j >= 0 and t[j] > x` du cours et compter une comparaison à chaque tour. Attention : quand la boucle s’arrête alors que `j >= 0`, c’est que le test `t[j] > x` a été fait (et était faux) : il faut aussi le compter.

Décommenter `tester_partie_A()` : les tests trient des listes de plusieurs tailles et de trois sortes, et comparent à `sorted`. Ils doivent tous passer avant de continuer.

??? corrige "Corrigé"

    ```python
    def tri_insertion_compte(t):
        comparaisons = 0
        decalages = 0
        for i in range(1, len(t)):
            x = t[i]
            j = i - 1
            while j >= 0 and t[j] > x:
                comparaisons = comparaisons + 1
                t[j + 1] = t[j]
                decalages = decalages + 1
                j = j - 1
            if j >= 0:                   # le test t[j] > x qui a arrete la boucle
                comparaisons = comparaisons + 1
            t[j + 1] = x
        return comparaisons, decalages
    ```

    Sur `[5, 3, 8, 1, 9, 2]` : 11 comparaisons et 8 décalages (insérer 3 : 1 décalage ; 8 : 0 ; 1 : 3 ; 9 : 0 ; 2 : 4).

## Le banc d’essai : compter

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 4</span> — Lancer le banc <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-les-algorithmes-de-tri-tp-1-4 }

<span class="run" title="À programmer et tester sur machine">▶</span> Décommenter `banc_essai([100, 200, 400])` puis recopier sur le cahier le tableau suivant et le compléter avec les résultats.

| `n` | liste | sélection : comparaisons | sélection : échanges | insertion : comparaisons | insertion : décalages |
|:--:|:---|:---|:---|:---|:---|
|  | aléatoire |  |  |  |  |
| $100$ | triée |  |  |  |  |
|  | inversée |  |  |  |  |
|  | aléatoire |  |  |  |  |
| $200$ | triée |  |  |  |  |
|  | inversée |  |  |  |  |
|  | aléatoire |  |  |  |  |
| $400$ | triée |  |  |  |  |
|  | inversée |  |  |  |  |

??? corrige "Corrigé"

     Résultats obtenus (les lignes « aléatoire » changent d’une exécution à l’autre, les autres sont exactes) :

    | `n` | liste | sél. : comparaisons | sél. : échanges | ins. : comparaisons | ins. : décalages |
    |:--:|:---|---:|---:|---:|---:|
    |  | aléatoire | $4\,950$ | $96$ | $2\,395$ | $2\,302$ |
    | $100$ | triée | $4\,950$ | $0$ | $99$ | $0$ |
    |  | inversée | $4\,950$ | $50$ | $4\,950$ | $4\,950$ |
    |  | aléatoire | $19\,900$ | $193$ | $9\,625$ | $9\,430$ |
    | $200$ | triée | $19\,900$ | $0$ | $199$ | $0$ |
    |  | inversée | $19\,900$ | $100$ | $19\,900$ | $19\,900$ |
    |  | aléatoire | $79\,800$ | $394$ | $42\,279$ | $41\,882$ |
    | $400$ | triée | $79\,800$ | $0$ | $399$ | $0$ |
    |  | inversée | $79\,800$ | $200$ | $79\,800$ | $79\,800$ |

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 5</span> — Faire parler les nombres <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-les-algorithmes-de-tri-tp-1-5 }

1.  Les comparaisons de la sélection dépendent-elles de la sorte de liste ? Vérifier qu’elles valent $\frac{n(n-1)}{2}$.

2.  Quand `n` double, par combien sont multipliées les comparaisons de la sélection ? celles de l’insertion sur une liste aléatoire ? Quel coût cela confirme-t-il ?

3.  Sur une liste **triée**, combien de comparaisons fait l’insertion ? Exprimer ce nombre en fonction de `n`. C’est le « meilleur atout » du cours : quel est alors son coût ?

4.  Sur une liste **inversée**, comparer les deux tris. Sur une liste **aléatoire**, l’insertion fait environ *deux fois moins* de comparaisons que la sélection : proposer une explication (de combien de cases recule, en moyenne, un élément inséré ?).

5.  La sélection fait au plus `n - 1` échanges, l’insertion des milliers de décalages. Dans quelle situation pourrait-on préférer la sélection ? *(Penser à des objets lourds à déplacer.)* <span class="horsprog">au-delà du programme</span>

6.  **Sur une liste inversée**, la sélection ne fait que `n/2` échanges. Dérouler-la sur `[6, 5, 4, 3, 2, 1]` pour comprendre pourquoi.

??? corrige "Corrigé"

    1.  Non : $4\,950 = \frac{100 \times 99}{2}$, $19\,900 = \frac{200 \times 199}{2}$, $79\,800 = \frac{400 \times 399}{2}$, quelle que soit la liste.

    2.  Sélection : $\times 4{,}0$ à chaque doublement ; insertion sur liste aléatoire : $\times 4{,}0$ puis $\times 4{,}4$ (le hasard fait varier). Multiplier par 4 quand $n$ double : coût **quadratique**.

    3.  $n - 1$ comparaisons (99, 199, 399) et aucun décalage : coût **linéaire**.

    4.  Sur liste inversée, les deux font $\frac{n(n-1)}{2}$ comparaisons (et l’insertion autant de décalages) : c’est le pire cas de l’insertion. Sur liste aléatoire, un élément inséré dans une partie triée de taille $i$ recule *en moyenne* jusqu’au milieu, soit $i/2$ cases ; le total vaut environ $\frac{n^2}{4}$ au lieu de $\frac{n^2}{2}$.

    5.  Quand déplacer un élément coûte cher (gros enregistrements, écritures lentes sur un support) : la sélection fait au plus $n - 1$ échanges, l’insertion de l’ordre de $n^2$ décalages.

    6.  `[6, 5, 4, 3, 2, 1]` $\to$ `[1, 5, 4, 3, 2, 6]` $\to$ `[1, 2, 4, 3, 5, 6]` $\to$ `[1, 2, 3, 4, 5, 6]`, puis plus rien à échanger : 3 échanges. Chaque échange place **deux** éléments à la fois (le minimum devant, et le grand élément qu’il remplace part à sa place symétrique) : la seconde moitié du travail est déjà faite.

## Le chronomètre

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — La course <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-les-algorithmes-de-tri-tp-1-6 }

1.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire `chronometre(tri, t)` qui renvoie la durée, en secondes, du tri d’une **copie** de `t` par la fonction `tri` (mesurée avec `time.perf_counter()`). Pourquoi est-il indispensable de trier une copie ?

    ??? pouce "Coup de pouce"

        `copie = [x for x in t]`, lire l’horloge, appeler `tri(copie)`, relire l’horloge. Que se passerait-il si la sélection triait `t` lui-même, puis que l’insertion recevait ce même `t` ?

2.  <span class="run" title="À programmer et tester sur machine">▶</span> La fonction `course(tailles)`, fournie, chronomètre la sélection, l’insertion et `sorted` sur une **même** liste aléatoire pour chaque taille. La lancer pour `[500, 1000, 2000, 4000]` puis recopier sur le cahier et compléter le tableau suivant (3 chiffres significatifs) :

|  **`n`** | sélection (s) | insertion (s) | `sorted` (s) | sélection / `sorted` |
|---------:|:--------------|:--------------|:-------------|:---------------------|
|    $500$ |               |               |              |                      |
| $1\,000$ |               |               |              |                      |
| $2\,000$ |               |               |              |                      |
| $4\,000$ |               |               |              |                      |

??? corrige "Corrigé"

    ```python
    def chronometre(tri, t):
        copie = [x for x in t]           # on ne trie jamais deux fois la meme liste
        debut = time.perf_counter()
        tri(copie)
        return time.perf_counter() - debut
    ```

    Sans copie, le premier tri chronométré trierait la liste `t` elle-même : le suivant recevrait une liste **déjà triée** (le meilleur cas de l’insertion), et la comparaison serait faussée.

    Mesures réellement obtenues (ordinateur portable récent) :

    |  **`n`** | sélection (s) | insertion (s) | `sorted` (s)  | sélection / `sorted` |
    |---------:|:-------------:|:-------------:|:-------------:|:--------------------:|
    |    $500$ |  $0{,}0120$   |  $0{,}0118$   | $0{,}0000420$ |    $\approx 290$     |
    | $1\,000$ |  $0{,}0470$   |  $0{,}0432$   | $0{,}0000780$ |    $\approx 600$     |
    | $2\,000$ |   $0{,}186$   |   $0{,}187$   | $0{,}000170$  |   $\approx 1\,100$   |
    | $4\,000$ |   $0{,}746$   |   $0{,}730$   | $0{,}000370$  |   $\approx 2\,000$   |

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Lire les temps <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-les-algorithmes-de-tri-tp-1-7 }

1.  Quand `n` double, par combien est multiplié le temps de chacun des deux tris ? et celui de `sorted` ?

2.  <span class="run" title="À programmer et tester sur machine">▶</span> Décommenter `tracer(...)` et décrire les trois courbes.

3.  Sur liste aléatoire, l’insertion faisait deux fois moins de comparaisons… mais est-elle deux fois plus rapide ? Proposer une explication (que fait-elle d’autre que comparer ?).

4.  <span class="run" title="À programmer et tester sur machine">▶</span> Chronométrer les deux tris sur `triee(4000)`. Quel est le rapport entre les deux temps ? Est-ce cohérent avec l’exercice 5 ?

5.  <span class="run" title="À programmer et tester sur machine">▶</span> Compter les comparaisons de l’insertion sur `presque_triee(1000, k)` pour `k` valant 0, 5, 20, 100. Que constate-t-on ? Pour quelles données réelles l’insertion est-elle donc un excellent choix ?

6.  **Prédire.** À partir de la mesure pour $n = 4\,000$, estimer le temps de la sélection pour trier $1\,000\,000$ de valeurs. Comparer à la phrase du cours : « des minutes, voire des heures ».

??? corrige "Corrigé"

    1.  Les deux tris : $\times 4$ environ (3,9 ; 4,0 ; 4,0) : quadratiques. `sorted` : $\times 2$ environ ($1{,}9$ ; $2{,}2$ ; $2{,}2$), un peu plus que 2 : c’est le coût $n\log_2 n$ évoqué dans le cours. L’écart avec nos tris **se creuse** à chaque doublement (dernière colonne).

    2.  Deux paraboles presque superposées pour la sélection et l’insertion ; `sorted` reste collée à l’axe.

    3.  Non, les temps sont presque égaux. À chaque tour de sa boucle, l’insertion fait plus que comparer : un décalage (une écriture dans le tableau), une décrémentation, un test `j >= 0`. Compter les comparaisons donne l’**ordre de grandeur** du coût, pas la durée exacte : deux algorithmes de même coût quadratique peuvent différer d’un facteur constant, dans un sens ou dans l’autre.

    4.  Sur `triee(4000)` : sélection $0{,}74$ s, insertion $0{,}000\,74$ s, un rapport d’environ **1 000**. Cohérent : $\frac{n(n-1)}{2}$ comparaisons contre $n - 1$, rapport $\frac{n}{2} = 2\,000$ en opérations.

    5.  Insertion sur `presque_triee(1000, k)` : $999$, $1\,004$, $1\,019$, $1\,095$ comparaisons pour $k = 0$, 5, 20, 100 (la sélection : toujours $499\,500$). Le coût reste $\approx n + k$ : **linéaire** tant que le désordre est faible. Excellent choix pour une liste triée à laquelle on ajoute quelques éléments, ou des données qui arrivent presque dans l’ordre (horodatages).

    6.  $10^6 = 4\,000 \times 250$ : $0{,}75 \times 250^2 \approx 47\,000$ s, soit **environ 13 heures** — le cours ne mentait pas. `sorted` trie un million de valeurs en une fraction de seconde.

## Voir le tri travailler

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — Des barres dans la console <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-les-algorithmes-de-tri-tp-1-8 }

1.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire `afficher_barres(t, i_actif)` qui affiche chaque valeur de `t` sur une ligne, suivie d’autant de `#` que sa valeur ; la ligne d’indice `i_actif` est marquée d’une flèche (`-1` : aucune flèche). *Rappel : `"#" * 5` vaut `"#####"`.*

2.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire `tri_insertion_visu(t, pause)` : le tri par insertion, qui affiche le tableau **après chaque insertion**, en marquant l’élément qu’on vient de placer, puis attend `pause` secondes (`time.sleep(pause)`). Voici un **extrait** de l’affichage attendu sur `[5, 3, 8, 1, 9, 2]` (l’état de départ, puis les étapes 1 et 3 ; l’étape 2, où 8 reste à sa place, n’est pas reproduite) :

```text
 5 #####
 3 ###
 8 ########
 1 #
 9 #########
 2 ##
```

```text
Étape 1 : on insère 3
 3 ###  <--
 5 #####
 8 ########
 1 #
 9 #########
 2 ##
```

```text
Étape 3 : on insère 1
 1 #  <--
 3 ###
 5 #####
 8 ########
 9 #########
 2 ##
```

1.  Sur l’affichage, repérer l’**invariant** du tri par insertion : quelle partie du tableau est triée après l’étape $i$ ?

2.  <span class="run" title="À programmer et tester sur machine">▶</span> <span class="horsprog">au-delà du programme</span> Écrire de même `tri_selection_visu`. Regarder les deux animations sur une liste de 12 entiers au hasard entre 1 et 30 (`[random.randint(1, 30) for k in range(12)]`) : en quoi « voit-on » que la sélection place chaque élément à sa place *définitive*, et pas l’insertion ?

??? corrige "Corrigé"

    ```python
    def afficher_barres(t, i_actif):
        for k in range(len(t)):
            marque = ""
            if k == i_actif:
                marque = "  <--"
            print(t[k], "#" * t[k] + marque)
        print()

    def tri_insertion_visu(t, pause=0.5):
        afficher_barres(t, -1)
        for i in range(1, len(t)):
            x = t[i]
            j = i - 1
            while j >= 0 and t[j] > x:
                t[j + 1] = t[j]
                j = j - 1
            t[j + 1] = x
            print("Étape", i, ": on insère", x)
            afficher_barres(t, j + 1)    # x vient d'etre pose en j + 1
            time.sleep(pause)
    ```

    Question 3 : après l’étape $i$, les cases `0` à `i` sont triées (mais des éléments plus petits arriveront encore). Question 4 : la sélection est le tri du cours, avec un affichage après chaque échange ; à l’écran, la zone de gauche n’est **plus jamais modifiée**, alors qu’avec l’insertion les barres déjà rangées glissent encore vers la droite.

## Défi : le classement en direct

Lors d’une course, les temps des coureurs arrivent **un par un**, et le tableau d’affichage doit toujours montrer un classement **trié**. Deux stratégies :

- **retrier** tout le classement par sélection à chaque arrivée (fonction `direct_en_retriant`, fournie) ;

- **insérer** le nouveau temps à sa place dans le classement déjà trié — exactement *une* étape du tri par insertion.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 9</span> — Insérer à sa place <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-les-algorithmes-de-tri-tp-1-9 }

1.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire `inserer(classement, x)` : `classement` est trié ; la fonction y ajoute `x` à la fin (`append`), le fait reculer à sa place par décalages, et renvoie le nombre de comparaisons effectuées.

    ```text
    >>> c = [47, 50, 53, 61]
    >>> inserer(c, 52)
    3
    >>> c
    [47, 50, 52, 53, 61]
    ```

2.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire `direct_par_insertion(arrivees)` qui part d’un classement vide, insère les temps un par un, et renvoie le couple `(classement, total des comparaisons)`.

3.  <span class="run" title="À programmer et tester sur machine">▶</span> Comparer les deux stratégies sur `aleatoire(300)` : vérifier que les classements obtenus sont identiques et relever les deux totaux de comparaisons.

4.  Expliquer l’écart. Combien coûte, au pire, l’arrivée d’un coureur dans chaque stratégie quand $k$ coureurs sont déjà classés ?

??? corrige "Corrigé"

    ```python
    def inserer(classement, x):
        classement.append(x)
        j = len(classement) - 2
        comparaisons = 0
        while j >= 0 and classement[j] > x:
            comparaisons = comparaisons + 1
            classement[j + 1] = classement[j]
            j = j - 1
        if j >= 0:                       # le test qui a arrete la boucle
            comparaisons = comparaisons + 1
        classement[j + 1] = x
        return comparaisons

    def direct_par_insertion(arrivees):
        classement = []
        total = 0
        for x in arrivees:
            total = total + inserer(classement, x)
        return classement, total
    ```

    Sur `aleatoire(300)` : classements identiques ; **environ 21 500** comparaisons par insertion (la valeur exacte dépend du tirage) contre **4 499 950** en retriant (environ 200 fois plus).

    Quand $k$ coureurs sont classés, insérer coûte au plus $k$ comparaisons (**linéaire** en $k$), alors que retrier par sélection en coûte toujours $\frac{(k+1)k}{2}$ (**quadratique** en $k$). Sur $n$ arrivées, on totalise de l’ordre de $\frac{n^2}{4}$ dans le premier cas (aléatoire) et exactement $1 + 3 + 6 + \cdots = \frac{(n+1)n(n-1)}{6}$ dans le second : pour $n = 300$, $\frac{301 \times 300 \times 299}{6} = 4\,499\,950$, le nombre mesuré.

## Bilan à rédiger

Sur le cahier, en huit à dix lignes, **en citant vos mesures** :

- ce que veut dire « quadratique » quand on double la taille d’une liste ;

- dans quels cas l’insertion est bien meilleure que la sélection, et pourquoi ;

- pourquoi, en pratique, on utilise `sort()` / `sorted()` ;

- une limite de vos mesures (ce qu’un chronomètre ne mesure pas bien).
