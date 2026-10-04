# Défis Advent of Code

<p class="sous-titre">Récursivité</p>

## <span class="etiquette">Défi 1</span> Password Philosophy

*les mots de passe — découpage de chaînes et ou exclusif*

<p class="infos-activite">Jour 2</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/01-defi-aoc-2020-02){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-01-defi-aoc-2020-02.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/2 ](https://adventofcode.com/2020/day/2 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/01-defi-aoc-2020-02>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| password | mot de passe | policy | règle, politique |
| corrupted | corrompu, abîmé | valid | valide, conforme |
| lowest / highest | plus petit / plus grand | number of times | nombre de fois |
| log in | se connecter | instance | occurrence (d’une lettre) |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Le héros part en vacances et doit descendre jusqu’à la côte en luge. Le loueur de luges ne parvient plus à se connecter : sa base de mots de passe est en partie abîmée. Chaque ligne du fichier décrit un mot de passe enregistré, accompagné de la règle de sécurité qui était en vigueur quand il a été choisi. Il s’agit de repérer les mots de passe qui respectent leur propre règle.

    **Ce qu’il faut faire.**

    - Une ligne a la forme `a-b l: motdepasse` : deux entiers $a \leqslant b$, une lettre `l`, puis le mot de passe, écrit en lettres minuscules.

    - La règle se lit ainsi : la lettre `l` doit apparaître dans le mot de passe au moins $a$ fois et au plus $b$ fois, bornes comprises. Autrement dit, le nombre d’occurrences de `l` doit appartenir à l’intervalle $[a, b]$.

    - Il faut renvoyer le nombre de lignes dont le mot de passe respecte sa règle.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-recursivite-aoc-1-1 }

Après lecture de l’énoncé et du résumé, vérifier sa compréhension :

1.  Le mot de passe `kkk` respecte-t-il la règle `1-3 k` ? Et la règle `4-5 k` ?

2.  Après `"2-3 z: zaz".split()`, que contient le deuxième morceau ? Quel piège pour comparer la lettre ?

3.  Les nombres peuvent avoir deux chiffres (`10-12`). Pourquoi est-il alors dangereux de lire la ligne à des positions fixes ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-recursivite-aoc-1-2 }

On considère le fichier (inventé) suivant :

```console
2-4 m: mmxmz
1-2 k: akkkb
3-5 t: tttxt
1-1 q: rst
2-6 e: eeabcf
```

Pour chaque ligne, dire si le mot de passe respecte la règle de la partie 1. Vérification : on doit compter `3` mots de passe valides.

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Découper une ligne <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-recursivite-aoc-1-3 }

Écrire une fonction `decouper(ligne)` qui renvoie le tuple `(a, b, lettre, mdp)` formé de deux entiers et de deux chaînes. Par exemple `decouper("2-4 m: mmxmz")` doit renvoyer `(2, 4, "m", "mmxmz")`. Tester avec `assert`.

??? pouce "Coup de pouce"

    `ligne.split()` coupe aux espaces et donne trois morceaux ; le premier se recoupe avec `split("-")`, le deuxième se débarrasse du `:` en ne gardant que son premier caractère.

!!! encadre "Outil Python : compter dans une chaîne (count) et comparaisons enchaînées"

    La méthode `count` renvoie le nombre d’apparitions d’un caractère (ou d’un morceau de chaîne) dans une chaîne, sans écrire de boucle. Python accepte aussi d’enchaîner les comparaisons, comme en mathématiques.

    ```python
    mot = "banane"
    print(mot.count("a"))     # 2
    print(mot.count("an"))    # 2 : on peut compter un morceau de chaine
    print(mot.count("z"))     # 0 si absent
    n = 3
    print(1 <= n <= 5)        # True : equivaut a 1 <= n and n <= 5
    ```

    **Intérêt.** Le code est plus court et plus lisible ; `count` parcourt la chaîne une fois, comme une boucle écrite à la main (coût proportionnel à la longueur).

    **À essayer.** Que renvoie `"aaaa".count("aa")` ? Pourquoi pas `3` ?

### <span class="exo-num">Exercice 4</span> — Valider et compter <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-recursivite-aoc-1-4 }

Écrire une fonction `valide1(a, b, lettre, mdp)` qui renvoie un booléen, puis le programme qui lit `input.txt` et compte les mots de passe valides. Tester sur l’exemple de la fiche, puis sur vos données.

