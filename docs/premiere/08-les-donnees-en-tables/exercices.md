# Exercices

<p class="sous-titre">Les données en tables</p>

!!! consignes "Mode d’emploi"

    -  Étoiles, <span class="essentiel">• essentiel</span>, coup de pouce, $\blacktriangleright$ et pastilles IA : voir le [mode d’emploi du chapitre 1](../01-les-bases-de-la-programmation-python/exercices.md#modeemploi).

    - <span class="run" title="À programmer et tester sur machine">▶</span> *À programmer et tester* en Python. Le symbole `>>>` figure une saisie dans la console.

    - On travaille sur le fichier `prenoms.csv` (extrait du *Fichier des prénoms* de l’INSEE, `data.gouv.fr`) : le **top 10** des filles et celui des garçons en 2023 et en 2025, soit 40 fiches ; descripteurs `prenom`, `sexe` (`F`/`G`), `annee` (2023 ou 2025), `nombre`. Et sur `communes.csv` / `departements.csv`.

    - **Réflexe n<sup>o</sup> 1** : les valeurs lues dans un CSV sont des **chaînes**. `int(...)` avant tout *calcul* ou *tri* numérique.

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

<span class="essentiel">• essentiel</span>

On donne les quatre premières lignes d’un fichier CSV public (jeux de la médiathèque) :

```text
titre;editeur;duree;age_min
Les Aventuriers du Rail;Days of Wonder;45;8
Dixit;Libellud;30;8
7 Wonders;Repos Prod;30;10
```

1.  Quel est le **séparateur** ? Combien y a-t-il de **descripteurs** ? d’**enregistrements** dans cet extrait ?

2.  Citer les descripteurs. Donner la valeur du descripteur `duree` pour l’enregistrement `Dixit`.

3.  Ce fichier est-il « à la française » ou « anglo-saxon » ? Justifier.

??? pouce "Coup de pouce"

    La première ligne contient les descripteurs (les noms de colonnes) ; chaque ligne suivante est un enregistrement. Quel caractère sépare les valeurs d’une même ligne ?

??? corrige "Corrigé"

    !!! remarque "Remarque"

        On donne **une** version simple ; d’autres écritures sont possibles.

    **1.** Le séparateur est le **point-virgule** `;`. Il y a **4 descripteurs** et **3 enregistrements**. **2.** Descripteurs : `titre`, `editeur`, `duree`, `age_min`. Pour `Dixit`, `duree` vaut `30`. **3.** « À la française » : le séparateur est le point-virgule, comme il se doit quand on veut réserver la virgule aux décimaux.

    <span class="erreurfreq">▷ Erreur fréquente.</span> compter la ligne d’en-tête parmi les enregistrements (4 au lieu de 3) : elle contient les noms des descripteurs, pas des données.

### Représenter une table en Python

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 2</span> — Une table à la main <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-08-2 }

<span class="essentiel">• essentiel</span>

Écrire la variable `jeux` représentant les **trois** lignes de l’exercice 1 sous forme d’une **liste de dictionnaires**.

??? pouce "Coup de pouce"

    Une fiche par enregistrement : un dictionnaire dont les clés sont les descripteurs. Comme `csv.DictReader`, écrire les valeurs sous forme de chaînes.

??? corrige "Corrigé"

    Une liste de trois dictionnaires, un par enregistrement, avec les descripteurs pour clés ; les valeurs sont des chaînes, comme après une lecture par `csv.DictReader`.

    ```python
    jeux = [
        {"titre": "Les Aventuriers du Rail", "editeur": "Days of Wonder",
         "duree": "45", "age_min": "8"},
        {"titre": "Dixit", "editeur": "Libellud", "duree": "30", "age_min": "8"},
        {"titre": "7 Wonders", "editeur": "Repos Prod",
         "duree": "30", "age_min": "10"},
    ]
    ```

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 3</span> — Accès <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-08-3 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Avec la variable `jeux` précédente, que renvoient ces expressions ?

```text
>>> jeux[1]["titre"]
>>> jeux[0]["age_min"]
>>> len(jeux)
```

Écrire une expression qui donne l’éditeur de `7 Wonders`.

??? pouce "Coup de pouce"

    On choisit d’abord la fiche par son indice dans la liste (à partir de `0`), puis la valeur par le nom du descripteur.

??? corrige "Corrigé"

    `jeux[1]["titre"]` $\rightarrow$ `’Dixit’` ; `jeux[0]["age_min"]` $\rightarrow$ `’8’` ; `len(jeux)` $\rightarrow$ `3`.  
    Éditeur de `7 Wonders` : `jeux[2]["editeur"]`.

    <span class="erreurfreq">▷ Erreur fréquente.</span> inverser les deux accès, `jeux["editeur"][2]` : `jeux` est une *liste*, on y choisit d’abord une fiche par son indice ; c’est la fiche, un dictionnaire, qui se lit par clé.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 4</span> — Descripteurs automatiques <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-4 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Écrire `descripteurs(table)` qui renvoie la liste des noms de colonnes d’une table (on suppose la table non vide).

