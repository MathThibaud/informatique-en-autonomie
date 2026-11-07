# Défis Advent of Code

<p class="sous-titre">Bases de données et SQL</p>

## <span class="etiquette">Défi 1</span> Passport Processing

*les passeports — dictionnaires et validation*

<p class="infos-activite">Jour 4</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/06-defi-aoc-2020-04){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-06-defi-aoc-2020-04.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/4 ](https://adventofcode.com/2020/day/4 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (lien ci-dessus) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - **Attention aux exemples.** L’énoncé en ligne a son propre exemple, avec d’autres réponses. Les valeurs de test de cette fiche portent sur **l’exemple inventé de la fiche** (exercice « À la main ») : l’enregistrer dans un fichier `exemple.txt` à côté du programme, et ouvrir `"exemple.txt"` au lieu de `"input.txt"` pour tester.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

!!! encadre "Le défi en bref"

    **Le problème.** Un scanner d’aéroport a lu quelques centaines de passeports, chacun décrit par une suite de champs (année de naissance, taille, couleur des yeux…). Il faut compter les passeports acceptables : d’abord ceux qui ont tous les champs nécessaires, puis ceux dont chaque valeur est plausible. Le fichier est long et ses passeports s’étalent sur un nombre variable de lignes : le travail consiste surtout à bien le découper, puis à appliquer des règles précises sans en oublier.

    **Ce qu’on réinvestit.** La notion de **domaine** vue dans ce chapitre : chaque champ d’un passeport n’est valide que si sa valeur appartient à un domaine précis (une année entre deux bornes, une couleur parmi une liste fixée, un numéro d’exactement neuf chiffres). Vérifier un passeport revient à vérifier, champ par champ, l’appartenance à ces domaines, comme une base de données vérifie ses contraintes avant d’accepter une ligne.

    **La démarche de la fiche.**

    1.  Comprendre ce qu’est un passeport complet, puis trier à la main un petit fichier.

    2.  Découper le fichier en passeports, puis chaque passeport en un dictionnaire.

    3.  Vérifier la présence des champs et compter : c’est la partie 1.

    4.  Partie 2 : écrire une petite fonction testée par champ, puis les combiner.

    5.  En approfondissement, décrire la forme d’une valeur par un motif.

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|                |                  |                    |                    |
|:---------------|:-----------------|:-------------------|:-------------------|
| field          | champ            | required           | obligatoire        |
| missing        | manquant         | optional           | facultatif         |
| batch file     | fichier de lot   | blank line         | ligne vide         |
| key:value pair | paire clé:valeur | at least / at most | au moins / au plus |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Arrivé à l’aéroport, le héros s’aperçoit qu’il a emporté une carte d’identité du pôle Nord, et non son passeport. La file devant les scanners automatiques est interminable, car ces machines vérifient mal les documents. Il faut écrire le programme qui décide si un document est acceptable.

    **Les données.** Le fichier contient les données lues par un scanner.

    - Les passeports sont séparés par une **ligne vide** ; un même passeport peut s’étaler sur une ou plusieurs lignes.

    - Un passeport est une suite de champs `cle:valeur`, séparés par des espaces ou des retours à la ligne, dans un ordre quelconque. Par exemple, `byr:1985` indique une année de naissance 1985.

    - Il existe huit clés : `byr` (année de naissance), `iyr` (année de délivrance), `eyr` (année d’expiration), `hgt` (taille), `hcl` (couleur des cheveux), `ecl` (couleur des yeux), `pid` (numéro de passeport) et `cid` (pays).

    **La règle.**

    - En partie 1, un passeport est valide si les sept premières clés (toutes sauf `cid`) sont présentes.

    - `cid` peut manquer : c’est ce qui laisse passer la carte du héros, à laquelle il manque justement ce champ.

    - Les valeurs ne sont pas encore examinées : seule compte la présence des clés.

    **La réponse attendue.** Le nombre de passeports valides. Par exemple, un passeport qui a les sept premières clés mais pas `cid` compte ; un passeport qui a `cid` mais pas `hgt` ne compte pas.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-bases-de-donnees-et-sql-aoc-1-1 }

**But.** Vérifier qu’on a compris ce qui rend un passeport valide en partie 1, et repérer la difficulté de la lecture du fichier.

