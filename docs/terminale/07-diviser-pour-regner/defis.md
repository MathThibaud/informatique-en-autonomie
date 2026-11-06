# Défis Advent of Code

<p class="sous-titre">Diviser pour régner</p>

## <span class="etiquette">Défi 1</span> Report Repair

*la note de frais — parcours de listes et complexité*

<p class="infos-activite">Jour 1</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/07-defi-aoc-2020-01){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-07-defi-aoc-2020-01.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/1 ](https://adventofcode.com/2020/day/1 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (lien ci-dessus) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

!!! encadre "Le défi en bref"

    **Le problème.** Une note de frais contient environ deux cents dépenses ; parmi elles, deux (puis trois) ont pour somme 2020, et il faut les retrouver. Essayer toutes les paires à la main est hors de portée : il y en a près de vingt mille. Un programme les essaie toutes sans peine, mais la vraie question du défi est ailleurs : **combien d’opérations** faut-il, et peut-on faire mieux ?

    **Ce qu’on réinvestit.** La **complexité** et la comparaison de plusieurs méthodes, comme dans ce chapitre. La méthode directe (deux boucles imbriquées) coûte $O(n^2)$ ; un ensemble permet de n’en garder qu’une ; enfin, trier la liste puis la parcourir par les deux bouts donne une troisième méthode. Ce tri coûte $O(n\log n)$ grâce à un algorithme « diviser pour régner » comme le tri fusion du cours : c’est lui qui rend la troisième méthode intéressante.

    **La démarche de la fiche.**

    1.  Lever les ambiguïtés de l’énoncé, puis trouver la paire à la main sur un petit exemple.

    2.  Lire le fichier dans une liste d’entiers.

    3.  Écrire la solution directe par double boucle, puis évaluer son coût.

    4.  Partie 2 : passer des paires aux triplets en ajoutant une boucle.

    5.  En approfondissement, obtenir les mêmes réponses plus vite, avec un ensemble puis avec un tri.

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| expense report | note de frais | entry | ligne, valeur du fichier |
| accounting | comptabilité | sum to | avoir pour somme |
| fix up | corriger | multiply | multiplier |
| puzzle input | vos données (fichier personnel) | star | étoile (une par partie réussie) |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Avant de partir en vacances, vous devez régler un dernier problème : les elfes de la comptabilité ont une note de frais qui ne tombe pas juste et vous demandent de les aider à la corriger. Il faut retrouver dans cette note les dépenses qui posent problème.

    **Les données.** Le fichier est la note de frais. Chaque ligne contient **un seul entier positif** : le montant d’une dépense. Il y a environ deux cents lignes ; leur ordre ne joue aucun rôle.

    **La règle.**

    - Parmi toutes les dépenses, exactement **deux** lignes ont des valeurs dont la somme vaut **2020**. Autrement dit, il faut trouver la seule paire de lignes qui « complètent » 2020.

    - Les deux lignes doivent être **différentes** : une valeur présente une seule fois dans le fichier ne peut pas être associée à elle-même.

    - Il n’y a qu’une seule paire qui convient : dès qu’on l’a trouvée, on peut s’arrêter.

    **La réponse attendue.** Le **produit** des deux valeurs trouvées (et non leur somme, qui vaut toujours 2020). Par exemple, pour les dépenses 1000, 300, 1020, 45, la paire est formée de 1000 et 1020 : la réponse serait 1020000.

### <span class="exo-num">Exercice 1</span> — Vérifier sa compréhension <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-diviser-pour-regner-aoc-1-1 }

**But.** Lever deux ambiguïtés de l’énoncé avant de programmer.

**À quoi ça sert ?** La première question fixe une contrainte du programme (ne jamais associer une ligne à elle-même) ; la seconde dit qu’on a le droit de réordonner la liste, par exemple de la trier, sans changer la réponse : l’approfondissement 2 s’en servira.

1.  Si le fichier contient une seule fois la valeur `1010`, peut-elle former la paire avec elle-même ?

2.  L’ordre des lignes dans le fichier a-t-il une importance pour la réponse ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-diviser-pour-regner-aoc-1-2 }

**But.** Trouver la paire à la main sur six nombres.

**À quoi ça sert ?** On dispose ainsi d’un exemple dont on **connaît la réponse** (`980896`) : chaque fonction écrite ensuite sera d’abord testée dessus, avant d’être lancée sur les vraies données.

On considère le fichier (inventé) suivant :