??? pouce "Coup de pouce"

    Les noms de colonnes sont les clés de n’importe quelle fiche, par exemple de la première, `table[0]`. Une boucle `for` sur un dictionnaire parcourt ses clés : il reste à les ranger dans une liste, par exemple avec une compréhension.

```text
>>> descripteurs(prenoms)
['prenom', 'sexe', 'annee', 'nombre']
```

<span class="routine">▷ Avant de coder.</span> Écrire trois appels attendus sous forme d’`assert` : un cas **normal**, un cas **limite**, un cas **piège**.

??? corrige "Corrigé"

    *Appels attendus, écrits avant de coder :*

    ```python
    assert descripteurs([{"a": "1", "b": "2"}]) == ["a", "b"]  # cas normal
    assert descripteurs([{"nom": "Ada"}]) == ["nom"]           # cas limite : une seule colonne
    assert descripteurs([{"x": "1"}, {"x": "2"}]) == ["x"]     # cas piege : chaque nom une seule fois
    ```

    Les noms de colonnes sont les clés de la première fiche ; une compréhension sur ce dictionnaire parcourt ses clés.

    ```python
    def descripteurs(table):
        return [cle for cle in table[0]]
    ```

### Importer, et le piège du texte

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 5</span> — Un fichier mal formé <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-08-5 }

Un camarade ouvre avec `csv.DictReader` le fichier des jeux de la médiathèque (exercice « Vocabulaire ») et obtient **une seule colonne** géante. Quelle est l’erreur la plus probable ? Comment la corriger dans l’appel à `csv.DictReader` ?

??? pouce "Coup de pouce"

    Par défaut, `csv.DictReader` sépare les valeurs par une virgule. Quel séparateur utilisent les fichiers « à la française » ? Le paramètre s’appelle `delimiter`.

??? corrige "Corrigé"

    Le fichier est « à la française » (séparateur `;`) mais lu avec le séparateur par défaut (la virgule) : chaque ligne entière est prise pour **une seule valeur**. On corrige en précisant le séparateur :

    ```python
    csv.DictReader(f, delimiter=";")
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Encodage <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-08-6 }

En ouvrant un fichier, l’élève voit `RaphaÃ«l` au lieu de `Raphaël`. Quel réglage a été oublié ? Écrire la ligne `open(...)` corrigée.

??? pouce "Coup de pouce"

    Quel paramètre de `open` indique comment lire les caractères accentués ? Quel est l’encodage standard aujourd’hui ?

??? corrige "Corrigé"

    L’`encoding` n’a pas été précisé (le fichier est en UTF-8 mais lu autrement). On corrige :

    ```python
    open(fichier, encoding="utf-8", newline="")
    ```

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

??? pouce "Coup de pouce"

    C’est le patron du compteur : `r` augmente de 1 pour chaque fiche qui vérifie la condition. Combien de fiches de filles contient `prenoms` (deux années, un top 10 par année) ?

??? corrige "Corrigé"

    Elle renvoie `20`. Elle **compte le nombre de fiches de filles** dans la table (10 en 2023 $+$ 10 en 2025).

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 8</span> — Le piège du texte <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-08-8 }

<span class="run" title="À programmer et tester sur machine">▶</span>  <span class="essentiel">• essentiel</span>

Prédire, *puis* vérifier, la valeur de chaque expression :

```text
>>> prenoms[0]["nombre"]
>>> prenoms[0]["nombre"] + prenoms[1]["nombre"]
>>> int(prenoms[0]["nombre"]) + int(prenoms[1]["nombre"])
```

Expliquer la différence entre les deux dernières lignes.

??? pouce "Coup de pouce"

    Quel est le type de `prenoms[0]["nombre"]` ? Que fait `+` entre deux chaînes ?

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

    <span class="erreurfreq">▷ Erreur fréquente.</span> convertir après l’addition, `int(prenoms[0]["nombre"] + prenoms[1]["nombre"])` : les chaînes sont déjà collées, on obtient `31773168`. On convertit chaque valeur *avant* de calculer.

### Rechercher et filtrer

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 9</span> — Filtrer <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-08-9 }

<span class="run" title="À programmer et tester sur machine">▶</span>  <span class="essentiel">• essentiel</span>

Écrire `selection(table, sexe, annee)` qui renvoie la liste des fiches correspondant à ce `sexe` et cette `annee`. Vérifier :

```text
>>> filles23 = selection(prenoms, "F", "2023")
>>> [l["prenom"] for l in filles23]
['Louise', 'Ambre', 'Alba', 'Jade', 'Emma', 'Rose',
 'Alma', 'Alice', 'Romy', 'Anna']