**À quoi ça sert ?** Les deux premières questions fixent la règle (présence des clés, pas leur valeur ; `cid` facultatif) ; la troisième montre qu’il faut découper le fichier par passeport, et non par ligne.

Après lecture de l’énoncé et du résumé, vérifier sa compréhension :

1.  Un passeport qui possède les huit champs mais contient `byr:abc` est-il valide en partie 1 ?

2.  Un passeport de sept champs, parmi lesquels `cid`, est-il valide ?

3.  Lire le fichier ligne par ligne rend-il le découpage en passeports facile ? Pourquoi ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-bases-de-donnees-et-sql-aoc-1-2 }

**But.** Repérer les passeports d’un petit fichier et dire lesquels sont complets.

**À quoi ça sert ?** On obtient un exemple dont on **connaît la réponse** (`4`), sur lequel on testera chaque étape du programme : nombre de blocs, dictionnaires, comptage.

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

**But.** Découper le texte du fichier en une liste de blocs, un bloc par passeport.

**À quoi ça sert ?** C’est la difficulté principale de la lecture : un passeport s’étale sur un nombre variable de lignes. Une fois les blocs isolés, chacun se traite indépendamment des autres.

Lire tout le fichier en une chaîne et construire la liste des blocs de texte, un bloc par passeport. Afficher le nombre de blocs.

??? pouce "Coup de pouce"

    Une ligne vide, c’est deux retours à la ligne consécutifs : `texte.split("\n\n")`.

### <span class="exo-num">Exercice 4</span> — Un passeport, un dictionnaire <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-bases-de-donnees-et-sql-aoc-1-4 }

**But.** Transformer un bloc de texte en un dictionnaire qui associe chaque clé à sa valeur.

**À quoi ça sert ?** Le dictionnaire permet de demander directement « la clé `byr` est-elle présente ? » ou « que vaut `hgt` ? », sans chercher dans le texte. Les deux parties travaillent sur ces dictionnaires.

Écrire une fonction `lire_passeport(bloc)` qui renvoie un dictionnaire, par exemple `{"byr": "1985", "hgt": "172cm", ...}`. Garder les valeurs sous forme de chaînes.

??? pouce "Coup de pouce"

    `bloc.split()` sans argument coupe à la fois aux espaces et aux retours à la ligne. Chaque morceau se coupe ensuite en deux au `:`.

!!! encadre "Rappel : « tous » avec un booléen drapeau"

    La méthode est présentée dans l’encadré « Méthode : « tous » ou « au moins un », avec un booléen drapeau » du défi *Handy Haversacks* (chapitre 1) : pour vérifier que **toutes** les valeurs conviennent, on part d’un booléen à `True`, que la boucle passe à `False` au premier contre-exemple.

    **À essayer.** Écrire `complet(passeport)` avec un drapeau `tout_present`. Que renvoie-t-elle si la liste des clés obligatoires est vide ?

### <span class="exo-num">Exercice 5</span> — Compter les passeports complets <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-bases-de-donnees-et-sql-aoc-1-5 }

**But.** Vérifier qu’un passeport possède toutes les clés obligatoires, puis compter les passeports complets.

**À quoi ça sert ?** C’est la réponse de la partie 1. La fonction `complet` resservira en partie 2 : un passeport incomplet y est refusé avant même qu’on examine les valeurs.

Écrire `complet(passeport)` qui vérifie la présence des champs obligatoires, puis compter. Tester sur l’exemple inventé de la fiche, puis sur vos données.

??? pouce "Coup de pouce"

    Ranger les clés obligatoires dans une liste et tester chacune avec l’opérateur `in`, qui teste la présence d’une **clé** dans un dictionnaire.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    **Ce qui change.** Des documents absurdes passent encore : il faut maintenant contrôler aussi les valeurs. Le fichier et le découpage en passeports ne changent pas.

    **La nouvelle règle.** Un passeport est valide si les sept clés sont présentes **et** si chaque valeur respecte sa règle :

    - `byr` est entre 1920 et 2002, `iyr` entre 2010 et 2020, `eyr` entre 2020 et 2030 (quatre chiffres, bornes comprises) ;

    - `hgt` est un nombre suivi de `cm` (de 150 à 193) ou de `in` (de 59 à 76) ;

    - `hcl` est `#` suivi d’exactement six caractères parmi `0-9` et `a-f` ; `ecl` vaut exactement l’un de `amb blu brn gry grn hzl oth` ;

    - `pid` compte exactement neuf chiffres (zéros de tête compris) ; `cid` est ignoré.

    Il suffit qu’une seule valeur sorte de sa règle pour que le passeport soit refusé.

    **La réponse attendue.** Le nombre de passeports valides selon ces règles. Par exemple, `hgt:180cm` est accepté, mais ni `hgt:180` (pas d’unité) ni `hgt:80in` (au-delà de 76 pouces).

