# Défis Advent of Code

<p class="sous-titre">Spécifier et mettre au point ses programmes</p>

## <span class="etiquette">Défi</span> Trebuchet?!

*l’étalonnage du trébuchet — chiffres dans une chaîne*

<p class="infos-activite">Jour 1</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/05-defi-aoc-2023-01){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/premiere-05-defi-aoc-2023-01.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2023/day/1 ](https://adventofcode.com/2023/day/1 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (lien ci-dessus) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

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

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-aoc-1-1 }

Après lecture du résumé (et de l’énoncé), vérifier sa compréhension sur ces cas particuliers :

1.  Que vaut la ligne `a7b` ? et `k0z5` ?

2.  Une ligne `x45y` vaut-elle 45, 4 ou 9 ?

3.  Quel type de données a un caractère comme `"7"` ? Que donne `"7" + "2"` ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-aoc-1-2 }

On considère le fichier (inventé) suivant :

```console
x3yz7k
ab5cd
9
q12w34e
```

Donner la valeur de chaque ligne. Vérification : on doit obtenir `205`. Attention : la valeur de `q12w34e` n’est pas $12 + 34$.

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Lire le fichier <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-aoc-1-3 }

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

### <span class="exo-num">Exercice 4</span> — Les chiffres d’une ligne <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-aoc-1-4 }

Écrire une fonction `chiffres(ligne)` qui renvoie la liste des chiffres de la ligne, dans l’ordre, sous forme de chaînes. Tester : `chiffres("q12w34e")` doit valoir `["1", "2", "3", "4"]`.

??? pouce "Coup de pouce"

    La méthode `c.isdigit()` renvoie `True` si le caractère `c` est un chiffre.

### <span class="exo-num">Exercice 5</span> — Valeur d’une ligne et total <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-aoc-1-5 }

Écrire une fonction `valeur(ligne)` puis calculer la somme sur tout le fichier. Vérifier `205` sur l’exemple.

??? pouce "Coup de pouce"

    Le premier élément d’une liste `L` est `L[0]`, le dernier `L[-1]` (ou `L[len(L) - 1]`).

??? pouce "Coup de pouce 2 (début de solution)"

    Accoler deux **chaînes** avec `+` puis convertir : `int(L[0] + L[-1])`. Si l’on additionnait des entiers, on obtiendrait une somme et non un nombre à deux chiffres.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    On s’aperçoit que certains chiffres étaient écrits en toutes lettres. Les chiffres de 1 à 9 écrits en anglais (`one`, `two`, …, `nine`) comptent maintenant aussi comme des chiffres. La valeur d’une ligne se calcule comme avant, avec le premier et le dernier chiffre, qu’ils soient écrits avec un chiffre ou en lettres.

### <span class="exo-num">Exercice 6</span> — Des chiffres en toutes lettres <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-aoc-1-6 }

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

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 1 : chercher par les deux bouts <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-aoc-1-7 }

On n’a besoin que du premier et du dernier chiffre.

1.  À la main, sur `zoneight` : en partant de la fin, à quel indice trouve-t-on pour la première fois un chiffre ou le début d’un mot ?

2.  Écrire une fonction `chiffre_en(ligne, i)` qui renvoie le chiffre (sous forme de chaîne) qui commence à l’indice `i`, ou `""` s’il n’y en a pas.

3.  En déduire une version qui parcourt la ligne depuis le début jusqu’au premier chiffre trouvé, puis depuis la fin jusqu’au dernier, sans construire la liste complète. Pourquoi le chevauchement de mots ne pose-t-il alors plus aucun problème ?

    ??? pouce "Coup de pouce"

        Deux boucles `while` : l’une avec un indice qui monte depuis `0`, l’autre avec un indice qui descend depuis `len(ligne) - 1`. Chacune s’arrête dès que `chiffre_en` renvoie autre chose que `""`.