```

??? pouce "Coup de pouce"

    Partir d’une liste vide et y ajouter (`append`) chaque fiche qui vérifie les deux conditions. Attention : l’année est lue comme une chaîne, d’où `"2023"` entre guillemets.

??? corrige "Corrigé"

    On part d’une liste vide et on y ajoute chaque fiche qui vérifie les deux conditions, reliées par `and`.

    ```python
    def selection(table, sexe, annee):
        resultat = []                                              # INITIALISER : liste vide
        for ligne in table:                                        # PARCOURIR
            if ligne["sexe"] == sexe and ligne["annee"] == annee:  # TESTER
                resultat.append(ligne)                             # METTRE A JOUR
        return resultat                                            # RENVOYER
    ```

    <span class="erreurfreq">▷ Erreur fréquente.</span> appeler `selection(prenoms, "F", 2023)` avec l’entier `2023` : `"2023" == 2023` est faux, et la sélection est vide, sans aucun message d’erreur.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 10</span> — En compréhension <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-10 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Réécrire `selection` en **une seule ligne** avec une compréhension de liste.

??? pouce "Coup de pouce"

    Une compréhension avec filtre a la forme `[expression for element in liste if condition]` : quelle condition reprendre de `selection` ?

<span class="routine">▷ Avant de coder.</span> Écrire trois appels attendus sous forme d’`assert` : un cas **normal**, un cas **limite**, un cas **piège**.

??? corrige "Corrigé"

    *Appels attendus, écrits avant de coder :*

    ```python
    assert len(selection(prenoms, "F", "2023")) == 10  # cas normal
    assert selection(prenoms, "F", "1990") == []       # cas limite : aucune fiche ne convient
    assert selection(prenoms, "F", 2023) == []         # cas piege : l'annee est une chaine
    ```

    La condition du `if` de `selection` devient le filtre de la compréhension, et l’élément gardé est la fiche elle-même.

    ```python
    def selection(table, sexe, annee):
        return [l for l in table if l["sexe"] == sexe and l["annee"] == annee]
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 11</span> — Rechercher une fiche <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-11 }

<span class="run" title="À programmer et tester sur machine">▶</span>  <span class="essentiel">• essentiel</span>

Écrire `chercher(table, prenom, annee)` qui renvoie **la** fiche de ce prénom pour cette année, ou `None` si elle n’existe pas. On s’arrêtera dès qu’on l’a trouvée.

??? pouce "Coup de pouce"

    C’est une recherche séquentielle : `return` dès que les deux critères sont vérifiés. À quel endroit placer le `return None` ?

```text
>>> chercher(prenoms, "Jade", "2025")["nombre"]
'2925'
>>> print(chercher(prenoms, "Kevin", "2025"))
None
```

<span class="routine">▷ Avant de coder.</span> Écrire trois appels attendus sous forme d’`assert` : un cas **normal**, un cas **limite**, un cas **piège**.

??? corrige "Corrigé"

    *Appels attendus, écrits avant de coder :*

    ```python
    assert chercher(prenoms, "Gabriel", "2023")["nombre"] == "4527"  # cas normal
    assert chercher(prenoms, "Kevin", "2025") == None                # cas limite : prenom absent
    assert chercher(prenoms, "Jade", "2025")["nombre"] == "2925"     # cas piege : la Jade de 2023 vient avant
    ```

    Recherche séquentielle : on renvoie la fiche dès que les deux critères sont vérifiés, et `None` seulement après avoir tout parcouru.

    ```python
    def chercher(table, prenom, annee):
        for ligne in table:                                            # PARCOURIR
            if ligne["prenom"] == prenom and ligne["annee"] == annee:  # TESTER
                return ligne                                           # RENVOYER : trouvee, on s'arrete
        return None                                                    # RENVOYER : parcours fini sans succes
    ```

    <span class="erreurfreq">▷ Erreur fréquente.</span> placer `return None` dans un `else`, à l’intérieur de la boucle : la fonction répond dès la première fiche et ne trouve que le premier prénom de la table.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 12</span> — Deux critères <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-12 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Écrire un appel (ou une compréhension) qui donne la liste des prénoms de **garçons de 2025** attribués **plus de 3000** fois. *(Attention au réflexe n<sup>o</sup> 1 du mode d’emploi.)*

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

??? pouce "Coup de pouce"

    Même patron que `mystere` dans l’exercice « Lecture de trace » ; seule la valeur comparée change.

??? corrige "Corrigé"

    Patron du compteur : `n` part de `0` et augmente de 1 pour chaque fiche de ce sexe.

    ```python
    def compter(table, sexe):
        n = 0                          # INITIALISER
        for ligne in table:            # PARCOURIR
            if ligne["sexe"] == sexe:  # TESTER
                n += 1                 # METTRE A JOUR
        return n                       # RENVOYER
    ```

    `compter(prenoms, "G")` $\rightarrow$ `20`.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 14</span> — Total et moyenne <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-14 }

