# Sujet 32 — Le grand escalier

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/pratique-32-grand-escalier){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-pratique-32-grand-escalier.zip){ .md-button }

??? corrige "Corrigé"

    !!! remarque "Remarque"

        On donne une version simple ; d’autres réponses sont possibles. Le fichier complet, `corrige_sujet_32.py`, est en ligne : [`github.com/MathThibaud/nsi-fichiers-eleves/tree/main/corriges/terminale/pratique-32`](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/corriges/terminale/pratique-32).

    Question 1

    *Justifier la relation, puis écrire `effort_rec(couts, i)`.*

    On arrive sur la marche `i` soit depuis la marche `i - 1` (un pas d’une marche), soit depuis la marche `i - 2` (un pas de deux marches). Dans les deux cas, on paie ensuite l’effort de la marche `i`. On a intérêt à venir de celle des deux où l’on arrive avec le moins d’effort, d’où `E(i) = couts[i] + min(E(i - 1), E(i - 2))`. Les marches $0$ et $1$ s’atteignent directement depuis le sol : ce sont les deux cas de base.

    ```python
    def effort_rec(couts, i):
        if i == 0 or i == 1:
            return couts[i]
        return couts[i] + min(effort_rec(couts, i - 1), effort_rec(couts, i - 2))
    ```

    $\blacktriangleright$ Appel professeur. justifier la terminaison : `i` est un entier positif qui diminue strictement à chaque appel, jusqu’à $0$ ou $1$.

    Question 2

    *Exécuter `compter_appels` pour $10$, $20$ et $25$ marches, expliquer la croissance.*

    ```console
    >>> compter_appels(10), compter_appels(20), compter_appels(25)
    (176, 21890, 242784)
    ```

    L’appel $E(4)$ lance $E(3)$ et $E(2)$ ; or $E(3)$ relance lui-même $E(2)$ et $E(1)$. $E(2)$ est donc calculé **deux fois**, $E(1)$ trois fois, et ainsi de suite : les sous-problèmes **se recouvrent**. Chaque marche supplémentaire multiplie environ par $1{,}6$ le nombre d’appels (comme la suite de Fibonacci) : le coût est **exponentiel**. Pour $100$ marches, il faudrait de l’ordre de $10^{21}$ appels : c’est impossible en pratique.

    $\blacktriangleright$ Appel professeur. dessiner l’arbre des appels de $E(4)$ et y repérer les calculs répétés.

    Question 3

    *Écrire `effort_memo(couts, i, memo)`, puis calculer l’effort pour `escalier.txt`.*

    ```python
    def effort_memo(couts, i, memo):
        if i == 0 or i == 1:
            return couts[i]
        if i in memo:                    # deja calcule : on le relit
            return memo[i]
        memo[i] = couts[i] + min(effort_memo(couts, i - 1, memo),
                                 effort_memo(couts, i - 2, memo))
        return memo[i]
    ```

    ```console
    >>> effort_total_memo(lire_escalier("escalier.txt"))
    185
    ```

    Chaque $E(i)$ n’est plus calculé qu’une fois : le coût devient **linéaire** en le nombre de marches.

    $\blacktriangleright$ Appel professeur. expliquer pourquoi le même dictionnaire `memo` doit être partagé par tous les appels.

    Question 4

    *Écrire `effort_tab(couts)`, puis comparer avec la stratégie gloutonne.*

    On remplit la liste du bas vers le haut : quand on calcule `e[i]`, les valeurs `e[i - 1]` et `e[i - 2]` sont déjà connues.

    ```python
    def effort_tab(couts):
        n = len(couts)
        e = [0] * n
        e[0] = couts[0]
        e[1] = couts[1]
        for i in range(2, n):
            e[i] = couts[i] + min(e[i - 1], e[i - 2])
        return min(e[n - 1], e[n - 2])
    ```

    ```console
    >>> effort_tab([10, 15, 20]), effort_glouton([10, 15, 20])
    (15, 25)
    >>> couts = lire_escalier("escalier.txt")
    >>> effort_tab(couts), effort_glouton(couts)
    (185, 213)
    ```

    Sur `[10, 15, 20]`, le glouton choisit la marche $0$ (effort $10$, la moins pénible des deux premières), puis la marche $1$ ($15$) : il paie $25$. Or monter directement sur la marche $1$ ne coûte que $15$. Le glouton fait à chaque pas le choix qui semble le meilleur sur le moment, sans jamais revenir en arrière. La programmation dynamique, elle, compare **toutes** les possibilités grâce à la relation de récurrence, sans les énumérer une à une : elle trouve toujours le minimum.

    $\blacktriangleright$ Appel professeur. citer un autre problème du cours où le glouton n’est pas optimal (rendu de monnaie avec le système $\{1, 3, 4\}$).

