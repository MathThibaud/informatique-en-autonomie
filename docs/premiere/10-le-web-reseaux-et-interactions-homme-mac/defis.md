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

!!! encadre "Le défi en bref"

    **Le problème.** Le fichier contient un seul très long flux de lettres (plusieurs milliers). Il faut trouver le premier endroit où 4 lettres consécutives sont toutes différentes, puis (partie 2) le premier endroit où 14 lettres consécutives le sont. Sur quelques dizaines de lettres, on y arrive à l’œil ; sur plusieurs milliers, il faut un programme.

    **Ce qu’on réinvestit.** Le lien avec ce chapitre sur les réseaux : un appareil qui reçoit des données doit savoir **où commence un paquet** dans le flux qui lui arrive, et les protocoles prévoient pour cela des **marqueurs**, des motifs reconnaissables. Côté programmation, on utilise une **fenêtre glissante** : une tranche de taille fixe que l’on décale d’un caractère à la fois le long de la chaîne, avec les tranches et le test `in`.

    **La démarche de la fiche.**

    1.  Comprendre la règle (en particulier comment on compte la position), puis la faire à la main sur deux petits flux.

    2.  Lire le fichier, qui ne contient qu’une ligne.

    3.  Écrire une fonction qui dit si une chaîne a tous ses caractères différents, puis faire glisser la fenêtre : on obtient la partie 1.

    4.  Pour la partie 2, ajouter un paramètre `taille` à la fonction : seul l’appel change.

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| datastream | flux de données | buffer | tampon, mémoire de réception |
| marker | marqueur | start-of-packet | début de paquet |
| all different | tous différents | characters processed | caractères traités |
| received | reçu | start-of-message | début de message |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Un elfe vous confie un petit appareil de communication, qui doit d’abord se caler sur le signal radio des elfes. Le signal arrive comme une suite de lettres reçues l’une après l’autre. Pour comprendre ce signal, l’appareil doit repérer où commence un paquet de données : ce début est signalé par un groupe de lettres consécutives toutes différentes.

    **Les données.** Le fichier contient tout le flux reçu sur **une seule ligne** : une longue suite de lettres minuscules, sans espace. Le premier caractère de la ligne est le premier reçu.

    **La règle.**

    - On lit les caractères de gauche à droite, un par un.

    - Après chaque caractère lu, on regarde les **4 derniers caractères lus** (le caractère qu’on vient de lire et les trois précédents).

    - Dès que ces 4 caractères sont tous différents, on a trouvé le marqueur de début de paquet, et l’on s’arrête.

    - On ne peut pas répondre avant d’avoir lu au moins 4 caractères.

    **La réponse attendue.** Le nombre de caractères lus depuis le début jusqu’au dernier caractère du marqueur inclus, positions comptées à partir de 1. Par exemple, pour le flux `xxyxzwq`, les 4 derniers caractères lus sont tous différents pour la première fois après la lecture du sixième caractère (`yxzw`) : la réponse serait 6.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-aoc-1-1 }

**But.** Vérifier sa compréhension de la règle, surtout de la façon dont on compte la position.

**À quoi ça sert ?** La difficulté de ce défi n’est pas la recherche elle-même, mais le décalage d’indices : Python compte à partir de 0, la réponse compte à partir de 1, et une tranche s’arrête juste avant sa borne de fin. Ces questions évitent une réponse fausse d’une ou trois unités.

Après lecture du résumé (et de l’énoncé), vérifier sa compréhension sur ces cas particuliers :

1.  Peut-on obtenir une réponse plus petite que 4 ?

2.  Pour `abcd...`, quelle est la réponse ? et pour `aaaabcd` ?

3.  Si la fenêtre `flux[i:i+4]` convient, faut-il répondre `i`, `i + 4` ou `i + 3` ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-aoc-1-2 }

**But.** Trouver à la main le marqueur de deux petits flux, en écrivant les fenêtres successives.

**À quoi ça sert ?** On voit concrètement la fenêtre « glisser » d’un caractère à la fois, ce que le programme fera ; et l’on obtient deux réponses connues (`7` et `10`) pour le tester.

