# Exercices

<p class="sous-titre">Les données structurées et leur traitement</p>

!!! consignes "Mode d’emploi"

    - Niveau : ★ échauffement, ★★ classique (niveau bac), ★★★ défi ; les *coups de pouce* et les *corrigés* se déplient sous chaque exercice.

    - <span class="tag">sur papier</span> *à faire sur papier* ; \[ au tableur \]  *à réaliser au tableur* (LibreOffice Calc, Excel ou Google Sheets).

    - Plusieurs exercices utilisent la table *jeu* (ventes en millions d’exemplaires) et la table *studio* ci-dessous.

    - Usage de l’IA, indiqué sur chaque exercice : <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> aucune ; <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> en appui (déboguer, reformuler, vérifier ; la réponse finale est écrite et comprise par vous) ; <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> l’exercice s’appuie sur une réponse d’IA. Voir la charte d’usage de l’IA.

**Table *jeu* :**

| **id** | **titre** | **studio** | **annee** | **genre** | **pegi** | **ventes** |
|:--:|:---|:--:|:--:|:---|:--:|:--:|
| 1 | Minecraft | 2 | 2011 | bac à sable | 7 | 300 |
| 2 | GTA V | 3 | 2013 | action | 18 | 190 |
| 3 | Wii Sports | 1 | 2006 | sport | 7 | 83 |
| 4 | Mario Kart 8 | 1 | 2014 | course | 3 | 60 |
| 5 | Red Dead Redemption 2 | 3 | 2018 | action | 18 | 55 |
| 6 | Animal Crossing | 1 | 2020 | simulation | 3 | 45 |

**Table *studio* :**

| **id** | **nom**        | **pays**   |
|:------:|:---------------|:-----------|
|   1    | Nintendo       | Japon      |
|   2    | Mojang         | Suède      |
|   3    | Rockstar Games | États-Unis |

### Données, données personnelles, métadonnées

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 1</span> — Donnée personnelle ou pas ? <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-05-1 }

<span class="tag">sur papier</span>  Pour chaque information, dire si c’est une **donnée personnelle** (elle permet d’identifier une personne) ou non. Justifier en trois mots.

1.  l’adresse e-mail d’un élève ;

2.  la température qu’il fait à Monaco aujourd’hui ;

3.  le numéro de téléphone de votre voisin ;

4.  le nombre d’habitants de la France ;

5.  la position GPS enregistrée dans votre dernière photo.

??? corrige "Corrigé"

    1.  **Oui** : une adresse e-mail identifie une personne.

    2.  **Non** : la température ne concerne personne en particulier.

    3.  **Oui** : un numéro de téléphone est rattaché à une personne.

    4.  **Non** : un chiffre global, aucune personne identifiée.

    5.  **Oui** : la position GPS révèle *indirectement* où était la personne (souvent son domicile).

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 2</span> — Donnée ou métadonnée ? <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-05-2 }

<span class="tag">sur papier</span>  Vous prenez une photo. Classer en deux colonnes (**donnée** / **métadonnée**) : les pixels de l’image ; la date de la prise de vue ; le modèle de l’appareil ; le contenu visible (un chat) ; les coordonnées GPS ; le poids du fichier.

??? corrige "Corrigé"

    - **Donnée** (le contenu) : les pixels de l’image ; le chat visible sur la photo.

    - **Métadonnée** (ce qui décrit) : la date de prise de vue ; le modèle d’appareil ; les coordonnées GPS ; le poids du fichier.

### Lire une table

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 3</span> — Vocabulaire de la table <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-05-3 }

<span class="tag">sur papier</span>  À l’aide de la table *jeu* :

1.  Combien la table a-t-elle de **descripteurs** ? d’**enregistrements** ?

2.  Citer tous les descripteurs.

3.  Donner la valeur du descripteur `genre` pour l’enregistrement d’`id` `5`.

4.  Pourquoi le descripteur `titre` ferait-il un moins bon **identifiant** que `id` ? (une phrase)

