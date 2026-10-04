# TP et projets

<p class="sous-titre">Cryptographie</p>

## <span class="etiquette">TP</span> Chiffrer, casser, signer

*de César à RSA, en Python*

<p class="infos-activite">Durée : 3 h (deux séances) · Sur machine, par deux</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/12-tp-crypto){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-12-tp-crypto.zip){ .md-button }

!!! consignes "Consignes"

    - Fichier à télécharger (lien ci-dessus) : `tp_crypto_depart.py`. Il contient un texte français `TEXTE`, un tableau `FREQ_FR` des fréquences des lettres en français, la fonction `normaliser` (majuscules, sans accents), des squelettes de fonctions et des tests. Le lancer affiche l’état des tests.

    - Les messages sont en **majuscules sans accents** ; seules les lettres `A` à `Z` sont chiffrées, les autres caractères (espaces, ponctuation) sont recopiés tels quels.

    - Niveau : ★ échauffement, ★★ classique (niveau bac), ★★★ défi ; les *coups de pouce* et les *corrigés* se déplient sous chaque exercice. Le symbole <span class="run" title="À programmer et tester sur machine">▶</span>  signale ce qui est à programmer et tester.

    - Usage de l’IA, indiqué sur chaque exercice : <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> aucune ; <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> en appui (déboguer, reformuler, vérifier ; la réponse finale est écrite et comprise par vous) ; <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> l’exercice s’appuie sur une réponse d’IA. Voir la [charte d’usage de l’IA](../charte.md).

!!! encadre "But du TP"

    Programmer les chiffrements du cours **et les attaques** qui les cassent : César par force brute puis par analyse de fréquences, Vigenère colonne par colonne, le masque jetable réutilisé ; puis construire un **RSA complet** — génération de clés avec l’algorithme d’Euclide étendu, chiffrement d’un message, signature — et mesurer pourquoi sa sécurité tient : **factoriser** $n$ devient vite hors de portée. *Produit final* : une petite bibliothèque de chiffrement et d’attaques, testée, et un tableau de mesures.

## Partie A — César : chiffrer, puis casser sans la clé

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 1</span> — César, version complète <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-cryptographie-tp-1-1 }

1.  <span class="run" title="À programmer et tester sur machine">▶</span>  Compléter `decaler(lettre, k)` : une majuscule de rang $x$ devient la lettre de rang `(x + k) % 26` ; tout autre caractère est renvoyé inchangé. Puis compléter `cesar(texte, k)`. Exemple : `cesar("BONJOUR !", 3)` vaut `"ERQMRXU !"`.

2.  <span class="run" title="À programmer et tester sur machine">▶</span>  Chiffrer `clair = normaliser(TEXTE)` avec la clé $11$, afficher le début du chiffré, puis le déchiffrer.

??? corrige "Corrigé"

    - César et Vigenère conservent les **fréquences** des lettres (globalement, ou colonne par colonne) ; le masque réutilisé laisse fuir $m_1 \oplus m_2$. Un bon chiffrement ne doit rien laisser paraître de la structure du message.

    - RSA : choisir $p$, $q$ premiers (`premier_aleatoire`) ; $n = pq$, $\varphi = (p-1)(q-1)$ ; $e$ premier avec $\varphi$ (`pgcd`) ; $d$ inverse de $e$ modulo $\varphi$ (`euclide_etendu`, `inverse_modulaire`).

    - La sécurité repose sur la difficulté de **factoriser** $n$ : chaque paire de chiffres en plus multiplie le temps par $10$ (partie E).

    - Chiffrer : clé **publique** du destinataire (confidentialité). Signer : clé **privée** de l’expéditeur (authenticité, intégrité).

    ```python
    def decaler(lettre, k):
        if "A" <= lettre <= "Z":
            return chr((ord(lettre) - 65 + k) % 26 + 65)
        return lettre

    def cesar(texte, k):
        resultat = ""
        for c in texte:
            resultat = resultat + decaler(c, k)
        return resultat

    clair = normaliser(TEXTE)
    chiffre = cesar(clair, 11)
    print(chiffre[:50])          # OPAFTD W'LYETBFTEP, WPD SZXXPD NSPCNSPYE L NLNSPC
    print(cesar(chiffre, -11) == clair)                    # True
    ```

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 2</span> — La force brute <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-cryptographie-tp-1-2 }

On a intercepté : `KXGWXS-OHNL WXOTGM EX FNLXX HVXTGHZKTIABJNX T FBWB`.

