# Défis Advent of Code

<p class="sous-titre">Arbres</p>

## <span class="etiquette">Défi 1</span> Binary Boarding

*les cartes d’embarquement — binaire et dichotomie*

<p class="infos-activite">Jour 5</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/05-defi-aoc-2020-05){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-05-defi-aoc-2020-05.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/5 ](https://adventofcode.com/2020/day/5 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (lien ci-dessus) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - **Attention aux exemples.** L’énoncé en ligne a son propre exemple, avec d’autres réponses. Les valeurs de test de cette fiche portent sur **l’exemple inventé de la fiche** (exercice « À la main ») : l’enregistrer dans un fichier `exemple.txt` à côté du programme, et ouvrir `"exemple.txt"` au lieu de `"input.txt"` pour tester.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

!!! encadre "Le défi en bref"

    **Le problème.** Chaque carte d’embarquement porte un code de dix lettres qui désigne un siège de l’avion. Il faut décoder plusieurs centaines de ces codes pour trouver le plus grand numéro de siège, puis le seul siège libre : celui du héros. Décoder un code à la main prend une minute ; en décoder des centaines demande un programme.

    **Ce qu’on réinvestit.** Les **arbres binaires** vus dans ce chapitre. Un code de place décrit un chemin depuis la racine d’un arbre binaire complet : chaque lettre choisit le fils gauche ou le fils droit, c’est-à-dire la moitié basse ou la moitié haute des places restantes, et la feuille atteinte est le siège. On découvrira que ce chemin n’est autre que l’écriture binaire du numéro, et qu’il s’agit d’une dichotomie.

    **La démarche de la fiche.**

    1.  Comprendre le découpage en moitiés, puis décoder un code à la main.

    2.  Reconnaître que le code est un nombre écrit en binaire.

    3.  Écrire la fonction de décodage et chercher le plus grand numéro : c’est la partie 1 ; la réécrire par dichotomie.

    4.  Partie 2 : trier les numéros et trouver le trou.

    5.  En approfondissement, trouver le trou sans trier.

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| boarding pass | carte d’embarquement | seat | siège, place |
| row / column | rang / colonne | seat ID | numéro de siège |
| front / back | avant / arrière | lower / upper half | moitié basse / haute |
| binary space partitioning | partition binaire de l’espace | sanity check | vérification de bon sens |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Le héros est enfin dans l’avion… mais il a perdu sa carte d’embarquement. Il photographie celles des autres passagers pour retrouver sa place par élimination. La première étape est de savoir lire ces cartes.

    **Les données.** Chaque ligne du fichier est le code de place imprimé sur une carte : 10 lettres. Les 7 premières (`F` ou `B`) donnent le rang, numéroté de 0 à 127 ; les 3 dernières (`L` ou `R`) donnent la colonne, de 0 à 7.

    **La règle.**

    - Pour le rang, on part de l’intervalle complet des rangs, de 0 à 127.

    - Chaque lettre coupe l’intervalle restant en deux moitiés égales : `F` garde la moitié basse, `B` la moitié haute. Après la septième lettre, il ne reste qu’un rang.

    - On procède de même pour la colonne, de 0 à 7, avec `L` (moitié basse) et `R` (moitié haute) : après trois lettres, il ne reste qu’une colonne.

    - Chaque siège a un numéro : rang $\times 8$ + colonne.

    **La réponse attendue.** Le plus grand numéro de siège présent dans le fichier. Par exemple, le code `FFFFFFBRLL` désigne le rang 1 et la colonne 4, donc le siège numéro $1 \times 8 + 4 = 12$.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-arbres-aoc-1-1 }

**But.** Vérifier qu’on sait interpréter un code dans les cas extrêmes.

**À quoi ça sert ?** Les cas extrêmes donnent les bornes des rangs et des numéros ; la dernière question prépare l’idée qu’un code et un numéro se correspondent un à un, ce qui justifiera la lecture en binaire.

Après lecture de l’énoncé et du résumé, vérifier sa compréhension :

1.  Quel rang donne `FFFFFFF` ? Et `BBBBBBB` ?

2.  Quels sont le plus petit et le plus grand numéro de siège possibles ?

3.  Deux codes différents peuvent-ils donner le même numéro de siège ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-arbres-aoc-1-2 }

**But.** Décoder deux codes à la main en suivant la méthode de l’énoncé, puis comparer avec l’écriture binaire.

**À quoi ça sert ?** On obtient des valeurs connues (`75`, `2`, `602`) pour tester le programme, et l’on soupçonne déjà un raccourci : le rang et la colonne se lisent peut-être directement en binaire.

