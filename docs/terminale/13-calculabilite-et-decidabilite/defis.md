# Défis Advent of Code

<p class="sous-titre">Calculabilité et décidabilité</p>

## <span class="etiquette">Défi 1</span> Handheld Halting

*la console bloquée — interpréteur et problème de l’arrêt*

<p class="infos-activite">Jour 8</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/13-defi-aoc-2020-08){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-13-defi-aoc-2020-08.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/8 ](https://adventofcode.com/2020/day/8 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (lien ci-dessus) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

!!! encadre "Le défi en bref"

    **Le problème.** Une console de jeu exécute un petit programme de plusieurs centaines d’instructions, qui tourne en rond. Il faut d’abord détecter la boucle infinie et dire où en est la machine à ce moment, puis trouver l’unique instruction à corriger pour que le programme se termine. Suivre des centaines de sauts à la main est impossible : on va écrire un **interpréteur**, c’est-à-dire un programme Python qui exécute ce programme.

    **Ce qu’on réinvestit.** Le **problème de l’arrêt** vu dans ce chapitre. On sait qu’aucun programme ne peut décider, pour tout programme, s’il s’arrête. Pourtant, on va ici détecter une boucle infinie à coup sûr : c’est possible seulement parce que cette machine a un nombre fini d’états. Le défi permet de comprendre précisément où passe la frontière entre ce qui est décidable et ce qui ne l’est pas.

    **La démarche de la fiche.**

    1.  Comprendre les trois instructions, puis exécuter un petit programme à la main.

    2.  Lire le programme du fichier dans une liste de tuples.

    3.  Écrire un interpréteur qui s’arrête dès qu’une instruction revient : c’est la partie 1.

    4.  Partie 2 : essayer chaque réparation possible avec ce même interpréteur.

    5.  En approfondissement, réduire le nombre d’essais, jusqu’à une réparation en temps linéaire.

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|                      |                        |             |              |
|:---------------------|:-----------------------|:------------|:-------------|
| boot code            | programme de démarrage | instruction | instruction  |
| operation / argument | opération / argument   | accumulator | accumulateur |
| jump                 | saut                   | offset      | décalage     |
| infinite loop        | boucle infinie         | terminate   | se terminer  |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** En plein vol, un enfant assis à côté du héros n’arrive plus à démarrer sa console de jeu portable : son programme de démarrage tourne en rond. On veut comprendre où il se bloque.

    **Les données.** Le fichier contient ce programme, écrit dans un langage très simple, avec une instruction par ligne. Une instruction est formée d’une opération (`acc`, `jmp` ou `nop`), d’un espace, puis d’un entier toujours écrit avec son signe (`+4`, `-20`). La machine ne possède qu’une seule mémoire, l’*accumulateur*, qui vaut 0 au départ.

    **La règle.**

    - `acc n` ajoute `n` à l’accumulateur, puis passe à la ligne suivante.

    - `jmp n` est un saut de `n` lignes compté à partir de l’instruction courante : `jmp +1` va à la ligne suivante, `jmp -2` remonte de deux lignes.

    - `nop n` ne fait rien (l’argument est ignoré) et passe à la ligne suivante.

    - On commence à la première ligne, et l’on exécute les instructions une à une.

    - Le programme finit par boucler : dès qu’une instruction est sur le point d’être exécutée une deuxième fois, on s’arrête **avant** de l’exécuter.

    **La réponse attendue.** La valeur de l’accumulateur à ce moment. Par exemple, pour le programme de trois lignes `acc +3`, `acc -1`, `jmp -2`, l’accumulateur vaut 3 puis 2, puis le saut ramène à la première ligne, déjà exécutée : la réponse serait 2.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-13-calculabilite-et-decidabilite-aoc-1-1 }

**But.** Vérifier qu’on sait exécuter les instructions dans les cas particuliers.

**À quoi ça sert ?** La première question montre qu’un saut nul boucle sur place et qu’un `nop` ignore son argument ; la seconde précise le moment exact de l’arrêt, donc la valeur de l’accumulateur à renvoyer.

Après lecture de l’énoncé et du résumé, vérifier sa compréhension :