1.  <span class="run" title="À programmer et tester sur machine">▶</span>  Afficher les $26$ déchiffrements possibles (un par ligne, précédé de la clé). Lequel est le bon ? Quelle est la clé ?

2.  Un programme doit faire ce tri tout seul. Proposer une idée pour reconnaître automatiquement « du français ».

??? corrige "Corrigé"

    **1.** `for k in range(26): print(k, cesar(message, -k))`. Seule la clé **19** donne du français : `RENDEZ-VOUS DEVANT LE MUSEE OCEANOGRAPHIQUE A MIDI`.

    **2.** Compter les mots d’un dictionnaire présents dans chaque candidat, ou comparer les fréquences de ses lettres à celles du français (c’est l’idée de l’exercice suivant).

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 3</span> — L’analyse de fréquences, automatisée <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-cryptographie-tp-1-3 }

1.  <span class="run" title="À programmer et tester sur machine">▶</span>  Compléter `frequences(texte)` (dictionnaire lettre $\to$ nombre d’apparitions, pour les lettres `A` à `Z` seulement) et `plus_frequente(texte)`. Quelles sont les trois lettres les plus fréquentes de `clair` ?

2.  <span class="run" title="À programmer et tester sur machine">▶</span>  Compléter `casser_cesar(chiffre)`, qui suppose que la lettre la plus fréquente du chiffré est un `E` et en déduit la clé. Vérifier qu’elle retrouve la clé $11$ sur le long texte.

3.  <span class="run" title="À programmer et tester sur machine">▶</span>  Essayer `casser_cesar` sur `cesar("ATTAQUE A L AUBE", 7)`. Quelle clé trouve-t-on ? Pourquoi l’hypothèse « la plus fréquente est un `E` » échoue-t-elle ici ?

4.  <span class="run" title="À programmer et tester sur machine">▶</span>  Méthode plus robuste : compléter `score(texte)`, la somme des valeurs `FREQ_FR[c]` pour toutes les lettres `c` du texte (un texte français contient beaucoup de lettres fréquentes, donc a un score élevé), puis `casser_cesar_score(chiffre)` qui renvoie la clé $k$ pour laquelle `cesar(chiffre, -k)` a le **meilleur score**. Tester sur le message court, sur le message intercepté, et sur le long texte.

    ??? pouce "Coup de pouce"

        Même structure qu’une recherche de maximum : une boucle `for k in range(26)`, deux variables `meilleure_cle` et `meilleur_score`.

??? corrige "Corrigé"

    ```python
    def frequences(texte):
        compte = {}
        for c in texte:
            if "A" <= c <= "Z":
                if c in compte:
                    compte[c] += 1
                else:
                    compte[c] = 1                 # premiere apparition
        return compte

    def plus_frequente(texte):
        compte = frequences(texte)
        meilleure = None
        for lettre in compte:
            if meilleure is None or compte[lettre] > compte[meilleure]:
                meilleure = lettre
        return meilleure

    def casser_cesar(chiffre):
        return (ord(plus_frequente(chiffre)) - ord("E")) % 26

    def score(texte):
        s = 0
        for c in texte:
            if "A" <= c <= "Z":
                s += FREQ_FR[c]
        return s

    def casser_cesar_score(chiffre):
        meilleure_cle = 0
        meilleur_score = -1
        for k in range(26):
            sc = score(cesar(chiffre, -k))
            if sc > meilleur_score:
                meilleur_score = sc
                meilleure_cle = k
        return meilleure_cle
    ```

    **1.** Dans `clair` : `E` ($297$ fois), `S` ($150$), `A` ($108$).

    **2.** `casser_cesar(cesar(clair, 11))` renvoie bien `11` (sur le message intercepté : `19`).

    **3.** Le chiffré est `HAAHXBL H S HBIL` ; sa lettre la plus fréquente est `H` (le `A` du clair) : la fonction renvoie $3$ au lieu de $7$. Sur un message de $13$ lettres, les fréquences n’ont rien de statistique : ici, aucun `E` n’est la lettre la plus fréquente.

    **4.** `casser_cesar_score` trouve $7$ sur le message court, $19$ sur le message intercepté et $11$ sur le long texte : elle utilise *toutes* les lettres et pas seulement la plus fréquente.

