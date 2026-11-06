# Défis Advent of Code

<p class="sous-titre">Systèmes sur puce et informatique embarquée</p>

## <span class="etiquette">Défi</span> Docking Data

*l’amarrage — masques et opérations bit à bit*

<p class="infos-activite">Jour 14</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/14-defi-aoc-2020-14){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-14-defi-aoc-2020-14.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/14 ](https://adventofcode.com/2020/day/14 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (lien ci-dessus) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

!!! encadre "Le défi en bref"

    **Le problème.** L’ordinateur d’un ferry exécute un petit programme de près de cinq cents lignes qui écrit des valeurs en mémoire, en les retouchant au passage avec un masque de 36 bits. Il faut savoir ce que contient la mémoire à la fin. Les calculs en binaire sur 36 bits sont trop longs à la main, et en partie 2 une seule ligne peut écrire dans des centaines d’adresses.

    **Ce qu’on réinvestit.** Le défi met en scène l’ordinateur embarqué d’un ferry, un système comme ceux de ce chapitre : il initialise sa mémoire adresse par adresse. On y manipule l’**écriture binaire** des entiers et des opérations bit à bit ; le masque, appliqué bit par bit, rappelle le masque de sous-réseau vu au chapitre 9. Un **dictionnaire** représente une mémoire immense dont seules quelques cases sont utilisées, et l’approfondissement 1 réinvestit la récursivité du chapitre 1.

    **La démarche de la fiche.**

    1.  Vérifier sa compréhension de la règle, puis appliquer un masque à la main sur un petit programme.

    2.  Analyser une ligne du fichier, puis appliquer le masque à une valeur avec deux opérations bit à bit.

    3.  Simuler la mémoire avec un dictionnaire : réponse de la partie 1.

    4.  Pour la partie 2, énumérer toutes les adresses obtenues en remplaçant les bits flottants, puis le faire par récursivité en approfondissement.

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| bitmask | masque de bits | overwrite | écraser, remplacer |
| unchanged | inchangé | memory address | adresse mémoire |
| 36-bit unsigned | entier positif sur 36 bits | most significant bit | bit de poids fort |
| initialization | initialisation | sum | somme |
| floating | flottant (bit qui prend les deux valeurs) | decoder | décodeur |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** À l’approche du port, l’ordinateur du ferry doit initialiser sa mémoire, mais il ne comprend pas le système de masques de bits utilisé par le port. Vous allez émuler ce système, c’est-à-dire le reproduire par un programme.

    **Les données.** Le fichier est un petit programme ; chaque ligne est de l’une des deux formes suivantes.

    - `mask = ` suivi de 36 caractères parmi `0`, `1`, `X` : elle change le masque courant. Le masque s’écrit bit de poids fort à gauche ($2^{35}$) et reste en vigueur jusqu’au `mask` suivant.

    - `mem[a] = v` : elle écrit la valeur $v$ à l’adresse $a$. Adresses et valeurs sont des entiers positifs sur 36 bits, écrits en décimal.

    **La règle.**

    - Juste avant chaque écriture, on applique le masque à la **valeur** : un `0` ou un `1` du masque impose ce bit, un `X` laisse le bit de $v$ tel quel. Autrement dit, le masque ne retouche que certains bits.

    - Toutes les cases de la mémoire valent 0 au départ.

    - Écrire à nouveau à la même adresse remplace l’ancienne valeur.

    **La réponse attendue.** La somme de toutes les valeurs présentes en mémoire à la fin du programme. Par exemple, si le masque se termine par `10XX` (et ne contient que des `X` avant), écrire 7 (`0111`) donne `1011`, soit 11, et écrire 1 (`0001`) donne `1001`, soit 9 ; à deux adresses différentes, la réponse serait $11 + 9 = 20$.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-14-systemes-sur-puce-et-informatique-embarq-aoc-1-1 }

**But.** Vérifier sur trois questions courtes qu’on a compris le rôle du masque et de la mémoire.

**À quoi ça sert ?** La dernière question prépare un choix essentiel du programme : la mémoire doit être un dictionnaire, pas une liste.

