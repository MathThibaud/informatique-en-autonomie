# Exercices

<p class="sous-titre">Bases de données et SQL</p>

!!! consignes "Mode d’emploi"

    - Niveau : ★ échauffement, ★★ classique (niveau bac), ★★★ défi ; les *coups de pouce* et les *corrigés* se déplient sous chaque exercice.

    - Écrire chaque requête SQL **sur plusieurs lignes** (`SELECT`… / `FROM`… / `WHERE`…).

    - **Tester ses requêtes** dans la console SQL de **Basthon** : `console.basthon.fr/?kernel=sql`. Trois bases sont fournies (`musique.sql`, `pays.sql`, `bibliotheque.sql`), à télécharger sur `github.com/MathThibaud/nsi-fichiers-eleves`, dossier `terminale/06-exercices-bdd-sql` : copier-coller le script de la base voulue, l’exécuter, puis interroger. Chaque exercice indique la base à charger.

    - Usage de l’IA, indiqué sur chaque exercice : <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> aucune ; <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> en appui (déboguer, reformuler, vérifier ; la réponse finale est écrite et comprise par vous) ; <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> l’exercice s’appuie sur une réponse d’IA. Voir la [charte d’usage de l’IA](../charte.md).

### Modèle relationnel

On travaillera ici sur la base `bibliotheque`, dont voici le schéma (clé primaire soulignée, clé étrangère notée `#`) :

auteur (id, nom, pays)  
livre (id, titre, #id_auteur, annee, genre)  
adherent (id, nom, prenom)  
emprunt (id, #id_livre, #id_adherent, date_emprunt)

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 1</span> — Lire un schéma <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-06-1 }

1.  Combien de relations comporte la base ? Combien d’attributs pour la relation `emprunt` ?

2.  Donner la clé primaire de `livre`, puis les clés étrangères de `emprunt`.

3.  Quel est le **rôle** de l’attribut `id_auteur` dans la relation `livre` ?

4.  Proposer un **domaine** (type) raisonnable pour `annee` et pour `date_emprunt`.

??? corrige "Corrigé"

    **1.** **4** relations ; `emprunt` a **4** attributs (`id`, `id_livre`, `id_adherent`, `date_emprunt`).  
    **2.** Clé primaire de `livre` : `id`. Clés étrangères de `emprunt` : `id_livre` (référence `livre.id`) et `id_adherent` (référence `adherent.id`).  
    **3.** `id_auteur` **relie** chaque livre à son auteur (il pointe vers `auteur.id`) : cela évite de recopier le nom de l’auteur et garantit la cohérence.  
    **4.** `annee` : `INTEGER` ; `date_emprunt` : `TEXT` (format `’AAAA-MM-JJ’` — SQLite n’a pas de type date natif).

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 2</span> — Clés et contraintes <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-06-2 }

1.  Expliquer pourquoi on préfère un attribut `id` plutôt que `titre` comme clé primaire de `livre`.

2.  Le SGBD refuse d’insérer dans `emprunt` une ligne dont l’`id_livre` vaut `99`. Quelle **contrainte** est en cause ? L’expliquer.

3.  Rappeler la **différence** entre une clé primaire et une clé étrangère.

??? corrige "Corrigé"

    **1.** Deux livres peuvent porter le **même titre** (rééditions, œuvres homonymes) : `titre` ne garantirait pas l’unicité. Un `id` numérique la garantit simplement.  
    **2.** La **contrainte de référence** : `id_livre = 99` ne correspond à aucun `id` de `livre` $\Rightarrow$ refus.  
    **3.** La clé **primaire** identifie de façon unique les lignes de *sa* table ; la clé **étrangère** pointe vers la clé primaire d’une *autre* table pour les relier (et peut, elle, se répéter).

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 3</span> — Faire évoluer le modèle <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-3 }

On souhaite désormais enregistrer, pour chaque livre, sa **maison d’édition** (nom, ville). Proposer une évolution du schéma qui **évite de recopier** ces informations dans chaque livre (on précisera la nouvelle relation, sa clé primaire, et la clé étrangère ajoutée).

??? pouce "Coup de pouce"

    Les informations d’un éditeur ne doivent figurer qu’**une** fois dans la base. Comment le modèle relationnel relie-t-il deux relations ?

??? corrige "Corrigé"

    On crée une relation `editeur (``id``, nom, ville)` et l’on ajoute dans `livre` une clé étrangère `#id_editeur` référençant `editeur.id`. Chaque éditeur n’est alors écrit **qu’une seule fois**.

### Les trois bases fournies

**Base `musique`** :

<table>
<thead>
<tr>
<th colspan="3" style="text-align: left;"><strong>artiste</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>id</strong></td>
<td style="text-align: left;"><strong>nom</strong></td>
<td style="text-align: left;"><strong>pays</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: left;">Daft Punk</td>
<td style="text-align: left;">France</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: left;">Stromae</td>
<td style="text-align: left;">Belgique</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: left;">Adele</td>
<td style="text-align: left;">Royaume-Uni</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: left;">Angèle</td>
<td style="text-align: left;">Belgique</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th colspan="6" style="text-align: left;"><strong>chanson</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>id</strong></td>
<td style="text-align: left;"><strong>titre</strong></td>
<td style="text-align: center;"><strong>id_artiste</strong></td>
<td style="text-align: center;"><strong>annee</strong></td>
<td style="text-align: center;"><strong>duree</strong></td>
<td style="text-align: center;"><strong>streams</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: left;">One More Time</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2000</td>
<td style="text-align: center;">320</td>
<td style="text-align: center;">450</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: left;">Get Lucky</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2013</td>
<td style="text-align: center;">369</td>
<td style="text-align: center;">900</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: left;">Instant Crush</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2013</td>
<td style="text-align: center;">337</td>
<td style="text-align: center;">600</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: left;">Alors on danse</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">2009</td>
<td style="text-align: center;">216</td>
<td style="text-align: center;">700</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: left;">Papaoutai</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">2013</td>
<td style="text-align: center;">232</td>
<td style="text-align: center;">850</td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: left;">Formidable</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">2013</td>
<td style="text-align: center;">197</td>
<td style="text-align: center;">500</td>
</tr>
<tr>
<td style="text-align: center;">7</td>
<td style="text-align: left;">Someone Like You</td>
<td style="text-align: center;">3</td>
<td style="text-align: center;">2011</td>
<td style="text-align: center;">285</td>
<td style="text-align: center;">950</td>
</tr>
<tr>
<td style="text-align: center;">8</td>
<td style="text-align: left;">Hello</td>
<td style="text-align: center;">3</td>
<td style="text-align: center;">2015</td>
<td style="text-align: center;">295</td>
<td style="text-align: center;">1000</td>
</tr>
<tr>
<td style="text-align: center;">9</td>
<td style="text-align: left;">Balance ton quoi</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">2018</td>
<td style="text-align: center;">191</td>
<td style="text-align: center;">400</td>
</tr>
<tr>
<td style="text-align: center;">10</td>
<td style="text-align: left;">Bruxelles je t’aime</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">2021</td>
<td style="text-align: center;">200</td>
<td style="text-align: center;">300</td>
</tr>
</tbody>
</table>