Décoder à la main le code `BFFBFBBLRL` en suivant la méthode de l’énoncé (diviser l’intervalle par deux à chaque lettre). On doit trouver le rang `75`, la colonne `2` et le numéro `602`.

Faire de même avec `FFBBFBFRLR`, puis comparer : écrire `75` et `2` en binaire. Que remarque-t-on ?

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Reconnaître le binaire <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-arbres-aoc-1-3 }

**But.** Montrer que le code de place est l’écriture binaire du numéro de siège.

**À quoi ça sert ?** Ce constat remplace sept puis trois découpages par une simple conversion de base : la fonction de décodage tiendra en quelques lignes.

1.  Remplacer dans `BFFBFBBLRL` chaque `F` et chaque `L` par `0`, chaque `B` et chaque `R` par `1`. Que vaut le nombre binaire obtenu ? Le comparer au numéro de siège.

2.  Expliquer pourquoi « multiplier le rang par 8 puis ajouter la colonne » revient à recoller les deux écritures binaires.

??? pouce "Coup de pouce"

    Multiplier par $8 = 2^3$ décale l’écriture binaire de trois rangs vers la gauche, ce qui laisse exactement la place des 3 bits de la colonne.

!!! encadre "Outil Python : conversions binaires (int(..., 2), bin) et traduction lettre par lettre"

    Python sait lire et écrire des nombres en base 2. Une chaîne n’étant pas modifiable, pour « traduire » ses lettres on construit une **nouvelle** chaîne en la parcourant, avec un dictionnaire qui donne la traduction de chaque lettre.

    ```python
    print(int("1011", 2))          # 11 : lit une chaine ecrite en base 2
    print(bin(11))                 # 0b1011 : ecriture binaire (une chaine)
    traduction = {"F": "0", "B": "1"}
    mot = "FBFB"
    binaire = ""
    for lettre in mot:
        binaire = binaire + traduction[lettre]
    print(binaire)                 # 0101 : nouvelle chaine
    print(mot)                     # FBFB : mot n'a pas change
    ```

    **Intérêt.** La conversion et la traduction prennent un temps proportionnel au nombre de caractères : un seul parcours suffit.

    **À essayer.** Que vaut `int("1111111111", 2)` ? Quel lien avec le plus grand numéro de siège possible ?

### <span class="exo-num">Exercice 4</span> — Décoder et chercher le maximum <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-arbres-aoc-1-4 }

**But.** Écrire la fonction qui décode un code, puis parcourir le fichier pour trouver le plus grand numéro.

**À quoi ça sert ?** C’est la réponse de la partie 1. La liste des numéros obtenus resservira telle quelle pour chercher la place libre en partie 2.

Écrire une fonction `numero_siege(code)` qui renvoie le numéro de siège, puis le programme qui donne la réponse sur `input.txt`. Vérifier `numero_siege("BFFBFBBLRL") == 602`. Sur la liste (inventée) `BFFBFBBLRL`, `FBBFFFBRRR`, `BBFBFFFLLR`, `FFBBFBFRLR`, `BFBBBFFLRR`, on doit trouver `833`.

??? pouce "Coup de pouce"

    `int("1011", 2)` convertit une chaîne écrite en binaire en entier. Pour traduire les lettres, parcourir le code avec un dictionnaire `{"F": "0", "B": "1", "L": "0", "R": "1"}` (voir l’encadré). Pour le maximum, une variable qui garde le plus grand numéro vu jusqu’ici.

### <span class="exo-num">Exercice 5</span> — Le lien avec la dichotomie <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-arbres-aoc-1-5 }

**But.** Réécrire le décodage en suivant littéralement l’énoncé : deux bornes et un intervalle divisé par deux à chaque lettre.

**À quoi ça sert ?** Comparer les deux versions montre que chaque lettre est un choix gauche ou droite dans un arbre binaire, comme dans une recherche dichotomique. Le nombre de lettres nécessaire est le nombre de divisions par deux, d’où le lien avec le logarithme en base 2.

Écrire une seconde version `numero_siege_dicho(code)` qui suit littéralement l’énoncé : deux bornes `bas` et `haut`, et chaque lettre garde une moitié. Vérifier qu’elle donne les mêmes résultats que la première. Combien de lettres faudrait-il pour un avion de $1024$ rangs ?

