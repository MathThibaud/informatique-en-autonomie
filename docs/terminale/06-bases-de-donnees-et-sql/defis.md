# Défis Advent of Code

<p class="sous-titre">Bases de données et SQL</p>

## <span class="etiquette">Défi 1</span> Passport Processing

*les passeports — dictionnaires et validation*

<p class="infos-activite">Jour 4</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/06-defi-aoc-2020-04){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-06-defi-aoc-2020-04.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/4 ](https://adventofcode.com/2020/day/4 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/06-defi-aoc-2020-04>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

*Ce défi fait écho à la notion de domaine vue dans ce chapitre : chaque champ d’un passeport n’est valide que si sa valeur appartient à un domaine précis.*

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|                |                  |                    |                    |
|:---------------|:-----------------|:-------------------|:-------------------|
| field          | champ            | required           | obligatoire        |
| missing        | manquant         | optional           | facultatif         |
| batch file     | fichier de lot   | blank line         | ligne vide         |
| key:value pair | paire clé:valeur | at least / at most | au moins / au plus |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Arrivé à l’aéroport, le héros s’aperçoit qu’il a emporté une carte d’identité du pôle Nord, et non son passeport. La file devant les scanners automatiques est interminable, car ces machines vérifient mal les documents. Le fichier contient les données lues par un scanner : chaque passeport y est décrit par une suite de champs (année de naissance, taille, couleur des yeux…). Il faut écrire le programme qui décide si un document est acceptable.

    **Ce qu’il faut faire.**

    - Les passeports sont séparés par une **ligne vide** ; un même passeport peut s’étaler sur plusieurs lignes.

    - Un passeport est une suite de champs `cle:valeur`, séparés par des espaces ou des retours à la ligne, dans un ordre quelconque.

    - Il existe huit clés : `byr` (année de naissance), `iyr` (année de délivrance), `eyr` (année d’expiration), `hgt` (taille), `hcl` (couleur des cheveux), `ecl` (couleur des yeux), `pid` (numéro de passeport) et `cid` (pays).

    - En partie 1, un passeport est valide si les sept premières clés sont présentes ; `cid` peut manquer, ce qui laisse passer la carte du héros. Les valeurs ne sont pas encore examinées.

    - Il faut renvoyer le nombre de passeports valides.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-bases-de-donnees-et-sql-aoc-1-1 }

Après lecture de l’énoncé et du résumé, vérifier sa compréhension :

1.  Un passeport qui possède les huit champs mais contient `byr:abc` est-il valide en partie 1 ?

2.  Un passeport de sept champs, parmi lesquels `cid`, est-il valide ?

3.  Lire le fichier ligne par ligne rend-il le découpage en passeports facile ? Pourquoi ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-bases-de-donnees-et-sql-aoc-1-2 }

On considère le fichier (inventé) suivant :

```console
byr:1985 hgt:172cm ecl:grn
pid:004512398 iyr:2015 eyr:2027 hcl:#a97842

iyr:2018 hcl:#18171d byr:2001
ecl:blu eyr:2029 pid:765432109

hgt:64in pid:12345678 cid:99 ecl:hzl
hcl:#cc33ff byr:1950 iyr:2012 eyr:2023

eyr:2031 ecl:oth byr:1999 iyr:2014 pid:000000042 hcl:#0a0b0c hgt:190cm

hcl:#623a2f pid:543210987 eyr:2025 byr:1932
iyr:2019 ecl:amb hgt:158cm cid:7
```

Combien de passeports contient-il ? Lesquels sont valides selon la partie 1 ? Vérification : on doit en trouver `4`.

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Séparer les passeports <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-bases-de-donnees-et-sql-aoc-1-3 }

Lire tout le fichier en une chaîne et construire la liste des blocs de texte, un bloc par passeport. Afficher le nombre de blocs.

??? pouce "Coup de pouce"

    Une ligne vide, c’est deux retours à la ligne consécutifs : `texte.split("\n\n")`.

### <span class="exo-num">Exercice 4</span> — Un passeport, un dictionnaire <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-bases-de-donnees-et-sql-aoc-1-4 }

Écrire une fonction `lire_passeport(bloc)` qui renvoie un dictionnaire, par exemple `{"byr": "1985", "hgt": "172cm", ...}`. Garder les valeurs sous forme de chaînes.

??? pouce "Coup de pouce"

    `bloc.split()` sans argument coupe à la fois aux espaces et aux retours à la ligne. Chaque morceau se coupe ensuite en deux au `:`.

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

    **À essayer.** Écrire `complet(passeport)` en une ligne avec `all`.

