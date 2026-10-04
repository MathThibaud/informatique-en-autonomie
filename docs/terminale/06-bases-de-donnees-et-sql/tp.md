# TP et projets

<p class="sous-titre">Bases de données et SQL</p>

## <span class="etiquette">TP</span> La ligue de futsal des quartiers

*modéliser, créer, interroger une base SQLite, puis la piloter depuis Python*

<p class="infos-activite">Durée : 2 séances (environ 3 h) · Par deux, sur machine</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/06-tp-bdd-sql){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-06-tp-bdd-sql.zip){ .md-button }

!!! consignes "Consignes"

    - Outils : **DB Browser for SQLite** (onglets « Structure de la base », « Parcourir les données », « Exécuter le SQL ») et **Python** (Thonny, IDLE ou VS Code).

    - Fichiers à télécharger (lien ci-dessus) : la base `tp_bdd_sql.db`, le script `tp_bdd_sql_creation.py` qui la fabrique (le relancer **remet la base dans son état de départ**) et le fichier `tp_bdd_sql_depart.py` de la partie 6.

    - Écrire chaque requête **sur plusieurs lignes** (`SELECT`… / `FROM`… / `WHERE`…), l’exécuter, puis noter sur le cahier (ou dans un fichier texte) le résultat demandé. <span class="run" title="À programmer et tester sur machine">▶</span>  signale ce qui se fait sur machine.

    - Dans DB Browser, une modification n’est enregistrée dans le fichier qu’après « **Écrire les modifications** » (Ctrl+S).

    - Usage de l’IA, indiqué sur chaque exercice : <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> aucune ; <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> en appui (déboguer, reformuler, vérifier ; la réponse finale est écrite et comprise par vous) ; <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> l’exercice s’appuie sur une réponse d’IA. Voir la [charte d’usage de l’IA](../charte.md).

!!! encadre "But du TP"

    Une ligue amateur (fictive) organise un championnat de futsal entre six quartiers de Monaco. On va **modéliser** ses données, **créer** des tables avec leurs contraintes et les **mettre à l’épreuve**, **interroger** la base de la saison (sélections, agrégats, regroupements, jointures), la **mettre à jour** après une journée de matchs, et enfin écrire en Python le programme qui calcule le **classement du championnat** — le produit final du TP.

## Partie 1 — Modéliser (sur papier, 20 min)

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 1</span> — Du cahier des charges au schéma <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-bases-de-donnees-et-sql-tp-1-1 }

Le secrétaire de la ligue décrit ses besoins : « Chaque **équipe** a un nom (deux équipes n’ont jamais le même), un quartier et une année de création. Chaque **joueur** a un nom, un prénom, une année de naissance, un poste (gardien, défenseur, milieu ou attaquant) et joue dans **une seule** équipe. Une **rencontre** a lieu lors d’une journée, à une date, entre une équipe qui reçoit et une équipe qui se déplace ; on note le score une fois le match joué. Enfin, on veut savoir **qui a marqué chaque but**, et à quelle minute. »

1.  Quelles relations (tables) proposez-vous ? Pour chacune, donner ses attributs, sa clé primaire et ses clés étrangères, dans la notation du cours.

2.  Pourquoi ne pas écrire le **nom** de l’équipe dans chaque ligne de la table des joueurs ?

3.  La relation des rencontres fait référence **deux fois** à la même relation. Laquelle, et pourquoi ?

4.  Avant que le match soit joué, que met-on dans les cases du score ?

