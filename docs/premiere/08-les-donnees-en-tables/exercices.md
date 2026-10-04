# Exercices

<p class="sous-titre">Les données en tables</p>

!!! consignes "Mode d’emploi"

    - Niveau : ★ échauffement, ★★ classique (niveau bac), ★★★ défi ; les *coups de pouce* et les *corrigés* se déplient sous chaque exercice.

    - <span class="run" title="À programmer et tester sur machine">▶</span> *À programmer et tester* en Python. Le symbole `>>>` figure une saisie dans la console.

    - On travaille sur le fichier `prenoms.csv` (extrait du *Fichier des prénoms* de l’INSEE, `data.gouv.fr`) : descripteurs `prenom`, `sexe` (`F`/`G`), `annee` (2023 ou 2025), `nombre`. Et sur `communes.csv` / `departements.csv`.

    - **Réflexe n<sup>o</sup> 1** : les valeurs lues dans un CSV sont des **chaînes**. `int(...)` avant tout *calcul* ou *tri* numérique.

    - Usage de l’IA, indiqué sur chaque exercice : <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> aucune ; <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> en appui (déboguer, reformuler, vérifier ; la réponse finale est écrite et comprise par vous) ; <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> l’exercice s’appuie sur une réponse d’IA. Voir la [charte d’usage de l’IA](../charte.md).

On suppose disponible dans tous les exercices la fonction d’importation du cours :

```python
import csv
def charger(fichier):
    with open(fichier, encoding="utf-8", newline="") as f:
        return [ligne for ligne in csv.DictReader(f)]

prenoms = charger("prenoms.csv")
```

### Lire une table, lire un CSV

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 1</span> — Vocabulaire <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-08-1 }

On donne le début d’un fichier CSV public (jeux de la médiathèque) :

```text
titre;editeur;duree;age_min
Les Aventuriers du Rail;Days of Wonder;45;8
Dixit;Libellud;30;8
7 Wonders;Repos Prod;30;10
```

1.  Quel est le **séparateur** ? Combien y a-t-il de **descripteurs** ? d’**enregistrements** ?

2.  Citer les descripteurs. Donner la valeur du descripteur `duree` pour l’enregistrement `Dixit`.

3.  Ce fichier est-il « à la française » ou « anglo-saxon » ? Justifier.

??? corrige "Corrigé"

    !!! remarque "Remarque"

        On donne **une** version simple ; d’autres écritures sont possibles.

    **1.** Le séparateur est le **point-virgule** `;`. Il y a **4 descripteurs** et **3 enregistrements**. **2.** Descripteurs : `titre`, `editeur`, `duree`, `age_min`. Pour `Dixit`, `duree` vaut `30`. **3.** « À la française » : le séparateur est le point-virgule, comme il se doit quand on veut réserver la virgule aux décimaux.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 2</span> — Un fichier mal formé <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-08-2 }

Un camarade obtient `prenoms.csv` avec **une seule colonne** géante quand il l’ouvre. Quelle est l’erreur la plus probable ? Comment la corriger dans l’appel à `csv.DictReader` ?

