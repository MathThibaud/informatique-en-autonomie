# Défis Advent of Code

<p class="sous-titre">Les algorithmes gloutons</p>

## <span class="etiquette">Défi</span> Lobby

*les batteries de l’escalator — un algorithme glouton*

<p class="infos-activite">Jour 3</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/11-defi-aoc-2025-03){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/premiere-11-defi-aoc-2025-03.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2025/day/3 ](https://adventofcode.com/2025/day/3 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (lien ci-dessus) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

*Ce défi est une application directe de ce chapitre : un algorithme glouton, dont il faudra justifier qu’il donne bien la meilleure solution.*

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|                  |                          |              |                  |
|:-----------------|:-------------------------|:-------------|:-----------------|
| battery          | pile, batterie           | bank         | rangée, groupe   |
| joltage rating   | tension indiquée (1 à 9) | turn on      | allumer, activer |
| exactly two      | exactement deux          | rearrange    | réordonner       |
| largest possible | le plus grand possible   | total output | total produit    |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Dans le hall d’un immeuble, les ascenseurs sont en panne, et même l’escalier mécanique est à l’arrêt faute de courant. Des batteries de secours peuvent l’alimenter. Elles sont rangées en groupes, et chaque batterie porte une tension de 1 à 9. Chaque ligne du fichier décrit un groupe : la suite des tensions de ses batteries, dans l’ordre où elles sont rangées.

    **Ce qu’il faut faire.**

    - Dans chaque groupe, on allume **exactement deux** batteries. Le groupe produit le nombre à deux chiffres formé par leurs tensions, **dans l’ordre de la ligne** : on ne peut pas réordonner les batteries.

    - On veut, pour chaque groupe, le plus grand nombre possible.

    - Réponse : la somme de ces maxima sur toutes les lignes.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-les-algorithmes-gloutons-aoc-1-1 }

Après lecture du résumé (et de l’énoncé), vérifier sa compréhension sur ces cas particuliers :

1.  Dans la ligne `19`, peut-on obtenir `91` ?

2.  Si le plus grand chiffre de la ligne est le dernier caractère, peut-il servir de chiffre des dizaines ?

3.  Dans `9399`, quels chiffres faut-il choisir ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-les-algorithmes-gloutons-aoc-1-2 }

On considère le fichier (inventé) suivant :

```console
372819465123987
111119111181111
564738291564738
999888777666555
```

Pour chaque ligne, trouver le plus grand nombre de deux chiffres possible. Vérification : on doit obtenir `394`. Pour la troisième ligne, pourquoi ne peut-on pas obtenir `99` ?

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Lire et tester toutes les paires <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-les-algorithmes-gloutons-aoc-1-3 }

Rappel pour lire un fichier ligne par ligne :

```python
fichier = open("input.txt", encoding="utf-8")
for ligne in fichier:
    ligne = ligne.strip()   # enlève le retour à la ligne final
fichier.close()
```

Écrire une fonction `meilleur_par_paires(ligne)` qui essaie tous les couples d’indices `i < j` et renvoie le plus grand nombre `int(ligne[i] + ligne[j])`. Calculer la réponse (`394` sur l’exemple).

??? pouce "Coup de pouce"

    Deux boucles imbriquées, la seconde commençant à `i + 1`, et un calcul de maximum.

!!! encadre "Outil Python : plus grand caractère et position (max, index)"

    `max` appliqué à une chaîne renvoie son plus grand caractère ; pour des chiffres, c’est le plus grand chiffre. `ligne.index(c)` renvoie l’indice de la **première** apparition de `c` dans `ligne`.

    ```python
    ligne = "38193"
    print(max(ligne))          # 9 : le plus grand caractere ("9" > "8" > ... > "1")
    print(ligne.index("9"))    # 3 : indice de la PREMIERE apparition
    print(ligne.index("3"))    # 0 : premiere apparition, pas la derniere
    print(max(ligne[:-1]))     # 9 : on peut chercher dans une tranche
    ```

    **Intérêt.** Deux appels remplacent une boucle de recherche du maximum avec mémorisation de sa position.

    *À essayer.* Que renvoie `"5958".index("5")` ? Et `max("5958"[1:])` ?

### <span class="exo-num">Exercice 4</span> — Une idée gloutonne <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-les-algorithmes-gloutons-aoc-1-4 }

Écrire une seconde fonction `meilleur_glouton(ligne)` qui ne fait que deux parcours : choisir d’abord le meilleur chiffre des dizaines, puis le meilleur chiffre des unités *après* lui. Vérifier qu’elle donne les mêmes résultats que la précédente.

??? pouce "Coup de pouce"

    Le chiffre des dizaines compte dix fois plus que celui des unités : il faut le prendre le plus grand possible. Mais il ne peut pas être le dernier caractère de la ligne (il faut laisser une place pour les unités).

