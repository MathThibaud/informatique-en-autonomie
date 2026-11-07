# Défis Advent of Code

<p class="sous-titre">Le binaire et l'écriture des nombres</p>

## <span class="etiquette">Défi</span> Dive!

*piloter le sous-marin — lire des commandes, variables d’état*

<p class="infos-activite">Jour 2</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/02-defi-aoc-2021-02){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/premiere-02-defi-aoc-2021-02.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2021/day/2 ](https://adventofcode.com/2021/day/2 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (facultatif), le lien *get your puzzle input* donne **vos** données, à enregistrer sous `input.txt` à côté du programme. Sans compte : le dossier du défi (lien ci-dessus) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - **Attention aux exemples.** L’énoncé en ligne a son propre exemple, avec d’autres réponses. Les valeurs de test de cette fiche portent sur **l’exemple inventé de la fiche** (exercice « À la main ») : l’enregistrer dans un fichier `exemple.txt` à côté du programme, et ouvrir `"exemple.txt"` au lieu de `"input.txt"` pour tester.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

!!! encadre "Le défi en bref"

    **Le problème.** Un sous-marin suit un trajet programmé de mille commandes environ : avancer, plonger, remonter. On veut savoir où il se trouvera à la fin du trajet. Suivre mille commandes à la main serait long et l’erreur quasi certaine : un programme le fait en un instant.

    **Ce qu’on réinvestit.** Les bases du chapitre 1 : lire une ligne et accéder à ses caractères par leurs **indices**, convertir un caractère en entier avec `int`, choisir l’action avec `if`/`elif`, et tenir à jour quelques **variables** qui décrivent l’état du sous-marin. L’approfondissement 2 réinvestit en plus l’écriture d’un nombre en base 10, chiffre par chiffre, vue dans ce chapitre.

    **La démarche de la fiche.**

    1.  Comprendre l’effet de chaque commande, puis suivre à la main un petit trajet dans un tableau.

    2.  Apprendre à reconnaître une commande et à lire son nombre à partir d’une ligne du fichier.

    3.  Écrire la fonction qui suit tout le trajet : elle donne la réponse de la partie 1.

    4.  Pour la partie 2, reprendre la même fonction avec une troisième variable et de nouveaux effets pour les commandes.

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|                     |                      |                |             |
|:--------------------|:---------------------|:---------------|:------------|
| forward             | en avant             | depth          | profondeur  |
| horizontal position | position horizontale | command        | commande    |
| to increase by      | augmenter de         | to decrease by | diminuer de |
| planned course      | trajet prévu         | to multiply    | multiplier  |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Vous pilotez maintenant le sous-marin. Son ordinateur de bord contient un trajet déjà programmé : une liste de commandes qui le font avancer, plonger ou remonter. Avant de lancer le trajet, on veut savoir où il va mener le sous-marin.

    **Les données.** Chaque ligne du fichier est une commande, exécutée dans l’ordre : un mot (`forward`, `down` ou `up`), une espace, puis un entier $X$, par exemple `down 4`.

    **La règle.**

    - On suit deux grandeurs, qui valent 0 au départ : la position horizontale et la profondeur.

    - `forward X` fait avancer : la position horizontale augmente de $X$.

    - `down X` fait plonger : la profondeur augmente de $X$.

    - `up X` fait remonter : la profondeur *diminue* de $X$ (c’est une profondeur, donc remonter la réduit).

    **La réponse attendue.** Le produit position horizontale $\times$ profondeur à la fin du trajet. Par exemple, après `forward 5`, `down 2`, `up 1`, `forward 3`, la position horizontale vaut 8 et la profondeur 1 : la réponse serait $8 \times 1 = 8$.

### <span class="exo-num">Exercice 1</span> — Vérifier sa compréhension <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-le-binaire-et-l-ecriture-des-nombres-aoc-1-1 }

**But.** Réfléchir à l’effet des commandes sur la réponse et à la façon de lire une ligne.

**À quoi ça sert ?** La première question montre l’effet d’une variable restée à 0 sur un produit ; la deuxième prépare la partie 2, où l’ordre des commandes compte ; la troisième annonce la méthode de lecture d’une ligne utilisée dans le programme.

Questions pièges, à traiter sur le cahier :

1.  Quelle est la réponse pour un trajet qui ne contient aucune commande `forward` ?

2.  Si l’on mélange l’ordre des lignes, la réponse de la partie 1 change-t-elle ?

3.  Pour la ligne `"down 7"`, que valent `ligne[0]` et `ligne[-1]` ? De quel type est `ligne[-1]` ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-le-binaire-et-l-ecriture-des-nombres-aoc-1-2 }