!!! encadre "Méthode : tester la forme d’une chaîne (boucle drapeau, tranches)"

    Pour savoir si une chaîne ne contient que des chiffres, on la parcourt avec un booléen drapeau (« tous ») ; les comparaisons de tranches testent le début ou la fin. Tout cela renvoie un booléen qui décrit la forme de la chaîne, sans la convertir.

    ```python
    def que_des_chiffres(s):
        """Renvoie True si s est non vide et ne contient que des chiffres."""
        if len(s) == 0:
            return False
        ok = True
        for c in s:
            if c not in "0123456789":
                ok = False
        return ok

    print(que_des_chiffres("2019"))   # True : que des chiffres
    print(que_des_chiffres("-12"))    # False : le signe n'est pas un chiffre
    print(que_des_chiffres(""))       # False : chaine vide
    taille = "172cm"
    print(taille[-2:] == "cm")      # True : les 2 derniers caracteres
    print(taille[:1] == "#")        # False : le premier caractere
    print(taille[:-2], taille[-2:]) # 172 cm : tranches avec indices negatifs
    ```

    **Intérêt.** Vérifier la forme d’une chaîne **avant** d’appeler `int`, qui provoque une erreur sur `"abc"` ou `"170cm"`.

    **À essayer.** Que renvoient `int("0042")` et `que_des_chiffres("0042")` ?

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

**But.** Écrire et tester une fonction de validation par champ, puis les combiner pour valider un passeport entier.

**À quoi ça sert ?** Une petite fonction testée par règle est bien plus facile à mettre au point qu’une seule longue condition : en cas de mauvaise réponse, les `assert` désignent la règle fautive. Leur combinaison donne la réponse de la partie 2.

1.  Pour chaque champ, écrire une fonction de validation : `valide_byr(valeur)`, `valide_hgt(valeur)`, etc. Pour chacune, écrire au moins un `assert` sur une valeur **acceptée** et un sur une valeur **refusée**, en visant les valeurs limites : par exemple `assert valide_byr("2002")` et `assert not valide_byr("2003")`.

2.  Écrire `valide(passeport)` qui combine le tout, puis compter. Sur l’exemple inventé de la fiche, on doit trouver `2` passeports valides.

??? pouce "Coup de pouce"

    Penser aux chaînes pièges : une taille sans unité, un identifiant trop court, une couleur en majuscules… La fonction `que_des_chiffres` de l’encadré « Méthode » et les tranches `valeur[:-2]` et `valeur[-2:]` sont utiles.

??? pouce "Coup de pouce 2 (début de solution)"

    Un dictionnaire peut associer chaque nom de champ à sa fonction de validation : `regles = {"byr": valide_byr, ...}`. On parcourt alors `regles.items()` et on appelle `fonction(passeport[cle])`.

## Approfondissement

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 7</span> — Défi : décrire la forme par un motif <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-bases-de-donnees-et-sql-aoc-1-7 }

**But.** Écrire une seule fonction générale qui vérifie la forme d’une chaîne d’après un motif.

**À quoi ça sert ?** Plusieurs règles de la partie 2 ne diffèrent que par la forme attendue : une fonction générale évite de répéter la même boucle. Les `assert` déjà écrits garantissent que la réécriture ne change pas les résultats.

Plusieurs règles décrivent la *forme* d’une chaîne, caractère par caractère. On la résume par un **motif** : dans un motif, `9` désigne un chiffre quelconque, `h` un caractère hexadécimal (`0` à `9` ou `a` à `f`) et tout autre caractère doit être recopié tel quel. Par exemple `"#hhhhhh"` décrit `hcl` et `"99h99"` accepte `"08a30"` mais ni `"8a30"` ni `"08g30"`.

