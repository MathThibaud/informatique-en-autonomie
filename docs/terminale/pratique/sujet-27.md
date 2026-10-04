# Sujet 27 — Calculatrice en notation polonaise inverse

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/pratique-27-npi){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-pratique-27-npi.zip){ .md-button }

??? corrige "Corrigé"

    !!! remarque "Remarque"

        On donne une version simple ; d’autres réponses sont possibles. Le fichier complet, `corrige_sujet_27.py`, est en ligne : [`github.com/MathThibaud/nsi-fichiers-eleves/tree/main/corriges/terminale/pratique-27`](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/corriges/terminale/pratique-27).

    Question 1

    *Évaluer à la main `5 1 2 + 4 * + 3 -` en dessinant la pile.*

    (sommet à droite)

    | **Élément** | **Action**                          | **Pile** |
    |:-----------:|:------------------------------------|:---------|
    |     `5`     | empiler                             | `5`      |
    |     `1`     | empiler                             | `5 1`    |
    |     `2`     | empiler                             | `5 1 2`  |
    |     `+`     | dépiler 2 et 1, empiler $1+2$       | `5 3`    |
    |     `4`     | empiler                             | `5 3 4`  |
    |     `*`     | dépiler 4 et 3, empiler $3\times 4$ | `5 12`   |
    |     `+`     | dépiler 12 et 5, empiler $5+12$     | `17`     |
    |     `3`     | empiler                             | `17 3`   |
    |     `-`     | dépiler 3 et 17, empiler $17-3$     | `14`     |

    La valeur est `14` : c’est l’expression $5 + (1+2)\times 4 - 3$.

    $\blacktriangleright$ Appel professeur. dérouler la pile à voix haute, en insistant sur l’ordre des opérandes pour `-`.

    Question 2

    *Écrire `evaluer_npi(expression)` avec une `Pile`.*

    ```python
    def evaluer_npi(expression):
        p = Pile()
        for element in expression.split():
            if element in OPERATEURS:
                droite = p.depiler()     # le dernier empile est l'operande de DROITE
                gauche = p.depiler()
                if element == "+":
                    p.empiler(gauche + droite)
                elif element == "-":
                    p.empiler(gauche - droite)
                else:
                    p.empiler(gauche * droite)
            else:
                p.empiler(int(element))
        return p.depiler()
    ```

    Erreur fréquente : dépiler dans le mauvais ordre, ce qui donne $2-7=-5$ pour `7 2 -` (le test le détecte).

    ```python
        assert evaluer_npi("5 1 2 + 4 * + 3 -") == 14
        assert evaluer_npi("2 3 4 * +") == 14
    ```

    $\blacktriangleright$ Appel professeur. expliquer pourquoi une pile convient (l’opérateur s’applique aux deux derniers résultats obtenus) et l’ordre des deux dépilements.

    Question 3

    *Renvoyer `None` pour une expression mal formée.*

    Deux situations à détecter :

    - à la lecture d’un opérateur, la pile contient **moins de deux** nombres (`"3 +"`, `"+"`) : dépiler provoquerait une erreur ;

    - à la fin, la pile ne contient **pas exactement un** nombre : il reste des nombres inutilisés (`"3 4"`) ou la pile est vide (expression vide `""`).

    ```python
    def evaluer_npi(expression):
        p = Pile()
        for element in expression.split():
            if element in OPERATEURS:
                if p.taille() < 2:       # il manque un operande
                    return None
                droite = p.depiler()
                gauche = p.depiler()
                if element == "+":
                    p.empiler(gauche + droite)
                elif element == "-":
                    p.empiler(gauche - droite)
                else:
                    p.empiler(gauche * droite)
            else:
                p.empiler(int(element))
        if p.taille() != 1:              # expression vide ou operateur manquant
            return None
        return p.depiler()
    ```

    ```python
        assert evaluer_npi("") is None
        assert evaluer_npi("+") is None
        assert evaluer_npi("1 2 + +") is None
    ```

    Question 4

    *Traduire $(2+3)\times(7-4)$ en NPI et vérifier.*

    On écrit l’expression de gauche, puis celle de droite, puis l’opérateur : `2 3 +` puis `7 4 -` puis `*`, soit `2 3 + 7 4 - *`.

    ```console
    >>> evaluer_npi("2 3 + 7 4 - *")
    15
    ```

    On retrouve bien $5\times 3=15$. C’est l’ordre du parcours **suffixe** de l’arbre de l’expression : voilà pourquoi la NPI n’a pas besoin de parenthèses.

    $\blacktriangleright$ Appel professeur. justifier la traduction et, si possible, faire le lien avec le parcours suffixe d’un arbre.

