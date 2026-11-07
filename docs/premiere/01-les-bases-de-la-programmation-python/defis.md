# Défis Advent of Code

<p class="sous-titre">Les bases de la programmation Python</p>

## <span class="etiquette">Défi</span> The Tyranny of the Rocket Equation

*le carburant de la fusée — division entière, fonctions, boucle while*

<p class="infos-activite">Jour 1</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/01-defi-aoc-2019-01){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/premiere-01-defi-aoc-2019-01.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2019/day/1 ](https://adventofcode.com/2019/day/1 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Créer un compte sur le site est **facultatif** (connexion avec GitHub, Google…). Avec un compte, le lien *get your puzzle input* affiche **vos** données : tout sélectionner, copier, puis coller dans un fichier texte vide enregistré sous le nom `input.txt`, **dans le même dossier** que votre programme Python. Sans compte : le dossier du défi (lien ci-dessus) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - **Attention aux exemples.** L’énoncé en ligne a son propre exemple, avec d’autres réponses. Les valeurs de test de cette fiche portent sur **l’exemple inventé de la fiche** (exercice « À la main ») : l’enregistrer dans un fichier `exemple.txt` à côté du programme, et ouvrir `"exemple.txt"` au lieu de `"input.txt"` pour tester.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

!!! encadre "Le défi en bref"

    **Le problème.** Une fusée est faite d’une centaine de modules, et chacun a besoin d’une quantité de carburant calculée à partir de sa masse. On veut le carburant total à embarquer. Le calcul pour un module est simple, mais le répéter pour cent modules (et, en partie 2, plusieurs fois pour chacun) devient vite pénible et source d’erreurs : un programme s’en charge.

    **Ce qu’on réinvestit.** Les notions de ce chapitre : une **fonction** qui fait le calcul pour un module (écrite une fois, appelée cent fois), la **division entière** `//` qui arrondit à l’unité inférieure, et la boucle `while` pour répéter un calcul tant qu’il donne une quantité positive, avec son **variant** pour être sûr qu’elle s’arrête.

    **La démarche de la fiche.**

    1.  Comprendre la formule sur des questions courtes et l’appliquer à la main à trois modules.

    2.  Choisir la bonne division en Python, puis écrire la fonction `carburant` pour un module.

    3.  Lire le fichier et additionner les carburants de tous les modules : c’est la réponse de la partie 1.

    4.  Pour la partie 2, réutiliser `carburant` dans une boucle `while`, puis vérifier que cette boucle s’arrête.

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| fuel | carburant | mass | masse |
| module | module (élément de la fusée) | required | nécessaire |
| to divide by | diviser par | to round down | arrondir à l’unité inférieure |
| to subtract | soustraire | to add together | additionner |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Le Père Noël est bloqué au bord du système solaire, et les elfes préparent une fusée pour aller le chercher. La fusée est faite de modules, et chaque module a besoin de carburant pour décoller, en quantité qui dépend de sa masse. Avant le décollage, il faut savoir combien de carburant embarquer en tout.

    **Les données.** Le fichier liste les masses des modules : chaque ligne contient **un seul entier positif**, la masse d’un module. Il y a une ligne par module, et l’ordre des lignes n’a pas d’importance.

    **La règle.**

    - Pour un module, on divise sa masse par 3 et on **arrondit à l’entier inférieur**.

    - On retire 2 au résultat : c’est le carburant de ce module. Autrement dit, c’est le quotient de la division entière par 3, moins 2.

    - On fait ce calcul séparément pour chaque module, puis on additionne les résultats.

    **La réponse attendue.** La somme des carburants de tous les modules. Par exemple, pour deux modules de masses 12 et 21, les carburants sont $12 // 3 - 2 = 2$ et $21 // 3 - 2 = 5$ : la réponse serait 7.

### <span class="exo-num">Exercice 1</span> — Vérifier sa compréhension <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-les-bases-de-la-programmation-python-aoc-1-1 }

**But.** S’assurer que l’arrondi « à l’entier inférieur » est bien compris, y compris pour de petites masses.

**À quoi ça sert ?** C’est le seul point délicat de la formule : un mauvais arrondi donne une réponse fausse, même si tout le reste du programme est juste. La dernière question prépare la partie 2, où l’on rencontrera des résultats nuls ou négatifs.

Questions pièges, à traiter sur le cahier :

1.  Quel carburant pour une masse de 9 ? de 10 ? de 11 ? Pourquoi trouve-t-on le même résultat ?

2.  Pour une masse de 2000, quelle différence entre arrondir à l’entier inférieur et arrondir à l’entier le plus proche ?

3.  Que donne la formule pour une masse de 6 ou de 7 ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-les-bases-de-la-programmation-python-aoc-1-2 }

