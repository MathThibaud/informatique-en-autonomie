# Cours

<p class="sous-titre">Les algorithmes de tri</p>

<span id="chap-06" class="ancre"></span>

|  |  |
|:---|:---|
| **Programme (BO)** | *« Algorithmes sur les tableaux »* : *tri par insertion*, *tri par sélection* ; *coût* d’un tri (coût *quadratique*). |
| **Prérequis** | les boucles `for`/`while`, les tableaux (indices, `len`), et surtout le chapitre **« Algorithmique : le parcours séquentiel »** : patron du parcours, invariant de boucle, coûts linéaire et quadratique. (→ fiches de révision : ch. 4) |
| **Objectifs** | comprendre *pourquoi* on trie ; connaître et savoir écrire **deux** algorithmes de tri (sélection, insertion) ; **tracer** leur exécution ; **évaluer leur coût** et les comparer. |

!!! situation "Situation de départ"

    1.  Pourquoi prendre la peine de ranger une liste dans l’ordre, si c’est seulement pour y chercher ensuite ?

    2.  Pour ranger un paquet de cartes, vaut-il mieux chercher à chaque fois la plus petite carte restante, ou glisser chaque nouvelle carte à sa place dans la main ?

    3.  Ranger 1 000 fois plus de cartes demande-t-il 1 000 fois plus de travail ?

!!! remarque "Remarque — Une histoire de rangement — et de vitesse"

    Un annuaire de dix millions de noms qui ne serait pas trié serait *inutilisable* : on ne retrouverait jamais personne. Trier, c’est **préparer les données** pour qu’on puisse ensuite y chercher, compter, comparer… à toute vitesse. C’est l’une des opérations les plus exécutées au monde : chaque tri de colonne dans un tableur, chaque classement de résultats d’un moteur de recherche, chaque « trier par date » de vos messages en déclenche un. Dans ce chapitre, on ouvre le capot. On y retrouvera notre question fétiche : **combien ça coûte ?** Les points qui dépassent le programme sont signalés par le badge <span class="horsprog">au-delà du programme</span>.

## Pourquoi trier ?

Trier un tableau, c’est ranger ses éléments **dans l’ordre** (croissant, le plus souvent). Cela paraît anodin, mais un tableau trié devient une donnée bien plus **puissante** :

- **chercher devient fulgurant** : dans une liste triée on pourra faire une *recherche dichotomique* (chapitre suivant, *La recherche dichotomique*), incomparablement plus rapide qu’un parcours ;

- **le plus petit / le plus grand** sont aux deux bouts ; la **médiane** est au milieu ;

- les **doublons** se retrouvent *côte à côte*, donc faciles à détecter ;

- **fusionner** deux listes déjà triées, ou **afficher** un classement, devient immédiat.

!!! regle "Règle 1 — L’idée-force"

    On ne trie pas pour le plaisir de ranger : on trie **une fois** pour ensuite chercher, comparer et calculer **beaucoup plus vite**. Le tri est un *investissement*.

!!! definition "Définition 1 — Le problème du tri"

    **Trier** un tableau `t`, c’est réorganiser ses éléments de sorte que $$\texttt{t[0]} \leq \texttt{t[1]} \leq \texttt{t[2]} \leq \cdots \leq \texttt{t[n-1]}.$$ On travaillera **en place** : on réarrange le tableau donné, sans en créer un nouveau. Les seules opérations autorisées sont **comparer** deux éléments et les **échanger** (ou les déplacer).

!!! encadre "À retenir — Deux opérations à compter"

    Pour mesurer le coût d’un tri, on compte deux choses : le nombre de **comparaisons** (`t[j] < t[i]` ?) et le nombre d’**échanges**. C’est là que se joue la rapidité de l’algorithme.