## Partie B — Vigenère, et comment Babbage l’a cassé

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 4</span> — Chiffrer avec une clé-mot <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-cryptographie-tp-1-4 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Compléter `vigenere(texte, cle, sens=1)` : la $i$<sup>e</sup> **lettre** du texte est décalée selon la lettre `cle[i % len(cle)]` (`A` $\to 0$, `B` $\to 1$…) ; avec `sens = -1`, on décale en arrière (déchiffrement). Les caractères qui ne sont pas des lettres sont recopiés et **ne font pas avancer** la clé. Vérifier l’exemple du cours : `vigenere("NSI ROCKS", "CLE")` vaut `"PDM TZGMD"`.

??? pouce "Coup de pouce"

    Garder un compteur `i` des lettres déjà chiffrées, distinct de la position dans le texte ; réutiliser `decaler` avec le décalage `sens * k`.

??? corrige "Corrigé"

    ```python
    def vigenere(texte, cle, sens=1):
        resultat = ""
        i = 0                                  # nombre de lettres deja chiffrees
        for c in texte:
            if "A" <= c <= "Z":
                k = ord(cle[i % len(cle)]) - 65
                resultat = resultat + decaler(c, sens * k)
                i += 1
            else:
                resultat = resultat + c
        return resultat
    ```

    `vigenere("NSI ROCKS", "CLE")` vaut `"PDM TZGMD"`, et `vigenere("PDM TZGMD", "CLE", -1)` redonne `"NSI ROCKS"`.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 5</span> — Casser Vigenère quand on connaît la longueur de la clé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-cryptographie-tp-1-5 }

On a chiffré `clair` avec une clé de $6$ lettres : `chiffre = vigenere(clair, "MONACO")`. Faisons comme si l’on ignorait la clé.

1.  Les lettres de rangs $0, 6, 12, \dots$ du texte sont toutes décalées avec la *même* lettre de la clé. Par quel chiffrement, déjà cassé, sont-elles donc chiffrées ?

2.  <span class="run" title="À programmer et tester sur machine">▶</span>  Compléter `colonnes(chiffre, L)`, qui renvoie la liste des $L$ chaînes formées des lettres de rangs $0, L, 2L\dots$, puis $1, L+1, \dots$, etc. (les caractères qui ne sont pas des lettres sont ignorés). Exemple : `colonnes("AB CDE", 2)` vaut `["ACE", "BD"]`.

    ??? pouce "Coup de pouce"

        Partir d’une liste de `L` chaînes vides. Parcourir le chiffré en comptant les lettres avec un compteur `i` (comme dans `vigenere`) : la lettre de rang `i` s’ajoute à la chaîne d’indice `i % L`.

3.  <span class="run" title="À programmer et tester sur machine">▶</span>  En déduire `casser_vigenere(chiffre, L)`, qui casse chaque colonne avec `casser_cesar_score` et renvoie la clé. Retrouve-t-on `MONACO` ? Déchiffrer.

??? corrige "Corrigé"

    **1.** Elles sont toutes décalées du même nombre de rangs : c’est un **chiffre de César**, que l’on sait casser.

    **2. et 3.**

    ```python
    def colonnes(chiffre, L):
        cols = ["" for j in range(L)]           # L chaines vides
        i = 0                                  # rang de la lettre dans le chiffre
        for c in chiffre:
            if "A" <= c <= "Z":
                cols[i % L] = cols[i % L] + c
                i += 1
        return cols

    def casser_vigenere(chiffre, L):
        cle = ""
        for col in colonnes(chiffre, L):
            cle = cle + chr(casser_cesar_score(col) + 65)
        return cle
    ```

    `casser_vigenere(vigenere(clair, "MONACO"), 6)` renvoie `"MONACO"`, et le déchiffrement redonne le texte clair. Chaque colonne compte environ $250$ lettres : assez pour que les fréquences parlent.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 6</span> — Défi : trouver la longueur de la clé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-cryptographie-tp-1-6 }

<span class="horsprog">au-delà du programme</span> L’**indice de coïncidence** d’un texte est la probabilité que deux lettres tirées au hasard soient identiques : si $n_A, n_B, \dots$ sont les nombres d’apparitions des lettres et $N$ le nombre total de lettres, $$IC = \frac{n_A(n_A-1) + n_B(n_B-1) + \dots + n_Z(n_Z-1)}{N(N-1)}.$$

1.  <span class="run" title="À programmer et tester sur machine">▶</span>  Écrire `indice_coincidence(texte)`. Calculer l’indice de `clair`, puis d’un texte de $2\,000$ lettres tirées au hasard. Qu’est-ce qui les distingue ?

