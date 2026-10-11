# Défis Advent of Code

<p class="sous-titre">Le Web : réseaux et interactions homme-machine</p>

## <span class="etiquette">Défi</span> Tuning Trouble

*le signal radio — fenêtre glissante sur une chaîne*

<p class="infos-activite">Jour 6</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/10-defi-aoc-2022-06){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/premiere-10-defi-aoc-2022-06.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2022/day/6 ](https://adventofcode.com/2022/day/6 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (lien ci-dessus) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| datastream | flux de données | buffer | tampon, mémoire de réception |
| marker | marqueur | start-of-packet | début de paquet |
| all different | tous différents | characters processed | caractères traités |
| received | reçu | start-of-message | début de message |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Un elfe vous confie un petit appareil de communication, qui doit d’abord se caler sur le signal radio des elfes. Le signal arrive comme une suite de lettres reçues l’une après l’autre ; le fichier contient tout ce flux sur une seule ligne. Le début d’un paquet de données est signalé par un groupe de lettres consécutives toutes différentes, qu’il faut repérer.

    **Ce qu’il faut faire.**

    - On lit les caractères de gauche à droite. On cherche le premier endroit où les **4 derniers caractères lus** sont tous différents : c’est le marqueur de début de paquet.

    - Réponse : le nombre de caractères lus depuis le début jusqu’au dernier caractère de ce marqueur, positions comptées à partir de 1. Autrement dit, si le marqueur occupe les caractères 3 à 6, la réponse est 6.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-aoc-1-1 }

Après lecture du résumé (et de l’énoncé), vérifier sa compréhension sur ces cas particuliers :

1.  Peut-on obtenir une réponse plus petite que 4 ?

2.  Pour `abcd...`, quelle est la réponse ? et pour `aaaabcd` ?

3.  Si la fenêtre `flux[i:i+4]` convient, faut-il répondre `i`, `i + 4` ou `i + 3` ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-aoc-1-2 }

Pour chacun des flux (inventés) suivants, trouver la réponse de la partie 1 :

```console
aabacbdeffgh
nsinsinsiabcdefghijklmnop
```

Vérification : on doit obtenir `7` pour le premier, `10` pour le second. Écrire les fenêtres de 4 caractères examinées l’une après l’autre pour le premier flux.

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Lire le fichier <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-aoc-1-3 }

Le fichier ne contient qu’une ligne : on le lit d’un coup.

```python
fichier = open("input.txt", encoding="utf-8")
flux = fichier.read().strip()   # toute la ligne, sans le retour final
fichier.close()
```

Afficher la longueur de `flux` et ses 10 premiers caractères (`flux[0:10]`).

### <span class="exo-num">Exercice 4</span> — Des caractères tous différents ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-aoc-1-4 }

Écrire une fonction `tous_differents(morceau)` qui renvoie `True` si la chaîne `morceau` ne contient pas deux fois le même caractère. Tester avec `"acbd"` et `"abac"`.

??? pouce "Coup de pouce"

    Pour chaque indice `i`, regarder si `morceau[i]` apparaît dans la suite de la chaîne, `morceau[i+1:]`, avec l’opérateur `in`.

### <span class="exo-num">Exercice 5</span> — Faire glisser la fenêtre <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-aoc-1-5 }

Écrire une fonction `position_marqueur(flux)` qui renvoie la réponse de la partie 1. Vérifier les deux valeurs de l’exemple, puis lancer sur vos données.

??? pouce "Coup de pouce"

    La fenêtre qui se termine juste avant l’indice `fin` est la tranche `flux[fin-4:fin]`. Le premier `fin` possible est `4`.

??? pouce "Coup de pouce 2 (début de solution)"

    Une boucle `while` qui avance `fin` de 1 tant que la fenêtre `flux[fin-4:fin]` n’est pas formée de caractères tous différents. À la sortie, `fin` est exactement le nombre de caractères traités.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    L’appareil doit aussi repérer le début des messages, signalé par un marqueur plus long. Même question, mais avec **14** caractères consécutifs tous différents au lieu de 4. Réponse : le nombre de caractères lus jusqu’à la fin de ce premier groupe de 14.