*Durée de l’épreuve : 1 heure.*

!!! encadre "Déroulement de l’épreuve"

    - Cette situation d’évaluation comporte ce document ainsi que des fichiers de codes et de données présents sur l’ordinateur. Le candidat doit **agir en autonomie** et faire preuve d’initiative tout au long de l’épreuve.

    - En cas de difficulté, le candidat peut solliciter l’examinateur. Des moments privilégiés sont indiqués sous la forme d’**appels professeur**. L’examinateur peut intervenir à tout moment s’il le juge utile.

Pour monter au Rocher, on emprunte un long escalier. Chaque marche demande un certain **effort** (elle est plus ou moins haute, glissante…), donné par un entier. On part du sol, au pied de l’escalier, et l’on monte à chaque pas **d’une ou de deux marches**. On paie l’effort de chaque marche sur laquelle on pose le pied. Le sommet est situé juste au-dessus de la dernière marche : on l’atteint depuis la dernière ou l’avant-dernière marche, sans effort supplémentaire.

Les efforts sont rangés dans une liste `couts` : `couts[i]` est l’effort de la marche `i`, numérotée à partir de $0$ (la plus basse). Par exemple, pour `couts = [10, 15, 20]`, le meilleur choix consiste à monter directement sur la marche $1$ (deux marches d’un coup), puis à sauter au sommet : l’effort total vaut $15$.

On note $E(i)$ l’effort minimal pour arriver sur la marche `i` (effort de la marche `i` compris). On a `E(0) = couts[0]`, `E(1) = couts[1]` et, pour $i \geqslant 2$ :

`E(i) = couts[i] + min(E(i - 1), E(i - 2))`

L’effort minimal pour atteindre le sommet d’un escalier de $n$ marches vaut alors `min(E(n - 1), E(n - 2))`.

Question 1

Justifier la relation donnant $E(i)$ en considérant la marche d’où l’on arrive sur la marche `i`. Écrire ensuite le corps de la fonction récursive `effort_rec(couts, i)` du fichier `escalier.py`, qui renvoie $E(i)$. Des tests sont fournis dans la fonction `test_effort_rec`.

**$\blacktriangleright$ Appel professeur.** Appeler le professeur pour lui présenter votre réponse ou en cas de difficulté.

Question 2

La fonction `compter_appels(n)` renvoie le nombre d’appels effectués par la version récursive pour un escalier de `n` marches. L’exécuter pour `n` valant $10$, $20$ et $25$. Dessiner le début de l’arbre des appels de $E(4)$ et expliquer pourquoi le nombre d’appels augmente si vite. Peut-on utiliser cette version pour l’escalier du fichier `escalier.txt`, qui compte $100$ marches ?

*Attention : ne pas appeler `effort_rec` sur un escalier de plus de $30$ marches, le calcul ne se terminerait pas en un temps raisonnable.*

**$\blacktriangleright$ Appel professeur.** Appeler le professeur pour lui présenter votre réponse ou en cas de difficulté.

Question 3

Écrire le corps de la fonction `effort_memo(couts, i, memo)`, qui renvoie elle aussi $E(i)$, mais mémorise dans le dictionnaire `memo` chaque valeur calculée, pour ne jamais la recalculer. Tester avec `test_effort_memo`, puis déterminer l’effort minimal pour monter l’escalier du fichier `escalier.txt` à l’aide des fonctions `lire_escalier` et `effort_total_memo`.

**$\blacktriangleright$ Appel professeur.** Appeler le professeur pour lui présenter votre réponse ou en cas de difficulté.

Question 4

Écrire le corps de la fonction `effort_tab(couts)`, qui calcule l’effort minimal pour atteindre le sommet **sans récursivité**, en remplissant une liste `e` du bas vers le haut de l’escalier (`e[i]` contient $E(i)$). Tester avec `test_effort_tab`.

La fonction `effort_glouton(couts)` fournie applique une stratégie gloutonne : poser toujours le pied sur la moins pénible des deux marches suivantes. Comparer son résultat à celui de `effort_tab` sur `[10, 15, 20]` et sur l’escalier du fichier, puis expliquer la différence.

### Description du dossier

Le dossier fourni au candidat comporte les éléments suivants :

- une version PDF de l’énoncé ;

- un code source de départ `escalier.py` ;

- un fichier de données `escalier.txt`.