*Durée de l’épreuve : 1 heure.*

!!! encadre "Déroulement de l’épreuve"

    - Cette situation d’évaluation comporte ce document ainsi que des fichiers de codes et de données présents sur l’ordinateur. Le candidat doit **agir en autonomie** et faire preuve d’initiative tout au long de l’épreuve.

    - En cas de difficulté, le candidat peut solliciter l’examinateur. Des moments privilégiés sont indiqués sous la forme d’**appels professeur**. L’examinateur peut intervenir à tout moment s’il le juge utile.

Dans la **notation polonaise inverse** (NPI), utilisée par certaines calculatrices, on écrit un opérateur **après** ses deux opérandes : l’expression $3+4$ s’écrit `3 4 +` et l’expression $(3+4)\times 2$ s’écrit `3 4 + 2 *`. Cette notation n’utilise jamais de parenthèses.

Une expression en NPI s’évalue avec une **pile**, en lisant ses éléments de gauche à droite :

- un nombre est **empilé** ;

- un opérateur **dépile** deux nombres, leur applique l’opération et **empile** le résultat. Le premier nombre dépilé est l’opérande de **droite**, le second celui de **gauche** : `7 2 -` vaut $7-2=5$.

À la fin, la pile contient un seul nombre : la valeur de l’expression.

Dans ce sujet, les expressions sont des chaînes de caractères dont les éléments, séparés par des espaces, sont des **entiers positifs** ou l’un des opérateurs `+`, `-` et `*`. On rappelle que `"3 4 +".split()` renvoie la liste `[’3’, ’4’, ’+’]` et que `int(’3’)` renvoie l’entier `3`. Le fichier `npi.py` fournit la classe `Pile` vue en cours (méthodes `est_vide`, `empiler`, `depiler`, `sommet` et `taille`).

Question 1

Évaluer à la main l’expression `5 1 2 + 4 * + 3 -` en dessinant l’état de la pile après la lecture de chaque élément.

**$\blacktriangleright$ Appel professeur.** Appeler le professeur pour lui présenter votre réponse ou en cas de difficulté.

Question 2

Écrire le corps de la fonction `evaluer_npi(expression)` qui renvoie la valeur d’une expression en NPI, en utilisant un objet de la classe `Pile`. Des tests sont fournis dans la fonction `test_evaluer`, on pourra les compléter.

**$\blacktriangleright$ Appel professeur.** Appeler le professeur pour lui présenter votre réponse ou en cas de difficulté.

Question 3

Une expression peut être mal formée : dans `"3 +"` il manque un opérande, et dans `"3 4"` il manque un opérateur. Modifier la fonction `evaluer_npi` pour qu’elle renvoie `None` lorsque l’expression est mal formée (sans provoquer d’erreur). Tester avec la fonction `test_erreurs`, que l’on complétera avec d’autres cas.

Question 4

Traduire en NPI l’expression $(2+3)\times(7-4)$, puis vérifier le résultat à l’aide de la fonction `evaluer_npi`.

**$\blacktriangleright$ Appel professeur.** Appeler le professeur pour lui présenter votre réponse ou en cas de difficulté.

### Description du dossier

Le dossier fourni au candidat comporte les éléments suivants :

- une version PDF de l’énoncé ;

- un code source de départ `npi.py`.

