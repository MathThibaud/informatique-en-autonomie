# Défis Advent of Code

<p class="sous-titre">Structures linéaires : piles, files, listes chaînées</p>

## <span class="etiquette">Défi 1</span> Operation Order

*les devoirs de maths — piles et analyse d’expressions*

<p class="infos-activite">Jour 18</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/03-defi-aoc-2020-18){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-03-defi-aoc-2020-18.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/18 ](https://adventofcode.com/2020/day/18 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (lien ci-dessus) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - **Attention aux exemples.** L’énoncé en ligne a son propre exemple, avec d’autres réponses. Les valeurs de test de cette fiche portent sur **l’exemple inventé de la fiche** (exercice « À la main ») : l’enregistrer dans un fichier `exemple.txt` à côté du programme, et ouvrir `"exemple.txt"` au lieu de `"input.txt"` pour tester.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

!!! encadre "Le défi en bref"

    **Le problème.** Le fichier contient plusieurs centaines de calculs avec des additions, des multiplications et des parenthèses imbriquées, mais les règles de priorité ne sont pas les règles habituelles. On veut la somme de tous les résultats. Python ne peut pas faire le calcul à notre place (il applique ses propres priorités) : il faut écrire soi-même un programme qui **évalue** une expression.

    **Ce qu’on réinvestit.** Les **piles** vues dans ce chapitre. Comme pour la vérification d’un parenthésage, une pile permet de traiter les parenthèses imbriquées : à chaque parenthèse ouvrante, on met de côté le calcul en cours (on l’empile) pour calculer l’intérieur, et à la parenthèse fermante on le reprend (on le dépile). La récursivité, qui utilise en coulisse la pile des appels, offre une autre solution.

    **La démarche de la fiche.**

    1.  Comprendre la règle de calcul sur des questions courtes, puis calculer un petit exemple à la main.

    2.  Découper chaque ligne en une liste de symboles (nombres, opérateurs, parenthèses).

    3.  Évaluer une liste de symboles avec la règle de la partie 1 (pile ou récursivité) : la somme sur le fichier est la réponse.

    4.  Adapter le programme à la nouvelle priorité de la partie 2.

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| homework | devoirs à la maison | expression | expression (calcul) |
| addition / multiplication | addition / multiplication | parentheses | parenthèses |
| evaluate | calculer, évaluer | precedence | priorité (des opérations) |
| left-to-right | de gauche à droite | regardless of | quel que soit |
| resulting value | valeur obtenue | sum | somme |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** En 2020, les elfes vous ont laissé partir en vacances sous les tropiques. Pendant un vol, un enfant assis à côté de vous vous demande de l’aide pour ses devoirs de calcul... mais dans son école, les règles de priorité ne sont pas celles que vous connaissez. Il faut donc refaire tous ses calculs avec les règles de son école.

    **Les données.** Chaque ligne du fichier est une expression du cahier. Elle contient des entiers positifs (d’un seul chiffre dans les données), les opérateurs `+` (addition) et `*` (multiplication), et des parenthèses, éventuellement imbriquées. Les nombres et les opérateurs sont séparés par des espaces ; une parenthèse est collée au nombre qui la suit ou la précède, comme dans `(2 + 4)`.

    **La règle.**

    - Les parenthèses gardent leur rôle : leur contenu se calcule d’abord, en commençant par les plus intérieures.

    - En revanche, `*` n’est **pas** prioritaire sur `+` : les deux opérateurs ont la même priorité.

    - En dehors des parenthèses, on effectue donc les opérations dans l’ordre où on les lit, de gauche à droite. Autrement dit, `2 + 3 * 4` se calcule comme `(2 + 3) * 4`.

    **La réponse attendue.** La somme des valeurs de toutes les lignes. Par exemple, un fichier de deux lignes `1 + 2 * 3` (qui vaut $3 \times 3 = 9$) et `2 * (1 + 1)` (qui vaut 4) donnerait 13.

### <span class="exo-num">Exercice 1</span> — Vérifier sa compréhension <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-structures-lineaires-piles-files-listes-aoc-1-1 }

**But.** S’entraîner à calculer avec la règle « de gauche à droite », parenthèses comprises.

**À quoi ça sert ?** On doit désapprendre un réflexe (la multiplication d’abord) : mieux vaut le faire sur des calculs courts avant de programmer. La dernière question vérifie qu’on n’aura pas de souci de taille d’entiers.

1.  Que valent `2 * 3 + 4` et `2 + 3 * 4` avec cette règle ?

2.  Que vaut `2 * (3 + 4) * 2` ? Et `((1 + 2))` ?

3.  La somme finale dépasse largement $10^{9}$ : est-ce un problème en Python ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-structures-lineaires-piles-files-listes-aoc-1-2 }

