# Défis Advent of Code

<p class="sous-titre">La recherche dichotomique</p>

## <span class="etiquette">Défi</span> High-Entropy Passphrases

*les phrases de passe — doublons et anagrammes*

<p class="infos-activite">Jour 4</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/07-defi-aoc-2017-04){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/premiere-07-defi-aoc-2017-04.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2017/day/4 ](https://adventofcode.com/2017/day/4 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (lien ci-dessus) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - **Attention aux exemples.** L’énoncé en ligne a son propre exemple, avec d’autres réponses. Les valeurs de test de cette fiche portent sur **l’exemple inventé de la fiche** (exercice « À la main ») : l’enregistrer dans un fichier `exemple.txt` à côté du programme, et ouvrir `"exemple.txt"` au lieu de `"input.txt"` pour tester.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

!!! encadre "Le défi en bref"

    **Le problème.** Le fichier contient plusieurs centaines de « phrases de passe », des suites de mots. Il faut compter celles qui ne contiennent aucun mot en double (partie 1), puis celles qui ne contiennent aucune paire de mots formés des mêmes lettres (partie 2). Comparer chaque mot à tous les autres, ligne après ligne, est un travail long et sans intérêt à la main : c’est le rôle du programme.

    **Ce qu’on réinvestit.** Le **tri** du chapitre précédent : pour savoir si deux mots sont formés des mêmes lettres, on range les lettres de chacun dans l’ordre alphabétique, et il suffit alors de comparer les résultats avec `==`. L’approfondissement 1 fait le lien avec ce chapitre : dans une liste triée, les doublons se retrouvent côte à côte, et un élément se retrouve vite par **recherche dichotomique**.

    **La démarche de la fiche.**

    1.  Comprendre la règle sur des cas particuliers, puis l’appliquer à la main sur cinq lignes.

    2.  Lire le fichier et découper chaque ligne en liste de mots.

    3.  Écrire une fonction qui dit si une liste ne contient aucun doublon : on obtient la partie 1.

    4.  Pour la partie 2, calculer la « signature » triée de chaque mot, puis réutiliser la même fonction sur la liste des signatures.

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|            |                 |                     |                         |
|:-----------|:----------------|:--------------------|:------------------------|
| passphrase | phrase de passe | valid               | valide                  |
| duplicate  | en double       | separated by spaces | séparés par des espaces |
| word       | mot             | policy              | règle, politique        |
| anagram    | anagramme       | rearrange           | réarranger, permuter    |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Un nouveau système informatique protège ses comptes par des « phrases de passe » plutôt que par des mots de passe. Pour qu’une phrase soit assez sûre, elle doit respecter une règle de construction. On dispose d’une liste de phrases de passe et l’on veut savoir combien d’entre elles sont acceptables.

    **Les données.** Le fichier contient une phrase de passe par ligne. Une phrase est formée de plusieurs mots en lettres minuscules, séparés par des espaces. Le nombre de mots varie d’une ligne à l’autre.

    **La règle.**

    - Une phrase est valide si elle ne contient **jamais deux fois le même mot**.

    - Il faut que les deux mots soient exactement identiques pour faire un doublon : une simple ressemblance (un mot contenu dans un autre, les mêmes lettres dans un autre ordre) ne rend pas la phrase invalide.

    - Une phrase d’un seul mot est donc toujours valide.

    **La réponse attendue.** Le nombre de lignes valides du fichier. Par exemple, la ligne `vert bleu vert` est invalide (`vert` deux fois), alors que `vert verte` est valide.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-la-recherche-dichotomique-aoc-1-1 }

**But.** Vérifier sa compréhension de la règle sur des cas particuliers.

**À quoi ça sert ?** Il faut savoir exactement ce qui est un doublon et ce qui n’en est pas avant d’écrire le test en Python. La troisième question prépare déjà la partie 2.

Après lecture du résumé (et de l’énoncé), vérifier sa compréhension sur ces cas particuliers :

1.  Les mots `abc` et `abcd` sont-ils considérés comme un doublon ?

2.  Une ligne d’un seul mot est-elle valide ?

