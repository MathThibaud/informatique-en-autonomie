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

!!! encadre "Le défi en bref"

    **Le problème.** Chaque ligne du fichier mélange des lettres et des chiffres ; il faut en extraire le premier et le dernier chiffre, former un nombre à deux chiffres, puis additionner ces nombres sur un millier de lignes. Chaque ligne est facile à traiter à la main, mais il y en a beaucoup trop, et la partie 2 ajoute des chiffres écrits en toutes lettres.

    **Ce qu’on réinvestit.** La démarche de ce chapitre : **tester** chaque fonction sur des cas limites choisis exprès (une ligne à un seul chiffre, des mots qui se chevauchent…) avant de faire confiance au résultat. C’est indispensable ici, car la partie 2 cache un piège qui donne une réponse fausse sans aucun message d’erreur. On utilise aussi les chaînes, leurs tranches et la concaténation.

    **La démarche de la fiche.**

    1.  Comprendre la règle avec des questions courtes, puis traiter à la main un petit fichier dont on connaît la réponse.

    2.  Lire le fichier et observer à quoi ressemblent les lignes.

    3.  Écrire une fonction qui extrait les chiffres d’une ligne, puis une fonction qui calcule la valeur d’une ligne : la somme donne la partie 1.

    4.  Pour la partie 2, modifier seulement la fonction qui extrait les chiffres, en la testant sur des lignes piégées.

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| calibration value | valeur d’étalonnage | digit | chiffre |
| combine | réunir, accoler | two-digit number | nombre à deux chiffres |
| sum | somme | spelled out | écrit en toutes lettres |
| amended | corrigé, modifié | letters | lettres |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Les elfes s’apprêtent à vous envoyer dans le ciel avec un trébuchet, mais son document de réglage a été « décoré » par un jeune elfe : à chaque ligne, les nombres utiles sont noyés au milieu de lettres et d’autres chiffres. Avant le lancement, il faut retrouver la valeur de réglage cachée dans chaque ligne.

    **Les données.** Chaque ligne du fichier est une chaîne qui mêle des lettres minuscules et des chiffres, par exemple `x3yz7k`. Chaque ligne contient au moins un chiffre.

    **La règle.**

    - Dans une ligne, on repère le **premier** chiffre (le plus à gauche) et le **dernier** chiffre (le plus à droite) ; les chiffres du milieu ne servent pas.

    - La valeur de la ligne est le nombre à deux chiffres obtenu en écrivant le premier chiffre puis le dernier. On accole les deux chiffres, on ne les additionne pas.

    - S’il n’y a qu’un chiffre, il sert à la fois de premier et de dernier.

    **La réponse attendue.** La somme des valeurs de toutes les lignes. Par exemple, la ligne `a4b7c2` vaut 42 (premier chiffre 4, dernier chiffre 2 ; le 7 ne sert pas) ; un fichier formé de cette seule ligne donnerait la réponse 42.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-aoc-1-1 }

**But.** Vérifier sur des cas particuliers qu’on a bien compris comment se calcule la valeur d’une ligne.

**À quoi ça sert ?** Ces cas (un seul chiffre, des chiffres à accoler et non à additionner) deviendront les premiers tests de la fonction `valeur`. La dernière question annonce la façon de former le nombre en Python.

Après lecture du résumé (et de l’énoncé), vérifier sa compréhension sur ces cas particuliers :

1.  Que vaut la ligne `a7b` ? et `k0z5` ?

2.  Une ligne `x45y` vaut-elle 45, 4 ou 9 ?

3.  Quel type de données a un caractère comme `"7"` ? Que donne `"7" + "2"` ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-aoc-1-2 }

**But.** Calculer à la main la valeur de quatre lignes et leur somme.

**À quoi ça sert ?** On obtient un exemple dont on **connaît la réponse** (205) : le programme devra la retrouver avant d’être lancé sur les vraies données.

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