!!! regle "Règle 2 — Échanger : le piège de la variable perdue"

    Pour échanger le contenu de deux cases `t[i]` et `t[j]`, on **ne peut pas** écrire naïvement :

    ```text
    t[i] = t[j]     # PERDU : l'ancienne valeur de t[i] est ecrasee...
    t[j] = t[i]     # ... donc ici, t[j] recopie la NOUVELLE valeur : rate !
    ```

    Il faut d’abord **mettre de côté** l’une des deux valeurs dans une **variable temporaire** :

    ```text
    temp = t[i]     # on sauvegarde t[i]
    t[i] = t[j]     # t[i] recoit t[j]
    t[j] = temp     # t[j] recoit l'ancienne valeur de t[i]
    ```

    C’est l’image des deux verres, l’un d’eau, l’autre de jus : pour intervertir leurs contenus, il faut un **troisième verre vide**. Cette variable temporaire est nécessaire dans la plupart des langages ; c’est la version que nous garderons.

!!! remarque "Remarque — En Python : l’échange en une ligne"

    L’affectation multiple du chapitre *Les types construits* permet aussi d’écrire `t[i], t[j] = t[j], t[i]` : Python évalue d’abord le p-uplet de droite (les deux *anciennes* valeurs), puis le déballe dans les deux cases. Aucune valeur n’est perdue. On rencontre cette forme dans des sujets de bac (par exemple le tri par insertion d’Amérique du Nord 2026, jour 2, exercice 2) : il faut savoir la lire.

## Le tri par sélection

**L’idée** est celle d’un joueur qui range sa main en la posant sur la table : *je cherche la plus petite carte de tout le paquet, je la mets en première position ; puis la plus petite du reste, en deuxième position ; et ainsi de suite.*

!!! regle "Règle 3 — Principe du tri par sélection"

    Pour chaque position `i` de gauche à droite : on **cherche le minimum** de la partie non encore triée (les cases d’indice `i` à la fin), puis on l’**échange** avec la case `i`. À la fin de l’étape, la case `i` contient sa valeur définitive.

<span class="retouract">↺ Retour sur l'activité.</span> La méthode 1 de l’activité « Trier sans tricher », « le plus petit d’abord », était déjà le tri par sélection : la carte « championne » est le minimum de la partie non encore triée.

```python
def tri_selection(t):
    """Trie le tableau t en place, dans l'ordre croissant."""
    n = len(t)
    for i in range(n):
        # 1. chercher l'indice du minimum dans la portion t[i:]
        i_min = i
        for j in range(i + 1, n):
            if t[j] < t[i_min]:
                i_min = j
        # 2. placer ce minimum en position i (echange via variable temporaire)
        temp = t[i]
        t[i] = t[i_min]
        t[i_min] = temp
```

!!! remarque "Remarque — On reconnaît deux vieilles connaissances"

    La boucle interne est *exactement* la recherche du **minimum** du chapitre *Algorithmique : le parcours séquentiel* (l’invariant du champion : `i_min` est l’indice du plus petit élément déjà vu). Ce minimum est ensuite « sélectionné » et rangé — d’où le nom.

### Dérouler l’algorithme

Traçons le tri de `[5, 3, 8, 1, 9, 2]`. Le tableau est montré **au début de chaque étape** : la zone `grisée` est **définitivement triée**, et on repère en `orange` le **minimum de la zone restante**, qu’on amène à sa place par un échange.