### <span class="exo-num">Exercice 5</span> — Compter les passeports complets <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-bases-de-donnees-et-sql-aoc-1-5 }

Écrire `complet(passeport)` qui vérifie la présence des champs obligatoires, puis compter. Tester sur l’exemple de la fiche, puis sur vos données.

??? pouce "Coup de pouce"

    Ranger les clés obligatoires dans une liste et tester chacune avec l’opérateur `in`, qui teste la présence d’une **clé** dans un dictionnaire.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    Des documents absurdes passent encore : il faut maintenant contrôler aussi les valeurs. Un passeport est valide si les sept clés sont présentes **et** si :

    - `byr` est entre 1920 et 2002, `iyr` entre 2010 et 2020, `eyr` entre 2020 et 2030 (quatre chiffres, bornes comprises) ;

    - `hgt` est un nombre suivi de `cm` (de 150 à 193) ou de `in` (de 59 à 76) ;

    - `hcl` est `#` suivi d’exactement six caractères parmi `0-9` et `a-f` ; `ecl` vaut exactement l’un de `amb blu brn gry grn hzl oth` ;

    - `pid` compte exactement neuf chiffres (zéros de tête compris) ; `cid` est ignoré.

!!! encadre "Outil Python : tester la forme d’une chaîne (isdigit, startswith, endswith)"

    Ces méthodes renvoient un booléen qui décrit la forme de la chaîne, sans la convertir.

    ```python
    print("2019".isdigit())         # True : que des chiffres
    print("-12".isdigit())          # False : le signe n'est pas un chiffre
    print("".isdigit())             # False : chaine vide
    taille = "172cm"
    print(taille.endswith("cm"))    # True
    print(taille.startswith("#"))   # False
    print(taille[:-2], taille[-2:]) # 172 cm : tranches avec indices negatifs
    ```

    **Intérêt.** Vérifier la forme d’une chaîne **avant** d’appeler `int`, qui provoque une erreur sur `"abc"` ou `"170cm"`.

    **À essayer.** Que renvoient `int("0042")` et `"0042".isdigit()` ?

!!! encadre "Outil Python : ranger des fonctions dans un dictionnaire"

    En Python, une fonction est une valeur comme une autre : on peut la ranger dans une variable, une liste ou un dictionnaire, puis l’appeler plus tard.

    ```python
    def double(x):
        return 2 * x

    def carre(x):
        return x * x

    operations = {"double": double, "carre": carre}   # sans parentheses
    for nom, f in operations.items():
        print(nom, f(5))      # double 10, puis carre 25
    ```

    **Intérêt.** Une seule boucle applique à chaque champ la règle qui lui correspond ; ajouter une règle revient à ajouter une ligne au dictionnaire.

    **À essayer.** Que contient le dictionnaire si l’on écrit `{"double": double(5)}` ?

### <span class="exo-num">Exercice 6</span> — Une fonction par règle <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-bases-de-donnees-et-sql-aoc-1-6 }

1.  Pour chaque champ, écrire une fonction de validation : `valide_byr(valeur)`, `valide_hgt(valeur)`, etc. Pour chacune, écrire au moins un `assert` qui doit réussir et un qui doit échouer, en visant les valeurs limites.

2.  Écrire `valide(passeport)` qui combine le tout, puis compter. Sur l’exemple de la fiche, on doit trouver `2` passeports valides.

??? pouce "Coup de pouce"

    Penser aux chaînes pièges : une taille sans unité, un identifiant trop court, une couleur en majuscules… Les méthodes `isdigit()`, `endswith()` et le découpage `valeur[:-2]` sont utiles.

??? pouce "Coup de pouce 2 (début de solution)"

    Un dictionnaire peut associer chaque nom de champ à sa fonction de validation : `regles = {"byr": valide_byr, ...}`. On parcourt alors `regles.items()` et on appelle `fonction(passeport[cle])`.

## Pour y arriver : les expressions régulières <span class="horsprog">au-delà du programme</span>

!!! encadre "Expressions régulières (facultatif)"

    Une *expression régulière* (regex) décrit la forme d’une chaîne. Le module `re` teste si une chaîne entière a cette forme avec `re.fullmatch(motif, chaine)`, qui renvoie `None` en cas d’échec.

    - `[0-9]` : un chiffre ; `[a-z]` : une lettre minuscule ; `[abc]` : un caractère parmi `a`, `b`, `c`.

    - `{3}` : répéter exactement 3 fois ce qui précède ; `+` : une fois ou plus.

    - `|` : ou ; les parenthèses regroupent.

    Exemple : `re.fullmatch(r"[0-9]{2}h[0-9]{2}", "08h30")` réussit, mais pas avec `"8h30"` ni `"08h300"`. Tout ce que fait une regex ici peut aussi s’écrire avec des tests sur les caractères : c’est seulement plus court.

