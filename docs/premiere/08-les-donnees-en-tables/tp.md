# TP et projets

<p class="sous-titre">Les données en tables</p>

## <span class="etiquette">TP</span> La météo de la Riviera

*importer, nettoyer, interroger, croiser et exporter une vraie table*

<p class="infos-activite">Durée : 2 à 3 h (deux séances) · Seul ou en binôme, sur machine</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/08-tp-meteo-riviera){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/premiere-08-tp-meteo-riviera.zip){ .md-button }

!!! encadre "But du TP"

    Un réseau de six stations météo, de Monaco à Gréolières, a transmis ses relevés quotidiens du mois d’août. Comme toutes les données réelles, le fichier reçu est **imparfait** : valeurs manquantes, lignes en double, capteur défectueux, station inconnue… Vous allez écrire en Python, **sans bibliothèque spécialisée**, la chaîne complète d’un traitement de données : **importer** le CSV, le **contrôler** et le **nettoyer**, l’**interroger** (filtres, moyennes, records), le **trier**, le **croiser** avec la table des stations, et **produire** un fichier CSV de bilan lisible dans un tableur.

!!! consignes "Consignes"

    - Un compte rendu court est demandé à la fin (partie 7).

    - Fichiers à télécharger (lien ci-dessus), à placer **dans le même dossier** : `releves_aout.csv`, `stations.csv` et `tp_donnees_tables_depart.py` (le programme à compléter : tout votre code s’y écrit).

    - Les données sont **fictives mais réalistes** (août 2025). Niveau : ★ échauffement, ★★ classique (niveau bac), ★★★ défi ; les *coups de pouce* et les *corrigés* se déplient sous chaque exercice.

    - <span class="run" title="À programmer et tester sur machine">▶</span> *À programmer et tester.* En bas du programme, des tests vérifient votre travail : à chaque lancement, chaque partie affiche `[OK]` ou `[A FAIRE]` (au début, tout est `[A FAIRE]` : c’est normal).

    - Usage de l’IA, indiqué sur chaque exercice : <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> aucune ; <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> en appui (déboguer, reformuler, vérifier ; la réponse finale est écrite et comprise par vous) ; <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> l’exercice s’appuie sur une réponse d’IA. Voir la [charte d’usage de l’IA](../charte.md).

## Prise en main : importer la table

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 1</span> — Regarder le fichier avant de programmer <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-08-les-donnees-en-tables-tp-1-1 }

Ouvrir `releves_aout.csv` dans un **éditeur de texte** (pas dans le tableur). En voici le début :

```text
station;date;tmin;tmax;pluie
MON;2025-08-01;23,1;29,0;0,0
MON;2025-08-02;22,2;27,2;0,0
```

1.  Quels sont les **descripteurs** ? Quel est le **séparateur** ? Pourquoi n’est-ce pas la virgule ?

2.  Que représentent `tmin`, `tmax` et `pluie` (unités probables) ? Sous quel format les dates sont-elles écrites ?

3.  Ouvrir aussi `stations.csv`. Quel descripteur est **commun** aux deux fichiers ?

??? corrige "Corrigé"

    Tous les résultats ci-dessous ont été obtenus en exécutant le programme corrigé sur les fichiers fournis (193 lignes de relevés, 6 stations). Les fonctions complètes sont regroupées en fin de document.

    ```python
    def en_nombre(texte):
        if texte == "":
            return None
        return float(texte.replace(",", "."))

    def est_complete(ligne):
        return ligne["tmin"] != "" and ligne["tmax"] != "" and ligne["pluie"] != ""

    def compter_par_cle(table):
        compteur = {}
        for ligne in table:
            cle = (ligne["station"], ligne["date"])
            if cle in compteur:
                compteur[cle] = compteur[cle] + 1
            else:
                compteur[cle] = 1
        return compteur

    def doublons(table):
        compteur = compter_par_cle(table)
        return [cle for cle in compteur if compteur[cle] > 1]

    def est_coherente(ligne):
        if not est_complete(ligne):
            return False
        tmin = en_nombre(ligne["tmin"])
        tmax = en_nombre(ligne["tmax"])
        return tmin <= tmax and -30 <= tmin <= 50 and -30 <= tmax <= 50

    def nettoyer(table):
        propre = []
        deja_vus = {}
        for ligne in table:
            cle = (ligne["station"], ligne["date"])
            if est_coherente(ligne) and cle not in deja_vus:
                deja_vus[cle] = True
                propre.append({"station": ligne["station"], "date": ligne["date"],
                               "tmin": en_nombre(ligne["tmin"]),
                               "tmax": en_nombre(ligne["tmax"]),
                               "pluie": en_nombre(ligne["pluie"])})
        return propre

    def releves_de(table, station):
        return [ligne for ligne in table if ligne["station"] == station]

    def moyenne(table, descripteur):
        total = 0
        for ligne in table:
            total = total + ligne[descripteur]
        return total / len(table)

    def jour_le_plus_chaud(table):
        champion = table[0]
        for ligne in table:
            if ligne["tmax"] > champion["tmax"]:
                champion = ligne
        return champion["station"], champion["date"], champion["tmax"]

    def compter_si(table, descripteur, seuil):
        n = 0
        for ligne in table:
            if ligne[descripteur] >= seuil:
                n = n + 1
        return n
    ```

    **1.** Descripteurs : `station`, `date`, `tmin`, `tmax`, `pluie`. Séparateur : le **point-virgule**, car la virgule sert déjà de séparateur décimal (`23,1`). **2.** Températures minimale et maximale de la journée en degrés Celsius, hauteur de pluie en millimètres ; dates au format `AAAA-MM-JJ`. **3.** Le descripteur commun est `station` (un code de trois lettres).

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 2</span> — Charger les deux tables <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-les-donnees-en-tables-tp-1-2 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

La fonction `charger(fichier, separateur)` est donnée : c’est celle du cours, avec en plus le paramètre `delimiter` de `csv.DictReader`.