??? pouce "Coup de pouce"

    La méthode `mdp.count(lettre)` compte les occurrences. Python accepte les comparaisons enchaînées : `a <= n <= b`.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    Le loueur s’aperçoit qu’il s’est trompé de règlement : les deux nombres n’ont pas le sens qu’on leur a donné.

    - Ils désignent maintenant deux **positions** dans le mot de passe, numérotées **à partir de 1** (il n’y a pas de position 0).

    - Le mot de passe est valide si la lettre se trouve à exactement une de ces deux positions : ni à aucune, ni aux deux. Les occurrences ailleurs dans le mot ne comptent plus.

### <span class="exo-num">Exercice 5</span> — Une nouvelle règle <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-recursivite-aoc-1-5 }

1.  Sans programme : la ligne `1-3 a: aba` est-elle valide selon la nouvelle règle ? Et `2-3 b: abc` ?

2.  Écrire `valide2(a, b, lettre, mdp)` et compter. Sur l’exemple de la fiche, on doit trouver `2` mots de passe valides.

??? pouce "Coup de pouce"

    Attention au décalage : la position `1` de l’énoncé correspond à l’indice `0` en Python.

??? pouce "Coup de pouce 2 (début de solution)"

    Calculer deux booléens `p` et `q` (la lettre est-elle à chacune des deux positions ?). « L’un ou l’autre mais pas les deux » s’écrit `p != q` : c’est le *ou exclusif*.

## Approfondissement

!!! encadre "Outil Python : les opérateurs bit à bit (&, |, ^)"

    Sur des entiers, ces opérateurs travaillent chiffre binaire par chiffre binaire : `&` (et), `|` (ou), `^` (ou exclusif). Sur des booléens, ils donnent le même résultat que `and`, `or` et le ou exclusif.

    ```python
    print(6 & 3)          # 110 et 011 -> 010, soit 2
    print(6 | 3)          # 110 ou 011 -> 111, soit 7
    print(6 ^ 3)          # 110 xor 011 -> 101, soit 5
    print(True ^ True)    # False
    print(5 ^ 5)          # 0 : x ^ x vaut toujours 0
    ```

    **Intérêt.** Un seul calcul traite tous les bits à la fois ; le ou exclusif est très utilisé en cryptographie (chiffrement de Vernam) et pour coder des ensembles de petits entiers.

    **À essayer.** Calculer à la main `12 ^ 10`, puis vérifier avec Python.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 6</span> — Défi : une table de vérité <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-recursivite-aoc-1-6 }

Dresser la table de vérité du ou exclusif. Vérifier que `p != q`, `p ^ q` et `(p or q) and not (p and q)` donnent le même résultat pour les quatre cas, en le faisant afficher par un programme.

??? pouce "Coup de pouce"

    Deux boucles `for p in (False, True)` imbriquées suffisent à parcourir les quatre cas.

## <span class="etiquette">Défi 2</span> Handy Haversacks

*les sacs emboîtés — dictionnaires et récursivité*

<p class="infos-activite">Jour 7</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/01-defi-aoc-2020-07){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-01-defi-aoc-2020-07.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/7 ](https://adventofcode.com/2020/day/7 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/01-defi-aoc-2020-07>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

*Ce défi réinvestit la récursivité vue dans ce chapitre : un sac contient des sacs, qui contiennent eux-mêmes des sacs…*

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| bag | sac | rule | règle |
| contain | contenir | no other bags | aucun autre sac (sac vide) |
| outermost | le plus à l’extérieur | eventually | au bout du compte, indirectement |
| color-coded | repéré par une couleur | shiny gold | or brillant |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Escale à l’aéroport : un nouveau règlement impose des sacs repérés par leur couleur, et chaque couleur de sac doit contenir un nombre précis de sacs d’autres couleurs. Le héros possède un sac `shiny gold` (or brillant) et se demande dans quels sacs il pourrait le ranger. Chaque ligne du fichier est une règle qui décrit le contenu imposé d’une couleur de sac.

    **Ce qu’il faut faire.**

    - Une règle a la forme `<couleur> bags contain <n> <couleur> bag(s), ...` ou bien `<couleur> bags contain no other bags.` Une couleur s’écrit en deux mots (`dull lime`) ; on lit `bag` ou `bags` selon le nombre, et la ligne se termine par un point.

    - Chaque couleur possède exactement une règle. Les sacs s’emboîtent : un sac contient des sacs, qui en contiennent d’autres, etc.

    - On cherche les couleurs dont un sac contient au moins un sac `shiny gold`, directement ou à l’intérieur d’autres sacs.

    - Il faut renvoyer le nombre de ces couleurs ; `shiny gold` ne se compte pas lui-même.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-recursivite-aoc-2-1 }