2.  <span class="run" title="À programmer et tester sur machine">▶</span>  Pour $L$ de $1$ à $8$, calculer la **moyenne** des indices des colonnes de `chiffre`. Pour quelles valeurs de $L$ retrouve-t-on l’indice d’un texte français ? Pourquoi ?

3.  <span class="run" title="À programmer et tester sur machine">▶</span>  Écrire `longueur_cle(chiffre)`, qui renvoie la plus petite longueur $L$ dont la moyenne dépasse $0{,}065$, puis casser sans aucune indication `vigenere(clair, "SECRETS")`.

??? corrige "Corrigé"

    ```python
    def indice_coincidence(texte):
        compte = frequences(texte)
        n = 0
        s = 0
        for lettre in compte:
            x = compte[lettre]
            n += x
            s += x * (x - 1)
        return s / (n * (n - 1))

    def longueur_cle(chiffre, Lmax=10, seuil=0.065):
        for L in range(1, Lmax + 1):
            total = 0
            for col in colonnes(chiffre, L):
                total += indice_coincidence(col)
            if total / L > seuil:
                return L
        return None
    ```

    **1.** $IC(\texttt{clair}) \approx 0{,}083$ ; pour $2\,000$ lettres au hasard, $IC \approx 0{,}038$ à $0{,}039$ selon le tirage (proche de $1/26$). Le français répète beaucoup certaines lettres (`E`, `S`, `A`…), le hasard non.

    **2.** Moyennes pour la clé `MONACO`, $L = 1$ à $8$ : $0{,}052$ ; $0{,}062$ ; $0{,}063$ ; $0{,}062$ ; $0{,}051$ ; **0,083** ; $0{,}052$ ; $0{,}063$. Seul $L = 6$ (et ses multiples) redonne l’indice du français : chaque colonne est alors un simple César, qui conserve l’indice ; pour un autre $L$, une colonne mélange plusieurs décalages et l’indice baisse.

    **3.** Pour `vigenere(clair, "SECRETS")`, `longueur_cle` renvoie $7$ et `casser_vigenere(…, 7)` renvoie `"SECRETS"` : Vigenère cassé sans aucune indication.

## Partie C — Le masque jetable, et l’erreur fatale

En Python, le type `bytes` représente une suite d’octets : `b"RDV"` est la suite `82, 68, 86`, et `bytes([3, 3])` la suite `3, 3`. On accède à l’octet `i` par `m[i]`, qui est un entier.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Un masque, deux messages <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-cryptographie-tp-1-7 }

1.  <span class="run" title="À programmer et tester sur machine">▶</span>  Compléter `xor_octets(a, b)`, qui renvoie la suite des `a[i] ^ b[i]` (construire la liste de ces entiers, puis la convertir avec `bytes(liste)`).

2.  <span class="run" title="À programmer et tester sur machine">▶</span>  Créer un masque aléatoire de la longueur du message ($22$ octets) :  
    `import secrets` puis `masque = secrets.token_bytes(22)`. Chiffrer `m1 = b"RDV A 18H SOUS LE PONT"`, afficher le chiffré (`c1.hex()` l’affiche en hexadécimal) et le déchiffrer. Pourquoi utiliser le module `secrets` plutôt que `random` pour fabriquer une clé ?

3.  <span class="run" title="À programmer et tester sur machine">▶</span>  L’expéditeur, paresseux, **réutilise** le même masque pour `m2 = b"LE CODE EST 4071 MERCI"`. Ève intercepte `c1` et `c2`. Calculer `xor_octets(c1, c2)` et le comparer à `xor_octets(m1, m2)`. Justifier l’égalité avec la propriété $(m \oplus k) \oplus k = m$.

4.  <span class="run" title="À programmer et tester sur machine">▶</span>  Ève devine le premier message (un rendez-vous, elle a vu la scène). Montrer qu’elle obtient alors le second **sans connaître le masque**. Conclure sur la règle « jetable ».

