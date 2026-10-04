# Défis Advent of Code

<p class="sous-titre">Algorithmique : le parcours séquentiel</p>

## <span class="etiquette">Défi 1</span> Sonar Sweep

*le sondeur du sous-marin — comparer à l’élément précédent*

<p class="infos-activite">Jour 1</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/04-defi-aoc-2021-01){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/premiere-04-defi-aoc-2021-01.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2021/day/1 ](https://adventofcode.com/2021/day/1 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (facultatif), le lien *get your puzzle input* donne **vos** données, à enregistrer sous `input.txt` à côté du programme. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/04-defi-aoc-2021-01>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

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

Que se passerait-il si la boucle allait de `0` à `len(mesures) - 1` en comparant `mesures[i]` et `mesures[i + 1]` ? Et jusqu’à `len(mesures)` ? Tester pour vérifier.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    Les mesures isolées sont trop sensibles au bruit du sonar : on les lisse en les regroupant. On remplace la liste par les sommes de **trois mesures consécutives** : mesures 1-2-3, puis 2-3-4, puis 3-4-5… Ces groupes se chevauchent, et l’on s’arrête quand il ne reste plus trois mesures. La réponse est le nombre de sommes strictement plus grandes que la somme précédente.

### <span class="exo-num">Exercice 6</span> — Des sommes de trois mesures <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-algorithmique-le-parcours-sequentiel-aoc-1-6 }

Écrire une fonction `sommes_par_trois(mesures)` qui renvoie la liste des sommes de trois mesures consécutives, puis réutiliser `nb_augmentations` sur cette nouvelle liste. Sur l’exemple de la fiche, on doit trouver `7`.

??? pouce "Coup de pouce"

    Si la liste a $n$ éléments, combien y a-t-il de groupes de trois éléments consécutifs ? La somme qui commence à l’indice `i` est `mesures[i] + mesures[i + 1] + mesures[i + 2]`.

??? pouce "Coup de pouce 2 (début de solution)"

    `for i in range(len(mesures) - 2):` et ajouter la somme ci-dessus à une liste `sommes`. Ensuite : `nb_augmentations(sommes)`.

## Approfondissement

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 1 : sans calculer les sommes <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-algorithmique-le-parcours-sequentiel-aoc-1-7 }

1.  Comparer la somme qui commence à `i` et celle qui commence à `i + 1` : quels termes ont-elles en commun ? Quelle comparaison suffit pour savoir laquelle est la plus grande ?

    ??? pouce "Coup de pouce"

        Les deux sommes partagent deux mesures sur trois. Il suffit de comparer les deux mesures qui ne sont pas communes.

2.  Sur l’exemple de la fiche, faire les comparaisons trouvées à la main et retrouver `7`.

3.  Écrire une fonction `nb_augmentations_fenetres(mesures)` qui résout la partie 2 sans calculer aucune somme.

    ??? pouce "Coup de pouce 2 (début de solution)"

        La somme commençant à `i - 2` est plus grande que celle commençant à `i - 3` exactement quand `mesures[i] > mesures[i - 3]` ; `i` va de 3 à `len(mesures) - 1`.

4.  Généraliser : écrire `nb_augmentations_taille(mesures, taille)` pour des groupes de `taille` mesures. Que donne-t-elle avec `taille = 1` ?

## <span class="etiquette">Défi 2</span> Inverse Captcha

*le code de la porte — chaînes de chiffres et indice circulaire*

