# Réussir la partie écrite

!!! encadre "Le cadre"

    En **juin**, **3 h 30**, notée sur **12**. Avec la partie pratique (1 h sur machine, notée sur 8), elle forme l’épreuve de spécialité, de coefficient **16**. Le sujet comporte **trois exercices indépendants**, chacun annoncé par les notions qu’il mobilise ; le barème de chaque exercice est indiqué sur le sujet. Calculatrice interdite : on calcule à la main, on raisonne en ordres de grandeur. Tout se fait **sans machine** : le code s’écrit et se teste sur papier.

### Lire le sujet et choisir l’ordre (10 minutes)

1.  **Survoler les trois exercices** : lire leurs titres, les notions annoncées, et souligner les questions que l’on sait traiter tout de suite.

2.  **Repérer les annexes** (à rendre avec la copie) et les **fonctions fournies** : l’énoncé les donne pour qu’on s’en serve.

3.  **Choisir l’ordre** : commencer par l’exercice où l’on est le plus à l’aise, pour sécuriser des points et prendre confiance. On peut traiter les exercices dans n’importe quel ordre, à condition de les **numéroter clairement**.

4.  **Ne jamais abandonner un exercice** : les questions de la fin sont souvent indépendantes, et une question non résolue peut être **admise** pour traiter la suivante.

### Gérer 3 h 30

|  | **Lecture** | **1<sup>er</sup> exercice** | **2<sup>e</sup> exercice** | **3<sup>e</sup> exercice** | **Relecture** |
|:---|:--:|:--:|:--:|:--:|:--:|
| Durée indicative | 10 min | $\approx$ 60 min | $\approx$ 60 min | $\approx$ 65 min | 15 min |

**Repère** : environ **10 minutes par point** de barème. Bloqué plus de **5 minutes** sur une question ? La marquer d’une croix dans la marge, passer à la suivante, y revenir à la fin. Dès qu’un exercice dépasse son temps de plus de 15 minutes, passer au suivant.

### Écrire du code sur papier

- **Indentation visible** : décaler nettement chaque bloc (au besoin, tracer au crayon un trait vertical sous chaque `for`, `if`, `def`).

- **Respecter la signature** imposée (nom de la fonction, ordre des paramètres) et choisir des **noms explicites** pour ses variables.

- **« Compléter »** : ne recopier que les lignes à trous, avec leur numéro.

- **Tester mentalement** sur un petit exemple *et* sur un cas limite (liste vide, un seul élément, valeurs négatives), puis **tracer** les variables dans un tableau.

**Exemple corrigé.** « Écrire une fonction `maximum(tab)` qui renvoie le plus grand élément d’une liste non vide d’entiers. »

*Copie à corriger :*

```python
def maximum(tab):
    m = 0
    for x in tab:
        if x > m:
            m = x
    print(m)
```

*Version juste :*

```python
def maximum(tab):
    m = tab[0]       # la liste est non vide
    for x in tab:
        if x > m:
            m = x
    return m
```

Deux erreurs : `print` n’est pas `return` (la copie renvoie `None`) ; `m = 0` donne un résultat faux pour `[-3, -1, -7]` (la copie affiche `0`, la version juste renvoie `-1`). **Trace** de `maximum([4, 9, 2])` :

| `x` |  —  | `4` | `9` | `2` |
|:---:|:---:|:---:|:---:|:---:|
| `m` | `4` | `4` | `9` | `9` |

renvoie `9`.

### Rédiger une justification

Une justification est une **phrase complète** qui cite le code ou le cours. Trois modèles, sur la boucle ci-contre.

```python
def nb_tours(n):
    tours = 0
    while n > 0:
        n = n // 2
        tours = tours + 1
    return tours
```

- **Terminaison** (un *variant*) : « `n` est un entier positif ou nul qui **diminue strictement** à chaque tour, car `n // 2 < n` dès que `n` $\geqslant 1$ ; il finit par valoir $0$ et la condition `n > 0` devient fausse. »

- **Coût** : « `n` est divisé par $2$ à chaque tour : `nb_tours(1000)` fait $10$ tours ($1000 \to 500 \to \dots \to 1 \to 0$). Le nombre de tours est de l’ordre de $\log_2 n$ : le coût est **logarithmique**. »

- **Correction** (un *invariant*, pour `maximum`) : « à la fin de chaque tour, `m` est le plus grand des éléments déjà parcourus ; après le dernier tour, c’est donc le plus grand de toute la liste. »

### Les verbes de consigne

| **Verbe** | **Ce qui est attendu** | **Exemple de réponse** |
|:---|:---|:---|
| **Donner**, **indiquer** | La réponse seule suffit. | « La clé primaire est `id`. » |
| **Justifier** | La réponse *et* sa raison, tirée du code, de l’énoncé ou du cours. | « Non : deux lignes ont la valeur `3` pour `num`, qui ne peut donc pas être une clé primaire. » |
| **Expliquer** | Le mécanisme ou le pourquoi, en phrases. | « La pile rend d’abord le dernier élément empilé, donc… » |
| **Écrire** | Le code complet (fonction, requête, classe), qui respecte la signature imposée. | Une fonction entière, indentée, avec son `return`. |
| **Compléter** | Uniquement les parties manquantes, repérées par leur numéro de ligne. | « Ligne 4 : `return 0` ». |
| **Déterminer**, **calculer** | Le résultat *et* la démarche qui y mène. | Un calcul posé, une trace. |

### Les erreurs qui coûtent des points

- **`print` au lieu de `return`** : la fonction doit *renvoyer* sa valeur (voir l’exemple de `maximum`).

- **Oublier la condition d’arrêt** d’une fonction récursive ou un **cas limite** (liste vide, arbre vide `None`).

- **`=` au lieu de `==`** dans un test ; **indices hors limites** : le dernier indice de `t` est `len(t) - 1`.

- **Ignorer la convention de l’énoncé** (hauteur d’un arbre, sens d’une pile, coût OSPF) : on applique *celle du sujet*.

- **SQL** : oublier la condition `ON` d’une jointure ou les apostrophes autour d’une chaîne (`WHERE nom = ’Durand’`).

- **Répondre sans justifier** quand le verbe est « justifier » ou « expliquer » : la réponse seule rapporte peu, voire rien.

- **Laisser une question blanche** : une démarche partielle juste, une idée bien exprimée rapportent des points.

- **Une copie illisible** : code mal indenté, numéros de questions absents, ratures partout. Le correcteur ne devine pas.
