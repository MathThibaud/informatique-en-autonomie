# Sujet 31 — Recherche d'un motif

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/pratique-31-recherche-motif){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-pratique-31-recherche-motif.zip){ .md-button }

??? corrige "Corrigé"

    !!! remarque "Remarque"

        On donne une version simple ; d’autres réponses sont possibles. Le fichier complet, `corrige_sujet_31.py`, est en ligne : [`github.com/MathThibaud/nsi-fichiers-eleves/tree/main/corriges/terminale/pratique-31`](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/corriges/terminale/pratique-31).

    Question 1

    *Écrire `recherche_naive(motif, texte)`, puis compter les occurrences de `"GATTACA"` dans `adn.txt`.*

    ```python
    def recherche_naive(motif, texte):
        n = len(texte)
        m = len(motif)
        positions = []
        for i in range(n - m + 1):
            j = 0
            while j < m and texte[i + j] == motif[j]:
                j = j + 1
            if j == m:
                positions.append(i)
        return positions
    ```

    Le `range(n - m + 1)` évite de dépasser la fin du texte (dernière position possible : `n - m`). Si le motif est plus long que le texte, la boucle ne fait aucun tour.

    ```console
    >>> adn = lire_fichier("adn.txt")
    >>> len(recherche_naive("GATTACA", adn))
    13
    ```

    $\blacktriangleright$ Appel professeur. expliquer le rôle de `n - m + 1` et l’ordre des deux conditions du `while` (on teste `j < m` avant de lire `motif[j]`).

    Question 2

    *Écrire `table_decalage(motif)`.*

    ```python
    def table_decalage(motif):
        m = len(motif)
        dec = {}
        for k in range(m - 1):        # toutes les lettres sauf la derniere
            dec[motif[k]] = m - 1 - k
        return dec
    ```

    On parcourt le motif de gauche à droite : pour une lettre répétée, la dernière affectation (la plus proche de la fin, donc la plus petite valeur) écrase les précédentes. Pour `"GATTACA"`, le `A` d’indice $1$ reçoit d’abord $5$, puis celui d’indice $4$ lui donne $2$. La dernière lettre n’est pas dans la table : sinon elle recevrait $0$, et le motif ne bougerait plus.

    $\blacktriangleright$ Appel professeur. expliquer pourquoi on garde la plus petite distance (ne jamais sauter par-dessus une occurrence possible).

    Question 3

    *Trouver et corriger l’erreur de `horspool`.*

    ```console
    >>> horspool("ABA", "ABABABA")
    [0, 4]
    ```

    Après une occurrence trouvée, la fonction fait `i = i + m` : elle saute toute la longueur du motif et manque les occurrences qui **chevauchent** celle qu’on vient de trouver (ici celle en position $2$). Après une occurrence, il faut décaler comme après un échec, avec la table, sans dépasser une autre occurrence possible :

    ```python
            if j < 0:
                positions.append(i)
            c = texte[i + m - 1]
            if c in dec:
                i = i + dec[c]
            else:
                i = i + m
    ```

    Sur `adn.txt`, `horspool("GATTACA", adn)` renvoie alors la même liste que `recherche_naive` (13 positions).

    $\blacktriangleright$ Appel professeur. montrer l’erreur sur `"AA"` dans `"AAAA"` et justifier le décalage après une occurrence.

    Question 4

    *Compléter `comparaisons_horspool`, exécuter `comparer()` et commenter.*

    On reprend la boucle de `horspool` corrigée, en comptant chaque comparaison, y compris celle qui échoue :

    ```python
    def comparaisons_horspool(motif, texte):
        n = len(texte)
        m = len(motif)
        dec = table_decalage(motif)
        nb = 0
        i = 0
        while i <= n - m:
            j = m - 1
            while j >= 0 and texte[i + j] == motif[j]:
                nb = nb + 1                # comparaison reussie
                j = j - 1
            if j >= 0:
                nb = nb + 1                # la comparaison qui a echoue
            c = texte[i + m - 1]
            if c in dec:
                i = i + dec[c]
            else:
                i = i + m
        return nb
    ```

    ```console
    >>> comparer()
    motif de longueur 7 dans un texte de longueur 100000
      naïve    : 133510
      horspool : 47069
    motif de longueur 13 dans un texte de longueur 105000
      naïve    : 113985
      horspool : 13497
    motif de longueur 10 dans un texte de longueur 100000
      naïve    : 999910
      horspool : 99991
    ```

    - **ADN** : Horspool fait environ $3$ fois moins de comparaisons. Avec seulement $4$ lettres, presque toutes figurent dans le motif, près de sa fin : les sauts restent courts.

    - **Texte français** : avec un alphabet plus grand, beaucoup de caractères (`P`, `U`, `S`…) sont absents du motif et provoquent un saut de toute sa longueur ($13$). Horspool fait environ $8$ fois moins de comparaisons : il ne lit même pas la plupart des caractères du texte (coût **sous-linéaire**).

    - **Pire cas de la méthode naïve** : à chaque position, elle compare $9$ `A` avant d’échouer sur le `B`, soit environ $n \times m$ comparaisons. Horspool, qui commence par la fin, échoue dès la première comparaison (`B` différent de `A`) et n’en fait qu’une par position.

    $\blacktriangleright$ Appel professeur. expliquer pourquoi la taille de l’alphabet et la longueur du motif influent sur l’efficacité de Horspool.