**But.** Lire le fichier ligne par ligne et regarder quelques lignes de vos données.

**À quoi ça sert ?** Observer les vraies données avant de programmer évite les mauvaises surprises (longueur des lignes, caractères présents) et permet de vérifier que la lecture fonctionne.

!!! encadre "Outil Python : strip (nettoyer une ligne lue)"

    Chaque ligne renvoyée par `readlines()` se termine par le caractère de fin de ligne `"\n"` (sauf parfois la dernière). `ligne.strip()` renvoie une copie de la ligne sans les espaces ni les fins de ligne placés au début et à la fin.

    ```python
    ligne = "1721\n"
    print(ligne.strip())                  # 1721
    print(len(ligne), len(ligne.strip())) # 5 4
    ```

    **Intérêt.** Comparer ou découper une ligne sans que la fin de ligne ne gêne : `"abc\n" == "abc"` vaut `False`.

Rappel pour lire un fichier ligne par ligne :

```python
fichier = open("input.txt", encoding="utf-8")
for ligne in fichier:
    ligne = ligne.strip()   # enlève le retour à la ligne final
fichier.close()
```

Afficher les 5 premières lignes de vos données pour voir à quoi elles ressemblent.

!!! encadre "Méthode : reconnaître un chiffre, repérer un mot avec une tranche"

    Un caractère `c` est un chiffre lorsqu’il fait partie de la chaîne `"0123456789"` : le test `c in "0123456789"` vaut alors `True`. La comparaison `ligne[i:i + len(mot)] == mot` dit si `mot` apparaît dans `ligne` à partir de l’indice `i`.

    ```python
    print("4" in "0123456789", "q" in "0123456789")   # True False
    ligne = "abcone2"
    print(ligne[3:6] == "one")              # True : "one" commence a l'indice 3
    print(ligne[2:5] == "one")              # False
    ```

    **Intérêt.** Avec `len(mot)`, la tranche a toujours la bonne longueur, quel que soit le mot cherché ; en faisant varier `i`, on teste toutes les positions possibles de la ligne.

    *À essayer.* Avec `ligne = "eightwo"`, que valent `ligne[0:5] == "eight"` et `ligne[4:7] == "two"` ? Les deux mots partagent-ils une lettre ?

### <span class="exo-num">Exercice 4</span> — Les chiffres d’une ligne <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-aoc-1-4 }

**But.** Écrire une fonction qui renvoie la liste des chiffres d’une ligne, dans l’ordre.

**À quoi ça sert ?** Une fois cette liste obtenue, le premier et le dernier chiffre sont simplement son premier et son dernier élément. C’est aussi la seule fonction qu’il faudra modifier dans la partie 2.

Écrire une fonction `chiffres(ligne)` qui renvoie la liste des chiffres de la ligne, dans l’ordre, sous forme de chaînes. Tester : `chiffres("q12w34e")` doit valoir `["1", "2", "3", "4"]`.

??? pouce "Coup de pouce"

    Le test `c in "0123456789"` vaut `True` si le caractère `c` est un chiffre.

### <span class="exo-num">Exercice 5</span> — Valeur d’une ligne et total <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-aoc-1-5 }

**But.** Calculer la valeur d’une ligne à partir de ses chiffres, puis la somme sur tout le fichier.

**À quoi ça sert ?** La somme obtenue est la réponse de la partie 1. Comme `valeur` s’appuie sur `chiffres`, il suffira d’améliorer `chiffres` pour obtenir la partie 2 sans toucher au reste.

Écrire une fonction `valeur(ligne)` puis calculer la somme sur tout le fichier. Vérifier `205` sur l’exemple.

??? pouce "Coup de pouce"

    Le premier élément d’une liste `L` est `L[0]`, le dernier `L[-1]` (ou `L[len(L) - 1]`).