??? corrige "Corrigé"

    1.  **7** descripteurs et **6** enregistrements.

    2.  `id`, `titre`, `studio`, `annee`, `genre`, `pegi`, `ventes`.

    3.  L’`id` `5` est *Red Dead Redemption 2*, de genre `action`.

    4.  Deux jeux pourraient porter le **même titre** (rééditions, versions) : le titre n’est pas forcément *unique*, contrairement à l’`id`.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 4</span> — Concevoir une table <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-05-4 }

<span class="tag">sur papier</span>  Le CDI du lycée veut enregistrer ses **prêts de livres** dans une table.

1.  Proposer au moins **quatre descripteurs** pour cette table.

2.  Lequel servira d’**identifiant** ? Pourquoi ne pas utiliser le nom de l’élève ?

3.  Écrire deux enregistrements possibles (on pourra les présenter sous forme de tableau).

??? pouce "Coup de pouce"

    Un descripteur est une colonne, un enregistrement est une ligne (ici, un prêt). Un identifiant doit être *unique* : deux élèves peuvent-ils porter le même nom ? Un même élève peut-il emprunter plusieurs fois ?

??? corrige "Corrigé"

    1.  Par exemple : `id_pret`, `titre_livre`, `nom_eleve`, `classe`, `date_pret`, `date_retour`.

    2.  L’identifiant est `id_pret`, un numéro **unique** pour chaque prêt. Le nom de l’élève ne convient pas : deux élèves peuvent porter le même nom, et un même élève emprunte plusieurs livres (son nom revient sur plusieurs lignes).

    3.  Par exemple :

        | **id_pret** | **titre_livre** | **nom_eleve** | **classe** | **date_pret** | **date_retour** |
        |:--:|:---|:---|:--:|:--:|:--:|
        | 1 | Le Petit Prince | Lina Rossi | 2nde 3 | 02/10 | 16/10 |
        | 2 | Le Petit Prince | Hugo Martin | 2nde 1 | 17/10 | 31/10 |

### Le format CSV

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 5</span> — Lire du CSV <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-05-5 }

<span class="tag">sur papier</span>  On donne le début d’un fichier CSV public (jeux de société d’une médiathèque) :

```text
titre;editeur;duree;age_min
Les Aventuriers du Rail;Days of Wonder;45;8
Dixit;Libellud;30;8
7 Wonders;Repos Prod;30;10
```

1.  Quel est le **séparateur** utilisé ?

2.  Combien y a-t-il de **descripteurs** ? d’**enregistrements** ?

3.  Donner la valeur du descripteur `duree` pour l’enregistrement *Dixit*.

4.  Ce fichier est-il en format **ouvert** ou **fermé** ? Citer un avantage de ce choix.

??? pouce "Coup de pouce"

    La première ligne est l’en-tête : elle donne les descripteurs, ce n’est pas un enregistrement. Le séparateur est le caractère qui revient entre deux valeurs.

??? corrige "Corrigé"

    1.  Le séparateur est le **point-virgule** `;`.

    2.  **4** descripteurs (`titre`, `editeur`, `duree`, `age_min`) et **3** enregistrements.

    3.  Pour *Dixit*, `duree` vaut `30`.

    4.  Format **ouvert** (c’est du texte). Avantage : lisible par n’importe quel logiciel, durable, et **sans limite** de nombre de lignes.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Écrire du CSV <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-6 }

<span class="tag">sur papier</span>  Écrire les **trois premières lignes** (en-tête comprise) du fichier CSV correspondant à la table *studio*, en utilisant la **virgule** comme séparateur.

??? pouce "Coup de pouce"

    Une ligne d’en-tête avec les descripteurs, puis une ligne par enregistrement ; sur chaque ligne, les valeurs se suivent dans le même ordre, séparées par des virgules.

??? corrige "Corrigé"

    ```text
    id,nom,pays
    1,Nintendo,Japon
    2,Mojang,Suede
    ```

    *(La 3<sup>e</sup> ligne est le 2<sup>e</sup> enregistrement. On écrit sans accent si l’encodage pose problème, ou en UTF-8.)*

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Un CSV mal formé <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-05-7 }

<span class="tag">sur papier</span>  Ce fichier CSV contient **trois** erreurs qui gêneront un tableur. Les trouver, puis recopier le fichier corrigé (on inventera la valeur manquante).