<p class="infos-activite">Jour 1</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/04-defi-aoc-2017-01){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/premiere-04-defi-aoc-2017-01.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2017/day/1 ](https://adventofcode.com/2017/day/1 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (facultatif), le lien *get your puzzle input* donne **vos** données, à enregistrer sous `input.txt` à côté du programme. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/04-defi-aoc-2017-01>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

*Ce défi réinvestit le parcours séquentiel vu dans ce chapitre, ici sur les indices d’une chaîne de caractères.*

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|           |                                  |          |         |
|:----------|:---------------------------------|:---------|:--------|
| digit     | chiffre                          | sequence | suite   |
| to match  | être identique à                 | next     | suivant |
| circular  | circulaire (on revient au début) | sum      | somme   |
| to review | examiner                         | to prove | prouver |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Vous êtes aspiré dans un ordinateur, devant une porte verrouillée. Pour sortir, il faut résoudre un « captcha » inversé, censé prouver que vous *n’êtes pas* un humain. Le fichier contient ce captcha : une très longue suite de chiffres, à traiter comme une suite de caractères.

    **Ce qu’il faut faire.**

    - Le fichier ne contient qu’**une seule ligne**, formée de chiffres collés les uns aux autres.

    - On compare chaque chiffre au chiffre **suivant**. Quand ils sont égaux, on ajoute la valeur de ce chiffre à une somme ; sinon, on n’ajoute rien.

    - La suite est **circulaire** : on imagine les chiffres disposés en cercle, si bien que le suivant du dernier chiffre est le premier.

    - La réponse est la somme obtenue.

### <span class="exo-num">Exercice 1</span> — Vérifier sa compréhension <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-algorithmique-le-parcours-sequentiel-aoc-2-1 }

Questions pièges, à traiter sur le cahier :

1.  Quelle somme donne la chaîne `77` ? Pourquoi n’est-ce pas `7` ?

2.  Dans `9339`, combien de fois le chiffre `3` est-il ajouté ? Et le `9` ?

3.  Faut-il convertir toute la chaîne en un seul entier ? Pourquoi serait-ce une mauvaise idée ?

### <span class="exo-num">Exercice 2</span> — À la main, sur de petits exemples <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-algorithmique-le-parcours-sequentiel-aoc-2-2 }

Pour chacune des chaînes (inventées) suivantes, trouver la réponse attendue : `7337`, `5225`, `123323`. Vérification : on doit obtenir `10`, `7` et `3`. Pour `7337`, quel couple n’est trouvé que grâce au caractère circulaire ?

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Lire l’unique ligne <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-algorithmique-le-parcours-sequentiel-aoc-2-3 }

Le fichier ne contient qu’une ligne. La lire ainsi :

```python
fichier = open("input.txt")
chiffres = fichier.readline().strip()   # une chaine de caracteres
fichier.close()
print(len(chiffres), chiffres[:10])
```

Que vaut `chiffres[0]` ? Est-ce un nombre ou un caractère ? Comment obtenir l’entier correspondant ?

??? pouce "Coup de pouce"

    `chiffres[0]` est un caractère comme `"7"` ; `int(chiffres[0])` donne l’entier `7`. Attention : `"7" == 7` vaut `False`.

### <span class="exo-num">Exercice 4</span> — L’indice du suivant <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-algorithmique-le-parcours-sequentiel-aoc-2-4 }

Pour une chaîne de longueur `n`, quel est l’indice du suivant de l’élément d’indice `i` si `i < n - 1` ? Et si `i = n - 1` ? Calculer `(i + 1) % n` pour `n = 4` et `i` allant de 0 à 3 : que remarque-t-on ?

### <span class="exo-num">Exercice 5</span> — La somme du captcha <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-algorithmique-le-parcours-sequentiel-aoc-2-5 }

Écrire une fonction `captcha(chiffres)` qui renvoie la réponse de la partie 1. Tester sur les trois exemples, puis sur vos données.

??? pouce "Coup de pouce"

    Parcourir les indices `i` de 0 à `n - 1` ; comparer `chiffres[i]` et `chiffres[(i + 1) % n]`.

??? pouce "Coup de pouce 2 (début de solution)"

    `somme = 0` ; `for i in range(n):` `if chiffres[i] == chiffres[(i + 1) % n]:` alors `somme += int(chiffres[i])`. On compare des caractères, on ne convertit qu’au moment d’additionner.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    Le système demande maintenant une vérification plus difficile. Même calcul, mais chaque chiffre est comparé au chiffre situé **une demi-longueur plus loin**, toujours en tournant en cercle (la longueur de la suite est paire). Autrement dit, sur le cercle, on compare chaque chiffre à celui qui lui fait face.

### <span class="exo-num">Exercice 6</span> — La partie 2 <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-algorithmique-le-parcours-sequentiel-aoc-2-6 }

Écrire une fonction `captcha2(chiffres)`. Avec la nouvelle règle, les chaînes inventées `5225`, `123323` et `81358136` donnent respectivement `0`, `10` et `24`.

??? pouce "Coup de pouce"

    Seul l’indice du chiffre auquel on compare change. Pour une chaîne de longueur 6, à quel indice compare-t-on le chiffre d’indice 4 ? Le modulo sert encore.

??? pouce "Coup de pouce 2 (début de solution)"

    Le décalage vaut `n // 2` au lieu de 1 : on compare `chiffres[i]` et `chiffres[(i + n // 2) % n]`.

## Approfondissement

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 1 : une seule fonction, deux fois moins de calculs <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-algorithmique-le-parcours-sequentiel-aoc-2-7 }

1.  Écrire une fonction `captcha_decale(chiffres, decalage)` qui traite les deux parties (avec `decalage = 1`, puis `decalage = len(chiffres) // 2`).

2.  Dans la partie 2, sur `81358136`, écrire les couples comparés quand `i` parcourt seulement la première moitié (indices 0 à 3). Que remarque-t-on en comparant avec la réponse `24` ?