Questions de vérification, à traiter sur le cahier :

1.  Si le masque ne contient que des `X`, quelle valeur est écrite ?

2.  Deux lignes `mem` écrivent à la même adresse : que contient la case à la fin ?

3.  Pourquoi ne peut-on pas représenter la mémoire par une liste de $2^{36}$ cases ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-14-systemes-sur-puce-et-informatique-embarq-aoc-1-2 }

**But.** Appliquer à la main le masque à trois valeurs écrites en binaire.

**À quoi ça sert ?** On obtient un exemple dont on **connaît la réponse** (40) et des valeurs intermédiaires pour tester `appliquer` ; on voit aussi l’effet d’une écriture qui en écrase une autre.

On considère le programme (inventé) suivant :

```console
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX1X0X0
mem[3] = 6
mem[10] = 21
mem[3] = 13
```

Écrire 6, 21 et 13 en binaire sur 6 bits, appliquer le masque et donner la valeur écrite à chaque fois. Vérification : la réponse est `40`.

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Lire une ligne <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-14-systemes-sur-puce-et-informatique-embarq-aoc-1-3 }

**But.** Transformer une ligne du fichier en une donnée facile à utiliser : le nouveau masque, ou le couple adresse–valeur.

**À quoi ça sert ?** Le reste du programme n’a plus à se soucier du texte : il distingue les deux sortes de lignes par le premier élément renvoyé. Cette fonction servira telle quelle en partie 2.

!!! encadre "Outil Python : strip (nettoyer une ligne lue)"

    Chaque ligne renvoyée par `readlines()` se termine par le caractère de fin de ligne `"\n"` (sauf parfois la dernière). `ligne.strip()` renvoie une copie de la ligne sans les espaces ni les fins de ligne placés au début et à la fin.

    ```python
    ligne = "1721\n"
    print(ligne.strip())                  # 1721
    print(len(ligne), len(ligne.strip())) # 5 4
    ```

    **Intérêt.** Comparer ou découper une ligne sans que la fin de ligne ne gêne : `"abc\n" == "abc"` vaut `False`.

Écrire une fonction `analyser(ligne)` qui renvoie `("mask", chaine)` ou `("mem", adresse, valeur)` selon la ligne.

??? pouce "Coup de pouce"

    `ligne.split(" = ")` sépare la partie gauche de la valeur. Pour l’adresse, on peut découper `"mem[3]"` avec une tranche qui enlève les 4 premiers caractères et le dernier.

!!! encadre "Outil Python : opérations bit à bit et conversions binaires (&, |, int(s, 2), bin)"

    Les opérateurs `&` (et) et `|` (ou) travaillent sur l’écriture binaire des entiers, bit par bit, tous les bits en même temps. `int(chaine, 2)` lit une chaîne binaire ; `bin(n)` écrit `n` en binaire avec le préfixe `0b`. Une tranche retire le préfixe, et une boucle complète par des zéros à gauche pour obtenir 36 chiffres.

    ```python
    a = int("1100", 2)             # 12 : chaine binaire -> entier
    b = int("1010", 2)             # 10
    print(a & b)                   # 8  (1000) : 1 la ou les deux bits valent 1
    print(a | b)                   # 14 (1110) : 1 la ou au moins un des bits vaut 1
    print(bin(a & b))              # 0b1000 : entier -> chaine binaire, prefixe 0b
    print(bin(5)[2:])              # 101 : la tranche retire le prefixe

    def en_binaire(n, nb_bits):
        """Renvoie l'ecriture binaire de n sur nb_bits chiffres (0 a gauche)."""
        chaine = bin(n)[2:]
        while len(chaine) < nb_bits:
            chaine = "0" + chaine
        return chaine

    print(en_binaire(5, 36))       # 36 caracteres, completes par des 0 a gauche
    ```

    **Intérêt.** `x & m` met à 0 tous les bits de `x` là où `m` a un 0 ; `x | m` met à 1 tous les bits de `x` là où `m` a un 1. Une seule opération, très rapide, remplace une boucle sur les 36 bits.

    **À essayer.** Calculer à la main `13 & 6` et `13 | 6` (écrire 13 et 6 sur 4 bits), puis vérifier avec Python.