**But.** Calculer à la main trois expressions avec parenthèses.

**À quoi ça sert ?** On obtient la valeur attendue de chaque ligne (et leur somme, 106) : ce seront les tests du programme. On voit aussi pourquoi `eval` ne convient pas.

On considère le fichier (inventé) suivant :

```console
3 * (2 + 4) + 5
2 + 3 * 4 + (1 * 6)
(4 + 5 * (2 + 1)) * 2 + 3
```

Calculer chaque ligne avec la règle de l’énoncé, en écrivant les étapes comme sur le site. Vérification : les trois valeurs ont pour somme `106`. Quelle valeur Python donne-t-il pour la deuxième ligne avec `eval` ? Pourquoi ne peut-on donc pas utiliser `eval` directement ?

## Programmer la partie 1

!!! encadre "Méthode : reconnaître un chiffre, ignorer un espace"

    Un caractère `c` est un chiffre exactement quand `c in "0123456789"` vaut `True`. Pour ignorer les espaces, il suffit de ne rien faire quand `c == " "` : on construit une nouvelle chaîne en n’y ajoutant que les autres caractères.

    ```python
    print("7" in "0123456789")   # True
    print("+" in "0123456789")   # False
    s = "3 * (2 + 4)"
    sans_espaces = ""
    for c in s:
        if c != " ":
            sans_espaces += c
    print(sans_espaces)          # 3*(2+4)
    print(s)                     # s est inchange : 3 * (2 + 4)
    ```

    **Intérêt.** Ces deux tests suffisent pour découper une ligne caractère par caractère. Question : recopier et exécuter ce code ; que valent `"12" in "0123456789"` et `"13" in "0123456789"` ? Pourquoi faut-il tester les caractères **un par un** ?

### <span class="exo-num">Exercice 3</span> — Découper une ligne en symboles <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-structures-lineaires-piles-files-listes-aoc-1-3 }

**But.** Transformer une ligne de texte en une liste de symboles exploitables : entiers, opérateurs et parenthèses.

**À quoi ça sert ?** Le calcul est bien plus simple sur une liste comme `[3, ’*’, ’(’, 2, ’+’, 4, ’)’]` que sur une chaîne où il faut se soucier des espaces et des parenthèses collées. Les deux parties utiliseront ce même découpage.

Écrire une fonction `decouper(ligne)` qui renvoie la liste des *symboles* de la ligne : les nombres (convertis en `int`), `’+’`, `’*’`, `’(’` et `’)’`. Par exemple `decouper("3 * (2 + 4)")` doit renvoyer `[3, ’*’, ’(’, 2, ’+’, 4, ’)’]`.

??? pouce "Coup de pouce"

    Parcourir la chaîne caractère par caractère, sans rien faire pour un espace, en accumulant les chiffres consécutifs dans une chaîne `nombre` : un nombre est terminé dès qu’on rencontre autre chose qu’un chiffre.

!!! encadre "Outil Python : strip (nettoyer une ligne lue)"

    Chaque ligne lue dans un fichier (avec `for ligne in fichier` ou `readlines()`) se termine par le caractère de fin de ligne `"\n"` (sauf parfois la dernière). `ligne.strip()` renvoie une copie de la ligne sans les espaces ni les fins de ligne placés au début et à la fin.

    ```python
    ligne = "1721\n"
    print(ligne.strip())                  # 1721
    print(len(ligne), len(ligne.strip())) # 5 4
    ```

    **Intérêt.** Comparer ou découper une ligne sans que la fin de ligne ne gêne : `"abc\n" == "abc"` vaut `False`.

### <span class="exo-num">Exercice 4</span> — Évaluer sans priorité <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-structures-lineaires-piles-files-listes-aoc-1-4 }

**But.** Calculer la valeur d’une liste de symboles avec la règle de la partie 1.

**À quoi ça sert ?** C’est le cœur du défi : appliquée à chaque ligne du fichier, cette fonction donne les valeurs dont la somme est la réponse. La vraie difficulté est de suspendre le calcul en cours à chaque parenthèse ouvrante, ce que permettent une pile ou un appel récursif.