<table>
<thead>
<tr>
<th style="text-align: right;"><strong>étape</strong></th>
<th colspan="6" style="text-align: left;"><strong>tableau</strong></th>
<th style="text-align: left;"><strong>action</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: right;"><code>i</code>=0</td>
<td style="text-align: center;"><code>5</code></td>
<td style="text-align: center;"><code>3</code></td>
<td style="text-align: center;"><code>8</code></td>
<td style="text-align: center;"><code>1</code></td>
<td style="text-align: center;"><code>9</code></td>
<td style="text-align: center;"><code>2</code></td>
<td style="text-align: left;">min <span class="math inline"> = 1</span> (case 3) <span class="math inline">→</span> échange avec la case 0</td>
</tr>
<tr>
<td style="text-align: right;"><code>i</code>=1</td>
<td style="text-align: center;"><code>1</code></td>
<td style="text-align: center;"><code>3</code></td>
<td style="text-align: center;"><code>8</code></td>
<td style="text-align: center;"><code>5</code></td>
<td style="text-align: center;"><code>9</code></td>
<td style="text-align: center;"><code>2</code></td>
<td style="text-align: left;">min <span class="math inline"> = 2</span> (case 5) <span class="math inline">→</span> échange avec la case 1</td>
</tr>
<tr>
<td style="text-align: right;"><code>i</code>=2</td>
<td style="text-align: center;"><code>1</code></td>
<td style="text-align: center;"><code>2</code></td>
<td style="text-align: center;"><code>8</code></td>
<td style="text-align: center;"><code>5</code></td>
<td style="text-align: center;"><code>9</code></td>
<td style="text-align: center;"><code>3</code></td>
<td style="text-align: left;">min <span class="math inline"> = 3</span> (case 5) <span class="math inline">→</span> échange avec la case 2</td>
</tr>
<tr>
<td style="text-align: right;"><code>i</code>=3</td>
<td style="text-align: center;"><code>1</code></td>
<td style="text-align: center;"><code>2</code></td>
<td style="text-align: center;"><code>3</code></td>
<td style="text-align: center;"><code>5</code></td>
<td style="text-align: center;"><code>9</code></td>
<td style="text-align: center;"><code>8</code></td>
<td style="text-align: left;">min <span class="math inline"> = 5</span> : déjà en place</td>
</tr>
<tr>
<td style="text-align: right;"><code>i</code>=4</td>
<td style="text-align: center;"><code>1</code></td>
<td style="text-align: center;"><code>2</code></td>
<td style="text-align: center;"><code>3</code></td>
<td style="text-align: center;"><code>5</code></td>
<td style="text-align: center;"><code>9</code></td>
<td style="text-align: center;"><code>8</code></td>
<td style="text-align: left;">min <span class="math inline"> = 8</span> (case 5) <span class="math inline">→</span> échange avec la case 4</td>
</tr>
<tr>
<td style="text-align: right;">arrivée</td>
<td style="text-align: center;"><code>1</code></td>
<td style="text-align: center;"><code>2</code></td>
<td style="text-align: center;"><code>3</code></td>
<td style="text-align: center;"><code>5</code></td>
<td style="text-align: center;"><code>8</code></td>
<td style="text-align: center;"><code>9</code></td>
<td style="text-align: left;">tableau trié</td>
</tr>
</tbody>
</table>

La même trace en **histogramme** : chaque barre a la hauteur de sa valeur. On voit la zone triée (colorée) grandir d’une barre à chaque étape, en partant de la gauche, et le minimum (orange) venir prendre sa place par un échange (flèche).

![](../figures/6d9b593f32c386fe.svg){ .tikz loading=lazy }

!!! regle "Règle 4 — L’invariant du tri par sélection"

    Juste avant de traiter la case `i`, la partie `t[0..i-1]` est **triée** *et* contient les `i` plus petits éléments du tableau, **à leur place définitive**. C’est cet invariant qui garantit qu’à la fin le tableau entier est trié. Il se démontre en deux étapes, comme au chapitre *Algorithmique : le parcours séquentiel*, et peut être vérifié par un `assert` pendant la mise au point, comme au chapitre *Spécifier et mettre au point ses programmes*.

!!! demonstration "Démonstration — L’invariant du tri par sélection"

    Notons $P$ la propriété : « `t[0..i-1]` est triée et contient les `i` plus petits éléments du tableau ».

    - **Initialisation** ($\texttt{i} = 0$) : la partie `t[0..-1]` est *vide* ; une partie vide est triée et contient bien les $0$ plus petits éléments. $P$ est vraie.

    - **Hérédité** : supposons $P$ vraie au début de l’étape `i`. Comme `t[0..i-1]` contient les `i` plus petits éléments, chaque élément de la partie restante `t[i..n-1]` est supérieur ou égal à chacun d’eux. La boucle interne trouve le minimum de cette partie restante (invariant du champion) : c’est donc le $(\texttt{i}+1)$<sup>e</sup> plus petit élément du tableau, et il est supérieur ou égal à `t[i-1]`. L’échange le place en case `i` et ne touche qu’aux cases `i` et `i_min`, toutes deux hors de `t[0..i-1]`. Au début de l’étape suivante, `t[0..i]` est triée et contient les $\texttt{i}+1$ plus petits éléments : $P$ reste vraie.

    Après la dernière étape ($\texttt{i} = \texttt{n}-1$), $P$ porte sur `t[0..n-1]` : le tableau entier est trié.