**But.** Appliquer la formule à la main à trois modules inventés, puis faire le total.

**À quoi ça sert ?** Ces trois valeurs serviront de tests : la fonction `carburant` devra les retrouver, et le total donne la réponse attendue du programme complet sur cet exemple.

Calculer le carburant nécessaire pour des modules (inventés) de masses `30`, `90` et `2000`, puis le total. Vérification : on doit obtenir `8`, `28`, `664`, soit un total de `700`.

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Division entière <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-les-bases-de-la-programmation-python-aoc-1-3 }

**But.** Repérer, parmi trois façons de diviser en Python, celle qui arrondit à l’unité inférieure.

**À quoi ça sert ?** C’est l’opérateur à utiliser dans la fonction `carburant`. Avec la mauvaise division, on obtiendrait un nombre à virgule, et toutes les réponses seraient fausses.

En Python, comparer `2000 / 3`, `2000 // 3` et `int(2000 / 3)`. Lequel correspond à « diviser puis arrondir à l’unité inférieure » pour un nombre positif ?

### <span class="exo-num">Exercice 4</span> — Une fonction pour un module <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-les-bases-de-la-programmation-python-aoc-1-4 }

**But.** Écrire la fonction qui calcule le carburant d’un seul module et la tester avec des `assert`.

**À quoi ça sert ?** Elle sera appelée pour chaque ligne du fichier dans la partie 1, puis réutilisée, sans modification, dans la boucle de la partie 2. Les `assert` garantissent qu’elle est juste avant qu’on s’en serve.

Écrire une fonction `carburant(masse)` qui renvoie le carburant d’un module. La tester avec des `assert` sur les trois masses de l’exemple, par exemple `assert carburant(30) == 8`.

??? pouce "Coup de pouce"

    Une seule ligne suffit dans la fonction : `return` suivi du calcul, avec l’opérateur `//`.

!!! encadre "Outil Python : strip (nettoyer une ligne lue)"

    Chaque ligne lue dans le fichier (par exemple avec `for ligne in fichier:`) se termine par le caractère de fin de ligne `"\n"` (sauf parfois la dernière). `ligne.strip()` renvoie une copie de la ligne sans les espaces ni les fins de ligne placés au début et à la fin.

    ```python
    ligne = "1721\n"
    print(ligne.strip())                  # 1721
    print(len(ligne), len(ligne.strip())) # 5 4
    ```

    **Intérêt.** Comparer ou découper une ligne sans que la fin de ligne ne gêne : `"abc\n" == "abc"` vaut `False`.

### <span class="exo-num">Exercice 5</span> — Le total <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-les-bases-de-la-programmation-python-aoc-1-5 }

**But.** Lire les masses dans le fichier et additionner les carburants de tous les modules.

**À quoi ça sert ?** Le résultat affiché sur vos données est la réponse de la partie 1. Le motif de l’accumulateur (un total qui part de 0 et grossit à chaque tour) servira encore dans la partie 2.

!!! encadre "Outil Python : lire un fichier ligne par ligne (open)"

    `open("input.txt")` ouvre le fichier ; une boucle `for` en parcourt les lignes une à une, sous forme de chaînes. Chaque ligne se termine par un retour à la ligne invisible, que `ligne.strip()` retire. Ces lignes sont fournies :

    ```python
    fichier = open("input.txt")      # ouvre le fichier
    for ligne in fichier:            # une ligne a chaque tour de boucle
        ligne = ligne.strip()        # retire le retour a la ligne final
        masse = int(ligne)           # la chaine "1969" devient l'entier 1969
        print(masse)
    fichier.close()                  # ferme le fichier
    ```

Recopier ce programme et l’exécuter sur le fichier `exemple.txt` contenant les trois masses inventées `30`, `90` et `2000` (une par ligne), en remplaçant `"input.txt"` par `"exemple.txt"`. Le modifier ensuite pour calculer la somme des carburants de tous les modules, avec le motif de l’accumulateur : sur l’exemple, on doit trouver `700`. Revenir enfin à `"input.txt"` pour obtenir la réponse.