<span class="run" title="À programmer et tester sur machine">▶</span>  <span class="essentiel">• essentiel</span>

1.  Écrire `total(table, sexe, annee)` qui renvoie la **somme** des `nombre` des fiches correspondantes.

    ??? pouce "Coup de pouce"

        Patron de l’accumulateur : un total initialisé à `0`, augmenté pour chaque fiche retenue. On peut réutiliser `selection`.

2.  En déduire combien de garçons nés en 2023 ont reçu l’un des 10 prénoms de garçons du fichier.

3.  Écrire `nombre_moyen(table)` (moyenne des `nombre`). Que vaut-elle sur `filles23` ?

    ??? pouce "Coup de pouce"

        La moyenne, c’est la somme des valeurs divisée par le nombre de fiches, `len(table)`.

<span class="routine">▷ Avant de coder.</span> Écrire trois appels attendus sous forme d’`assert` : un cas **normal**, un cas **limite**, un cas **piège**.

??? corrige "Corrigé"

    *Appels attendus pour `total`, écrits avant de coder :*

    ```python
    assert total(prenoms, "G", "2023") == 32684  # cas normal
    assert total(prenoms, "G", "1990") == 0      # cas limite : aucune fiche retenue
    t = [{"sexe": "F", "annee": "2023", "nombre": "900"},
         {"sexe": "F", "annee": "2023", "nombre": "3070"}]
    assert total(t, "F", "2023") == 3970         # cas piege : additionner des nombres, pas du texte
    ```

    Patron de l’accumulateur : on ajoute `int(ligne["nombre"])` pour chaque fiche retenue ; la moyenne divise la somme par `len(table)`.

    ```python
    def total(table, sexe, annee):
        s = 0                                                      # INITIALISER
        for ligne in table:                                        # PARCOURIR
            if ligne["sexe"] == sexe and ligne["annee"] == annee:  # TESTER
                s = s + int(ligne["nombre"])                       # METTRE A JOUR : convertir !
        return s                                                   # RENVOYER

    def nombre_moyen(table):
        total_val = 0                                              # INITIALISER
        for ligne in table:                                        # PARCOURIR
            total_val = total_val + int(ligne["nombre"])           # METTRE A JOUR
        return total_val / len(table)                              # RENVOYER
    ```

    `total(prenoms, "G", "2023")` $\rightarrow$ `32684`. `nombre_moyen(filles23)` $\rightarrow$ `2628.7`.

    <span class="erreurfreq">▷ Erreur fréquente.</span> oublier `int` dans l’accumulateur : `s + ligne["nombre"]` ajoute une chaîne à un entier, et Python lève une `TypeError`.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 15</span> — Champion et lanterne rouge <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-15 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

1.  Écrire `plus_donne(table)` qui renvoie le couple (prénom, nombre), le nombre étant un **entier**, de la fiche au plus grand `nombre` (invariant du champion).

    ??? pouce "Coup de pouce"

        Prendre la première fiche comme championne provisoire, puis la remplacer dès qu’une fiche a un `nombre` plus grand (comparer des entiers). Renvoyer à la fin un p-uplet construit à partir de la championne.

2.  Écrire `moins_donne(table)` sur le même modèle.

3.  Tester sur `prenoms` entier. *Pourquoi faut-il convertir avec `int` pour que ce soit correct ?*

<span class="routine">▷ Avant de coder.</span> Écrire trois appels attendus sous forme d’`assert` : un cas **normal**, un cas **limite**, un cas **piège**.

??? corrige "Corrigé"

    *Appels attendus pour `plus_donne`, écrits avant de coder :*

    ```python
    assert plus_donne(prenoms) == ("Gabriel", 4625)                        # cas normal
    assert plus_donne([{"prenom": "Ada", "nombre": "12"}]) == ("Ada", 12)  # cas limite : une seule fiche
    t = [{"prenom": "Ana", "nombre": "900"}, {"prenom": "Eve", "nombre": "3070"}]
    assert plus_donne(t) == ("Eve", 3070)                                  # cas piege : "900" > "3070" en texte
    ```

    ```python
    def plus_donne(table):
        champion = table[0]                                     # INITIALISER : la premiere fiche
        for ligne in table:                                     # PARCOURIR
            if int(ligne["nombre"]) > int(champion["nombre"]):  # TESTER
                champion = ligne                                # METTRE A JOUR
        return champion["prenom"], int(champion["nombre"])      # RENVOYER

    def moins_donne(table):
        champion = table[0]                                     # INITIALISER
        for ligne in table:                                     # PARCOURIR
            if int(ligne["nombre"]) < int(champion["nombre"]):  # TESTER
                champion = ligne                                # METTRE A JOUR
        return champion["prenom"], int(champion["nombre"])      # RENVOYER
    ```

    `plus_donne(prenoms)` $\rightarrow$ `(’Gabriel’, 4625)` ; `moins_donne(prenoms)` $\rightarrow$ `(’Anna’, 2129)`. Sans `int`, on comparerait des *chaînes*. Sur ce fichier, le champion serait le bon *par chance* : tous les effectifs ont 4 chiffres. Mais dès que les longueurs diffèrent, `"900"` serait jugé « plus grand » que `"3070"` (comparaison caractère par caractère) et le champion serait faux.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 16</span> — Coût <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-16 }