Pour chacun des flux (inventés) suivants, trouver la réponse de la partie 1 :

```console
aabacbdeffgh
nsinsinsiabcdefghijklmnop
```

Vérification : on doit obtenir `7` pour le premier, `10` pour le second. Écrire les fenêtres de 4 caractères examinées l’une après l’autre pour le premier flux.

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Lire le fichier <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-aoc-1-3 }

**But.** Lire tout le flux dans une seule chaîne `flux`.

**À quoi ça sert ?** Le fichier n’a qu’une ligne : on n’a pas besoin de boucle de lecture, mais il faut retirer le retour à la ligne final, qui serait compté comme un caractère du flux.

!!! encadre "Outil Python : strip (nettoyer une ligne lue)"

    Chaque ligne renvoyée par `readlines()` se termine par le caractère de fin de ligne `"\n"` (sauf parfois la dernière). `ligne.strip()` renvoie une copie de la ligne sans les espaces ni les fins de ligne placés au début et à la fin.

    ```python
    ligne = "1721\n"
    print(ligne.strip())                  # 1721
    print(len(ligne), len(ligne.strip())) # 5 4
    ```

    **Intérêt.** Comparer ou découper une ligne sans que la fin de ligne ne gêne : `"abc\n" == "abc"` vaut `False`.

Le fichier ne contient qu’une ligne : on le lit d’un coup.

```python
fichier = open("input.txt", encoding="utf-8")
flux = fichier.read().strip()   # toute la ligne, sans le retour final
fichier.close()
```

Afficher la longueur de `flux` et ses 10 premiers caractères (`flux[0:10]`).

### <span class="exo-num">Exercice 4</span> — Des caractères tous différents ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-aoc-1-4 }

**But.** Écrire une fonction qui dit si une chaîne courte n’a aucun caractère en double.

**À quoi ça sert ?** C’est le test appliqué à chaque fenêtre : la recherche du marqueur consiste à appeler cette fonction sur des fenêtres successives jusqu’à ce qu’elle renvoie `True`.

Écrire une fonction `tous_differents(morceau)` qui renvoie `True` si la chaîne `morceau` ne contient pas deux fois le même caractère. Tester avec `"acbd"` et `"abac"`.

??? pouce "Coup de pouce"

    Pour chaque indice `i`, regarder si `morceau[i]` apparaît dans la suite de la chaîne, `morceau[i+1:]`, avec l’opérateur `in`.

### <span class="exo-num">Exercice 5</span> — Faire glisser la fenêtre <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-aoc-1-5 }

**But.** Parcourir le flux avec une fenêtre de 4 caractères et renvoyer la position du premier marqueur.

**À quoi ça sert ?** C’est la réponse de la partie 1. La fenêtre glissante est une technique qu’on retrouve souvent : moyennes sur plusieurs jours, recherche d’un motif dans un texte, etc.

Écrire une fonction `position_marqueur(flux)` qui renvoie la réponse de la partie 1. Vérifier les deux valeurs de l’exemple, puis lancer sur vos données.

??? pouce "Coup de pouce"

    La fenêtre qui se termine juste avant l’indice `fin` est la tranche `flux[fin-4:fin]`. Le premier `fin` possible est `4`.

??? pouce "Coup de pouce 2 (début de solution)"

    Une boucle `while` qui avance `fin` de 1 tant que la fenêtre `flux[fin-4:fin]` n’est pas formée de caractères tous différents. À la sortie, `fin` est exactement le nombre de caractères traités.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    **Ce qui change.** L’appareil doit aussi repérer le début des messages, signalé par un marqueur plus long que celui des paquets.

    **La nouvelle règle.**

    - Même lecture qu’à la partie 1, mais on regarde les **14** derniers caractères lus au lieu des 4 derniers.

    - On s’arrête dès que ces 14 caractères sont tous différents.

    **La réponse attendue.** Le nombre de caractères lus jusqu’au dernier caractère de ce premier groupe de 14, positions comptées à partir de 1 comme dans la partie 1.