!!! encadre "Le schéma retenu par la ligue"

    equipe (id, nom, quartier, annee_creation)  
    joueur (id, nom, prenom, annee_naissance, poste, #id_equipe)  
    rencontre (id, journee, date_match, #id_domicile, #id_exterieur, buts_dom, buts_ext)  
    but (id, #id_rencontre, #id_joueur, minute)

    `id_domicile` et `id_exterieur` référencent `equipe.id` ; un score non encore connu vaut `NULL`. Les dates sont du texte `’AAAA-MM-JJ’`. Comparer avec votre proposition avant de continuer.

??? corrige "Corrigé"

    - Trois erreurs parmi : clé primaire en double (entité), nom d’équipe en double (`UNIQUE`), quartier absent (`NOT NULL`), équipe ou joueur inexistant (référence), poste inconnu ou équipe contre elle-même (`CHECK`), suppression d’un joueur qui a marqué (référence).

    - `WHERE` filtre les **lignes** avant le regroupement ; `HAVING` filtre les **groupes** après `GROUP BY` (Q13 : `HAVING COUNT(*) >= 10`).

    - Le `?` empêche l’injection SQL : la valeur reste une donnée, alors qu’une valeur collée dans le texte de la requête peut en changer le sens.

    - Classement final ci-dessus ; c’est la **transaction** (atomicité) qui garantit qu’aucun match n’est à moitié saisi.

    **1.** Quatre relations, exactement celles du schéma retenu (encadré du sujet). Toute proposition équivalente convient (par exemple `numero` au lieu de `id`). Pièges : oublier la clé primaire de `but`, ou mettre une liste de buteurs dans `rencontre` (un attribut ne contient qu’**une** valeur).  
    **2.** Le nom serait recopié six fois : une faute de frappe créerait une équipe fantôme, et renommer l’équipe obligerait à modifier toutes les lignes. On écrit chaque information **une seule fois** et on relie par une **clé étrangère** (`id_equipe`).  
    **3.** `rencontre` référence deux fois `equipe` : une fois pour l’équipe qui reçoit (`id_domicile`), une fois pour celle qui se déplace (`id_exterieur`).  
    **4.** Rien : la valeur `NULL` (case vide), que l’on teste avec `IS NULL`.

## Partie 2 — Créer des tables avec leurs contraintes

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 2</span> — Deux tables dans une base vierge <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-bases-de-donnees-et-sql-tp-1-2 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Dans DB Browser, créer une **nouvelle** base `essai.db` (« Nouvelle base de données »), puis, dans l’onglet « Exécuter le SQL », écrire et exécuter les deux `CREATE TABLE` des relations `equipe` et `joueur`, en traduisant **toutes** les règles suivantes :

- chaque `id` est la clé primaire (`INTEGER PRIMARY KEY`) ;

- le nom d’une équipe est **obligatoire** et **unique** ; son quartier est obligatoire ;

- le nom et le prénom d’un joueur sont obligatoires ; son année de naissance est comprise entre $1950$ et $2015$ ; son poste est l’un des quatre mots `’gardien’`, `’defenseur’`, `’milieu’`, `’attaquant’` ;

- `id_equipe` est obligatoire et **référence** `equipe(id)`.

??? pouce "Coup de pouce"

    Mots-clés utiles : `NOT NULL`, `UNIQUE`, `CHECK (…)`, `REFERENCES equipe(id)`. Dans un `CHECK`, on peut écrire `x BETWEEN a AND b` et `x IN (’…’, ’…’)`.

Insérer ensuite deux équipes et deux joueurs de votre choix, et vérifier dans « Parcourir les données » qu’ils sont bien là.

??? corrige "Corrigé"

    Ce sont les instructions qui ont créé la base de la ligue (suivies des `INSERT` de deux équipes et de deux joueurs, au choix) :

    ```sql
    CREATE TABLE equipe (
        id             INTEGER PRIMARY KEY,
        nom            TEXT NOT NULL UNIQUE,
        quartier       TEXT NOT NULL,
        annee_creation INTEGER
    );

    CREATE TABLE joueur (
        id              INTEGER PRIMARY KEY,
        nom             TEXT NOT NULL,
        prenom          TEXT NOT NULL,
        annee_naissance INTEGER CHECK (annee_naissance BETWEEN 1950 AND 2015),
        poste           TEXT CHECK (poste IN ('gardien', 'defenseur', 'milieu', 'attaquant')),
        id_equipe       INTEGER NOT NULL REFERENCES equipe(id)
    );
    ```

    On accepte aussi la syntaxe `FOREIGN KEY (id_equipe) REFERENCES equipe(id)` placée en fin de table.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 3</span> — La table des rencontres <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-bases-de-donnees-et-sql-tp-1-3 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Toujours dans `essai.db`, écrire le `CREATE TABLE rencontre`. Les deux équipes sont obligatoires et référencent `equipe(id)` ; les deux scores sont positifs ou nuls ; et une équipe ne peut pas jouer **contre elle-même**.

??? pouce "Coup de pouce"

    La dernière règle porte sur **deux** attributs : on l’écrit après la liste des attributs, sous la forme `CHECK (… <> …)`.

??? corrige "Corrigé"

    ```sql
    CREATE TABLE rencontre (
        id           INTEGER PRIMARY KEY,
        journee      INTEGER NOT NULL,
        date_match   TEXT NOT NULL,
        id_domicile  INTEGER NOT NULL REFERENCES equipe(id),
        id_exterieur INTEGER NOT NULL REFERENCES equipe(id),
        buts_dom     INTEGER CHECK (buts_dom >= 0),
        buts_ext     INTEGER CHECK (buts_ext >= 0),
        CHECK (id_domicile <> id_exterieur)
    );
    ```

    La contrainte « une équipe ne joue pas contre elle-même » porte sur deux attributs : elle s’écrit après la liste des attributs. La table `but` est construite sur le même modèle (`minute` entre $1$ et $40$ : un match de futsal dure $2 \times 20$ minutes).

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 4</span> — Comparer avec la vraie base <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-bases-de-donnees-et-sql-tp-1-4 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Ouvrir `tp_bdd_sql.db`. Dans l’onglet « Structure de la base » (ou avec la requête `SELECT sql` `FROM sqlite_master;`), lire les `CREATE TABLE` de la ligue et les comparer aux vôtres. Noter sur le cahier les différences éventuelles.

??? corrige "Corrigé"

    Différences typiquement relevées : un `NOT NULL` oublié, la contrainte « domicile $\neq$ extérieur » écrite sur une seule colonne (impossible : elle porte sur deux attributs), une clé étrangère sans `REFERENCES`.

## Partie 3 — Mettre les contraintes à l’épreuve

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 5</span> — Le SGBD monte la garde <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-bases-de-donnees-et-sql-tp-1-5 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Sur `tp_bdd_sql.db`, exécuter les instructions suivantes **une par une**. Pour chacune, noter sur le cahier si elle est **acceptée** ou **refusée**, et quelle contrainte du cours est en jeu (domaine, entité, référence, `NOT NULL`, `UNIQUE`, contrainte métier).

|  | **Instruction** |
|:--:|:---|
| a | `INSERT INTO equipe VALUES (1, ’Les Pingouins’, ’Fontvieille’, 2020);` |
| b | `INSERT INTO equipe VALUES (7, ’Condamine FC’, ’La Condamine’, 2020);` |
| c | `INSERT INTO equipe (id, nom, annee_creation) VALUES (7, ’Saint-Roman FC’, 2020);` |
| d | `INSERT INTO joueur VALUES (37, ’Durand’, ’Léa’, 2007, ’attaquant’, 9);` |
| e | `INSERT INTO joueur VALUES (37, ’Durand’, ’Léa’, 2007, ’avant-centre’, 2);` |
| f | `INSERT INTO rencontre VALUES (16, 6, ’2026-10-10’, 3, 3, NULL, NULL);` |
| g | `DELETE FROM equipe WHERE id = 6;` |
| h | `INSERT INTO equipe VALUES (8, ’Saint-Roman FC’, ’Saint-Roman’, ’hier’);` |

1.  Pourquoi l’instruction g est-elle refusée, alors qu’elle ne fait que **supprimer** ?

2.  L’instruction h est acceptée ! Que montre-t-elle sur la façon dont SQLite applique la contrainte de **domaine** ? Proposer une contrainte `CHECK` qui l’aurait empêchée.

3.  <span class="run" title="À programmer et tester sur machine">▶</span>  Écrire la requête qui supprime l’équipe insérée en h (et seulement elle).

??? corrige "Corrigé"

    Messages réels de SQLite (DB Browser affiche les mêmes) :

    |  | **Message** | **Contrainte** |
    |:--:|:---|:---|
    | a | `UNIQUE constraint failed: equipe.id` | d’entité : la clé primaire `1` existe déjà |
    | b | `UNIQUE constraint failed: equipe.nom` | `UNIQUE` sur le nom |
    | c | `NOT NULL constraint failed: equipe.quartier` | `NOT NULL` : quartier manquant |
    | d | `FOREIGN KEY constraint failed` | de référence : pas d’équipe `9` |
    | e | `CHECK constraint failed: poste IN (…)` | métier (`CHECK`) |
    | f | `CHECK constraint failed: id_domicile <> id_exterieur` | métier : une équipe contre elle-même |
    | g | `FOREIGN KEY constraint failed` | de référence : des joueurs et des rencontres pointent vers l’équipe `6` |
    | h | *acceptée* | domaine *non* vérifié par SQLite |

    **1.** Supprimer l’équipe $6$ laisserait des joueurs et des rencontres qui désignent une équipe **inexistante** : la contrainte de référence interdit aussi les suppressions qui créeraient de telles « références pendantes ».  
    **2.** SQLite a un typage **souple** : le type déclaré n’est qu’une préférence (« affinité »). `’2021’` serait converti en entier, mais `’hier’` est stocké tel quel, en texte (`typeof(annee_creation)` vaut `’text’`). D’autres SGBD (PostgreSQL, MySQL) refusent. Parade : `annee_creation INTEGER CHECK (typeof(annee_creation) = ’integer’)` — testé : `2020` et `’2021’` acceptés, `’hier’` refusé (depuis SQLite 3.37, on peut aussi déclarer la table `STRICT`).  
    **3.** Requête :

    ```sql
    DELETE FROM equipe
    WHERE id = 8;
    ```

## Partie 4 — Interroger la base de la saison

**Pour chaque requête :** l’écrire sur plusieurs lignes, l’exécuter, puis noter le nombre de lignes obtenues et la première ligne du résultat. *Après quatre journées, la cinquième n’a pas encore été jouée.*

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 6</span> — Sélectionner, filtrer, trier <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-bases-de-donnees-et-sql-tp-1-6 }

1.  Le nom et le quartier des équipes, de la plus ancienne à la plus récente.

2.  Le prénom, le nom et l’année de naissance des joueurs nés en $2008$ ou après, du plus jeune au plus âgé.

3.  Les gardiens nés avant $2000$ (nom, prénom, numéro de leur équipe).

4.  Les différents postes, chacun une seule fois.

5.  Les joueurs dont le nom se termine par la lettre `i` (avec `LIKE`). <span class="horsprog">au-delà du programme</span>

6.  Les rencontres (numéro, journée, date) dont le score n’est pas encore connu.

??? corrige "Corrigé"

    ```sql
    -- Q1 (6 lignes) : Rocher Club | Monaco-Ville  en premier (1995)
    SELECT nom, quartier
    FROM equipe
    ORDER BY annee_creation;

    -- Q2 (5 lignes)
    SELECT prenom, nom, annee_naissance
    FROM joueur
    WHERE annee_naissance >= 2008
    ORDER BY annee_naissance DESC;

    -- Q3 (4 lignes)
    SELECT nom, prenom, id_equipe
    FROM joueur
    WHERE poste = 'gardien' AND annee_naissance < 2000;

    -- Q4 (4 lignes) : gardien, defenseur, milieu, attaquant
    SELECT DISTINCT poste
    FROM joueur;

    -- Q5 (6 lignes) : Rossi, Bianchi, Ricci, Benali, Moretti, Bellini
    SELECT nom, prenom
    FROM joueur
    WHERE nom LIKE '%i';

    -- Q6 (3 lignes) : rencontres 13 et 14 (2026-10-03), 15 (2026-10-04)
    SELECT id, journee, date_match
    FROM rencontre
    WHERE buts_dom IS NULL;
    ```

    **Q1** : Rocher Club (1995), AS Fontvieille (1998), Monte-Carlo United (2001), Condamine FC (2004), Moneghetti Futsal (2011), Larvotto Sporting (2016). **Q2** : Gianni Esposito 2010, Sacha Brun 2009, Simone Gallo 2009, Yanis Moreau 2008, Maxime Faure 2008 (l’ordre entre deux joueurs de la même année n’est pas garanti). **Q3** : Rossi Luca (1), Fabre Louis (2), Lefebvre Paul (4), Girard Antoine (5).

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Agréger et regrouper <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-bases-de-donnees-et-sql-tp-1-7 }

1.  En une seule requête : le nombre de joueurs, l’année de naissance du plus âgé et celle du plus jeune.

2.  Le nombre total de buts marqués pendant la saison, puis la moyenne de buts par match joué. Vérifier le total en comptant les lignes de la table `but`.

3.  Le nombre de joueurs pour chaque poste (`GROUP BY`). <span class="horsprog">au-delà du programme</span>

4.  Le nombre de buts marqués lors de chaque journée (`GROUP BY`). <span class="horsprog">au-delà du programme</span>

??? corrige "Corrigé"

    ```sql
    -- Q7 : 36 | 1990 | 2010
    SELECT COUNT(*), MIN(annee_naissance), MAX(annee_naissance)
    FROM joueur;

    -- Q8 : 56 | 4.666...   (et SELECT COUNT(*) FROM but; donne aussi 56)
    SELECT SUM(buts_dom + buts_ext), AVG(buts_dom + buts_ext)
    FROM rencontre
    WHERE buts_dom IS NOT NULL;

    -- Q9 : attaquant 12, defenseur 12, gardien 6, milieu 6
    SELECT poste, COUNT(*) AS nb
    FROM joueur
    GROUP BY poste;

    -- Q10 : journee 1 -> 14, 2 -> 14, 3 -> 17, 4 -> 11
    SELECT journee, SUM(buts_dom + buts_ext) AS buts
    FROM rencontre
    WHERE buts_dom IS NOT NULL
    GROUP BY journee;
    ```

    Remarque sur Q8 : sans le `WHERE`, `AVG` ignore de toute façon les lignes où la somme vaut `NULL` ; le filtre rend l’intention explicite.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — Croiser les tables <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-bases-de-donnees-et-sql-tp-1-8 }