*(`duree` en secondes, `streams` en millions.)*

**Base `pays`** (`population` en millions d’habitants, `superficie` en milliers de km<sup>2</sup>) :

| **id** | **nom**   | **continent** | **capitale** | **population** | **superficie** |
|:------:|:----------|:--------------|:-------------|:--------------:|:--------------:|
|   1    | France    | Europe        | Paris        |       68       |      552       |
|   2    | Allemagne | Europe        | Berlin       |       84       |      358       |
|   3    | Italie    | Europe        | Rome         |       59       |      301       |
|   4    | Espagne   | Europe        | Madrid       |       48       |      506       |
|   5    | Japon     | Asie          | Tokyo        |      125       |      378       |
|   6    | Chine     | Asie          | Pékin        |      1412      |      9597      |
|   7    | Inde      | Asie          | New Delhi    |      1417      |      3287      |
|   8    | Brésil    | Amérique      | Brasilia     |      215       |      8516      |
|   9    | Canada    | Amérique      | Ottawa       |       39       |      9985      |
|   10   | Mexique   | Amérique      | Mexico       |      128       |      1964      |
|   11   | Égypte    | Afrique       | Le Caire     |      109       |      1002      |
|   12   | Nigéria   | Afrique       | Abuja        |      219       |      924       |
|   13   | Australie | Océanie       | Canberra     |       26       |      7692      |
|   14   | Maroc     | Afrique       | Rabat        |       37       |      447       |

**Base `bibliotheque`** : schéma donné au début (relations `auteur`, `livre`, `adherent`, `emprunt`). *Charger `bibliotheque.sql` pour la découvrir.*

### Interroger : `SELECT` et `WHERE`

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 4</span> — Sélections simples <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-06-4 }

\[base `pays` — Basthon\]

Écrire une requête qui affiche :

1.  le `nom` de tous les pays d’`Europe` ;

2.  le `nom` et la `capitale` des pays de plus de `100` millions d’habitants ;

3.  le `nom` des pays d’`Asie` dont la superficie dépasse `1000`.

??? corrige "Corrigé"

    ```sql
    SELECT nom FROM pays WHERE continent = 'Europe';                 -- 1.

    SELECT nom, capitale FROM pays WHERE population > 100;           -- 2.

    SELECT nom FROM pays WHERE continent = 'Asie' AND superficie > 1000; -- 3.
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 5</span> — Conditions composées <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-06-5 }

\[base `pays` — Basthon\]

1.  le `nom` des pays d’`Afrique` **ou** d’`Océanie` ;

2.  la `capitale` des pays dont la population est comprise entre `50` et `150` millions ;

3.  le `nom` des pays qui ne sont **pas** en `Europe`.

??? pouce "Coup de pouce"

    Question 2 : « compris entre » cache **deux** comparaisons ; quel opérateur logique les relie ? Question 3 : le cours donne un opérateur de différence, et aussi `NOT`.

??? corrige "Corrigé"

    ```sql
    SELECT nom FROM pays                                             -- 1.
    WHERE continent = 'Afrique' OR continent = 'Océanie';

    SELECT capitale FROM pays                                        -- 2.
    WHERE population >= 50 AND population <= 150;

    SELECT nom FROM pays WHERE continent <> 'Europe';                -- 3.
    ```

### Trier, dédoublonner, rechercher un motif

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 6</span> — Trier et dédoublonner <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-06-6 }

\[base `pays` — Basthon\]

1.  le `nom` de tous les pays, triés par population **décroissante** ;

2.  la liste des `continent`s, **sans doublon**.

??? corrige "Corrigé"

    ```sql
    SELECT nom FROM pays ORDER BY population DESC;   -- 1.
    SELECT DISTINCT continent FROM pays;             -- 2.
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — `LIMIT` et `LIKE` <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-7 }

\[base `pays` — Basthon\]

1.  le `nom` et la `superficie` des **3** pays les plus vastes ;

2.  le `nom` des pays commençant par la lettre `A` ;

3.  la `capitale` des pays dont le nom de capitale contient un **espace**.

??? pouce "Coup de pouce"

    Question 1 : trier d’abord, puis ne garder que les premières lignes. Questions 2 et 3 : dans un motif `LIKE`, le symbole `%` remplace n’importe quelle suite de caractères ; où le placer ?

??? corrige "Corrigé"

    ```sql
    SELECT nom, superficie FROM pays                 -- 1.
    ORDER BY superficie DESC LIMIT 3;

    SELECT nom FROM pays WHERE nom LIKE 'A%';         -- 2.

    SELECT capitale FROM pays WHERE capitale LIKE '% %';  -- 3.
    ```

### Agréger

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 8</span> — Fonctions d’agrégation <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-06-8 }

\[base `pays` — Basthon\]

