# Défis Advent of Code

<p class="sous-titre">Spécifier et mettre au point ses programmes</p>

## <span class="etiquette">Défi 1</span> Inventory Management System

*l’inventaire — compter des lettres, double boucle*

<p class="infos-activite">Jour 2</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/05-defi-aoc-2018-02){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/premiere-05-defi-aoc-2018-02.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2018/day/2 ](https://adventofcode.com/2018/day/2 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/05-defi-aoc-2018-02>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

*Ce défi est l’occasion d’appliquer la démarche de ce chapitre : spécifier chaque petite fonction et la tester avec des `assert` avant de l’utiliser.*

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|               |                      |                |                   |
|:--------------|:---------------------|:---------------|:------------------|
| box ID        | identifiant de boîte | checksum       | somme de contrôle |
| exactly two   | exactement deux      | count          | compter, nombre   |
| letter        | lettre               | differ by      | différer de       |
| same position | même position        | common letters | lettres communes  |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Dans l’entrepôt des elfes, on cherche deux boîtes qui contiennent un tissu précieux. Chaque boîte porte un identifiant fait de lettres minuscules, et le fichier donne la liste de ces identifiants, un par ligne. Avant de chercher les boîtes, on calcule une « somme de contrôle » de la liste, qui sert à vérifier qu’on a bien recopié tous les identifiants.

    **Ce qu’il faut faire.**

    - On compte $A$, le nombre d’identifiants dans lesquels **au moins une** lettre apparaît **exactement deux fois**.

    - On compte $B$, le nombre d’identifiants dans lesquels au moins une lettre apparaît **exactement trois fois**.

    - Un identifiant compte au plus une fois dans $A$, même s’il a plusieurs lettres doubles ; il peut en revanche compter à la fois dans $A$ et dans $B$.

    - Réponse : le produit $A \times B$.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-aoc-1-1 }

Après lecture du résumé (et de l’énoncé), vérifier sa compréhension sur ces cas particuliers :

1.  Une lettre présente quatre fois rend-elle l’identifiant « double » ?

2.  L’identifiant `aabbcc` ajoute-t-il 1 ou 3 au compte $A$ ?

3.  Que vaut la réponse si aucun identifiant n’a de lettre triple ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-aoc-1-2 }

On considère le fichier (inventé) suivant :

```console
mnoppq
rrsttt
uvwxyz
aabbcc
dedede
fghfgk
```

Pour chaque identifiant, noter s’il contient une lettre exactement deux fois, une lettre exactement trois fois. Vérification : on doit obtenir `8`.

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Lire le fichier <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-aoc-1-3 }

Rappel pour lire un fichier ligne par ligne :

```python
fichier = open("input.txt", encoding="utf-8")
for ligne in fichier:
    ligne = ligne.strip()   # enlève le retour à la ligne final
fichier.close()
```

Construire la liste `identifiants` des chaînes du fichier et afficher sa longueur.

??? pouce "Coup de pouce"

    Partir d’une liste vide `identifiants = []` et, dans la boucle, faire `identifiants.append(ligne)`.

!!! encadre "Outil Python : compter dans une chaîne (count)"

    La méthode `count` d’une chaîne renvoie le nombre d’apparitions d’un caractère, ou d’un morceau de chaîne, dans cette chaîne.

    ```python
    mot = "banane"
    print(mot.count("a"))      # 2 : nombre d'apparitions du caractere "a"
    print(mot.count("an"))     # 2 : marche aussi avec un morceau de chaine
    print(mot.count("z"))      # 0 : absent
    ```

    **Intérêt.** Elle évite d’écrire soi-même une boucle de comptage. Attention, elle parcourt toute la chaîne à chaque appel : l’appeler pour chaque lettre d’un mot de longueur $m$ coûte environ $m^2$ opérations.

    *À essayer.* Que renvoie `"banane".count("ana")` ? Pourquoi pas 2 ?