1.  Que fait l’instruction `jmp +0` ? Et `nop -5` ?

2.  Si l’instruction qui revient est un `acc`, son ajout est-il compté une seconde fois ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-13-calculabilite-et-decidabilite-aoc-1-2 }

**But.** Exécuter un programme de huit lignes à la main, en notant l’accumulateur après chaque instruction.

**À quoi ça sert ?** Le tableau obtenu est exactement ce que l’interpréteur devra calculer ; il donne un exemple dont on **connaît la réponse** (`8`), et il servira à retrouver une erreur pas à pas en cas de résultat faux.

```console
acc +2
jmp +3
acc +10
jmp +3
nop -2
acc -4
jmp -4
acc +7
```

On considère le programme (inventé) suivant, dont les lignes sont numérotées à partir de 0.

Exécuter le programme à la main dans un tableau à trois colonnes : numéro de ligne, instruction, accumulateur après l’instruction. Vérification : on doit trouver `8`.

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Lire le programme <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-13-calculabilite-et-decidabilite-aoc-1-3 }

**But.** Transformer chaque ligne du fichier en un tuple (opération, argument entier).

**À quoi ça sert ?** L’interpréteur travaille sur cette liste : la ligne numéro `ip` du programme est simplement `programme[ip]`. Les arguments doivent être des entiers pour pouvoir être ajoutés à l’accumulateur ou au numéro de ligne.

Construire la liste `programme` de tuples `(operation, argument)`, l’argument étant un entier. Par exemple la ligne `jmp -4` donne `("jmp", -4)`.

??? pouce "Coup de pouce"

    `int("+3")` et `int("-4")` fonctionnent directement : pas besoin de traiter le signe à part.

!!! encadre "Outil Python : les ensembles (set) — rappel"

    Tout est présenté dans l’encadré « Outil Python : les ensembles » du défi *Crab Combat* (chapitre 4) : ensemble vide `set()`, ajout avec `add`, retrait avec `remove`, test `x in ensemble` en temps constant, éléments non modifiables (tuples). Un ensemble ne contient jamais deux fois le même élément.

    **À essayer.** Que vaut `len(vus)` après `vus = {1, 2}` puis `vus.add(2)` ?

### <span class="exo-num">Exercice 4</span> — Un interpréteur <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-13-calculabilite-et-decidabilite-aoc-1-4 }

**But.** Simuler la machine, une instruction par tour de boucle, et s’arrêter dès qu’une instruction revient.

**À quoi ça sert ?** C’est la réponse de la partie 1. Cet interpréteur est l’outil central du défi : la partie 2 le réutilise pour tester chaque réparation possible.

Écrire une fonction `executer(programme)` qui simule la machine : une variable `acc`, une variable `ip` (numéro de l’instruction courante), et une boucle qui exécute une instruction par tour. La fonction s’arrête dès qu’une instruction s’apprête à être exécutée pour la deuxième fois et renvoie `acc`. Tester sur l’exemple du défi, puis sur vos données.

??? pouce "Coup de pouce"

    Garder dans un ensemble `deja_vues` les numéros des instructions exécutées. La condition de la boucle `while` porte sur `ip`.

!!! encadre "Le problème de l’arrêt : rappel du cours"

    Peut-on écrire un programme `arret(P, x)` qui dirait, pour **tout** programme `P` et toute entrée `x`, si `P` finit par s’arrêter sur `x` ? Turing a démontré en 1936 que non : ce problème est *indécidable*. On le prouve par l’absurde, en construisant un programme qui fait le contraire de ce que `arret` prédit pour lui-même.

    Pourquoi la détection réussit-elle ici ? Parce que la machine de l’énigme a un état **fini** : l’état ne dépend que de `ip`, et l’accumulateur n’influence jamais la suite des instructions. Si une instruction revient, tout se répète à l’identique. Un programme quelconque peut, lui, utiliser une mémoire non bornée sans jamais repasser par le même état.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    **Ce qui change.** Il faut maintenant réparer la console pour que le programme aille jusqu’au bout. Les instructions s’exécutent toujours de la même façon ; on cherche quelle ligne modifier.

    **La nouvelle règle.**

    - Exactement une instruction est fautive : un `jmp` devrait être un `nop`, ou un `nop` un `jmp`. L’argument ne change pas, et les `acc` sont corrects.

    - Le programme réparé se termine, c’est-à-dire qu’il cherche à exécuter la ligne qui suit immédiatement la dernière.

    **La réponse attendue.** La valeur de l’accumulateur quand le programme réparé se termine. Par exemple, le programme `acc +4`, `jmp -1` boucle ; en remplaçant `jmp -1` par `nop -1`, il se termine avec un accumulateur égal à 4.

