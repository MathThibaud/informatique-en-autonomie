# Défis Advent of Code

<p class="sous-titre">Récursivité</p>

## <span class="etiquette">Défi</span> Handy Haversacks

*les sacs emboîtés — dictionnaires et récursivité*

<p class="infos-activite">Jour 7</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/01-defi-aoc-2020-07){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-01-defi-aoc-2020-07.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/7 ](https://adventofcode.com/2020/day/7 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (lien ci-dessus) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

!!! encadre "Le défi en bref"

    **Le problème.** Un règlement impose le contenu de chaque couleur de sac : tel sac doit contenir tant de sacs de telle couleur, qui doivent à leur tour en contenir d’autres. Avec près de six cents règles, il faut savoir quelles couleurs peuvent, au bout du compte, renfermer le sac doré du héros, puis combien de sacs ce sac doré doit contenir en tout. Les emboîtements sont trop profonds et trop nombreux pour être suivis à la main.

    **Ce qu’on réinvestit.** La **récursivité** vue dans ce chapitre : un sac contient des sacs, qui contiennent eux-mêmes des sacs… La question posée pour un sac (« contient-il le sac doré ? », « combien de sacs contient-il ? ») se ramène à la même question posée pour les sacs qu’il contient. Une fonction récursive traduit directement ce raisonnement ; le sac vide fournit la condition d’arrêt.

    **La démarche de la fiche.**

    1.  Comprendre ce qu’on cherche, puis dessiner les règles d’un petit exemple sous forme de schéma fléché.

    2.  Traduire les règles du fichier en un dictionnaire de dictionnaires.

    3.  Écrire une fonction récursive qui dit si une couleur peut contenir le sac doré : c’est la partie 1.

    4.  Partie 2 : une seconde fonction récursive, qui suit les règles dans l’autre sens et compte les sacs.

    5.  En approfondissement, inverser les règles, puis dresser l’inventaire du sac doré et compter les appels récursifs.

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| bag | sac | rule | règle |
| contain | contenir | no other bags | aucun autre sac (sac vide) |
| outermost | le plus à l’extérieur | eventually | au bout du compte, indirectement |
| color-coded | repéré par une couleur | shiny gold | or brillant |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Escale à l’aéroport : un nouveau règlement impose des sacs repérés par leur couleur, et chaque couleur de sac doit contenir un nombre précis de sacs d’autres couleurs. Le héros possède un sac `shiny gold` (or brillant) et se demande dans quels sacs il pourrait le ranger.

    **Les données.** Chaque ligne du fichier est une règle qui décrit le contenu imposé d’une couleur de sac.

    - Une règle a la forme <code>&lt;couleur&gt; bags contain &lt;n&gt; &lt;couleur&gt; bag(s), ...</code> ou bien <code>&lt;couleur&gt; bags contain no other bags.</code> (sac vide).

    - Une couleur s’écrit en deux mots (`dull lime`) ; on lit `bag` ou `bags` selon le nombre, et la ligne se termine par un point.

    - Chaque couleur possède exactement une règle.

    **La règle.**

    - Les sacs s’emboîtent : un sac contient des sacs, qui en contiennent d’autres, etc.

    - On cherche les couleurs dont un sac contient au moins un sac `shiny gold`, directement ou à l’intérieur d’autres sacs, à n’importe quelle profondeur.

    - Seule la possibilité compte : une couleur qui contient plusieurs sacs dorés n’est comptée qu’une fois, et les quantités ne jouent aucun rôle.

    - `shiny gold` ne se compte pas lui-même.

    **La réponse attendue.** Le nombre de ces couleurs. Par exemple, si un sac A contient un sac B, qui contient lui-même un sac doré, alors A et B comptent tous les deux : la réponse serait 2.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-recursivite-aoc-1-1 }

**But.** Vérifier qu’on a compris ce qui fait compter une couleur, et repérer ce qu’il faut extraire d’une ligne.

**À quoi ça sert ?** La première question fait apparaître l’emboîtement à plusieurs niveaux, donc la récursivité ; la deuxième précise qu’on compte des couleurs et non des sacs ; la troisième prépare la lecture des règles.

Après lecture de l’énoncé et du résumé, vérifier sa compréhension :

1.  Si un sac A contient un sac B qui contient un sac `shiny gold`, la couleur de A compte-t-elle ?

2.  Une couleur dont un sac contient 5 sacs `shiny gold` compte-t-elle 5 fois ?

3.  Quels morceaux d’une ligne faut-il écarter pour ne garder que des nombres et des couleurs ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-recursivite-aoc-1-2 }

**But.** Représenter les règles par un schéma fléché, puis répondre à la partie 1 en remontant les flèches.

**À quoi ça sert ?** Le schéma rend visibles les emboîtements que le programme devra parcourir, et l’on obtient un exemple dont on **connaît la réponse** (`3`) pour tester les fonctions.

On considère les règles (inventées) suivantes :

