# Sujet 30 — Messages secrets

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/pratique-30-messages-secrets){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-pratique-30-messages-secrets.zip){ .md-button }

??? corrige "Corrigé"

    !!! remarque "Remarque"

        On donne une version simple ; d’autres réponses sont possibles. Le fichier complet, `corrige_sujet_30.py`, est en ligne : [`github.com/MathThibaud/nsi-fichiers-eleves/tree/main/corriges/terminale/pratique-30`](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/corriges/terminale/pratique-30).

    Question 1

    *Écrire `cesar(message, k)` (les caractères autres que `A`–`Z` restent inchangés).*

    ```python
    def cesar(message, k):
        resultat = ""
        for lettre in message:
            if "A" <= lettre <= "Z":
                rang = ord(lettre) - ord("A")
                nouveau = (rang + k) % 26
                resultat = resultat + chr(nouveau + ord("A"))
            else:
                resultat = resultat + lettre
        return resultat
    ```

    Le `% 26` rend le décalage circulaire (`Z` décalé de $1$ donne `A`). Il fonctionne aussi pour une clé négative : en Python, `-3 % 26` vaut `23`. C’est pourquoi `cesar(c, -k)` déchiffre.

    $\blacktriangleright$ Appel professeur. expliquer le rôle du modulo et pourquoi le même code déchiffre avec `-k`.

    Question 2

    *Compléter `occurrences`, puis retrouver la clé de `message_secret.txt` et afficher le clair.*

    ```python
    def occurrences(texte):
        occ = {}
        for lettre in texte:
            if "A" <= lettre <= "Z":
                if lettre in occ:
                    occ[lettre] = occ[lettre] + 1
                else:
                    occ[lettre] = 1
        return occ
    ```

    ```console
    >>> secret = lire_fichier("message_secret.txt")
    >>> lettre_plus_frequente(secret)
    'L'
    ```

    La lettre la plus fréquente, `L` (rang $11$), est très probablement un `E` (rang $4$) chiffré : la clé vaut $11 - 4 = 7$. On déchiffre avec `cesar(secret, -7)` :

    ```console
    >>> cesar(secret, -7)
    'EN MIL NEUF CENT QUARANTE, DANS LE PARC DE BLETCHLEY, UNE EQUIPE ...'
    ```

    Le texte parle d’Alan Turing et des attaques par **force brute**. On pouvait aussi essayer les $26$ clés et repérer à l’œil le seul résultat lisible. La clé se calcule aussi en Python : `(ord(lettre) - ord("E")) % 26`.

    $\blacktriangleright$ Appel professeur. expliquer pourquoi l’analyse des fréquences casse César : une même lettre est **toujours** chiffrée de la même façon, donc les fréquences sont conservées.

    Question 3

    *Trouver et corriger l’erreur de `vigenere`.*

    ```console
    >>> vigenere("NSIROCKS", "CLE")
    'CQZGMTZQ'
    ```

    L’erreur est à la ligne `decalage = ord(cle[i % len(cle)])` : elle prend le **code** de la lettre de la clé (`ord("C")` vaut $67$) au lieu de son **rang** ($2$). Il faut retirer `ord("A")`, comme pour le message :

    ```python
            decalage = ord(cle[i % len(cle)]) - ord("A")
    ```

    $\blacktriangleright$ Appel professeur. montrer comment l’erreur a été localisée (calcul à la main de la première lettre, affichage de `decalage`).

    Question 4

    *Écrire `dechiffre_vigenere(message, cle)`, puis expliquer pourquoi la méthode de la question 2 ne suffit plus.*

    On refait le même parcours en **retranchant** le décalage :

    ```python
    def dechiffre_vigenere(message, cle):
        resultat = ""
        for i in range(len(message)):
            decalage = ord(cle[i % len(cle)]) - ord("A")
            rang = ord(message[i]) - ord("A")
            nouveau = (rang - decalage) % 26
            resultat = resultat + chr(nouveau + ord("A"))
        return resultat
    ```

    ```python
        assert dechiffre_vigenere("", "CLE") == ""
        assert dechiffre_vigenere(vigenere("ZZZ", "B"), "B") == "ZZZ"
    ```

    Avec Vigenère, une même lettre du clair est chiffrée de façons **différentes** selon sa position (`ANANAS` chiffré avec `CLE` donne `CYEPLW` : les trois `A` deviennent `C`, `E` et `L`). Les `E` du clair se répartissent sur plusieurs lettres chiffrées : la lettre la plus fréquente du chiffré ne correspond plus à un seul `E`, et un seul décalage ne suffit pas à tout déchiffrer. Si l’on connaît la **longueur** $L$ de la clé, on peut en revanche refaire l’analyse des fréquences sur les lettres d’indices $0, L, 2L, \dots$ (toutes décalées pareil), puis sur $1, L+1, \dots$ : c’est l’idée de Babbage et Kasiski.

    $\blacktriangleright$ Appel professeur. expliquer la différence avec César et, si possible, l’idée de l’attaque par longueur de clé.