!!! encadre "Méthode : copier une liste avec une tranche (a[:])"

    Écrire `b = a` ne copie pas la liste : `a` et `b` désignent la **même** liste, et modifier l’une modifie « l’autre ». La tranche complète `a[:]` (du début à la fin) fabrique une nouvelle liste contenant les mêmes éléments.

    ```python
    a = [1, 2, 3]
    b = a              # meme liste, deux noms
    b[0] = 9
    print(a)           # [9, 2, 3] : a a change aussi !
    c = a[:]           # vraie copie : une nouvelle liste
    c[0] = 0
    print(a, c)        # [9, 2, 3] [0, 2, 3]
    ```

    **Intérêt.** Chaque essai de la partie 2 part d’un programme intact. Une copie coûte un temps proportionnel à la longueur de la liste.

    **À essayer.** Avec `a = [[1], [2]]` et `c = a[:]`, que devient `a` après `c[0].append(5)` ? Pourquoi n’est-ce pas un problème pour une liste de tuples ?

### <span class="exo-num">Exercice 5</span> — Réparer le programme <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-13-calculabilite-et-decidabilite-aoc-1-5 }

**But.** Essayer une à une les réparations autorisées et repérer celle qui fait terminer le programme.

**À quoi ça sert ?** C’est la réponse de la partie 2. Il faut pour cela que l’interpréteur distingue une fin normale d’une boucle, et que chaque essai parte du programme d’origine.

1.  Modifier `executer` pour qu’elle renvoie aussi un booléen indiquant si le programme s’est terminé normalement. Quelle condition sur `ip` signale une fin normale ?

2.  Essayer toutes les modifications autorisées par l’énoncé, une à une, jusqu’à trouver celle qui fait terminer le programme. Sur l’exemple du défi, on doit obtenir `5`.

??? pouce "Coup de pouce"

    Chaque essai doit partir du programme **d’origine** : si l’on modifie la liste sans la recopier, les modifications s’accumulent d’un essai à l’autre.

??? pouce "Coup de pouce 2 (début de solution)"

    `copie = programme[:]`, puis on remplace un seul tuple de `copie`. Inutile d’essayer les lignes `acc`.

## Approfondissement

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 6</span> — Défi : combien d’exécutions ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-13-calculabilite-et-decidabilite-aoc-1-6 }

**But.** Évaluer le coût de la méthode par essais successifs, puis réduire le nombre d’essais.

**À quoi ça sert ?** La méthode précédente relance tout le programme à chaque essai : estimer son coût au pire montre ce qu’on peut gagner en éliminant les essais inutiles.

Pour un programme de $n$ instructions, combien d’instructions la méthode précédente exécute-t-elle au pire ? Proposer et tester une idée pour réduire le nombre d’essais.

??? pouce "Coup de pouce"

    Modifier une instruction jamais atteinte par l’exécution de la partie 1 ne change rien.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 1 : une réparation en temps linéaire <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-13-calculabilite-et-decidabilite-aoc-1-7 }

**But.** Trouver la ligne à réparer sans essais, en voyant le programme comme un graphe de lignes.

**À quoi ça sert ?** En remontant les flèches depuis la fin du programme, on sait d’avance quelles lignes y mènent : une seule exécution réparée suffit. Le problème de réparation, qui semblait demander de nombreux essais, se résout en temps linéaire.

On note $n$ le nombre de lignes et $\mathrm{succ}(k)$ la ligne exécutée juste après la ligne $k$ ; la valeur $n$ représente la fin du programme.