1.  Le prénom, le nom et le poste des joueurs du `’Rocher Club’`, triés par nom.

2.  **Le classement des buteurs** : les cinq meilleurs buteurs avec leur prénom, leur nom, le nom de leur équipe et leur nombre de buts (en cas d’égalité, par ordre alphabétique des noms). <span class="horsprog">au-delà du programme</span>

    ??? pouce "Coup de pouce"

        Trois tables : `but`, `joueur`, `equipe`. On regroupe par joueur (`GROUP BY joueur.id`), on trie par nombre de buts décroissant, puis `LIMIT 5`.

3.  Les équipes dont les joueurs ont marqué **au moins** $10$ buts, avec ce nombre (`GROUP BY` … `HAVING`). <span class="horsprog">au-delà du programme</span>

??? corrige "Corrigé"

    ```sql
    -- Q11 (6 lignes) : Andrea Bellini (milieu) en premier
    SELECT joueur.prenom, joueur.nom, joueur.poste
    FROM joueur
    JOIN equipe ON joueur.id_equipe = equipe.id
    WHERE equipe.nom = 'Rocher Club'
    ORDER BY joueur.nom;

    -- Q12 : le classement des buteurs
    SELECT joueur.prenom, joueur.nom, equipe.nom AS equipe, COUNT(*) AS nb_buts
    FROM but
    JOIN joueur ON but.id_joueur = joueur.id
    JOIN equipe ON joueur.id_equipe = equipe.id
    GROUP BY joueur.id
    ORDER BY nb_buts DESC, joueur.nom
    LIMIT 5;

    -- Q13 (3 lignes)
    SELECT equipe.nom, COUNT(*) AS buts_marques
    FROM but
    JOIN joueur ON but.id_joueur = joueur.id
    JOIN equipe ON joueur.id_equipe = equipe.id
    GROUP BY equipe.id
    HAVING COUNT(*) >= 10;
    ```

    **Q12** :

    | **prenom** | **nom** | **equipe**         | **nb_buts** |
    |:-----------|:--------|:-------------------|:-----------:|
    | Yanis      | Moreau  | AS Fontvieille     |      7      |
    | Karim      | Benali  | Monte-Carlo United |      6      |
    | Nicolo     | Ferraro | Rocher Club        |      5      |
    | Alessio    | Moretti | Monte-Carlo United |      5      |
    | Tom        | Barbier | Moneghetti Futsal  |      4      |

    Diego Carvalho et Marco Colombo ont eux aussi $4$ buts : le tri par nom départage.

    **Q13** :

    | **nom**            | **buts_marques** |
    |:-------------------|:----------------:|
    | AS Fontvieille     |        10        |
    | Condamine FC       |        10        |
    | Monte-Carlo United |        15        |

    (ordre non garanti sans `ORDER BY`). `WHERE` ne peut pas filtrer sur `COUNT(*)` : c’est le rôle de `HAVING`.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 9</span> — Les résultats d’une journée <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-bases-de-donnees-et-sql-tp-1-9 }