Écrire une fonction `evaluer(symboles)` qui renvoie la valeur de l’expression avec la règle de la partie 1. Tester sur les trois lignes de l’exemple, puis calculer la somme sur `input.txt`.

??? pouce "Coup de pouce"

    Deux méthodes possibles. **Avec une pile** : quand on rencontre `’(’`, on empile le résultat partiel et l’opérateur en attente, puis on repart de zéro ; quand on rencontre `’)’`, on dépile et on combine. **Récursivement** : une fonction lit l’expression de gauche à droite et s’appelle elle-même dès qu’elle rencontre une parenthèse ouvrante ; elle renvoie la valeur *et* l’indice où elle s’est arrêtée.

??? pouce "Coup de pouce 2 (début de solution)"

    Version récursive : `evaluer_depuis(symboles, i)` garde une variable `total` et un opérateur courant `op` (au départ `’+’` et `total = 0`). Pour chaque symbole : un nombre, ou une sous-expression obtenue par appel récursif après `’(’`, est combiné à `total` avec `op` ; `’+’` ou `’*’` met à jour `op` ; `’)’` ou la fin de la liste arrête la boucle et l’on renvoie `(total, i)`.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    **Ce qui change.** Vous aviez mal compris : dans cette école, il existe bien une priorité entre les opérations, mais elle est à l’envers de la vôtre.

    **La nouvelle règle.**

    - Les parenthèses passent toujours en premier.

    - Ensuite, l’**addition est prioritaire** sur la multiplication : on effectue toutes les additions avant les multiplications.

    - À priorité égale, on calcule de gauche à droite.

    - Ainsi `2 * 3 + 4` vaut maintenant $2 \times 7 = 14$, alors qu’il valait 10 en partie 1.

    **La réponse attendue.** La somme des valeurs de toutes les lignes, calculées avec cette nouvelle règle.

### <span class="exo-num">Exercice 5</span> — Changer la priorité <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-structures-lineaires-piles-files-listes-aoc-1-5 }

**But.** Adapter l’évaluation pour que `+` soit calculé avant `*`.

**À quoi ça sert ?** Le découpage et le traitement des parenthèses restent valables ; il suffit de changer la façon de combiner les opérations. Une méthode bien choisie (gare de triage avec une table de priorités) résout même les deux parties avec le même code.

Seule la priorité entre `+` et `*` change. Adapter le programme. Sur l’exemple inventé de la fiche, on doit trouver les valeurs `33`, `50` et `135`, de somme `218`.

??? pouce "Coup de pouce"

    Avec la méthode récursive, il suffit de repérer qu’une expression devient un *produit de sommes* : une fonction calcule une somme (de nombres ou de parenthèses), une autre fait le produit de ces sommes.

??? pouce "Coup de pouce 2 (début de solution)"

    Algorithme de la gare de triage (Dijkstra) : une pile d’opérateurs et une pile de valeurs. On donne à chaque opérateur une priorité (un dictionnaire `{’+’: 2, ’*’: 1}`). Avant d’empiler un opérateur, on applique tous ceux du sommet de pile de priorité supérieure ou égale ; une `’)’` applique les opérateurs jusqu’à la `’(’` correspondante. Avec `{’+’: 1, ’*’: 1}`, le même code résout la partie 1.

## Approfondissement

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Approfondissement 1 : la descente récursive <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-structures-lineaires-piles-files-listes-aoc-1-6 }

**But.** Évaluer les expressions de la partie 2 avec trois fonctions qui s’appellent mutuellement.

**À quoi ça sert ?** Décrire la forme des expressions par des définitions récursives, puis écrire une fonction par définition, est la méthode utilisée par les interpréteurs de langages, Python compris ; elle traite naturellement les parenthèses et les priorités.

En partie 2, une expression est un **produit de sommes** : `2 + 3 * 4 + (1 * 6)` se lit $(2 + 3) \times (4 + (1 \times 6))$. On peut décrire toutes les expressions par trois définitions qui s’appellent mutuellement :

- un *produit* est une somme, éventuellement suivie de `* somme`, `* somme`…

- une *somme* est un facteur, éventuellement suivi de `+ facteur`, `+ facteur`…

- un *facteur* est un nombre, ou bien un produit entre parenthèses.