1.  Sur l’exemple du défi, donner $\mathrm{succ}(k)$ pour $k$ de $0$ à $7$.

2.  Quelles lignes mènent, sans modification, jusqu’à la fin $8$ ? On les trouve en **remontant** les flèches depuis $8$.

3.  Parmi les lignes atteintes lors de l’exécution de la partie 1, laquelle, une fois échangée (`jmp` et `nop`), envoie vers une ligne trouvée à la question 2 ?

4.  Écrire `reparer_lineaire(programme)` qui applique cette méthode et renvoie l’accumulateur du programme réparé. Quelle est sa complexité ?

??? pouce "Coup de pouce"

    Construire le graphe inverse : un dictionnaire qui associe à chaque ligne $s$ la liste des lignes $k$ telles que $\mathrm{succ}(k) = s$. Un parcours (avec une pile) depuis $n$ donne l’ensemble `vers_fin`.

??? pouce "Coup de pouce 2 (début de solution)"

    Une seule exécution réparée suffit à la fin. Pourquoi est-on sûr qu’elle se termine ? Si la ligne $k$ modifiée était sur le chemin de la nouvelle ligne vers la fin, $k$ serait dans `vers_fin`, et le programme d’origine se terminerait.

## <span class="etiquette">Défi 2</span> Conway Cubes

*les cubes de Conway — ensembles et simulation en 3D puis 4D*

<p class="infos-activite">Jour 17</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/13-defi-aoc-2020-17){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-13-defi-aoc-2020-17.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/17 ](https://adventofcode.com/2020/day/17 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (lien ci-dessus) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

!!! encadre "Le défi en bref"

    **Le problème.** On part d’une petite grille plate de cases allumées ou éteintes, plongée dans un espace infini. À chaque étape, chaque case s’allume ou s’éteint selon le nombre de ses voisines allumées. On veut savoir combien de cases sont allumées après six étapes. La zone allumée grandit dans toutes les directions et chaque case a 26 voisines (80 en dimension 4) : impossible de suivre cela à la main.

    **Ce qu’on réinvestit.** Ce défi est une variante en trois dimensions du *jeu de la vie* de Conway, dont la version plane est un exemple célèbre de système Turing-complet, notion vue dans ce chapitre : des règles locales très simples suffisent à produire des comportements aussi riches qu’un programme. Côté programmation, on représente l’espace infini par l’**ensemble** des seules cases allumées, et on construit les voisins d’un point de façon à ce que la dimension soit un simple paramètre.

    **La démarche de la fiche.**

    1.  Comprendre les règles (voisinage, allumage, extinction) et les appliquer à la main sur un petit exemple.

    2.  Lire le fichier dans un ensemble de coordonnées.

    3.  Écrire la fonction des voisins, puis celle qui calcule un cycle : six cycles donnent la réponse de la partie 1.

    4.  Passer en dimension 4 en modifiant le moins de code possible, puis écrire un code valable pour toute dimension.

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|          |                             |                   |                 |
|:---------|:----------------------------|:------------------|:----------------|
| cube     | cube (une case de l’espace) | active / inactive | actif / inactif |
| neighbor | voisin                      | coordinate        | coordonnée      |
| cycle    | cycle, étape                | simultaneously    | en même temps   |
| slice    | tranche, coupe              | boot up           | démarrer        |
| infinite | infini                      | dimension         | dimension       |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Les elfes vous demandent de l’aide pour une source d’énergie expérimentale : une grille infinie de cubes, chacun actif ou inactif, qui évolue par cycles selon l’état de ses voisins. C’est une version en trois dimensions du célèbre *jeu de la vie* de Conway. Avant de démarrer la source, il faut prévoir son état après la phase de démarrage, qui dure six cycles.

    **Les données.** Le fichier est une petite grille de `#` (actif) et de `.` (inactif), toutes les lignes ayant la même longueur. C’est la tranche $z = 0$ de l’espace : le caractère de la ligne $y$, colonne $x$ (en numérotant à partir de 0), donne l’état du cube $(x, y, 0)$. Tous les autres cubes de l’espace, en nombre infini, sont inactifs au départ.

    **La règle.**

    - Les voisins d’un cube sont les 26 cubes dont chaque coordonnée diffère d’au plus 1 de la sienne : les cubes qui le touchent par une face, une arête ou un coin. Un cube n’est pas son propre voisin.

    - À chaque cycle, on compte les voisins actifs de chaque cube **dans l’état d’avant le cycle**, puis tous les cubes changent **en même temps**.

    - Un cube actif reste actif s’il a exactement 2 ou 3 voisins actifs ; sinon, il devient inactif.

    - Un cube inactif devient actif s’il a exactement 3 voisins actifs ; sinon, il reste inactif.

    - Des cubes situés hors de la grille de départ (y compris hors du plan $z = 0$) peuvent donc s’allumer : la zone active grandit.

    **La réponse attendue.** Le nombre de cubes actifs après 6 cycles. Par exemple, avec trois cubes actifs alignés au départ, le cube du milieu reste seul actif parmi eux (2 voisins actifs), les deux bouts s’éteignent (1 seul voisin actif) et 8 cubes qui entourent le milieu s’allument : après un cycle, il y a 9 cubes actifs.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-13-calculabilite-et-decidabilite-aoc-2-1 }