```text
nom;ville;age
Lina;Monaco;15
Hugo,Nice,16
Zoe;Menton
Tom;Beausoleil;quinze
```

??? pouce "Coup de pouce"

    Comparez chaque ligne à l’en-tête : même séparateur ? Même nombre de valeurs ? Dans une même colonne, des valeurs de même nature ?

??? corrige "Corrigé"

    Les trois erreurs :

    - ligne *Hugo* : le séparateur est la **virgule** au lieu du point-virgule (le tableur verra une seule valeur) ;

    - ligne *Zoe* : il manque une valeur (**deux valeurs** pour trois descripteurs) ;

    - ligne *Tom* : l’âge est écrit **en lettres** ; ce n’est plus un nombre, le tableur ne pourra ni trier ni calculer correctement sur la colonne `age`.

    Fichier corrigé (l’âge de Zoé est inventé) :

    ```text
    nom;ville;age
    Lina;Monaco;15
    Hugo;Nice;16
    Zoe;Menton;15
    Tom;Beausoleil;15
    ```

### Rechercher, filtrer, trier

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 8</span> — Rechercher <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-05-8 }

<span class="tag">sur papier</span>  À l’aide de la table *jeu* :

1.  Quel est le **genre** de *Mario Kart 8* ?

2.  Quel jeu s’est vendu à **300** millions d’exemplaires ?

??? corrige "Corrigé"

    1.  *Mario Kart 8* est de genre `course`.

    2.  Le jeu vendu à **300** millions est *Minecraft*.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 9</span> — Filtrer <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-05-9 }

<span class="tag">sur papier</span>  Donner la liste des **titres** des jeux qui vérifient chaque critère :

1.  genre `action` ;

2.  `pegi` $\leqslant$ 7 (tout public) ;

3.  sortis **après 2013** **ET** vendus à plus de 50 millions.

??? pouce "Coup de pouce"

    Pour le critère 3, un jeu n’est retenu que s’il vérifie les *deux* conditions à la fois : vérifiez-les l’une après l’autre, jeu par jeu.

??? corrige "Corrigé"

    1.  genre `action` : *GTA V*, *Red Dead Redemption 2*.

    2.  `pegi` $\leqslant$ 7 : *Minecraft* (7), *Wii Sports* (7), *Mario Kart 8* (3), *Animal Crossing* (3).

    3.  après 2013 **et** plus de 50 M : *Mario Kart 8* (2014, 60) et *Red Dead Redemption 2* (2018, 55). *(Animal Crossing est écarté : 45 M seulement.)*

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 10</span> — Trier <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-05-10 }

<span class="tag">sur papier</span> 

1.  Ranger les jeux par `ventes` **décroissantes** (donner la liste des titres).

2.  Ranger les jeux par `annee` **croissante**.

3.  **Filtrer puis trier** : les jeux `pegi` = 18, du plus récent au plus ancien.

??? pouce "Coup de pouce"

    Question 3 : on ne garde d’abord que les jeux de `pegi` 18, puis on range ces seuls jeux selon l’année.

??? corrige "Corrigé"

    1.  ventes décroissantes : Minecraft (300), GTA V (190), Wii Sports (83), Mario Kart 8 (60), Red Dead Redemption 2 (55), Animal Crossing (45).

    2.  annee croissante : Wii Sports (2006), Minecraft (2011), GTA V (2013), Mario Kart 8 (2014), Red Dead Redemption 2 (2018), Animal Crossing (2020).

    3.  `pegi` = 18, du plus récent au plus ancien : *Red Dead Redemption 2* (2018), *GTA V* (2013).

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 11</span> — Calculer sur une colonne <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-05-11 }

<span class="tag">sur papier</span>  À l’aide de la table *jeu* :

1.  Combien de jeux ont un `pegi` de 18 ?

2.  Calculer la **moyenne** des ventes des jeux de genre `action`.

3.  Quelle est l’année de sortie du jeu le plus ancien ? De quel jeu s’agit-il ?

