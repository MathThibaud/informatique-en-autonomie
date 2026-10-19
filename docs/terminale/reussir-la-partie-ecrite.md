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

**Repère** : le sujet est barémé sur **20** (en général $6$, $6$ et $8$ points), puis la note est ramenée sur $12$. Une fois la lecture et la relecture mises de côté, il reste un peu plus de 3 h, soit environ **9 minutes par point** de ce barème : l’exercice sur $8$ points mérite un peu plus de temps que les deux autres. Bloqué plus de **5 minutes** sur une question ? La marquer d’une croix dans la marge, passer à la suivante, y revenir à la fin. Dès qu’un exercice dépasse son temps de plus de 15 minutes, passer au suivant.

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

### Un calendrier de révision, d’avril à juin

Les dix semaines qui précèdent l’écrit se préparent. Le principe : revoir chaque chapitre **plusieurs fois, à quelques semaines d’intervalle**, plutôt qu’une seule fois longuement. C’est cette **révision espacée** qui fait tenir les connaissances jusqu’au jour de l’épreuve. Comptez **3 à 4 heures par semaine**, en plusieurs séances courtes (un peu plus pendant les deux dernières). Dans le tableau, S-10 désigne la dixième semaine avant l’écrit, S-1 la dernière ; les autres mots employés sont expliqués juste en dessous.

<table>
<thead>
<tr>
<th style="text-align: left;"><strong>Semaine</strong></th>
<th style="text-align: left;"><strong>Chapitres</strong></th>
<th style="text-align: left;"><strong>Écrit</strong></th>
<th style="text-align: left;"><strong>Pratique et Grand Oral</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><strong>S-10</strong></td>
<td style="text-align: left;"><strong>À fond</strong> : 1 Récursivité ; 2 POO</td>
<td style="text-align: left;">Type bac ch. 1</td>
<td style="text-align: left;">GO : choisir vos deux questions, formuler chacune en une phrase</td>
</tr>
<tr>
<td style="text-align: left;"><strong>S-9</strong></td>
<td style="text-align: left;"><strong>À fond</strong> : 3 Piles, files, listes chaînées ; 4 Processus<br />
<strong>Rappel</strong> : 1</td>
<td style="text-align: left;">Type bac ch. 3 ; synthèse 1 à 3</td>
<td style="text-align: left;">Pratique : sujet 27<br />
GO : problématique et plan de la question 1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>S-8</strong></td>
<td style="text-align: left;"><strong>À fond</strong> : 5 Arbres<br />
<strong>Rappel</strong> : 2, 3</td>
<td style="text-align: left;">Type bac ch. 5 ; synthèse 5</td>
<td style="text-align: left;">Pratique : sujets 24 et 25<br />
GO : exemple déroulé et schéma de la question 1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>S-7</strong></td>
<td style="text-align: left;"><strong>À fond</strong> : 6 Bases de données ; 7 Diviser pour régner<br />
<strong>Rappel</strong> : 1, 4</td>
<td style="text-align: left;">Type bac ch. 6 (SQL)</td>
<td style="text-align: left;">Pratique : sujet 29<br />
GO : problématique et plan de la question 2</td>
</tr>
<tr>
<td style="text-align: left;"><strong>S-6</strong></td>
<td style="text-align: left;"><strong>À fond</strong> : 8 Graphes<br />
<strong>Rappel</strong> : 3, 5</td>
<td style="text-align: left;">Type bac ch. 8 ; synthèse 6 à 8</td>
<td style="text-align: left;">Pratique : sujets 26 et 28<br />
GO : exemple déroulé et schéma de la question 2</td>
</tr>
<tr>
<td style="text-align: left;"><strong>S-5</strong></td>
<td style="text-align: left;"><strong>À fond</strong> : 9 Réseaux ; 10 Cryptographie<br />
<strong>Rappel</strong> : 2, 6</td>
<td style="text-align: left;">Type bac ch. 9 ou 10 ; synthèse 9 et 10</td>
<td style="text-align: left;">Pratique : sujet 30<br />
GO : chaque exposé à voix haute, chronométré (10 min), avec vos seules notes</td>
</tr>
<tr>
<td style="text-align: left;"><strong>S-4</strong></td>
<td style="text-align: left;"><strong>À fond</strong> : 11 Programmation dynamique ; 12 Recherche textuelle<br />
<strong>Rappel</strong> : 7, 8</td>
<td style="text-align: left;">Type bac ch. 11 ou 12</td>
<td style="text-align: left;">Pratique : sujet 32<br />
GO : trois relances par question, avec vos réponses</td>
</tr>
<tr>
<td style="text-align: left;"><strong>S-3</strong></td>
<td style="text-align: left;"><strong>À fond</strong> : 13 Calculabilité ; 14 Systèmes sur puce<br />
<strong>Rappel</strong> : 4, 9, 10</td>
<td style="text-align: left;">Type bac ch. 13 ou 14 ; synthèse 11 à 14</td>
<td style="text-align: left;">Pratique : sujet 31<br />
GO : exposés devant un camarade, avec la grille entre camarades</td>
</tr>
<tr>
<td style="text-align: left;"><strong>S-2</strong></td>
<td style="text-align: left;"><strong>Rappel</strong> : 1 à 7</td>
<td style="text-align: left;">Un <strong>sujet complet</strong> (3 exercices, 3 h 30) en conditions réelles, puis sa correction</td>
<td style="text-align: left;">GO : un oral blanc complet (20 min de préparation, 10 min d’exposé, 10 min d’échange)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>S-1</strong></td>
<td style="text-align: left;"><strong>Rappel</strong> : 8 à 14</td>
<td style="text-align: left;">Deux exercices type bac sur vos chapitres les moins sûrs ; relire votre liste d’erreurs. Rien de nouveau les deux derniers jours</td>
<td style="text-align: left;">GO : relire vos deux plans, sans plus</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Épreuve pratique</strong></td>
<td style="text-align: left;">Notions de Première et POO (ch. 2), les plus fréquentes à l’épreuve ; puis vos chapitres les moins sûrs</td>
<td colspan="2" style="text-align: left;">Les jours qui la précèdent (avant ou après l’écrit, selon le calendrier de l’année) : deux ou trois sujets en 1 h chrono, dont les sujets 24 à 32 pas encore faits ; relire la fiche « Réussir l’épreuve pratique ».</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Grand Oral</strong></td>
<td style="text-align: left;">Les chapitres de vos deux questions</td>
<td colspan="2" style="text-align: left;">Après l’écrit, chaque jour : un exposé de 10 minutes par question, chronométré, en partant de notes préparées en 20 minutes ; revoir les relances.</td>
</tr>
</tbody>
</table>