<span class="duree">≈ 10 min</span>

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

<span class="run" title="À programmer et tester sur machine">▶</span>  <span class="essentiel">• essentiel</span>

Écrire `trier_par_nombre(table)` qui renvoie la table triée du plus donné au moins donné. Afficher les **3 premiers** prénoms de garçons de 2025.

??? pouce "Coup de pouce"

    `sorted` avec `key` (sur quoi comparer ?) et `reverse=True` ; pour la clé, penser au réflexe n<sup>o</sup> 1. Pour les 3 premiers : filtrer avec `selection`, trier, puis une tranche `[:3]`.

<span class="routine">▷ Avant de coder.</span> Écrire trois appels attendus sous forme d’`assert` : un cas **normal**, un cas **limite**, un cas **piège**.

??? corrige "Corrigé"

    *Appels attendus, écrits avant de coder :*

    ```python
    assert trier_par_nombre(filles23)[0]["prenom"] == "Louise"  # cas normal
    assert trier_par_nombre([]) == []                           # cas limite : table vide
    t = [{"prenom": "Ana", "nombre": "900"}, {"prenom": "Eve", "nombre": "3070"}]
    assert trier_par_nombre(t)[0]["prenom"] == "Eve"            # cas piege : comparer des entiers
    ```

    `sorted` avec une clé qui convertit le `nombre` en entier, et `reverse=True` pour aller du plus donné au moins donné ; on filtre d’abord, on garde les 3 premiers à la fin.

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

Trier `filles23` avec `key=lambda l: l["nombre"]` (sans `int`) et `reverse=True`. Le résultat est-il le bon classement ? Est-ce **garanti** ? **Expliquer** précisément pourquoi, si un prénom n’avait été donné que 900 fois, la chaîne `"900"` passerait avant `"3070"` dans ce tri avec `reverse=True`.

??? pouce "Coup de pouce"

    Deux chaînes se comparent caractère par caractère, de gauche à droite, comme les mots d’un dictionnaire : comparer d’abord le premier caractère de chacune.