## Approfondissement

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 7</span> — Défi : tout en regex <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-bases-de-donnees-et-sql-aoc-1-7 }

Réécrire les validations des champs de la partie 2 qui s’y prêtent avec `re.fullmatch`. Les tests écrits plus haut doivent toujours passer.

??? pouce "Coup de pouce"

    Les tests de la partie 2 servent ici de filet de sécurité : on modifie le code, on relance les `assert`.

## <span class="etiquette">Défi 2</span> Ticket Translation

*les billets de train — dictionnaires et ensembles*

<p class="infos-activite">Jour 16</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/06-defi-aoc-2020-16){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-06-defi-aoc-2020-16.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/16 ](https://adventofcode.com/2020/day/16 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/06-defi-aoc-2020-16>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

*Ce défi fait écho aux contraintes de domaine vues dans ce chapitre : chaque champ d’un billet n’accepte que certaines valeurs, et l’on s’en sert pour écarter les enregistrements incohérents.*

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| ticket | billet | field | champ |
| range | intervalle | inclusive | bornes comprises |
| nearby | voisin, proche | invalid | non valide |
| scanning error rate | taux d’erreur de lecture | comma-separated | séparé par des virgules |
| determine | déterminer | position | position, rang |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Votre trajet passe par un train à grande vitesse, mais le billet est écrit dans une langue inconnue : vous ne pouvez lire que les nombres. Vous avez rassemblé dans un fichier les règles de validité des différents champs d’un billet, votre billet, et ceux d’autres voyageurs aperçus à la gare.

    **Ce qu’il faut faire.**

    - Le fichier a trois blocs séparés par une ligne vide. D’abord les règles `nom: a-b or c-d` : la valeur de ce champ doit être dans l’un des deux intervalles, bornes comprises. Puis votre billet (`your ticket:` suivi d’une ligne). Enfin les billets voisins (`nearby tickets:` suivi d’une ligne par billet).

    - Un billet est une suite d’entiers séparés par des virgules. Les champs sont dans le même ordre sur tous les billets, mais on ne sait pas quel champ est à quelle position.

    - Une valeur est non valide si elle ne respecte **aucune** règle : elle ne peut correspondre à aucun champ, quelle que soit sa position.

    - La réponse est la somme de toutes les valeurs non valides des billets voisins (votre propre billet est laissé de côté).

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-bases-de-donnees-et-sql-aoc-2-1 }

Questions de vérification, à traiter sur le cahier :

1.  Pour la règle `2-6 or 9-12`, les valeurs 6, 7 et 9 sont-elles acceptées ?

2.  Une valeur non valide égale à `0` change-t-elle la somme ? Son billet est-il valide pour autant ?

3.  Une valeur peut-elle respecter plusieurs règles à la fois ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-bases-de-donnees-et-sql-aoc-2-2 }

On considère le fichier (inventé) suivant :

```console
poids: 1-4 or 8-12
taille: 3-6 or 10-15
depart: 5-11 or 14-20

your ticket:
9,14,7

nearby tickets:
3,13,10
2,21,10
12,15,11
7,0,13
4,13,10
25,4,4
3,6,11
```

Repérer les valeurs non valides. Vérification : la réponse est `46`. Que remarque-t-on sur le quatrième billet voisin ?

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Lire le fichier <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-bases-de-donnees-et-sql-aoc-2-3 }

Écrire une fonction `lire(nom_fichier)` qui renvoie trois objets : un dictionnaire `regles` (nom du champ $\to$ liste de deux couples de bornes), votre billet et la liste des billets voisins (listes d’entiers).

??? pouce "Coup de pouce"

    `open(...).read().split("\n\n")` sépare les trois blocs, car ils sont séparés par une ligne vide.

!!! encadre "Outil Python : any et all"

    `any(...)` vaut `True` si **au moins une** des valeurs est vraie ; `all(...)` vaut `True` si **toutes** le sont. On leur donne une liste de booléens, ou directement une expression comme dans une compréhension.

    ```python
    valeurs = [3, 8, 12]
    print(any(v > 10 for v in valeurs))   # True : au moins une valeur depasse 10
    print(all(v > 10 for v in valeurs))   # False : pas toutes
    print(all(v > 0 for v in []))         # True : aucun contre-exemple
    ```

    **Intérêt.** Le code se lit comme la phrase « il existe… » ou « pour tout… », et le calcul s’arrête dès que la réponse est connue (premier `True` pour `any`, premier `False` pour `all`).

    **À essayer.** Que vaut `any([])` ? Pourquoi est-ce cohérent avec `all([])` ?

