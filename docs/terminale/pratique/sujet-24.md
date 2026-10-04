# Sujet 24 — Arbre d'une expression arithmétique

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/pratique-24-arbre-expression){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-pratique-24-arbre-expression.zip){ .md-button }

??? corrige "Corrigé"

    !!! remarque "Remarque"

        On donne une version simple ; d’autres réponses sont possibles. Le fichier complet, `corrige_sujet_24.py`, est en ligne : [`github.com/MathThibaud/nsi-fichiers-eleves/tree/main/corriges/terminale/pratique-24`](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/corriges/terminale/pratique-24).

    Question 1

    *Dessiner `e4` et `e5`, donner l’expression et la valeur de chacun. Pourquoi un arbre n’a-t-il pas besoin de parenthèses ?*

    `e4 = Noeud(’-’, Noeud(’-’, Noeud(8), Noeud(3)), Noeud(1))` : la racine `-` a pour fils gauche le nœud `-` (de fils `8` et `3`) et pour fils droit la feuille `1`. Elle représente $(8-3)-1 = 4$.

    `e5 = Noeud(’-’, Noeud(8), Noeud(’-’, Noeud(3), Noeud(1)))` : la racine `-` a pour fils gauche la feuille `8` et pour fils droit le nœud `-` (de fils `3` et `1`). Elle représente $8-(3-1) = 6$.

    Les deux arbres ont les mêmes nombres et les mêmes opérateurs, mais pas la même forme, et pas la même valeur. C’est la **forme de l’arbre** qui dit dans quel ordre les calculs sont faits : un opérateur s’applique aux valeurs de ses deux sous-arbres, qu’il faut donc calculer avant lui. Les parenthèses (et les règles de priorité) ne servent qu’à retrouver cette structure à partir d’une écriture sur une ligne ; dans l’arbre, elle est déjà explicite.

    $\blacktriangleright$ Appel professeur. dessiner les deux arbres, justifier les valeurs 4 et 6 et expliquer que la structure de l’arbre remplace les parenthèses.

    Question 2

    *Expliquer pourquoi `en_chaine(e1)` est ambigu, puis corriger la fonction.*

    ```console
    >>> en_chaine(e1)
    '3 + 5 * 7 - 2'
    ```

    Sans parenthèses, avec les règles de priorité habituelles, cette chaîne vaut $3 + 35 - 2 = 36$ et non $40$ : on a perdu la structure de l’arbre (et `e4` et `e5` donneraient la même chaîne `"8 - 3 - 1"`). Il suffit d’entourer de parenthèses chaque opération, c’est-à-dire le résultat de chaque nœud qui n’est pas une feuille :

    ```python
    def en_chaine(a):
        if est_feuille(a):
            return str(a.valeur)
        return "(" + en_chaine(a.gauche) + " " + a.valeur + " " + en_chaine(a.droite) + ")"
    ```

    ```python
        assert en_chaine(e2) == "((2 * (1 + 9)) - 4)"
        assert en_chaine(e4) == "((8 - 3) - 1)"
        assert en_chaine(e5) == "(8 - (3 - 1))"
    ```

    Question 3

    *Écrire la fonction récursive `evaluer`.*

    Une feuille vaut son nombre (cas de base). Sinon, on évalue récursivement les deux sous-arbres, puis on applique l’opérateur de la racine, **dans l’ordre** gauche puis droite (important pour la soustraction).

    ```python
    def evaluer(a):
        if est_feuille(a):
            return a.valeur
        valeur_gauche = evaluer(a.gauche)
        valeur_droite = evaluer(a.droite)
        if a.valeur == '+':
            return valeur_gauche + valeur_droite
        elif a.valeur == '-':
            return valeur_gauche - valeur_droite
        else:
            return valeur_gauche * valeur_droite
    ```

    ```python
        assert evaluer(e2) == 16
        assert evaluer(e4) == 4
        assert evaluer(e5) == 6
    ```

    $\blacktriangleright$ Appel professeur. identifier le cas de base et l’appel récursif, justifier la terminaison (chaque appel porte sur un sous-arbre strictement plus petit) et montrer que `e4` et `e5` donnent bien 4 et 6.

    Question 4

    *Écrire la fonction récursive `nb_operateurs`.*

    Une feuille ne contient aucun opérateur ; un nœud opérateur compte pour `1`, plus les opérateurs de ses deux sous-arbres.

    ```python
    def nb_operateurs(a):
        if est_feuille(a):
            return 0
        return 1 + nb_operateurs(a.gauche) + nb_operateurs(a.droite)
    ```

    ```python
        assert nb_operateurs(e2) == 3
        assert nb_operateurs(Noeud('+', Noeud(1), Noeud(2))) == 1
    ```

    $\blacktriangleright$ Appel professeur. faire le lien avec le calcul de la taille d’un arbre vu en cours (même schéma récursif, seul le cas de base change).