??? corrige "Corrigé"

    Le fichier est « à la française » (séparateur `;`) mais lu avec le séparateur par défaut (la virgule) : chaque ligne entière est prise pour **une seule valeur**. On corrige en précisant le séparateur :

    ```python
    csv.DictReader(f, delimiter=";")
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 3</span> — Encodage <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-08-3 }

En ouvrant un fichier, l’élève voit `RaphaÃ«l` au lieu de `Raphaël`. Quel réglage a été oublié ? Écrire la ligne `open(...)` corrigée.

??? pouce "Coup de pouce"

    Quel paramètre de `open` indique comment lire les caractères accentués ? Quel est l’encodage standard aujourd’hui ?

??? corrige "Corrigé"

    L’`encoding` n’a pas été précisé (le fichier est en UTF-8 mais lu autrement). On corrige :

    ```python
    open(fichier, encoding="utf-8", newline="")
    ```

### Représenter une table en Python

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 4</span> — Une table à la main <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-08-4 }

Écrire la variable `jeux` représentant les **trois** lignes de l’exercice 1 sous forme d’une **liste de dictionnaires**.

??? corrige "Corrigé"

    ```python
    jeux = [
        {"titre": "Les Aventuriers du Rail", "editeur": "Days of Wonder",
         "duree": "45", "age_min": "8"},
        {"titre": "Dixit", "editeur": "Libellud", "duree": "30", "age_min": "8"},
        {"titre": "7 Wonders", "editeur": "Repos Prod",
         "duree": "30", "age_min": "10"},
    ]
    ```

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 5</span> — Accès <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-08-5 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Avec la variable `jeux` précédente, que renvoient ces expressions ?

```text
>>> jeux[1]["titre"]
>>> jeux[0]["age_min"]
>>> len(jeux)
```

Écrire une expression qui donne l’éditeur de `7 Wonders`.

??? corrige "Corrigé"

    `jeux[1]["titre"]` $\rightarrow$ `’Dixit’` ; `jeux[0]["age_min"]` $\rightarrow$ `’8’` ; `len(jeux)` $\rightarrow$ `3`.  
    Éditeur de `7 Wonders` : `jeux[2]["editeur"]`.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Descripteurs automatiques <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-6 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Écrire `descripteurs(table)` qui renvoie la liste des noms de colonnes d’une table (on suppose la table non vide).

??? pouce "Coup de pouce"

    Les noms de colonnes sont les clés de n’importe quelle fiche, par exemple de la première, `table[0]`. Comment obtenir les clés d’un dictionnaire ?

```text
>>> descripteurs(prenoms)
['prenom', 'sexe', 'annee', 'nombre']
```

??? corrige "Corrigé"

    ```python
    def descripteurs(table):
        return list(table[0].keys())
    ```

### Importer, et le piège du texte

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 7</span> — Lecture de trace <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-08-7 }

Sans machine, dire ce que renvoie `mystere(prenoms)`.

```python
def mystere(table):
    r = 0
    for ligne in table:
        if ligne["sexe"] == "F":
            r = r + 1
    return r
```

Que calcule cette fonction, en une phrase ?

??? corrige "Corrigé"

    Elle renvoie `20`. Elle **compte le nombre de fiches de filles** dans la table (10 en 2023 $+$ 10 en 2025).

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 8</span> — Le piège du texte <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-08-8 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Prédire, *puis* vérifier, la valeur de chaque expression :

```text
>>> prenoms[0]["nombre"]
>>> prenoms[0]["nombre"] + prenoms[1]["nombre"]
>>> int(prenoms[0]["nombre"]) + int(prenoms[1]["nombre"])
```

Expliquer la différence entre les deux dernières lignes.

??? corrige "Corrigé"

    ```text
    >>> prenoms[0]["nombre"]
    '3177'
    >>> prenoms[0]["nombre"] + prenoms[1]["nombre"]
    '31773168'
    >>> int(prenoms[0]["nombre"]) + int(prenoms[1]["nombre"])
    6345
    ```

    Sur des **chaînes**, `+` *colle* les textes (concaténation). Il faut `int(...)` pour obtenir une vraie **addition**.

### Rechercher et filtrer

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 9</span> — Filtrer <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-08-9 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Écrire `selection(table, sexe, annee)` qui renvoie la liste des fiches correspondant à ce `sexe` et cette `annee`. Vérifier :

```text
>>> filles23 = selection(prenoms, "F", "2023")
>>> [l["prenom"] for l in filles23]
['Louise', 'Ambre', 'Alba', 'Jade', 'Emma', 'Rose',
 'Alma', 'Alice', 'Romy', 'Anna']
```

??? corrige "Corrigé"

    ```python
    def selection(table, sexe, annee):
        resultat = []
        for ligne in table:
            if ligne["sexe"] == sexe and ligne["annee"] == annee:
                resultat.append(ligne)
        return resultat
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 10</span> — En compréhension <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-10 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Réécrire `selection` en **une seule ligne** avec une compréhension de liste.

??? pouce "Coup de pouce"

    Une compréhension avec filtre a la forme `[expression for element in liste if condition]` : quelle condition reprendre de `selection` ?

