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

!!! encadre "Le défi en bref"

    **Le problème.** On dispose d’une longue liste de profondeurs mesurées les unes après les autres (plus de deux mille dans les vraies données). On veut savoir combien de fois la profondeur augmente d’une mesure à la suivante. À la main, sur quelques nombres, c’est immédiat ; sur deux mille, il faut un programme.

    **Ce qu’on réinvestit.** Le parcours d’un tableau **par indices**, vu dans ce chapitre : avec l’indice `i`, on accède à la fois à l’élément `mesures[i]` et à son voisin `mesures[i - 1]`, ce qu’une boucle `for x in mesures` ne permet pas directement. On utilise aussi un compteur.

    **La démarche de la fiche.**

    1.  Comprendre la règle avec des questions courtes, puis l’appliquer à la main sur un petit exemple dont on connaît la réponse.

    2.  Lire le fichier de données et le ranger dans une liste d’entiers.

    3.  Écrire une fonction qui compte les augmentations : elle donne la réponse de la partie 1.

    4.  Réutiliser cette même fonction, sans la modifier, pour la partie 2.

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|             |                 |             |                |
|:------------|:----------------|:------------|:---------------|
| depth       | profondeur      | sea floor   | fond de la mer |
| measurement | mesure          | to increase | augmenter      |
| to decrease | diminuer        | previous    | précédent      |
| report      | relevé, rapport | N/A         | sans objet     |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Les clés du traîneau sont tombées à la mer, et vous voilà dans un sous-marin pour les récupérer. Pendant que le sous-marin avance, son sonar mesure la profondeur du fond marin, point après point. Avant de plonger plus loin, on veut savoir à quel point le fond descend : est-ce qu’il s’enfonce souvent, ou est-ce qu’il reste plat ?

    **Les données.** Le fichier est le relevé du sonar. Chaque ligne contient **un seul entier** : une profondeur, en mètres. Les lignes sont dans l’ordre où les mesures ont été faites : la ligne 2 a été mesurée juste après la ligne 1, et ainsi de suite. Plus le nombre est grand, plus le fond est profond.

    **La règle.**

    - On compare chaque mesure à la mesure **juste avant elle** (et seulement à celle-là).

    - Si elle est **strictement** plus grande, le fond s’est enfoncé : on compte une augmentation.

    - Si elle est plus petite ou égale, on ne compte rien.

    - La première mesure n’a pas de mesure avant elle : elle ne peut pas compter.

    **La réponse attendue.** Le nombre total d’augmentations dans tout le fichier. Par exemple, pour les quatre mesures 10, 12, 12, 15, il y a deux augmentations (de 10 à 12, puis de 12 à 15) : la réponse serait 2.

### <span class="exo-num">Exercice 1</span> — Vérifier sa compréhension <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-algorithmique-le-parcours-sequentiel-aoc-1-1 }

**But.** S’assurer qu’on a bien compris la règle, en particulier ses cas limites, avant d’écrire la moindre ligne de code.

**À quoi ça sert ?** Chacune de ces questions correspond à une erreur fréquente dans le programme : une boucle qui fait une comparaison de trop ou de moins, une égalité comptée par erreur.

À traiter sur le cahier :

1.  Pour un fichier de 5 mesures, combien de comparaisons faut-il faire ?

2.  Que vaut la réponse si toutes les mesures sont égales ? Si elles sont rangées par ordre décroissant ?

3.  Une mesure plus grande que *toutes* les précédentes, mais plus petite que celle juste avant, est-elle comptée ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-algorithmique-le-parcours-sequentiel-aoc-1-2 }

**But.** Appliquer la règle à la main sur dix mesures.

**À quoi ça sert ?** On obtient un petit exemple dont on **connaît la réponse**. Plus loin, on testera le programme sur cet exemple avant de le lancer sur les vraies données : si le programme ne trouve pas 5 ici, inutile d’aller plus loin.

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

**But.** Transformer le fichier texte en une liste Python d’entiers, `mesures`.

**À quoi ça sert ?** Le fichier contient du texte (des chaînes de caractères comme `"152\n"`), qu’on ne peut pas comparer correctement : il faut des entiers. Une fois la liste construite, tout le reste du défi travaille sur elle, sans relire le fichier.

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

**But.** Écrire la fonction qui applique la règle à toute la liste.

**À quoi ça sert ?** C’est le cœur du défi : appelée sur la liste lue dans le fichier, elle donne directement la réponse de la partie 1. On l’écrit sous forme de **fonction** (qui prend une liste et renvoie un nombre) pour pouvoir la réutiliser telle quelle dans la partie 2.

Écrire une fonction `nb_augmentations(mesures)` qui renvoie le nombre de mesures plus grandes que la précédente. Tester sur l’exemple (`5`), puis sur vos données.