!!! regle "Règle 5 — Terminaison du tri par sélection"

    Le tri par sélection ne contient que deux boucles `for`, donc **bornées** : la boucle externe fait `n` tours, la boucle interne au plus $\texttt{n}-1$ à chacun d’eux. Le tri se termine toujours ; nul besoin de variant.

<span id="cours-06-1" class="ancre"></span>

<span class="afaire">▶ Exercices d'application :</span> exercices **[1](exercices.md#ex-06-1) à [5](exercices.md#ex-06-5)** et **[22](exercices.md#ex-06-22)** (dérouler la sélection ; programmer le tri par sélection)

## Le tri par insertion

**L’idée** est celle du joueur qui ramasse ses cartes *une par une* et garde sa main toujours triée : *je prends la carte suivante, et je la glisse à la bonne place parmi celles que je tiens déjà.* C’est le tri le plus « naturel » pour un humain.

!!! regle "Règle 6 — Principe du tri par insertion"

    On parcourt le tableau de la gauche vers la droite. À chaque étape, la partie de gauche est *déjà triée* ; on prend l’élément suivant et on l’**insère** à sa place dans cette partie triée, en **décalant** vers la droite tous les éléments plus grands que lui.

<span class="retouract">↺ Retour sur l'activité.</span> La méthode 2 de l’activité, « comme une main de cartes », était le tri par insertion : chaque carte, comparée à ses voisines de gauche, était glissée à sa place parmi les cartes déjà rangées.

```python
def tri_insertion(t):
    """Trie le tableau t en place, dans l'ordre croissant."""
    n = len(t)
    for i in range(1, n):
        x = t[i]              # l'element a inserer dans la partie triee
        j = i - 1
        # decaler vers la droite tant que l'on rencontre plus grand que x
        while j >= 0 and t[j] > x:
            t[j + 1] = t[j]
            j = j - 1
        t[j + 1] = x          # on depose x dans le "trou" cree
```

!!! remarque "Remarque — Le rôle du while"

    La condition d’arrêt `t[j] > x` fait reculer `j` *seulement* tant qu’il y a des éléments plus grands à décaler. Dès qu’on trouve un élément *plus petit ou égal* (ou que `j` devient $-1$ : la condition `j >= 0` est alors fausse), on s’arrête : la place de `x` est trouvée. On range `x` juste après, en `t[j+1]`.

### Dérouler l’algorithme

Traçons le tri de `[5, 3, 8, 1, 9, 2]`. Le tableau est montré **après chaque insertion** : la zone `grisée` est **triée mais provisoire** (elle bougera encore), et l’élément `orange` est celui qu’on **vient d’insérer** à sa place.