1.  Écrire `respecte(motif, valeur)` qui renvoie `True` si `valeur` a la forme décrite par `motif`.

2.  Réécrire `valide_hcl`, `valide_pid` et la vérification des années avec `respecte`. Les tests écrits plus haut doivent toujours passer.

??? pouce "Coup de pouce"

    Commencer par comparer les longueurs, puis parcourir les deux chaînes en parallèle avec un indice `i`.

??? pouce "Coup de pouce 2 (début de solution)"

    Les tests de la partie 2 servent ici de filet de sécurité : on modifie le code, on relance les `assert`.

## <span class="etiquette">Défi 2</span> Ticket Translation

*les billets de train — dictionnaires et ensembles*

<p class="infos-activite">Jour 16</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/06-defi-aoc-2020-16){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-06-defi-aoc-2020-16.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/16 ](https://adventofcode.com/2020/day/16 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (lien ci-dessus) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - **Attention aux exemples.** L’énoncé en ligne a son propre exemple, avec d’autres réponses. Les valeurs de test de cette fiche portent sur **l’exemple inventé de la fiche** (exercice « À la main ») : l’enregistrer dans un fichier `exemple.txt` à côté du programme, et ouvrir `"exemple.txt"` au lieu de `"input.txt"` pour tester.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

!!! encadre "Le défi en bref"

    **Le problème.** On dispose des règles de validité d’une vingtaine de champs et de plus de deux cents billets de train dont on ne lit que les nombres. Il faut d’abord repérer les valeurs impossibles, puis, en partie 2, retrouver à quel champ correspond chaque position du billet. Croiser des milliers de valeurs avec toutes les règles, puis déduire l’attribution des champs, demande un programme organisé.

    **Ce qu’on réinvestit.** Ce défi fait écho aux **contraintes de domaine** vues dans ce chapitre : chaque champ d’un billet n’accepte que certaines valeurs, comme un attribut de base de données, et l’on s’en sert pour écarter les enregistrements incohérents. On utilise aussi des dictionnaires, des booléens drapeaux (« au moins un », « tous ») et des ensembles pour raisonner par élimination.

    **La démarche de la fiche.**

    1.  Vérifier sa compréhension des règles, puis repérer à la main les valeurs non valides d’un petit fichier.

    2.  Lire les trois blocs du fichier, puis tester chaque valeur contre les règles : réponse de la partie 1.

    3.  Écarter les billets non valides, puis attribuer les champs aux positions par élimination : réponse de la partie 2.

    4.  En défi, réfléchir à ce qu’il faudrait faire si l’élimination se bloquait.

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

    **Les données.** Le fichier a trois blocs séparés par une ligne vide.

    - D’abord les règles, une par ligne, de la forme `nom: a-b or c-d` : la valeur de ce champ doit être dans l’un des deux intervalles, bornes comprises.

    - Puis votre billet : la ligne `your ticket:` suivie d’une ligne.

    - Enfin les billets voisins : la ligne `nearby tickets:` suivie d’une ligne par billet.

    Un billet est une suite d’entiers séparés par des virgules. Les champs sont dans le même ordre sur tous les billets, mais on ne sait pas quel champ est à quelle position.

    **La règle.**

    - Une valeur est non valide si elle ne respecte **aucune** règle : elle ne peut correspondre à aucun champ, quelle que soit sa position.

    - Il suffit qu’elle respecte une seule règle (n’importe laquelle) pour ne pas être comptée.

    - On examine seulement les billets voisins : votre propre billet est laissé de côté.

    **La réponse attendue.** La somme de toutes les valeurs non valides des billets voisins. Par exemple, avec les deux règles `1-3 or 7-9` et `4-6 or 10-12` et les billets voisins `2,5`, `8,13` et `20,4`, seules 13 et 20 ne respectent aucune règle : la réponse serait $13 + 20 = 33$.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-bases-de-donnees-et-sql-aoc-2-1 }

**But.** Vérifier sur trois questions courtes qu’on a compris quand une valeur est valide.

**À quoi ça sert ?** Elles visent trois pièges : les bornes comprises, une valeur non valide égale à 0 (invisible dans la somme mais pas pour la partie 2), une valeur compatible avec plusieurs règles.