```console
pale cyan bags contain 2 shiny gold bags, 1 dull lime bag.
striped coral bags contain 1 pale cyan bag.
dull lime bags contain no other bags.
shiny gold bags contain 3 dull lime bags, 2 wavy ochre bags.
wavy ochre bags contain 4 dull lime bags.
clear navy bags contain 5 wavy ochre bags.
bold mauve bags contain 1 striped coral bag, 2 clear navy bags.
```

Faire un schéma : écrire chaque couleur, et tracer une flèche de $A$ vers $B$, étiquetée $n$, si un sac $A$ contient $n$ sacs $B$. Répondre à la partie 1 en remontant les flèches depuis `shiny gold`. Vérification : on doit trouver `3`.

## Programmer la partie 1

!!! encadre "Outil Python : tester le début ou la fin d’une chaîne avec une tranche"

    On compare une tranche au morceau cherché : `s[:n]` contient les `n` premiers caractères, `s[-n:]` les `n` derniers.

    ```python
    reste = "no other bags."
    print(reste[:8] == "no other")          # True : les 8 premiers caracteres
    print(reste[-1:] == ".")                # True : le dernier caractere
    print("2 dull lime bags"[:2] == "no")   # False
    ```

    **Intérêt.** Pour ne pas compter les caractères à la main, écrire `reste[:len("no other")] == "no other"`. Une tranche plus longue que la chaîne ne provoque pas d’erreur : elle s’arrête à la fin.

    **À essayer.** Que vaut `"bags"[:3] == "bag"` ? Et `"bag"[:4] == "bags"` ?

### <span class="exo-num">Exercice 3</span> — Les règles en dictionnaire <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-recursivite-aoc-1-3 }

**But.** Traduire chaque ligne du fichier en données Python : un dictionnaire qui associe à chaque couleur le contenu de son sac.

**À quoi ça sert ?** Le texte des règles est difficile à exploiter tel quel. Avec le dictionnaire `contenu`, on obtient en une instruction ce que contient un sac et en quelle quantité : les deux parties s’appuient dessus.

Écrire une fonction `lire_regle(ligne)` qui renvoie la couleur du contenant et un dictionnaire de son contenu, par exemple `("wavy ochre", {"dull lime": 4})`. Construire ensuite le dictionnaire `contenu` qui associe à chaque couleur le dictionnaire de son contenu (un dictionnaire de dictionnaires).

??? pouce "Coup de pouce"

    Couper d’abord sur `" bags contain "`. Si la suite commence par `"no other"`, le contenu est vide ; sinon, couper sur `", "` : chaque morceau commence par un nombre suivi de deux mots de couleur.

!!! encadre "Méthode : « tous » ou « au moins un », avec un booléen drapeau"

    Pour savoir si **tous** les éléments d’une collection vérifient une condition, ou si **au moins un** la vérifie, on utilise un booléen appelé « drapeau » : on lui donne une valeur de départ, et la boucle la change dès qu’elle rencontre un élément décisif.

    ```python
    notes = [12, 15, 9]
    tous_admis = True          # aucun contre-exemple pour l'instant
    for n in notes:
        if n < 10:
            tous_admis = False
    print(tous_admis)          # False : 9 ne convient pas
    un_tres_bien = False       # aucun exemple pour l'instant
    for n in notes:
        if n >= 15:
            un_tres_bien = True
    print(un_tres_bien)        # True : 15 convient
    ```

    **Intérêt.** Pour une collection vide, la boucle ne fait aucun tour : le drapeau garde sa valeur de départ (`True` pour « tous », `False` pour « au moins un »). Pour ne plus rien calculer une fois la réponse connue, on place le drapeau en tête de la condition, par exemple `if not un_tres_bien and n >= 15:` : quand le drapeau est déjà levé, Python n’évalue pas la suite du `and`.

    **À essayer.** Un drapeau `trouve` vaut `False` avant la boucle `for x in {}:` (un sac vide). Que vaut-il après ? Qu’en déduire pour un sac vide dans `peut_contenir` ?

### <span class="exo-num">Exercice 4</span> — Peut contenir le sac doré ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-recursivite-aoc-1-4 }

**But.** Écrire une fonction récursive qui dit si un sac d’une couleur donnée peut renfermer, à une profondeur quelconque, le sac doré.

**À quoi ça sert ?** En l’appelant pour chaque couleur et en comptant les réponses vraies, on obtient la réponse de la partie 1. C’est l’occasion de bien identifier le cas de base et l’appel récursif.

Écrire une fonction récursive `peut_contenir(couleur)` qui renvoie `True` si un sac de cette couleur contient, directement ou non, un sac `shiny gold`. Compter les couleurs concernées. Tester sur l’exemple du défi, puis sur vos données.

??? pouce "Coup de pouce"

    Cas de base : le contenu de `couleur` a `"shiny gold"` parmi ses clés. Sinon, il suffit qu’**un** des sacs contenus puisse lui-même le contenir.

