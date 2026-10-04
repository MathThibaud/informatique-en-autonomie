# Sujet 26 — Sortir d'un labyrinthe

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/pratique-26-labyrinthe){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-pratique-26-labyrinthe.zip){ .md-button }

??? corrige "Corrigé"

    !!! remarque "Remarque"

        On donne une version simple ; d’autres réponses sont possibles. Le fichier complet, `corrige_sujet_26.py`, est en ligne : [`github.com/MathThibaud/nsi-fichiers-eleves/tree/main/corriges/terminale/pratique-26`](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/corriges/terminale/pratique-26).

    Question 1

    *Écrire `cases_voisines(grille, case)` (ordre : haut, bas, gauche, droite).*

    On écrit les quatre cases candidates dans l’ordre demandé, puis on construit **par compréhension** la liste de celles qui sont dans la grille et ne sont pas des murs.

    ```python
    def cases_voisines(grille, case):
        ligne, colonne = case
        candidates = [(ligne - 1, colonne), (ligne + 1, colonne),
                      (ligne, colonne - 1), (ligne, colonne + 1)]
        return [(l, c) for (l, c) in candidates
                if 0 <= l < len(grille) and 0 <= c < len(grille[l])
                and grille[l][c] != "#"]
    ```

    *Autre méthode :* on part d’une liste vide et on ajoute chaque candidate valable avec `append`.

    ```python
        voisines = []
        for (l, c) in candidates:
            if 0 <= l < len(grille) and 0 <= c < len(grille[l]) and grille[l][c] != "#":
                voisines.append((l, c))
        return voisines
    ```

    Le test des bornes n’est pas indispensable ici (les labyrinthes sont entourés de murs), mais il rend la fonction sûre pour n’importe quelle grille.

    ```python
        assert cases_voisines(grille, (1, 3)) == [(1, 2), (1, 4)]
    ```

    $\blacktriangleright$ Appel professeur. expliquer le calcul des quatre voisines (quelle coordonnée change, dans quel sens) et l’ordre imposé.

    Question 2

    *Compléter `plus_court_chemin` (parcours en largeur).*

    Quand on découvre un voisin, il faut : le marquer comme découvert, l’enfiler, et noter son parent.

    ```python
            for voisin in graphe[sommet]:
                if voisin not in decouverts:
                    decouverts.append(voisin)
                    en_attente.append(voisin)
                    parent[voisin] = sommet
    ```

    ```python
        assert plus_court_chemin(graphe, (1, 1), (1, 1)) == [(1, 1)]
        assert plus_court_chemin(graphe, (1, 1), (3, 3)) == [(1, 1), (2, 1), (3, 1), (3, 2), (3, 3)]
    ```

    Question 3

    *Utiliser `sortir` sur `labyrinthe.txt`.*

    ```console
    >>> sortir("labyrinthe.txt")
    #####################
    #Eoooooooo#         #
    #########o####### # #
    #       #ooooooo  # #
    # # # # #######o### #
    # #       #    o    #
    # ##### ### ###o#####
    #     #     #  ooooo#
    ### # ####### #####o#
    #             #    S#
    #####################
    26
    ```

    Il faut **26 déplacements** (le chemin compte 27 cases, entrée et sortie comprises).

    $\blacktriangleright$ Appel professeur. expliquer pourquoi le parcours en largeur donne un plus court chemin : il découvre les cases par distance croissante à l’entrée, et le parent d’une case est toujours à distance un de moins.

    Question 4

    *Remplacer `pop(0)` par `pop()` : obtient-on encore un chemin ? le plus court ?*

    ```console
    >>> sortir("labyrinthe.txt")
    #####################
    #Eoooooooo#      ooo#
    #########o#######o#o#
    #ooo    #ooooooooo#o#
    #o#o# # ####### ###o#
    #o#ooooo  #ooooooooo#
    #o#####o###o### #####
    #ooooo#ooooo#ooooooo#
    ### #o#######o#####o#
    #    ooooooooo#    S#
    #####################
    78
    ```

    On obtient encore un chemin **valide** de l’entrée à la sortie (chaque case a pour parent une case voisine), mais de **78** déplacements au lieu de 26 : ce n’est plus le plus court.

    Avec `pop()`, `en_attente` n’est plus une file mais une **pile** : on repart toujours de la dernière case découverte, on s’enfonce le plus loin possible avant de revenir en arrière. C’est un **parcours en profondeur**, qui ne découvre plus les cases par distance croissante. Comme ce labyrinthe contient des **cycles** (plusieurs chemins possibles), le parent retenu pour une case n’est pas forcément sur un plus court chemin.

    $\blacktriangleright$ Appel professeur. faire le lien file $\leftrightarrow$ largeur, pile $\leftrightarrow$ profondeur, et expliquer que seul le parcours en largeur garantit un plus court chemin (en nombre d’arêtes).