1.  Afficher les résultats de la journée $3$ sous la forme : *nom de l’équipe qui reçoit, buts_dom, buts_ext, nom de l’équipe qui se déplace*.

    ??? pouce "Coup de pouce"

        Il faut joindre la table `equipe` **deux fois** : une fois pour l’équipe qui reçoit, une fois pour celle qui se déplace. On la renomme à chaque fois avec un alias : `JOIN equipe AS d ON …`, `JOIN equipe AS e ON …`.

2.  **Contrôle de cohérence.** Dans une base saine, pour chaque rencontre jouée, le nombre de lignes de la table `but` est égal à `buts_dom + buts_ext`. Écrire une requête qui affiche les rencontres pour lesquelles ce n’est **pas** le cas. Que doit-elle renvoyer ici ? <span class="horsprog">au-delà du programme</span>

??? corrige "Corrigé"

    ```sql
    -- Q14 : la table equipe jointe deux fois, sous deux alias
    SELECT d.nom AS domicile, r.buts_dom, r.buts_ext, e.nom AS exterieur
    FROM rencontre AS r
    JOIN equipe AS d ON r.id_domicile = d.id
    JOIN equipe AS e ON r.id_exterieur = e.id
    WHERE r.journee = 3;

    -- Q15 : controle de coherence
    SELECT rencontre.id, rencontre.buts_dom + rencontre.buts_ext AS score_total,
           COUNT(but.id) AS buts_saisis
    FROM rencontre
    JOIN but ON but.id_rencontre = rencontre.id
    GROUP BY rencontre.id
    HAVING score_total <> buts_saisis;
    ```

    **Q14** : AS Fontvieille 4 – 4 Moneghetti Futsal ; Condamine FC 1 – 0 Rocher Club ; Monte-Carlo United 6 – 2 Larvotto Sporting.  
    **Q15** : résultat **vide** — la base est cohérente (vérifié pour les $12$ rencontres jouées). Limite : un match joué sur le score de $0$ à $0$ n’a aucune ligne dans `but` et échappe à la jointure ; il n’y en a pas ici.