??? pouce "Coup de pouce 2 (début de solution)"

    Accoler deux **chaînes** avec `+` puis convertir : `int(L[0] + L[-1])`. Si l’on additionnait des entiers, on obtiendrait une somme et non un nombre à deux chiffres.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    **Ce qui change.** On s’aperçoit que certains chiffres étaient écrits en toutes lettres, en anglais, au milieu des autres lettres : ils comptaient eux aussi.

    **La nouvelle règle.**

    - Les mots `one`, `two`, `three`, `four`, `five`, `six`, `seven`, `eight`, `nine` comptent maintenant comme les chiffres 1 à 9.

    - Le premier et le dernier chiffre d’une ligne peuvent donc être écrits avec un chiffre ou en lettres.

    - La valeur d’une ligne se calcule comme avant, en accolant le premier et le dernier chiffre.

    **La réponse attendue.** La somme des nouvelles valeurs de toutes les lignes. Par exemple, la ligne `xtwo3sevenx` vaut 27 : son premier chiffre est `two` et son dernier est `seven`.

### <span class="exo-num">Exercice 6</span> — Des chiffres en toutes lettres <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-aoc-1-6 }

**But.** Améliorer la fonction `chiffres` pour qu’elle reconnaisse aussi les chiffres écrits en toutes lettres, puis recalculer la somme.

**À quoi ça sert ?** La fonction `valeur` et le calcul du total restent inchangés : seule l’extraction des chiffres change. Les lignes de test proposées, construites exprès, permettent de détecter le piège avant de lancer le programme sur les vraies données.

Modifier la fonction `chiffres(ligne)` pour qu’elle reconnaisse aussi les chiffres écrits en toutes lettres, comme le demande la partie 2. Sur le fichier (inventé) ci-dessous, on doit obtenir `215`.

```console
twone4x
7pqrsixteen
zoneight
nine87seven
```

**Piège** : deux mots peuvent partager des lettres (regarder `twone` et `zoneight`). Une méthode qui remplace les mots par des chiffres dans la chaîne risque de détruire l’un des deux mots : vérifier votre programme sur ces lignes.

??? pouce "Coup de pouce"

    Ranger les neuf mots anglais dans une liste `mots`, dans l’ordre, de sorte que `mots[0]` soit le mot de 1. Le chiffre correspondant au mot d’indice `k` est alors `str(k + 1)`.

??? pouce "Coup de pouce 2 (début de solution)"

    Plutôt que de modifier la ligne, la parcourir indice par indice : à chaque indice `i`, regarder si le caractère est un chiffre, puis, pour chaque mot de la liste, si la ligne contient ce mot **à partir de** l’indice `i` (une tranche de la bonne longueur : `ligne[i:i + len(mot)]`).

## Approfondissement

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 1 : chercher par les deux bouts <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-aoc-1-7 }

**But.** Trouver le premier et le dernier chiffre sans construire la liste de tous les chiffres.

**À quoi ça sert ?** On ne fait que le travail nécessaire : une recherche depuis le début, une depuis la fin. Cette version est plus rapide et, en prime, elle élimine complètement le problème des mots qui se chevauchent.

On n’a besoin que du premier et du dernier chiffre.

1.  À la main, sur `zoneight` : en partant de la fin, à quel indice trouve-t-on pour la première fois un chiffre ou le début d’un mot ?

2.  Écrire une fonction `chiffre_en(ligne, i)` qui renvoie le chiffre (sous forme de chaîne) qui commence à l’indice `i`, ou `""` s’il n’y en a pas.

3.  En déduire une version qui parcourt la ligne depuis le début jusqu’au premier chiffre trouvé, puis depuis la fin jusqu’au dernier, sans construire la liste complète. Pourquoi le chevauchement de mots ne pose-t-il alors plus aucun problème ?

    ??? pouce "Coup de pouce"

        Deux boucles `while` : l’une avec un indice qui monte depuis `0`, l’autre avec un indice qui descend depuis `len(ligne) - 1`. Chacune s’arrête dès que `chiffre_en` renvoie autre chose que `""`.