1.  À la main : découper la deuxième ligne de l’exemple en sommes, puis chaque somme en facteurs. Faire de même pour la troisième ligne. Où intervient la définition récursive du facteur ?

2.  Écrire trois fonctions `facteur(symboles, i)`, `somme(symboles, i)` et `produit(symboles, i)` qui lisent la liste à partir de l’indice `i` et renvoient le couple `(valeur, indice du premier symbole non lu)`. Vérifier qu’on retrouve `33`, `50` et `135`.

    ??? pouce "Coup de pouce"

        Chaque fonction suit sa définition : `somme` appelle `facteur`, puis, tant que le symbole courant est `’+’`, saute ce symbole et appelle à nouveau `facteur`. `produit` fait de même avec `somme` et `’*’`.

    ??? pouce "Coup de pouce 2 (début de solution)"

        `facteur` : si `symboles[i]` vaut `’(’`, appeler `produit(symboles, i + 1)`, qui renvoie `(v, j)` avec `symboles[j] == ’)’` ; renvoyer alors `(v, j + 1)`. Sinon renvoyer `(symboles[i], i + 1)`.

3.  Quelle est la complexité de cette méthode ? Comment l’adapter à la partie 1 (une seule priorité) ?

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 2 : la notation postfixe <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-structures-lineaires-piles-files-listes-aoc-1-7 }

**But.** Évaluer une expression écrite en notation postfixe, puis traduire une expression ordinaire dans cette notation.

**À quoi ça sert ?** Sans parenthèses ni priorités, l’évaluation n’utilise plus qu’une seule pile ; on sépare ainsi le problème en deux étapes simples (traduire, puis calculer), comme le font certaines calculatrices et machines virtuelles.

En **notation postfixe** (ou « polonaise inverse »), on écrit chaque opérateur *après* ses deux opérandes, et l’on n’a plus besoin de parenthèses : `(3 + 4) * 2` s’écrit `3 4 + 2 *`. Certaines calculatrices fonctionnent ainsi.

1.  Évaluer à la main `3 4 + 2 *` en utilisant une pile : on lit de gauche à droite ; un nombre est empilé ; un opérateur dépile deux valeurs et empile le résultat. Dessiner la pile après chaque symbole.

2.  Écrire `evaluer_postfixe(expression)` qui évalue une liste comme `[3, 4, ’+’, 2, ’*’]`.

    ??? pouce "Coup de pouce"

        Une seule pile (une liste avec `append` et `pop`) ; un symbole est un opérateur s’il vaut `’+’` ou `’*’`, sinon c’est un nombre. Attention à l’ordre : le premier élément dépilé est l’opérande de **droite**.

3.  L’algorithme de la gare de triage peut, au lieu de calculer, **écrire** l’expression en notation postfixe : un nombre va directement dans la liste de sortie, un opérateur dépilé y est ajouté au lieu d’être appliqué. Écrire `postfixe(symboles, priorite)`. Écrire à la main la notation postfixe de la deuxième ligne de l’exemple pour chacune des deux parties : qu’est-ce qui change ?

    ??? pouce "Coup de pouce"

        Reprendre le code de la gare de triage : là où l’on appliquait un opérateur dépilé, on l’ajoute à la fin de la liste `sortie`.

    ??? pouce "Coup de pouce 2 (début de solution)"

        Partie 1 : `2 3 + 4 * 1 6 * +`. Il reste à trouver celle de la partie 2 et à vérifier que `evaluer_postfixe(postfixe(...))` redonne bien `50`.

4.  Combien de piles au total pour calculer une expression de cette façon ? Quelle est la complexité ?

## <span class="etiquette">Défi 2</span> Crab Cups

*les gobelets du crabe — listes chaînées*

