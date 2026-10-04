# Sujet 29 — Recherche dichotomique

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/pratique-29-dichotomie){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-pratique-29-dichotomie.zip){ .md-button }

??? corrige "Corrigé"

    !!! remarque "Remarque"

        On donne une version simple ; d’autres réponses sont possibles. Le fichier complet, `corrige_sujet_29.py`, est en ligne : [`github.com/MathThibaud/nsi-fichiers-eleves/tree/main/corriges/terminale/pratique-29`](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/corriges/terminale/pratique-29).

    Question 1

    *Écrire `recherche_dichotomique(tab, x)` avec une boucle `while`.*

    ```python
    def recherche_dichotomique(tab, x):
        debut = 0
        fin = len(tab) - 1
        while debut <= fin:
            milieu = (debut + fin) // 2
            if tab[milieu] == x:
                return milieu
            elif tab[milieu] < x:
                debut = milieu + 1
            else:
                fin = milieu - 1
        return -1
    ```

    Pour un tableau vide, `fin` vaut `-1` : on n’entre pas dans la boucle et on renvoie `-1`.

    $\blacktriangleright$ Appel professeur. justifier la terminaison : la longueur `fin - debut + 1` de la zone de recherche est un entier qui diminue strictement à chaque tour (grâce aux `+ 1` et `- 1`).

    Question 2

    *Compléter `comparaisons_dichotomique`, exécuter `comparer(1000)` et `comparer(1000000)`, expliquer.*

    Même boucle que la question 1, avec un compteur incrémenté à chaque élément du milieu examiné :

    ```python
    def comparaisons_dichotomique(tab, x):
        nb = 0
        debut = 0
        fin = len(tab) - 1
        while debut <= fin:
            milieu = (debut + fin) // 2
            nb = nb + 1
            if tab[milieu] == x:
                return nb
            elif tab[milieu] < x:
                debut = milieu + 1
            else:
                fin = milieu - 1
        return nb
    ```

    ```console
    >>> comparer(1000)
    n = 1000
      séquentielle : 1000
      dichotomique : 10
    >>> comparer(1000000)
    n = 1000000
      séquentielle : 1000000
      dichotomique : 20
    ```

    La valeur cherchée est absente : la recherche séquentielle examine les $n$ éléments (coût **linéaire**). La recherche dichotomique divise la zone par deux à chaque étape ; le nombre d’étapes est le nombre de divisions par 2 pour passer de $n$ à $0$, environ $\log_2(n)$ : $2^{10} = 1024$ et $2^{20} \approx 10^6$ (coût **logarithmique**). Multiplier la taille par 1000 ajoute seulement une dizaine de comparaisons.

    $\blacktriangleright$ Appel professeur. expliquer le lien entre « diviser par deux » et le logarithme en base 2.

    Question 3

    *Corriger `premiere_occurrence` (plus petit indice de `x`).*

    ```console
    >>> premiere_occurrence([1, 2, 2, 2, 3], 2)
    2
    ```

    L’erreur : dès que `tab[milieu] == x`, la fonction renvoie `milieu`, qui est **une** occurrence de `x`, pas forcément la première : d’autres `x` peuvent se trouver à gauche. Correction : quand on trouve `x`, on **mémorise** l’indice et on **continue** à chercher dans la moitié gauche.

    ```python
    def premiere_occurrence(tab, x):
        resultat = -1
        debut = 0
        fin = len(tab) - 1
        while debut <= fin:
            milieu = (debut + fin) // 2
            if tab[milieu] == x:
                resultat = milieu    # une occurrence, peut-etre pas la premiere :
                fin = milieu - 1     # on continue a chercher a gauche
            elif tab[milieu] < x:
                debut = milieu + 1
            else:
                fin = milieu - 1
        return resultat
    ```

    La zone continue d’être divisée par deux à chaque tour : le coût reste logarithmique.

    ```python
        assert premiere_occurrence([], 4) == -1
        assert premiere_occurrence([1, 1, 2, 2, 2, 2, 2, 2, 3], 2) == 2
    ```

    $\blacktriangleright$ Appel professeur. expliquer l’erreur sur l’exemple, puis pourquoi la version corrigée renvoie bien le plus petit indice et reste une dichotomie.

    Question 4

    *Écrire la fonction récursive `recherche_rec(tab, x, debut, fin)`.*

    La condition d’arrêt est la zone vide (`debut > fin`) ; sinon, on examine le milieu et on relance la recherche sur une seule moitié.

    ```python
    def recherche_rec(tab, x, debut, fin):
        if debut > fin:
            return -1
        milieu = (debut + fin) // 2
        if tab[milieu] == x:
            return milieu
        elif tab[milieu] < x:
            return recherche_rec(tab, x, milieu + 1, fin)
        else:
            return recherche_rec(tab, x, debut, milieu - 1)
    ```

    ```python
        assert recherche_rec(tab, 2, 0, len(tab) - 1) == 0
        assert recherche_rec([], 4, 0, -1) == -1
    ```