**But.** Vérifier sa compréhension du voisinage et des deux règles d’évolution.

**À quoi ça sert ?** Ce sont exactement les tests que fera la fonction `cycle` ; la dernière question explique pourquoi on ne pourra pas se contenter de parcourir la grille de départ.

Questions de vérification, à traiter sur le cahier :

1.  Le cube $(0, 0, 0)$ est-il voisin de $(1, 1, -1)$ ? De $(2, 0, 0)$ ?

2.  Un cube actif qui a 4 voisins actifs reste-t-il actif ? Un cube inactif qui en a 2 devient-il actif ?

3.  Un cube situé en dehors de la grille de départ peut-il devenir actif ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-13-calculabilite-et-decidabilite-aoc-2-2 }

**But.** Appliquer les règles à la main sur une grille de 3 lignes.

**À quoi ça sert ?** On obtient des valeurs de référence (5 cubes au départ, 12 après un cycle) qui serviront à tester chaque fonction avant de lancer la simulation sur les vraies données.

On considère l’état initial (inventé) suivant, dans le plan $z = 0$ :

```console
#.#
.##
#..
```

Combien de cubes actifs au départ ? Compter les voisins actifs du cube central $(1, 1, 0)$ et dire s’il reste actif. Vérification : après un cycle, il y a `12` cubes actifs ; après six cycles, `138`.

## Programmer la partie 1

!!! encadre "Outil Python : les ensembles (set) — rappel"

    Tout est présenté dans l’encadré « Outil Python : les ensembles » du défi *Crab Combat* (chapitre 4) : `set()`, `add`, `remove`, test `x in ensemble` en temps constant, éléments non modifiables (tuples).

    **À essayer.** Essayer `actifs = set()` puis `actifs.add([1, 2, 3])` : que se passe-t-il ? Pourquoi range-t-on les cubes sous forme de tuples `(x, y, z)` ? L’ensemble en compréhension `{(x, 0, 0) for x in range(3)}` contient les trois cubes d’une ligne.

!!! encadre "Outil Python : strip (nettoyer une ligne lue)"

    Chaque ligne renvoyée par `readlines()` se termine par le caractère de fin de ligne `"\n"` (sauf parfois la dernière). `ligne.strip()` renvoie une copie de la ligne sans les espaces ni les fins de ligne placés au début et à la fin.

    ```python
    ligne = "1721\n"
    print(ligne.strip())                  # 1721
    print(len(ligne), len(ligne.strip())) # 5 4
    ```

    **Intérêt.** Comparer ou découper une ligne sans que la fin de ligne ne gêne : `"abc\n" == "abc"` vaut `False`.

### <span class="exo-num">Exercice 3</span> — Un ensemble de tuples <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-13-calculabilite-et-decidabilite-aoc-2-3 }