```console
1010
812
1500
1208
33
487
```

Trouver à la main la réponse attendue. Vérification : on doit obtenir `980896`. Pourquoi la ligne `1010` ne donne-t-elle pas de solution à elle seule ?

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Lire le fichier <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-diviser-pour-regner-aoc-1-3 }

**But.** Transformer le fichier texte en une liste Python d’entiers, `nombres`.

**À quoi ça sert ?** Toutes les méthodes du défi travaillent sur cette liste. Les lignes lues sont des chaînes : sans conversion en entiers, la somme `"1010" + "1010"` donnerait `"10101010"` et non 2020. Afficher la longueur vérifie qu’aucune ligne n’a été perdue.

Écrire les lignes qui lisent `input.txt` et construisent la liste `nombres` des entiers qu’il contient. Afficher sa longueur pour vérifier.

!!! encadre "Outil Python : strip (nettoyer une ligne lue)"

    Chaque ligne renvoyée par `readlines()` se termine par le caractère de fin de ligne `"\n"` (sauf parfois la dernière). `ligne.strip()` renvoie une copie de la ligne sans les espaces ni les fins de ligne placés au début et à la fin.

    ```python
    ligne = "1721\n"
    print(ligne.strip())                  # 1721
    print(len(ligne), len(ligne.strip())) # 5 4
    ```

    **Intérêt.** Comparer ou découper une ligne sans que la fin de ligne ne gêne : `"abc\n" == "abc"` vaut `False`.

### <span class="exo-num">Exercice 4</span> — Une première solution <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-diviser-pour-regner-aoc-1-4 }

**But.** Écrire la méthode la plus directe : essayer toutes les paires de lignes.

**À quoi ça sert ?** Elle donne la réponse de la partie 1. Elle sert aussi de **référence** : juste mais lente, elle permettra de vérifier les méthodes plus rapides des approfondissements.

Écrire une fonction `paire_2020(nombres)` qui renvoie le produit des deux valeurs recherchées. Tester sur l’exemple du défi, puis sur vos données.

??? pouce "Coup de pouce"

    Deux boucles imbriquées sur les **indices** `i` et `j`, avec `j > i` pour ne jamais prendre deux fois la même ligne.

### <span class="exo-num">Exercice 5</span> — Combien d’opérations ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-diviser-pour-regner-aoc-1-5 }

**But.** Évaluer le coût de la double boucle en fonction du nombre $n$ de dépenses.

**À quoi ça sert ?** C’est cette estimation qui dit si la méthode reste utilisable quand $n$ grandit, et qui servira de point de comparaison pour les autres méthodes du défi.

Le fichier contient environ $200$ nombres. Combien de paires la fonction précédente examine-t-elle au pire ? Quelle est sa complexité en fonction de $n$ ?

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    **Ce qui change.** Les elfes sont ravis, mais il leur reste une ancienne note de frais à vérifier selon une autre règle. Le fichier est le même ; seul le nombre de dépenses à associer change.

    **La nouvelle règle.**

    - Il faut cette fois trouver les **trois** lignes différentes dont les valeurs ont pour somme 2020.

    - Comme dans la partie 1, une ligne ne peut servir qu’une fois, et il n’y a qu’un seul triplet qui convient.

    **La réponse attendue.** Le produit de ces trois valeurs. Par exemple, pour les dépenses 1000, 700, 320, 55, le triplet est formé de 1000, 700 et 320 : la réponse serait 224000000.

### <span class="exo-num">Exercice 6</span> — La partie 2 <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-diviser-pour-regner-aoc-1-6 }

**But.** Passer des paires aux triplets en ajoutant une boucle à la solution de la partie 1.

**À quoi ça sert ?** On obtient la réponse de la partie 2 et l’on voit le prix à payer : chaque boucle imbriquée de plus multiplie le coût par $n$, ce qui motive la recherche de méthodes plus économes.

Adapter le programme pour répondre à la nouvelle question. Sur l’exemple du défi, on doit trouver `24106500`.

??? pouce "Coup de pouce"

    Une boucle de plus. Combien de triplets pour $n = 200$ ? C’est encore rapide.

## Approfondissement