### <span class="exo-num">Exercice 4</span> — Compter les lettres <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-aoc-1-4 }

Écrire une fonction `a_une_lettre_n_fois(mot, n)` qui renvoie `True` si au moins une lettre de `mot` apparaît exactement `n` fois. Tester : `a_une_lettre_n_fois("dedede", 3)` vaut `True` et `a_une_lettre_n_fois("dedede", 2)` vaut `False`.

??? pouce "Coup de pouce"

    Pour chaque lettre du mot, compter combien de fois elle apparaît dans le mot avec une boucle (ou la méthode `mot.count(lettre)`).

??? pouce "Coup de pouce 2 (début de solution)"

    `for lettre in mot:` puis `if mot.count(lettre) == n:` on peut renvoyer `True` tout de suite. Après la boucle, renvoyer `False`.

### <span class="exo-num">Exercice 5</span> — La somme de contrôle <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-aoc-1-5 }

Écrire une fonction `somme_controle(identifiants)` qui compte les identifiants concernés par « deux », ceux concernés par « trois » et renvoie la réponse. Vérifier `8` sur l’exemple, puis lancer sur vos données.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    Il reste à trouver les deux boîtes au tissu précieux : ce sont les deux seules dont les identifiants diffèrent d’**exactement un caractère**, à la même position (toutes les autres positions sont identiques). La réponse est la chaîne des caractères communs, autrement dit l’un des deux identifiants privé du caractère qui diffère.

### <span class="exo-num">Exercice 6</span> — Différer d’un seul caractère <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-aoc-1-6 }

Écrire une fonction `nb_differences(mot1, mot2)` qui compte les positions où les deux mots (de même longueur) ont des caractères différents. Tester : `nb_differences("lunes", "lunas")` vaut `1`.

??? pouce "Coup de pouce"

    Une boucle sur les indices `i` de `0` à `len(mot1) - 1` et un compteur.

### <span class="exo-num">Exercice 7</span> — Chercher la bonne paire <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-aoc-1-7 }

Trouver les deux identifiants qui ne diffèrent que d’un caractère et afficher la réponse demandée. Sur le petit fichier (inventé) ci-dessous, on doit trouver `luns`.

```console
lunes
marte
lunas
sabor
```

??? pouce "Coup de pouce"

    Deux boucles imbriquées sur les **indices** `i` et `j` de la liste, avec `j > i` pour ne pas comparer un identifiant avec lui-même ni deux fois la même paire.

??? pouce "Coup de pouce 2 (début de solution)"

    Une fois la paire trouvée, construire une chaîne vide `commun = ""` et y ajouter (`commun += ...`) les caractères qui sont identiques à la même position dans les deux mots.

## Approfondissement

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — Approfondissement 1 : combien de comparaisons ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-aoc-1-8 }

1.  À la main : pour la liste de 4 identifiants de la partie 2, écrire toutes les paires que la double boucle compare. Combien y en a-t-il ?

2.  Le fichier contient $n$ identifiants. Combien de paires la double boucle examine-t-elle au pire ? Calculer ce nombre pour vos données.

    ??? pouce "Coup de pouce"

        Le premier identifiant est comparé aux $n - 1$ suivants, le deuxième aux $n - 2$ suivants, etc.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 9</span> — Approfondissement 2 : compter en un seul parcours <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-aoc-1-9 }

1.  À la main : construire le dictionnaire des effectifs des lettres de `fghfgk`.

2.  Écrire `a_une_lettre_n_fois_dico(mot, n)` qui construit ce dictionnaire en **un seul parcours** du mot, puis regarde si la valeur `n` figure parmi les valeurs. Vérifier qu’elle donne les mêmes résultats que la première version.

    ??? pouce "Coup de pouce"

        Pour chaque lettre : si elle est déjà une clé, ajouter 1 à sa valeur ; sinon, créer la clé avec la valeur 1.

    ??? pouce "Coup de pouce 2 (début de solution)"

        Le test final peut s’écrire `n in effectifs.values()`.