3.  Montrer qu’on peut ne parcourir que la première moitié de la chaîne et multiplier le résultat par 2. Écrire la fonction `captcha2_moitie(chiffres)`. A-t-on encore besoin du modulo ?

    ??? pouce "Coup de pouce"

        Si le chiffre d’indice `i` est égal à celui d’indice `i + n // 2`, que se passe-t-il quand on arrive à l’indice `i + n // 2` ?

    ??? pouce "Coup de pouce 2 (début de solution)"

        Pour `i` de 0 à `n // 2 - 1`, l’indice `i + n // 2` est toujours inférieur à `n`. Chaque couple trouvé sera rencontré une seconde fois dans l’autre moitié, avec la même valeur.

## <span class="etiquette">Défi 3</span> Red-Nosed Reports

*les relevés du réacteur — suites croissantes ou décroissantes*

<p class="infos-activite">Jour 2</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/04-defi-aoc-2024-02){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/premiere-04-defi-aoc-2024-02.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2024/day/2 ](https://adventofcode.com/2024/day/2 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (facultatif), le lien *get your puzzle input* donne **vos** données, à enregistrer sous `input.txt` à côté du programme. Sans compte : le dossier du défi (<https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/04-defi-aoc-2024-02>) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

*Ce défi réinvestit le parcours séquentiel vu dans ce chapitre, avec l’idée de s’arrêter dès qu’un élément ne convient pas.*

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|                    |                    |              |                    |
|:-------------------|:-------------------|:-------------|:-------------------|
| report             | relevé (une ligne) | level        | niveau (un nombre) |
| safe / unsafe      | sûr / dangereux    | adjacent     | voisin, consécutif |
| increasing         | croissant          | decreasing   | décroissant        |
| gradually          | progressivement    | to differ by | différer de        |
| at least / at most | au moins / au plus | to tolerate  | tolérer            |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Dans une centrale nucléaire du pôle Nord, les ingénieurs vous demandent d’analyser des relevés étranges du réacteur. Chaque relevé est une suite de mesures (des « niveaux »). Le réacteur ne supporte que des niveaux qui évoluent régulièrement, sans à-coups : il faut repérer les relevés rassurants.

    **Ce qu’il faut faire.**

    - Chaque ligne est un relevé : des entiers séparés par une espace. Le nombre de niveaux varie d’une ligne à l’autre.

    - Un relevé est **sûr** si deux conditions sont vraies à la fois. Première condition : les niveaux sont tous croissants ou tous décroissants. Seconde condition : deux niveaux voisins diffèrent d’**au moins 1** et d’**au plus 3**.

    - Autrement dit, d’un niveau au suivant, le relevé avance toujours dans le même sens, par petits pas, sans jamais stagner.

    - La réponse est le nombre de relevés sûrs.

### <span class="exo-num">Exercice 1</span> — Vérifier sa compréhension <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-algorithmique-le-parcours-sequentiel-aoc-3-1 }

Questions pièges, à traiter sur le cahier :

1.  Un relevé qui contient deux niveaux voisins égaux peut-il être sûr ?

2.  Les relevés `5 4 3 2 1` et `1 4 7 10` sont-ils sûrs ? Et `1 5 6` ?

3.  Un relevé qui monte puis redescend, avec des écarts de 1, est-il sûr ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-algorithmique-le-parcours-sequentiel-aoc-3-2 }

On considère les relevés (inventés) suivants :

```console
2 4 5 7 8
9 8 4 3 1
1 2 2 3 5
6 5 7 8 9
10 7 4 1 0
3 8 9 10 11
1 5 9 10
```

Pour chaque relevé, écrire la liste des écarts entre niveaux voisins (par exemple `+2`, `-4`…), puis dire s’il est sûr. Vérification : on doit trouver `2` relevés sûrs.

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Lire un relevé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-algorithmique-le-parcours-sequentiel-aoc-3-3 }

Écrire une fonction `lire_releve(ligne)` qui renvoie la liste des entiers d’une ligne. Exemple : `lire_releve("1 5 9 10")` renvoie `[1, 5, 9, 10]`.

??? pouce "Coup de pouce"

    `ligne.split()`, puis une boucle qui convertit chaque morceau avec `int` et l’ajoute à une liste.

### <span class="exo-num">Exercice 4</span> — Les écarts <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-algorithmique-le-parcours-sequentiel-aoc-3-4 }

Écrire une fonction `ecarts(releve)` qui renvoie la liste des écarts entre niveaux voisins. Exemple : `ecarts([9, 8, 4, 3, 1])` renvoie `[-1, -4, -1, -2]`.