??? corrige "Corrigé"

    ```python
    def selection(table, sexe, annee):
        return [l for l in table if l["sexe"] == sexe and l["annee"] == annee]
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 11</span> — Rechercher une fiche <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-11 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Écrire `chercher(table, prenom, annee)` qui renvoie **la** fiche de ce prénom pour cette année, ou `None` si elle n’existe pas. On s’arrêtera dès qu’on l’a trouvée.

??? pouce "Coup de pouce"

    C’est une recherche séquentielle : `return` dès que les deux critères sont vérifiés. À quel endroit placer le `return None` ?

```text
>>> chercher(prenoms, "Jade", "2025")["nombre"]
'2925'
>>> chercher(prenoms, "Kevin", "2025")
None
```

??? corrige "Corrigé"

    ```python
    def chercher(table, prenom, annee):
        for ligne in table:
            if ligne["prenom"] == prenom and ligne["annee"] == annee:
                return ligne
        return None
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 12</span> — Deux critères <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-12 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Écrire un appel (ou une compréhension) qui donne la liste des prénoms de **garçons de 2025** attribués **plus de 3000** fois. *(Attention au piège n<sup>o</sup> 1.)*

??? pouce "Coup de pouce"

    Trois conditions reliées par `and` (sexe, année, nombre). Sur quel type doit porter la comparaison avec `3000` ?

??? corrige "Corrigé"

    ```python
    [l["prenom"] for l in prenoms
     if l["sexe"] == "G" and l["annee"] == "2025" and int(l["nombre"]) > 3000]
    # -> ['Gabriel', 'Noah', 'Leo', 'Raphael', 'Louis', 'Jules']
    ```

    Le `int(...)` est indispensable : sans lui, on comparerait une chaîne à un entier (erreur), ou un tri de texte donnerait un résultat faux.

### Calculer sur une colonne

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 13</span> — Compter <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-08-13 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Écrire `compter(table, sexe)` qui renvoie le nombre de *fiches* pour ce sexe. Combien pour `"G"` ?

??? corrige "Corrigé"

    ```python
    def compter(table, sexe):
        n = 0
        for ligne in table:
            if ligne["sexe"] == sexe:
                n += 1
        return n
    ```

    `compter(prenoms, "G")` $\rightarrow$ `20`.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 14</span> — Total et moyenne <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-14 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

1.  Écrire `total(table, sexe, annee)` qui renvoie la **somme** des `nombre` des fiches correspondantes.

    ??? pouce "Coup de pouce"

        Patron de l’accumulateur : un total initialisé à `0`, augmenté pour chaque fiche retenue. On peut réutiliser `selection`.

2.  En déduire combien de garçons ont reçu l’un de ces 10 prénoms en 2023.

3.  Écrire `nombre_moyen(table)` (moyenne des `nombre`). Que vaut-elle sur `filles23` ?

    ??? pouce "Coup de pouce"

        La moyenne, c’est la somme des valeurs divisée par le nombre de fiches, `len(table)`.

??? corrige "Corrigé"

    ```python
    def total(table, sexe, annee):
        s = 0
        for ligne in table:
            if ligne["sexe"] == sexe and ligne["annee"] == annee:
                s = s + int(ligne["nombre"])
        return s

    def nombre_moyen(table):
        total_val = 0
        for ligne in table:
            total_val = total_val + int(ligne["nombre"])
        return total_val / len(table)
    ```

    `total(prenoms, "G", "2023")` $\rightarrow$ `32684`. `nombre_moyen(filles23)` $\rightarrow$ `2628.7`.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 15</span> — Champion et lanterne rouge <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-15 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

1.  Écrire `plus_donne(table)` qui renvoie le couple (prénom, nombre) de la fiche au plus grand `nombre` (invariant du champion).

    ??? pouce "Coup de pouce"

        Prendre la première fiche comme championne provisoire, puis la remplacer dès qu’une fiche a un `nombre` plus grand (comparer des entiers). Renvoyer à la fin un p-uplet construit à partir de la championne.

2.  Écrire `moins_donne(table)` sur le même modèle.

3.  Tester sur `prenoms` entier. *Pourquoi faut-il convertir avec `int` pour que ce soit correct ?*