<table>
<thead>
<tr>
<th style="text-align: right;"><strong>étape</strong></th>
<th colspan="6" style="text-align: left;"><strong>tableau</strong></th>
<th style="text-align: left;"><strong>action</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: right;">départ</td>
<td style="text-align: center;"><code>5</code></td>
<td style="text-align: center;"><code>3</code></td>
<td style="text-align: center;"><code>8</code></td>
<td style="text-align: center;"><code>1</code></td>
<td style="text-align: center;"><code>9</code></td>
<td style="text-align: center;"><code>2</code></td>
<td style="text-align: left;">la case 0 est triée à elle seule</td>
</tr>
<tr>
<td style="text-align: right;">insérer 3</td>
<td style="text-align: center;"><code>3</code></td>
<td style="text-align: center;"><code>5</code></td>
<td style="text-align: center;"><code>8</code></td>
<td style="text-align: center;"><code>1</code></td>
<td style="text-align: center;"><code>9</code></td>
<td style="text-align: center;"><code>2</code></td>
<td style="text-align: left;">3 s’insère avant 5</td>
</tr>
<tr>
<td style="text-align: right;">insérer 8</td>
<td style="text-align: center;"><code>3</code></td>
<td style="text-align: center;"><code>5</code></td>
<td style="text-align: center;"><code>8</code></td>
<td style="text-align: center;"><code>1</code></td>
<td style="text-align: center;"><code>9</code></td>
<td style="text-align: center;"><code>2</code></td>
<td style="text-align: left;">8 est déjà bien placé</td>
</tr>
<tr>
<td style="text-align: right;">insérer 1</td>
<td style="text-align: center;"><code>1</code></td>
<td style="text-align: center;"><code>3</code></td>
<td style="text-align: center;"><code>5</code></td>
<td style="text-align: center;"><code>8</code></td>
<td style="text-align: center;"><code>9</code></td>
<td style="text-align: center;"><code>2</code></td>
<td style="text-align: left;">1 remonte tout au début</td>
</tr>
<tr>
<td style="text-align: right;">insérer 9</td>
<td style="text-align: center;"><code>1</code></td>
<td style="text-align: center;"><code>3</code></td>
<td style="text-align: center;"><code>5</code></td>
<td style="text-align: center;"><code>8</code></td>
<td style="text-align: center;"><code>9</code></td>
<td style="text-align: center;"><code>2</code></td>
<td style="text-align: left;">9 est déjà bien placé</td>
</tr>
<tr>
<td style="text-align: right;">insérer 2</td>
<td style="text-align: center;"><code>1</code></td>
<td style="text-align: center;"><code>2</code></td>
<td style="text-align: center;"><code>3</code></td>
<td style="text-align: center;"><code>5</code></td>
<td style="text-align: center;"><code>8</code></td>
<td style="text-align: center;"><code>9</code></td>
<td style="text-align: left;">2 se glisse en 2<sup>e</sup> position</td>
</tr>
</tbody>
</table>

En **histogramme**, après chaque insertion : la zone triée (colorée) grandit d’une barre, mais ses barres *changent de place* ; la barre orange vient d’être glissée à sa place (la flèche part de sa case d’origine), et les barres plus grandes qu’elle ont été décalées d’un cran vers la droite.

![](../figures/1c34be866985d587.svg){ .tikz loading=lazy }

!!! regle "Règle 7 — L’invariant du tri par insertion"

    Au début de l’étape `i`, la partie `t[0..i-1]` est formée des éléments qui étaient **initialement** en `t[0..i-1]`, rangés dans l’ordre **croissant**. Ce ne sont pas forcément les `i` plus petits du tableau : ils pourront être « poussés » plus loin par les insertions suivantes. Après le dernier tour ($\texttt{i} = \texttt{n}-1$), la propriété vaut pour `t[0..n-1]` : le tableau entier est trié.

!!! regle "Règle 8 — Terminaison du tri par insertion"

    La boucle `for` est bornée. La boucle `while`, elle, ne l’est pas : il faut un **variant** (chapitre *Les bases de la programmation Python*, § V.B). La quantité `j` convient : c’est un entier, positif ou nul tant que la boucle tourne (la condition impose `j >= 0`), qui diminue de $1$ à chaque tour (`j = j - 1`). La boucle `while` s’arrête donc après au plus `i` tours, et le tri se termine.

!!! encadre "À retenir — Sélection ou insertion : deux philosophies"

    Le tri par **sélection** place, à chaque étape, un élément à sa position *définitive* (il ne bougera plus). Le tri par **insertion** garde une partie gauche toujours triée, mais qui *grandit et se réorganise* au fil de l’eau. Même résultat, chemins différents.

<span id="cours-06-6" class="ancre"></span>