## Partie 5 — Mettre la base à jour

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 10</span> — Le week-end de la journée 5 <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-bases-de-donnees-et-sql-tp-1-10 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Écrire et exécuter les requêtes qui traduisent les nouvelles suivantes. **Relire chaque `WHERE` avant d’exécuter.**

1.  La rencontre $14$ (Larvotto Sporting – Condamine FC) s’est terminée sur le score de $1$ à $1$ : buts de Gianni Esposito (joueur $36$) à la $12^\text{e}$ minute et de Diego Carvalho (joueur $11$) à la $29^\text{e}$. Mettre à jour le score, puis insérer les deux buts en **une seule** instruction `INSERT`.

2.  La rencontre $15$ est reportée au 11 octobre 2026.

3.  Le Rocher Club a été créé en $1993$, et non en $1995$.

4.  Yanis Moreau (joueur $6$) quitte la ligue. Tenter de le supprimer de la table `joueur`. Que se passe-t-il, et pourquoi ? Combien de lignes de `but` le concernent ?

5.  Raphaël Petit quitte lui aussi la ligue : le supprimer (en le désignant par son nom **et** son prénom). Pourquoi cette fois la suppression réussit-elle ?

6.  Que ferait l’instruction `DELETE FROM joueur;` ? *(Ne pas l’exécuter !)*

Relancer la requête de contrôle de cohérence : elle doit toujours ne rien renvoyer. Puis **écrire les modifications** (Ctrl+S) et **fermer** la base dans DB Browser avant de passer à Python (un fichier ouvert en écriture par un logiciel peut être *verrouillé* pour les autres).