*Durée de l’épreuve : 1 heure.*

!!! encadre "Déroulement de l’épreuve"

    - Cette situation d’évaluation comporte ce document ainsi que des fichiers de codes et de données présents sur l’ordinateur. Le candidat doit **agir en autonomie** et faire preuve d’initiative tout au long de l’épreuve.

    - En cas de difficulté, le candidat peut solliciter l’examinateur. Des moments privilégiés sont indiqués sous la forme d’**appels professeur**. L’examinateur peut intervenir à tout moment s’il le juge utile.

On numérote les lettres majuscules de `A` à `Z` par leur **rang** : `A` a le rang $0$, `B` le rang $1$, …, `Z` le rang $25$. En Python, le rang de la lettre `lettre` est `ord(lettre) - ord("A")`, et la lettre de rang `r` est `chr(r + ord("A"))`. Tous les textes de ce sujet sont en majuscules, sans accents.

Dans le **chiffre de César** de clé `k`, chaque lettre de rang `r` est remplacée par la lettre de rang `(r + k) % 26` : le décalage est circulaire (avec `k = 3`, `Z` devient `C`). Pour déchiffrer, on décale de `-k`.

Question 1

Écrire le corps de la fonction `cesar(message, k)` du fichier `crypto.py`. Les caractères qui ne sont pas des lettres de `A` à `Z` (espaces, ponctuation) restent inchangés. Par exemple, `cesar("BONJOUR", 3)` renvoie `"ERQMRXU"`. Des tests sont fournis dans la fonction `test_cesar`.

**$\blacktriangleright$ Appel professeur.** Appeler le professeur pour lui présenter votre réponse ou en cas de difficulté.

Question 2

Le fichier `message_secret.txt` contient un texte français chiffré par César, avec une clé inconnue. En français, la lettre la plus fréquente est presque toujours le `E`.

1.  Écrire le corps de la fonction `occurrences(texte)`, qui renvoie un dictionnaire associant à chaque lettre présente dans `texte` son nombre d’apparitions (les autres caractères sont ignorés). Tester avec `test_occurrences`.

2.  À l’aide de la fonction `lire_fichier` et de la fonction `lettre_plus_frequente` fournies, déterminer la clé utilisée, puis afficher le message en clair.

**$\blacktriangleright$ Appel professeur.** Appeler le professeur pour lui présenter votre réponse ou en cas de difficulté.

Question 3

Dans le **chiffre de Vigenère**, la clé est un mot, répété autant que nécessaire : la lettre d’indice `i` du message est décalée du **rang** de la lettre d’indice `i % len(cle)` de la clé. Par exemple, avec la clé `"CLE"`, la première lettre est décalée de $2$, la deuxième de $11$, la troisième de $4$, la quatrième à nouveau de $2$, etc. Ainsi, `NSIROCKS` chiffré avec la clé `CLE` donne `PDMTZGMD`.

La fonction `vigenere(message, cle)` fournie ne donne pas ce résultat : le test `test_vigenere` échoue. Trouver l’erreur et corriger la fonction.

**$\blacktriangleright$ Appel professeur.** Appeler le professeur pour lui présenter votre réponse ou en cas de difficulté.

Question 4

Écrire le corps de la fonction `dechiffre_vigenere(message, cle)`, qui déchiffre un message chiffré par Vigenère avec la clé `cle`. Tester avec `test_dechiffre_vigenere`.

Expliquer ensuite pourquoi la méthode de la question 2 ne permet pas, telle quelle, de retrouver la clé d’un message chiffré par Vigenère.

### Description du dossier

Le dossier fourni au candidat comporte les éléments suivants :

- une version PDF de l’énoncé ;

- un code source de départ `crypto.py` ;

- un fichier de données `message_secret.txt`.