1.  le **nombre** de pays de la base ;

2.  la population **moyenne** ;

3.  la plus grande `superficie`.

??? corrige "Corrigé"

    ```sql
    SELECT COUNT(*) FROM pays;         -- 1.
    SELECT AVG(population) FROM pays;  -- 2.
    SELECT MAX(superficie) FROM pays; -- 3.
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 9</span> — Agrégats et filtre <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-9 }

\[base `pays` — Basthon\]

1.  la population **totale** des pays d’`Asie` ;

2.  la plus petite **et** la plus grande population, en **une** requête.

??? pouce "Coup de pouce"

    Le `WHERE` s’applique **avant** l’agrégat : on filtre les lignes, puis on calcule. Un même `SELECT` peut contenir plusieurs agrégats séparés par des virgules.

??? corrige "Corrigé"

    ```sql
    SELECT SUM(population) FROM pays WHERE continent = 'Asie';  -- 1.
    SELECT MIN(population), MAX(population) FROM pays;          -- 2.
    ```

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 10</span> — Agréger la base musique <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-06-10 }

\[base `musique` — Basthon\]

1.  le nombre de chansons sorties en `2013` ;

2.  la durée **moyenne** des chansons ;

3.  le total des `streams` de la base.

??? corrige "Corrigé"

    ```sql
    SELECT COUNT(*) FROM chanson WHERE annee = 2013;  -- 1.
    SELECT AVG(duree) FROM chanson;                   -- 2.
    SELECT SUM(streams) FROM chanson;                 -- 3.
    ```

### Regrouper : `GROUP BY`

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 11</span> — Regrouper par continent <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-11 }

\[base `pays` — Basthon\]

1.  le **nombre de pays** par continent ;

2.  la population **totale** par continent, triée de la plus grande à la plus petite ;

3.  les continents comptant **au moins 4** pays.

??? pouce "Coup de pouce"

    `GROUP BY continent` forme un groupe par continent : les agrégats du `SELECT` se calculent alors **groupe par groupe**. Question 3 : on filtre des **groupes**, pas des lignes.

??? pouce "Coup de pouce 2 (début de solution)"

    Question 1 :  
    `SELECT continent, COUNT(*)`  
    `FROM pays`  
    `GROUP BY continent;`  
    Les questions 2 et 3 partent de la même structure.

??? corrige "Corrigé"

    ```sql
    SELECT continent, COUNT(*) FROM pays GROUP BY continent;   -- 1.

    SELECT continent, SUM(population) FROM pays                 -- 2.
    GROUP BY continent
    ORDER BY SUM(population) DESC;

    SELECT continent FROM pays                                  -- 3.  (Europe)
    GROUP BY continent
    HAVING COUNT(*) >= 4;
    ```

### Croiser des tables : les jointures

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 12</span> — Jointure de deux tables <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-12 }

\[base `bibliotheque` — Basthon\]

1.  le `titre` de chaque livre **avec le nom** de son auteur ;

2.  les `titre`s des livres écrits par `Camus` ;

3.  les `titre`s des livres dont l’auteur est du `Royaume-Uni`.

??? pouce "Coup de pouce"

    Quelle clé étrangère de `livre` référence la relation `auteur` ? C’est elle qui donne la condition du `ON`. Préfixer les attributs par le nom de leur table en cas d’ambiguïté.

??? corrige "Corrigé"

    ```sql
    SELECT livre.titre, auteur.nom                    -- 1.
    FROM livre
    JOIN auteur ON livre.id_auteur = auteur.id;

    SELECT livre.titre                                -- 2.
    FROM livre
    JOIN auteur ON livre.id_auteur = auteur.id
    WHERE auteur.nom = 'Camus';

    SELECT livre.titre                                -- 3.
    FROM livre
    JOIN auteur ON livre.id_auteur = auteur.id
    WHERE auteur.pays = 'Royaume-Uni';
    ```

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 13</span> — Jointure de trois tables <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-13 }

\[base `bibliotheque` — Basthon\]

1.  pour chaque emprunt, le `nom` et le `prenom` de l’adhérent **avec le titre** du livre emprunté ;

2.  le `nom` de chaque adhérent **avec son nombre d’emprunts**.

??? pouce "Coup de pouce"

    `emprunt` est au centre : elle contient une clé étrangère vers chacune des deux autres relations, d’où deux `JOIN … ON` successifs. Question 2 : il faut regrouper par adhérent.

??? pouce "Coup de pouce 2 (début de solution)"

    `SELECT adherent.nom, adherent.prenom, livre.titre`  
    `FROM emprunt`  
    `JOIN adherent ON emprunt.id_adherent = adherent.id` …

??? corrige "Corrigé"

    ```sql
    SELECT adherent.nom, adherent.prenom, livre.titre    -- 1.
    FROM emprunt
    JOIN adherent ON emprunt.id_adherent = adherent.id
    JOIN livre    ON emprunt.id_livre    = livre.id;

    SELECT adherent.nom, COUNT(*)                        -- 2.
    FROM emprunt
    JOIN adherent ON emprunt.id_adherent = adherent.id
    GROUP BY adherent.id;      -- par l'identifiant : deux homonymes restent distincts
    ```

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 14</span> — Jointure et agrégat (musique) <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-14 }

\[base `musique` — Basthon\]

Afficher le `nom` de chaque artiste **belge** avec son **total de streams**.

??? pouce "Coup de pouce"

    Trois étapes : joindre `chanson` et `artiste`, ne garder que les artistes belges, regrouper par artiste pour faire la somme.

??? pouce "Coup de pouce 2 (début de solution)"

    `SELECT artiste.nom, SUM(chanson.streams)`  
    `FROM chanson`  
    `JOIN artiste ON chanson.id_artiste = artiste.id` …

??? corrige "Corrigé"

    ```sql
    SELECT artiste.nom, SUM(chanson.streams)
    FROM chanson
    JOIN artiste ON chanson.id_artiste = artiste.id
    WHERE artiste.pays = 'Belgique'
    GROUP BY artiste.id;
    ```

### Modifier la base

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 15</span> — Ajouter, modifier, supprimer <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-15 }

\[base `bibliotheque` — Basthon\]

1.  ajouter l’auteur Victor `Hugo` (`id` `6`, pays `’France’`) ;

2.  remplacer le `genre` du livre d’`id` `1` par `’Dystopie’` ;

3.  supprimer l’emprunt d’`id` `6`. *(Que se passerait-il sans le `WHERE` ?)*

??? pouce "Coup de pouce"

    Une instruction par question : `INSERT INTO … VALUES`, `UPDATE … SET … WHERE`, `DELETE FROM … WHERE`. Les chaînes de caractères s’écrivent entre apostrophes.

??? corrige "Corrigé"

    ```sql
    INSERT INTO auteur (id, nom, pays) VALUES (6, 'Hugo', 'France'); -- 1.

    UPDATE livre SET genre = 'Dystopie' WHERE id = 1;                -- 2.

    DELETE FROM emprunt WHERE id = 6;                                -- 3.
    ```

    **3.** Sans le `WHERE`, `DELETE FROM emprunt;` effacerait **tous** les emprunts.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 16</span> — Le virement bancaire : transactions et ACID <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-06-16 }

Une banque stocke ses comptes dans la relation `compte (``id``, titulaire, solde)`, avec la contrainte `CHECK (solde >= 0)` : un solde ne peut pas être négatif. Au départ, le compte `1` (Léa) contient `100` € et le compte `2` (Noé) `30` €.

Un SGBD garantit qu’une **transaction** (un groupe d’opérations, ouvert par `BEGIN TRANSACTION;` et validé par `COMMIT;`) respecte quatre propriétés, résumées par l’acronyme **ACID** :

- **Atomicité** : toutes les opérations de la transaction sont faites, ou **aucune** (en cas d’échec, `ROLLBACK` annule tout) ;

- **Cohérence** : la transaction fait passer la base d’un état qui respecte les contraintes à un autre état qui les respecte ;

- **Isolation** : des transactions exécutées en même temps ne se perturbent pas, comme si elles avaient lieu l’une après l’autre ;

- **Durabilité** : une fois validée, une transaction n’est plus perdue, même en cas de panne.

1.  Écrire les **deux** requêtes `UPDATE` qui réalisent un virement de `50` € du compte `1` vers le compte `2`.

2.  Sans transaction, le serveur tombe en panne juste après la première requête. Quel est alors l’état de la base ? Quelle propriété aurait évité ce problème ?

3.  On recommence en entourant les deux requêtes de `BEGIN TRANSACTION;` et `COMMIT;`. Que contient la base après le `COMMIT` ? Juste après, une coupure de courant survient : quelle propriété garantit que le virement n’est pas perdu ?

4.  On tente maintenant de virer `80` € du compte `1` vers le compte `2`, dans une transaction. Laquelle des deux requêtes échoue, et pourquoi ? Que devient la requête qui avait réussi ? Quelle propriété est en jeu ?

5.  Le compte `1` contient maintenant `50` €. Léa et son père, chacun depuis son téléphone, retirent **au même moment** `20` € de ce compte. Chaque application **lit** le solde, calcule le nouveau solde, puis l’**écrit**. Quel solde final attend-on ? Montrer qu’avec l’ordre « lecture de Léa, lecture du père, écriture de Léa, écriture du père », le compte finit à `30` €. Qu’est-ce que la banque a perdu ? Quelle propriété le SGBD doit-il assurer ?

??? pouce "Coup de pouce"

    Question 1 : `UPDATE compte SET solde = solde - … WHERE …`. Question 5 : faire un tableau à deux colonnes (Léa, père) et noter, ligne après ligne, la valeur lue puis la valeur écrite par chacun.

??? corrige "Corrigé"

    **1.**

    ```sql
    UPDATE compte SET solde = solde - 50 WHERE id = 1;
    UPDATE compte SET solde = solde + 50 WHERE id = 2;
    ```

    **2.** Le compte `1` a été débité (`50` €) mais le compte `2` n’a pas été crédité (toujours `30` €) : `50` € ont **disparu**. L’**atomicité** l’aurait évité : la transaction est faite entièrement ou pas du tout, donc la panne aurait tout annulé (Léa retrouve ses `100` €).

    **3.** Après le `COMMIT` : compte `1` à `50` €, compte `2` à `80` €. La **durabilité** garantit qu’une transaction validée survit à la coupure (elle est écrite sur disque).

    **4.** Le débit `UPDATE compte SET solde = solde - 80 WHERE id = 1;` échoue : le solde deviendrait $50 - 80 = -30$, ce que la contrainte `CHECK (solde >= 0)` interdit. Le crédit de `80` € sur le compte `2`, lui, réussit. Attention : le SGBD (SQLite, par exemple) n’annule que l’**instruction fautive** ; la transaction reste ouverte avec le crédit déjà fait. Si l’on exécutait alors `COMMIT`, le compte `2` passerait à `160` € : `80` € créés de nulle part ! C’est donc à l’**application** de détecter l’erreur et d’exécuter `ROLLBACK;`, qui défait le crédit : les soldes restent `50` € et `80` €. Propriétés : **atomicité** (tout ou rien), qui préserve la **cohérence** (la base ne quitte jamais un état qui respecte les contraintes). *(Testé dans SQLite : « CHECK constraint failed » ; avec `COMMIT`, soldes `50` et `160` ; avec `ROLLBACK`, soldes `50` et `80`.)*

    **5.** On attend $50 - 20 - 20 = \mathbf{10}$ €.

    | **Étape** |       **Léa**        |       **Père**       |
    |:---------:|:--------------------:|:--------------------:|
    |     1     |       lit `50`       |                      |
    |     2     |                      |       lit `50`       |
    |     3     | écrit $50-20 =$ `30` |                      |
    |     4     |                      | écrit $50-20 =$ `30` |

    Le compte finit à `30` € : `40` € ont été retirés mais seulement `20` € débités. L’écriture de Léa a été **écrasée** et la banque a perdu `20` €. Le SGBD doit assurer l’**isolation** : la seconde transaction doit attendre que la première soit terminée, comme si elles s’exécutaient l’une après l’autre.

### Vers le bac

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 17</span> — Location entre particuliers (d’après Polynésie 2023, jour 2) <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-17 }

Un site de location d’objets entre particuliers utilise le schéma relationnel suivant. La table `Possede` relie un membre aux objets qu’il propose.

Membre (id_membre, nom, prenom, cp)  
Objet (id_objet, type, tarif)  
Reservation (id_reservation, #id_objet, #id_membre, date_location, date_retour)  
Possede (#id_membre, #id_objet)

1.  Écrire une requête affichant le `nom` et le `prenom` des membres dont le code postal `cp` est `’69003’`.

2.  Écrire une requête qui **modifie** le `tarif` de l’objet d’`id_objet` `1` pour le passer à `15`.

3.  Écrire une requête qui **ajoute** le membre Wendie Renard (`id_membre` `6`, `cp` `’69100’`).

4.  On exécute `DELETE FROM Membre WHERE nom = ’Ali’ AND prenom = ’Mohamed’;`. Expliquer pourquoi cette requête **produit une erreur**.

    ??? pouce "Coup de pouce"

        Ce membre apparaît-il dans d’autres relations ? Que garantit une contrainte de clé étrangère ?

5.  Mohamed Ali a pour `id_membre` `1`. Proposer la **suite de requêtes** permettant de le supprimer **correctement** de la base.

    ??? pouce "Coup de pouce"

        Dans quel ordre supprimer : les lignes qui **référencent** ce membre, ou le membre lui-même ?

6.  *(jointure)* Écrire une requête comptant le **nombre de réservations** réalisées par le membre Fernando Alonso.

7.  *(jointure)* Écrire une requête donnant les `nom` et `prenom` des membres qui possèdent un objet de type `’appareil à raclette’`.

    ??? pouce "Coup de pouce"

        `Possede` fait le lien entre `Membre` et `Objet` : il faut donc deux jointures.

??? corrige "Corrigé"

    ```sql
    SELECT nom, prenom FROM Membre WHERE cp = '69003';   -- 1.

    UPDATE Objet SET tarif = 15 WHERE id_objet = 1;      -- 2.

    INSERT INTO Membre (id_membre, nom, prenom, cp)      -- 3.
    VALUES (6, 'Renard', 'Wendie', '69100');
    ```

    **4.** Mohamed Ali est référencé (clé étrangère `id_membre`) par des lignes de `Reservation` et/ou `Possede` : le supprimer violerait la **contrainte de référence** $\Rightarrow$ erreur.  
    **5.** On supprime d’abord les lignes qui le référencent, puis le membre :

    ```sql
    DELETE FROM Reservation WHERE id_membre = 1;
    DELETE FROM Possede WHERE id_membre = 1;
    DELETE FROM Membre WHERE id_membre = 1;
    ```

    ```sql
    SELECT COUNT(*)                                      -- 6.
    FROM Reservation
    JOIN Membre ON Reservation.id_membre = Membre.id_membre
    WHERE Membre.nom = 'Alonso' AND Membre.prenom = 'Fernando';

    SELECT Membre.nom, Membre.prenom                     -- 7.
    FROM Membre
    JOIN Possede ON Membre.id_membre = Possede.id_membre
    JOIN Objet   ON Possede.id_objet = Objet.id_objet
    WHERE Objet.type = 'appareil à raclette';
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 18</span> — Location de véhicules (d’après La Réunion 2023, jour 2) <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-18 }