!!! encadre "Méthode : parcourir une chaîne caractère par caractère"

    Pour remplacer, compter ou repérer un caractère dans une chaîne, on la parcourt avec une boucle. Une chaîne n’est pas modifiable : on en construit une **nouvelle** par concaténations successives.

    ```python
    def remplacer(s, a, b):
        """Renvoie une copie de s ou chaque caractere a est remplace par b."""
        resultat = ""
        for c in s:
            if c == a:
                resultat += b
            else:
                resultat += c
        return resultat

    def premier_indice(s, a):
        """Renvoie l'indice de la premiere occurrence de a dans s, ou -1."""
        i = 0
        while i < len(s) and s[i] != a:
            i += 1
        if i == len(s):
            return -1
        return i

    m = "X1X0"
    print(remplacer(m, "X", "0"))      # 0100 : une NOUVELLE chaine
    print(premier_indice(m, "X"))      # 0 : indice de la premiere occurrence
    print(premier_indice(m, "Z"))      # -1 : absent
    ```

    **Intérêt.** Pour compter les `X`, on reprend la même boucle avec un compteur. Le coût de ces fonctions est proportionnel à la longueur de la chaîne ; `premier_indice` s’arrête dès qu’il a trouvé.

    **À essayer.** Après `remplacer(m, "X", "0")`, que vaut `m` ? Pourquoi ?

### <span class="exo-num">Exercice 4</span> — Appliquer le masque avec deux opérations bit à bit <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-14-systemes-sur-puce-et-informatique-embarq-aoc-1-4 }

**But.** Calculer la valeur réellement écrite, avec deux opérations bit à bit au lieu d’une boucle sur les 36 bits.

**À quoi ça sert ?** C’est le cœur de la partie 1 : chaque écriture du programme passe par cette fonction.

Écrire une fonction `appliquer(masque, valeur)`. On construira deux entiers à partir du masque : l’un pour forcer des bits à `1`, l’autre pour forcer des bits à `0`. Vérifier : `appliquer(m, 6)` vaut `18` avec le masque de l’exemple.

??? pouce "Coup de pouce"

    En Python, `a | b` (ou bit à bit) et `a & b` (et bit à bit) agissent sur chaque bit ; `int("101", 2)` convertit une chaîne binaire en entier.

??? pouce "Coup de pouce 2 (début de solution)"

    Remplacer (par une boucle sur les caractères) les `X` du masque par des `0` donne un entier `ou_masque` à combiner avec `|` ; les remplacer par des `1` donne un entier `et_masque` à combiner avec `&`.

### <span class="exo-num">Exercice 5</span> — La mémoire <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-14-systemes-sur-puce-et-informatique-embarq-aoc-1-5 }

**But.** Exécuter tout le programme en stockant la mémoire dans un dictionnaire.

**À quoi ça sert ?** On obtient la réponse de la partie 1. Le dictionnaire ne contient que les adresses réellement écrites : quelques centaines au lieu de $2^{36}$ cases.

La mémoire a $2^{36}$ cases : une liste est impossible. Utiliser un dictionnaire `memoire` (adresse $\to$ valeur), exécuter le programme et afficher la somme des valeurs. Tester sur l’exemple du défi, puis sur vos données.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    **Ce qui change.** Le programme ne fonctionne toujours pas : la version du système utilisée par le port est en fait un « décodeur d’adresses ». Le masque agit maintenant sur l’**adresse**, et la valeur est écrite telle quelle.

    **La nouvelle règle.**

    - Un `0` du masque laisse le bit de l’adresse inchangé (attention : ce n’est plus comme en partie 1).

    - Un `1` force le bit de l’adresse à 1.

    - Un `X` est *flottant* : il prend les deux valeurs 0 et 1. Avec $k$ bits flottants, la valeur est donc écrite dans $2^k$ adresses.

    **La réponse attendue.** La même qu’en partie 1 : la somme des valeurs en mémoire à la fin. Par exemple, si le masque se termine par `0X1` (que des `0` avant), écrire 7 à l’adresse 4 (`100`) donne le modèle `1X1` : la valeur 7 est écrite aux adresses 5 et 7, ce qui apporte 14 à la somme.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Un masque sur les adresses <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-14-systemes-sur-puce-et-informatique-embarq-aoc-1-6 }