1.  Charger les deux fichiers dans des variables `releves` et `stations`. Afficher le nombre de lignes de chaque table, puis `releves[0]`.

2.  Essayer `charger("releves_aout.csv", ",")`. Que contient alors `releves[0]` ? Expliquer.

3.  De quel type est `releves[0]["tmax"]` ? Pourquoi `float(releves[0]["tmax"])` provoque-t-il une erreur ?

??? corrige "Corrigé"

    **1.** `len(releves)` vaut **193**, `len(stations)` vaut **6** ; `releves[0]` est `{’station’: ’MON’, ’date’: ’2025-08-01’, ’tmin’: ’23,1’, ’tmax’: ’29,0’, ’pluie’: ’0,0’}`.

    **2.** Avec `","`, l’en-tête n’est qu’une seule colonne nommée `’station;date;tmin;tmax;pluie’`, et chaque ligne est découpée au milieu des nombres : `releves[0]` vaut `{’station;date;tmin;tmax;pluie’: ’MON;2025-08-01;23’, None: [’1;29’, ’0;0’, ’0’]}`. Le mauvais séparateur ne provoque *aucune erreur* : il produit silencieusement une table absurde.

    **3.** C’est une chaîne (`str`). `float("29,0")` échoue (`ValueError`) car Python attend un **point** décimal.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 3</span> — Convertir un nombre « à la française » <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-les-donnees-en-tables-tp-1-3 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Compléter `en_nombre(texte)` qui convertit une valeur lue dans le fichier en `float` (`"23,4"` donne `23.4`) et renvoie `None` si la chaîne est vide (valeur manquante).

??? pouce "Coup de pouce"

    Les chaînes ont une méthode `replace` : `"23,4".replace(",", ".")` vaut `"23.4"`.

```python
>>> en_nombre("23,4")
23.4
>>> en_nombre("") is None
True
```

??? corrige "Corrigé"

    ```python
    def en_nombre(texte):
        if texte == "":
            return None
        return float(texte.replace(",", "."))
    ```

## Contrôle qualité : repérer les lignes douteuses

Avant de calculer quoi que ce soit, un analyste **vérifie** ses données. Une seule valeur absurde suffit à fausser une moyenne ou un record.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 4</span> — Les valeurs manquantes <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-les-donnees-en-tables-tp-1-4 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Compléter `est_complete(ligne)`, qui renvoie `True` si `tmin`, `tmax` et `pluie` sont toutes renseignées. Afficher ensuite, par une **compréhension**, la station et la date des lignes incomplètes. Combien y en a-t-il ?

??? corrige "Corrigé"

    La compréhension

    ```python
    [(l["station"], l["date"]) for l in releves if not est_complete(l)]
    ```

    donne **2** lignes : `(’NIC’, ’2025-08-07’)` (`tmax` vide) et `(’SOS’, ’2025-08-23’)` (`tmin` vide).

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 5</span> — Les doublons <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-les-donnees-en-tables-tp-1-5 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Une même station ne doit envoyer qu’**un** relevé par jour : la clé d’une ligne est le couple `(station, date)`.

1.  Compléter `compter_par_cle(table)`, qui renvoie un **dictionnaire** associant à chaque clé `(station, date)` le nombre de lignes qui la portent.

    ??? pouce "Coup de pouce"

        C’est le patron du comptage avec un dictionnaire : si la clé est déjà présente, on ajoute 1 ; sinon on la crée avec la valeur 1.

2.  En déduire `doublons(table)`, la liste des clés présentes plus d’une fois. Quelles sont-elles ?

3.  Afficher les lignes de chacun de ces doublons. Sont-ils tous **identiques** ? Lequel pose un vrai problème ?

??? corrige "Corrigé"

    **1.** Patron du comptage : si la clé est déjà dans `compteur`, on ajoute 1, sinon on la crée avec la valeur 1 (code complet de `compter_par_cle` et de `doublons` en fin de document).

    **2.** Trois clés en double : `(’MON’, ’2025-08-14’)`, `(’NIC’, ’2025-08-15’)`, `(’SOS’, ’2025-08-02’)`. **3.** Les doublons de Monaco et de Sospel sont **identiques** (relevé transmis deux fois : sans gravité). Celui de Nice est **conflictuel** : `tmax` vaut `30,4` dans la première ligne et `30,8` dans la seconde. On ne peut pas savoir laquelle est juste : on garde la première par convention, mais il faudrait le **signaler**.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Les valeurs incohérentes <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-les-donnees-en-tables-tp-1-6 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Compléter `est_coherente(ligne)` : elle renvoie `True` si la ligne est complète, si `tmin` $\leqslant$ `tmax`, et si les deux températures sont comprises entre $-30$ et $50$ degrés. Lister les lignes complètes mais incohérentes et proposer, pour chacune, une **explication** plausible de l’erreur.

??? corrige "Corrigé"

    Trois lignes complètes mais incohérentes :

    - `MEN`, 12 août : `tmin = 32,9` et `tmax = 25,8` ; `ANT`, 28 août : `tmin = 29,5` et `tmax = 20,3` $\to$ les deux colonnes ont manifestement été **inversées** à la saisie ;

    - `GRE`, 5 août : `tmax = 99,9` $\to$ valeur impossible (à 1 400 m d’altitude !) : **capteur défectueux** ou code d’erreur.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Nettoyer la table <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-les-donnees-en-tables-tp-1-7 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Compléter `nettoyer(table)`, qui construit une **nouvelle** table :

- ne garde que les lignes complètes et cohérentes ;

- ne garde, pour chaque clé `(station, date)`, que la **première** ligne rencontrée (un dictionnaire `deja_vus` retient les clés déjà gardées) ;

- range dans chaque nouvelle fiche des **nombres** (`float`) et non plus des chaînes.