Schéma de la base :

vehicule (id_vehicule, immatriculation, marque, modele, type, carburant)  
utilisateur (id_utilisateur, nom, prenom, permis, adresse, ville)  
location (id_location, #id_utilisateur, #id_vehicule, date_debut, date_fin)

Extrait de la relation `vehicule` :

| **id_vehicule** | **immatriculation** | **marque** | **modele** | **type** | **carburant** |
|:--:|:---|:---|:---|:---|:---|
| 1 | AB-135-YZ | Peugeot | 208 | citadine | diesel |
| 2 | EC-246-TP | Renault | Zoe | citadine | electrique |
| 3 | LC-231-MG | Tesla | Model X | SUV | electrique |
| 4 | ML-128-VM | Citroën | C3 | citadine | essence |
| 5 | CL-142-CE | Citroën | C5 | berline | diesel |
| 6 | JL-526-LM | Peugeot | 508 | berline | diesel |

1.  Donner le **résultat** de :

    ```sql
    SELECT id_vehicule
    FROM vehicule
    WHERE type = 'citadine';
    ```

2.  Écrire une requête affichant les `immatriculation` des véhicules **diesel**.

3.  Écrire une requête calculant le **nombre** de véhicules de la table.

4.  Citer, **en justifiant**, les clés étrangères de la relation `location`.

5.  Expliquer pourquoi la requête suivante **produit une erreur** (l’`id_location` `1` existe déjà) :

    ??? pouce "Coup de pouce"

        Quel est le rôle de `id_location` dans la relation, et quelle propriété doit-il vérifier ?

    ```sql
    INSERT INTO location
    VALUES (1, 132, 4, '2022-05-10', '2022-05-12');
    ```

6.  Louise `DUBOIS` (`id_utilisateur` `133`) habite au numéro `50`, et non `52`, de la rue de la Liberté. Écrire la requête qui **corrige** son adresse.

7.  *(jointure)* Écrire une requête listant le `modele` et l’`immatriculation` des véhicules dont la location a débuté le `’2022-06-21’`, ainsi que le `nom` et le `prenom` des utilisateurs correspondants.

    ??? pouce "Coup de pouce"

        Les informations demandées sont réparties dans trois relations : laquelle contient les deux clés étrangères ?

??? corrige "Corrigé"

    **1.** Résultat : `1`, `2`, `4` (les trois citadines).

    ```sql
    SELECT immatriculation FROM vehicule WHERE carburant = 'diesel'; -- 2.
    SELECT COUNT(*) FROM vehicule;                                   -- 3.
    ```

    **4.** Dans `location`, `id_utilisateur` et `id_vehicule` sont des clés étrangères : ce sont les clés primaires de `utilisateur` et `vehicule`, utilisées ici pour référencer ces relations.  
    **5.** L’`id_location` `1` existe déjà : l’insertion violerait la **contrainte d’entité** (unicité de la clé primaire).

    ```sql
    UPDATE utilisateur                                   -- 6.
    SET adresse = '50 rue de la Liberté'
    WHERE id_utilisateur = 133;

    SELECT vehicule.modele, vehicule.immatriculation,    -- 7.
           utilisateur.nom, utilisateur.prenom
    FROM location
    JOIN vehicule    ON location.id_vehicule    = vehicule.id_vehicule
    JOIN utilisateur ON location.id_utilisateur = utilisateur.id_utilisateur
    WHERE location.date_debut = '2022-06-21';
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 19</span> — Podcasts de radio (d’après Centres étrangers 2023, jour 1) <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-19 }

Extraits de `podcast` (clé primaire `id_podcast`, `#id_emission` clé étrangère vers `emission`) :

| **id_podcast** | **theme** | **annee** | **id_emission** |
|:--:|:---|:--:|:--:|
| 1 | L’enseignement supérieur est-il juste ? | 2022 | 10081 |
| 3 | Travailleurs de plateformes | 2021 | 10175 |
| 4 | Souveraineté numérique française | 2019 | 10183 |
| 5 | Dans le cloud en Islande | 2019 | 10212 |

La relation `emission` (id_emission, nom, radio, animateur) décrit les émissions ; la relation `description` contient un `id_description`, un `resume`, une `duree` (en minutes) et l’`id_podcast` du podcast décrit.

1.  Écrire le **schéma relationnel** de la relation `description` (attributs et types probables, clé primaire soulignée, clé étrangère).

    ??? pouce "Coup de pouce"

        Repérer l’attribut qui identifie chaque description, puis celui qui fait référence à une autre relation.

2.  Écrire ce qu’**affiche** :

    ```sql
    SELECT theme, annee
    FROM podcast
    WHERE id_emission = 10081;
    ```

3.  Écrire une requête affichant les `theme` des podcasts de l’année `2019`.

4.  Décrire ce que renvoie `SELECT DISTINCT theme FROM podcast;`.

5.  Le nom de l’animateur de l’émission « Le Temps du débat » doit devenir « Emmanuel L. ». Écrire la requête de **mise à jour**.

6.  Écrire une requête **ajoutant** l’émission « Hashtag » (radio « France inter », animateur « Mathieu V. », `id_emission` `12850`).

7.  *(jointure)* Écrire une requête listant le `theme`, le `nom` de l’émission et le `resume` des podcasts dont la `duree` est strictement inférieure à `5` minutes.

    ??? pouce "Coup de pouce"

        `description` est reliée à `podcast` par `id_podcast`, et `podcast` à `emission` par `id_emission` : ce sont ces attributs qui servent dans les conditions de jointure.

??? corrige "Corrigé"

    **1.** `description (``id_description``:INT, resume:TEXT, duree:INT, #id_podcast:INT)`.  
    **2.** `(’L’enseignement supérieur est-il juste ?’, 2022)`.

    ```sql
    SELECT theme FROM podcast WHERE annee = 2019;        -- 3.
    ```

    **4.** La liste des thèmes de `podcast`, **sans doublon**.

    ```sql
    UPDATE emission                                      -- 5.
    SET animateur = 'Emmanuel L.'
    WHERE nom = 'Le Temps du débat';

    INSERT INTO emission (id_emission, nom, radio, animateur)   -- 6.
    VALUES (12850, 'Hashtag', 'France inter', 'Mathieu V.');

    SELECT podcast.theme, emission.nom, description.resume      -- 7.
    FROM description
    JOIN podcast  ON description.id_podcast = podcast.id_podcast
    JOIN emission ON podcast.id_emission    = emission.id_emission
    WHERE description.duree < 5;
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 20</span> — Vols spatiaux (d’après Métropole 2023, jour 2) <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-20 }

La base comporte les relations suivantes ; extrait de `Fusee` ci-dessous.

Astronaute (id_astronaute, nom, prenom, nationalite, nb_vols)  
Fusee (id_fusee, modele, constructeur, nb_places)  
Vol (id_vol, #id_fusee, date)  
Equipe (#id_vol, #id_astronaute)

| **id_fusee** | **modele** | **constructeur** | **nb_places** |
|:------------:|:-----------|:-----------------|:-------------:|
|      1       | Falcon 9   | SpaceX           |       6       |
|      2       | Starship   | SpaceX           |      100      |
|      3       | Soyouz     | TsSKB Progress   |       2       |
|      4       | SLS        | Boeing           |       6       |

1.  Donner la **définition** d’une clé primaire.

2.  On tente d’insérer un astronaute avec `id_astronaute = 1` (déjà attribué à PESQUET). Expliquer pourquoi le SGBD **renvoie une erreur**.

3.  Écrire le **schéma relationnel** de la table `Fusee` en précisant le **domaine** de chaque attribut.

4.  Écrire le **résultat** de `SELECT COUNT(*) FROM Fusee WHERE constructeur = ’SpaceX’;`.

5.  Écrire une requête affichant le `modele` et le `constructeur` des fusées ayant **au moins 4 places**.

6.  Écrire une requête affichant les `nom` et `prenom` des astronautes dans l’**ordre alphabétique** du nom.

7.  *(jointure)* Écrire une requête donnant le `nom` et le `prenom` des astronautes ayant décollé le `’25/10/2022’`.

??? pouce "Coup de pouce"

    Question 7 : la date est dans `Vol`, les noms dans `Astronaute` ; quelle relation fait le lien entre les deux ?

??? corrige "Corrigé"

    **1.** Une clé primaire est un attribut (ou groupe d’attributs) qui **identifie de façon unique** chaque enregistrement.  
    **2.** `id_astronaute = 1` est déjà attribué : l’insertion violerait la **contrainte d’entité** (unicité de la clé primaire).  
    **3.** `Fusee (``id_fusee``:INT, modele:TEXT, constructeur:TEXT, nb_places:INT)`.  
    **4.** Résultat : `2` (Falcon 9 et Starship).

    ```sql
    SELECT modele, constructeur                          -- 5.
    FROM Fusee
    WHERE nb_places >= 4;

    SELECT nom, prenom                                   -- 6.
    FROM Astronaute
    ORDER BY nom;

    SELECT Astronaute.nom, Astronaute.prenom             -- 7.
    FROM Astronaute
    JOIN Equipe ON Astronaute.id_astronaute = Equipe.id_astronaute
    JOIN Vol    ON Equipe.id_vol            = Vol.id_vol
    WHERE Vol.date = '25/10/2022';
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 21</span> — Ludothèque (d’après Métropole 2025, jour 2) <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-21 }