!!! encadre "Outil Python : les ensembles (set) — rappel"

    Tout est présenté dans l’encadré « Outil Python : les ensembles » du défi *Crab Combat* (chapitre 4). On n’utilise ici que `set()` (ensemble vide), `add`, `remove` et le test `x in ensemble`, en temps constant (en moyenne). Les éléments doivent être non modifiables (nombres, chaînes, tuples).

    **À essayer.** Avec `vus = {812, 1208}`, que valent `812 in vus` et `2020 - 812 in vus` ? Sur un million d’éléments, la différence de temps avec une liste est énorme.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 1 : une seule boucle grâce à un ensemble <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-diviser-pour-regner-aoc-1-7 }

**But.** Remplacer la boucle intérieure par un test d’appartenance à un ensemble.

**À quoi ça sert ?** Le test `x in ensemble` se fait en temps constant (en moyenne) : la partie 1 passe de $O(n^2)$ à $O(n)$, la partie 2 de $O(n^3)$ à $O(n^2)$. Le choix de la structure de données compte souvent plus que la vitesse de la machine.

1.  Recopier puis exécuter le code de l’encadré du défi *Crab Combat* (chapitre 4). Que se passe-t-il si l’on ajoute deux fois `1208` à un ensemble ?

2.  Écrire `paire_rapide(nombres)` qui résout la partie 1 avec une **seule** boucle et un ensemble `vus`. Quelle est sa complexité ?

    ??? pouce "Coup de pouce"

        Pour chaque nombre `x`, la seule valeur qui le complète est `2020 - x`. Il suffit de savoir si on l’a déjà rencontrée.

    ??? pouce "Coup de pouce 2 (début de solution)"

        On parcourt les nombres un par un ; **avant** d’ajouter `x` à l’ensemble `vus`, on regarde si `2020 - x` y est déjà. Tester avant d’ajouter évite d’utiliser deux fois la même ligne.

3.  En déduire une solution de la partie 2 en $O(n^2)$ au lieu de $O(n^3)$.

    ??? pouce "Coup de pouce"

        Généraliser la fonction avec un paramètre `cible` : pour chaque `x`, chercher une paire de somme `2020 - x` parmi les nombres **suivants**.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — Approfondissement 2 : trier puis rapprocher deux indices <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-diviser-pour-regner-aoc-1-8 }

**But.** Résoudre le même problème sans ensemble, en triant la liste puis en rapprochant deux indices.

**À quoi ça sert ?** Une fois la liste triée, chaque comparaison permet d’écarter définitivement un élément. On dispose alors de trois méthodes pour la même réponse, et l’on peut comparer leurs coûts : c’est l’objet du défi.

Une autre idée, sans ensemble, réinvestit le **tri** : avec le tri fusion de ce chapitre, il coûte $O(n\log n)$. On trie la liste, puis on place un indice `g` au début et un indice `d` à la fin.

1.  Sur la liste triée `[33, 487, 812, 1010, 1208, 1500]`, on a `g = 0` et `d = 5` : la somme vaut $33 + 1500 = 1533$, trop petite. Faut-il avancer `g` ou reculer `d` ? Justifier, puis dérouler la méthode à la main jusqu’à trouver la paire.

2.  Écrire `paire_triee(nombres, cible)` qui applique cette méthode (on travaille sur une copie triée, obtenue avec **votre** fonction `tri_fusion` du cours, qui renvoie une nouvelle liste) et renvoie le produit, ou `None` s’il n’y a pas de paire.

    ??? pouce "Coup de pouce"

        Tant que `g < d` : si la somme est trop petite, la seule façon de l’augmenter est d’avancer `g` ; si elle est trop grande, reculer `d`.

    ??? pouce "Coup de pouce 2 (début de solution)"

        Si `t[g] + t[d] < cible`, alors `t[g]` associé à n’importe quel élément situé avant `d` donne aussi une somme trop petite : `t[g]` ne peut faire partie d’aucune paire, on peut l’écarter.

3.  Quelle est la complexité totale (tri compris) ? Comparer avec les deux méthodes précédentes.

4.  Utiliser `paire_triee` pour résoudre la partie 2 en $O(n^2)$, sans ensemble.

## <span class="etiquette">Défi 2</span> Encoding Error

*la faille du chiffrement — fenêtre glissante et complexité*