3.  (Pour plus tard.) Les mots `ab` et `aab` utilisent les mêmes lettres : sont-ils des anagrammes ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-la-recherche-dichotomique-aoc-1-2 }

**But.** Décider à la main quelles lignes d’un petit fichier sont valides.

**À quoi ça sert ?** On obtient un exemple dont on connaît la réponse (`3`) pour tester le programme ; ce même fichier resservira pour la partie 2.

On considère le fichier (inventé) suivant :

```console
le chat et le chien
un deux trois
ab ba abc
mer rame arme
sol los sol
```

Indiquer pour chaque ligne si elle est valide. Vérification : on doit obtenir `3`. Les mots `ab` et `ba` sont-ils des doublons au sens de la partie 1 ?

## Programmer la partie 1

!!! encadre "Outil Python : strip (nettoyer une ligne lue)"

    Chaque ligne lue dans un fichier (avec `for ligne in fichier` ou `readlines()`) se termine par le caractère de fin de ligne `"\n"` (sauf parfois la dernière). `ligne.strip()` renvoie une copie de la ligne sans les espaces ni les fins de ligne placés au début et à la fin.

    ```python
    ligne = "1721\n"
    print(ligne.strip())                  # 1721
    print(len(ligne), len(ligne.strip())) # 5 4
    ```

    **Intérêt.** Comparer ou découper une ligne sans que la fin de ligne ne gêne : `"abc\n" == "abc"` vaut `False`.

### <span class="exo-num">Exercice 3</span> — Lire et découper <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-la-recherche-dichotomique-aoc-1-3 }

**But.** Transformer chaque ligne du fichier en une liste de mots.

**À quoi ça sert ?** La règle porte sur les mots, pas sur les caractères : c’est cette liste qu’on examinera pour chercher des doublons.

Rappel pour lire un fichier ligne par ligne :

```python
fichier = open("input.txt", encoding="utf-8")
for ligne in fichier:
    ligne = ligne.strip()   # enleve le retour a la ligne final
fichier.close()
```

Pour chaque ligne, construire la liste de ses mots et l’afficher.

??? pouce "Coup de pouce"

    `ligne.split()` (sans argument) découpe la chaîne sur les espaces et renvoie une liste de chaînes.

### <span class="exo-num">Exercice 4</span> — Tous distincts ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-la-recherche-dichotomique-aoc-1-4 }

**But.** Écrire une fonction qui dit si une liste ne contient aucun doublon, puis compter les lignes valides.

**À quoi ça sert ?** C’est la réponse de la partie 1. La fonction, écrite pour une liste quelconque, sera réutilisée sans modification dans la partie 2.

Écrire une fonction `tous_distincts(mots)` qui renvoie `True` si la liste `mots` ne contient aucun doublon. Tester sur les lignes de l’exemple, puis compter les lignes valides de vos données.

??? pouce "Coup de pouce"

    Deux boucles imbriquées sur les indices `i` et `j > i` : dès que `mots[i] == mots[j]`, la liste contient un doublon.

??? pouce "Coup de pouce 2 (début de solution)"

    `for i in range(len(mots)):` puis `for j in range(i + 1, len(mots)):` ; renvoyer `False` dès que `mots[i] == mots[j]`, et `True` après les deux boucles.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    **Ce qui change.** Le service de sécurité durcit la règle : un mot ne doit pas pouvoir s’obtenir en mélangeant les lettres d’un autre mot de la même ligne.

    **La nouvelle règle.**

    - Une phrase est valide si aucun de ses mots n’est une **anagramme** d’un autre de ses mots.

    - Deux mots sont anagrammes s’ils ont les mêmes lettres, chacune en même nombre, dans un ordre éventuellement différent.

    - Deux mots identiques sont aussi anagrammes : une ligne invalide dans la partie 1 reste invalide.

    **La réponse attendue.** Le nombre de lignes valides avec cette nouvelle règle. Par exemple, `pot top` est maintenant invalide, mais `pot pots` reste valide (un `s` de plus).