??? pouce "Coup de pouce"

    Le milieu est `(bas + haut) // 2` ; une lettre « basse » modifie `haut`, une lettre « haute » modifie `bas`.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    **Ce qui change.** Il reste à trouver la place du héros, puisque c’est la seule dont la carte manque. On utilise les mêmes numéros de siège que dans la partie 1.

    **La nouvelle règle.**

    - L’avion est plein, sauf quelques sièges tout à l’avant et tout à l’arrière qui n’existent pas : ces numéros-là manquent aussi dans la liste, mais ce ne sont pas des places.

    - Le siège du héros est absent de la liste, mais les numéros juste avant et juste après le sien y figurent.

    **La réponse attendue.** Le numéro du siège du héros. Par exemple, si les numéros présents étaient 40, 41, 43 et 44, sa place serait la 42.

### <span class="exo-num">Exercice 6</span> — La place libre <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-arbres-aoc-1-6 }

**But.** Trouver le seul numéro manquant entre deux numéros présents.

**À quoi ça sert ?** C’est la réponse de la partie 2. Une fois les numéros triés, le trou se voit en comparant chaque numéro au suivant.

Trouver la place du héros en suivant les indications de la partie 2.

??? pouce "Coup de pouce"

    Trier la liste des numéros avec un tri écrit par vous (le tri par insertion de Première), puis la parcourir en comparant chaque numéro au suivant.

??? pouce "Coup de pouce 2 (début de solution)"

    Dans la liste triée, le trou se repère au premier indice `k` tel que `tries[k + 1] != tries[k] + 1` : la place cherchée est alors `tries[k] + 1`.

## Approfondissement

!!! encadre "Outil Python : les ensembles (set) — rappel"

    Tout est présenté dans l’encadré « Outil Python : les ensembles » du défi *Crab Combat* (chapitre 4). On n’utilise ici que `set()` (ensemble vide), `add`, `remove` et le test `x in ensemble`, en temps constant (en moyenne). Les éléments doivent être non modifiables (nombres, chaînes, tuples).

    **À essayer.** Construire l’ensemble des numéros de la liste inventée de la partie 1 (les cinq codes de l’exercice « Décoder et chercher le maximum ») en partant de `set()` et en ajoutant chaque numéro avec `add`, puis tester si `602` et `603` en font partie.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — La place libre avec un ensemble <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-arbres-aoc-1-7 }

**But.** Trouver la place libre sans trier, en testant l’appartenance de chaque candidat à un ensemble.

**À quoi ça sert ?** C’est une autre méthode sans tri, qui ne demande aucune astuce de calcul : on teste chaque candidat, et chaque test coûte un temps constant. Comparer les complexités des méthodes, c’est choisir en connaissance de cause.

1.  Répondre à la question « À essayer » de l’encadré (le code complet est dans le défi *Crab Combat*, chapitre 4).

2.  À la main : les numéros présents sont $\{12, 13, 14, 16, 17\}$. Parcourir les entiers de $12$ à $17$ et dire, pour chacun, s’il est dans l’ensemble. Quelle place est libre ?

3.  Écrire `place_libre_ensemble(numeros)` qui trouve la place libre sans trier, puis vérifier qu’elle donne le même résultat que l’exercice de la partie 2.

4.  Comparer les complexités des deux méthodes (tri, ensemble).

??? pouce "Coup de pouce"

    Les seules places candidates sont les entiers compris entre le plus petit numéro présent `mini` et le plus grand `maxi`, à calculer par une boucle : `range(mini, maxi)`.

??? pouce "Coup de pouce 2 (début de solution)"

    On parcourt ces entiers et l’on renvoie le premier qui n’est pas dans l’ensemble `presents` (rempli avec `add`) : chaque test coûte un temps constant.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 8</span> — Défi : sans tri <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-arbres-aoc-1-8 }

**But.** Trouver la place libre en un seul parcours, sans trier, à l’aide d’un calcul de somme.

**À quoi ça sert ?** Le tri coûte plus qu’un parcours : un raisonnement mathématique permet ici de descendre à un coût linéaire, avec très peu de mémoire.

Trouver la place libre en temps linéaire sans trier ni utiliser d’ensemble, en comparant la somme des numéros présents à une somme connue.

??? pouce "Coup de pouce"

    La somme des entiers de $a$ à $b$ vaut $\frac{(a+b)(b-a+1)}{2}$.

## <span class="etiquette">Défi 2</span> Custom Customs

*la douane — ensembles, union et intersection*