??? corrige "Corrigé"

    Avec `key=lambda l: l["nombre"]`, on trie les `nombre` **comme des mots**. Deux chaînes se comparent caractère par caractère : `"900"` commence par `’9’`, `"3070"` par `’3’` ; comme `’9’ > ’3’`, la chaîne `"900"` est jugée « plus grande » que `"3070"`. Sur `filles23`, le résultat est pourtant le bon classement, mais *par chance* : tous les effectifs ont 4 chiffres, et pour des chaînes de chiffres de même longueur, l’ordre des mots coïncide avec l’ordre des nombres. Il suffirait d’un prénom donné 900 fois pour que le classement devienne faux : il faut `int(...)`.

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
fusion = {c: lg[c] for c in lg}
for lg in gauche:
for c in ld:
```

??? pouce "Coup de pouce"

    Deux boucles imbriquées (gauche, puis droite) et un test d’égalité sur la clé. Quand les clés sont égales : copier la fiche de gauche, y ajouter les colonnes de droite, ranger le résultat.

??? corrige "Corrigé"

    ```python
    def jointure(gauche, droite, cle):
        resultat = []                                # INITIALISER : la table fusionnee, vide au depart
        for lg in gauche:                            # PARCOURIR : chaque fiche de gauche...
            for ld in droite:                        # PARCOURIR : ... comparee a chaque fiche de droite
                if lg[cle] == ld[cle]:               # TESTER : meme valeur de la cle
                    fusion = {c: lg[c] for c in lg}  # copie de la fiche de gauche
                    for c in ld:
                        fusion[c] = ld[c]            # on ajoute les colonnes de droite
                    resultat.append(fusion)          # METTRE A JOUR : on range la fiche combinee
        return resultat                              # RENVOYER
    ```

    À noter : `resultat = []` est *avant* les boucles (sinon on le vide à chaque tour) ; `resultat.append(fusion)` est dans le `if`, *après* la boucle sur `c` (sinon on ajouterait des fiches incomplètes) ; `return resultat` est au niveau de la fonction, après toutes les boucles.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 21</span> — Jointure <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-21 }

<span class="run" title="À programmer et tester sur machine">▶</span>  <span class="essentiel">• essentiel</span>

On charge `communes = charger("communes.csv")` et `departements = charger("departements.csv")`, reliées par le descripteur `dep`.

1.  Écrire `jointure(gauche, droite, cle)` (patron du cours).

2.  Vérifier que la fiche de `Nice` obtient bien sa `region`.

3.  Le fichier `communes.csv` contient `Ajaccio` (code `2A`), *absent* de `departements.csv`. Que devient Ajaccio après la jointure ? Pourquoi ?

    ??? pouce "Coup de pouce"

        Pour la fiche d’Ajaccio, la condition `lg[cle] == ld[cle]` est-elle vraie pour au moins une fiche de droite ? Que se passe-t-il alors dans la boucle ?

<span class="routine">▷ Avant de coder.</span> Écrire trois appels attendus sous forme d’`assert` : un cas **normal**, un cas **limite**, un cas **piège**.

??? corrige "Corrigé"

    *Appels attendus, écrits avant de coder :*

    ```python
    villes = jointure(communes, departements, "dep")
    assert villes[0]["region"] == "Provence-Alpes-Cote d'Azur"  # cas normal
    assert jointure([], departements, "dep") == []              # cas limite : aucune commune
    assert len(villes) == 7                                     # cas piege : Ajaccio (2A) disparait
    ```

    ```python
    def jointure(gauche, droite, cle):
        resultat = []                        # INITIALISER
        for lg in gauche:                    # PARCOURIR
            for ld in droite:                # PARCOURIR
                if lg[cle] == ld[cle]:       # TESTER
                    fusion = {c: lg[c] for c in lg}
                    for c in ld:
                        fusion[c] = ld[c]
                    resultat.append(fusion)  # METTRE A JOUR
        return resultat                      # RENVOYER

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
    n = 0                                                    # INITIALISER
    for ligne in villes:                                     # PARCOURIR
        if ligne["region"] == "Provence-Alpes-Cote d'Azur":  # TESTER
            n += 1                                           # METTRE A JOUR
    print(n)                                                 # 3  (Nice, Menton, Marseille)
    ```

    *Autre méthode :* construire par compréhension la liste des communes de la région, puis prendre sa longueur.

    ```python
    paca = [l["nom"] for l in villes if l["region"] == "Provence-Alpes-Cote d'Azur"]
    print(len(paca))   # 3
    ```

### Mini-projets de synthèse (données réelles)

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 23</span> — Le palmarès à la loupe <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-23 }

<span class="run" title="À programmer et tester sur machine">▶</span>  <span class="duree">≈ 20 min</span>

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
    print("Moyenne filles :", nombre_moyen(filles25))       # 2489.0
    print("Moyenne garcons :", nombre_moyen(garcons25))     # 3231.5
    top3 = trier_par_nombre(garcons25)[:3]
    print("Top 3 garcons :", [l["prenom"] for l in top3])   # Gabriel, Noah, Leo
    ```

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 24</span> — Qui monte, qui descend ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-24 }

<span class="run" title="À programmer et tester sur machine">▶</span>  <span class="duree">≈ 20 min</span>

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

<span class="routine">▷ Avant de coder.</span> Écrire trois appels attendus sous forme d’`assert` : un cas **normal**, un cas **limite**, un cas **piège**.

??? corrige "Corrigé"

    *Appels attendus pour `rang`, écrits avant de coder :*

    ```python
    assert rang(prenoms, "G", "2023")["Gabriel"] == 1  # cas normal
    assert rang(prenoms, "G", "1990") == {}            # cas limite : aucune fiche
    assert rang(prenoms, "G", "2025")["Mael"] == 10    # cas piege : le rang commence a 1, pas a 0
    ```

    ```python
    def rang(table, sexe, annee):
        lignes = trier_par_nombre(selection(table, sexe, annee))
        resultat = {}                              # INITIALISER
        for i in range(len(lignes)):               # PARCOURIR
            resultat[lignes[i]["prenom"]] = i + 1  # METTRE A JOUR : le rang commence a 1
        return resultat                            # RENVOYER

    r23 = rang(prenoms, "G", "2023")
    r25 = rang(prenoms, "G", "2025")
    for prenom in r23:
        if prenom in r25:
            print(prenom, r23[prenom], "->", r25[prenom])
    # Noah 6 -> 2 (monte), Mael 5 -> 10 (descend)
    ```

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 25</span> — Entrants et sortants <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-25 }