??? corrige "Corrigé"

    ```python
    import secrets

    def xor_octets(a, b):
        resultat = [a[i] ^ b[i] for i in range(len(a))]
        return bytes(resultat)

    m1 = b"RDV A 18H SOUS LE PONT"
    m2 = b"LE CODE EST 4071 MERCI"
    masque = secrets.token_bytes(22)
    c1 = xor_octets(m1, masque)
    c2 = xor_octets(m2, masque)             # ERREUR : masque reutilise
    print(xor_octets(c1, masque))            # b'RDV A 18H SOUS LE PONT'
    print(xor_octets(c1, c2) == xor_octets(m1, m2))   # True
    print(xor_octets(xor_octets(c1, c2), m1))         # b'LE CODE EST 4071 MERCI'
    ```

    **2.** `random` produit une suite **prévisible** (elle est entièrement déterminée par sa graine) : elle convient aux simulations, pas aux secrets. `secrets` utilise l’aléa du système d’exploitation, imprévisible.

    **3.** $c_1 \oplus c_2 = (m_1 \oplus k) \oplus (m_2 \oplus k) = m_1 \oplus m_2 \oplus (k \oplus k) = m_1 \oplus m_2$ : le masque **disparaît**.

    **4.** $(c_1 \oplus c_2) \oplus m_1 = m_2$ : connaissant (ou devinant) un message, Ève lit l’autre sans le masque. Le masque jetable n’est inviolable que s’il ne sert **qu’une seule fois**.

## Partie D — Un RSA complet

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 8</span> — Six jeux de clés <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-cryptographie-tp-1-8 }

Voici six jeux de clés RSA. Pour chacun : $n = pq$, $\varphi = (p-1)(q-1)$, $d$ est l’inverse de $e$ modulo $\varphi$, et $C = M^{e} \bmod n$.

| $p$  | $q$  | $n=pq$ | $\varphi$ | $e$ | $d$  | $M$  | $C=M^{e}\bmod n$ |
|:----:|:----:|:------:|:---------:|:---:|:----:|:----:|:----------------:|
| $3$  | $11$ |  $33$  |   $20$    | $3$ | $7$  | $4$  |       $31$       |
| $5$  | $11$ |        |           | $3$ |      | $7$  |                  |
| $5$  | $7$  |  $35$  |   $24$    | $5$ | $5$  | $10$ |       $5$        |
| $7$  | $11$ |  $77$  |   $60$    | $7$ | $43$ | $2$  |       $51$       |
| $11$ | $13$ |        |           | $7$ |      | $9$  |                  |
| $13$ | $17$ | $221$  |   $192$   | $5$ | $77$ | $8$  |       $60$       |

1.  À la main, sur le cahier, compléter la deuxième ligne ($p=5$, $q=11$) : trouver $d$ en testant $d = 1, 2, 3\dots$, puis calculer $C$. Vérifier que $C^{d} \bmod n$ redonne $M$ (calcul fait par Python : `pow(C, d, n)`).

2.  <span class="run" title="À programmer et tester sur machine">▶</span>  Écrire une boucle qui, pour chaque ligne, calcule $n$, $\varphi$, $d$ (avec `pow(e, -1, phi)`) et $C$, et vérifie par un `assert` que le déchiffrement redonne $M$. En déduire la cinquième ligne.

3.  Dans la troisième ligne, $d = e$ : clé publique et clé privée ont le même exposant. Pourquoi ce jeu de clés serait-il catastrophique en vrai ?

??? corrige "Corrigé"

    **1.** $n = 55$, $\varphi = 4 \times 10 = 40$ ; $3d \equiv 1\ [40]$ : $3 \times 27 = 81 = 2 \times 40 + 1$, donc $d = 27$. $C = 7^{3} \bmod 55 = 343 \bmod 55 = 13$, et `pow(13, 27, 55)` vaut $7$.

    **2.**

    ```python
    jeux = [(3, 11, 3, 4), (5, 11, 3, 7), (5, 7, 5, 10),
            (7, 11, 7, 2), (11, 13, 7, 9), (13, 17, 5, 8)]
    for p, q, e, M in jeux:
        n = p * q
        phi = (p - 1) * (q - 1)
        d = pow(e, -1, phi)
        C = pow(M, e, n)
        assert pow(C, d, n) == M
        print(p, q, n, phi, e, d, M, C)
    ```

    Cinquième ligne : $n = 143$, $\varphi = 120$, $d = 103$, $C = 48$. Les six vérifications passent.

    **3.** Si $d = e$, la clé privée est **connue de tous** (elle est égale à la clé publique) : n’importe qui déchiffre. Cela arrive pour de tout petits $\varphi$ ; il faut le refuser lors de la génération.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 9</span> — Calculer $d$ soi-même : l’algorithme d’Euclide étendu <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-cryptographie-tp-1-9 }

<span class="horsprog">au-delà du programme</span> Tester $d = 1, 2, 3\dots$ est impossible quand $\varphi$ a des centaines de chiffres. On utilise l’**algorithme d’Euclide étendu**, qui calcule $g = \mathrm{pgcd}(a, b)$ **et** deux entiers $u$, $v$ tels que $a u + b v = g$. Il est récursif :