??? pouce "Coup de pouce 2 (début de solution)"

    Chercher le maximum de `ligne[:-1]` et l’indice `p` de sa **première** apparition (`index`), puis le maximum de `ligne[p+1:]`. Les chiffres se comparent très bien sous forme de caractères : `"9" > "8"`.

!!! encadre "Lien avec le cours : algorithmes gloutons"

    Un algorithme **glouton** construit une solution en faisant, à chaque étape, le choix qui semble le meilleur sur le moment, sans jamais revenir en arrière (comme le rendu de monnaie du cours). Il est rapide, mais il ne donne pas toujours la meilleure solution : il faut le **justifier**. Ici, pourquoi est-il correct ? Deux nombres de même longueur se comparent d’abord par leur premier chiffre ; le premier chiffre choisi doit donc être le plus grand *parmi ceux qui laissent assez de chiffres après eux*. Si ce maximum apparaît plusieurs fois, prendre sa *première* apparition laisse le plus de choix pour la suite. Après ce choix, il reste le même problème, plus petit, sur la fin de la ligne.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    Deux batteries par groupe ne suffisent pas à faire repartir l’escalier. On allume maintenant **exactement 12** batteries dans chaque groupe, toujours sans changer leur ordre, pour former le plus grand nombre de 12 chiffres possible. Réponse : la somme de ces maxima sur toutes les lignes.

### <span class="exo-num">Exercice 5</span> — Combien de possibilités ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-les-algorithmes-gloutons-aoc-1-5 }

Dans la partie 2, on ne choisit plus deux chiffres. Regarder la longueur des lignes de vos données. Pour une ligne de 100 chiffres, essayer toutes les possibilités est-il raisonnable ? (Pour 12 chiffres choisis parmi 100, il y a plus de $10^{15}$ possibilités.)

### <span class="exo-num">Exercice 6</span> — Le glouton généralisé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-les-algorithmes-gloutons-aoc-1-6 }

Écrire une fonction `meilleur(ligne, k)` qui choisit `k` chiffres, de gauche à droite, avec le même principe glouton. La partie 1 correspond à `k = 2`. Sur l’exemple du défi, avec `k = 12`, la première ligne donne `819465123987` et le total vaut `2676756647502`.

??? pouce "Coup de pouce"

    Quand il reste `r` chiffres à choisir, le prochain chiffre doit laisser au moins `r - 1` chiffres après lui : on le cherche donc entre l’indice `debut` (juste après le chiffre choisi précédemment) et l’indice `len(ligne) - r` inclus.

??? pouce "Coup de pouce 2 (début de solution)"

    Une boucle `for r in range(k, 0, -1):` ; la fenêtre de recherche est `ligne[debut:len(ligne) - r + 1]` ; on y prend le maximum, on avance `debut` juste après sa première apparition, et on ajoute ce chiffre à une chaîne `resultat`.

## Approfondissement

!!! encadre "Outil Python : hasard et combinaisons (random, itertools)"

    Le module `random` tire des nombres au hasard ; `randint(a, b)` renvoie un entier entre `a` et `b` inclus. La fonction `combinations` du module `itertools` énumère tous les choix de `k` éléments d’une chaîne ou d’une liste, **dans leur ordre d’origine**.

    ```python
    import random
    from itertools import combinations

    print(random.randint(1, 9))            # un entier au hasard entre 1 et 9 (inclus)
    for choix in combinations("1234", 2):  # tous les choix de 2 caracteres, ordre conserve
        print(choix)                       # ('1', '2'), ('1', '3'), ..., ('3', '4')
    print(len([t for t in combinations("12345", 3)]))   # 10
    ```

    **Intérêt.** Pour tester un algorithme rapide, on le compare à une recherche exhaustive lente mais sûre, sur beaucoup de petits cas tirés au hasard.

    *À essayer.* Combien de choix `combinations("123456", 2)` fournit-il ?

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 1 : convaincre et tester <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-11-les-algorithmes-gloutons-aoc-1-7 }

1.  Écrire une fonction `exhaustif(ligne, k)` qui essaie tous les choix de `k` chiffres avec `combinations` et renvoie le plus grand nombre obtenu.

    ??? pouce "Coup de pouce"

        Chaque choix est un p-uplet de caractères : `"".join(choix)` le transforme en chaîne.

2.  Comparer `meilleur(ligne, k)` et `exhaustif(ligne, k)` sur 300 lignes de 15 chiffres tirées au hasard, avec `k` lui aussi au hasard. Combien de désaccords ?

3.  Rédiger en quelques lignes la justification du glouton pour `k` quelconque.

4.  Que se passerait-il si l’on prenait la *dernière* apparition du maximum ? Tester la ligne `"9919"` avec `k = 3`.

    ??? pouce "Coup de pouce"

        Prendre une apparition plus tardive laisse moins de chiffres après elle.