Une ludothèque (un seul exemplaire par jeu) utilise le schéma (`#` = clé étrangère). Quand un jeu est emprunté et pas encore rendu, `dateRendu` vaut `NULL`.

jeu (nomJeu, editeur, anneeSortie, ageMinimum, categorie)  
adherent (idAdherent, nom, prenom, dateNaissance, adresse)  
emprunt (idEmprunt, #nomJeu, #idAdherent, dateEmprunt, dateRendu)

1.  Expliquer pourquoi on ne peut pas prendre l’attribut `nom` comme clé primaire de `adherent`.

2.  Décrire ce que renvoie `SELECT nomJeu, editeur FROM jeu ORDER BY nomJeu;`.

3.  Écrire une requête affichant le `nomJeu` et la `categorie` des jeux sortis **à partir de 2010** **et** d’`ageMinimum` strictement inférieur à `10`.

4.  Écrire une requête affichant le `nomJeu` des jeux **en cours d’emprunt** (non encore rendus).

    ??? pouce "Coup de pouce"

        Une valeur `NULL` ne se teste pas avec `=` : quel opérateur SQL du cours teste l’absence de valeur ?

5.  *(jointure)* Écrire une requête affichant le `nom` et le `prenom` des adhérents ayant emprunté le jeu « Catan ».

6.  Le jeu « Catan » (emprunt d’`idEmprunt` `1538`) a été rendu le `’2025-06-03’`. Écrire la requête de **mise à jour** correspondante.

7.  *(modélisation)* La ludothèque ajoute une relation `evenement (``nom``, dateEvenement, heure)` et une relation `participation` reliant les adhérents aux événements auxquels ils participent. Proposer les **clés étrangères** de `participation` en précisant les attributs référencés.

    ??? pouce "Coup de pouce"

        Une participation associe **un** adhérent et **un** événement : comment chacun est-il identifié dans sa relation ?

??? corrige "Corrigé"

    **1.** Deux adhérents peuvent avoir le **même nom** (homonymes) : `nom` ne serait pas **unique**.  
    **2.** Affiche le `nomJeu` et l’`editeur` de tous les jeux, **triés par ordre alphabétique** du nom.

    ```sql
    SELECT nomJeu, categorie                             -- 3.
    FROM jeu
    WHERE anneeSortie >= 2010 AND ageMinimum < 10;

    SELECT nomJeu                                        -- 4.  (en cours d'emprunt)
    FROM emprunt
    WHERE dateRendu IS NULL;

    SELECT adherent.nom, adherent.prenom                 -- 5.
    FROM adherent
    JOIN emprunt ON adherent.idAdherent = emprunt.idAdherent
    WHERE emprunt.nomJeu = 'Catan';

    UPDATE emprunt                                       -- 6.
    SET dateRendu = '2025-06-03'
    WHERE idEmprunt = 1538;
    ```

    **7.** `participation` a deux clés étrangères : `#nom` (référence `evenement.nom`) et `#idAdherent` (référence `adherent.idAdherent`).

### Critiquer une réponse d’IA

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 22</span> — Une requête proposée par un assistant d’IA <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> { #ex-06-22 }

\[base `bibliotheque` — Basthon\]

Sur la base `bibliotheque` (schéma de la section 1), un élève demande à un assistant d’IA : « Écris la requête SQL qui compte le nombre d’emprunts effectués par l’adhérente dont le nom est `’Durand’`. » Voici la réponse obtenue :

```sql
SELECT COUNT(*)
FROM emprunt
JOIN adherent
WHERE adherent.nom = 'Durand';
```

*« On joint la table des emprunts à celle des adhérents, on ne garde que les lignes de l’adhérente Durand, et `COUNT(*)` compte les lignes restantes. »*

1.  La réponse est-elle correcte ? La vérifier sur une mini-base : `adherent` contient `(1, ’Durand’, ’Léa’)`, `(2, ’Martin’, ’Noé’)`, `(3, ’Petit’, ’Zoé’)` ; `emprunt` contient cinq lignes, dont deux d’`id_adherent` `1`, deux d’`id_adherent` `2` et une d’`id_adherent` `3`. Quel résultat attend-on ? Quel résultat renvoie la requête ? (On pourra créer ces deux tables dans Basthon et tester.)

2.  Localiser et corriger l’erreur.

    ??? pouce "Coup de pouce"

        Sans condition `ON`, avec quelles lignes de `adherent` chaque emprunt est-il associé ? Combien de lignes la jointure produit-elle avant le `WHERE` ?

3.  Quelle vérification simple, faite avant de faire confiance à la réponse, aurait suffi à détecter l’erreur ?

??? corrige "Corrigé"

    **1.** **Non.** On attend **2** (les deux emprunts d’`id_adherent` `1`). Testée sur la mini-base, la requête renvoie **5** : sans condition `ON`, la jointure produit le **produit cartésien** ($5 \times 3 = 15$ lignes, toutes les combinaisons emprunt/adhérent) ; le `WHERE` n’en conserve que celles associées à la ligne « Durand », soit les **cinq** emprunts, quel que soit leur emprunteur.

    **2.** L’erreur est l’**absence de condition de jointure** (`JOIN` sans `ON`). Correction (résultat sur la mini-base : **2**) :

    ```sql
    SELECT COUNT(*)
    FROM emprunt
    JOIN adherent ON emprunt.id_adherent = adherent.id
    WHERE adherent.nom = 'Durand';
    ```

    **3.** La tester sur une **toute petite base** dont on connaît la réponse, ou afficher les lignes jointes (`SELECT *`) : les emprunts de Martin ou de Petit sur la ligne « Durand » sautent aux yeux. Réflexe : **tout `JOIN` a son `ON`**.

### S’entraîner à l’oral

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 23</span> — Expliquer en deux minutes <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-06-23 }

Au Grand Oral comme devant l’examinateur de l’épreuve pratique, il faut savoir **expliquer** une notion clairement, sans notes. Choisir l’un des sujets suivants (ou le tirer au sort) :

1.  Expliquer à un camarade pourquoi une médiathèque gère ses emprunts avec une **base de données relationnelle** plutôt qu’avec un tableur.

2.  Expliquer le rôle d’une **clé primaire** et celui d’une **clé étrangère**.

3.  Expliquer ce que fait une **jointure**, sur l’exemple de deux tables.

**Préparation (5 min, seul).** Noter au brouillon **trois idées** et **un exemple**, rien de plus, puis retourner la feuille. **Exposé (2 min, chronométré).** Debout, face à un camarade, **sans lire de notes** : tout passe par la parole. **Retour (2 min).** Le camarade pose une question de relance (on peut alors s’aider d’un schéma), remplit la grille ci-dessous et donne un conseil ; puis on échange les rôles. Cette grille reprend les critères d’évaluation du Grand Oral.

??? pouce "Coup de pouce"

    Structurer chaque explication en trois temps : une **définition** en une phrase, un **exemple** petit et concret déroulé à voix haute, puis le **piège** (l’erreur que l’auditeur risque de faire). Finir par une phrase qui répond à la question posée. Garder le même exemple pour tout l’exposé (des livres, des adhérents, des emprunts) et dire pour chaque notion quel problème concret elle évite.

<table>
<thead>
<tr>
<th style="text-align: left;"><strong>Grille entre camarades</strong></th>
<th style="text-align: center;"><strong>Oui</strong></th>
<th style="text-align: center;"><strong>En partie</strong></th>
<th style="text-align: center;"><strong>Pas encore</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><strong>Clair</strong> — audible, posé ; chaque mot technique est expliqué</td>
<td style="text-align: center;"><span class="math inline">▫</span></td>
<td style="text-align: center;"><span class="math inline">▫</span></td>
<td style="text-align: center;"><span class="math inline">▫</span></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Juste</strong> — c’est exact, et l’exemple montre vraiment l’idée</td>
<td style="text-align: center;"><span class="math inline">▫</span></td>
<td style="text-align: center;"><span class="math inline">▫</span></td>
<td style="text-align: center;"><span class="math inline">▫</span></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Construit</strong> — un fil conducteur, tenu en deux minutes, sans lire</td>
<td style="text-align: center;"><span class="math inline">▫</span></td>
<td style="text-align: center;"><span class="math inline">▫</span></td>
<td style="text-align: center;"><span class="math inline">▫</span></td>
</tr>
<tr>
<td colspan="4" style="text-align: left;"><strong>Un conseil</strong> pour la prochaine fois :</td>
</tr>
</tbody>
</table>

??? corrige "Corrigé"

    Pas de texte à apprendre par cœur : voici les **éléments attendus** pour chaque sujet. L’ordre, les mots et l’exemple peuvent être différents ; l’explication est réussie si ces idées y sont, justes et reliées entre elles.

    **Sujet 1.**

    - Les données sont réparties en **relations** (tables) liées entre elles, sans redondance : l’adresse d’un adhérent n’est écrite qu’une fois.

    - Les **contraintes d’intégrité** sont vérifiées par le SGBD : il refuse, par exemple, l’emprunt d’un livre qui n’existe pas.

    - Le **SGBD** gère les accès simultanés de plusieurs utilisateurs, les droits d’accès, les sauvegardes, et répond aux requêtes SQL sur des millions de lignes.

    - Piège : un argument de confort (« c’est plus pratique ») ; les vrais arguments sont la cohérence, la sécurité et le partage.

    **Sujet 2.**

    - **Clé primaire** : attribut (ou groupe d’attributs) qui identifie chaque enregistrement de façon **unique** ; deux lignes ne peuvent pas avoir la même.

    - **Clé étrangère** : attribut qui fait référence à la clé primaire d’une autre table ; c’est elle qui crée le lien entre les tables.

    - Exemple : `Livre(id, titre)` et `Emprunt(id, id_livre, date)`, où `id_livre` fait référence à `Livre.id`.

    - Piège : une clé étrangère n’est pas unique (un livre est emprunté plusieurs fois) ; on ne peut pas supprimer un livre encore référencé par un emprunt.

    **Sujet 3.**

    - Une jointure (`JOIN … ON …`) associe chaque ligne d’une table aux lignes de l’autre qui vérifient la condition, en général « clé étrangère $=$ clé primaire ».

    - Exemple :

      ```sql
      SELECT Livre.titre, Emprunt.date
      FROM Emprunt
      JOIN Livre ON Emprunt.id_livre = Livre.id;
      ```

    - Le résultat est une table qui réunit des colonnes des deux tables : on lit le titre de chaque livre emprunté.

    - Piège : oublier la condition `ON` (on obtient toutes les combinaisons) ; préfixer par le nom de la table les attributs de même nom.