<span class="run" title="À programmer et tester sur machine">▶</span>  <span class="duree">≈ 15 min</span>

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
    sortis = []                # INITIALISER
    for p in noms2023:         # PARCOURIR
        if p not in noms2025:  # TESTER
            sortis.append(p)   # METTRE A JOUR
    ```

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 26</span> — Écrire un CSV <span class="horsprog">au-delà du programme</span> <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-26 }

<span class="run" title="À programmer et tester sur machine">▶</span>  <span class="duree">≈ 20 min</span>

*Bonus, au-delà du programme.* À l’aide de `csv.DictWriter`, écrire une fonction `exporter(table, fichier)` qui **sauvegarde** une table (par exemple le résultat d’un filtre) dans un nouveau fichier CSV, puis vérifier en le rechargeant avec `charger`.

??? pouce "Coup de pouce"

    Ouvrir le fichier en écriture (`"w"`) ; un `csv.DictWriter` a besoin de la liste des noms de colonnes (paramètre `fieldnames`) : la fonction `descripteurs` la donne.

??? pouce "Coup de pouce 2 (début de solution)"

    `with open(fichier, "w", encoding="utf-8", newline="") as f:`  
    `ecrivain = csv.DictWriter(f, fieldnames=descripteurs(table))`  
    `ecrivain.writeheader()`

<span class="routine">▷ Avant de coder.</span> Écrire trois appels attendus sous forme d’`assert` : un cas **normal**, un cas **limite**, un cas **piège**.

??? corrige "Corrigé"

    *Appels attendus, écrits avant de coder :*

    ```python
    exporter(filles23, "essai.csv")
    assert charger("essai.csv") == filles23                  # cas normal
    exporter([{"nom": "Ada"}], "essai.csv")
    assert charger("essai.csv") == [{"nom": "Ada"}]          # cas limite : une fiche, une colonne
    exporter([{"nom": "Dupont, Jean", "ville": "Nice"}], "essai.csv")
    assert charger("essai.csv")[0]["nom"] == "Dupont, Jean"  # cas piege : une virgule dans une valeur
    ```

    ```python
    def exporter(table, fichier):
        with open(fichier, "w", encoding="utf-8", newline="") as f:
            ecrivain = csv.DictWriter(f, fieldnames=[cle for cle in table[0]])
            ecrivain.writeheader()
            for ligne in table:           # PARCOURIR
                ecrivain.writerow(ligne)  # une ligne du fichier par fiche

    exporter(filles23, "filles_2023.csv")
    verif = charger("filles_2023.csv")
    print(len(verif))                     # 10
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
        total = 0                                 # INITIALISER
        for ligne in table:                       # PARCOURIR
            total = total + int(ligne["nombre"])  # METTRE A JOUR : int, car csv lit du texte
        return total / len(table)                 # RENVOYER
    ```

    **3.** Regarder une fiche avant de calculer : `prenoms[0]` affiche `’nombre’: ’3177’`, avec des guillemets, donc du texte (ou demander `type(prenoms[0]["nombre"])`). C’est le réflexe du cours : dès qu’on calcule sur une colonne, on convertit.

### Entraînement

*Exercices courts pour s’entraîner aux gestes de base, chacun avec plusieurs données. Ils font tous partie du parcours essentiel.*

Dans les deux exercices, on utilise la petite table suivante, lue dans un CSV (les valeurs sont donc des chaînes) :

```python
eleves = [{"nom": "Ada", "classe": "1A", "note": "15"},
          {"nom": "Léo", "classe": "1B", "note": "9"},
          {"nom": "Zoé", "classe": "1A", "note": "12"}]
```

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 28</span> — Lire et filtrer une table <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-08-28 }

<span class="essentiel">• essentiel</span>

Sans machine, donner la valeur de chaque expression, puis <span class="run" title="À programmer et tester sur machine">▶</span> vérifier.

1.  `eleves[2]["nom"]`

2.  `eleves[0]["note"] + eleves[1]["note"]`

3.  `int(eleves[0]["note"]) + int(eleves[1]["note"])`

4.  `[e["nom"] for e in eleves if e["classe"] == "1A"]`

5.  `[e["nom"] for e in eleves if int(e["note"]) < 10]`

??? pouce "Coup de pouce"

    D’abord la fiche (indice dans la liste), puis la valeur (nom du descripteur). Entre deux chaînes, `+` colle les textes.

??? corrige "Corrigé"

    a) `’Zoé’` b) `’159’` (deux chaînes collées) c) `24` d) `[’Ada’, ’Zoé’]` e) `[’Léo’]`.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 29</span> — Trier une table : prédire l’ordre <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-08-29 }

<span class="essentiel">• essentiel</span>

Sans machine, donner la liste des noms dans l’ordre obtenu par chaque tri, puis <span class="run" title="À programmer et tester sur machine">▶</span> vérifier.

1.  `sorted(eleves, key=lambda e: e["nom"])`

2.  `sorted(eleves, key=lambda e: int(e["note"]))`

3.  `sorted(eleves, key=lambda e: int(e["note"]), reverse=True)`

4.  `sorted(eleves, key=lambda e: e["note"])`

Pourquoi les résultats de b) et d) diffèrent-ils ?

??? pouce "Coup de pouce"

    La clé dit sur quoi comparer les fiches. Sans `int`, on compare des chaînes caractère par caractère, comme des mots du dictionnaire : comparer d’abord les premiers caractères de `"15"`, `"9"` et `"12"`.

??? corrige "Corrigé"

    a) `[’Ada’, ’Léo’, ’Zoé’]` (ordre alphabétique des noms) ; b) `[’Léo’, ’Zoé’, ’Ada’]` (notes 9, 12, 15) ; c) `[’Ada’, ’Zoé’, ’Léo’]` (notes décroissantes) ; d) `[’Zoé’, ’Ada’, ’Léo’]`. En d), les notes sont comparées comme des **chaînes** : `"12"` et `"15"` commencent par `’1’`, qui vient avant `’9’` : `"9"` passe en dernier, comme si c’était la meilleure note. C’est le piège n<sup>o</sup> 1 : on convertit avec `int` dans la clé.

    <span class="erreurfreq">▷ Erreur fréquente.</span> trier une colonne de nombres lue dans un CSV sans `int` : le tri ne signale aucune erreur, mais il range les valeurs dans l’ordre du dictionnaire, pas dans l’ordre numérique.

### Nettoyer une table

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 30</span> — Doublons et notes impossibles <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-08-30 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Un professeur a saisi les notes d’un devoir dans un CSV, avec quelques erreurs :

```python
notes = [{"nom": "Ada", "classe": "1A", "note": "15"},
         {"nom": "Léo", "classe": "1B", "note": "9"},
         {"nom": "Ada", "classe": "1A", "note": "15"},
         {"nom": "Zoé", "classe": "1A", "note": "23"},
         {"nom": "Tom", "classe": "1B", "note": "-2"},
         {"nom": "Ada", "classe": "1B", "note": "11"}]