*Durée de l’épreuve : 1 heure.*

!!! encadre "Déroulement de l’épreuve"

    - Cette situation d’évaluation comporte ce document ainsi que des fichiers de codes et de données présents sur l’ordinateur. Le candidat doit **agir en autonomie** et faire preuve d’initiative tout au long de l’épreuve.

    - En cas de difficulté, le candidat peut solliciter l’examinateur. Des moments privilégiés sont indiqués sous la forme d’**appels professeur**. L’examinateur peut intervenir à tout moment s’il le juge utile.

Un labyrinthe est décrit dans un fichier texte : chaque ligne du fichier est une ligne du labyrinthe, le caractère `#` est un **mur**, une espace est une case libre, `E` est l’entrée et `S` la sortie. On se déplace d’une case à une case voisine (en haut, en bas, à gauche ou à droite, jamais en diagonale), sans traverser les murs.

```console
#######
#E    #
# ### #
#   #S#
#######
```

**Figure 1.** Le labyrinthe du fichier `petit.txt`.

Une case est repérée par le couple `(ligne, colonne)`, les numéros commençant à `0` en haut à gauche : dans `petit.txt`, l’entrée est la case `(1, 1)` et la sortie la case `(3, 5)`.

Le labyrinthe est vu comme un **graphe** : les sommets sont les cases qui ne sont pas des murs, et deux sommets sont reliés s’ils sont voisins. Dans le fichier `labyrinthe.py`, la fonction `lire_labyrinthe` renvoie la grille (liste de chaînes de caractères, une par ligne) et la fonction `construire_graphe` renvoie le graphe sous forme d’un **dictionnaire** qui associe à chaque case la liste de ses cases voisines.

Question 1

Écrire le corps de la fonction `cases_voisines(grille, case)` qui renvoie la liste des cases qui ne sont pas des murs parmi les quatre cases voisines de `case`, dans l’ordre : haut, bas, gauche, droite. Par exemple, avec la grille de `petit.txt`, `cases_voisines(grille, (1, 1))` renvoie `[(2, 1), (1, 2)]`. Tester avec la fonction `test_voisines`.

**$\blacktriangleright$ Appel professeur.** Appeler le professeur pour lui présenter votre réponse ou en cas de difficulté.

Question 2

La fonction `plus_court_chemin` réalise un **parcours en largeur** du graphe à partir de la case de départ, en mémorisant pour chaque case découverte la case qui l’a fait découvrir (dictionnaire `parent`), puis reconstruit le chemin en remontant les parents depuis l’arrivée. Compléter les lignes manquantes de cette fonction, repérées par `A COMPLETER`. Tester avec la fonction `test_chemin`.

Question 3

Utiliser la fonction fournie `sortir` sur le fichier `labyrinthe.txt`. Relever le nombre de déplacements nécessaires pour sortir et observer le chemin affiché.

**$\blacktriangleright$ Appel professeur.** Appeler le professeur pour lui présenter votre réponse ou en cas de difficulté.

Question 4

Dans la fonction `plus_court_chemin`, on remplace `en_attente.pop(0)` par `en_attente.pop()`, puis on appelle de nouveau `sortir("labyrinthe.txt")`. Obtient-on encore un chemin de l’entrée à la sortie ? Est-il le plus court ? Expliquer ce qui a changé dans le parcours.

**$\blacktriangleright$ Appel professeur.** Appeler le professeur pour lui présenter votre réponse ou en cas de difficulté.

### Description du dossier

Le dossier fourni au candidat comporte les éléments suivants :

- une version PDF de l’énoncé ;

- un code source de départ `labyrinthe.py` ;

- deux labyrinthes au format texte : `petit.txt` et `labyrinthe.txt`.