??? corrige "Corrigé"

    ```python
    def plus_donne(table):
        champion = table[0]
        for ligne in table:
            if int(ligne["nombre"]) > int(champion["nombre"]):
                champion = ligne
        return champion["prenom"], int(champion["nombre"])

    def moins_donne(table):
        champion = table[0]
        for ligne in table:
            if int(ligne["nombre"]) < int(champion["nombre"]):
                champion = ligne
        return champion["prenom"], int(champion["nombre"])
    ```

    `plus_donne(prenoms)` $\rightarrow$ `(’Gabriel’, 4625)` ; `moins_donne(prenoms)` $\rightarrow$ `(’Anna’, 2129)`. Sans `int`, on comparerait des *chaînes* : `"900"` serait jugé « plus grand » que `"3070"` (comparaison caractère par caractère), et le champion serait faux.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 16</span> — Coût <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-16 }

On veut, pour *chaque* fiche, afficher son `nombre` **et** la moyenne de la table. Un élève écrit :

```python
for ligne in table:
    print(ligne["nombre"], nombre_moyen(table))   # <-- ?
```

Pourquoi le coût devient-il **quadratique** ? Comment le rendre **linéaire** ? (Rappel du chapitre *Algorithmique : le parcours séquentiel*.)

??? pouce "Coup de pouce"

    Combien de fiches `nombre_moyen` parcourt-elle à chaque appel ? Combien de fois est-elle appelée ? La moyenne change-t-elle d’un tour à l’autre ?

??? pouce "Coup de pouce 2 (début de solution)"

    Calculer la moyenne **une seule fois**, avant la boucle : `m = nombre_moyen(table)`, puis utiliser `m` dans la boucle.

??? corrige "Corrigé"

    À chaque tour de boucle (il y en a $n$), `nombre_moyen(table)` **re-parcourt** toute la table ($n$ opérations) : coût total $n \times n$, **quadratique**. On rend le coût **linéaire** en calculant la moyenne **une seule fois, avant** la boucle :

    ```python
    m = nombre_moyen(table)
    for ligne in table:
        print(ligne["nombre"], m)
    ```

### Trier une table

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 17</span> — Trier par nombre <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-17 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Écrire `trier_par_nombre(table)` qui renvoie la table triée du plus donné au moins donné. Afficher les **3 premiers** prénoms de garçons de 2025.

??? pouce "Coup de pouce"

    `sorted` avec `key` (sur quoi comparer ?) et `reverse=True` ; pour la clé, penser au piège n<sup>o</sup> 1. Pour les 3 premiers : filtrer avec `selection`, trier, puis une tranche `[:3]`.

??? corrige "Corrigé"

    ```python
    def trier_par_nombre(table):
        return sorted(table, key=lambda ligne: int(ligne["nombre"]), reverse=True)

    top = trier_par_nombre(selection(prenoms, "G", "2025"))
    print([l["prenom"] for l in top][:3])   # ['Gabriel', 'Noah', 'Leo']
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 18</span> — Alphabétique <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-18 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Trier `filles23` par **ordre alphabétique** des prénoms. Quelle est la seule ligne à changer par rapport à l’exercice précédent ?

??? pouce "Coup de pouce"

    Seule la clé du tri change : sur quel descripteur trier ? Faut-il convertir ?

??? corrige "Corrigé"

    On change seulement la **clé** (et on enlève `reverse`) :

    ```python
    sorted(filles23, key=lambda l: l["prenom"])
    # -> Alba, Alice, Alma, Ambre, Anna, Emma, Jade, Louise, Romy, Rose
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 19</span> — Le tri qui ment <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-19 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Trier `filles23` avec `key=lambda l: l["nombre"]` (sans `int`) et `reverse=True`. Le résultat est-il le bon classement ? **Expliquer** précisément pourquoi, dans ce tri de chaînes avec `reverse=True`, `"900"` passerait avant `"3070"`.

??? pouce "Coup de pouce"

    Deux chaînes se comparent caractère par caractère, de gauche à droite, comme les mots d’un dictionnaire : comparer d’abord le premier caractère de chacune.

??? corrige "Corrigé"

    Avec `key=lambda l: l["nombre"]`, on trie les `nombre` **comme des mots**. Deux chaînes se comparent caractère par caractère : `"900"` commence par `’9’`, `"3070"` par `’3’` ; comme `’9’ > ’3’`, la chaîne `"900"` est jugée « plus grande » que `"3070"`. Le classement est donc faux : il faut `int(...)`.