3.  Comparer le nombre d’opérations des deux versions pour un mot de longueur $m$.

## <span class="etiquette">Défi 2</span> Trebuchet?!

*l’étalonnage du trébuchet — chiffres dans une chaîne*

<p class="infos-activite">Jour 1</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/05-defi-aoc-2023-01){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/premiere-05-defi-aoc-2023-01.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2023/day/1 ](https://adventofcode.com/2023/day/1 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/05-defi-aoc-2023-01>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

*Ce défi est l’occasion d’appliquer la démarche de ce chapitre : tester chaque fonction avec des `assert` sur des cas limites choisis exprès, car la partie 2 cache un piège.*

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| calibration value | valeur d’étalonnage | digit | chiffre |
| combine | réunir, accoler | two-digit number | nombre à deux chiffres |
| sum | somme | spelled out | écrit en toutes lettres |
| amended | corrigé, modifié | letters | lettres |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Les elfes s’apprêtent à vous envoyer dans le ciel avec un trébuchet, mais son document de réglage a été « décoré » par un jeune elfe : à chaque ligne, les nombres utiles sont noyés au milieu de lettres et d’autres chiffres. Il faut retrouver, pour chaque ligne, une valeur de réglage avant le lancement.

    **Ce qu’il faut faire.**

    - Chaque ligne est une chaîne mêlant lettres et chiffres, avec au moins un chiffre.

    - La valeur d’une ligne est le nombre à deux chiffres formé par son **premier** chiffre suivi de son **dernier** chiffre. On accole les deux chiffres, on ne les additionne pas.

    - S’il n’y a qu’un chiffre, il sert à la fois de premier et de dernier.

    - Réponse : la somme des valeurs de toutes les lignes.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-aoc-2-1 }

Après lecture du résumé (et de l’énoncé), vérifier sa compréhension sur ces cas particuliers :

1.  Que vaut la ligne `a7b` ? et `k0z5` ?

2.  Une ligne `x45y` vaut-elle 45, 4 ou 9 ?

3.  Quel type de données a un caractère comme `"7"` ? Que donne `"7" + "2"` ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-aoc-2-2 }

On considère le fichier (inventé) suivant :

```console
x3yz7k
ab5cd
9
q12w34e
```

Donner la valeur de chaque ligne. Vérification : on doit obtenir `205`. Attention : la valeur de `q12w34e` n’est pas $12 + 34$.

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Lire le fichier <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-aoc-2-3 }

Rappel pour lire un fichier ligne par ligne :

```python
fichier = open("input.txt", encoding="utf-8")
for ligne in fichier:
    ligne = ligne.strip()   # enlève le retour à la ligne final
fichier.close()
```

Afficher les 5 premières lignes de vos données pour voir à quoi elles ressemblent.

!!! encadre "Outil Python : méthodes de chaînes (isdigit, startswith, replace)"

    `c.isdigit()` renvoie `True` si la chaîne `c` n’est faite que de chiffres. `ligne.startswith(mot, i)` dit si `mot` apparaît dans `ligne` à partir de l’indice `i`. `ligne.replace(a, b)` renvoie une copie de `ligne` où chaque `a` est remplacé par `b`.

    ```python
    print("4".isdigit(), "q".isdigit())     # True False
    ligne = "abcone2"
    print(ligne.startswith("one", 3))       # True : "one" commence a l'indice 3
    print(ligne.startswith("one", 2))       # False
    print(ligne[3:6] == "one")              # meme test avec une tranche
    print("onetwo".replace("one", "1"))     # 1two : remplace TOUTES les apparitions
    ```

    **Intérêt.** Ces méthodes évitent d’écrire des boucles de comparaison. `startswith(mot, i)` équivaut à la tranche `ligne[i:i + len(mot)] == mot`.

    *À essayer.* Que renvoie `"eightwo".replace("two", "2")` ? Le mot `eight` est-il encore lisible ?