<p class="infos-activite">Jour 6</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/05-defi-aoc-2020-06){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-05-defi-aoc-2020-06.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/6 ](https://adventofcode.com/2020/day/6 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (lien ci-dessus) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - **Attention aux exemples.** L’énoncé en ligne a son propre exemple, avec d’autres réponses. Les valeurs de test de cette fiche portent sur **l’exemple inventé de la fiche** (exercice « À la main ») : l’enregistrer dans un fichier `exemple.txt` à côté du programme, et ouvrir `"exemple.txt"` au lieu de `"input.txt"` pour tester.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

!!! encadre "Le défi en bref"

    **Le problème.** Des passagers, répartis en groupes de voyage, ont rempli un formulaire de 26 questions fermées. Pour chaque groupe, il faut compter les questions auxquelles quelqu’un a répondu oui (partie 1), puis celles auxquelles tout le monde a répondu oui (partie 2), et faire la somme sur plusieurs centaines de groupes. Compter à la main sans doublon ni oubli est fastidieux ; avec la bonne structure de données, le programme est très court.

    **Ce qu’on réinvestit.** Les **ensembles** et leurs opérations : « au moins une personne » correspond à la réunion, « toutes les personnes » à l’intersection. Un ensemble peut se représenter par un arbre binaire de recherche, vu dans ce chapitre : tester l’appartenance d’une valeur coûte alors la hauteur de l’arbre. Le type `set` de Python, lui, utilise une table de hachage, comme les dictionnaires.

    **La démarche de la fiche.**

    1.  Comprendre ce qu’on compte dans un groupe, puis le calculer à la main sur un petit fichier.

    2.  Découper le fichier en groupes, puis en personnes.

    3.  Réunir les réponses de chaque groupe et sommer : c’est la partie 1.

    4.  Partie 2 : remplacer la réunion par l’intersection.

    5.  En approfondissement, résoudre les deux parties avec un dictionnaire de compteurs.

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| customs | douane | declaration form | formulaire de déclaration |
| yes-or-no question | question fermée (oui/non) | group | groupe |
| anyone | au moins une personne | everyone | tout le monde |
| duplicate | doublon | sum of those counts | somme de ces nombres |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Pendant le vol, on distribue des formulaires de douane comportant 26 questions fermées, repérées par les lettres de `a` à `z`. Le héros aide les autres passagers, regroupés par groupes de voyage, à les remplir. On veut résumer leurs réponses groupe par groupe.

    **Les données.** Le fichier recense les réponses.

    - Les groupes sont séparés par une **ligne vide** ; à l’intérieur d’un groupe, il y a une ligne par personne.

    - Une ligne contient, sans doublon et dans un ordre quelconque, les lettres des questions où la personne a répondu oui. Une question absente de la ligne correspond donc à un non.

    **La règle.**

    - Pour chaque groupe, on compte les lettres différentes cochées par **au moins une** personne du groupe.

    - Une même lettre cochée par plusieurs personnes du groupe ne compte qu’une fois.

    - On fait ce calcul pour chaque groupe séparément, puis on additionne.

    **La réponse attendue.** La somme de ces nombres sur tous les groupes. Par exemple, pour un groupe formé des lignes `ab` et `bc`, les lettres cochées sont `a`, `b`, `c` : ce groupe compte pour 3.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-arbres-aoc-2-1 }

**But.** Vérifier qu’on a compris ce qu’on compte dans un groupe et comment le fichier délimite les groupes.

**À quoi ça sert ?** La première question montre que les doublons ne comptent pas, la deuxième que l’ordre est sans importance (deux propriétés exactes d’un ensemble) ; la troisième prépare le découpage du fichier en groupes.

Après lecture de l’énoncé et du résumé, vérifier sa compréhension :

1.  Un groupe formé des deux lignes `ab` et `ba` compte pour combien ?

2.  L’ordre des lettres dans une ligne a-t-il une importance ? Et l’ordre des personnes dans un groupe ?

3.  Peut-on traiter le fichier ligne par ligne sans perdre l’information « fin de groupe » ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-arbres-aoc-2-2 }

**But.** Découper un petit fichier en groupes et calculer, pour chacun, l’ensemble des lettres cochées.

**À quoi ça sert ?** On obtient un exemple dont on **connaît la réponse** (`15`) pour tester le programme ; écrire les ensembles à la main fait apparaître l’opération à programmer.

```console
xyz
yz

m
m
m

pqr
qrs
rst

abcd

hk
kh
h
```

On considère le fichier (inventé) suivant.

1.  Combien contient-il de groupes, et combien de personnes dans chaque groupe ?

2.  Pour chaque groupe, écrire l’ensemble des lettres demandé par la partie 1 et son cardinal.

Vérification : la somme doit valoir `15`.

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Découper en groupes <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-arbres-aoc-2-3 }

**But.** Transformer le fichier en une liste de groupes, chaque groupe étant la liste des réponses de ses membres.

**À quoi ça sert ?** Les deux parties posent leur question groupe par groupe : avec cette liste, il suffira d’écrire une fonction qui traite un groupe, puis de l’appliquer à chacun.