**But.** Lire le fichier et ne garder que les coordonnées des cubes actifs, dans un ensemble.

**À quoi ça sert ?** Un tableau ne peut pas représenter un espace infini qui grandit à chaque cycle ; l’ensemble des cubes actifs, lui, ne stocke que l’utile et permet de savoir en temps constant si un cube est actif. Toute la simulation travaillera sur cet ensemble.

L’espace est infini : pas de liste de listes. Écrire une fonction `lire_actifs(nom_fichier)` qui renvoie l’**ensemble** des coordonnées `(x, y, 0)` des cubes actifs. Vérifier qu’on obtient 5 éléments sur l’exemple.

??? pouce "Coup de pouce"

    Un `set` de tuples : l’appartenance `(x, y, z) in actifs` se teste en temps quasi constant, et un cube inactif n’est tout simplement pas dans l’ensemble.

!!! encadre "Méthode : construire les décalages coordonnée par coordonnée"

    Pour obtenir tous les tuples de longueur `d` formés de $-1$, $0$ et $1$, on part de la liste `[()]` (le tuple vide) et, à chaque tour, on prolonge chaque tuple par $-1$, par $0$ et par $1$ : la longueur des tuples augmente de 1 et leur nombre est multiplié par 3.

    ```python
    tuples = [()]
    for _ in range(2):                         # deux coordonnees
        tuples = [t + (c,) for t in tuples for c in (-1, 0, 1)]
    print(tuples)       # [(-1, -1), (-1, 0), (-1, 1), (0, -1), ..., (1, 1)]
    print(len(tuples))  # 9 : 3 ** 2 couples
    ```

    **Intérêt.** Le nombre de boucles imbriquées devient un **paramètre** : le même code sert en dimension 3, 4 ou plus.

    **À essayer.** Combien de tuples obtient-on avec 4 tours de boucle ? Lequel faut-il retirer pour obtenir les décalages vers les voisins ?

### <span class="exo-num">Exercice 4</span> — Les voisins <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-13-calculabilite-et-decidabilite-aoc-2-4 }

**But.** Obtenir la liste des 26 voisins d’un cube.

**À quoi ça sert ?** Compter les voisins actifs d’un cube, c’est parcourir cette liste et tester l’appartenance à l’ensemble des actifs : cette fonction est appelée des milliers de fois par cycle, et c’est la seule qui changera vraiment en dimension 4.

Écrire une fonction `voisins(cube)` qui renvoie la liste des 26 voisins d’un cube. La tester sur `(0, 0, 0)`.

??? pouce "Coup de pouce"

    Trois boucles imbriquées sur les décalages dans `[-1, 0, 1]`, en excluant le décalage nul.

### <span class="exo-num">Exercice 5</span> — Un cycle <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-13-calculabilite-et-decidabilite-aoc-2-5 }

**But.** Calculer l’ensemble des cubes actifs après un cycle, puis répéter six fois.

**À quoi ça sert ?** C’est la simulation elle-même : six appels successifs donnent la réponse de la partie 1. La difficulté est de choisir les cubes à examiner, puisqu’on ne peut pas parcourir un espace infini.

Écrire une fonction `cycle(actifs)` qui renvoie le **nouvel** ensemble des cubes actifs. Quels cubes faut-il examiner ? Pas seulement les cubes actifs : la zone active grandit à chaque cycle. Simuler six cycles sur l’exemple du défi, puis sur vos données.

??? pouce "Coup de pouce"

    Seul un cube voisin d’au moins un cube actif peut être actif après le cycle. Les cubes à examiner sont donc les cubes actifs et leurs voisins.