<p class="infos-activite">Jour 9</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/07-defi-aoc-2020-09){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-07-defi-aoc-2020-09.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/9 ](https://adventofcode.com/2020/day/9 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (lien ci-dessus) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

!!! encadre "Le défi en bref"

    **Le problème.** Un fichier contient un millier de nombres, dont chacun devrait pouvoir s’écrire comme la somme de deux nombres parmi les 25 qui le précèdent. Il faut repérer le premier nombre qui viole cette règle, puis retrouver une suite de nombres consécutifs dont la somme vaut ce nombre fautif. À la main, tester des milliers de paires et de tranches est impossible ; un programme le fait en quelques instants, à condition d’être bien conçu.

    **Ce qu’on réinvestit.** Ce défi prolonge le défi précédent (*Report Repair*, recherche d’une paire de somme donnée) et surtout l’analyse de **complexité** de ce chapitre. La première solution qui vient à l’esprit essaie toutes les tranches : elle est quadratique. Comme le tri fusion détrône les tris quadratiques, une meilleure idée — deux indices qui ne font qu’avancer, une *fenêtre glissante* — permet un parcours linéaire. Cette fenêtre glissante reviendra au chapitre 12, avec la recherche naïve d’un motif dans un texte.

    **La démarche de la fiche.**

    1.  Vérifier sa compréhension de la règle, puis l’appliquer à la main sur un petit exemple dont on connaît la réponse.

    2.  Écrire une fonction qui teste si une cible est la somme de deux éléments d’une fenêtre, puis faire glisser cette fenêtre : réponse de la partie 1.

    3.  Pour la partie 2, écrire une première solution qui essaie toutes les tranches, puis une solution linéaire à deux indices.

    4.  En approfondissement, mesurer les durées pour confirmer les complexités, et accélérer la partie 1 avec un ensemble.

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|                |                           |                 |                   |
|:---------------|:--------------------------|:----------------|:------------------|
| preamble       | préambule                 | previous        | précédent         |
| sum of any two | somme de deux quelconques | different       | différent         |
| weakness       | faiblesse, faille         | valid / invalid | valide / invalide |
| contiguous set | suite contiguë            | at least two    | au moins deux     |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Le héros branche son ordinateur sur une prise de données de l’avion. Il en sort une longue suite de nombres, chiffrée avec un vieux procédé qui comporte une faille. Dans ce procédé, chaque nombre doit pouvoir s’obtenir à partir des nombres reçus juste avant lui : un nombre qui ne le peut pas trahit l’erreur, et c’est lui qu’on cherche.

    **Les données.** Le fichier contient **un entier positif par ligne**, dans l’ordre de réception. Seule la position compte : le nombre de la ligne 30 est testé à l’aide des nombres des lignes qui le précèdent immédiatement.

    **La règle.**

    - Les 25 premiers nombres forment le *préambule* (le petit exemple de l’énoncé en utilise 5). Ils ne sont pas testés : ils servent seulement de point de départ.

    - Chaque nombre suivant doit être la somme de deux nombres de **valeurs différentes** pris parmi les 25 nombres qui le précèdent immédiatement. Deux nombres égaux ne forment donc pas une paire valable.

    - On regarde ainsi une *fenêtre* de 25 nombres qui glisse d’un cran à chaque nouveau nombre : le plus ancien en sort, le nombre qu’on vient de tester y entre. Un nombre sorti de la fenêtre ne peut plus servir.

    - Le premier nombre pour lequel aucune paire ne convient est le nombre fautif.

    **La réponse attendue.** Ce premier nombre qui ne respecte pas la règle. Par exemple, avec un préambule de 3 et la suite 2, 5, 4, 7, 9, 30 : 7 vaut $2 + 5$, 9 vaut $5 + 4$, mais 30 ne s’obtient pas avec 4, 7 et 9 : la réponse serait 30.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-diviser-pour-regner-aoc-2-1 }

**But.** Vérifier sur trois cas simples qu’on a bien compris la règle : valeurs différentes, contenu exact de la fenêtre.

**À quoi ça sert ?** Ces trois questions correspondent aux trois erreurs les plus fréquentes du programme : accepter deux valeurs égales, décaler la fenêtre d’un cran, utiliser un nombre déjà sorti.

À traiter sur le cahier :

1.  La fenêtre contient `3 7 10 7 2`. Le nombre suivant `14` est-il valide ?

2.  Avec un préambule de longueur $p$, quels indices forment la fenêtre du nombre d’indice $i$ ?

3.  La paire peut-elle utiliser un nombre sorti de la fenêtre ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-diviser-pour-regner-aoc-2-2 }

**But.** Faire glisser à la main une fenêtre de 5 nombres sur une liste de quinze nombres.

**À quoi ça sert ?** On obtient un exemple dont on **connaît la réponse** (22) : le programme devra la retrouver avant d’être lancé sur les vraies données. Écrire les fenêtres successives aide aussi à trouver les bonnes bornes de la tranche.