??? corrige "Corrigé"

    !!! remarque "Remarque"

        On donne une version simple ; d’autres réponses sont possibles. Le fichier complet, `corrige_sujet_27.py`, est en ligne : [`github.com/MathThibaud/nsi-fichiers-eleves/tree/main/corriges/terminale/pratique-27`](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/corriges/terminale/pratique-27).

    Question 1

    *Évaluer à la main `5 1 2 + 4 * + 3 -` en dessinant la pile.*

    (sommet à droite)

    | **Élément** | **Action**                          | **Pile** |
    |:-----------:|:------------------------------------|:---------|
    |     `5`     | empiler                             | `5`      |
    |     `1`     | empiler                             | `5 1`    |
    |     `2`     | empiler                             | `5 1 2`  |
    |     `+`     | dépiler 2 et 1, empiler $1+2$       | `5 3`    |
    |     `4`     | empiler                             | `5 3 4`  |
    |     `*`     | dépiler 4 et 3, empiler $3\times 4$ | `5 12`   |
    |     `+`     | dépiler 12 et 5, empiler $5+12$     | `17`     |
    |     `3`     | empiler                             | `17 3`   |
    |     `-`     | dépiler 3 et 17, empiler $17-3$     | `14`     |

    La valeur est `14` : c’est l’expression $5 + (1+2)\times 4 - 3$.

    $\blacktriangleright$ Appel professeur. dérouler la pile à voix haute, en insistant sur l’ordre des opérandes pour `-`.

    Question 2

    *Écrire `evaluer_npi(expression)` avec une `Pile`.*

    ```python
    def evaluer_npi(expression):
        p = Pile()
        for element in expression.split():
            if element in OPERATEURS:
                droite = p.depiler()     # le dernier empile est l'operande de DROITE
                gauche = p.depiler()
                if element == "+":
                    p.empiler(gauche + droite)
                elif element == "-":
                    p.empiler(gauche - droite)
                else:
                    p.empiler(gauche * droite)
            else:
                p.empiler(int(element))
        return p.depiler()
    ```

    Erreur fréquente : dépiler dans le mauvais ordre, ce qui donne $2-7=-5$ pour `7 2 -` (le test le détecte).

    ```python
        assert evaluer_npi("5 1 2 + 4 * + 3 -") == 14
        assert evaluer_npi("2 3 4 * +") == 14
    ```

    $\blacktriangleright$ Appel professeur. expliquer pourquoi une pile convient (l’opérateur s’applique aux deux derniers résultats obtenus) et l’ordre des deux dépilements.

    Question 3

    *Renvoyer `None` pour une expression mal formée.*

    Deux situations à détecter :

    - à la lecture d’un opérateur, la pile contient **moins de deux** nombres (`"3 +"`, `"+"`) : dépiler provoquerait une erreur ;

    - à la fin, la pile ne contient **pas exactement un** nombre : il reste des nombres inutilisés (`"3 4"`) ou la pile est vide (expression vide `""`).

    ```python
    def evaluer_npi(expression):
        p = Pile()
        for element in expression.split():
            if element in OPERATEURS:
                if p.taille() < 2:       # il manque un operande
                    return None
                droite = p.depiler()
                gauche = p.depiler()
                if element == "+":
                    p.empiler(gauche + droite)
                elif element == "-":
                    p.empiler(gauche - droite)
                else:
                    p.empiler(gauche * droite)
            else:
                p.empiler(int(element))
        if p.taille() != 1:              # expression vide ou operateur manquant
            return None
        return p.depiler()
    ```

    ```python
        assert evaluer_npi("") is None
        assert evaluer_npi("+") is None
        assert evaluer_npi("1 2 + +") is None
    ```

    Question 4

    *Traduire $(2+3)\times(7-4)$ en NPI et vérifier.*

    On écrit l’expression de gauche, puis celle de droite, puis l’opérateur : `2 3 +` puis `7 4 -` puis `*`, soit `2 3 + 7 4 - *`.

    ```console
    >>> evaluer_npi("2 3 + 7 4 - *")
    15
    ```

    On retrouve bien $5\times 3=15$. C’est l’ordre du parcours **suffixe** de l’arbre de l’expression : voilà pourquoi la NPI n’a pas besoin de parenthèses.

    $\blacktriangleright$ Appel professeur. justifier la traduction et, si possible, faire le lien avec le parcours suffixe d’un arbre.