??? corrige "Corrigé"

    **1. à 3.** puis tentatives des questions 4 et 5 :

    ```sql
    UPDATE rencontre
    SET buts_dom = 1, buts_ext = 1
    WHERE id = 14;

    INSERT INTO but (id_rencontre, id_joueur, minute)
    VALUES (14, 36, 12), (14, 11, 29);

    UPDATE rencontre
    SET date_match = '2026-10-11'
    WHERE id = 15;

    UPDATE equipe
    SET annee_creation = 1993
    WHERE nom = 'Rocher Club';

    DELETE FROM joueur
    WHERE id = 6;                      -- refusee : FOREIGN KEY constraint failed

    DELETE FROM joueur
    WHERE nom = 'Petit' AND prenom = 'Raphaël';   -- 1 ligne supprimee
    ```

    **4.** Refus (`FOREIGN KEY constraint failed`) : $7$ lignes de `but` désignent Yanis Moreau ; les supprimer avec lui effacerait l’histoire de la saison. Dans la vraie vie, on garderait le joueur (par exemple avec un attribut « actif »).  
    **5.** Raphaël Petit (gardien de Larvotto) n’a marqué aucun but : aucune ligne ne le référence. Il reste $35$ joueurs.  
    **6.** Elle tenterait de supprimer **tous** les joueurs. Ici, SQLite la refuse en bloc (des buts référencent certains joueurs) : testé, il reste bien $35$ joueurs. Mais sans clés étrangères actives, la table serait vidée : « le `WHERE` qui sauve des vies ».  
    La requête de contrôle (Q15) renvoie toujours un résultat vide.

## Partie 6 — Piloter la base depuis Python

Le module `sqlite3` (fourni avec Python) permet d’envoyer des requêtes SQL à une base et de récupérer les résultats sous forme de **liste de tuples**. Ouvrir `tp_bdd_sql_depart.py` (dans le même dossier que la base). On y trouve :

```python
connexion = sqlite3.connect("tp_bdd_sql.db")
connexion.execute("PRAGMA foreign_keys = ON")   # sinon : cles etrangeres ignorees !

def equipes_creees_avant(annee):
    requete = """SELECT nom, quartier
                 FROM equipe
                 WHERE annee_creation < ?
                 ORDER BY annee_creation"""
    return connexion.execute(requete, (annee,)).fetchall()
```

Le point d’interrogation `?` est un **paramètre** : `sqlite3` le remplace par la valeur du tuple `(annee,)`. `fetchall()` renvoie toutes les lignes, `fetchone()` la première seulement.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 11</span> — Premières requêtes depuis Python <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-bases-de-donnees-et-sql-tp-1-11 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Dans la console, que renvoie `equipes_creees_avant(2005)` ?

<span class="run" title="À programmer et tester sur machine">▶</span>  Compléter `joueurs_de(nom_equipe)` (liste des triplets `(prenom, nom, poste)` des joueurs de l’équipe, triés par nom) et `nb_buts(nom, prenom)` (un **entier**). Lancer le fichier : les tests `test_joueurs_de` et `test_nb_buts` doivent afficher `OK`.

??? pouce "Coup de pouce"

    Pour `nb_buts`, la requête `SELECT COUNT(*)` … renvoie une seule ligne d’une seule colonne : `connexion.execute(…).fetchone()[0]`.