??? pouce "Coup de pouce"

    Filtrez d’abord les enregistrements concernés, puis faites le calcul sur eux seuls. Une moyenne est une somme divisée par le nombre de valeurs.

??? corrige "Corrigé"

    1.  **Deux** jeux ont un `pegi` de 18 : *GTA V* et *Red Dead Redemption 2*.

    2.  Jeux d’action : $190$ et $55$ ; moyenne $= (190 + 55) \div 2 = \mathbf{122{,}5}$ millions.

    3.  Le jeu le plus ancien est sorti en **2006** : c’est *Wii Sports*.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 12</span> — Croiser deux tables <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-12 }

<span class="tag">sur papier</span>  En utilisant les tables *jeu* **et** *studio* (reliées par le numéro de studio) :

1.  Quel **studio** (nom) a édité *Minecraft* ? Dans quel **pays** ?

2.  Donner les titres de tous les jeux édités par un studio **japonais**.

3.  *Défi :* quel **pays** totalise le plus grand nombre de `ventes` cumulées ?

??? pouce "Coup de pouce"

    Le numéro de la colonne `studio` de la table *jeu* est l’`id` d’une ligne de la table *studio* : c’est lui qui relie les deux tables.

??? pouce "Coup de pouce 2 (début de solution)"

    Question 3 : additionnez les ventes des jeux de chaque studio (studio $1$ : *Wii Sports*, *Mario Kart 8*, *Animal Crossing* ; puis studio $2$, puis studio $3$), puis cherchez le pays de chaque studio.

??? corrige "Corrigé"

    1.  *Minecraft* a `studio` = `2` : édité par **Mojang**, un studio de **Suède**.

    2.  Studio japonais = **Nintendo** (`id` `1`). Ses jeux : *Wii Sports*, *Mario Kart 8*, *Animal Crossing*.

    3.  Ventes cumulées par pays :

        - Suède (Mojang) : $300$ ;

        - États-Unis (Rockstar) : $190 + 55 = 245$ ;

        - Japon (Nintendo) : $83 + 60 + 45 = 188$.

        Le pays au plus grand total est la **Suède** ($300$ M), à elle seule grâce à *Minecraft*.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 13</span> — Pourquoi deux tables ? <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-05-13 }

<span class="tag">sur papier</span>  Un élève propose de supprimer la table *studio* : dans la table *jeu*, il remplacerait le numéro de studio par deux descripteurs, `nom_studio` et `pays_studio`.

1.  Combien de fois faudrait-il alors écrire « Nintendo » et « Japon » ?

2.  Le studio Rockstar Games change de nom. Combien de cases faut-il modifier avec une seule table ? Et avec les deux tables actuelles ?

3.  Que risque-t-on si l’on oublie de modifier l’une des cases ?

4.  On ajoute un nouveau jeu de Mojang. Que suffit-il d’écrire, pour le studio, dans la table *jeu* actuelle ?

??? pouce "Coup de pouce"

    Imaginez la grande table : sur chaque ligne de jeu, on recopierait le nom et le pays du studio. Combien de jeux chaque studio a-t-il édités ?

??? pouce "Coup de pouce 2 (début de solution)"

    Avec deux tables, « Nintendo » n’est écrit qu’*une* fois, dans la table *studio* ; la table *jeu* ne contient que son numéro, $1$. Comptez de la même façon pour Rockstar Games.

??? corrige "Corrigé"

    1.  Nintendo a édité trois jeux : « Nintendo » et « Japon » seraient écrits **trois fois** chacun (une fois par jeu), au lieu d’une seule fois dans la table *studio*.

    2.  Rockstar Games a édité deux jeux. Avec une seule table : **deux** cases à modifier ; avec les deux tables : **une seule** case (dans la table *studio*).

    3.  Si l’on oublie une case, les données deviennent **incohérentes** : le même studio apparaît sous deux noms différents, et une recherche ou un total par studio sera faux.

    4.  Il suffit d’écrire son **numéro de studio**, $2$ ; le nom et le pays se retrouvent en croisant avec la table *studio*. *Ranger chaque information à un seul endroit évite les répétitions et les erreurs.*

### Au tableur

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 14</span> — Fouiller au tableur <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-14 }