??? corrige "Corrigé"

    !!! remarque "Remarque"

        On donne une version simple ; d’autres réponses sont possibles. Le fichier complet, `corrige_sujet_32.py`, est en ligne : [`github.com/MathThibaud/nsi-fichiers-eleves/tree/main/corriges/terminale/pratique-32`](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/corriges/terminale/pratique-32).

    Question 1

    *Justifier la relation, puis écrire `effort_rec(couts, i)`.*

    On arrive sur la marche `i` soit depuis la marche `i - 1` (un pas d’une marche), soit depuis la marche `i - 2` (un pas de deux marches). Dans les deux cas, on paie ensuite l’effort de la marche `i`. On a intérêt à venir de celle des deux où l’on arrive avec le moins d’effort, d’où `E(i) = couts[i] + min(E(i - 1), E(i - 2))`. Les marches $0$ et $1$ s’atteignent directement depuis le sol : ce sont les deux cas de base.

    ```python
    def effort_rec(couts, i):
        if i == 0 or i == 1:
            return couts[i]
        return couts[i] + min(effort_rec(couts, i - 1), effort_rec(couts, i - 2))
    ```

    $\blacktriangleright$ Appel professeur. justifier la terminaison : `i` est un entier positif qui diminue strictement à chaque appel, jusqu’à $0$ ou $1$.

    Question 2

    *Exécuter `compter_appels` pour $10$, $20$ et $25$ marches, expliquer la croissance.*

    ```console
    >>> compter_appels(10), compter_appels(20), compter_appels(25)
    (176, 21890, 242784)
    ```

    L’appel $E(4)$ lance $E(3)$ et $E(2)$ ; or $E(3)$ relance lui-même $E(2)$ et $E(1)$. $E(2)$ est donc calculé **deux fois**, $E(1)$ trois fois, et ainsi de suite : les sous-problèmes **se recouvrent**. Chaque marche supplémentaire multiplie environ par $1{,}6$ le nombre d’appels (comme la suite de Fibonacci) : le coût est **exponentiel**. Pour $100$ marches, il faudrait de l’ordre de $10^{21}$ appels : c’est impossible en pratique.

    $\blacktriangleright$ Appel professeur. dessiner l’arbre des appels de $E(4)$ et y repérer les calculs répétés.

    Question 3

    *Écrire `effort_memo(couts, i, memo)`, puis calculer l’effort pour `escalier.txt`.*

    ```python
    def effort_memo(couts, i, memo):
        if i == 0 or i == 1:
            return couts[i]
        if i in memo:                    # deja calcule : on le relit
            return memo[i]
        memo[i] = couts[i] + min(effort_memo(couts, i - 1, memo),
                                 effort_memo(couts, i - 2, memo))
        return memo[i]
    ```

    ```console
    >>> effort_total_memo(lire_escalier("escalier.txt"))
    185
    ```

    Chaque $E(i)$ n’est plus calculé qu’une fois : le coût devient **linéaire** en le nombre de marches.

    $\blacktriangleright$ Appel professeur. expliquer pourquoi le même dictionnaire `memo` doit être partagé par tous les appels.

    Question 4

    *Écrire `effort_tab(couts)`, puis comparer avec la stratégie gloutonne.*

    On remplit la liste du bas vers le haut : quand on calcule `e[i]`, les valeurs `e[i - 1]` et `e[i - 2]` sont déjà connues.

    ```python
    def effort_tab(couts):
        n = len(couts)
        e = [0] * n
        e[0] = couts[0]
        e[1] = couts[1]
        for i in range(2, n):
            e[i] = couts[i] + min(e[i - 1], e[i - 2])
        return min(e[n - 1], e[n - 2])
    ```

    ```console
    >>> effort_tab([10, 15, 20]), effort_glouton([10, 15, 20])
    (15, 25)
    >>> couts = lire_escalier("escalier.txt")
    >>> effort_tab(couts), effort_glouton(couts)
    (185, 213)
    ```

    Sur `[10, 15, 20]`, le glouton choisit la marche $0$ (effort $10$, la moins pénible des deux premières), puis la marche $1$ ($15$) : il paie $25$. Or monter directement sur la marche $1$ ne coûte que $15$. Le glouton fait à chaque pas le choix qui semble le meilleur sur le moment, sans jamais revenir en arrière. La programmation dynamique, elle, compare **toutes** les possibilités grâce à la relation de récurrence, sans les énumérer une à une : elle trouve toujours le minimum.

    $\blacktriangleright$ Appel professeur. citer un autre problème du cours où le glouton n’est pas optimal (rendu de monnaie avec le système $\{1, 3, 4\}$).