<span class="afaire">▶ Exercices d'application :</span> exercices **[6](exercices.md#ex-06-6) à [10](exercices.md#ex-06-10)** et **[23](exercices.md#ex-06-23)** (dérouler l’insertion, comparer les deux tris ; programmer le tri par insertion) ; exercice **[24](exercices.md#ex-06-24)** (invariant et terminaison des deux tris)

## Combien ça coûte ?

Reprenons notre réflexe : on compte les opérations en fonction de la taille `n` du tableau. Or nos deux tris ont la même forme : **une boucle dans une boucle**. Le chapitre *Algorithmique : le parcours séquentiel* nous a appris à reconnaître ce motif…

!!! regle "Règle 9 — Nos deux tris (sélection, insertion) sont quadratiques"

    La sélection comme l’insertion consistent à parcourir le tableau *à l’intérieur* d’un autre parcours. Le nombre de comparaisons est de l’ordre de $n^2$ : leur coût est **quadratique**. Si l’on double le nombre d’éléments, le temps de tri est multiplié par **quatre**.

!!! demonstration "Démonstration — Le compte exact pour la sélection"

    Pour placer la case $0$, on compare le minimum candidat aux $n-1$ éléments suivants. Pour la case $1$, aux $n-2$ suivants. … Pour l’avant-dernière, à $1$ seul. Le nombre total de comparaisons vaut $$(n-1) + (n-2) + \cdots + 2 + 1 = \frac{n(n-1)}{2},$$ une quantité proportionnelle à $n^2$ : c’est bien un coût **quadratique**. Et ce, *quel que soit* le tableau de départ.

!!! demonstration "Démonstration — Le pire cas pour l’insertion"

    Le pire cas est le tableau trié *à l’envers* : chaque élément est plus petit que tous ceux qui le précèdent. L’élément d’indice $i$ recule alors de $i$ cases : $i$ comparaisons et $i$ décalages (la boucle s’arrête quand `j` vaut $-1$). Au total, $$1 + 2 + \cdots + (n-1) = \frac{n(n-1)}{2}$$ comparaisons, et autant de décalages : là encore, un coût **quadratique**.

### Le meilleur atout de l’insertion

Les deux tris sont quadratiques *dans le pire des cas*. Mais l’insertion a une qualité que la sélection n’a pas :

!!! regle "Règle 10 — Le cas favorable de l’insertion"

    Si le tableau est **déjà trié** (ou presque), la boucle `while` du tri par insertion ne fait *aucun* (ou très peu de) décalage : elle s’arrête tout de suite, ou presque. Le tri se réduit alors à un **seul parcours** : son coût devient **linéaire** ! Le tri par sélection, lui, refait bêtement tout son travail : il est quadratique *même sur un tableau déjà trié*.

<span class="retouract">↺ Retour sur l'activité.</span> Dans l’activité, la méthode 1 faisait toujours $7 + 6 + \cdots + 1 = 28$ comparaisons pour 8 cartes, quel que soit l’ordre de départ ; la méthode 2 n’en faisait que 7 sur des cartes déjà rangées, mais 28 sur des cartes dans l’ordre inverse.

| **Tri**   |     **meilleur cas**      | **pire cas**  |     **échanges**     |
|:----------|:-------------------------:|:-------------:|:--------------------:|
| Sélection | $\approx n^2$ (toujours)  | $\approx n^2$ |  peu ($\approx n$)   |
| Insertion | $\approx n$ (déjà trié !) | $\approx n^2$ | beaucoup (décalages) |

!!! curieux "Pour les curieux (facultatif) — Concrètement, ce que « quadratique » veut dire"

    Pour $n = 1\,000$ éléments, un tri quadratique fait de l’ordre de $500\,000$ comparaisons : instantané. Mais pour $n = 1\,000\,000$, il en faudrait de l’ordre de $5 \times 10^{11}$ : **des minutes, voire des heures**. C’est pourquoi les vrais logiciels utilisent des tris plus malins (coût $n\log_2 n$), que vous découvrirez en terminale.

<span id="cours-06-11" class="ancre"></span>