- si $b = 0$ : renvoyer $(a, 1, 0)$ (car $a \times 1 + 0 \times 0 = a$) ;

- sinon : calculer $(g, u', v')$ pour le couple $(b,\ a \,\%\, b)$, puis renvoyer $(g,\ v',\ u' - (a\,//\,b) \times v')$.

1.  <span class="run" title="À programmer et tester sur machine">▶</span>  Compléter `pgcd(a, b)` (version itérative : tant que $b \neq 0$, remplacer $(a, b)$ par $(b, a \,\%\, b)$) et `euclide_etendu(a, b)`. Vérifier : `euclide_etendu(240, 46)` vaut `(2, -9, 47)`, et $240 \times (-9) + 46 \times 47 = 2$.

2.  Si $\mathrm{pgcd}(e, \varphi) = 1$, on obtient $e u + \varphi v = 1$. Expliquer pourquoi $u \,\%\, \varphi$ est alors l’inverse de $e$ modulo $\varphi$.

3.  <span class="run" title="À programmer et tester sur machine">▶</span>  En déduire `inverse_modulaire(e, phi)` (qui renvoie `None` si $\mathrm{pgcd}(e, \varphi) \neq 1$), et la comparer à `pow(e, -1, phi)` sur les six jeux de clés.

??? corrige "Corrigé"

    ```python
    def pgcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def euclide_etendu(a, b):
        if b == 0:                             # condition d'arret
            return (a, 1, 0)
        g, u, v = euclide_etendu(b, a % b)
        return (g, v, u - (a // b) * v)

    def inverse_modulaire(e, phi):
        g, u, v = euclide_etendu(e, phi)
        if g != 1:
            return None
        return u % phi
    ```

    **1.** `euclide_etendu(240, 46)` vaut `(2, -9, 47)` et $240 \times (-9) + 46 \times 47 = -2160 + 2162 = 2$.

    **2.** $e u = 1 - \varphi v$ : le reste de la division de $e u$ par $\varphi$ vaut $1$, c’est-à-dire $e u \equiv 1\ [\varphi]$. Comme $u$ peut être négatif (ici `euclide_etendu(3, 40)` vaut `(1, -13, 1)`), on prend `u % phi`, compris entre $0$ et $\varphi - 1$ : `-13 % 40` vaut $27$, et l’on retrouve bien $d = 27$ pour $p = 5$, $q = 11$.

    **3.** `inverse_modulaire` et `pow(e, -1, phi)` coïncident sur les six jeux ; `inverse_modulaire(4, 20)` renvoie `None` ($\mathrm{pgcd} = 4$).

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 10</span> — Fabriquer ses propres clés <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-cryptographie-tp-1-10 }

1.  <span class="run" title="À programmer et tester sur machine">▶</span>  Compléter `est_premier(n)` (on teste les diviseurs $d$ tant que $d \times d \leqslant n$). Écrire `premier_aleatoire(mini, maxi)`, qui tire des entiers au hasard entre `mini` et `maxi` jusqu’à en trouver un premier.

2.  <span class="run" title="À programmer et tester sur machine">▶</span>  Écrire `generer_cles()` : tirer deux premiers distincts $p$, $q$ entre $1\,000$ et $9\,999$, prendre $e = 65\,537$ (l’exposant utilisé en pratique), recommencer si $\mathrm{pgcd}(e, \varphi) \neq 1$, et renvoyer `((e, n), (d, n))`. Afficher vos clés.

3.  Pourquoi faut-il que $p \neq q$ ? Pourquoi `pgcd(e, phi)` doit-il valoir $1$ ?

??? corrige "Corrigé"

    ```python
    def est_premier(n):
        if n < 2:
            return False
        d = 2
        while d * d <= n:
            if n % d == 0:
                return False
            d += 1
        return True

    def premier_aleatoire(mini, maxi):
        p = random.randint(mini, maxi)
        while not est_premier(p):
            p = random.randint(mini, maxi)
        return p

    def generer_cles(mini=1000, maxi=9999, e=65537):
        p = premier_aleatoire(mini, maxi)
        q = premier_aleatoire(mini, maxi)
        while p == q or pgcd(e, (p - 1) * (q - 1)) != 1:
            p = premier_aleatoire(mini, maxi)       # on recommence
            q = premier_aleatoire(mini, maxi)
        n = p * q
        phi = (p - 1) * (q - 1)
        return (e, n), (inverse_modulaire(e, phi), n)
    ```

    **2.** Avec `random.seed(2026)` : clé publique `(65537, 32431187)`, clé privée `(18049793, 32431187)` ($n = 4931 \times 6577$).

    **3.** Si $p = q$, $n = p^2$ et l’on retrouve $p$ par une simple racine carrée ; de plus, la formule $\varphi = (p-1)(q-1)$ n’est plus la bonne et le déchiffrement échoue. Si $\mathrm{pgcd}(e, \varphi) \neq 1$, $e$ n’a pas d’inverse modulo $\varphi$ : pas de clé privée.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 11</span> — Chiffrer un vrai message <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-cryptographie-tp-1-11 }