*Durée de l’épreuve : 1 heure.*

!!! encadre "Déroulement de l’épreuve"

    - Cette situation d’évaluation comporte ce document ainsi que des fichiers de codes et de données présents sur l’ordinateur. Le candidat doit **agir en autonomie** et faire preuve d’initiative tout au long de l’épreuve.

    - En cas de difficulté, le candidat peut solliciter l’examinateur. Des moments privilégiés sont indiqués sous la forme d’**appels professeur**. L’examinateur peut intervenir à tout moment s’il le juge utile.

On cherche toutes les positions où un **motif** (une chaîne de longueur `m`) apparaît dans un **texte** (une chaîne de longueur `n`). Une occurrence commence à la position `i` si `texte[i + j] == motif[j]` pour tout `j` de `0` à `m - 1`. Par exemple, `"AA"` apparaît aux positions `0`, `1` et `2` dans `"AAAA"` : les occurrences peuvent se chevaucher.

Le fichier `adn.txt` contient un brin d’ADN de $100\,000$ bases (lettres `A`, `C`, `G`, `T`). La fonction `lire_fichier` fournie dans `recherche.py` renvoie son contenu sous forme de chaîne.

Question 1

Dans la **méthode naïve**, on place le motif sous le texte à chaque position `i` possible, et on compare les caractères de gauche à droite jusqu’au premier désaccord. Écrire le corps de la fonction `recherche_naive(motif, texte)`, qui renvoie la liste de toutes les positions où commence une occurrence. Tester avec `test_recherche_naive`, puis déterminer combien de fois le motif `"GATTACA"` apparaît dans le brin d’ADN.

**$\blacktriangleright$ Appel professeur.** Appeler le professeur pour lui présenter votre réponse ou en cas de difficulté.

Question 2

L’algorithme de **Boyer-Moore-Horspool** compare le motif au texte de **droite à gauche**. En cas d’échec, il regarde le caractère `c` du texte aligné avec la **dernière** case du motif et décale le motif d’autant de cases que l’indique une **table de décalage** :

- chaque lettre du motif, **sauf la dernière**, est associée à sa distance à la fin du motif : la lettre d’indice `k` reçoit `m - 1 - k` (pour une lettre répétée, on garde la valeur la plus petite) ;

- une lettre absente de la table provoque un décalage de `m`.

Par exemple, la table de `"MOTIF"` est :

`{"M": 4, "O": 3, "T": 2, "I": 1}`

Écrire le corps de la fonction `table_decalage(motif)`, qui renvoie cette table sous forme de dictionnaire. Tester avec `test_table_decalage`.

**$\blacktriangleright$ Appel professeur.** Appeler le professeur pour lui présenter votre réponse ou en cas de difficulté.

Question 3

La fonction `horspool(motif, texte)` fournie programme cet algorithme, mais le test `test_horspool` échoue : certaines occurrences ne sont pas trouvées. Trouver l’erreur et corriger la fonction.

**$\blacktriangleright$ Appel professeur.** Appeler le professeur pour lui présenter votre réponse ou en cas de difficulté.

Question 4

La fonction `comparaisons_naive` renvoie le nombre de comparaisons de caractères effectuées par la méthode naïve. Compléter de même la fonction `comparaisons_horspool` (on compte chaque comparaison entre un caractère du texte et un caractère du motif). Tester avec `test_comparaisons`, puis exécuter `comparer()`. Commenter les résultats obtenus pour chacun des trois cas.

### Description du dossier

Le dossier fourni au candidat comporte les éléments suivants :

- une version PDF de l’énoncé ;

- un code source de départ `recherche.py` ;

- un fichier de données `adn.txt`.