Après lecture de l’énoncé et du résumé, vérifier sa compréhension :

1.  Si un sac A contient un sac B qui contient un sac `shiny gold`, la couleur de A compte-t-elle ?

2.  Une couleur dont un sac contient 5 sacs `shiny gold` compte-t-elle 5 fois ?

3.  Quels morceaux d’une ligne faut-il écarter pour ne garder que des nombres et des couleurs ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-recursivite-aoc-2-2 }

On considère les règles (inventées) suivantes :

```console
pale cyan bags contain 2 shiny gold bags, 1 dull lime bag.
striped coral bags contain 1 pale cyan bag.
dull lime bags contain no other bags.
shiny gold bags contain 3 dull lime bags, 2 wavy ochre bags.
wavy ochre bags contain 4 dull lime bags.
clear navy bags contain 5 wavy ochre bags.
bold mauve bags contain 1 striped coral bag, 2 clear navy bags.
```

Faire un schéma : écrire chaque couleur, et tracer une flèche de $A$ vers $B$, étiquetée $n$, si un sac $A$ contient $n$ sacs $B$. Répondre à la partie 1 en remontant les flèches depuis `shiny gold`. Vérification : on doit trouver `3`.

## Programmer la partie 1

!!! encadre "Outil Python : tester le début ou la fin d’une chaîne (startswith, endswith)"

    Ces deux méthodes renvoient un booléen : la chaîne commence-t-elle (finit-elle) par le morceau donné ?

    ```python
    reste = "no other bags."
    print(reste.startswith("no other"))   # True
    print(reste.endswith("."))            # True
    print("2 dull lime bags".startswith("no"))   # False
    ```

    **Intérêt.** Plus lisible et plus sûr que de comparer une tranche à la main (`reste[:8] == "no other"`), où il faut compter les caractères.

    **À essayer.** Que renvoie `"bags".startswith("bag")` ? Et `"bag".startswith("bags")` ?

### <span class="exo-num">Exercice 3</span> — Les règles en dictionnaire <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-recursivite-aoc-2-3 }

Écrire une fonction `lire_regle(ligne)` qui renvoie la couleur du contenant et un dictionnaire de son contenu, par exemple `("wavy ochre", {"dull lime": 4})`. Construire ensuite le dictionnaire `contenu` qui associe à chaque couleur le dictionnaire de son contenu (un dictionnaire de dictionnaires).

??? pouce "Coup de pouce"

    Couper d’abord sur `" bags contain "`. Si la suite commence par `"no other"`, le contenu est vide ; sinon, couper sur `", "` : chaque morceau commence par un nombre suivi de deux mots de couleur.

!!! encadre "Outil Python : all et any"

    `all(...)` renvoie `True` si **tous** les éléments sont vrais, `any(...)` si **au moins un** l’est. On les écrit souvent avec une expression de la forme d’une compréhension de liste.

    ```python
    notes = [12, 15, 9]
    print(all(n >= 10 for n in notes))    # False : 9 ne convient pas
    print(any(n >= 15 for n in notes))    # True : 15 convient
    print(all([]))                        # True : aucun contre-exemple
    print(any([]))                        # False : aucun exemple
    ```

    **Intérêt.** Ils remplacent une boucle accompagnée d’un booléen « drapeau », et s’arrêtent dès que la réponse est connue (au premier faux pour `all`, au premier vrai pour `any`).

    **À essayer.** Prévoir puis vérifier `any(x == "shiny gold" for x in {})` : que renvoie `any` pour un sac vide ?

### <span class="exo-num">Exercice 4</span> — Peut contenir le sac doré ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-recursivite-aoc-2-4 }