Questions de vérification, à traiter sur le cahier :

1.  Pour la règle `2-6 or 9-12`, les valeurs 6, 7 et 9 sont-elles acceptées ?

2.  Une valeur non valide égale à `0` change-t-elle la somme ? Son billet est-il valide pour autant ?

3.  Une valeur peut-elle respecter plusieurs règles à la fois ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-bases-de-donnees-et-sql-aoc-2-2 }

**But.** Repérer à la main les valeurs non valides d’un petit fichier.

**À quoi ça sert ?** On obtient un exemple dont on **connaît la réponse** (46). Le même fichier sert d’exemple pour toute la partie 2, et la remarque sur le quatrième billet prépare son premier piège.

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

!!! encadre "Outil Python : strip (nettoyer une ligne lue)"

    Chaque ligne lue dans un fichier (avec `for ligne in fichier` ou `readlines()`) se termine par le caractère de fin de ligne `"\n"` (sauf parfois la dernière). `ligne.strip()` renvoie une copie de la ligne sans les espaces ni les fins de ligne placés au début et à la fin.

    ```python
    ligne = "1721\n"
    print(ligne.strip())                  # 1721
    print(len(ligne), len(ligne.strip())) # 5 4
    ```

    **Intérêt.** Comparer ou découper une ligne sans que la fin de ligne ne gêne : `"abc\n" == "abc"` vaut `False`.

### <span class="exo-num">Exercice 3</span> — Lire le fichier <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-bases-de-donnees-et-sql-aoc-2-3 }

**But.** Transformer les trois blocs du fichier en données Python : un dictionnaire de règles, votre billet, la liste des billets voisins.

**À quoi ça sert ?** Tout le défi travaille sur ces trois objets : une fois le fichier lu, on n’a plus à manipuler de texte.

Écrire une fonction `lire(nom_fichier)` qui renvoie trois objets : un dictionnaire `regles` (nom du champ $\to$ liste de deux couples de bornes), votre billet et la liste des billets voisins (listes d’entiers).

??? pouce "Coup de pouce"

    `open(...).read().strip().split("\n\n")` sépare les trois blocs, car ils sont séparés par une ligne vide.

!!! encadre "Rappel : « au moins un » et « tous » avec un booléen drapeau"

    La méthode est présentée dans l’encadré « Méthode : « tous » ou « au moins un », avec un booléen drapeau » du défi *Handy Haversacks* (chapitre 1) : pour « au moins un », le drapeau part de `False` et passe à `True` au premier exemple ; pour « tous », il part de `True` et passe à `False` au premier contre-exemple.

    **À essayer.** Pour une liste vide, que vaut à la fin un drapeau « au moins un » ? un drapeau « tous » ? Pourquoi ces deux résultats sont-ils cohérents ?

### <span class="exo-num">Exercice 4</span> — Valeurs non valides <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-bases-de-donnees-et-sql-aoc-2-4 }

**But.** Tester si une valeur respecte au moins une règle, puis additionner les valeurs qui n’en respectent aucune.

**À quoi ça sert ?** Cette somme est la réponse de la partie 1, et la fonction `valable_quelque_part` servira de nouveau en partie 2 pour trier les billets.

Écrire une fonction `respecte(valeur, bornes)` puis une fonction `valable_quelque_part(valeur, regles)`. En déduire la réponse de la partie 1 : la somme des valeurs non valides (l’énoncé en ligne l’appelle « taux d’erreur »). Tester sur l’exemple inventé de la fiche, puis sur vos données.

??? pouce "Coup de pouce"

    `a <= valeur <= b` s’écrit tel quel en Python. Les deux fonctions sont des « au moins un » : un drapeau initialisé à `False` dans chacune.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    **Ce qui change.** Il s’agit maintenant de déchiffrer votre billet : savoir à quel champ correspond chaque position.

    **La nouvelle règle.**

    - Écarter d’abord les billets voisins qui contiennent au moins une valeur non valide (même si cette valeur vaut 0).

    - Avec les billets restants, déterminer la position de chaque champ : un champ ne peut être à une position que si **toutes** les valeurs des billets restants à cette position respectent sa règle. Une seule attribution est possible.

    - Repérer les champs dont le nom commence par `departure`.

    **La réponse attendue.** Le produit des valeurs de **votre** billet pour les champs dont le nom commence par `departure`. Par exemple, s’il n’y avait que deux tels champs et que votre billet portait 7 et 11 à leurs positions, la réponse serait 77.