**But.** Suivre un petit trajet inventé dans un tableau, commande après commande.

**À quoi ça sert ?** Le tableau montre exactement ce que le programme devra faire : mettre à jour deux variables à chaque ligne. Sa dernière ligne donne un résultat connu, qui servira à tester la fonction `trajet`.

On considère le trajet (inventé) suivant :

```console
forward 3
down 4
forward 6
up 1
down 5
forward 2
up 2
```

Faire un tableau avec une ligne par commande et deux colonnes : position horizontale et profondeur. Vérification : on doit arriver à `11` et `6`, soit la réponse `66`.

## Programmer la partie 1

!!! encadre "Outil Python : strip (nettoyer une ligne lue)"

    Chaque ligne lue dans le fichier (avec `for ligne in fichier:`) se termine par le caractère de fin de ligne `"\n"` (sauf parfois la dernière). `ligne.strip()` renvoie une copie de la ligne sans les espaces ni les fins de ligne placés au début et à la fin.

    ```python
    ligne = "1721\n"
    print(ligne.strip())                  # 1721
    print(len(ligne), len(ligne.strip())) # 5 4
    ```

    **Intérêt.** Comparer ou découper une ligne sans que la fin de ligne ne gêne : `"abc\n" == "abc"` vaut `False`.

### <span class="exo-num">Exercice 3</span> — Lire une commande <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-le-binaire-et-l-ecriture-des-nombres-aoc-1-3 }

**But.** Extraire d’une ligne du fichier la lettre qui identifie la commande et le nombre $X$.

**À quoi ça sert ?** Ce sont les deux seules informations dont le programme a besoin pour chaque ligne : la lettre choisit l’action, le nombre dit de combien bouger. Cette lecture sera utilisée dans les deux parties.

Dans les fichiers de données de ce défi, le nombre $X$ n’a qu’**un seul chiffre** (le vérifier en parcourant votre fichier). On peut donc lire une commande sans la découper : sa première lettre suffit à reconnaître la commande, et son dernier caractère est le nombre.

```python
ligne = "forward 3\n"           # une ligne telle qu'on la lit dans le fichier
ligne = ligne.strip()           # "forward 3"
print(ligne[0])                 # f
print(int(ligne[-1]))           # 3 (un entier)
```

Recopier et exécuter ce code. Pourquoi faut-il `strip()` avant de lire `ligne[-1]` ? Les trois commandes ont-elles bien des premières lettres différentes ?

### <span class="exo-num">Exercice 4</span> — Suivre le trajet <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-le-binaire-et-l-ecriture-des-nombres-aoc-1-4 }

**But.** Écrire la fonction qui lit tout le fichier, applique chaque commande et renvoie le produit final.

**À quoi ça sert ?** Elle donne la réponse de la partie 1. Sa structure (lecture, deux variables d’état, un choix selon la lettre) sera reprise telle quelle dans la partie 2, avec une variable de plus.

Écrire une fonction `trajet(nom_fichier)` qui lit le fichier ligne par ligne (`open`, boucle `for`, `strip`), met à jour deux variables `horizontal` et `profondeur`, et renvoie leur produit. Tester sur l’exemple, puis sur vos données.

??? pouce "Coup de pouce"

    Les deux variables valent 0 avant la boucle ; dans la boucle, on calcule `lettre` et `x`, puis un `if` / `elif` / `elif` sur la lettre.

??? pouce "Coup de pouce 2 (début de solution)"

    `lettre = ligne[0]` et `x = int(ligne[-1])` après le `strip()` ; puis `if lettre == "f":` `horizontal += x`, `elif lettre == "d":` …

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    **Ce qui change.** En relisant le manuel du sous-marin, on découvre que les commandes ne signifient pas tout à fait ce qu’on croyait. Une troisième grandeur entre en jeu, la *visée* (*aim*), qui vaut 0 au départ et indique l’inclinaison du sous-marin : plus elle est grande, plus le sous-marin descend quand il avance.

    **La nouvelle règle.**

    - `down X` augmente la visée de $X$, sans toucher à la profondeur.

    - `up X` diminue la visée de $X$, sans toucher à la profondeur.

    - `forward X` augmente la position horizontale de $X$ **et** augmente la profondeur de visée $\times X$.

    **La réponse attendue.** Le même produit position horizontale $\times$ profondeur à la fin du trajet. Avec le même trajet inventé `forward 5`, `down 2`, `up 1`, `forward 3` : la visée vaut 0 au premier `forward`, puis 1 au second, qui fait donc descendre de $1 \times 3 = 3$. On arrive à la position 8 et à la profondeur 3 : la réponse serait 24.