??? pouce "Coup de pouce"

    Pour une liste de $n$ niveaux, il y a $n - 1$ écarts : `releve[i + 1] - releve[i]` pour `i` de 0 à $n - 2$.

### <span class="exo-num">Exercice 5</span> — Sûr ou non <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-algorithmique-le-parcours-sequentiel-aoc-3-5 }

Écrire une fonction `est_sur(releve)` qui renvoie `True` ou `False`, puis compter les relevés sûrs de l’exemple et de vos données.

??? pouce "Coup de pouce"

    Le relevé est sûr si **tous** les écarts sont entre 1 et 3, ou bien si **tous** sont entre $-3$ et $-1$. Écrire deux petites fonctions qui parcourent les écarts et renvoient `False` dès qu’un écart ne convient pas.

??? pouce "Coup de pouce 2 (début de solution)"

    `def tous_entre(liste, mini, maxi):` parcourt la liste et renvoie `False` dès qu’un élément sort de l’intervalle, `True` à la fin de la boucle. Alors `est_sur` renvoie `tous_entre(e, 1, 3) or tous_entre(e, -3, -1)` où `e = ecarts(releve)`.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    Les ingénieurs signalent que le réacteur dispose d’un « amortisseur » capable d’ignorer une seule mesure aberrante. Un relevé compte donc maintenant aussi comme sûr s’il devient sûr quand on lui retire **un seul** de ses niveaux, n’importe lequel. La réponse est le nouveau nombre de relevés sûrs.

### <span class="exo-num">Exercice 6</span> — En retirant un niveau <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-algorithmique-le-parcours-sequentiel-aoc-3-6 }

Sur l’exemple de la fiche, on doit maintenant trouver `5` relevés sûrs : pour chacun des trois relevés qui deviennent sûrs, dire quel niveau on retire.

1.  Écrire une fonction `sans(releve, i)` qui renvoie une **nouvelle** liste, copie de `releve` sans l’élément d’indice `i`, sans modifier `releve`.

2.  Écrire une fonction `est_sur2(releve)` qui essaie toutes les possibilités, puis répondre à la partie 2.

??? pouce "Coup de pouce"

    Le découpage `releve[:i]` donne les éléments avant l’indice `i`, `releve[i + 1:]` ceux après. On peut coller deux listes avec `+`. Attention : `del` ou `pop` modifieraient la liste d’origine.

??? pouce "Coup de pouce 2 (début de solution)"

    `est_sur2` renvoie `True` si `est_sur(releve)`, ou si `est_sur(sans(releve, i))` pour au moins un indice `i` (boucle sur `range(len(releve))` avec un `return True` dès que ça marche).

## Approfondissement

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 1 : combien de calculs ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-algorithmique-le-parcours-sequentiel-aoc-3-7 }

Un relevé a au plus 8 niveaux et le fichier compte 1000 lignes. Combien d’appels à `est_sur` fait la méthode de la partie 2 au pire ? Pourquoi cette « force brute » est-elle ici tout à fait raisonnable ? Que se passerait-il avec des relevés de 100 000 niveaux ?

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 8</span> — Approfondissement 2 : ne pas tout essayer <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-04-algorithmique-le-parcours-sequentiel-aoc-3-8 }

On fixe d’abord le sens : croissant (`sens = 1`) ou décroissant (`sens = -1`). Un écart `d` convient si `1 <= d * sens <= 3`.

1.  Écrire une fonction `premier_defaut(releve, sens)` qui renvoie le premier indice `i` tel que l’écart entre `releve[i]` et `releve[i + 1]` ne convient pas, ou $-1$ s’il n’y en a pas.

2.  Sur `6 5 7 8 9` avec `sens = 1`, que renvoie `premier_defaut` ? Quel niveau faut-il retirer pour que le relevé devienne croissant ?

3.  Justifier : si le premier défaut est en `i`, alors pour réparer le relevé dans ce sens, il faut forcément retirer `releve[i]` ou `releve[i + 1]`.

    ??? pouce "Coup de pouce"

        Si l’on retire un autre niveau, les niveaux d’indices `i` et `i + 1` restent voisins, et leur écart ne convient toujours pas.

4.  En déduire une fonction `est_sur2_rapide(releve)` qui fait au plus quelques appels à `premier_defaut`, quel que soit le nombre de niveaux. Vérifier qu’elle donne les mêmes résultats que `est_sur2` sur tout le fichier.

    ??? pouce "Coup de pouce 2 (début de solution)"

        Pour chacun des deux sens : si `premier_defaut` renvoie $-1$, le relevé est sûr ; sinon, tester `sans(releve, i)` et `sans(releve, i + 1)` dans ce même sens.