On considère la liste (inventée) suivante, avec un préambule de longueur $5$ :

```console
6  3  7  11  1  13  24  8  25  33  37  62  70  58  22
```

Vérifier à la main les nombres situés après le préambule, en écrivant à chaque fois la fenêtre des 5 nombres précédents et une paire qui convient. Vérification : le premier nombre invalide est `22`.

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Somme de deux <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-diviser-pour-regner-aoc-2-3 }

**But.** Écrire la fonction qui dit si une cible est la somme de deux éléments distincts d’une fenêtre.

**À quoi ça sert ?** C’est la brique de base de la partie 1 : la fonction suivante l’appellera une fois pour chaque nombre à tester. Les `assert` garantissent qu’elle est juste avant de s’en servir.

Écrire une fonction `somme_de_deux(fenetre, cible)` qui renvoie `True` si deux éléments de la liste `fenetre` ont pour somme `cible`, en respectant la règle des valeurs différentes. L’essayer avec des `assert` sur des cas simples.

??? pouce "Coup de pouce"

    Deux boucles sur les indices, avec `j > i`, comme pour le jour 1, et un test sur les valeurs des deux éléments.

### <span class="exo-num">Exercice 4</span> — La fenêtre glissante <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-diviser-pour-regner-aoc-2-4 }

**But.** Faire glisser la fenêtre sur toute la liste et renvoyer le premier nombre invalide.

**À quoi ça sert ?** Cette fonction donne directement la réponse de la partie 1. Le nombre trouvé sert ensuite de cible pour toute la partie 2 ; le paramètre `p` permet de tester sur l’exemple ($p = 5$) avant les vraies données ($p = 25$).

Écrire une fonction `premier_invalide(nombres, p)` où `p` est la longueur du préambule. Tester avec `p = 5` sur l’exemple du défi, puis avec la bonne longueur sur vos données.

??? pouce "Coup de pouce"

    Pour le nombre d’indice `i`, la fenêtre est la tranche `nombres[i - p:i]`. Faire un petit dessin pour vérifier les bornes.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    **Ce qui change.** Pour exploiter la faille, on se sert du nombre fautif trouvé en partie 1 : on ne cherche plus une paire, mais une **suite contiguë** de nombres du fichier, c’est-à-dire des nombres qui se suivent sans trou.

    **La nouvelle règle.**

    - Trouver une suite d’**au moins deux** nombres consécutifs du fichier dont la somme vaut exactement le nombre fautif. Le nombre fautif seul ne compte donc pas comme une suite.

    - Dans cette suite, repérer le plus petit et le plus grand nombre. Attention : ce ne sont pas forcément le premier et le dernier de la suite.

    **La réponse attendue.** La somme du plus petit et du plus grand nombre de cette suite. Par exemple, si le nombre fautif était 18 et que le fichier contenait 2, 5, 4, 7 à la suite, la suite serait 2, 5, 4, 7 et la réponse $2 + 7 = 9$.

### <span class="exo-num">Exercice 5</span> — Une première solution <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-diviser-pour-regner-aoc-2-5 }

**But.** Trouver la suite contiguë en essayant toutes les positions de début et de fin possibles.

**À quoi ça sert ?** Cette méthode simple donne une première réponse juste à la partie 2. Elle servira aussi de référence pour vérifier, et chronométrer, la méthode plus rapide de l’exercice suivant.

Écrire une fonction qui cherche la suite demandée en essayant toutes les positions de début et de fin. Sur l’exemple du défi, on doit trouver `12`.

??? pouce "Coup de pouce"

    Une suite contiguë, c’est une tranche `nombres[debut:fin]`. Attention : la suite réduite au seul nombre invalide ne compte pas. Le plus petit et le plus grand nombre de la tranche se trouvent avec une boucle, comme une recherche de maximum.

### <span class="exo-num">Exercice 6</span> — Deux indices <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-diviser-pour-regner-aoc-2-6 }

**But.** Remplacer la double boucle par deux indices qui ne reculent jamais, en justifiant que c’est correct.

**À quoi ça sert ?** On passe d’une méthode quadratique à une méthode linéaire : c’est exactement le gain de complexité étudié dans ce chapitre. La justification (les nombres sont positifs) est aussi importante que le code.

Les nombres de vos données sont tous positifs. Expliquer pourquoi on peut alors trouver la suite avec seulement deux indices `debut` et `fin` qui ne font qu’avancer, en tenant à jour la somme de la tranche. Programmer cette méthode et comparer sa complexité à celle de l’exercice précédent.