??? corrige "Corrigé"

    !!! remarque "Remarque"

        On donne une version simple ; d’autres réponses sont possibles. Le fichier complet, `corrige_sujet_31.py`, est en ligne : [`github.com/MathThibaud/nsi-fichiers-eleves/tree/main/corriges/terminale/pratique-31`](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/corriges/terminale/pratique-31).

    Question 1

    *Écrire `recherche_naive(motif, texte)`, puis compter les occurrences de `"GATTACA"` dans `adn.txt`.*

    ```python
    def recherche_naive(motif, texte):
        n = len(texte)
        m = len(motif)
        positions = []
        for i in range(n - m + 1):
            j = 0
            while j < m and texte[i + j] == motif[j]:
                j = j + 1
            if j == m:
                positions.append(i)
        return positions
    ```

    Le `range(n - m + 1)` évite de dépasser la fin du texte (dernière position possible : `n - m`). Si le motif est plus long que le texte, la boucle ne fait aucun tour.

    ```console
    >>> adn = lire_fichier("adn.txt")
    >>> len(recherche_naive("GATTACA", adn))
    13
    ```

    $\blacktriangleright$ Appel professeur. expliquer le rôle de `n - m + 1` et l’ordre des deux conditions du `while` (on teste `j < m` avant de lire `motif[j]`).

    Question 2

    *Écrire `table_decalage(motif)`.*

    ```python
    def table_decalage(motif):
        m = len(motif)
        dec = {}
        for k in range(m - 1):        # toutes les lettres sauf la derniere
            dec[motif[k]] = m - 1 - k
        return dec
    ```

    On parcourt le motif de gauche à droite : pour une lettre répétée, la dernière affectation (la plus proche de la fin, donc la plus petite valeur) écrase les précédentes. Pour `"GATTACA"`, le `A` d’indice $1$ reçoit d’abord $5$, puis celui d’indice $4$ lui donne $2$. La dernière lettre n’est pas dans la table : sinon elle recevrait $0$, et le motif ne bougerait plus.

    $\blacktriangleright$ Appel professeur. expliquer pourquoi on garde la plus petite distance (ne jamais sauter par-dessus une occurrence possible).

    Question 3

    *Trouver et corriger l’erreur de `horspool`.*

    ```console
    >>> horspool("ABA", "ABABABA")
    [0, 4]
    ```

    Après une occurrence trouvée, la fonction fait `i = i + m` : elle saute toute la longueur du motif et manque les occurrences qui **chevauchent** celle qu’on vient de trouver (ici celle en position $2$). Après une occurrence, il faut décaler comme après un échec, avec la table, sans dépasser une autre occurrence possible :

    ```python
            if j < 0:
                positions.append(i)
            c = texte[i + m - 1]
            if c in dec:
                i = i + dec[c]
            else:
                i = i + m
    ```

    Sur `adn.txt`, `horspool("GATTACA", adn)` renvoie alors la même liste que `recherche_naive` (13 positions).

    $\blacktriangleright$ Appel professeur. montrer l’erreur sur `"AA"` dans `"AAAA"` et justifier le décalage après une occurrence.

    Question 4

    *Compléter `comparaisons_horspool`, exécuter `comparer()` et commenter.*

    On reprend la boucle de `horspool` corrigée, en comptant chaque comparaison, y compris celle qui échoue :

    ```python
    def comparaisons_horspool(motif, texte):
        n = len(texte)
        m = len(motif)
        dec = table_decalage(motif)
        nb = 0
        i = 0
        while i <= n - m:
            j = m - 1
            while j >= 0 and texte[i + j] == motif[j]:
                nb = nb + 1                # comparaison reussie
                j = j - 1
            if j >= 0:
                nb = nb + 1                # la comparaison qui a echoue
            c = texte[i + m - 1]
            if c in dec:
                i = i + dec[c]
            else:
                i = i + m
        return nb
    ```

    ```console
    >>> comparer()
    motif de longueur 7 dans un texte de longueur 100000
      naïve    : 133510
      horspool : 47069
    motif de longueur 13 dans un texte de longueur 105000
      naïve    : 113985
      horspool : 13497
    motif de longueur 10 dans un texte de longueur 100000
      naïve    : 999910
      horspool : 99991
    ```

    - **ADN** : Horspool fait environ $3$ fois moins de comparaisons. Avec seulement $4$ lettres, presque toutes figurent dans le motif, près de sa fin : les sauts restent courts.

    - **Texte français** : avec un alphabet plus grand, beaucoup de caractères (`P`, `U`, `S`…) sont absents du motif et provoquent un saut de toute sa longueur ($13$). Horspool fait environ $8$ fois moins de comparaisons : il ne lit même pas la plupart des caractères du texte (coût **sous-linéaire**).

    - **Pire cas de la méthode naïve** : à chaque position, elle compare $9$ `A` avant d’échouer sur le `B`, soit environ $n \times m$ comparaisons. Horspool, qui commence par la fin, échoue dès la première comparaison (`B` différent de `A`) et n’en fait qu’une par position.

    $\blacktriangleright$ Appel professeur. expliquer pourquoi la taille de l’alphabet et la longueur du motif influent sur l’efficacité de Horspool.