!!! encadre "Méthode : ranger les lettres d’un mot dans l’ordre alphabétique"

    Une chaîne ne se modifie pas. On passe donc par une **liste** de caractères, que l’on trie avec le tri par insertion du chapitre précédent (les caractères se comparent avec `<` et `>`, dans l’ordre alphabétique pour les minuscules), puis on recolle les caractères un par un dans une chaîne.

    ```python
    def tri_insertion(t):
        n = len(t)
        for i in range(1, n):
            x = t[i]
            j = i - 1
            while j >= 0 and t[j] > x:
                t[j + 1] = t[j]
                j = j - 1
            t[j + 1] = x

    lettres = [c for c in "rame"]   # liste des caracteres
    tri_insertion(lettres)
    print(lettres)                  # ['a', 'e', 'm', 'r']
    mot_trie = ""
    for c in lettres:               # on recolle les caracteres
        mot_trie += c
    print(mot_trie)                 # aemr
    ```

    **Intérêt.** Une chaîne se compare directement à une autre avec `==` ; une liste comparée à une chaîne donne toujours `False`. Recoller la liste évite ce piège.

    *À essayer.* Que vaut `["a", "e", "m", "r"] == "aemr"` ? Que donne la même méthode sur le mot `"banane"` ?

### <span class="exo-num">Exercice 5</span> — Reconnaître deux anagrammes <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-la-recherche-dichotomique-aoc-1-5 }

**But.** Écrire une fonction qui range les lettres d’un mot dans l’ordre alphabétique.

**À quoi ça sert ?** Deux anagrammes donnent la même chaîne triée : la question « ces mots sont-ils anagrammes ? » devient la question « ces chaînes sont-elles égales ? », à laquelle on sait déjà répondre.

Écrire une fonction `signature(mot)` qui renvoie la chaîne formée des lettres du mot rangées dans l’ordre alphabétique. Par exemple, `signature("rame")` doit valoir `"aemr"`. Expliquer pourquoi deux mots sont anagrammes l’un de l’autre si et seulement s’ils ont la même signature.

??? pouce "Coup de pouce"

    Reprendre la méthode de l’encadré : liste des caractères, tri par insertion, puis une boucle qui recolle les caractères dans une chaîne vide au départ.

### <span class="exo-num">Exercice 6</span> — La partie 2 <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-la-recherche-dichotomique-aoc-1-6 }

**But.** Répondre à la partie 2 en combinant les deux fonctions déjà écrites.

**À quoi ça sert ?** En remplaçant chaque mot par sa signature, une anagramme devient un doublon : la fonction de la partie 1 s’applique alors telle quelle. C’est l’intérêt d’avoir écrit des fonctions réutilisables.

En réutilisant `signature` et `tous_distincts`, répondre à la nouvelle question. Sur le petit exemple inventé de l’exercice 2, on doit trouver `1`.

??? pouce "Coup de pouce"

    Pour une ligne, construire la liste des signatures de ses mots (boucle et `append`), puis appliquer la fonction de la partie 1 à cette nouvelle liste.

## Approfondissement

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 1 : trier pour rapprocher les doublons <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-la-recherche-dichotomique-aoc-1-7 }

**But.** Détecter les doublons d’une liste en la triant d’abord, puis en ne comparant que des voisins.

**À quoi ça sert ?** On compare le coût de deux méthodes pour le même problème, et l’on fait le lien avec la recherche dichotomique de ce chapitre, qui exige elle aussi une liste triée.

Une autre idée pour `tous_distincts` réutilise le **tri**.

1.  À la main : trier les mots de la ligne `le chat et le chien`. Où se trouvent les deux `le` dans la liste triée ?

2.  Expliquer pourquoi, dans une liste triée, il suffit de comparer chaque élément à son **voisin** pour savoir s’il y a un doublon.

3.  Écrire `tous_distincts_tri(mots)` avec une seule boucle et vérifier qu’elle donne la même réponse que la partie 1.

    ??? pouce "Coup de pouce"

        Travailler sur une copie `t = [m for m in mots]`, triée avec `tri_insertion(t)`, pour ne pas modifier la liste de départ.

    ??? pouce "Coup de pouce 2 (début de solution)"

        Comparer `t[i]` et `t[i + 1]` pour `i` de `0` à `len(t) - 2` ; attention à ne pas sortir de la liste.