*Durée de l’épreuve : 1 heure.*

!!! encadre "Déroulement de l’épreuve"

    - Cette situation d’évaluation comporte ce document ainsi que des fichiers de codes et de données présents sur l’ordinateur. Le candidat doit **agir en autonomie** et faire preuve d’initiative tout au long de l’épreuve.

    - En cas de difficulté, le candidat peut solliciter l’examinateur. Des moments privilégiés sont indiqués sous la forme d’**appels professeur**. L’examinateur peut intervenir à tout moment s’il le juge utile.

On cherche une valeur `x` dans un tableau `tab` (une liste Python). La **recherche séquentielle**, fournie dans le fichier `dichotomie.py`, compare `x` à tous les éléments, l’un après l’autre.

Lorsque le tableau est **trié dans l’ordre croissant**, on peut faire beaucoup mieux avec la **recherche dichotomique** : on maintient deux indices `debut` et `fin` qui délimitent la zone où `x` peut encore se trouver (au départ, tout le tableau). Tant que cette zone n’est pas vide, on compare `x` à l’élément du milieu, d’indice `milieu = (debut + fin) // 2` :

- s’il est égal à `x`, on a trouvé ;

- s’il est plus petit que `x`, on continue dans la moitié droite (`debut = milieu + 1`) ;

- sinon, on continue dans la moitié gauche (`fin = milieu - 1`).

Si la zone devient vide (`debut > fin`), `x` n’est pas dans le tableau.

Question 1

Écrire le corps de la fonction `recherche_dichotomique(tab, x)` qui renvoie un indice où se trouve `x` dans le tableau trié `tab`, ou `-1` si `x` n’y est pas. La fonction utilisera une boucle `while`. Des tests sont fournis dans la fonction `test_recherche`.

**$\blacktriangleright$ Appel professeur.** Appeler le professeur pour lui présenter votre réponse ou en cas de difficulté.

Question 2

La fonction `comparaisons_sequentielle` renvoie le nombre d’éléments du tableau comparés à `x` par la recherche séquentielle. Compléter de même la fonction `comparaisons_dichotomique` (on compte un passage dans la boucle pour chaque élément du milieu examiné), puis exécuter `comparer(1000)` et `comparer(1000000)`. Comparer et expliquer les nombres obtenus.

**$\blacktriangleright$ Appel professeur.** Appeler le professeur pour lui présenter votre réponse ou en cas de difficulté.

Question 3

Le tableau peut contenir plusieurs fois la même valeur. La fonction `premiere_occurrence(tab, x)` doit renvoyer le **plus petit** indice où se trouve `x`, en effectuant elle aussi une recherche dichotomique, mais le test `test_premiere_occurrence` échoue. Trouver l’erreur et corriger la fonction, sans en faire une recherche séquentielle.

**$\blacktriangleright$ Appel professeur.** Appeler le professeur pour lui présenter votre réponse ou en cas de difficulté.

Question 4

Écrire le corps de la fonction **récursive** `recherche_rec(tab, x, debut, fin)` qui cherche `x` entre les indices `debut` et `fin` (inclus) du tableau trié `tab` et renvoie un indice où il se trouve, ou `-1`. Pour chercher dans tout le tableau, on appelle `recherche_rec(tab, x, 0, len(tab) - 1)`. Tester avec la fonction `test_recherche_rec`.

### Description du dossier

Le dossier fourni au candidat comporte les éléments suivants :

- une version PDF de l’énoncé ;

- un code source de départ `dichotomie.py`.