??? pouce "Coup de pouce"

    Une variable `total` qui vaut 0 avant la boucle ; à chaque tour, on lui ajoute `carburant(masse)`. On affiche `total` après la boucle.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    **Ce qui change.** On avait oublié un détail : le carburant lui-même pèse, et il faut donc du carburant pour le transporter ! Et ce carburant supplémentaire pèse à son tour…

    **La nouvelle règle.**

    - Pour un module, on calcule son carburant avec la formule de la partie 1.

    - On calcule ensuite le carburant de ce carburant, avec la même formule, puis le carburant de ce nouveau carburant, et ainsi de suite.

    - On s’arrête dès qu’on obtient une valeur nulle ou négative : elle compte pour 0.

    - Le carburant du module est la somme de toutes ces quantités. Ce calcul se fait **module par module**.

    **La réponse attendue.** La somme, sur tous les modules, de ces carburants. Par exemple, pour un module de masse 60 : on trouve 18, puis 4 (carburant de 18), puis une valeur négative (carburant de 4) qui arrête le calcul ; le carburant de ce module est $18 + 4 = 22$.

### <span class="exo-num">Exercice 6</span> — Du carburant pour le carburant <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-les-bases-de-la-programmation-python-aoc-1-6 }

**But.** Écrire la fonction qui applique la nouvelle règle à un module, en répétant le calcul tant qu’il donne une quantité positive.

**À quoi ça sert ?** En remplaçant `carburant` par `carburant_total` dans le programme du total, on obtient la réponse de la partie 2. Comme on ne sait pas à l’avance combien de fois répéter le calcul, c’est le rôle de la boucle `while`.

Écrire une fonction `carburant_total(masse)` qui applique la nouvelle règle à un module. Avec les masses de l’exemple, on doit trouver `8`, `35` et `980`, soit un total de `1023`. (Le détail à la main du cas de la masse `90` est demandé à l’exercice suivant.)

??? pouce "Coup de pouce"

    On ne sait pas à l’avance combien de fois il faut recalculer : c’est le cas typique d’une boucle `while`. Que faut-il faire d’une quantité nulle ou négative ?

??? pouce "Coup de pouce 2 (début de solution)"

    `total = 0` et `ajout = carburant(masse)` ; `while ajout > 0:` on ajoute `ajout` à `total`, puis on remplace `ajout` par `carburant(ajout)`. Bien réutiliser la fonction de la partie 1.

### <span class="exo-num">Exercice 7</span> — Vérifier la boucle <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-les-bases-de-la-programmation-python-aoc-1-7 }

**But.** Suivre à la main l’exécution de la boucle sur un exemple, puis justifier qu’elle s’arrête toujours.

**À quoi ça sert ?** Un tableau de valeurs permet de trouver une erreur dans une boucle. Justifier l’arrêt (la quantité diminue à chaque tour : c’est le variant) garantit que le programme ne tournera pas indéfiniment sur les vraies données.

Pour la masse `90`, écrire le tableau des valeurs successives de `ajout` et `total` à chaque tour de boucle. Combien de tours fait la boucle ? Pourquoi est-on sûr qu’elle s’arrête ?

## Approfondissement

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 8</span> — Approfondissement 1 (pour aller plus loin, notion de Terminale) : une fonction qui s’appelle elle-même <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-les-bases-de-la-programmation-python-aoc-1-8 }

**But.** Réécrire `carburant_total` sans boucle, avec une fonction qui s’appelle elle-même.

**À quoi ça sert ?** La règle de la partie 2 se décrit naturellement « en fonction d’elle-même ». Cette découverte prépare la récursivité, étudiée en Terminale, et donne une seconde méthode pour vérifier la réponse.

Une fonction peut s’appeler elle-même : on parle de fonction *récursive*. C’est une notion de Terminale, proposée ici pour les curieux.

1.  Expliquer pourquoi, pour une masse $m$ : carburant total de $m$ = carburant de $m$ + carburant total *de ce carburant*, **lorsque** le carburant de $m$ est strictement positif (sinon le carburant total vaut 0).

2.  Écrire une fonction `carburant_total_rec(masse)`, sans boucle, qui s’appelle elle-même sur la quantité de carburant qu’elle vient de calculer.

    ??? pouce "Coup de pouce"

        Si le carburant d’une masse est nul ou négatif, la réponse est 0 et on s’arrête : c’est le *cas de base* (la condition d’arrêt). Sinon, la réponse est ce carburant, plus le carburant total de ce carburant.

    ??? pouce "Coup de pouce 2 (début de solution)"

        `c = carburant(masse)` ; `if c <= 0:` `return 0` ; sinon `return c + carburant_total_rec(c)`.

3.  Écrire la suite des appels pour la masse 90 et vérifier qu’on retrouve `35`. Pourquoi est-on sûr que les appels s’arrêtent ?