```

On considère qu’un élève est identifié par son `nom` **et** sa `classe`.

1.  Écrire `notes_impossibles(table)` qui renvoie la liste des **noms** des fiches dont la note n’est pas comprise entre 0 et 20. Que renvoie-t-elle sur `notes` ?

2.  Écrire `doublons(table)` qui renvoie la liste des fiches dont le couple (`nom`, `classe`) a déjà été rencontré plus haut dans la table. Combien de doublons dans `notes` ? Pourquoi la dernière fiche n’en est-elle pas un ?

3.  Écrire `nettoyer(table)` qui renvoie une **nouvelle** table sans doublon et sans note impossible. Calculer la moyenne des notes avant et après nettoyage.

??? pouce "Coup de pouce"

    Pour les doublons, garder une liste `deja_vus` des couples `(nom, classe)` rencontrés, comme dans le cours ; une fiche est un doublon si son couple est déjà dans cette liste.

<span class="routine">▷ Avant de coder.</span> Écrire trois appels attendus sous forme d’`assert` : un cas **normal**, un cas **limite**, un cas **piège**.

??? corrige "Corrigé"

    *Appels attendus pour `doublons`, écrits avant de coder :*

    ```python
    assert len(doublons(notes)) == 1  # cas normal
    assert doublons([]) == []         # cas limite : table vide
    t = [{"nom": "Ada", "classe": "1A"}, {"nom": "Ada", "classe": "1B"}]
    assert doublons(t) == []          # cas piege : meme nom, autre classe
    ```

    **1.** Un test de cohérence est un filtre (sans oublier `int`) :

    ```python
    def notes_impossibles(table):
        return [ligne["nom"] for ligne in table
                if int(ligne["note"]) < 0 or int(ligne["note"]) > 20]
    ```

    `notes_impossibles(notes)` renvoie `[’Zoé’, ’Tom’]` (23 et $-2$).

    **2.** On mémorise les identifiants déjà vus :

    ```python
    def doublons(table):
        deja_vus = []                   # INITIALISER : identifiants rencontres
        resultat = []                   # INITIALISER
        for ligne in table:             # PARCOURIR
            cle = (ligne["nom"], ligne["classe"])
            if cle in deja_vus:         # TESTER
                resultat.append(ligne)  # METTRE A JOUR : c'est un doublon
            else:
                deja_vus.append(cle)    # METTRE A JOUR : premiere rencontre
        return resultat                 # RENVOYER
    ```

    Il y a **1** doublon : la troisième fiche (Ada, 1A). La dernière fiche est une autre élève, Ada de **1B** : même nom, mais pas même identifiant (`nom`, `classe`).

    **3.** On garde une fiche si elle est cohérente et si son identifiant n’a pas encore été gardé :

    ```python
    def nettoyer(table):
        propre = []                                               # INITIALISER
        deja_vus = []                                             # INITIALISER
        for ligne in table:                                       # PARCOURIR
            cle = (ligne["nom"], ligne["classe"])
            note = int(ligne["note"])
            if note >= 0 and note <= 20 and cle not in deja_vus:  # TESTER
                deja_vus.append(cle)                              # METTRE A JOUR
                propre.append(ligne)                              # METTRE A JOUR
        return propre                                             # RENVOYER
    ```

    Avant nettoyage : $(15 + 9 + 15 + 23 - 2 + 11) / 6 = 71 / 6 \approx 11{,}83$. Après : il reste Ada (1A), Léo et Ada (1B), soit $(15 + 9 + 11) / 3 = 35 / 3 \approx 11{,}67$.