1.  <span class="run" title="À programmer et tester sur machine">▶</span>  Écrire `chiffrer_message(message, cle_publique)`, qui renvoie la liste des `pow(ord(c), e, n)` pour chaque caractère `c`, et `dechiffrer_message(nombres, cle_privee)`, qui reconstruit la chaîne avec `chr`. Chiffrer puis déchiffrer `"Rendez-vous à 18 h"`. Pourquoi faut-il $n >$ `ord(c)` pour tout caractère ?

2.  Observer la liste chiffrée : que remarque-t-on pour les lettres répétées ? Quelle attaque de la partie A redevient possible ? *(En pratique, RSA ajoute un « remplissage » aléatoire au message, et ne sert qu’à chiffrer une clé de session AES, comme dans HTTPS.)*

??? corrige "Corrigé"

    ```python
    def chiffrer_message(message, cle_publique):
        e, n = cle_publique
        return [pow(ord(c), e, n) for c in message]

    def dechiffrer_message(nombres, cle_privee):
        d, n = cle_privee
        message = ""
        for x in nombres:
            message = message + chr(pow(x, d, n))
        return message
    ```

    **1.** Le déchiffrement redonne `"Rendez-vous à 18 h"`. RSA travaille modulo $n$ : un nombre $M \geqslant n$ serait ramené à son reste et ne pourrait pas être retrouvé.

    **2.** Début de la liste : `[28766602, 17717906, 4785882, 22928393, 17717906, …]` : les deux `e` de « Rendez » donnent le même nombre $17\,717\,906$. Caractère par caractère, RSA se comporte comme un **chiffrement par substitution** : l’analyse de fréquences de la partie A s’applique. D’où le remplissage aléatoire en pratique.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 12</span> — Signer <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-cryptographie-tp-1-12 }

Pour signer, on chiffre avec la clé **privée** ; tout le monde vérifie avec la clé **publique**. On ne signe pas le message lui-même mais son **empreinte** (fonction fournie `empreinte(message, n)`, un nombre entre $0$ et $n-1$ calculé par la fonction de hachage SHA-256 : changer une seule lettre du message change complètement l’empreinte).

1.  <span class="run" title="À programmer et tester sur machine">▶</span>  Écrire `signer(message, cle_privee)`, qui renvoie $h^{d} \bmod n$ où $h$ est l’empreinte, et `verifier(message, signature, cle_publique)`, qui renvoie `True` si $s^{e} \bmod n$ est égal à l’empreinte du message.

2.  <span class="run" title="À programmer et tester sur machine">▶</span>  Signer `"Je dois 10 euros a Bob"`, vérifier la signature, puis vérifier la même signature avec le message `"Je dois 1000 euros a Bob"`. Qu’est-ce qu’une signature garantit ?

??? corrige "Corrigé"

    ```python
    def signer(message, cle_privee):
        d, n = cle_privee
        return pow(empreinte(message, n), d, n)

    def verifier(message, signature, cle_publique):
        e, n = cle_publique
        return pow(signature, e, n) == empreinte(message, n)
    ```

    Avec les clés de l’exercice 10 : la signature vaut $24\,670\,169$ ; `verifier` renvoie `True` pour le message signé et `False` pour « 1000 euros ». La signature garantit l’**authenticité** (seul le détenteur de la clé privée a pu la produire) et l’**intégrité** (le message n’a pas été modifié) ; elle ne le rend pas secret.

## Partie E — Factoriser $n$ : l’expérience qui rassure

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 13</span> — Quand la factorisation devient lente <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-cryptographie-tp-1-13 }

1.  <span class="run" title="À programmer et tester sur machine">▶</span>  Compléter `factoriser(n)`, qui cherche le plus petit diviseur $d \geqslant 2$ de $n$ (tant que $d \times d \leqslant n$) et renvoie `(d, n // d)`, ou `None` si $n$ est premier. Vérifier : `factoriser(3233)` vaut `(53, 61)`.