??? corrige "Corrigé"

    !!! remarque "Remarque"

        On donne une version simple ; d’autres réponses sont possibles. Le fichier complet, `corrige_sujet_30.py`, est en ligne : [`github.com/MathThibaud/nsi-fichiers-eleves/tree/main/corriges/terminale/pratique-30`](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/corriges/terminale/pratique-30).

    Question 1

    *Écrire `cesar(message, k)` (les caractères autres que `A`–`Z` restent inchangés).*

    ```python
    def cesar(message, k):
        resultat = ""
        for lettre in message:
            if "A" <= lettre <= "Z":
                rang = ord(lettre) - ord("A")
                nouveau = (rang + k) % 26
                resultat = resultat + chr(nouveau + ord("A"))
            else:
                resultat = resultat + lettre
        return resultat
    ```

    Le `% 26` rend le décalage circulaire (`Z` décalé de $1$ donne `A`). Il fonctionne aussi pour une clé négative : en Python, `-3 % 26` vaut `23`. C’est pourquoi `cesar(c, -k)` déchiffre.

    $\blacktriangleright$ Appel professeur. expliquer le rôle du modulo et pourquoi le même code déchiffre avec `-k`.

    Question 2

    *Compléter `occurrences`, puis retrouver la clé de `message_secret.txt` et afficher le clair.*

    ```python
    def occurrences(texte):
        occ = {}
        for lettre in texte:
            if "A" <= lettre <= "Z":
                if lettre in occ:
                    occ[lettre] = occ[lettre] + 1
                else:
                    occ[lettre] = 1
        return occ
    ```

    ```console
    >>> secret = lire_fichier("message_secret.txt")
    >>> lettre_plus_frequente(secret)
    'L'
    ```

    La lettre la plus fréquente, `L` (rang $11$), est très probablement un `E` (rang $4$) chiffré : la clé vaut $11 - 4 = 7$. On déchiffre avec `cesar(secret, -7)` :

    ```console
    >>> cesar(secret, -7)
    'EN MIL NEUF CENT QUARANTE, DANS LE PARC DE BLETCHLEY, UNE EQUIPE ...'
    ```

    Le texte parle d’Alan Turing et des attaques par **force brute**. On pouvait aussi essayer les $26$ clés et repérer à l’œil le seul résultat lisible. La clé se calcule aussi en Python : `(ord(lettre) - ord("E")) % 26`.

    $\blacktriangleright$ Appel professeur. expliquer pourquoi l’analyse des fréquences casse César : une même lettre est **toujours** chiffrée de la même façon, donc les fréquences sont conservées.

    Question 3

    *Trouver et corriger l’erreur de `vigenere`.*

    ```console
    >>> vigenere("NSIROCKS", "CLE")
    'CQZGMTZQ'
    ```

    L’erreur est à la ligne `decalage = ord(cle[i % len(cle)])` : elle prend le **code** de la lettre de la clé (`ord("C")` vaut $67$) au lieu de son **rang** ($2$). Il faut retirer `ord("A")`, comme pour le message :

    ```python
            decalage = ord(cle[i % len(cle)]) - ord("A")
    ```

    $\blacktriangleright$ Appel professeur. montrer comment l’erreur a été localisée (calcul à la main de la première lettre, affichage de `decalage`).

    Question 4

    *Écrire `dechiffre_vigenere(message, cle)`, puis expliquer pourquoi la méthode de la question 2 ne suffit plus.*

    On refait le même parcours en **retranchant** le décalage :

    ```python
    def dechiffre_vigenere(message, cle):
        resultat = ""
        for i in range(len(message)):
            decalage = ord(cle[i % len(cle)]) - ord("A")
            rang = ord(message[i]) - ord("A")
            nouveau = (rang - decalage) % 26
            resultat = resultat + chr(nouveau + ord("A"))
        return resultat
    ```

    ```python
        assert dechiffre_vigenere("", "CLE") == ""
        assert dechiffre_vigenere(vigenere("ZZZ", "B"), "B") == "ZZZ"
    ```

    Avec Vigenère, une même lettre du clair est chiffrée de façons **différentes** selon sa position (`ANANAS` chiffré avec `CLE` donne `CYEPLW` : les trois `A` deviennent `C`, `E` et `L`). Les `E` du clair se répartissent sur plusieurs lettres chiffrées : la lettre la plus fréquente du chiffré ne correspond plus à un seul `E`, et un seul décalage ne suffit pas à tout déchiffrer. Si l’on connaît la **longueur** $L$ de la clé, on peut en revanche refaire l’analyse des fréquences sur les lettres d’indices $0, L, 2L, \dots$ (toutes décalées pareil), puis sur $1, L+1, \dots$ : c’est l’idée de Babbage et Kasiski.

    $\blacktriangleright$ Appel professeur. expliquer la différence avec César et, si possible, l’idée de l’attaque par longueur de clé.