??? pouce "Coup de pouce 2 (début de solution)"

    Plus efficace : parcourir les cubes actifs et, pour chacun de leurs voisins, ajouter 1 dans un dictionnaire `compte`. On applique ensuite les règles à chaque clé de `compte` ; un cube actif absent de `compte` n’a aucun voisin actif.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    **Ce qui change.** Mauvaise surprise : la source d’énergie fonctionne en réalité dans un espace à quatre dimensions. Chaque cube a donc une quatrième coordonnée $w$, et beaucoup plus de voisins.

    **La nouvelle règle.**

    - Les points sont des quadruplets $(x, y, z, w)$ ; la grille du fichier donne l’état des points $(x, y, 0, 0)$, tous les autres sont inactifs.

    - Les voisins sont définis de la même façon : chaque coordonnée diffère d’au plus 1, le point lui-même exclu.

    - Les règles d’allumage et d’extinction sont exactement les mêmes qu’en partie 1.

    **La réponse attendue.** Le nombre de cubes actifs après 6 cycles, en dimension 4.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Une dimension de plus <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-13-calculabilite-et-decidabilite-aoc-2-6 }

**But.** Adapter la lecture et les voisins à la dimension 4, sans toucher à la logique du cycle.

**À quoi ça sert ?** Si les fonctions ont été bien découpées, la règle d’évolution ne dépend pas de la dimension : seules les fonctions qui fabriquent les points changent, et la réponse de la partie 2 s’obtient presque gratuitement.

Combien de voisins un point a-t-il en dimension 4 ? Si votre code est bien écrit, peu de choses changent : adapter `lire_actifs` et `voisins`. Sur l’exemple du défi, on doit trouver `36` cubes actifs après un cycle et `680` après six cycles.

??? pouce "Coup de pouce"

    En dimension $d$, un point a $3^d - 1$ voisins.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 7</span> — Défi : un code pour toutes les dimensions <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-13-calculabilite-et-decidabilite-aoc-2-7 }

**But.** Écrire une seule fonction de simulation où la dimension est un paramètre.

**À quoi ça sert ?** Plutôt que deux programmes presque identiques, un seul code résout les deux parties : c’est la généralisation, et elle permet aussi de mesurer comment le temps de calcul explose quand la dimension augmente.

Écrire `voisins(point)` pour un tuple de longueur quelconque, sans écrire une boucle par dimension, et une fonction `simuler(grille, dimension, nb_cycles)` qui sert aux deux parties. Que donne la dimension 2 ? Et la dimension 5 sur l’exemple (mesurer le temps) ?

??? pouce "Coup de pouce"

    Construire les décalages coordonnée par coordonnée (voir l’encadré « Méthode »), ou utiliser la fonction récursive de l’approfondissement 1.

## Approfondissement

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — Approfondissement 1 : les décalages par récursivité <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-13-calculabilite-et-decidabilite-aoc-2-8 }

**But.** Construire les décalages vers les voisins avec une fonction récursive.

**À quoi ça sert ?** La liste des décalages en dimension $d$ se déduit de celle en dimension $d - 1$ : c’est une définition récursive naturelle, qui donne un code court valable pour toute dimension, et une autre manière de répondre au défi précédent.

On veut construire la liste des décalages par une fonction récursive, plutôt qu’avec la boucle de l’encadré « Méthode ».

1.  Lister à la main les tuples de longueur 1 formés de $-1$, $0$, $1$, puis ceux de longueur 2, obtenus en plaçant $-1$, $0$ ou $1$ devant chacun des précédents. Combien y en a-t-il en longueur $d$ ?

2.  Écrire une fonction récursive `decalages_rec(dimension)` qui renvoie les $3^d$ tuples, le tuple nul compris. Le cas de base est la dimension 0, qui renvoie `[()]` (une liste contenant le tuple vide).

    ??? pouce "Coup de pouce"

        `(-1,)` est un tuple à un seul élément (la virgule est obligatoire), et `(-1,) + (0, 1)` vaut `(-1, 0, 1)`.

    ??? pouce "Coup de pouce 2 (début de solution)"

        Pour chaque `debut` dans `(-1, 0, 1)` et chaque `fin` de `decalages_rec(dimension - 1)`, ajouter `(debut,) + fin` au résultat.

3.  Vérifier qu’une fois le tuple nul retiré, on obtient les mêmes décalages qu’avec la méthode coordonnée par coordonnée en dimension 3 et 4, puis l’utiliser dans `simuler`.

4.  Combien d’appels récursifs fait `decalages_rec(d)` ? Combien de voisins un point a-t-il en dimension 5 ?