<p class="infos-activite">Jour 23</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/03-defi-aoc-2020-23){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-03-defi-aoc-2020-23.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/23 ](https://adventofcode.com/2020/day/23 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (lien ci-dessus) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - **Attention aux exemples.** L’énoncé en ligne a son propre exemple, avec d’autres réponses. Les valeurs de test de cette fiche portent sur **l’exemple inventé de la fiche** (exercice « À la main ») : l’enregistrer dans un fichier `exemple.txt` à côté du programme, et ouvrir `"exemple.txt"` au lieu de `"input.txt"` pour tester.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

!!! encadre "Le défi en bref"

    **Le problème.** Des gobelets numérotés sont disposés en cercle ; à chaque coup, trois gobelets sont déplacés selon une règle précise. On veut connaître l’ordre des gobelets après un grand nombre de coups. En partie 1 (9 gobelets, 100 coups), une simulation directe suffit ; en partie 2 (un million de gobelets, dix millions de coups), il faut une structure de données où chaque coup coûte un temps constant.

    **Ce qu’on réinvestit.** Les **listes chaînées** de ce chapitre : un cercle de gobelets est une liste chaînée circulaire, où chaque gobelet connaît seulement celui qui le suit. Déplacer trois gobelets revient alors à changer quelques liens, sans décaler les autres. On verra qu’un simple tableau suffit à représenter cette liste chaînée, et l’on comparera les **complexités** des deux méthodes.

    **La démarche de la fiche.**

    1.  Comprendre la règle d’un coup (en particulier le choix de la destination) et jouer quelques coups à la main.

    2.  Simuler le jeu avec une liste Python : cela suffit pour la partie 1.

    3.  Évaluer le coût de cette méthode et constater qu’elle est bien trop lente pour la partie 2.

    4.  Réécrire la simulation avec un tableau des successeurs (une liste chaînée), puis mesurer le gain.

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| cup | gobelet | label | étiquette, numéro |
| clockwise | dans le sens des aiguilles d’une montre | circle | cercle |
| current cup | gobelet courant | pick up | ramasser, retirer |
| destination cup | gobelet de destination | move | coup |
| wrap around | repartir de l’autre bout | immediately | juste (après) |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Le crabe vous défie maintenant à un jeu de bonneteau : il déplace des gobelets numérotés disposés en cercle, et vous devez prédire où ils seront à la fin. Comme ses déplacements suivent une règle fixe, on peut les simuler.

    **Les données.** Le fichier est une simple suite de 9 chiffres, de 1 à 9, chacun une fois : les étiquettes des gobelets dans l’ordre du cercle, dans le sens horaire. Après le dernier chiffre, on revient au premier. Le premier gobelet de la suite est le gobelet « courant » au début du jeu.

    **La règle.** Un coup se déroule ainsi :

    - Retirer du cercle les 3 gobelets qui suivent le gobelet courant (dans le sens horaire).

    - Choisir la destination : c’est l’étiquette du courant moins 1 ; si cette étiquette fait partie des gobelets retirés, on enlève encore 1, et ainsi de suite. Si l’on passe sous la plus petite étiquette, on repart de la plus grande.

    - Replacer les 3 gobelets retirés, dans le même ordre, juste après la destination.

    - Le nouveau gobelet courant est celui qui suit alors l’ancien courant.

    Autrement dit, le crabe déplace un paquet de trois gobelets vers le plus grand numéro inférieur disponible.

    **La réponse attendue.** Après 100 coups, les étiquettes lues dans le sens horaire à partir du gobelet 1, sans lui, écrites en une seule chaîne. Par exemple, si le cercle lu à partir du 1 était alors 1, 4, 7, 2, 9, 3, 5, 8, 6, la réponse serait `47293586`.

### <span class="exo-num">Exercice 1</span> — Vérifier sa compréhension <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-structures-lineaires-piles-files-listes-aoc-2-1 }

**But.** Maîtriser le choix de la destination et l’ordre des étapes d’un coup.

**À quoi ça sert ?** Le choix de la destination, avec ses sauts et son retour à la plus grande étiquette, est la partie de la règle la plus souvent mal programmée ; ces questions en traitent les cas limites.

1.  Avec 9 gobelets, le courant porte 2 et les gobelets retirés sont 1, 9 et 8 : quelle est la destination ?

2.  Le gobelet courant peut-il être la destination ? Un gobelet retiré ?

3.  Le nouveau courant se choisit-il avant ou après avoir replacé les trois gobelets ? Cela change-t-il quelque chose ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-structures-lineaires-piles-files-listes-aoc-2-2 }

**But.** Jouer trois coups à la main sur un cercle de 9 gobelets.

**À quoi ça sert ?** On vérifie qu’on applique correctement la règle, et l’état connu après le premier coup servira à tester la fonction `jouer` coup par coup.

On part de l’étiquetage (inventé) `527164839`. Jouer le premier coup à la main. Vérification : en lisant le cercle à partir du `5`, on obtient `5 6 4 2 7 1 8 3 9`. Quel est le nouveau gobelet courant ? Jouer encore deux coups.

## Programmer la partie 1