4.  Pour une ligne de $k$ mots, comparer le nombre de comparaisons de la double boucle et de cette méthode, au pire (le tri par insertion fait au pire $\frac{k(k-1)}{2}$ comparaisons). Le gain serait-il le même avec un tri qui ne fait qu’environ $k \log_2 k$ comparaisons (on en verra un en Terminale) ?

5.  **Lien avec la dichotomie.** Une fois la liste de mots triée, comment savoir si un mot donné y figure sans la parcourir en entier ? Combien de comparaisons faut-il au plus pour une liste de $1\,000$ mots ?

    ??? pouce "Coup de pouce"

        Les chaînes se comparent avec `<` dans l’ordre alphabétique : la recherche dichotomique du cours s’applique telle quelle.

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

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — Approfondissement 2 : une signature sans tri <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-la-recherche-dichotomique-aoc-1-8 }

**But.** Remplacer la signature triée par le tableau des effectifs des 26 lettres.

**À quoi ça sert ?** Cette signature se calcule en un seul parcours du mot, sans tri ; on vérifie qu’elle donne la même réponse à la partie 2, ce qui confirme les deux méthodes.

1.  À la main : donner les effectifs des lettres `a`, `e`, `m`, `r` dans `rame` et dans `arme`. Que constate-t-on ?

2.  Écrire `signature26(mot)` qui renvoie la liste des 26 effectifs (nombre de `a`, de `b`…) du mot, puis refaire la partie 2 avec cette signature. Obtient-on la même réponse ?

    ??? pouce "Coup de pouce"

        Partir de `[0] * 26` et ajouter 1 à la case d’indice `ord(lettre) - ord("a")` pour chaque lettre.

    ??? pouce "Coup de pouce 2 (début de solution)"

        Deux listes se comparent directement avec `==` : la fonction `tous_distincts` marche telle quelle sur une liste de signatures-listes.

!!! encadre "Outil Python : les ensembles (set)"

    Un **ensemble** (`set`) est une collection **sans doublon** et **sans ordre** : pas d’indice, on peut seulement ajouter un élément, en retirer un, et demander s’il est présent. On peut y ranger des nombres, des chaînes ou des p-uplets comme `(0, 0)`. Cet encadré sert aussi pour les défis des chapitres suivants.

    ```python
    vus = set()                 # ensemble vide (attention : {} est un dictionnaire vide)
    vus.add("a")                # ajout
    vus.add("b")
    vus.add("a")                # deja present : rien ne change
    print(len(vus))             # 2
    print("a" in vus)           # True : test d'appartenance
    print(len(set("nsin")))     # 3 : les caracteres distincts de "nsin"
    a = {1, 2, 3}               # ensemble ecrit directement
    b = {2, 3, 4}
    print(a | b)                # reunion : {1, 2, 3, 4}
    print(a & b)                # intersection (elements communs) : {2, 3}
    ```

    **Intérêt.** Avec une liste, `x in liste` compare `x` aux éléments un par un : jusqu’à $n$ comparaisons. Un ensemble range chaque élément à un endroit calculé à partir de sa valeur (comme les clés d’un dictionnaire) : Python va directement voir à cet endroit. Le test `x in ensemble` prend un temps qui ne dépend pas du nombre d’éléments.

    *À essayer.* Que vaut `len(set(["le", "chat", "le"]))` ?

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 9</span> — Approfondissement 3 : tous distincts en une ligne <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-la-recherche-dichotomique-aoc-1-9 }

**But.** Réécrire `tous_distincts` à l’aide d’un ensemble.

**À quoi ça sert ?** Un ensemble supprime automatiquement les doublons : comparer les longueurs suffit. On découvre un outil qui servira dans les défis des chapitres suivants.

Un ensemble ne garde qu’un exemplaire de chaque élément. En déduire une version de `tous_distincts(mots)` en une seule ligne, et la tester sur l’exemple.

??? pouce "Coup de pouce"

    Comparer la longueur de la liste et celle de l’ensemble de ses éléments.
