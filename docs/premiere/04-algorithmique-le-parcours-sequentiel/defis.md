# Défis Advent of Code

<p class="sous-titre">Algorithmique : le parcours séquentiel</p>

## <span class="etiquette">Défi</span> Sonar Sweep

*le sondeur du sous-marin — comparer à l’élément précédent*

<p class="infos-activite">Jour 1</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/04-defi-aoc-2021-01){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/premiere-04-defi-aoc-2021-01.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2021/day/1 ](https://adventofcode.com/2021/day/1 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (facultatif), le lien *get your puzzle input* donne **vos** données, à enregistrer sous `input.txt` à côté du programme. Sans compte : le dossier du défi (lien ci-dessus) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

*Ce défi réinvestit le parcours séquentiel d’un tableau vu dans ce chapitre : comparer chaque élément au précédent et compter.*

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|             |                 |             |                |
|:------------|:----------------|:------------|:---------------|
| depth       | profondeur      | sea floor   | fond de la mer |
| measurement | mesure          | to increase | augmenter      |
| to decrease | diminuer        | previous    | précédent      |
| report      | relevé, rapport | N/A         | sans objet     |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Les clés du traîneau sont tombées à la mer, et vous voilà dans un sous-marin pour les récupérer. En s’éloignant, le sonar du sous-marin mesure la profondeur du fond marin, point après point. Le fichier est ce relevé : chaque ligne est une profondeur, dans l’ordre où elles ont été mesurées. On veut savoir si le fond descend vite.

    **Ce qu’il faut faire.**

    - Le fichier contient une mesure (un entier) par ligne.

    - Il faut compter combien de fois une mesure est **strictement** plus grande que la mesure juste avant elle ; autrement dit, combien de fois le fond s’enfonce d’un point au suivant.

    - La première mesure n’a pas de précédente : elle n’est jamais comptée. Deux mesures égales ne comptent pas non plus.

    - La réponse est ce nombre d’augmentations.

### <span class="exo-num">Exercice 1</span> — Vérifier sa compréhension <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-algorithmique-le-parcours-sequentiel-aoc-1-1 }

Questions pièges, à traiter sur le cahier :

1.  Pour un fichier de 5 mesures, combien de comparaisons faut-il faire ?

2.  Que vaut la réponse si toutes les mesures sont égales ? Si elles sont rangées par ordre décroissant ?

3.  Une mesure plus grande que *toutes* les précédentes, mais plus petite que celle juste avant, est-elle comptée ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-algorithmique-le-parcours-sequentiel-aoc-1-2 }

On considère le relevé (inventé) suivant, écrit ici sur une seule ligne pour gagner de la place (dans le fichier, il y a un nombre par ligne) :

```console
150  152  149  155  160  160  158  165  170  168
```

Écrire sous chaque nombre (sauf le premier) « + » s’il augmente par rapport au précédent, « $-$ » s’il diminue, « $=$ » s’il ne change pas. Vérification : la réponse attendue est `5`.

## Programmer la partie 1

!!! encadre "Outil Python : strip (nettoyer une ligne lue)"

    Chaque ligne renvoyée par `readlines()` se termine par le caractère de fin de ligne `"\n"` (sauf parfois la dernière). `ligne.strip()` renvoie une copie de la ligne sans les espaces ni les fins de ligne placés au début et à la fin.

    ```python
    ligne = "1721\n"
    print(ligne.strip())                  # 1721
    print(len(ligne), len(ligne.strip())) # 5 4
    ```

    **Intérêt.** Comparer ou découper une ligne sans que la fin de ligne ne gêne : `"abc\n" == "abc"` vaut `False`.

### <span class="exo-num">Exercice 3</span> — Lire le fichier dans une liste <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-algorithmique-le-parcours-sequentiel-aoc-1-3 }

Compléter ce programme pour qu’il construise la liste `mesures` des entiers du fichier :

```python
mesures = []
fichier = open("input.txt")
for ligne in fichier:
    ...          # convertir la ligne en entier et l'ajouter a la liste
fichier.close()
print(len(mesures), mesures[:5])
```