!!! encadre "Outil Python : strip (nettoyer une ligne lue)"

    Chaque ligne lue dans un fichier (avec `for ligne in fichier` ou `readlines()`) se termine par le caractère de fin de ligne `"\n"` (sauf parfois la dernière). `ligne.strip()` renvoie une copie de la ligne sans les espaces ni les fins de ligne placés au début et à la fin.

    ```python
    ligne = "1721\n"
    print(ligne.strip())                  # 1721
    print(len(ligne), len(ligne.strip())) # 5 4
    ```

    **Intérêt.** Comparer ou découper une ligne sans que la fin de ligne ne gêne : `"abc\n" == "abc"` vaut `False`.

!!! encadre "Méthode : chercher un élément dans une liste"

    Pour trouver la position d’un gobelet, on parcourt la liste avec un indice jusqu’à le rencontrer. Une boucle `while` s’arrête dès qu’il est trouvé, sans `break`.

    ```python
    def indice(liste, x):
        """Indice de la premiere occurrence de x, ou -1 si x est absent."""
        i = 0
        while i < len(liste) and liste[i] != x:
            i += 1
        if i == len(liste):
            return -1
        return i

    g = [5, 6, 4, 2, 7, 1, 8, 3, 9]
    print(indice(g, 1))        # 5
    k = indice(g, 4)
    g = g[:k + 1] + [0] + g[k + 1:]    # insertion juste apres le 4
    print(g)                   # [5, 6, 4, 0, 2, 7, 1, 8, 3, 9]
    ```

    La plus grande étiquette, elle, n’a pas besoin d’être cherchée : les étiquettes sont exactement les entiers de $1$ à $n$, elle vaut donc `len(g)`.

    **Intérêt et limite.** La recherche parcourt la liste : elle coûte jusqu’à $n$ comparaisons. Question : que renvoie `indice(g, 10)` ? Pourquoi faut-il écrire le test `i < len(liste)` *avant* le test `liste[i] != x` ?

### <span class="exo-num">Exercice 3</span> — Une première simulation avec une liste <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-structures-lineaires-piles-files-listes-aoc-2-3 }

**But.** Simuler le jeu avec une liste Python et écrire la réponse sous forme de chaîne.

**À quoi ça sert ?** C’est la réponse de la partie 1. Cette version simple servira ensuite de référence pour vérifier la version rapide de la partie 2.

Écrire une fonction `jouer(gobelets, nb_coups)` qui simule le jeu sur une liste Python d’entiers et renvoie la liste des gobelets après `nb_coups` coups, puis une fonction `reponse(gobelets)` qui renvoie la chaîne des étiquettes lues après le gobelet 1. Sur l’exemple inventé de la fiche, on doit obtenir `53269478` après 10 coups et `98357642` après 100 coups.

??? pouce "Coup de pouce"

    Le plus simple est de garder le gobelet courant toujours en tête de liste : après chaque coup, faire « tourner » la liste d’un cran (le premier élément passe à la fin). Les trois gobelets ramassés sont alors aux indices 1, 2 et 3.

### <span class="exo-num">Exercice 4</span> — Combien ça coûte ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-structures-lineaires-piles-files-listes-aoc-2-4 }

**But.** Estimer la complexité d’un coup avec une liste Python, puis le temps nécessaire pour la partie 2.

**À quoi ça sert ?** Avant d’écrire du code, on prévoit si la méthode est utilisable : ce calcul montre qu’il faut changer de structure de données, et indique quelles opérations il faut rendre plus rapides.

Quelle est la complexité d’un coup avec cette méthode, en fonction du nombre $n$ de gobelets ? Lire la partie 2 (une fois débloquée) : combien d’opérations élémentaires faudrait-il environ ?

??? pouce "Coup de pouce"

    Chercher le gobelet de destination (parcours de la liste), retirer et insérer des éléments dans une liste Python : chacune de ces opérations est en $O(n)$.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    **Ce qui change.** Le crabe sort beaucoup plus de gobelets et joue beaucoup plus longtemps : un million de gobelets et dix millions de coups.

    **La nouvelle règle.**

    - Après vos 9 chiffres, le cercle est complété par les étiquettes $10, 11, \dots$ jusqu’à $1\,000\,000$, dans l’ordre ; après le gobelet $1\,000\,000$, on revient au premier de vos chiffres.

    - Le gobelet courant de départ est toujours le premier de vos chiffres.

    - On joue $10\,000\,000$ coups avec exactement les mêmes règles (la plus grande étiquette vaut maintenant $1\,000\,000$).

    **La réponse attendue.** Le produit des deux étiquettes qui suivent le gobelet 1. Par exemple, si ces deux gobelets portaient les étiquettes 12 et 1000, la réponse serait 12000.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 5</span> — Une liste chaînée dans un tableau <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-structures-lineaires-piles-files-listes-aoc-2-5 }