??? pouce "Coup de pouce"

    Si la somme courante est trop petite, on ajoute le nombre suivant (`fin` avance) ; si elle est trop grande, on retire le premier (`debut` avance).

??? pouce "Coup de pouce 2 (début de solution)"

    Chaque indice avance au plus $n$ fois : la méthode est linéaire. La boucle `while` s’arrête quand la somme est atteinte avec au moins deux nombres.

## Approfondissement

!!! encadre "Outil Python : mesurer une durée (time) et tirer au hasard (random)"

    Le module `time` fournit un chronomètre précis ; le module `random` tire des nombres au hasard, utile pour fabriquer de grosses données de test.

    ```python
    import random
    import time

    def somme_entiers(n):
        """Somme des entiers de 0 a n - 1, calculee par une boucle."""
        total = 0
        for k in range(n):
            total += k
        return total

    x = random.randint(1, 6)         # entier au hasard entre 1 et 6 (bornes comprises)
    liste = [random.randint(1, 1000) for _ in range(5)]
    depart = time.perf_counter()     # top depart (en secondes)
    total = somme_entiers(10**6)
    duree = time.perf_counter() - depart
    print(f"{duree:.4f} s")          # 4 chiffres apres la virgule
    ```

    **Intérêt.** Vérifier expérimentalement une complexité : si l’on double $n$, une méthode linéaire prend environ deux fois plus de temps, une méthode quadratique environ quatre fois plus. Une mesure isolée varie : la répéter.

    **À essayer.** Mesurer `somme_entiers(10**6)` puis `somme_entiers(2 * 10**6)` : le rapport des durées est-il proche de 2 ?

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 7</span> — Défi : mesurer <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-diviser-pour-regner-aoc-2-7 }

**But.** Chronométrer les deux méthodes de la partie 2 sur des données de plus en plus grosses.

**À quoi ça sert ?** Une complexité annoncée se vérifie par l’expérience : si l’écart entre les deux méthodes grandit avec la taille des données, l’analyse théorique est confirmée.

Mesurer avec le module `time` la durée des deux méthodes de la partie 2 sur vos données, puis sur une liste aléatoire de $10\,000$ nombres. Les mesures sont-elles cohérentes avec les complexités annoncées ?

??? pouce "Coup de pouce"

    `time.perf_counter()` avant et après l’appel ; la différence donne la durée en secondes.

!!! encadre "Outil Python : les ensembles (set) — rappel"

    Tout est présenté dans l’encadré « Outil Python : les ensembles » du défi *Crab Combat* (chapitre 4) : ensemble vide `set()`, ajout avec `add`, retrait avec `remove`, test `x in ensemble` en temps constant, éléments non modifiables (tuples). Un ensemble ne contient jamais deux fois le même élément.

    **À essayer.** Avec `fenetre = [3, 7, 10, 7, 2]`, que vaut `set(fenetre)` ? Combien d’éléments ?

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — Approfondissement 1 : la partie 1 avec un ensemble <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-07-diviser-pour-regner-aoc-2-8 }

**But.** Tester une paire de somme donnée avec une seule boucle, grâce à un ensemble.

**À quoi ça sert ?** La partie 1 passe de $p^2$ à $p$ tests par nombre. L’idée — chercher directement le complément `cible - x` au lieu d’essayer toutes les paires — resservira chaque fois qu’on cherche deux valeurs liées par une somme.

1.  À la main : avec la fenêtre `3 7 10 7 2` et la cible `13`, calculer pour chaque `x` la valeur `13 - x` et dire si elle est dans la fenêtre. Recommencer avec la cible `14` : pourquoi le complément `7` de `7` ne convient-il pas ?

2.  Écrire `somme_de_deux_ensemble(fenetre, cible)` avec une seule boucle et un ensemble, puis l’utiliser pour retrouver `22` sur l’exemple du défi.

3.  Pour $p = 25$, combien de tests environ fait chaque version pour un nombre ? En déduire les complexités totales.

??? pouce "Coup de pouce"

    Pour chaque `x` de la fenêtre, la seule valeur qui le complète est `cible - x`.

??? pouce "Coup de pouce 2 (début de solution)"

    Construire `valeurs = set(fenetre)`, puis tester `cible - x in valeurs` sans oublier la règle des valeurs différentes : `cible - x != x`.