**But.** Calculer la liste de toutes les adresses désignées par une adresse et un masque contenant des bits flottants.

**À quoi ça sert ?** C’est la seule vraie nouveauté de la partie 2 : avec cette fonction, il suffit d’écrire la valeur à chacune de ces adresses dans le dictionnaire pour obtenir la réponse.

Écrire une fonction `adresses(masque, adresse)` qui renvoie la liste de toutes ces adresses.

Pour tester, on utilise un autre programme inventé :

```console
mask = 000000000000000000000000000000X10X0X
mem[5] = 4
mask = 0000000000000000000000000000000X0000
mem[1] = 10
```

Vérification : `mem[5] = 4` écrit dans 8 adresses, de `16` à `53` ; la réponse finale est `48` (une adresse est écrite deux fois).

??? pouce "Coup de pouce"

    Travailler sur des chaînes de 36 caractères : `en_binaire(adresse, 36)` (encadré de la partie 1) donne l’écriture binaire complétée par des zéros. On construit d’abord la chaîne résultat avec ses `X`.

??? pouce "Coup de pouce 2 (début de solution)"

    Pour remplacer les $k$ bits `X` : énumérer les entiers de $0$ à $2^k - 1$ et utiliser leurs $k$ bits ; ou bien écrire une fonction récursive qui remplace le premier `X` par `0`, puis par `1`.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 7</span> — Défi : combien de `X` au maximum ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-14-systemes-sur-puce-et-informatique-embarq-aoc-1-7 }

**But.** Mesurer, sur vos données, combien d’adresses la partie 2 écrit réellement.

**À quoi ça sert ?** On vérifie par l’expérience que le nombre de bits flottants reste petit, ce qui explique pourquoi la méthode termine rapidement alors que la mémoire est immense.

Afficher le plus grand nombre de `X` parmi les masques de vos données, et le nombre total d’adresses écrites. Pourquoi le dictionnaire reste-t-il de taille raisonnable alors que la mémoire a $2^{36}$ cases ?

## Approfondissement

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — Approfondissement 1 : énumérer les adresses par récursivité <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-14-systemes-sur-puce-et-informatique-embarq-aoc-1-8 }

**But.** Énumérer les $2^k$ adresses par une fonction récursive qui remplace un `X` à la fois.

**À quoi ça sert ?** La récursivité donne une solution courte et naturelle à ce problème d’énumération ; compter les appels relie cette solution à sa complexité.

1.  À la main, pour le modèle `X1X` : remplacer le premier `X` par `0`, puis par `1`, et recommencer sur chacune des deux chaînes obtenues. Dessiner l’arbre de ces remplacements et lister les chaînes finales dans l’ordre.

2.  Écrire une fonction récursive `remplacer_x(modele)` qui renvoie la liste de toutes les chaînes obtenues en remplaçant les `X` par des `0` et des `1`. Quel est le cas de base ?

    ??? pouce "Coup de pouce"

        Cas de base : le modèle ne contient aucun `X` (`premier_indice` renvoie $-1$) ; la liste ne contient alors que le modèle lui-même.

    ??? pouce "Coup de pouce 2 (début de solution)"

        Sinon, avec `i = premier_indice(modele, "X")`, construire par tranches `modele[:i] + "0" + modele[i + 1:]` et la même chaîne avec `"1"`, puis concaténer les deux listes renvoyées par les appels récursifs.

3.  Utiliser `remplacer_x` pour réécrire `adresses` ; vérifier les 8 adresses de l’exemple de la partie 2 et la réponse `48`.

4.  Combien d’appels récursifs pour un modèle contenant $k$ fois `X` ? Comparer avec la version qui énumère les entiers de $0$ à $2^k - 1$.