??? corrige "Corrigé"

    Après la partie 5 (Rocher Club créé en 1993), `equipes_creees_avant(2005)` renvoie :

    ```console
    [('Rocher Club', 'Monaco-Ville'), ('AS Fontvieille', 'Fontvieille'),
     ('Monte-Carlo United', 'Monte-Carlo'), ('Condamine FC', 'La Condamine')]
    ```

    ```python
    def joueurs_de(nom_equipe):
        requete = """SELECT joueur.prenom, joueur.nom, joueur.poste
                     FROM joueur
                     JOIN equipe ON joueur.id_equipe = equipe.id
                     WHERE equipe.nom = ?
                     ORDER BY joueur.nom"""
        return connexion.execute(requete, (nom_equipe,)).fetchall()

    def nb_buts(nom, prenom):
        requete = """SELECT COUNT(*)
                     FROM but
                     JOIN joueur ON but.id_joueur = joueur.id
                     WHERE joueur.nom = ? AND joueur.prenom = ?"""
        return connexion.execute(requete, (nom, prenom)).fetchone()[0]
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 12</span> — Pourquoi le point d’interrogation ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-bases-de-donnees-et-sql-tp-1-12 }

Un camarade construit plutôt la requête en y collant directement le nom : `requete = f"… WHERE equipe.nom = ’{nom_equipe}’"`.

1.  <span class="run" title="À programmer et tester sur machine">▶</span>  Essayer sa version avec `joueurs_de("x’ OR ’1’=’1")`. Combien de joueurs obtient-on ? Écrire la condition `WHERE` réellement envoyée au SGBD.

2.  Ce piège s’appelle une **injection SQL**. Pourquoi est-il dangereux sur un site web où l’utilisateur tape lui-même le texte ? Que fait le `?` de différent ?

??? corrige "Corrigé"

    **1.** La condition envoyée devient `WHERE equipe.nom = ’x’ OR ’1’=’1’`, toujours vraie : on obtient **tous** les joueurs ($35$ après la partie 5, $36$ sinon). **2.** Sur un site, un utilisateur malveillant peut ainsi lire, modifier ou détruire des données auxquelles il n’a pas droit (*injection SQL*, l’une des failles les plus exploitées du Web). Avec `?`, la valeur est transmise **à part**, comme une simple donnée : elle n’est jamais interprétée comme du SQL ; la version avec `?` renvoie une liste vide (c’est un test du fichier).

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 13</span> — Le classement du championnat <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-bases-de-donnees-et-sql-tp-1-13 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Compléter `classement()` : écrire la requête qui sélectionne `id_domicile`, `id_exterieur`, `buts_dom`, `buts_ext` des rencontres **déjà jouées**, puis, pour chacune, mettre à jour le dictionnaire des deux équipes (`J`, `G`, `N`, `P`, buts pour `bp`, buts contre `bc`, points `pts` : victoire $3$, nul $1$, défaite $0$). Le tri final est fourni. Décommenter `afficher_classement()` et recopier le podium sur le cahier (rang, équipe, points, différence de buts).

??? pouce "Coup de pouce"

    Une même rencontre compte pour **deux** équipes : pour l’équipe qui reçoit, les buts « pour » sont `bd` et les buts « contre » `be` ; pour l’autre, c’est l’inverse. On peut parcourir les deux cas avec `for (equipe, pour, contre) in ((dom, bd, be), (ext, be, bd)):`.

Pourquoi les tests vérifient-ils que la somme des buts pour est égale à la somme des buts contre ?

??? corrige "Corrigé"

    *Idée.* Une rencontre jouée compte pour **deux** équipes, avec les mêmes buts vus de deux côtés : pour l’équipe qui reçoit, les buts « pour » sont `bd` et les buts « contre » `be` ; pour l’équipe qui se déplace, c’est l’inverse. On écrit donc **une seule fois** la mise à jour d’une ligne du classement (fonction `compter_match`), et on l’appelle deux fois par rencontre.

    ```python
    def compter_match(s, pour, contre):
        # met a jour la ligne s du classement apres un match
        s["J"] = s["J"] + 1
        s["bp"] = s["bp"] + pour
        s["bc"] = s["bc"] + contre
        if pour > contre:
            s["G"] = s["G"] + 1
            s["pts"] = s["pts"] + 3
        elif pour == contre:
            s["N"] = s["N"] + 1
            s["pts"] = s["pts"] + 1
        else:
            s["P"] = s["P"] + 1
    ```

    Dans `classement()`, à la place des trous :

    ```python
        requete = """SELECT id_domicile, id_exterieur, buts_dom, buts_ext
                     FROM rencontre
                     WHERE buts_dom IS NOT NULL"""
        for (dom, ext, bd, be) in connexion.execute(requete):
            compter_match(stats[dom], bd, be)   # equipe qui recoit
            compter_match(stats[ext], be, bd)   # equipe qui se deplace : buts inverses
    ```

    *Autre méthode :* sans fonction auxiliaire, la boucle du coup de pouce `for (equipe, pour, contre) in ((dom, bd, be), (ext, be, bd)):` parcourt les deux cas, et son corps contient les mêmes instructions que `compter_match`, appliquées à `s = stats[equipe]`.

    Affichage obtenu après la partie 5 (journées 1 à 4 et rencontre 14) :

    ```console
       Equipe                J  G  N  P  bp  bc diff  Pts
    1  Monte-Carlo United    4  2  2  0  15   8   +7    8
    2  Condamine FC          5  2  2  1  11   7   +4    8
    3  AS Fontvieille        4  2  1  1  10   8   +2    7
    4  Rocher Club           4  1  2  1   7   7   +0    5
    5  Moneghetti Futsal     4  1  1  2   9  14   -5    4
    6  Larvotto Sporting     5  0  2  3   6  14   -8    2
    ```

    Chaque but marqué par une équipe est un but encaissé par une autre : sur tout le championnat, la somme des buts pour égale la somme des buts contre. C’est un **invariant** qui détecte une inversion `bd`/`be`.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 14</span> — Saisir un résultat en « tout ou rien » <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-bases-de-donnees-et-sql-tp-1-14 }

On veut saisir les deux autres matchs de la journée 5 **depuis Python**, sans risquer une base incohérente (des buts enregistrés mais un score faux, ou l’inverse).

<span class="run" title="À programmer et tester sur machine">▶</span>  Compléter `saisir_resultat(id_rencontre, buts)`, où `buts` est une liste de couples `(id_joueur, minute)` : à l’intérieur du bloc `with connexion:`, insérer chaque but, **compter** les buts de chaque équipe (le joueur doit appartenir à l’une des deux équipes de la rencontre, sinon lever une erreur avec `raise ValueError(…)`), puis mettre à jour le score. Le bloc `with connexion:` est une **transaction** : si une erreur survient, **tout** ce qui a été fait dans le bloc est annulé.

1.  Tester d’abord ces deux appels (le joueur $1$ joue pour Fontvieille, le joueur $99$ n’existe pas) :  
    `saisir_resultat(15, [(30, 14), (1, 20)])`  
    `saisir_resultat(15, [(30, 14), (99, 20)])`  
    Dans chaque cas, quelle erreur obtient-on ? Combien de buts de la rencontre $15$ sont enregistrés ensuite ? Quelle propriété des transactions est illustrée ?

2.  Saisir pour de bon : rencontre $13$ avec `[(6, 5), (23, 11), (5, 18), (24, 30), (23, 38)]` et rencontre $15$ avec `[(30, 14), (29, 33)]`. Donner les scores obtenus, puis le **classement final** de la saison et le meilleur buteur.

??? corrige "Corrigé"

    *Idée.* Dans le bloc `with connexion:`, on insère chaque but en comptant au passage les buts de chaque équipe (on cherche l’équipe du buteur) ; un buteur étranger au match provoque une erreur, qui annule tout le bloc. Le score n’est écrit qu’à la fin, une fois tous les buts insérés.

    ```python
    def saisir_resultat(id_rencontre, buts):
        dom, ext = connexion.execute(
            "SELECT id_domicile, id_exterieur FROM rencontre WHERE id = ?",
            (id_rencontre,)).fetchone()
        bd = 0
        be = 0
        with connexion:
            for (id_joueur, minute) in buts:
                connexion.execute(
                    "INSERT INTO but (id_rencontre, id_joueur, minute) VALUES (?, ?, ?)",
                    (id_rencontre, id_joueur, minute))
                ligne = connexion.execute("SELECT id_equipe FROM joueur WHERE id = ?",
                                          (id_joueur,)).fetchone()
                if ligne[0] == dom:
                    bd = bd + 1
                elif ligne[0] == ext:
                    be = be + 1
                else:
                    raise ValueError(f"le joueur {id_joueur} ne joue pas ce match")
            connexion.execute(
                "UPDATE rencontre SET buts_dom = ?, buts_ext = ? WHERE id = ?",
                (bd, be, id_rencontre))
    ```

    **1.** Premier appel : `ValueError: le joueur 1 ne joue pas ce match` ; second : `sqlite3.IntegrityError: FOREIGN KEY constraint failed` (joueur $99$ inexistant). Dans les deux cas, le premier but (joueur $30$), pourtant inséré, a été **annulé** : $0$ but enregistré pour la rencontre $15$, score toujours `NULL`. C’est l’**atomicité** (le A de ACID) : tout ou rien.  
    **2.** Rencontre 13 : AS Fontvieille 2 – 3 Monte-Carlo United ; rencontre 15 : Moneghetti Futsal 0 – 2 Rocher Club. Classement final :

    ```console
       Equipe                J  G  N  P  bp  bc diff  Pts
    1  Monte-Carlo United    5  3  2  0  18  10   +8   11
    2  Condamine FC          5  2  2  1  11   7   +4    8
    3  Rocher Club           5  2  2  1   9   7   +2    8
    4  AS Fontvieille        5  2  1  2  12  11   +1    7
    5  Moneghetti Futsal     5  1  1  3   9  16   -7    4
    6  Larvotto Sporting     5  0  2  3   6  14   -8    2
    ```

    Meilleurs buteurs : **égalité** entre Karim Benali (Monte-Carlo United) et Yanis Moreau (AS Fontvieille), $8$ buts chacun (requête Q12 relancée), devant Nicolo Ferraro et Alessio Moretti ($6$). La base contient alors $65$ buts.

## Pour aller plus loin

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 15</span> — Le classement en une seule requête SQL <span class="horsprog">au-delà du programme</span> <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-bases-de-donnees-et-sql-tp-1-15 }

Obtenir les points et la différence de buts de chaque équipe **sans Python**. Idée : fabriquer une table intermédiaire qui contient **deux lignes par rencontre jouée** (une par équipe, avec ses buts « pour » et « contre ») grâce à `UNION ALL`, puis regrouper par équipe. Pour les points, SQL possède une expression conditionnelle : `CASE WHEN pour > contre THEN 3 WHEN pour = contre THEN 1 ELSE 0 END`. Comparer avec le classement obtenu en Python.

??? corrige "Corrigé"

    ```sql
    SELECT equipe.nom,
           COUNT(*) AS j,
           SUM(CASE WHEN pour > contre THEN 3
                    WHEN pour = contre THEN 1
                    ELSE 0 END) AS pts,
           SUM(pour) - SUM(contre) AS diff
    FROM (SELECT id_domicile AS id_eq, buts_dom AS pour, buts_ext AS contre
          FROM rencontre
          WHERE buts_dom IS NOT NULL
          UNION ALL
          SELECT id_exterieur, buts_ext, buts_dom
          FROM rencontre
          WHERE buts_dom IS NOT NULL) AS resultats
    JOIN equipe ON resultats.id_eq = equipe.id
    GROUP BY equipe.id
    ORDER BY pts DESC, diff DESC;
    ```

    Sur la base finale : Monte-Carlo United 11 (+8), Condamine FC 8 (+4), Rocher Club 8 (+2), AS Fontvieille 7 (+1), Moneghetti Futsal 4 ($-7$), Larvotto Sporting 2 ($-8$) — identique au classement Python. `UNION ALL`, `CASE` et les sous-requêtes dépassent le programme : défi réservé aux plus rapides.

## Bilan à rédiger

En une dizaine de lignes, sur le cahier ou dans un fichier :

- citer **trois** erreurs de saisie que les contraintes de la base ont empêchées pendant le TP, et la contrainte responsable de chacune ;

- expliquer la différence entre `WHERE` et `HAVING` à l’aide d’une requête du TP ;

- expliquer pourquoi on passe les valeurs avec `?` plutôt qu’en les collant dans le texte de la requête ;

- recopier le classement final et dire quel « service » du SGBD a garanti qu’aucun match n’a été à moitié saisi.