### <span class="exo-num">Exercice 5</span> — Avec une troisième variable <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-le-binaire-et-l-ecriture-des-nombres-aoc-1-5 }

**But.** Refaire le trajet de l’exemple avec la visée, puis adapter la fonction de la partie 1 à la nouvelle règle.

**À quoi ça sert ?** Le tableau fait à la main donne un résultat connu (`440`) pour tester `trajet2`, qui donne la réponse de la partie 2. On voit qu’une nouvelle règle se traduit souvent par une variable d’état de plus.

Refaire le tableau du trajet inventé de l’exercice « À la main » (7 commandes) avec une colonne de plus (la visée) : on doit arriver à `11` et `40`, soit la réponse `440`. Écrire enfin la fonction `trajet2(nom_fichier)`.

??? pouce "Coup de pouce"

    Les mots ne changent pas, mais leur effet, si : deux des commandes ne modifient plus la profondeur directement.

??? pouce "Coup de pouce 2 (début de solution)"

    Trois variables à 0 : `horizontal`, `profondeur`, `visee`. La commande `forward` modifie maintenant **deux** variables, dont l’une avec une multiplication par `visee`.

## Approfondissement

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Approfondissement 1 : un trajet contrôlé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-le-binaire-et-l-ecriture-des-nombres-aoc-1-6 }

**But.** Ajouter une nouvelle commande et signaler clairement les commandes inconnues, avec le numéro de la ligne fautive.

**À quoi ça sert ?** Un vrai programme doit réagir proprement à des données imprévues au lieu de donner un résultat faux sans prévenir. Le numéro de ligne permet de retrouver tout de suite l’erreur dans le fichier.

1.  Ajouter une commande inventée `back X` : la position horizontale *diminue* de `X` dans une fonction `trajet_controle(nom_fichier)` qui reprend la partie 1.

2.  Faire en sorte qu’une commande inconnue affiche un message d’erreur clair avec le numéro de la ligne fautive (la première ligne porte le numéro 1), sans arrêter le programme.

    ??? pouce "Coup de pouce"

        Un compteur `numero`, augmenté de 1 au début de chaque tour de boucle, et un dernier `else` pour les mots inconnus.

3.  On ajoute à la fin du trajet inventé de la fiche (7 lignes) les deux lignes `back 4` et `jump 3`. Prévoir à la main le message affiché et le résultat, puis vérifier avec le programme.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 2 : des nombres à plusieurs chiffres <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-le-binaire-et-l-ecriture-des-nombres-aoc-1-7 }

**But.** Lire un nombre de plusieurs chiffres, caractère par caractère, sans découper la ligne.

**À quoi ça sert ?** La méthode de la fiche ne marche que si $X$ a un seul chiffre ; celle-ci lève cette limite. Elle reprend la reconstitution d’un nombre en base 10 vue dans ce chapitre, et s’adapte aux autres bases.

Et si $X$ pouvait avoir plusieurs chiffres, comme dans `forward 125` ? On lit alors les chiffres un par un, de gauche à droite, comme lorsqu’on reconstitue la valeur d’un nombre écrit en base 10.

1.  On part de `nombre = 0`. À chaque chiffre $c$ lu, on remplace `nombre` par $10 \times \texttt{nombre} + c$. Écrire les valeurs successives de `nombre` pour les chiffres de `125`.

2.  Écrire une fonction `valeur_longue(ligne)` qui renvoie le nombre écrit après l’espace, quel que soit son nombre de chiffres.

    ??? pouce "Coup de pouce"

        Parcourir les caractères de la ligne avec une variable booléenne `apres_espace`, qui passe à `True` quand on rencontre l’espace.

    ??? pouce "Coup de pouce 2 (début de solution)"

        Dans la boucle : `if apres_espace:` on met à jour `nombre` avec `int(c)` ; `elif c == " ":` on passe `apres_espace` à `True`.

3.  Comment adapter cette méthode à un nombre écrit en base 2 ?