*Durée de l’épreuve : 1 heure.*

!!! encadre "Déroulement de l’épreuve"

    - Cette situation d’évaluation comporte ce document ainsi que des fichiers de codes et de données présents sur l’ordinateur. Le candidat doit **agir en autonomie** et faire preuve d’initiative tout au long de l’épreuve.

    - En cas de difficulté, le candidat peut solliciter l’examinateur. Des moments privilégiés sont indiqués sous la forme d’**appels professeur**. L’examinateur peut intervenir à tout moment s’il le juge utile.

Une expression arithmétique comme $(3+5)\times(7-2)$ peut être représentée par un **arbre binaire** : chaque **feuille** porte un nombre entier et chaque autre nœud porte un **opérateur** (`’+’`, `’-’` ou `’*’`) qui s’applique à la valeur de son sous-arbre gauche et à celle de son sous-arbre droit, **dans cet ordre**.

\*(image manquante : P24_arbre_e1)\*

**Figure 1.** L’arbre `e1` de l’expression $(3+5)\times(7-2)$.

Dans le fichier `expression.py`, un nœud est un objet de la classe `Noeud` (attributs `valeur`, `gauche` et `droite`) et la fonction `est_feuille` indique si un nœud n’a aucun fils. L’arbre de la figure 1 s’écrit :

```python
e1 = Noeud('*',
           Noeud('+', Noeud(3), Noeud(5)),
           Noeud('-', Noeud(7), Noeud(2)))
```

Le fichier définit aussi les arbres `e2`, `e3`, `e4` et `e5`. Les fonctions de ce sujet sont **récursives** : on traite séparément le cas d’une feuille, puis celui d’un opérateur, en s’appuyant sur les deux sous-arbres.

Question 1

Dessiner sur papier les arbres `e4` et `e5` définis dans le fichier, puis donner, pour chacun, l’expression qu’il représente et sa valeur. Expliquer pourquoi une expression représentée par un arbre n’a pas besoin de parenthèses.

**$\blacktriangleright$ Appel professeur.** Appeler le professeur pour lui présenter votre réponse ou en cas de difficulté.

Question 2

La fonction `en_chaine` doit renvoyer l’écriture de l’expression où chaque opération est entourée de parenthèses : `en_chaine(e1)` doit valoir `"((3 + 5) * (7 - 2))"`. Exécuter `en_chaine(e1)` et expliquer pourquoi le résultat obtenu est ambigu, puis corriger la fonction. La fonction `test_en_chaine` permet de vérifier la correction.

Question 3

Écrire le corps de la fonction récursive `evaluer` qui renvoie la valeur de l’expression représentée par un arbre. Par exemple `evaluer(e1)` doit renvoyer `40`. Des tests sont fournis dans la fonction `test_evaluer`, on pourra les compléter avec les arbres `e2`, `e4` et `e5`.

**$\blacktriangleright$ Appel professeur.** Appeler le professeur pour lui présenter votre réponse ou en cas de difficulté.

Question 4

Écrire le corps de la fonction récursive `nb_operateurs` qui renvoie le nombre d’opérateurs d’une expression (c’est-à-dire le nombre de nœuds qui ne sont pas des feuilles). Tester avec la fonction `test_nb_operateurs`.

**$\blacktriangleright$ Appel professeur.** Appeler le professeur pour lui présenter votre réponse ou en cas de difficulté.

### Description du dossier

Le dossier fourni au candidat comporte les éléments suivants :

- une version PDF de l’énoncé ;

- un code source de départ `expression.py` ;

- l’image de la figure 1 (`arbre_e1.png`).