### Fusionner deux tables

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 20</span> — Remettre la jointure dans l’ordre <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-08-20 }

Voici les lignes de la fonction `jointure` du cours, **mélangées** et **sans indentation**. Les remettre dans le bon ordre et les indenter correctement. Pour chaque ligne, dire en quelques mots son rôle.

```text
resultat.append(fusion)
for ld in droite:
def jointure(gauche, droite, cle):
fusion[c] = ld[c]
return resultat
if lg[cle] == ld[cle]:
resultat = []
fusion = dict(lg)
for lg in gauche:
for c in ld:
```

??? corrige "Corrigé"

    ```python
    def jointure(gauche, droite, cle):
        resultat = []                 # la table fusionnee, vide au depart
        for lg in gauche:             # chaque fiche de gauche...
            for ld in droite:         # ... est comparee a chaque fiche de droite
                if lg[cle] == ld[cle]:          # meme valeur de la cle
                    fusion = dict(lg)           # copie de la fiche de gauche
                    for c in ld:
                        fusion[c] = ld[c]       # on ajoute les colonnes de droite
                    resultat.append(fusion)     # on range la fiche combinee
        return resultat
    ```

    À noter : `resultat = []` est *avant* les boucles (sinon on le vide à chaque tour) ; `resultat.append(fusion)` est dans le `if`, *après* la boucle sur `c` (sinon on ajouterait des fiches incomplètes) ; `return resultat` est au niveau de la fonction, après toutes les boucles.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 21</span> — Jointure <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-21 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

On charge `communes = charger("communes.csv")` et `departements = charger("departements.csv")`, reliées par le descripteur `dep`.

1.  Écrire `jointure(gauche, droite, cle)` (patron du cours).

2.  Vérifier que la fiche de `Nice` obtient bien sa `region`.

3.  Le fichier `communes.csv` contient `Ajaccio` (code `2A`), *absent* de `departements.csv`. Que devient Ajaccio après la jointure ? Pourquoi ?

    ??? pouce "Coup de pouce"

        Pour la fiche d’Ajaccio, la condition `lg[cle] == ld[cle]` est-elle vraie pour au moins une fiche de droite ? Que se passe-t-il alors dans la boucle ?

??? corrige "Corrigé"

    ```python
    def jointure(gauche, droite, cle):
        resultat = []
        for lg in gauche:
            for ld in droite:
                if lg[cle] == ld[cle]:
                    fusion = dict(lg)
                    for c in ld:
                        fusion[c] = ld[c]
                    resultat.append(fusion)
        return resultat

    villes = jointure(communes, departements, "dep")
    ```

    La fiche de `Nice` obtient `region` $=$ `"Provence-Alpes-Cote d’Azur"`. **Ajaccio disparaît** : son code `dep` `"2A"` n’a *aucune* correspondance dans `departements`, donc la condition `lg[cle] == ld[cle]` n’est jamais vraie et aucune ligne n’est produite pour lui.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 22</span> — Compter par groupe <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-22 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

À l’aide de la jointure précédente, écrire un code qui affiche, pour la **région** `"Provence-Alpes-Cote d’Azur"` (écrite sans accent dans `departements.csv`), le nombre de communes du fichier qui s’y trouvent.

??? pouce "Coup de pouce"

    Parcourir le résultat de la jointure avec un compteur, comme dans l’exercice « Compter ».

??? corrige "Corrigé"

    ```python
    villes = jointure(communes, departements, "dep")
    n = 0
    for ligne in villes:
        if ligne["region"] == "Provence-Alpes-Cote d'Azur":
            n += 1
    print(n)   # 3  (Nice, Menton, Marseille)
    ```

    *Autre méthode :* construire par compréhension la liste des communes de la région, puis prendre sa longueur.

    ```python
    paca = [l["nom"] for l in villes if l["region"] == "Provence-Alpes-Cote d'Azur"]
    print(len(paca))   # 3
    ```

### Mini-projets de synthèse (données réelles)

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 23</span> — Le palmarès à la loupe <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-23 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Écrire un programme qui, à partir de `prenoms.csv`, affiche pour l’année **2025** :

1.  le prénom de fille et le prénom de garçon les plus donnés ;

2.  la moyenne des attributions chez les filles, puis chez les garçons ;