Tester d’abord avec un fichier `exemple.txt` contenant l’exemple ci-dessus (un nombre par ligne).

??? pouce "Coup de pouce"

    `ligne.strip()` enlève le retour à la ligne, `int(...)` convertit en entier, `mesures.append(...)` ajoute à la liste.

### <span class="exo-num">Exercice 4</span> — Compter les augmentations <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-algorithmique-le-parcours-sequentiel-aoc-1-4 }

Écrire une fonction `nb_augmentations(mesures)` qui renvoie le nombre de mesures plus grandes que la précédente. Tester sur l’exemple (`5`), puis sur vos données.

??? pouce "Coup de pouce"

    Parcourir les **indices** avec `for i in range(1, len(mesures))` : l’élément précédent de `mesures[i]` est `mesures[i - 1]`.

??? pouce "Coup de pouce 2 (début de solution)"

    Un compteur `nb = 0` avant la boucle ; dans la boucle, `if mesures[i] > mesures[i - 1]:` alors `nb += 1`. Pourquoi la boucle commence-t-elle à 1 et non à 0 ?

### <span class="exo-num">Exercice 5</span> — Erreur classique <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-algorithmique-le-parcours-sequentiel-aoc-1-5 }

Que se passerait-il si la boucle était `for i in range(len(mesures) - 1)` en comparant `mesures[i]` et `mesures[i + 1]` ? Et avec `for i in range(len(mesures))` ? Tester pour vérifier.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    Les mesures isolées sont trop sensibles au bruit du sonar : on les lisse en les regroupant. On remplace la liste par les sommes de **trois mesures consécutives** : mesures 1-2-3, puis 2-3-4, puis 3-4-5… Ces groupes se chevauchent, et l’on s’arrête quand il ne reste plus trois mesures. La réponse est le nombre de sommes strictement plus grandes que la somme précédente.

### <span class="exo-num">Exercice 6</span> — Des sommes de trois mesures <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-algorithmique-le-parcours-sequentiel-aoc-1-6 }

Écrire une fonction `sommes_par_trois(mesures)` qui renvoie la liste des sommes de trois mesures consécutives, puis réutiliser `nb_augmentations` sur cette nouvelle liste. Sur l’exemple du défi, on doit trouver `7`.

??? pouce "Coup de pouce"

    Si la liste a $n$ éléments, combien y a-t-il de groupes de trois éléments consécutifs ? La somme qui commence à l’indice `i` est `mesures[i] + mesures[i + 1] + mesures[i + 2]`.

??? pouce "Coup de pouce 2 (début de solution)"

    `for i in range(len(mesures) - 2):` et ajouter la somme ci-dessus à une liste `sommes`. Ensuite : `nb_augmentations(sommes)`.

## Approfondissement

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 1 : sans calculer les sommes <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-algorithmique-le-parcours-sequentiel-aoc-1-7 }

1.  Comparer la somme qui commence à `i` et celle qui commence à `i + 1` : quels termes ont-elles en commun ? Quelle comparaison suffit pour savoir laquelle est la plus grande ?

    ??? pouce "Coup de pouce"

        Les deux sommes partagent deux mesures sur trois. Il suffit de comparer les deux mesures qui ne sont pas communes.

2.  Sur l’exemple du défi, faire les comparaisons trouvées à la main et retrouver `7`.

3.  Écrire une fonction `nb_augmentations_fenetres(mesures)` qui résout la partie 2 sans calculer aucune somme.

    ??? pouce "Coup de pouce 2 (début de solution)"

        La somme commençant à `i - 2` est plus grande que celle commençant à `i - 3` exactement quand `mesures[i] > mesures[i - 3]` ; `i` va de 3 à `len(mesures) - 1`.

4.  Généraliser : écrire `nb_augmentations_taille(mesures, taille)` pour des groupes de `taille` mesures. Que donne-t-elle avec `taille = 1` ?