Écrire une fonction récursive `peut_contenir(couleur)` qui renvoie `True` si un sac de cette couleur contient, directement ou non, un sac `shiny gold`. Compter les couleurs concernées. Tester sur l’exemple de la fiche, puis sur vos données.

??? pouce "Coup de pouce"

    Cas de base : le contenu de `couleur` a `"shiny gold"` parmi ses clés. Sinon, il suffit qu’**un** des sacs contenus puisse lui-même le contenir.

??? pouce "Coup de pouce 2 (début de solution)"

    Le résultat est vrai si, pour au moins un sac `x` du contenu, `x` est le sac doré **ou** `peut_contenir(x)` est vrai : c’est exactement ce que calcule `any` (voir l’encadré). Un sac vide donne `False` : c’est la condition d’arrêt.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    Le héros se rend compte que son sac doré, une fois rempli selon le règlement, va peser lourd.

    - Il faut renvoyer le nombre total de sacs qu’un sac `shiny gold` doit contenir. On compte à tous les niveaux d’emboîtement, en tenant compte des quantités ; le sac doré lui-même ne compte pas.

### <span class="exo-num">Exercice 5</span> — Dans l’autre sens <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-recursivite-aoc-2-5 }

1.  Dans la partie 1, on cherchait des sacs « au-dessus » du sac doré. Dans quel sens suit-on maintenant les règles ?

2.  Écrire une fonction récursive qui répond à la question. Sur l’exemple de la fiche, on doit trouver `13`.

??? pouce "Coup de pouce"

    Un sac contenu compte-t-il lui-même, en plus de tout ce qu’il contient ?

??? pouce "Coup de pouce 2 (début de solution)"

    Pour un sac `A` qui contient `n` sacs `B` : ces `n` sacs comptent, et chacun d’eux apporte en plus tout son propre contenu. Le sac vide fournit le cas de base.

## Approfondissement

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 6</span> — Défi : dans l’autre sens <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-recursivite-aoc-2-6 }

Pour chaque couleur, construire la liste des couleurs qui la contiennent **directement** (dictionnaire `contenants`). Écrire ensuite une fonction récursive `ajouter_contenants(couleur, trouves)` qui ajoute à la liste `trouves`, sans doublon, toutes les couleurs qui contiennent `couleur`, directement ou non. En déduire la réponse de la partie 1 et la comparer à celle de la version précédente.

??? pouce "Coup de pouce"

    Sur l’exemple de la fiche, `contenants["shiny gold"]` vaut `["pale cyan"]` et `contenants["pale cyan"]` vaut `["striped coral"]`.

??? pouce "Coup de pouce 2 (début de solution)"

    Pour chaque couleur `c` de `contenants[couleur]` qui n’est pas encore dans `trouves` : l’ajouter, puis appeler la fonction sur `c`. La réponse est la longueur de `trouves`.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 1 : l’inventaire du sac doré <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-recursivite-aoc-2-7 }

1.  À la main, sur l’exemple de la fiche : combien de sacs de chaque couleur trouve-t-on, à tous les niveaux, dans un sac `shiny gold` ? Vérifier que le total redonne `13`.

2.  Écrire une fonction récursive `inventaire(couleur)` qui renvoie un dictionnaire associant à chaque couleur le nombre de sacs de cette couleur contenus dans un sac `couleur`.

3.  Combien de fois la fonction de la partie 2 est-elle appelée pour `dull lime` sur l’exemple ? Vérifier en comptant les appels dans un dictionnaire.

4.  On imagine des règles où chaque sac $c_i$ contient un sac $c_{i+1}$ et un sac $c_{i+2}$. Montrer que le nombre d’appels $A(i)$ pour $c_i$ vérifie $A(i) = 1 + A(i+1) + A(i+2)$. Quel exemple du cours sur la récursivité retrouve-t-on ? (Le chapitre sur la programmation dynamique montrera comment éviter ces recalculs.)

??? pouce "Coup de pouce"

    Un sac `A` qui contient `n` sacs `B` apporte `n` sacs `B`, plus `n` fois tout l’inventaire d’un sac `B`.

??? pouce "Coup de pouce 2 (début de solution)"

    Écrire une petite fonction `ajouter(total, couleur, nombre)` qui crée ou augmente l’entrée d’un dictionnaire ; `inventaire` parcourt `contenu[couleur].items()` et appelle `inventaire(x)` pour chaque sac contenu.