**But.** Représenter le cercle par le tableau des successeurs, où chaque coup ne modifie que trois cases.

**À quoi ça sert ?** Un coup devient une opération en temps constant : dix millions de coups deviennent faisables en quelques secondes, ce qui donne la réponse de la partie 2. Vérifier d’abord les résultats de la partie 1 garantit que la nouvelle version applique bien la même règle.

Réécrire la simulation avec un **tableau des successeurs** (lire l’encadré), vérifier qu’elle redonne les résultats de la partie 1, puis répondre à la partie 2. Sur l’exemple inventé de la fiche, on doit trouver `28997820592`. Le calcul peut prendre une dizaine de secondes.

??? pouce "Coup de pouce"

    Un coup ne modifie que **trois** cases du tableau `suivant`. Les écrire sur un dessin avant de coder : le successeur du courant, celui du dernier gobelet ramassé, celui de la destination.

??? pouce "Coup de pouce 2 (début de solution)"

    Avec `a = suivant[courant]`, `b = suivant[a]`, `c = suivant[b]` : le courant doit maintenant pointer vers `suivant[c]` ; `c` doit pointer vers l’ancien successeur de la destination ; la destination doit pointer vers `a`. Attention à l’ordre des affectations.

!!! encadre "Le tableau des successeurs"

    Une **liste chaînée** n’a pas besoin d’objets `Cellule` (la classe du cours) : comme les étiquettes sont les entiers de $1$ à $n$, on peut ranger dans une liste `suivant` de taille $n + 1$ l’étiquette qui suit chaque gobelet dans le cercle : `suivant[x]` est le gobelet juste après `x` (la case `0` ne sert pas). Pour le cercle `3 1 2` : `suivant[3] = 1`, `suivant[1] = 2` et `suivant[2] = 3` (le dernier pointe vers le premier : la liste est *circulaire*).

    **Avantages.** Trouver le gobelet d’étiquette `x` ne demande aucune recherche : c’est la case `x`. Retirer ou insérer un morceau de la chaîne revient à modifier quelques cases, sans décaler les autres éléments. Un coup se fait donc en temps constant, $O(1)$, quel que soit $n$.

    **Pour lire le cercle** à partir du gobelet `1`, on suit les flèches : `x = suivant[1]`, puis `x = suivant[x]`, jusqu’à revenir à `1`.

!!! encadre "Outil Python : mesurer un temps (time.perf_counter)"

    `perf_counter()` renvoie un temps en secondes, très précis ; la différence entre deux appels donne une durée. On s’en sert ici uniquement pour **comparer** des programmes et vérifier une complexité.

    ```python
    from time import perf_counter
    debut = perf_counter()
    total = 0
    for k in range(1_000_000):
        total += k
    print(f"{perf_counter() - debut:.3f} s")   # duree de la boucle
    ```

    Question : mesurer la durée de la boucle ci-dessus avec $10^6$ puis $10^7$ tours. Le temps est-il proportionnel au nombre de tours ?

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 6</span> — Défi : aller plus vite <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-structures-lineaires-piles-files-listes-aoc-2-6 }

**But.** Mesurer les temps des deux versions et les comparer aux complexités prévues.

**À quoi ça sert ?** Confronter une prédiction théorique à des mesures est la seule façon de savoir si une analyse de complexité est juste ; on apprend aussi quelques réglages qui accélèrent une boucle très longue.

Avec `perf_counter`, comparer les deux versions (liste et tableau des successeurs) : jouer $100$ coups avec $10^4$, puis $10^5$ gobelets étiquetés dans l’ordre. Les mesures confirment-elles les complexités trouvées plus haut ? Peut-on ensuite réduire le temps de la version chaînée en évitant de recalculer des valeurs dans la boucle ?

??? pouce "Coup de pouce"

    Dans une boucle de dix millions de tours, chaque accès à une variable globale ou chaque appel de fonction compte : placer toute la boucle dans une fonction et utiliser des variables locales.