<span class="afaire">▶ Exercices d'application :</span> exercices **[11](exercices.md#ex-06-11) à [13](exercices.md#ex-06-13)** (le coût d’un tri)

## D’autres tris existent

Sélection et insertion ne sont que deux membres d’une grande famille.

- Le **tri à bulles** fait « remonter » les grandes valeurs vers la fin par échanges de voisins successifs. Simple à comprendre, mais rarement efficace — vous le programmerez en exercice guidé.

- Le **tri fusion** et le **tri rapide** atteignent un coût $n\log_2 n$, bien meilleur : ce sont eux (et leurs cousins) qui trient « pour de vrai » dans les logiciels. <span class="horsprog">au-delà du programme</span>

- En Python, il suffit d’écrire `t.sort()` (tri en place) ou `sorted(t)` (nouveau tableau trié). Derrière ces mots se cache **Timsort**, un algorithme hybride très rapide inventé en 2002 par Tim Peters, aujourd’hui utilisé aussi par Java et Android. <span class="horsprog">au-delà du programme</span>

!!! curieux "Pour les curieux (facultatif) — Danser un algorithme"

    Pour *voir* un tri prendre vie, cherchez les vidéos « **AlgoRythmics** » : l’université Sapientia de Transylvanie (à Târgu Mureş, en Roumanie) y met en scène des **danses folkloriques** qui exécutent, pas à pas, le tri par sélection, par insertion, à bulles ou le tri rapide. C’est étrangement hypnotique — et bien plus parlant qu’un long discours.

!!! curieux "Pour les curieux (facultatif) — Le pire tri du monde, pour rire"

    Le **bogosort** (« tri stupide ») consiste à… mélanger le tableau au hasard, puis vérifier s’il est trié ; sinon, recommencer. Sur un jeu de 52 cartes, il faudrait en moyenne de l’ordre de $8 \times 10^{67}$ tirages (autant que d’ordres possibles pour les 52 cartes), bien plus qu’il n’y a d’atomes dans toute la Terre (environ $10^{50}$). À ne *jamais* utiliser — mais il rappelle avec humour qu’un algorithme *correct* peut être catastrophiquement *lent*.

<span id="cours-06-14" class="ancre"></span>

<span class="afaire">▶ Exercices d'application :</span> exercice **[14](exercices.md#ex-06-14)** (le tri à bulles)

## Un peu d’histoire

!!! curieux "Pour les curieux (facultatif) — Trier, aux origines de l’informatique"

    Trier des données mécaniquement est *antérieur* aux ordinateurs : dès le recensement américain de **1890**, les machines à cartes perforées de **Herman Hollerith** (dont l’entreprise deviendra IBM) dépouillaient des millions de fiches : à chaque carte lue, le couvercle d’un casier s’ouvrait et l’opérateur y rangeait la carte. Dès **1901**, des trieuses automatiques faisaient tomber chaque carte dans un casier selon la position d’un trou. En **1945**, dans l’un des tout premiers programmes de l’histoire, **John von Neumann** écrit la routine de *fusion*, cœur du tri fusion, pour la machine EDVAC : le tri fut ainsi l’un des premiers problèmes que l’on chercha à faire résoudre par une machine à programme enregistré. Depuis, il reste un terrain d’étude central : c’est sur des problèmes simples à énoncer comme « ranger dans l’ordre » que l’informatique a forgé sa science du **coût** des algorithmes.

    ![](../img/06_hist_trieuse_hollerith.jpg){ .photo loading=lazy style="width:157px" }  
    Une trieuse de cartes perforées Hollerith

    ![](../img/06_hist_edvac.jpg){ .photo loading=lazy style="width:118px" }  
    L’EDVAC, en service à partir de 1951