Combien de lignes reste-t-il ? Combien ont été écartées ? **Tout le reste du TP utilise la table nettoyée**, notée `propre`.

??? pouce "Coup de pouce"

    Pour chaque ligne : si elle est cohérente et que sa clé n’est pas dans `deja_vus`, on enregistre la clé, puis on ajoute à `propre` un nouveau dictionnaire dont les trois valeurs numériques passent par `en_nombre`.

??? corrige "Corrigé"

    Il reste **185** lignes ; **8** ont été écartées : 2 incomplètes, 3 incohérentes, 3 doublons. (On pourrait « réparer » les deux inversions plutôt que les supprimer : bonne idée à discuter, mais c’est une décision d’analyste à justifier.)

## Interroger la table : filtres et calculs

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 8</span> — Une station à la loupe <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-les-donnees-en-tables-tp-1-8 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Compléter `releves_de(table, station)` (filtre par compréhension) et `moyenne(table, descripteur)`. Pour Monaco (`"MON"`), afficher le nombre de relevés et la moyenne des températures maximales, arrondie au dixième avec `round(x, 1)`.

??? corrige "Corrigé"

    Monaco : **31** relevés, moyenne des `tmax` : **29,1** degrés.

    ```python
    monaco = releves_de(propre, "MON")
    print(len(monaco), round(moyenne(monaco, "tmax"), 1))     # 31 29.1
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 9</span> — Records et comptages <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-les-donnees-en-tables-tp-1-9 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

1.  Compléter `jour_le_plus_chaud(table)`, qui renvoie le triplet `(station, date, tmax)` de la ligne où `tmax` est maximale (invariant du champion). Quel est le record du mois, toutes stations confondues ? Et celui de Monaco ?

2.  Compléter `compter_si(table, descripteur, seuil)`, qui compte les lignes dont la valeur est $\geqslant$ `seuil`. Une **nuit tropicale** est une nuit où la température ne descend pas sous **20 degrés** : combien Monaco en a-t-elle connu ? Et Gréolières ?

3.  Un **jour de pluie** est un jour avec au moins **1 mm**. Pour chaque station, afficher le cumul de pluie du mois et le nombre de jours de pluie (une boucle sur la table `stations`).

??? corrige "Corrigé"

    **1.** Record du mois : `(’SOS’, ’2025-08-11’, 34.4)`, à Sospel ; record de Monaco : `(’MON’, ’2025-08-13’, 32.1)`.

    **2.** Monaco : **31** nuits tropicales sur 31 ; Gréolières : **0**.

    **3.** Cumul de pluie (mm) et jours de pluie :

    |                        | Monaco | Menton | Nice | Antibes | Sospel | Gréolières |
    |:-----------------------|:------:|:------:|:----:|:-------:|:------:|:----------:|
    | cumul (mm)             |  34,0  |  38,2  | 23,1 |  47,4   |  96,4  |   115,6    |
    | jours $\geqslant 1$ mm |   4    |   2    |  4   |    3    |   7    |     9      |

    ```python
    for s in stations:
        r = releves_de(propre, s["station"])
        cumul = 0
        for ligne in r:
            cumul = cumul + ligne["pluie"]
        print(s["nom"], round(cumul, 1), compter_si(r, "pluie", 1))
    ```

    *Autre méthode :* pour le cumul, construire par compréhension la liste des hauteurs de pluie de la station, puis l’additionner avec `sum` : `cumul = sum([ligne["pluie"] for ligne in r])`.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 10</span> — L’épisode orageux <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-les-donnees-en-tables-tp-1-10 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

On veut maintenant regrouper les relevés **par date**, toutes stations confondues.

1.  Écrire `pluie_par_jour(table)` qui renvoie un **dictionnaire** associant à chaque date le cumul de pluie de toutes les stations ce jour-là. Combien de clés contient-il ?

2.  Quel jour le réseau a-t-il été le plus arrosé, et combien de millimètres sont tombés au total ? Quel autre jour le suit de près ?

3.  Combien de jours du mois n’a-t-il plu **nulle part** ?

??? pouce "Coup de pouce"

    Même patron que `compter_par_cle` : la clé est la date, et au lieu d’ajouter 1, on ajoute la pluie de la ligne. Pour le jour le plus arrosé, appliquer l’invariant du champion aux clés du dictionnaire.

??? corrige "Corrigé"

    ```python
    def pluie_par_jour(table):
        cumul = {}
        for ligne in table:
            d = ligne["date"]
            if d in cumul:
                cumul[d] = cumul[d] + ligne["pluie"]
            else:
                cumul[d] = ligne["pluie"]
        return cumul

    cumul = pluie_par_jour(propre)
    jour_max = None
    for d in cumul:
        if jour_max is None or cumul[d] > cumul[jour_max]:
            jour_max = d
    print(len(cumul), jour_max, round(cumul[jour_max], 1))
    print(len([d for d in cumul if cumul[d] == 0]))
    ```

    **1.** 31 clés (une par jour d’août). **2.** Le **20 août** (132,5 mm au total), suivi de près par le **19 août** (127,8 mm) : c’est l’épisode orageux, très loin devant le 28 août (13,5 mm). **3.** **14** jours sans aucune pluie sur le réseau.

## Trier

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 11</span> — Palmarès <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-les-donnees-en-tables-tp-1-11 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

1.  Avec `sorted` et une clé, afficher les **cinq** journées les plus chaudes du mois (station, date, `tmax`). Que remarquez-vous ?

2.  Construire la liste des couples `(nom de la station, cumul de pluie)` et la trier du plus arrosé au plus sec.

3.  Les dates sont écrites `AAAA-MM-JJ`. Comparer `sorted(["2025-08-15", "2025-09-02", "2025-08-20"])` et `sorted(["15/08/2025", "02/09/2025", "20/08/2025"])`. Pourquoi les informaticiens préfèrent-ils le premier format ?

??? corrige "Corrigé"

    **1.** Les cinq journées les plus chaudes sont **toutes à Sospel** : 11 août (34,4), 12 août (34,1), 14 août (34,0), 13 août (33,7), 9 août (33,4). L’arrière-pays, loin de la mer, chauffe davantage ; la vague de chaleur se situe vers le 10–16 août.

    ```python
    top = sorted(propre, key=lambda l: l["tmax"], reverse=True)
    for l in top[:5]:
        print(l["station"], l["date"], l["tmax"])
    ```

    **2.** Gréolières (115,6), Sospel (96,4), Antibes (47,4), Menton (38,2), Monaco (34,0), Nice (23,1).

    ```python
    pluies = []
    for s in stations:
        r = releves_de(propre, s["station"])
        pluies.append((s["nom"], round(moyenne(r, "pluie") * len(r), 1)))
    print(sorted(pluies, key=lambda c: c[1], reverse=True))
    ```

    **3.** `[’2025-08-15’, ’2025-08-20’, ’2025-09-02’]` est dans l’ordre chronologique ; `[’02/09/2025’, ’15/08/2025’, ’20/08/2025’]` ne l’est pas (le 2 septembre passe en premier). Les chaînes se comparent caractère par caractère : avec l’année, puis le mois, puis le jour, l’ordre « des mots » coïncide avec l’ordre du temps. C’est le format international **ISO 8601**.

## Croiser : la jointure avec la table des stations

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 12</span> — Littoral ou arrière-pays ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-les-donnees-en-tables-tp-1-12 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

La fonction `jointure` du cours est fournie dans le programme.

1.  Calculer la jointure de `propre` et de `stations` sur le descripteur `"station"`. Combien de lignes obtient-on ? Comparer avec `len(propre)` : quelles lignes ont **disparu**, et pourquoi ? Comment un analyste devrait-il réagir ?

2.  Grâce au descripteur `littoral` apporté par la jointure, comparer la moyenne des `tmin` des stations du littoral et celle des stations de l’arrière-pays. Même question pour les `tmax`.

3.  Calculer, pour les deux groupes, l’**écart moyen** entre `tmax` et `tmin`. Proposer une explication (la mer, l’altitude).

4.  La station `VIL` est celle de **Villefranche-sur-Mer** (altitude 10 m, sur le littoral). Ajouter sa fiche à la table `stations` avec `append` (un dictionnaire ayant les mêmes descripteurs que les autres fiches), puis refaire la jointure : combien de lignes obtient-on maintenant ?

??? corrige "Corrigé"

    **1.** La jointure compte **181** lignes contre **185** : les 4 relevés de la station `VIL` (absente de `stations.csv`) ont disparu, faute de correspondance. Un analyste doit le **remarquer** (comparer les effectifs avant et après) et compléter la table des stations plutôt que de perdre ces données sans le dire.

    **2. et 3.**

    |              | lignes | moyenne `tmin` | moyenne `tmax` | écart moyen |
    |:-------------|:------:|:--------------:|:--------------:|:-----------:|
    | littoral     |  121   |      22,6      |      29,4      |     6,7     |
    | arrière-pays |   60   |      14,6      |      27,5      |    13,0     |

    La mer, lente à se réchauffer et à se refroidir, **adoucit** les écarts : nuits chaudes, journées modérées. Dans l’arrière-pays, l’écart jour/nuit est deux fois plus grand ; l’altitude (Gréolières, 1 400 m) abaisse en plus toutes les températures, ce qui explique une moyenne des `tmax` plus basse malgré les records de Sospel.

    **4.** Après

    ```python
    stations.append({"station": "VIL", "nom": "Villefranche-sur-Mer",
                     "commune": "Villefranche-sur-Mer", "altitude": "10",
                     "littoral": "oui"})
    ```

    la jointure compte **185** lignes : plus aucun relevé n’est perdu. (Pour les questions 2 et 3, les valeurs du tableau ont été calculées *avant* cet ajout.)

    ```python
    j = jointure(propre, stations, "station")
    littoral = [l for l in j if l["littoral"] == "oui"]
    arriere = [l for l in j if l["littoral"] == "non"]
    for groupe in (littoral, arriere):
        print(round(moyenne(groupe, "tmin"), 1), round(moyenne(groupe, "tmax"), 1),
              round(moyenne(groupe, "tmax") - moyenne(groupe, "tmin"), 1))
    ```

## Produire : exporter un CSV de bilan

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 13</span> — Le fichier `bilan_stations.csv` <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-les-donnees-en-tables-tp-1-13 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

1.  Compléter `en_texte(nombre)`, réciproque de `en_nombre` : `en_texte(23.4)` vaut `"23,4"`.

2.  Construire une table `bilan` contenant **une fiche par station**, avec les descripteurs `station`, `nom`, `tmin_moy`, `tmax_moy`, `pluie_totale`, `nuits_tropicales` (moyennes et cumul arrondis au dixième, écrits avec `en_texte`).

3.  Compléter la fonction `exporter` (une ligne manque : écrire chaque fiche avec `ecrivain.writerow`) et produire `bilan_stations.csv`, séparateur `;`.

4.  Vérifier le résultat de deux façons : en le rechargeant avec `charger`, puis en l’ouvrant dans le **tableur**. Les nombres sont-ils bien reconnus ?

!!! remarque "Remarque — Pourquoi écrire 23,4 et pas 23.4 ?"

    Un tableur réglé en français attend une virgule décimale ; avec `23.4`, il risque de lire du texte, voire une date. Produire un fichier, c’est penser à **celui qui va le relire**.

??? corrige "Corrigé"

    ```python
    def en_texte(nombre):
        return str(nombre).replace(".", ",")

    bilan = []
    for s in stations:
        r = releves_de(propre, s["station"])
        bilan.append({"station": s["station"], "nom": s["nom"],
                      "tmin_moy": en_texte(round(moyenne(r, "tmin"), 1)),
                      "tmax_moy": en_texte(round(moyenne(r, "tmax"), 1)),
                      "pluie_totale": en_texte(round(moyenne(r, "pluie") * len(r), 1)),
                      "nuits_tropicales": compter_si(r, "tmin", 20)})
    exporter(bilan, "bilan_stations.csv", ";")
    ```

    La boucle parcourt la table `stations`, qui contient **sept** fiches depuis l’ajout de `VIL` (exercice 12, question 4). La ligne manquante de `exporter` est la boucle `for ligne in table: ecrivain.writerow(ligne)`. Fichier obtenu :

    ```text
    station;nom;tmin_moy;tmax_moy;pluie_totale;nuits_tropicales
    MON;Monaco;23,4;29,1;34,0;31
    MEN;Menton;22,9;29,6;38,2;30
    NIC;Nice;22,4;29,2;23,1;29
    ANT;Antibes;21,7;29,5;47,4;29
    SOS;Sospel;17,0;31,2;96,4;0
    GRE;Gréolières;12,1;23,9;115,6;0
    VIL;Villefranche-sur-Mer;23,2;28,8;1,2;4
    ```

    La fiche de `VIL` ne repose que sur **4** relevés : ses moyennes sont bien moins fiables que celles des autres stations (une trentaine de relevés chacune), il faut le signaler. Rechargé avec `charger(..., ";")`, on retrouve 7 fiches (dont toutes les valeurs sont redevenues des chaînes !). Dans un tableur réglé en français, les nombres doivent être reconnus comme tels (alignés à droite, utilisables dans une formule) ; avec des points décimaux, ce n’est pas garanti.

## Pour aller plus loin, et compte rendu

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 14</span> — La plus longue vague de chaleur <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-les-donnees-en-tables-tp-1-14 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Écrire `plus_longue_serie(table, seuil)` qui renvoie le plus grand nombre de **jours consécutifs** où `tmax` $\geqslant$ `seuil`, pour une table ne contenant qu’une station. Quelle station a connu la plus longue série de jours à 30 degrés ou plus ? *Attention : la table doit être parcourue dans l’ordre des dates, et il peut manquer des jours.*

??? pouce "Coup de pouce"

    Trier d’abord les relevés par date. Garder deux compteurs : la longueur de la série en cours (remise à 0 dès qu’un jour est sous le seuil) et la meilleure longueur vue jusque-là.

??? corrige "Corrigé"

    ```python
    def plus_longue_serie(table, seuil):
        meilleure = 0
        en_cours = 0
        jour_precedent = 0
        for ligne in sorted(table, key=lambda l: l["date"]):
            jour = int(ligne["date"][8:10])          # "2025-08-13" -> 13
            if ligne["tmax"] >= seuil and jour == jour_precedent + 1:
                en_cours = en_cours + 1
            elif ligne["tmax"] >= seuil:
                en_cours = 1                          # un jour manque : on repart
            else:
                en_cours = 0
            if en_cours > meilleure:
                meilleure = en_cours
            jour_precedent = jour
        return meilleure
    ```

    Séries à 30 degrés ou plus : Monaco 9, Menton 5, Nice 7, Antibes 8, **Sospel 11**, Gréolières 0. La plus longue vague de chaleur est donc à **Sospel** (11 jours). *Si l’on ne tient pas compte des jours manquants* (version qui remet seulement le compteur à 0 sous le seuil), Menton obtient 8 au lieu de 5 : le relevé écarté du 12 août « recolle » artificiellement deux séries. La réponse finale (Sospel) ne change pas, mais la version simple n’est correcte que si l’on signale cette limite.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 15</span> — <span class="horsprog">au-delà du programme</span> La même chose avec `pandas` <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-les-donnees-en-tables-tp-1-15 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

*Si la bibliothèque `pandas` est installée.* Les scientifiques des données écrivent ce TP en quelques lignes :

```python
import pandas
t = pandas.read_csv("releves_aout.csv", sep=";", decimal=",")
t = t.dropna()                                        # lignes incompletes
t = t[(t["tmin"] <= t["tmax"]) & (t["tmax"] <= 50)]   # lignes incoherentes
t = t.drop_duplicates(subset=["station", "date"])     # doublons
print(t.groupby("station")["tmax"].mean().round(1))
```

Exécuter ce code et comparer avec vos moyennes. Une station apparaît ici alors qu’elle avait disparu de votre première jointure (exercice 12, question 1) : laquelle, et pourquoi ? Qu’est-ce que votre propre code vous a appris que ces cinq lignes cachent ?

??? corrige "Corrigé"

    Les moyennes coïncident avec les nôtres (Sospel 31,2 ; Menton 29,6 ; Antibes 29,5 ; Nice 29,2 ; Monaco 29,1 ; Gréolières 23,9). La station `VIL` apparaît aussi (28,8) alors qu’elle avait disparu de notre première jointure : le code `pandas` ne fait **pas de jointure** avec la table des stations, il ne « perd » donc pas ces lignes. Ce que notre code a appris : *chaque* étape (séparateur, virgule décimale, doublons, lignes perdues par la jointure) est une décision ; `pandas` les rend invisibles, mais elles existent toujours.

### <span class="exo-num">Exercice 16</span> — Compte rendu <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-les-donnees-en-tables-tp-1-16 }

Rédiger, en quelques lignes, un compte rendu (dans un fichier texte placé à côté du programme, ou sur le cahier) :

1.  combien de lignes le fichier contenait, combien ont été écartées, et pour quelles raisons ;

2.  trois résultats chiffrés tirés de votre bilan (un record, une comparaison littoral/arrière-pays, un classement) ;

3.  une phrase sur ce qui se serait passé si l’on avait calculé les records **sans** nettoyer la table.

??? corrige "Corrigé"

    Attendus : 193 lignes lues, 8 écartées (2 incomplètes, 3 incohérentes dont 2 inversions et une valeur à 99,9, 3 doublons dont un conflictuel), 4 relevés perdus par la jointure ; trois résultats chiffrés exacts ; sans nettoyage, le « record » du mois aurait été **99,9 degrés à Gréolières**, et les moyennes auraient planté (valeurs vides) ou été faussées.

## <span class="etiquette">Projet</span> Les prénoms de l’INSEE

*filtrer, trier, regrouper et croiser un vrai fichier de données publiques*

<p class="infos-activite">Durée : 2 à 3 séances · En binôme, sur machine</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/08-projet-prenoms-insee){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/premiere-08-projet-prenoms-insee.zip){ .md-button }

!!! encadre "But du projet"

    Depuis 1900, l’INSEE compte, année après année, les prénoms donnés aux enfants nés en France, et publie ces données en accès libre. Vous allez explorer ce fichier **réel** avec Python, **sans bibliothèque spécialisée** : l’**importer** et le **nettoyer**, l’**interroger** (popularité d’un prénom, palmarès d’une année), **regrouper** ses lignes avec un dictionnaire, **trier**, **croiser** deux tables et **tracer** des courbes. Pour finir, chaque binôme pose **sa propre question** aux données, la traite et présente sa réponse à la classe.

!!! consignes "Consignes"

    - Plus la restitution (partie 8). Les parties 2 à 7 sont guidées, la partie 8 est libre.

    - Fichiers à télécharger (lien ci-dessus), à placer **dans le même dossier** : `prenoms_insee_extrait.csv` (les données), `projet_prenoms_evenements.csv` (une petite table pour la partie 6) et `projet_prenoms_insee_depart.py` (le programme à compléter : tout votre code s’y écrit).

    - <span class="run" title="À programmer et tester sur machine">▶</span> *À programmer.* À chaque exécution, le programme teste vos fonctions et affiche, pour chaque partie, `OK` ou `ECHEC`. Au début, tout est en échec : c’est normal. Niveau : ★ échauffement, ★★ classique (niveau bac), ★★★ défi ; les *coups de pouce* et les *corrigés* se déplient sous chaque exercice.

    - Usage de l’IA, indiqué sur chaque exercice : <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> aucune ; <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> en appui (déboguer, reformuler, vérifier ; la réponse finale est écrite et comprise par vous) ; <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> l’exercice s’appuie sur une réponse d’IA. Voir la [charte d’usage de l’IA](../charte.md).

!!! encadre "Les données"

    **Source** : Insee, *Fichier des prénoms*, édition 2025 (parue en juillet 2026), fichier national : naissances en France de 1900 à 2025. Données publiées sous **licence ouverte** (Etalab 2.0) : on peut les copier, les transformer et les rediffuser librement, à condition de **citer la source**. Page de téléchargement : `www.insee.fr/fr/statistiques/8595130`.

    Le fichier complet compte près de 725 000 lignes (16 Mo). L’extrait fourni a été fabriqué par un petit programme (`projet_prenoms_extraire.py`) qui garde le **même format** mais seulement les naissances de **1950 à 2025** et les lignes dont l’effectif atteint **au moins 100**.

## Découvrir le fichier

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 1</span> — Regarder avant de programmer <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-08-les-donnees-en-tables-tp-2-1 }

Ouvrir `prenoms_insee_extrait.csv` dans un **éditeur de texte**. En voici le début :

```text
sexe;prenom;periode;valeur;rang
1;GABRIEL;2025;4625;1
1;NOAH;2025;3465;2
1;LÉO;2025;3420;3
```

1.  Quels sont les descripteurs ? Quel est le séparateur ? Comment le sexe est-il codé (chercher `LOUISE`) ?

2.  Comment les prénoms sont-ils écrits ? Que vaut le dernier chiffre de *toutes* les valeurs de `valeur` ? D’après la documentation de l’INSEE, les effectifs sont **arrondis au multiple de 5 le plus proche** : pourquoi, à votre avis ?

3.  Le cours rappelle l’ancien en-tête `sexe;preusuel;annais;nombre`, celui des **éditions précédentes** du fichier. Quelle leçon en tirer pour un programme qui lit des données publiques ?

4.  Le prénom Léo n’apparaît pas en 1980 dans l’extrait. Peut-on en conclure qu’aucun Léo n’est né en 1980 ?

## Importer et nettoyer

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 2</span> — Charger la table <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-les-donnees-en-tables-tp-2-2 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Écrire `charger(fichier, separateur)` : c’est la fonction du cours, avec en plus le paramètre `delimiter` de `csv.DictReader`. Charger l’extrait dans une variable `brut`. Combien de lignes contient-il ? Afficher `brut[0]` : de quel type sont les valeurs ?

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 3</span> — Une fiche propre <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-les-donnees-en-tables-tp-2-3 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Pour travailler confortablement, on transforme chaque ligne brute en une **nouvelle** fiche, plus lisible. Compléter `convertir(ligne)` :

```text
>>> convertir({"sexe": "1", "prenom": "LÉO", "periode": "2025", "valeur": "3420", "rang": "3"})
{'sexe': 'G', 'prenom': 'Léo', 'annee': 2025, 'nombre': 3420, 'rang': 3}
```

??? pouce "Coup de pouce"

    La méthode `title` des chaînes met une majuscule au début de chaque mot et des minuscules ailleurs : `"JEAN-PIERRE".title()` vaut `"Jean-Pierre"`.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 4</span> — Un programme robuste <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-les-donnees-en-tables-tp-2-4 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Les éditions précédentes du fichier contenaient des lignes qui ne décrivent pas un vrai prénom une année connue : le prénom `_PRENOMS_RARES` (le cumul des prénoms trop rares, regroupés pour qu’on ne puisse pas reconnaître les personnes) et l’année `XXXX` (année de naissance inconnue). L’extrait n’en contient pas, mais votre programme doit pouvoir lire *aussi* ces anciennes éditions.

1.  Compléter `est_valide(ligne)`, qui renvoie `False` si le prénom commence par `_` ou si l’année n’est pas écrite avec des chiffres.

    ??? pouce "Coup de pouce"

        Les chaînes ont deux méthodes utiles : `"_PRENOMS".startswith("_")` vaut `True` et `"XXXX".isdigit()` vaut `False`.

2.  Un camarade propose plutôt le test `"RARES" in ligne["prenom"]`. Or le fichier complet contient la ligne `1;RARES;2025;15;2053`. Que décrit-elle ? Pourquoi ce test serait-il une erreur ?

3.  Compléter `nettoyer(table)`, qui renvoie la table des fiches converties, pour les seules lignes valides. **Toute la suite utilise cette table nettoyée**, notée `table`.

## Interroger la table

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 5</span> — Combien de Louise ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-les-donnees-en-tables-tp-2-5 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Compléter `nombre_de(table, prenom, sexe, annee)`, qui renvoie le nombre de naissances, ou `0` si la table ne contient pas de ligne correspondante. Combien de Louise sont nées en 1950, en 1975, en 2000, en 2025 ? Que signifie exactement le `0` renvoyé pour 1975 ?

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — La carrière d’un prénom <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-les-donnees-en-tables-tp-2-6 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

1.  Compléter `evolution(table, prenom, sexe)`, qui renvoie un **dictionnaire** `{annee: nombre}`. En combien d’années le prénom Kevin figure-t-il dans l’extrait ? Quelle est la première ?

2.  Compléter `annee_record(table, prenom, sexe)`, qui renvoie le couple `(annee, nombre)` de l’année la plus forte (invariant du champion sur les clés du dictionnaire). Donner l’année record de Marie, de Kevin, de Léo et de Jade. Pourquoi le record de Marie est-il à prendre avec précaution ?

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Le top 10 d’une année <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-les-donnees-en-tables-tp-2-7 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Compléter `top(table, annee, sexe, n)`, qui renvoie la liste des `n` couples `(prenom, nombre)` les plus donnés. Afficher le top 10 de 2025 pour les filles et pour les garçons, puis celui de 1950. Vérifier votre classement grâce au descripteur `rang`.

## Regrouper avec un dictionnaire

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — Totaliser sur plusieurs années <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-les-donnees-en-tables-tp-2-8 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Compléter `total_par_prenom(table, sexe, debut, fin)`, qui renvoie un dictionnaire associant à chaque prénom le total de ses naissances de `debut` à `fin` (inclus), puis `champion(dico)`, qui renvoie le couple `(cle, valeur)` de la plus grande valeur. Quel prénom de fille a été le plus donné de 2020 à 2025, et combien de fois ?

??? pouce "Coup de pouce"

    C’est le patron du comptage avec un dictionnaire, mais au lieu d’ajouter 1, on ajoute le nombre de la fiche.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 9</span> — Le prénom de chaque décennie <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-les-donnees-en-tables-tp-2-9 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Compléter `plus_donne_par_decennie(table, sexe)`, qui renvoie un dictionnaire `{1950: (prenom, total), 1960: …, 2020: …}`. Présenter les résultats des filles et des garçons dans un tableau. Pourquoi la décennie 2020 n’est-elle pas comparable aux autres ?

??? pouce "Coup de pouce"

    Une boucle `for debut in range(1950, 2030, 10)`, et dans la boucle, un appel à `champion` sur le résultat de `total_par_prenom`.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 10</span> — Des prénoms de plus en plus variés ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-les-donnees-en-tables-tp-2-10 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Compléter `diversite(table, annee, sexe)`, qui renvoie le nombre de prénoms différents de l’année, le total des naissances correspondantes et la **part du top 10** dans ce total (en pourcentage, arrondie au dixième). Comparer 1950, 1975, 2000 et 2025, pour chaque sexe, puis rédiger deux phrases de conclusion. Le total obtenu pour 2025 est-il le nombre de bébés nés en France cette année-là ?

## Trier

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 11</span> — Le palmarès de 1950 à 2025 <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-les-donnees-en-tables-tp-2-11 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Compléter `palmares(totaux, n)`, qui transforme le dictionnaire `totaux` en une liste de couples `(prenom, total)`, la trie avec `sorted` et une clé, et renvoie les `n` premiers. Afficher le palmarès des 10 prénoms les plus donnés de 1950 à 2025, pour chaque sexe. Combien de ces prénoms figurent dans un top 10 de 2025 ?

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 12</span> — Les ex aequo <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-les-donnees-en-tables-tp-2-12 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

1.  En 2025, deux prénoms de filles du top 20 ont exactement la même valeur. Lesquels ? Quel rang l’INSEE donne-t-il à chacun ?

2.  Compléter `classement(table, annee, sexe)`, qui renvoie la liste des prénoms de l’année du plus donné au moins donné et, **à égalité**, dans l’ordre alphabétique.

    ??? pouce "Coup de pouce"

        La clé de tri peut être un couple : Python compare d’abord les premiers éléments, puis les seconds en cas d’égalité. Avec la clé `(-nombre, prenom)`, les grands nombres passent devant.

3.  Votre classement et celui de l’INSEE diffèrent-ils sur ces deux prénoms ? Pourquoi l’INSEE peut-il les départager, et pas vous ?

## Croiser deux tables

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 13</span> — Qui monte, qui descend en dix ans ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-les-donnees-en-tables-tp-2-13 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

On veut comparer 2015 et 2025 par une **jointure** sur le descripteur `prenom` (la fonction `jointure` du cours est fournie).

1.  Pourquoi ne peut-on pas joindre directement les fiches de 2015 et celles de 2025 ? Que deviendrait le descripteur `nombre` dans la fiche fusionnée ?

2.  Compléter `colonne_annee(table, annee, sexe)`, qui renvoie des fiches réduites à deux descripteurs, comme `{"prenom": "Louise", "n2015": 4545}`.

3.  Compléter `montees(table, sexe, a1, a2)` (voir sa spécification dans le programme). Combien de prénoms de filles figurent à la fois en 2015 et en 2025 ? Quels sont les 5 plus fortes hausses et les 5 plus fortes baisses, chez les filles puis chez les garçons ?

4.  Les prénoms donnés en 2025 mais absents en 2015 ont **disparu** de la jointure. Compléter `nouveaux(table, sexe, a1, a2)` pour les retrouver. Combien y en a-t-il chez les garçons ? Expliquer la présence simultanée d’`Elio` parmi les hausses et d’`Élio` parmi les nouveaux.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 14</span> — L’effet d’un film, d’une série, d’un champion <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-les-donnees-en-tables-tp-2-14 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

On entend souvent qu’un film, une série ou un sportif lance la mode d’un prénom. Pour le vérifier, on dispose d’une petite table qui associe cinq prénoms à un événement et à son année (descripteurs `prenom`, `annee_evt`, `evenement`) : c’est le fichier `projet_prenoms_evenements.csv`.

1.  Charger cette table, convertir `annee_evt` en entier, puis calculer sa jointure avec `table` sur le descripteur `prenom`. Combien de lignes obtient-on ? Que contient chacune ?

2.  Compléter `avant_apres(fusion, prenom)` (voir sa spécification) et dresser, pour les cinq prénoms, le tableau : événement, nombre l’année d’avant, maximum dans les années qui suivent.

3.  Pour quels prénoms les données appuient-elles l’idée d’un « effet » ? Pour lequel la courbe montre-t-elle que la hausse avait commencé **bien avant** ? Un tableau de chiffres suffit-il à prouver qu’un événement est la *cause* d’une mode ?

## Tracer des courbes

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 15</span> — La courbe d’un prénom <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-les-donnees-en-tables-tp-2-15 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

La fonction `tracer` est presque complète : elle utilise la bibliothèque `matplotlib`, où `plt.plot(abscisses, ordonnees)` trace une courbe à partir de deux listes de même longueur.

1.  Compléter la ligne `nombres = ...` : une liste qui contient, pour chaque année de `annees`, le nombre de naissances, ou `0` si l’année est absente du dictionnaire `evo`.

2.  Tracer les courbes de Marie, Léa et Kevin, puis celles des cinq prénoms de la table des événements. Les courbes confirment-elles vos conclusions de l’exercice précédent ?

3.  Le fichier `courbes.png` produit servira pour la restitution.

## Votre question, votre réponse

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 16</span> — Une question posée aux données <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-les-donnees-en-tables-tp-2-16 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Chaque binôme formule **une question précise** à laquelle le fichier permet de répondre, la soumet au professeur, puis la traite en **réutilisant** les fonctions déjà écrites. Quelques pistes (on peut en choisir une autre) :

- les **prénoms composés** (`Marie-…`, `Jean-…`) : quelle part des naissances, décennie par décennie ?

- les prénoms **mixtes**, donnés aux filles *et* aux garçons la même année : lesquels, et depuis quand ?

- la **longueur moyenne** des prénoms (pondérée par le nombre de naissances) a-t-elle changé ?

- les **variantes d’orthographe** (Kevin, Kévin ; Eric, Éric ; Elio, Élio) : laquelle l’emporte, et quand ?

- la « **durée de vie** » d’une mode : pendant combien d’années un prénom reste-t-il au-dessus de la moitié de son record ?

- les prénoms de la **génération de vos parents** : que sont devenus les dix prénoms préférés de 1985 ?

Le binôme rend son programme (commenté) et prépare une **restitution** au choix : un **court oral** de 3 minutes devant la classe, ou une **affiche** A3. Dans les deux cas, on y trouve : la question ; la méthode (quelles fonctions, quels filtres, quels regroupements) ; le résultat, chiffré, avec au moins un tableau ou une courbe ; **une limite** des données qui pourrait fausser la réponse.

| **Critères d’évaluation** | **Observations** |
|:---|:--:|
| Parties 2 à 7 : fonctions écrites, tests `OK`, réponses aux questions |  |
| Question précise, à laquelle le fichier permet vraiment de répondre |  |
| Traitement : fonctions réutilisées, code lisible, commenté et testé |  |
| Résultat chiffré, présenté par un tableau ou une courbe lisible |  |
| Regard critique : une limite des données identifiée (seuil de 100, arrondi à 5, orthographes…) |  |
| Restitution claire, dans le temps imparti ; chaque membre du binôme sait expliquer le code |  |

## Pour aller plus loin

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 17</span> — Le fichier complet <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-les-donnees-en-tables-tp-2-17 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Télécharger le fichier national complet sur la page de l’INSEE (`www.insee.fr/fr/statistiques/8595130`, lien « Fichier national », archive `prenoms-2025-nat_csv.zip`), le décompresser, et relancer votre programme sur `prenoms-2025-nat.csv`. Combien de temps prend le chargement ? et la partie 6 (pensez au coût de la jointure) ? Les naissances de Léo en 1980, de Lilou en 1997 ou d’Arya en 2011 apparaissent-elles maintenant ? Quels résultats de votre projet changent ?

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 18</span> — <span class="horsprog">au-delà du programme</span> Et avec `pandas` ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-les-donnees-en-tables-tp-2-18 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

*Si la bibliothèque `pandas` est installée.* Exécuter le code suivant et retrouver deux résultats de votre projet. Qu’a dû deviner `pandas` que votre fonction `convertir` faisait explicitement ?

```python
import pandas
t = pandas.read_csv("prenoms_insee_extrait.csv", sep=";")
filles25 = t[(t["periode"] == 2025) & (t["sexe"] == 2)]
print(filles25.sort_values("valeur", ascending=False).head(3))
print(t[t["sexe"] == 1].groupby("prenom")["valeur"].sum().nlargest(3))
```
