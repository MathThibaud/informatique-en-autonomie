# Activités préparatoires

<p class="sous-titre">Spécifier et mettre au point ses programmes</p>

## <span class="etiquette">Activité 1</span> La chasse aux bugs

*faire échouer un programme qui « marche presque »*

<p class="infos-activite">Durée : 20 min · Sans ordinateur, par deux, crayon en main</p>

!!! consignes "Consignes"

    - Les réponses et les tableaux s’écrivent sur le cahier.

    - Un programmeur pressé a écrit deux fonctions. Il affirme : « je les ai essayées, elles marchent ». Vous êtes **testeurs** : votre mission est de les **faire échouer**.

    - Un **cas** se note en trois colonnes : ce qu’on donne à la fonction, ce qu’elle *devrait* renvoyer d’après la commande du client, ce qu’elle renvoie *vraiment* (obtenu en exécutant le code à la main).

### <span class="exo-num">Exercice 1</span> — La mention au bac <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-act-1-1 }

La commande du client : « La fonction reçoit une note sur 20. Elle renvoie `"Tres bien"` à partir de 16, `"Bien"` à partir de 14, `"Assez bien"` à partir de 12, `"Admis"` à partir de 10 et `"Refuse"` en dessous de 10. »

```python
def mention(note):
    if note >= 16:
        return "Tres bien"
    elif note >= 14:
        return "Bien"
    elif note > 12:
        return "Assez bien"
    elif note >= 10:
        return "Admis"
    else:
        return "Refuse"
```

1.  Recopier sur le cahier le tableau suivant, en prévoyant une ligne par cas essayé.

    | **note donnée** | **résultat attendu** | **résultat obtenu** |
    |:----------------|:---------------------|:--------------------|
    | …               | …                    | …                   |

    Le programmeur a essayé les notes `17`, `15` et `8` : remplir les trois premières lignes du tableau. Ses essais prouvent-ils que la fonction est correcte ?

2.  Chercher une note **entre 0 et 20** pour laquelle la fonction se trompe, et l’ajouter au tableau. Quelle ligne du programme est en cause ?

3.  Si vous deviez n’essayer que cinq ou six notes, lesquelles choisiriez-vous pour avoir le plus de chances de débusquer ce genre d’erreur ? Pourquoi celles-là ?

4.  Que renvoient `mention(23)` et `mention(-5)` ? Est-ce la faute du programme ou de celui qui l’appelle ? Que vaudrait-il mieux que le programme fasse ?

??? corrige "Corrigé"

    **1.** `17` : attendu `"Tres bien"`, obtenu `"Tres bien"` ; `15` : `"Bien"` et `"Bien"` ; `8` : `"Refuse"` et `"Refuse"`. Les trois essais sont justes, mais ils ne prouvent **rien** : ils ne passent jamais par la branche `"Assez bien"`, ni près d’une frontière.

    **2.** `12` : attendu `"Assez bien"` (« à partir de 12 »), obtenu `"Admis"`. En cause : `elif note > 12:`, qui exclut $12$ ; il faut `>=`. Les notes strictement supérieures à $12$ sont bien traitées (`12.5` ou `13` donnent `"Assez bien"`) : seule la valeur exacte de la frontière révèle l’erreur.

    **3.** Les **valeurs limites** : $10$, $12$, $14$, $16$ (chaque frontière), plus les extrémités $0$ et $20$. Les erreurs se cachent presque toujours sur les frontières entre deux cas (`>` au lieu de `>=`), qu’un essai « au milieu » ne touche jamais.

    **4.** `mention(23)` renvoie `"Tres bien"` et `mention(-5)` renvoie `"Refuse"`, sans aucune alerte. C’est l’appel qui est fautif (la commande dit « une note sur 20 »), mais le programme le laisse passer en silence : il vaudrait mieux qu’il **refuse** une note hors de $[0 \,;\, 20]$, en s’arrêtant avec un message clair.

### <span class="exo-num">Exercice 2</span> — La moyenne d’une classe <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-act-1-2 }

La commande du client : « La fonction reçoit le tableau des notes d’une classe et renvoie leur moyenne. »

```python
def moyenne(notes):
    total = 0
    for i in range(1, len(notes)):
        total = total + notes[i]
    return total / len(notes)
```

1.  Le programmeur a essayé `moyenne([0, 10, 20])` et `moyenne([0, 0])`. Recopier sur le cahier le tableau suivant, exécuter ces deux appels à la main et le remplir.

    | **tableau donné** | **résultat attendu** | **résultat obtenu** |
    |:------------------|:---------------------|:--------------------|
    | …                 | …                    | …                   |

2.  Trouver un tableau pour lequel la fonction se trompe, et l’ajouter au tableau. Expliquer l’erreur en une phrase.

3.  Pourquoi les deux essais du programmeur n’avaient-ils rien révélé ?

4.  Que se passe-t-il lors de l’appel `moyenne([])` ? Que devrait prévoir la commande du client ?

??? corrige "Corrigé"

    **5.** `moyenne([0, 10, 20])` : la boucle additionne `notes[1]` et `notes[2]`, `total` vaut $30$, résultat $30 / 3 = 10{,}0$ (attendu $10$ : juste). `moyenne([0, 0])` : $0 / 2 = 0{,}0$ (juste).

    **6.** Par exemple `moyenne([10, 10])` : attendu $10$, obtenu $5{,}0$ (ou `moyenne([12, 14, 16])` : attendu $14$, obtenu $10{,}0$). La boucle commence à l’indice `1` : la **première note est oubliée** dans la somme, alors qu’on divise bien par le nombre total de notes. Il faut `range(len(notes))`.

    **7.** Dans les deux essais, la première note valait $0$ : l’oublier ne change pas la somme. Le programme a donné le bon résultat **par hasard**.

    **8.** `moyenne([])` provoque une **division par zéro** : comme `len(notes)` vaut $0$, Python s’arrête et signale l’erreur `ZeroDivisionError`. La commande devrait préciser ce qui est permis : « le tableau ne doit pas être vide » (ou bien ce que la fonction doit renvoyer dans ce cas).

### <span class="exo-num">Exercice 3</span> — Ce qu’on a découvert <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-act-1-3 }

1.  Recopier et compléter sur le cahier avec vos mots.

    - Un programme qui donne le bon résultat sur quelques essais …

    - Les cas qui font le plus souvent échouer un programme sont …

    - Pour savoir si un résultat est juste, il faut d’abord savoir précisément …

    - Refaire tous ces essais à la main après chaque correction est long : on aimerait …

??? corrige "Corrigé"

    **9.**

    - Un programme qui donne le bon résultat sur quelques essais **peut quand même être faux**.

    - Les cas qui font le plus souvent échouer un programme sont **les valeurs limites** (les frontières entre deux cas, les extrémités), **le tableau vide**, et les **données hors du domaine prévu**.

    - Pour savoir si un résultat est juste, il faut d’abord savoir précisément **ce que la fonction doit faire, et pour quelles données** (la commande du client).

    - Refaire ces essais à la main est long : on aimerait **les écrire une fois pour toutes, et que la machine les vérifie** à chaque modification.