!!! curieux "Pour les curieux (facultatif) — Liens avec d’autres chapitres"

    - **Ce qu’il réutilise.** Le tri par sélection n’est qu’une suite de recherches du minimum (*Algorithmique : le parcours séquentiel*), justifiée par un **invariant de boucle** (*Spécifier et mettre au point ses programmes*).

    - **Ce qu’il prépare.** Trier rendra possible la **recherche dichotomique** ; trier une table selon une colonne servira dans *Les données en tables*, *Les algorithmes gloutons* et *Les $k$ plus proches voisins*.

    - **En Terminale.** *Diviser pour régner* présentera le **tri fusion**, en $n\log_2 n$, bien plus rapide que nos tris quadratiques sur de grands tableaux.

## Bilan — la carte mémoire

| **Notion** | **À retenir** |
|:---|:---|
| Trier | ranger dans l’ordre croissant, **en place** (comparaisons + échanges) |
| Pourquoi trier | chercher/comparer vite ensuite (dichotomie, médiane, doublons…) |
| Tri par sélection | chercher le **min** du reste, le placer ; position définitive à chaque étape |
| Tri par insertion | **insérer** chaque élément dans la partie gauche déjà triée (décalages) |
| Invariant (sélection) | `t[0..i-1]` triée, formée des `i` plus petits (place définitive) |
| Invariant (insertion) | `t[0..i-1]` : ses éléments de départ, rangés dans l’ordre |
| Terminaison | boucles `for` bornées ; variant `j` pour le `while` de l’insertion |
| Échanger | `temp = t[i]` ; `t[i] = t[j]` ; `t[j] = temp` (Python : `t[i], t[j] = t[j], t[i]`) |
| Coût des deux tris | **quadratique** ($\approx n^2$) : une boucle dans une boucle |
| Atout de l’insertion | **linéaire** si le tableau est déjà (presque) trié |
| En pratique | `t.sort()` / `sorted(t)` : Python utilise Timsort ($n\log_2 n$) |

!!! situation "Retour à la situation de départ"

    1.  Trier est un **investissement** : une fois le tableau trié, chercher devient fulgurant (recherche dichotomique), le minimum et le maximum sont aux deux bouts, les doublons côte à côte (§ I).

    2.  Ce sont le **tri par sélection** et le **tri par insertion** (§ II et III). Tous deux sont quadratiques dans le pire cas, mais l’insertion devient **linéaire** sur une main déjà presque rangée, alors que la sélection fait toujours $n(n-1)/2$ comparaisons (§ IV).

    3.  Non : le coût est **quadratique**, de l’ordre de $n^2$ comparaisons. Pour 1 000 fois plus de cartes, il faut environ un million de fois plus de comparaisons (§ IV).

## Erreurs fréquentes

- **Échanger deux valeurs sans variable temporaire.** `t[i] = t[j]` puis `t[j] = t[i]` **perd** la première valeur. *Le réflexe :* `temp = t[i]` ; `t[i] = t[j]` ; `t[j] = temp` (ou, en Python, `t[i], t[j] = t[j], t[i]`).

- **Se tromper de bornes.** Le dernier indice est `len(t)-1` ; attention aux `range` du tri.

- **Perdre de vue l’élément « en cours de tri ».** À chaque passe, on place **un** élément (le minimum choisi / l’élément inséré).

- **Tri par insertion : mal décaler.** On décale vers la droite les éléments **plus grands** avant de poser l’élément à sa place.

- **Croire qu’un tri quadratique passe partout.** Sur de grands tableaux, $n^2$ devient énorme. *Le réflexe :* en pratique, `sort()` / `sorted()` (Timsort, $n\log_2 n$).

## Savoir-faire à maîtriser

*À la fin du chapitre, je sais…*

- **dérouler** à la main un tri par sélection et un tri par insertion ;

- écrire le **tri par sélection** (recherche de l’indice du minimum, puis échange) ;

- écrire le **tri par insertion** ;

- **échanger** deux valeurs avec une variable temporaire ;

- énoncer l’**invariant** de chaque tri et justifier sa **terminaison** ;

- justifier le **coût quadratique** ($\approx n^2$, soit $\frac{n(n-1)}{2}$ comparaisons) ;

- reconnaître l’**atout de l’insertion** sur un tableau presque trié ;

- savoir qu’en pratique on utilise `sort()` / `sorted()`.