### <span class="exo-num">Exercice 4</span> — Les chiffres d’une ligne <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-aoc-2-4 }

Écrire une fonction `chiffres(ligne)` qui renvoie la liste des chiffres de la ligne, dans l’ordre, sous forme de chaînes. Tester : `chiffres("q12w34e")` doit valoir `["1", "2", "3", "4"]`.

??? pouce "Coup de pouce"

    La méthode `c.isdigit()` renvoie `True` si le caractère `c` est un chiffre.

### <span class="exo-num">Exercice 5</span> — Valeur d’une ligne et total <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-aoc-2-5 }

Écrire une fonction `valeur(ligne)` puis calculer la somme sur tout le fichier. Vérifier `205` sur l’exemple.

??? pouce "Coup de pouce"

    Le premier élément d’une liste `L` est `L[0]`, le dernier `L[-1]` (ou `L[len(L) - 1]`).

??? pouce "Coup de pouce 2 (début de solution)"

    Accoler deux **chaînes** avec `+` puis convertir : `int(L[0] + L[-1])`. Si l’on additionnait des entiers, on obtiendrait une somme et non un nombre à deux chiffres.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    On s’aperçoit que certains chiffres étaient écrits en toutes lettres. Les chiffres de 1 à 9 écrits en anglais (`one`, `two`, …, `nine`) comptent maintenant aussi comme des chiffres. La valeur d’une ligne se calcule comme avant, avec le premier et le dernier chiffre, qu’ils soient écrits avec un chiffre ou en lettres.

### <span class="exo-num">Exercice 6</span> — Des chiffres en toutes lettres <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-aoc-2-6 }

Modifier la fonction `chiffres(ligne)` pour qu’elle reconnaisse aussi les chiffres écrits en toutes lettres, comme le demande la partie 2. Sur le fichier (inventé) ci-dessous, on doit obtenir `215`.

```console
twone4x
7pqrsixteen
zoneight
nine87seven
```

**Piège** : deux mots peuvent partager des lettres (regarder `twone` et `zoneight`). Une méthode qui remplace les mots par des chiffres dans la chaîne avec `replace` risque de détruire l’un des deux mots : vérifier votre programme sur ces lignes.

??? pouce "Coup de pouce"

    Ranger les neuf mots anglais dans une liste `mots`, dans l’ordre, de sorte que `mots[0]` soit le mot de 1. Le chiffre correspondant au mot d’indice `k` est alors `str(k + 1)`.

??? pouce "Coup de pouce 2 (début de solution)"

    Plutôt que de modifier la ligne, la parcourir indice par indice : à chaque indice `i`, regarder si le caractère est un chiffre, puis, pour chaque mot de la liste, si la ligne contient ce mot **à partir de** l’indice `i` (une tranche de la bonne longueur, ou `ligne.startswith(mot, i)`).

## Approfondissement

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 1 : chercher par les deux bouts <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-aoc-2-7 }

On n’a besoin que du premier et du dernier chiffre.

1.  À la main, sur `zoneight` : en partant de la fin, à quel indice trouve-t-on pour la première fois un chiffre ou le début d’un mot ?

2.  Écrire une fonction `chiffre_en(ligne, i)` qui renvoie le chiffre (sous forme de chaîne) qui commence à l’indice `i`, ou `""` s’il n’y en a pas.

3.  En déduire une version qui parcourt la ligne depuis le début jusqu’au premier chiffre trouvé, puis depuis la fin jusqu’au dernier, sans construire la liste complète. Pourquoi le chevauchement de mots ne pose-t-il alors plus aucun problème ?

    ??? pouce "Coup de pouce"

        Deux boucles `while` : l’une avec un indice qui monte depuis `0`, l’autre avec un indice qui descend depuis `len(ligne) - 1`. Chacune s’arrête dès que `chiffre_en` renvoie autre chose que `""`.