**Les mots du tableau**

- **À fond** : le chapitre est revu avec sa **fiche de révision** (liste « Savoir-faire », puis « Se tester » de mémoire) ; pour chaque savoir-faire mal maîtrisé, refaire un exercice $\bullet$ essentiel.

- **Rappel** : 15 minutes par chapitre, livre fermé, avec les questions « Se tester » et « Et avant ? » de sa fiche.

- **Type bac** : un exercice type bac du chapitre, **chronométré** à la durée indiquée à côté de son titre (de 15 à 60 minutes), puis corrigé.

- **Synthèse** : un problème de synthèse (fin de la première partie du livre), choisi dans la rubrique indiquée (« 1 à 3 » renvoie à « Après les chapitres 1 à 3 »).

- **Pratique** : un sujet d’épreuve pratique de la deuxième partie du livre (sujets 24 à 32), en 1 h sur machine ; **GO** : Grand Oral.

**Cinq conseils de méthode**

- **Un planning réaliste.** Reportez le tableau dans votre agenda en tenant compte de vos autres matières et des vacances : quatre séances courtes valent mieux qu’une longue, toujours repoussée. Une semaine a sauté ? Ne rattrapez pas tout : décalez la suite, mais gardez les rappels.

- **Des sujets complets, en conditions réelles.** Au moins un sujet entier (deux, c’est mieux), d’une traite, en 3 h 30, sans cours, sans machine ni IA, en suivant la gestion du temps présentée plus haut. Les vacances de printemps s’y prêtent bien.

- **Corriger avec le corrigé du livre**, d’une autre couleur : comparer point par point, noter ce qui manque (une justification, un cas limite, un `return`), lire les *erreurs fréquentes* signalées. Le corrigé ne se lit qu’après avoir vraiment cherché.

- **Refaire ses erreurs.** Tenez une liste « mes erreurs » (une ligne par erreur : chapitre, exercice, ce qu’il fallait faire) et refaites chaque exercice raté une semaine plus tard, sans regarder le corrigé. C’est cette liste que l’on relit la veille de l’épreuve.

- **Se tester plutôt que relire.** Livre fermé : répondre aux questions « Se tester », écrire le code sur papier avant de le taper, dérouler un algorithme à la main. Relire donne l’impression de savoir ; se tester montre ce que l’on sait vraiment.