\[ au tableur \]  On fournit le fichier `jeux.csv` (la table *jeu*, séparateur `;`, encodage UTF-8). L’ouvrir dans un tableur, puis :

1.  **Trier** le tableau par `ventes` décroissantes. Quel jeu apparaît en tête ?

2.  Activer le **filtre automatique** et n’afficher que les jeux de genre `action`.

3.  Dans une cellule vide, écrire la formule `=SOMME(...)` qui calcule le **total** des ventes, puis `=MOYENNE(...)` pour la moyenne.

4.  *Bonus :* créer un **graphique en barres** des ventes par jeu.

??? pouce "Coup de pouce"

    Dans une formule, une plage de cellules s’écrit de la première à la dernière cellule, séparées par deux-points (par exemple `B2:B10`). Repérez d’abord la colonne et les lignes des ventes.

??? corrige "Corrigé"

    1.  Tri par `ventes` décroissantes : *Minecraft* apparaît en tête.

    2.  Le filtre automatique sur `genre` = `action` n’affiche que *GTA V* et *Red Dead Redemption 2*.

    3.  Les ventes sont en colonne `G`, lignes 2 à 7 : `=SOMME(G2:G7)` donne **733** ; `=MOYENNE(G2:G7)` donne environ **122,2**.

    4.  Graphique en barres : une barre par jeu, dont la hauteur est le nombre de ventes (Minecraft largement en tête).

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 15</span> — Lire des formules <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-05-15 }

<span class="tag">sur papier</span>  La table *jeu* est recopiée dans un tableur : les en-têtes sont en ligne 1, les six enregistrements en lignes 2 à 7, et les descripteurs dans les colonnes A (`id`) à G (`ventes`), dans l’ordre de la table.

1.  Quelle valeur affichent les formules `=MAX(G2:G7)`, `=MIN(D2:D7)` et `=SOMME(G3:G4)` ?

2.  Écrire la formule qui calcule la moyenne des `pegi`, puis donner son résultat (arrondi au dixième).

??? pouce "Coup de pouce"

    Écrivez la lettre de chaque colonne au-dessus de la table (A pour `id`, B pour `titre`…) et le numéro de ligne devant chaque enregistrement (la ligne 1 est l’en-tête).

??? corrige "Corrigé"

    1.  `=MAX(G2:G7)` affiche **300** (les ventes de Minecraft) ; `=MIN(D2:D7)` affiche **2006** (l’année la plus ancienne) ; `=SOMME(G3:G4)` additionne les ventes des lignes 3 et 4 (GTA V et Wii Sports) : $190 + 83 = \mathbf{273}$.

    2.  Les `pegi` sont en colonne F : `=MOYENNE(F2:F7)`, qui donne $(7 + 18 + 7 + 3 + 18 + 3) \div 6 = 56 \div 6 \approx \mathbf{9{,}3}$.

### Open data, vie privée et nuage

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 16</span> — Les données ouvertes <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-16 }

<span class="tag">sur papier</span> 

1.  Qu’est-ce que l’*open data* ? Citer un site où en trouver.

2.  Pourquoi les données ouvertes sont-elles souvent publiées en **CSV** plutôt qu’en `.xlsx` ?

??? corrige "Corrigé"

    1.  L’*open data* désigne des données **publiques librement réutilisables**, par exemple sur `data.gouv.fr` (ou le portail open data de Monaco).

    2.  Le CSV est un **format ouvert** (texte) : lisible par tous les logiciels, durable et sans limite de lignes, alors que le `.xlsx` est un format **propriétaire**.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 17</span> — Mes données, mes droits <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-17 }

<span class="tag">sur papier</span> 

1.  Que protège le **RGPD** ? Citer un droit qu’il vous accorde sur vos données.

2.  Stocker ses photos « dans le nuage » : donner un **avantage** et un **inconvénient**.

3.  Les « 3 V » du **big data** : les nommer.

4.  Monaco n’est pas dans l’Union européenne. Quelle **loi** protège les données personnelles d’un lycéen qui réside à Monaco, et quelle **autorité** contrôle son application ?