### <span class="exo-num">Exercice 4</span> — Valeurs non valides <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-bases-de-donnees-et-sql-aoc-2-4 }

Écrire une fonction `respecte(valeur, bornes)` puis une fonction `valable_quelque_part(valeur, regles)`. En déduire le taux d’erreur. Tester sur l’exemple de la fiche, puis sur vos données.

??? pouce "Coup de pouce"

    `a <= valeur <= b` s’écrit tel quel en Python. La fonction `any` évite d’écrire une boucle de plus.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    Il s’agit maintenant de déchiffrer votre billet : savoir à quel champ correspond chaque position.

    - Écarter d’abord les billets voisins qui contiennent au moins une valeur non valide.

    - Avec les billets restants, déterminer la position de chaque champ (une seule attribution est possible).

    - La réponse est le produit des valeurs de **votre** billet pour les champs dont le nom commence par `departure`.

### <span class="exo-num">Exercice 5</span> — Ne garder que les bons billets <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-bases-de-donnees-et-sql-aoc-2-5 }

Construire la liste des billets voisins valides. Attention : un billet peut contenir une valeur non valide qui ne change pas la somme de la partie 1. Sur l’exemple de la fiche, il reste 4 billets valides.

!!! encadre "Outil Python : les ensembles (set)"

    Un **ensemble** est une collection **sans doublon** et **sans ordre** : pas d’indice, on peut seulement ajouter, retirer et tester l’appartenance. Attention, `{}` est un dictionnaire vide ; l’ensemble vide s’écrit `set()`.

    ```python
    champs = {"poids", "taille"}     # ensemble ecrit directement
    champs.add("depart")             # ajout (sans effet si deja present)
    champs.discard("taille")         # retrait, sans erreur si l'element est absent
    print("poids" in champs)         # True : test d'appartenance en temps constant
    print(len(champs))               # 2
    seul = {"quai"}
    print(seul.pop())                # quai : retire et renvoie un element
    pairs = {n for n in range(10) if n % 2 == 0}   # ensemble en comprehension
    print({1, 2, 3} & {2, 3, 4})     # {2, 3} : elements communs (intersection)
    ```

    **Intérêt.** Comme les clés d’un dictionnaire, les éléments sont rangés grâce à une *fonction de hachage* : `x in ensemble`, `add` et `discard` prennent un temps qui ne dépend pas de la taille de l’ensemble, alors que `x in liste` peut parcourir toute la liste.

    **À essayer.** Que contient `{1, 2, 2, 3}` ? Que se passe-t-il si l’on remplace `discard` par `remove` pour retirer un élément absent ?

!!! encadre "Outil Python : startswith"

    `s.startswith(debut)` vaut `True` si la chaîne `s` commence par `debut`.

    ```python
    nom = "departure track"
    print(nom.startswith("departure"))       # True
    print("arrival".startswith("depart"))    # False
    ```

    **Intérêt.** Plus lisible et plus sûr que `s[:9] == "departure"`, où il faut compter les lettres.

    **À essayer.** Que renvoie `"dep".startswith("departure")` ?

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Élimination par contraintes <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-bases-de-donnees-et-sql-aoc-2-6 }

Pour chaque position, construire l’**ensemble** des champs compatibles avec *toutes* les valeurs des billets valides à cette position. Puis : tant qu’il reste des positions non attribuées, trouver une position qui n’a plus qu’un seul champ possible, l’attribuer, et retirer ce champ des autres ensembles. Sur l’exemple, la position 0 est compatible avec `poids` et `taille`, la position 1 avec `taille` seulement ; à la fin, `depart` est en position 2 et vaut `7` sur votre billet.

??? pouce "Coup de pouce"

    Un dictionnaire `possibles` associant à chaque position un `set` de noms de champs. La méthode `discard` retire un élément sans erreur s’il est absent.

??? pouce "Coup de pouce 2 (début de solution)"

    La boucle principale est un `while` sur le nombre de positions déjà attribuées. À chaque tour, on cherche une position `p` telle que `len(possibles[p]) == 1`.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 7</span> — Défi : et si l’élimination bloquait ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-bases-de-donnees-et-sql-aoc-2-7 }

Inventer un petit exemple où, à un moment, aucune position n’a un seul champ possible alors qu’une attribution existe. Comment faudrait-il alors chercher la solution ?

??? pouce "Coup de pouce"

    Penser au retour sur trace : on essaie un choix, et on revient en arrière s’il mène à une impasse.