3.  le **top 3** des garçons, dans l’ordre.

??? pouce "Coup de pouce"

    Inutile de tout réécrire : chaque question combine des fonctions déjà écrites (`selection`, `plus_donne`, `nombre_moyen`, `trier_par_nombre`).

??? pouce "Coup de pouce 2 (début de solution)"

    `filles25 = selection(prenoms, "F", "2025")`  
    `garcons25 = selection(prenoms, "G", "2025")`  
    `print(plus_donne(filles25), plus_donne(garcons25))`

??? corrige "Corrigé"

    ```python
    filles25 = selection(prenoms, "F", "2025")
    garcons25 = selection(prenoms, "G", "2025")

    print("Fille la plus donnee :", plus_donne(filles25))     # ('Louise', 3070)
    print("Garcon le plus donne :", plus_donne(garcons25))    # ('Gabriel', 4625)
    print("Moyenne filles :", round(nombre_moyen(filles25), 1))    # 2489.0
    print("Moyenne garcons :", round(nombre_moyen(garcons25), 1))  # 3231.5
    top3 = trier_par_nombre(garcons25)[:3]
    print("Top 3 garcons :", [l["prenom"] for l in top3])   # Gabriel, Noah, Leo
    ```

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 24</span> — Qui monte, qui descend ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-24 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

On veut comparer 2023 et 2025 chez les **garçons**.

1.  Écrire `rang(table, sexe, annee)` qui renvoie un *dictionnaire* `{prenom : rang}` (rang 1 $=$ le plus donné), obtenu en triant puis en numérotant.

2.  En comparant les rangs 2023 et 2025, déterminer un prénom qui a **gagné** des places et un qui en a **perdu**. *(Sur les vraies données, Noah passe 6<sup>e</sup>$\to$<!-- -->2<sup>e</sup> et `Mael`, écrit sans accent dans le fichier, 5<sup>e</sup>$\to$<!-- -->10<sup>e</sup>.)*

??? pouce "Coup de pouce"

    Après le tri décroissant, la fiche d’indice `i` a le rang `i + 1`. Pour comparer, parcourir les prénoms de 2023 et regarder s’ils ont aussi un rang en 2025 (test `in` sur les clés).

??? pouce "Coup de pouce 2 (début de solution)"

    `lignes = trier_par_nombre(selection(table, sexe, annee))`  
    `resultat = {}`  
    `for i in range(len(lignes)):`  
    `...`

??? corrige "Corrigé"

    ```python
    def rang(table, sexe, annee):
        lignes = trier_par_nombre(selection(table, sexe, annee))
        resultat = {}
        for i in range(len(lignes)):
            resultat[lignes[i]["prenom"]] = i + 1
        return resultat

    r23 = rang(prenoms, "G", "2023")
    r25 = rang(prenoms, "G", "2025")
    for prenom in r23:
        if prenom in r25:
            print(prenom, r23[prenom], "->", r25[prenom])
    # Noah 6 -> 2 (monte), Mael 5 -> 10 (descend)
    ```

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 25</span> — Entrants et sortants <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-25 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

On note `noms2023` et `noms2025` les listes des prénoms du top 10 des filles en 2023 et en 2025. À l’aide de **tests d’appartenance** (`in` / `not in`, par exemple dans une compréhension), déterminer : les prénoms présents **en 2023 et en 2025**, ceux qui en sont **sortis** (en 2023 mais plus en 2025), ceux qui y sont **entrés** (en 2025 mais pas en 2023). *(Résultat attendu : `’Anna’` sort, `’Adele’` entre — les prénoms sont écrits sans accents dans le fichier.)*

??? pouce "Coup de pouce"

    Construire d’abord les deux listes de prénoms (par compréhension avec filtre), puis, pour chaque question, une compréhension qui garde les prénoms d’une liste selon qu’ils sont `in` ou `not in` l’autre.

??? pouce "Coup de pouce 2 (début de solution)"

    `noms2023 = [l["prenom"] for l in selection(prenoms, "F", "2023")]`  
    `sortis = [p for p in noms2023 if p not in noms2025]`