??? corrige "Corrigé"

    1.  Le **RGPD** protège les **données personnelles**. Droits : accéder à ses données, les corriger, les faire **effacer** (droit à l’oubli), donner (ou refuser) son consentement.

    2.  Nuage : **avantage** = accès partout et partage facile ; **inconvénient** = données chez un tiers (souvent à l’étranger), besoin d’une connexion, question de confidentialité.

    3.  Les « 3 V » : **Volume**, **Vélocité**, **Variété**.

    4.  À Monaco, c’est la **loi n° 1.565** du 3 décembre 2024 relative à la protection des données personnelles (mêmes grands droits que le RGPD) ; l’autorité de contrôle est l’**APDP** (Autorité de protection des données personnelles), qui a succédé à la CCIN. *(En France : RGPD et loi Informatique et libertés, autorité CNIL.)*

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 18</span> — Défi — data-détective sur l’open data <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-18 }

\[ au tableur \]  Sur `data.gouv.fr` (ou le portail open data de Monaco), télécharger un jeu de données en CSV qui vous intéresse, l’ouvrir au tableur, et **répondre à une question** de votre choix en utilisant un **tri** ou un **filtre**. Rédiger : la question posée, l’opération faite, la réponse trouvée.

??? pouce "Coup de pouce"

    Choisissez un jeu de données de petite taille (quelques centaines de lignes) et une question à laquelle un tri ou un filtre répond directement (« quel est le plus grand…? », « combien de…? »).

??? pouce "Coup de pouce 2 (début de solution)"

    Exemple de démarche : « Quelle commune des Alpes-Maritimes compte le plus d’habitants ? » $\to$ filtre sur le département, tri décroissant sur la population, lecture de la première ligne.

??? corrige "Corrigé"

    Réponse ouverte : on attend une **question** claire, l’**opération** réalisée (tri ou filtre) et la **réponse** lue dans les données. *(Exemple : « Quelle commune a la plus forte population ? » $\rightarrow$ tri décroissant sur la colonne population $\rightarrow$ on lit la première ligne.)*

### Critiquer une réponse d’IA

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 19</span> — Le jeu le plus récent, selon un assistant <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> { #ex-05-19 }

<span class="tag">sur papier</span>  Un élève a donné la table *jeu* et la table *studio* à un assistant d’IA et lui a demandé : « Quel est le jeu le plus récent, et quel studio l’a édité ? » Voici la réponse obtenue :

> Pour trouver le jeu le plus récent, on trie la table jeu selon le descripteur `ventes`, en ordre décroissant : le premier enregistrement est alors Minecraft. Pour connaître son studio, on lit sa valeur pour le descripteur `studio`, qui vaut 2, et on croise avec la table studio : l’enregistrement d’identifiant 2 est Mojang, en Suède. Le jeu le plus récent est donc Minecraft, édité par Mojang.

1.  La réponse est-elle correcte ? Refaire l’opération sur la table et comparer.

2.  Localiser l’erreur et donner la bonne réponse.

    ??? pouce "Coup de pouce"

        Relisez la question posée : quel descripteur faut-il trier pour trouver le jeu « le plus récent » ? Comparez avec ce qu’a fait l’assistant.

3.  Quelle vérification simple, faite *avant* de faire confiance à cette réponse, aurait suffi à détecter l’erreur ?

??? corrige "Corrigé"

    1.  Non. Le croisement est bien fait (studio 2 $=$ Mojang, Suède) et Minecraft est bien le premier jeu *par ventes*, mais sa valeur pour `annee` est $2011$ : quatre jeux de la table sont plus récents.

    2.  L’erreur : le tri porte sur la **mauvaise colonne**. « Le plus récent » se lit sur le descripteur `annee` (tri décroissant), pas sur `ventes`. Bonne réponse : *Animal Crossing* ($2020$), studio $1$ $=$ **Nintendo**, au Japon.

    3.  Relire la **question** et vérifier que le descripteur trié est celui qu’elle nomme (« récent » $\to$ `annee`) ; puis contrôler la réponse sur la table : l’année de Minecraft ($2011$) n’est visiblement pas la plus grande.