Lire tout le fichier en une chaîne et construire une liste de groupes, chaque groupe étant la liste des lignes de ses membres. Afficher le nombre de groupes.

??? pouce "Coup de pouce"

    Couper d’abord aux lignes vides (`"\n\n"`), puis couper chaque bloc avec `split()`.

!!! encadre "Outil Python : les ensembles (set) — rappel"

    Tout est présenté dans l’encadré « Outil Python : les ensembles » du défi *Crab Combat* (chapitre 4) : ensemble vide `set()`, ajout avec `add`, retrait avec `remove`, test `x in ensemble` en temps constant, éléments non modifiables (tuples), réunion `a | b` et intersection `a & b`. Un ensemble ne contient jamais deux fois le même élément.

    **À essayer.** Que renvoie `len(set("banane"))` ? Après `e = set("abc")`, puis `e.add("d")`, `e.add("a")` et `e.remove("b")`, que contient `e` ? Que valent `set("abc") | set("bcd")` et `set("abc") & set("bcd")` ?

### <span class="exo-num">Exercice 4</span> — Réunir les réponses <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-arbres-aoc-2-4 }

**But.** Calculer, pour un groupe, le nombre de lettres cochées par au moins une personne, puis faire la somme sur tous les groupes.

**À quoi ça sert ?** C’est la réponse de la partie 1. La réunion d’ensembles élimine d’elle-même les doublons, sans aucun test à écrire.

Écrire une fonction `nb_oui_quelquun(groupe)` qui renvoie le nombre de lettres présentes chez au moins un membre, puis faire la somme sur tout le fichier. Tester sur l’exemple inventé de la fiche, puis sur vos données.

??? pouce "Coup de pouce"

    `set("pqr")` donne l’ensemble `{"p", "q", "r"}`. Les doublons disparaissent d’eux-mêmes dans un ensemble.

??? pouce "Coup de pouce 2 (début de solution)"

    Partir d’un ensemble vide `set()`, puis, pour chaque membre, le remplacer par sa réunion avec l’ensemble des lettres de ce membre : `reunion = reunion | set(personne)`.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    **Ce qui change.** Le héros a mal lu la consigne : ce qui compte n’est pas ce que quelqu’un a coché, mais ce que tout le groupe a coché. Le fichier et le découpage en groupes restent les mêmes.

    **La nouvelle règle.**

    - Pour chaque groupe, on compte les lettres cochées par **toutes** les personnes du groupe.

    - Une lettre oubliée par une seule personne du groupe ne compte plus.

    **La réponse attendue.** La somme de ces nombres sur tous les groupes. Par exemple, le groupe formé des lignes `ab` et `bc` ne compte plus que pour 1 : seule la lettre `b` est cochée par les deux personnes.

### <span class="exo-num">Exercice 5</span> — Changer d’opération <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-arbres-aoc-2-5 }

**But.** Reconnaître l’opération sur les ensembles qui traduit « toutes les personnes », puis adapter la fonction.

**À quoi ça sert ?** C’est la réponse de la partie 2, obtenue en changeant une seule opération. Attention au point de départ du calcul, qui ne peut plus être l’ensemble vide.

1.  Quelle opération sur les ensembles correspond à la nouvelle question ?

2.  Écrire la fonction correspondante et faire la somme. Sur l’exemple inventé de la fiche, on doit trouver `9`.

??? pouce "Coup de pouce"

    Les lettres communes à deux ensembles `a` et `b` forment leur intersection `a & b`. Il suffit de remplacer `|` par `&` dans la fonction de la partie 1… ou presque (voir le coup de pouce suivant).

??? pouce "Coup de pouce 2 (début de solution)"

    Attention au point de départ : partir de l’ensemble vide ne marche plus ici. Partir plutôt de l’ensemble des réponses du **premier** membre du groupe.

## Approfondissement

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 6</span> — Défi : sans ensembles <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-arbres-aoc-2-6 }

**But.** Résoudre les deux parties avec un dictionnaire de compteurs au lieu d’ensembles.

**À quoi ça sert ?** Un même dictionnaire répond aux deux questions à la fois : on voit qu’une structure qui garde un peu plus d’information (combien de personnes, et pas seulement « oui ou non ») peut servir à plusieurs usages.

Résoudre les deux parties sans ensemble, avec un dictionnaire qui compte, pour chaque lettre, le nombre de membres du groupe qui l’ont cochée. Comment lit-on alors les deux réponses dans ce dictionnaire ?

??? pouce "Coup de pouce"

    Une lettre compte pour la partie 2 si son compteur est égal au nombre de membres du groupe.