??? corrige "Corrigé"

    !!! remarque "Remarque"

        On donne une version simple ; d’autres réponses sont possibles. Le fichier complet, `corrige_sujet_26.py`, est en ligne : [`github.com/MathThibaud/nsi-fichiers-eleves/tree/main/corriges/terminale/pratique-26`](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/corriges/terminale/pratique-26).

    Question 1

    *Écrire `cases_voisines(grille, case)` (ordre : haut, bas, gauche, droite).*

    On écrit les quatre cases candidates dans l’ordre demandé, puis on construit **par compréhension** la liste de celles qui sont dans la grille et ne sont pas des murs.

    ```python
    def cases_voisines(grille, case):
        ligne, colonne = case
        candidates = [(ligne - 1, colonne), (ligne + 1, colonne),
                      (ligne, colonne - 1), (ligne, colonne + 1)]
        return [(l, c) for (l, c) in candidates
                if 0 <= l < len(grille) and 0 <= c < len(grille[l])
                and grille[l][c] != "#"]
    ```

    *Autre méthode :* on part d’une liste vide et on ajoute chaque candidate valable avec `append`.

    ```python
        voisines = []
        for (l, c) in candidates:
            if 0 <= l < len(grille) and 0 <= c < len(grille[l]) and grille[l][c] != "#":
                voisines.append((l, c))
        return voisines
    ```

    Le test des bornes n’est pas indispensable ici (les labyrinthes sont entourés de murs), mais il rend la fonction sûre pour n’importe quelle grille.

    ```python
        assert cases_voisines(grille, (1, 3)) == [(1, 2), (1, 4)]
    ```

    $\blacktriangleright$ Appel professeur. expliquer le calcul des quatre voisines (quelle coordonnée change, dans quel sens) et l’ordre imposé.

    Question 2

    *Compléter `plus_court_chemin` (parcours en largeur).*

    Quand on découvre un voisin, il faut : le marquer comme découvert, l’enfiler, et noter son parent.

    ```python
            for voisin in graphe[sommet]:
                if voisin not in decouverts:
                    decouverts.append(voisin)
                    en_attente.append(voisin)
                    parent[voisin] = sommet
    ```

    ```python
        assert plus_court_chemin(graphe, (1, 1), (1, 1)) == [(1, 1)]
        assert plus_court_chemin(graphe, (1, 1), (3, 3)) == [(1, 1), (2, 1), (3, 1), (3, 2), (3, 3)]
    ```

    Question 3

    *Utiliser `sortir` sur `labyrinthe.txt`.*

    ```console
    >>> sortir("labyrinthe.txt")
    #####################
    #Eoooooooo#         #
    #########o####### # #
    #       #ooooooo  # #
    # # # # #######o### #
    # #       #    o    #
    # ##### ### ###o#####
    #     #     #  ooooo#
    ### # ####### #####o#
    #             #    S#
    #####################
    26
    ```

    Il faut **26 déplacements** (le chemin compte 27 cases, entrée et sortie comprises).

    $\blacktriangleright$ Appel professeur. expliquer pourquoi le parcours en largeur donne un plus court chemin : il découvre les cases par distance croissante à l’entrée, et le parent d’une case est toujours à distance un de moins.

    Question 4

    *Remplacer `pop(0)` par `pop()` : obtient-on encore un chemin ? le plus court ?*

    ```console
    >>> sortir("labyrinthe.txt")
    #####################
    #Eoooooooo#      ooo#
    #########o#######o#o#
    #ooo    #ooooooooo#o#
    #o#o# # ####### ###o#
    #o#ooooo  #ooooooooo#
    #o#####o###o### #####
    #ooooo#ooooo#ooooooo#
    ### #o#######o#####o#
    #    ooooooooo#    S#
    #####################
    78
    ```

    On obtient encore un chemin **valide** de l’entrée à la sortie (chaque case a pour parent une case voisine), mais de **78** déplacements au lieu de 26 : ce n’est plus le plus court.

    Avec `pop()`, `en_attente` n’est plus une file mais une **pile** : on repart toujours de la dernière case découverte, on s’enfonce le plus loin possible avant de revenir en arrière. C’est un **parcours en profondeur**, qui ne découvre plus les cases par distance croissante. Comme ce labyrinthe contient des **cycles** (plusieurs chemins possibles), le parent retenu pour une case n’est pas forcément sur un plus court chemin.

    $\blacktriangleright$ Appel professeur. faire le lien file $\leftrightarrow$ largeur, pile $\leftrightarrow$ profondeur, et expliquer que seul le parcours en largeur garantit un plus court chemin (en nombre d’arêtes).