??? pouce "Coup de pouce 2 (début de solution)"

    Le résultat est vrai si, pour au moins un sac `x` du contenu, `x` est le sac doré **ou** `peut_contenir(x)` est vrai : c’est un « au moins un », à calculer avec un drapeau (voir l’encadré). Un sac vide donne `False` : c’est la condition d’arrêt.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    **Ce qui change.** Le héros se rend compte que son sac doré, une fois rempli selon le règlement, va peser lourd. On ne cherche plus les sacs qui contiennent le sac doré, mais ce que le sac doré contient ; et cette fois, les quantités comptent.

    **La nouvelle règle.**

    - On compte tous les sacs qu’un sac `shiny gold` doit contenir, à tous les niveaux d’emboîtement.

    - On tient compte des quantités : si un sac contient 2 sacs B, et que chaque sac B contient d’autres sacs, il faut compter le contenu des deux sacs B.

    - Le sac doré lui-même ne compte pas.

    **La réponse attendue.** Le nombre total de sacs contenus dans le sac doré. Par exemple, si le sac doré contenait 2 sacs A, chacun contenant 3 sacs B vides, la réponse serait $2 + 2 \times 3 = 8$.

### <span class="exo-num">Exercice 5</span> — Dans l’autre sens <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-recursivite-aoc-1-5 }

**But.** Compter, par une seconde fonction récursive, tous les sacs contenus dans le sac doré.

**À quoi ça sert ?** C’est la réponse de la partie 2. Cette fois, on descend dans le contenu du sac doré et l’on tient compte des quantités : il faut bien compter chaque sac contenu, plus ce qu’il contient.

1.  Dans la partie 1, on cherchait des sacs « au-dessus » du sac doré. Dans quel sens suit-on maintenant les règles ?

2.  Écrire une fonction récursive qui répond à la question. Sur l’exemple du défi, on doit trouver `13`.

??? pouce "Coup de pouce"

    Un sac contenu compte-t-il lui-même, en plus de tout ce qu’il contient ?

??? pouce "Coup de pouce 2 (début de solution)"

    Pour un sac `A` qui contient `n` sacs `B` : ces `n` sacs comptent, et chacun d’eux apporte en plus tout son propre contenu. Le sac vide fournit le cas de base.

## Approfondissement

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 6</span> — Défi : dans l’autre sens <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-recursivite-aoc-1-6 }

**But.** Inverser les règles (qui contient qui ?) pour résoudre la partie 1 en partant du sac doré.

**À quoi ça sert ?** Au lieu de tester toutes les couleurs, on ne visite que celles qui mènent au sac doré. On retrouve la réponse de la partie 1, ce qui valide les deux versions l’une par l’autre.

Pour chaque couleur, construire la liste des couleurs qui la contiennent **directement** (dictionnaire `contenants`). Écrire ensuite une fonction récursive `ajouter_contenants(couleur, trouves)` qui ajoute à la liste `trouves`, sans doublon, toutes les couleurs qui contiennent `couleur`, directement ou non. En déduire la réponse de la partie 1 et la comparer à celle de la version précédente.

??? pouce "Coup de pouce"

    Sur l’exemple du défi, `contenants["shiny gold"]` vaut `["pale cyan"]` et `contenants["pale cyan"]` vaut `["striped coral"]`.

??? pouce "Coup de pouce 2 (début de solution)"

    Pour chaque couleur `c` de `contenants[couleur]` qui n’est pas encore dans `trouves` : l’ajouter, puis appeler la fonction sur `c`. La réponse est la longueur de `trouves`.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 1 : l’inventaire du sac doré <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-recursivite-aoc-1-7 }

**But.** Détailler le contenu du sac doré couleur par couleur, puis compter combien de fois la fonction récursive est appelée.

**À quoi ça sert ?** L’inventaire vérifie le total de la partie 2 de façon plus fine. Compter les appels montre que la récursivité naïve refait plusieurs fois les mêmes calculs, ce qui prépare la programmation dynamique.

1.  À la main, sur l’exemple du défi : combien de sacs de chaque couleur trouve-t-on, à tous les niveaux, dans un sac `shiny gold` ? Vérifier que le total redonne `13`.

2.  Écrire une fonction récursive `inventaire(couleur)` qui renvoie un dictionnaire associant à chaque couleur le nombre de sacs de cette couleur contenus dans un sac `couleur`.

3.  Combien de fois la fonction de la partie 2 est-elle appelée pour `dull lime` sur l’exemple ? Vérifier en comptant les appels dans un dictionnaire.

4.  On imagine des règles où chaque sac $c_i$ contient un sac $c_{i+1}$ et un sac $c_{i+2}$. Montrer que le nombre d’appels $A(i)$ pour $c_i$ vérifie $A(i) = 1 + A(i+1) + A(i+2)$. Quel exemple du cours sur la récursivité retrouve-t-on ? (Le chapitre sur la programmation dynamique montrera comment éviter ces recalculs.)

??? pouce "Coup de pouce"

    Un sac `A` qui contient `n` sacs `B` apporte `n` sacs `B`, plus `n` fois tout l’inventaire d’un sac `B`.

??? pouce "Coup de pouce 2 (début de solution)"

    Écrire une petite fonction `ajouter(total, couleur, nombre)` qui crée ou augmente l’entrée d’un dictionnaire ; `inventaire` parcourt `contenu[couleur].items()` et appelle `inventaire(x)` pour chaque sac contenu.