### <span class="exo-num">Exercice 5</span> — Ne garder que les bons billets <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-bases-de-donnees-et-sql-aoc-2-5 }

**But.** Ne conserver que les billets voisins dont toutes les valeurs sont valides.

**À quoi ça sert ?** Seuls ces billets sont fiables pour déduire la position des champs : un seul billet faux suffirait à fausser l’attribution.

Construire la liste des billets voisins valides. Attention : un billet peut contenir une valeur non valide qui ne change pas la somme de la partie 1. Sur l’exemple inventé de la fiche, il reste 4 billets valides.

!!! encadre "Outil Python : les ensembles (set) — rappel"

    Tout est présenté dans l’encadré « Outil Python : les ensembles » du défi *Crab Combat* (chapitre 4) : `set()`, `add`, `remove`, test `x in ensemble` en temps constant, éléments non modifiables (tuples). Dans ce défi, ces opérations suffisent.

    **À essayer.** Que contient `{1, 2, 2, 3}` ? Que se passe-t-il si l’on appelle `remove` pour retirer un élément absent ? Comment l’éviter avec un test `in` ?

!!! encadre "Outil Python : tester le début d’une chaîne avec une tranche"

    `s[:n]` est la chaîne des `n` premiers caractères de `s`. Pour savoir si `s` commence par `debut`, on compare `s[:len(debut)]` à `debut`.

    ```python
    nom = "departure track"
    debut = "departure"
    print(nom[:len(debut)] == debut)     # True
    print("arrival"[:6] == "depart")     # False
    ```

    **Intérêt.** `len(debut)` évite de compter les lettres à la main. Une tranche plus longue que la chaîne ne provoque pas d’erreur : elle s’arrête à la fin de la chaîne.

    **À essayer.** Que vaut `"dep"[:9]` ? En déduire la valeur de `"dep"[:9] == "departure"`.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Élimination par contraintes <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-bases-de-donnees-et-sql-aoc-2-6 }

**But.** Déduire la position de chaque champ, d’abord en listant les champs possibles par position, puis par élimination.

**À quoi ça sert ?** C’est le cœur de la partie 2 : une fois chaque champ placé, on lit sur votre billet les valeurs des champs `departure` et l’on obtient la réponse.

Pour chaque position, construire l’**ensemble** des champs compatibles avec *toutes* les valeurs des billets valides à cette position. Puis : tant qu’il reste des positions non attribuées, trouver une position qui n’a plus qu’un seul champ possible, l’attribuer, et retirer ce champ des autres ensembles. Sur l’exemple, la position 0 est compatible avec `poids` et `taille`, la position 1 avec `taille` seulement ; à la fin, `depart` est en position 2 et vaut `7` sur votre billet.

??? pouce "Coup de pouce"

    Un dictionnaire `possibles` associant à chaque position un `set` de noms de champs. Avant d’appeler `remove`, tester avec `in` que le champ est encore dans l’ensemble. Pour récupérer l’unique élément d’un ensemble, une boucle `for` suffit.

??? pouce "Coup de pouce 2 (début de solution)"

    La boucle principale est un `while` sur le nombre de positions déjà attribuées. À chaque tour, on cherche une position `p` telle que `len(possibles[p]) == 1`.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 7</span> — Défi : et si l’élimination bloquait ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-bases-de-donnees-et-sql-aoc-2-7 }

**But.** Imaginer un cas où l’élimination ne suffit pas, et la méthode qu’il faudrait alors employer.

**À quoi ça sert ?** La méthode de la fiche fonctionne parce que les données s’y prêtent ; savoir repérer ses limites conduit au retour sur trace, une méthode générale de recherche de solution.

Inventer un petit exemple où, à un moment, aucune position n’a un seul champ possible alors qu’une attribution existe. Comment faudrait-il alors chercher la solution ?

??? pouce "Coup de pouce"

    Penser au retour sur trace : on essaie un choix, et on revient en arrière s’il mène à une impasse.