### <span class="exo-num">Exercice 6</span> — Généraliser <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-aoc-1-6 }

**But.** Rendre la taille de la fenêtre réglable par un paramètre.

**À quoi ça sert ?** Une seule fonction répond alors aux deux parties : la partie 2 ne demande que de changer l’appel. C’est l’intérêt de ne pas écrire de valeur « en dur » dans une fonction.

Ajouter un paramètre : `position_marqueur(flux, taille)`. La partie 1 correspond à `taille = 4`. Répondre à la partie 2. Sur le second flux de l’exemple, on doit trouver `23`.

??? pouce "Coup de pouce"

    Remplacer chaque `4` écrit « en dur » par `taille`. Si la fonction était bien écrite, la partie 2 ne demande que de changer l’appel.

## Approfondissement

!!! encadre "Rappel : les ensembles (set)"

    Les ensembles sont présentés dans l’encadré « Outil Python : les ensembles » du défi *High-Entropy Passphrases* (chapitre 7). L’essentiel : `set()` crée un ensemble vide, `e.add(x)` ajoute `x` (sans doublon), `len(e)` compte les éléments, et le test `x in e` est quasi instantané, quelle que soit la taille de `e`. Ici, on construit l’ensemble des caractères d’une chaîne en les ajoutant un à un dans une boucle : les doublons disparaissent d’eux-mêmes.

    ```python
    caracteres = set()
    for c in "abac":
        caracteres.add(c)
    ```

    *À essayer.* Que vaut alors `len(caracteres)` ? Comparer avec `len("abac")`.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 1 : tous différents avec un ensemble <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-aoc-1-7 }

**But.** Compter le travail fait par `tous_differents`, puis l’écrire avec un ensemble.

**À quoi ça sert ?** Le nombre de comparaisons grandit vite avec la taille de la fenêtre (14 au lieu de 4) ; l’ensemble évite de comparer chaque caractère à tous les autres.

1.  Pour une fenêtre de taille $k$, combien de comparaisons de caractères `tous_differents` fait-elle au pire ? Calculer pour $k = 4$ et $k = 14$.

    ??? pouce "Coup de pouce"

        Le premier caractère est comparé aux $k - 1$ suivants, le deuxième aux $k - 2$ suivants, etc.

2.  Écrire `tous_differents_ens(morceau)` avec un ensemble, et vérifier qu’elle donne les mêmes réponses.

    ??? pouce "Coup de pouce"

        Parcourir la fenêtre en mettant chaque caractère dans un ensemble : les caractères sont tous différents si et seulement si, à la fin, l’ensemble a la même taille que la fenêtre.

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

**But.** Mettre à jour les compteurs de lettres quand la fenêtre glisse, au lieu de tout réexaminer.

**À quoi ça sert ?** On obtient un programme dont la durée ne dépend presque plus de la taille de la fenêtre : c’est la version efficace de la fenêtre glissante.

Quand la fenêtre glisse d’un cran, un seul caractère entre et un seul sort : les autres ne changent pas.

1.  À la main, sur `aabacbdeffgh` avec $k = 4$ : écrire, pour chaque glissement, le caractère qui entre et celui qui sort.

2.  Écrire `position_rapide(flux, taille)` qui tient à jour une liste de 26 compteurs (un par lettre) et le nombre de lettres différentes présentes dans la fenêtre. Vérifier qu’elle redonne les réponses des parties 1 et 2.

    ??? pouce "Coup de pouce"

        Quand un caractère entre, ajouter 1 à son compteur ; si ce compteur passe de 0 à 1, une lettre différente de plus est présente.

    ??? pouce "Coup de pouce 2 (début de solution)"

        Quand un caractère sort (celui d’indice `i - taille`), retirer 1 à son compteur ; s’il retombe à 0, une lettre différente de moins. On a trouvé le marqueur quand le nombre de lettres différentes vaut `taille`.

3.  Combien d’opérations pour un flux de $n$ caractères ? Cela dépend-il encore de $k$ ?