??? corrige "Corrigé"

    !!! remarque "Remarque"

        On donne une version simple ; d’autres réponses sont possibles. Le fichier complet, `corrige_sujet_29.py`, est en ligne : [`github.com/MathThibaud/nsi-fichiers-eleves/tree/main/corriges/terminale/pratique-29`](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/corriges/terminale/pratique-29).

    Question 1

    *Écrire `recherche_dichotomique(tab, x)` avec une boucle `while`.*

    ```python
    def recherche_dichotomique(tab, x):
        debut = 0
        fin = len(tab) - 1
        while debut <= fin:
            milieu = (debut + fin) // 2
            if tab[milieu] == x:
                return milieu
            elif tab[milieu] < x:
                debut = milieu + 1
            else:
                fin = milieu - 1
        return -1
    ```

    Pour un tableau vide, `fin` vaut `-1` : on n’entre pas dans la boucle et on renvoie `-1`.

    $\blacktriangleright$ Appel professeur. justifier la terminaison : la longueur `fin - debut + 1` de la zone de recherche est un entier qui diminue strictement à chaque tour (grâce aux `+ 1` et `- 1`).

    Question 2

    *Compléter `comparaisons_dichotomique`, exécuter `comparer(1000)` et `comparer(1000000)`, expliquer.*

    Même boucle que la question 1, avec un compteur incrémenté à chaque élément du milieu examiné :

    ```python
    def comparaisons_dichotomique(tab, x):
        nb = 0
        debut = 0
        fin = len(tab) - 1
        while debut <= fin:
            milieu = (debut + fin) // 2
            nb = nb + 1
            if tab[milieu] == x:
                return nb
            elif tab[milieu] < x:
                debut = milieu + 1
            else:
                fin = milieu - 1
        return nb
    ```

    ```console
    >>> comparer(1000)
    n = 1000
      séquentielle : 1000
      dichotomique : 10
    >>> comparer(1000000)
    n = 1000000
      séquentielle : 1000000
      dichotomique : 20
    ```

    La valeur cherchée est absente : la recherche séquentielle examine les $n$ éléments (coût **linéaire**). La recherche dichotomique divise la zone par deux à chaque étape ; le nombre d’étapes est le nombre de divisions par 2 pour passer de $n$ à $0$, environ $\log_2(n)$ : $2^{10} = 1024$ et $2^{20} \approx 10^6$ (coût **logarithmique**). Multiplier la taille par 1000 ajoute seulement une dizaine de comparaisons.

    $\blacktriangleright$ Appel professeur. expliquer le lien entre « diviser par deux » et le logarithme en base 2.

    Question 3

    *Corriger `premiere_occurrence` (plus petit indice de `x`).*

    ```console
    >>> premiere_occurrence([1, 2, 2, 2, 3], 2)
    2
    ```

    L’erreur : dès que `tab[milieu] == x`, la fonction renvoie `milieu`, qui est **une** occurrence de `x`, pas forcément la première : d’autres `x` peuvent se trouver à gauche. Correction : quand on trouve `x`, on **mémorise** l’indice et on **continue** à chercher dans la moitié gauche.

    ```python
    def premiere_occurrence(tab, x):
        resultat = -1
        debut = 0
        fin = len(tab) - 1
        while debut <= fin:
            milieu = (debut + fin) // 2
            if tab[milieu] == x:
                resultat = milieu    # une occurrence, peut-etre pas la premiere :
                fin = milieu - 1     # on continue a chercher a gauche
            elif tab[milieu] < x:
                debut = milieu + 1
            else:
                fin = milieu - 1
        return resultat
    ```

    La zone continue d’être divisée par deux à chaque tour : le coût reste logarithmique.

    ```python
        assert premiere_occurrence([], 4) == -1
        assert premiere_occurrence([1, 1, 2, 2, 2, 2, 2, 2, 3], 2) == 2
    ```

    $\blacktriangleright$ Appel professeur. expliquer l’erreur sur l’exemple, puis pourquoi la version corrigée renvoie bien le plus petit indice et reste une dichotomie.

    Question 4

    *Écrire la fonction récursive `recherche_rec(tab, x, debut, fin)`.*

    La condition d’arrêt est la zone vide (`debut > fin`) ; sinon, on examine le milieu et on relance la recherche sur une seule moitié.

    ```python
    def recherche_rec(tab, x, debut, fin):
        if debut > fin:
            return -1
        milieu = (debut + fin) // 2
        if tab[milieu] == x:
            return milieu
        elif tab[milieu] < x:
            return recherche_rec(tab, x, milieu + 1, fin)
        else:
            return recherche_rec(tab, x, debut, milieu - 1)
    ```

    ```python
        assert recherche_rec(tab, 2, 0, len(tab) - 1) == 0
        assert recherche_rec([], 4, 0, -1) == -1
    ```