2.  <span class="run" title="À programmer et tester sur machine">▶</span>  Chacun des nombres suivants est le produit de deux nombres premiers. Mesurer le temps de `factoriser` (avec `time.perf_counter()`), puis recopier et compléter le tableau :

|               $n$ | **chiffres de $n$** | **facteurs trouvés** | **durée (s)** |
|------------------:|:-------------------:|:--------------------:|:-------------:|
|         `1373249` |         $7$         |                      |               |
|       `133763569` |         $9$         |                      |               |
|     `13334100011` |        $11$         |                      |               |
|   `1333361000071` |        $13$         |                      |               |
| `133333863333859` |        $15$         |                      |               |

1.  Par combien la durée est-elle multipliée quand $n$ gagne deux chiffres ? Expliquer ce facteur à partir du nombre de tours de boucle.

2.  Une clé RSA réelle de $2\,048$ bits a un $n$ de $617$ chiffres. En prolongeant vos mesures, estimer la durée de `factoriser` sur un tel nombre, et la comparer à l’âge de l’Univers (environ $4 \times 10^{17}$ secondes). *(Il existe des algorithmes de factorisation bien meilleurs, mais aucun ne casse une telle clé.)*

3.  <span class="run" title="À programmer et tester sur machine">▶</span>  **Attaque** : échanger sa clé publique avec un autre binôme, puis factoriser son $n$, recalculer $\varphi$ et $d$, et déchiffrer un message qu’il vous a envoyé. Combien de temps a-t-il fallu ? Qu’en conclure sur des nombres premiers à $4$ chiffres ?

??? corrige "Corrigé"

    ```python
    def factoriser(n):
        d = 2
        while d * d <= n:
            if n % d == 0:
                return d, n // d
            d += 1
        return None

    for n in (1373249, 133763569, 13334100011, 1333361000071, 133333863333859):
        debut = time.perf_counter()
        f = factoriser(n)
        print(n, len(str(n)), f, time.perf_counter() - debut)
    ```

    | $n$ | **chiffres** | **facteurs** | **durée mesurée** |
    |---:|:--:|:--:|:--:|
    | `1373249` | $7$ | $1\,009 \times 1\,361$ | $0{,}0001$ s |
    | `133763569` | $9$ | $10\,007 \times 13\,367$ | $0{,}001$ s |
    | `13334100011` | $11$ | $100\,003 \times 133\,337$ | $0{,}013$ s |
    | `1333361000071` | $13$ | $1\,000\,003 \times 1\,333\,357$ | $0{,}13$ s |
    | `133333863333859` | $15$ | $10\,000\,019 \times 13\,333\,361$ | $1{,}26$ s |

    **3.** La durée est multipliée par environ **10** à chaque fois que $n$ gagne deux chiffres. La boucle tourne jusqu’au plus petit facteur $p \approx \sqrt{n}$ ; quand $n$ est multiplié par $100$, $\sqrt{n}$ (donc le nombre de tours) est multiplié par $10$. Le coût est exponentiel en le *nombre de chiffres* de $n$.

    **4.** De $15$ à $617$ chiffres, on ajoute $602$ chiffres, soit $301$ fois un facteur $10$ : environ $1{,}26 \times 10^{301}$ secondes, soit plus de $10^{283}$ fois l’âge de l’Univers.

    **5.** Avec des premiers à $4$ chiffres, $n$ en a $7$ ou $8$ : `factoriser(32431187)` renvoie `(4931, 6577)` instantanément, puis $\varphi = 4930 \times 6576$ et `d = pow(65537, -1, phi)` : la clé privée est retrouvée et le message déchiffré en moins d’une seconde. De tels nombres ne protègent rien : la sécurité exige des premiers de plus de $150$ chiffres.

## Bilan du TP

!!! encadre "À rédiger (une quinzaine de lignes)"

    1.  Pour César, Vigenère et le masque jetable réutilisé : quelle faiblesse a-t-on exploitée ? Qu’est-ce qu’un bon chiffrement ne doit pas conserver du message ?

    2.  Résumer en quatre étapes la fabrication d’une paire de clés RSA, en citant les fonctions écrites.

    3.  Sur quoi repose la sécurité de RSA ? Appuyer la réponse sur les mesures de la partie E.

    4.  Chiffrer et signer : quelle clé utilise-t-on dans chaque cas, et qu’est-ce que chacun garantit ?