??? corrige "Corrigé"

    !!! remarque "Remarque"

        On donne une version simple ; d’autres réponses sont possibles. Le fichier complet, `corrige_sujet_24.py`, est en ligne : [`github.com/MathThibaud/nsi-fichiers-eleves/tree/main/corriges/terminale/pratique-24`](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/corriges/terminale/pratique-24).

    Question 1

    *Dessiner `e4` et `e5`, donner l’expression et la valeur de chacun. Pourquoi un arbre n’a-t-il pas besoin de parenthèses ?*

    `e4 = Noeud(’-’, Noeud(’-’, Noeud(8), Noeud(3)), Noeud(1))` : la racine `-` a pour fils gauche le nœud `-` (de fils `8` et `3`) et pour fils droit la feuille `1`. Elle représente $(8-3)-1 = 4$.

    `e5 = Noeud(’-’, Noeud(8), Noeud(’-’, Noeud(3), Noeud(1)))` : la racine `-` a pour fils gauche la feuille `8` et pour fils droit le nœud `-` (de fils `3` et `1`). Elle représente $8-(3-1) = 6$.

    Les deux arbres ont les mêmes nombres et les mêmes opérateurs, mais pas la même forme, et pas la même valeur. C’est la **forme de l’arbre** qui dit dans quel ordre les calculs sont faits : un opérateur s’applique aux valeurs de ses deux sous-arbres, qu’il faut donc calculer avant lui. Les parenthèses (et les règles de priorité) ne servent qu’à retrouver cette structure à partir d’une écriture sur une ligne ; dans l’arbre, elle est déjà explicite.

    $\blacktriangleright$ Appel professeur. dessiner les deux arbres, justifier les valeurs 4 et 6 et expliquer que la structure de l’arbre remplace les parenthèses.

    Question 2

    *Expliquer pourquoi `en_chaine(e1)` est ambigu, puis corriger la fonction.*

    ```console
    >>> en_chaine(e1)
    '3 + 5 * 7 - 2'
    ```

    Sans parenthèses, avec les règles de priorité habituelles, cette chaîne vaut $3 + 35 - 2 = 36$ et non $40$ : on a perdu la structure de l’arbre (et `e4` et `e5` donneraient la même chaîne `"8 - 3 - 1"`). Il suffit d’entourer de parenthèses chaque opération, c’est-à-dire le résultat de chaque nœud qui n’est pas une feuille :

    ```python
    def en_chaine(a):
        if est_feuille(a):
            return str(a.valeur)
        return "(" + en_chaine(a.gauche) + " " + a.valeur + " " + en_chaine(a.droite) + ")"
    ```

    ```python
        assert en_chaine(e2) == "((2 * (1 + 9)) - 4)"
        assert en_chaine(e4) == "((8 - 3) - 1)"
        assert en_chaine(e5) == "(8 - (3 - 1))"
    ```

    Question 3

    *Écrire la fonction récursive `evaluer`.*

    Une feuille vaut son nombre (cas de base). Sinon, on évalue récursivement les deux sous-arbres, puis on applique l’opérateur de la racine, **dans l’ordre** gauche puis droite (important pour la soustraction).

    ```python
    def evaluer(a):
        if est_feuille(a):
            return a.valeur
        valeur_gauche = evaluer(a.gauche)
        valeur_droite = evaluer(a.droite)
        if a.valeur == '+':
            return valeur_gauche + valeur_droite
        elif a.valeur == '-':
            return valeur_gauche - valeur_droite
        else:
            return valeur_gauche * valeur_droite
    ```

    ```python
        assert evaluer(e2) == 16
        assert evaluer(e4) == 4
        assert evaluer(e5) == 6
    ```

    $\blacktriangleright$ Appel professeur. identifier le cas de base et l’appel récursif, justifier la terminaison (chaque appel porte sur un sous-arbre strictement plus petit) et montrer que `e4` et `e5` donnent bien 4 et 6.

    Question 4

    *Écrire la fonction récursive `nb_operateurs`.*

    Une feuille ne contient aucun opérateur ; un nœud opérateur compte pour `1`, plus les opérateurs de ses deux sous-arbres.

    ```python
    def nb_operateurs(a):
        if est_feuille(a):
            return 0
        return 1 + nb_operateurs(a.gauche) + nb_operateurs(a.droite)
    ```

    ```python
        assert nb_operateurs(e2) == 3
        assert nb_operateurs(Noeud('+', Noeud(1), Noeud(2))) == 1
    ```

    $\blacktriangleright$ Appel professeur. faire le lien avec le calcul de la taille d’un arbre vu en cours (même schéma récursif, seul le cas de base change).