### <span class="exo-num">Exercice 6</span> — Généraliser <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-aoc-1-6 }

Ajouter un paramètre : `position_marqueur(flux, taille)`. La partie 1 correspond à `taille = 4`. Répondre à la partie 2. Sur le second flux de l’exemple, on doit trouver `23`.

??? pouce "Coup de pouce"

    Remplacer chaque `4` écrit « en dur » par `taille`. Si la fonction était bien écrite, la partie 2 ne demande que de changer l’appel.

## Approfondissement

!!! encadre "Rappel : les ensembles (set)"

    Les ensembles sont présentés dans l’encadré « Outil Python : les ensembles » du défi *High-Entropy Passphrases* (chapitre 7). L’essentiel : `set()` crée un ensemble vide, `e.add(x)` ajoute `x` (sans doublon), `len(e)` compte les éléments, et le test `x in e` est quasi instantané, quelle que soit la taille de `e`. Ici, on se sert surtout de `set(chaine)`, qui donne l’ensemble des caractères distincts de la chaîne.

    *À essayer.* Que vaut `len(set("abac"))` ? Comparer avec `len("abac")`.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 1 : tous différents avec un ensemble <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-aoc-1-7 }

1.  Pour une fenêtre de taille $k$, combien de comparaisons de caractères `tous_differents` fait-elle au pire ? Calculer pour $k = 4$ et $k = 14$.

    ??? pouce "Coup de pouce"

        Le premier caractère est comparé aux $k - 1$ suivants, le deuxième aux $k - 2$ suivants, etc.

2.  Écrire `tous_differents_ens(morceau)` en une ligne, avec un ensemble, et vérifier qu’elle donne les mêmes réponses.

    ??? pouce "Coup de pouce"

        Les caractères sont tous différents si et seulement si l’ensemble des caractères a la même taille que la fenêtre.

!!! encadre "Outil Python : codes des caractères (ord, chr)"

    Chaque caractère a un numéro (son code). `ord` donne le code d’un caractère, `chr` fait l’inverse. Les lettres minuscules ont des codes consécutifs.

    ```python
    print(ord("a"))              # 97 : code du caractere
    print(ord("c") - ord("a"))   # 2 : rang de "c" dans l'alphabet (a -> 0)
    print(chr(98))               # b : operation inverse
    compteurs = [0] * 26
    compteurs[ord("c") - ord("a")] += 1    # on compte un "c"
    ```

    **Intérêt.** `ord(c) - ord("a")` transforme une lettre en un indice de $0$ à $25$ : on peut alors compter les lettres dans une simple liste de 26 entiers.

    *À essayer.* Que vaut `ord("z") - ord("a")` ? Et `chr(ord("a") + 3)` ?

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 8</span> — Approfondissement 2 : ne pas tout recompter <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-aoc-1-8 }

Quand la fenêtre glisse d’un cran, un seul caractère entre et un seul sort : les autres ne changent pas.

1.  À la main, sur `aabacbdeffgh` avec $k = 4$ : écrire, pour chaque glissement, le caractère qui entre et celui qui sort.

2.  Écrire `position_rapide(flux, taille)` qui tient à jour une liste de 26 compteurs (un par lettre) et le nombre de lettres différentes présentes dans la fenêtre. Vérifier qu’elle redonne les réponses des parties 1 et 2.

    ??? pouce "Coup de pouce"

        Quand un caractère entre, ajouter 1 à son compteur ; si ce compteur passe de 0 à 1, une lettre différente de plus est présente.

    ??? pouce "Coup de pouce 2 (début de solution)"

        Quand un caractère sort (celui d’indice `i - taille`), retirer 1 à son compteur ; s’il retombe à 0, une lettre différente de moins. On a trouvé le marqueur quand le nombre de lettres différentes vaut `taille`.

3.  Combien d’opérations pour un flux de $n$ caractères ? Cela dépend-il encore de $k$ ?