??? corrige "Corrigé"

    ```python
    noms2023 = [l["prenom"] for l in prenoms if l["sexe"] == "F" and l["annee"] == "2023"]
    noms2025 = [l["prenom"] for l in prenoms if l["sexe"] == "F" and l["annee"] == "2025"]

    deux_annees = [p for p in noms2023 if p in noms2025]
    sortis = [p for p in noms2023 if p not in noms2025]    # ['Anna']
    entres = [p for p in noms2025 if p not in noms2023]    # ['Adele']
    print("dans les deux :", deux_annees)
    print("sortis :", sortis)
    print("entres :", entres)
    ```

    *Autre méthode :* sans compréhension, avec une boucle et `append` (même idée : on garde les prénoms de 2023 absents de 2025).

    ```python
    sortis = []
    for p in noms2023:
        if p not in noms2025:
            sortis.append(p)
    ```

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 26</span> — Écrire un CSV <span class="horsprog">au-delà du programme</span> <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-26 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

*Bonus, au-delà du programme.* À l’aide de `csv.DictWriter`, écrire une fonction `exporter(table, fichier)` qui **sauvegarde** une table (par exemple le résultat d’un filtre) dans un nouveau fichier CSV, puis vérifier en le rechargeant avec `charger`.

??? pouce "Coup de pouce"

    Ouvrir le fichier en écriture (`"w"`) ; un `csv.DictWriter` a besoin de la liste des noms de colonnes (paramètre `fieldnames`) : la fonction `descripteurs` la donne.

??? pouce "Coup de pouce 2 (début de solution)"

    `with open(fichier, "w", encoding="utf-8", newline="") as f:`  
    `ecrivain = csv.DictWriter(f, fieldnames=descripteurs(table))`  
    `ecrivain.writeheader()`

??? corrige "Corrigé"

    ```python
    def exporter(table, fichier):
        with open(fichier, "w", encoding="utf-8", newline="") as f:
            ecrivain = csv.DictWriter(f, fieldnames=list(table[0].keys()))
            ecrivain.writeheader()
            for ligne in table:
                ecrivain.writerow(ligne)

    exporter(filles23, "filles_2023.csv")
    verif = charger("filles_2023.csv")
    print(len(verif))   # 10
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 27</span> — Une moyenne selon un assistant d’IA <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> { #ex-08-27 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Un élève demande à un assistant d’IA : « J’ai chargé `prenoms.csv` avec `csv.DictReader` dans une liste de dictionnaires `prenoms`. Écris une fonction qui calcule le nombre moyen d’attributions (colonne `nombre`). » Voici la réponse obtenue.

```python
def moyenne_nombre(table):
    total = 0
    for ligne in table:
        total = total + ligne["nombre"]
    return total / len(table)
```

« On parcourt la table en accumulant la colonne `nombre` dans `total`, puis on divise par le nombre de lignes. Comme `DictReader` a déjà lu les valeurs numériques, il n’y a rien à convertir : `moyenne_nombre(prenoms)` renvoie directement la moyenne. »

1.  La réponse est-elle correcte ? Exécuter `moyenne_nombre(prenoms)` et noter ce qui se passe.

    ??? pouce "Coup de pouce"

        Quel est le type de `ligne["nombre"]` ? Relire le réflexe n<sup>o</sup> 1 du mode d’emploi.

2.  Localiser et corriger l’erreur.

3.  Quelle vérification simple, faite avant de faire confiance à la réponse, aurait suffi à détecter l’erreur ?

??? corrige "Corrigé"

    **1.** Non. L’appel s’interrompt dès la première ligne de la table :

    ```text
    >>> moyenne_nombre(prenoms)
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    ```

    `total` est un entier (`0`) et `ligne["nombre"]` une **chaîne** (`’3177’`) : Python refuse de les additionner. **2.** L’erreur est l’affirmation « rien à convertir » : `csv` lit du *texte*, toutes les valeurs sont des `str`, même les nombres. On convertit avec `int` :

    ```python
    def moyenne_nombre(table):
        total = 0
        for ligne in table:
            total = total + int(ligne["nombre"])
        return total / len(table)
    ```

    **3.** Regarder une fiche avant de calculer : `prenoms[0]` affiche `’nombre’: ’3177’`, avec des guillemets, donc du texte (ou demander `type(prenoms[0]["nombre"])`). C’est le réflexe du cours : dès qu’on calcule sur une colonne, on convertit.