??? pouce "Coup de pouce"

    Parcourir les **indices** avec `for i in range(1, len(mesures))` : l’élément précédent de `mesures[i]` est `mesures[i - 1]`.

??? pouce "Coup de pouce 2 (début de solution)"

    Un compteur `nb = 0` avant la boucle ; dans la boucle, `if mesures[i] > mesures[i - 1]:` alors `nb += 1`. Pourquoi la boucle commence-t-elle à 1 et non à 0 ?

### <span class="exo-num">Exercice 5</span> — Erreur classique <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-algorithmique-le-parcours-sequentiel-aoc-1-5 }

**But.** Comprendre pourquoi la boucle doit commencer à l’indice 1.

**À quoi ça sert ?** Les erreurs d’indices (un élément oublié, un élément de trop, une erreur `IndexError`) sont les plus fréquentes dans les parcours de tableaux ; savoir les repérer fera gagner beaucoup de temps dans les défis suivants.

Que se passerait-il si la boucle était `for i in range(len(mesures) - 1)` en comparant `mesures[i]` et `mesures[i + 1]` ? Et avec `for i in range(len(mesures))` ? Tester pour vérifier.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    **Ce qui change.** Une mesure isolée peut être faussée par le bruit du sonar : un poisson qui passe, une vague. Pour avoir une idée plus fiable du relief, on ne compare plus les mesures une à une, mais des **groupes de trois mesures consécutives**.

    **La nouvelle règle.**

    - On calcule la somme des mesures 1, 2 et 3 ; puis celle des mesures 2, 3 et 4 ; puis 3, 4 et 5, et ainsi de suite. Les groupes se **chevauchent** : chaque nouveau groupe perd la plus ancienne mesure et gagne la suivante.

    - On s’arrête quand il ne reste plus trois mesures pour former un groupe complet.

    - On compte, comme dans la partie 1, combien de fois une somme est strictement plus grande que la somme juste avant elle.

    **La réponse attendue.** Ce nombre d’augmentations entre sommes consécutives.

### <span class="exo-num">Exercice 6</span> — Des sommes de trois mesures <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-algorithmique-le-parcours-sequentiel-aoc-1-6 }

**But.** Fabriquer la liste des sommes de trois mesures consécutives, puis compter ses augmentations.

**À quoi ça sert ?** La partie 2 pose la même question que la partie 1, mais sur une autre liste. Plutôt que de tout réécrire, on construit cette nouvelle liste et on lui applique la fonction `nb_augmentations` déjà écrite : c’est tout l’intérêt d’avoir écrit une fonction.

Écrire une fonction `sommes_par_trois(mesures)` qui renvoie la liste des sommes de trois mesures consécutives, puis réutiliser `nb_augmentations` sur cette nouvelle liste. Sur l’exemple du défi, on doit trouver `7`.

??? pouce "Coup de pouce"

    Si la liste a $n$ éléments, combien y a-t-il de groupes de trois éléments consécutifs ? La somme qui commence à l’indice `i` est `mesures[i] + mesures[i + 1] + mesures[i + 2]`.

??? pouce "Coup de pouce 2 (début de solution)"

    `for i in range(len(mesures) - 2):` et ajouter la somme ci-dessus à une liste `sommes`. Ensuite : `nb_augmentations(sommes)`.

## Approfondissement

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 1 : sans calculer les sommes <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-algorithmique-le-parcours-sequentiel-aoc-1-7 }

**But.** Trouver une façon plus courte de résoudre la partie 2, en raisonnant avant de programmer.

**À quoi ça sert ?** En observant ce que deux sommes voisines ont en commun, on remplace une addition de trois nombres par une seule comparaison. Simplifier un calcul par un raisonnement est une démarche qui reviendra souvent en informatique.

1.  Comparer la somme qui commence à `i` et celle qui commence à `i + 1` : quels termes ont-elles en commun ? Quelle comparaison suffit pour savoir laquelle est la plus grande ?

    ??? pouce "Coup de pouce"

        Les deux sommes partagent deux mesures sur trois. Il suffit de comparer les deux mesures qui ne sont pas communes.

2.  Sur l’exemple du défi, faire les comparaisons trouvées à la main et retrouver `7`.

3.  Écrire une fonction `nb_augmentations_fenetres(mesures)` qui résout la partie 2 sans calculer aucune somme.

    ??? pouce "Coup de pouce 2 (début de solution)"

        La somme commençant à `i - 2` est plus grande que celle commençant à `i - 3` exactement quand `mesures[i] > mesures[i - 3]` ; `i` va de 3 à `len(mesures) - 1`.

4.  Généraliser : écrire `nb_augmentations_taille(mesures, taille)` pour des groupes de `taille` mesures. Que donne-t-elle avec `taille = 1` ?
