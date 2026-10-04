# Exercices

<p class="sous-titre">Cryptographie</p>

Usage de l’IA, indiqué sur chaque exercice : <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> aucune ; <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> en appui (déboguer, reformuler, vérifier ; la réponse finale est écrite et comprise par vous) ; <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> l’exercice s’appuie sur une réponse d’IA. Voir la [charte d’usage de l’IA](../charte.md).

*Rappel des rangs : `A`${=}0$, `B`${=}1$, …, `Z`${=}25$. On travaille toujours en majuscules, sans accents.* Niveau : ★ échauffement, ★★ classique (niveau bac), ★★★ défi ; les *coups de pouce* et les *corrigés* se déplient sous chaque exercice.

### Chiffrements symétriques

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 1</span> — Le chiffre de César, à la main <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-12-1 }

1.  Chiffrer le mot `NSI` avec la clé $k=4$.

2.  Le mot `KHOOR` a été chiffré avec la clé $k=3$. Le déchiffrer.

3.  Combien y a-t-il de clés possibles pour le chiffre de César ? En déduire pourquoi ce code est très facile à casser par un ordinateur.

4.  On intercepte le mot chiffré `YLUKLGCVBZ`, obtenu avec une clé de César inconnue. Expliquer la stratégie de l’**attaque par force brute** pour retrouver le message clair (on ne demande pas de tout dérouler).

??? corrige "Corrigé"

    1.  `N`(13)$\to$<!-- -->17 `R`, `S`(18)$\to$<!-- -->22 `W`, `I`(8)$\to$<!-- -->12 `M` : `NSI` devient **`RWM`**.

    2.  On décale de $3$ en arrière : `K`$\to$`H`, `H`$\to$`E`, `O`$\to$`L`, `O`$\to$`L`, `R`$\to$`O` : **`HELLO`**.

    3.  Il y a **26 clés** ($k$ de $0$ à $25$). Un ordinateur les teste *toutes* instantanément : le code est cassé en quelques microsecondes.

    4.  **Force brute** : on déchiffre `YLUKLGCVBZ` avec chacun des $26$ décalages ; un seul essai donne un mot français lisible. Ici, pour $k=7$, on obtient `RENDEZVOUS` : c’est le message clair.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 2</span> — Le chiffre de César, en Python <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-2 }

Recopier et compléter la fonction `cesar` qui chiffre `message` avec la clé `k`.

```python
def cesar(message, k):
    resultat = ""
    for lettre in message:
        rang = ord(lettre) - ord("A")
        nouveau = ...                 # (a) decaler de k, modulo 26
        resultat = resultat + ...     # (b) reconvertir en lettre
    return resultat
```

1.  Compléter les lignes `(a)` et `(b)`.

2.  Comment appeler `cesar` pour *déchiffrer* un message chiffré avec la clé `k` ? (Deux façons possibles.)

??? corrige "Corrigé"

    1.  `(a)` `nouveau = (rang + k) % 26` ; `(b)` `resultat + chr(nouveau + ord("A"))`.

    2.  Pour déchiffrer : `cesar(message, -k)` ou, de façon équivalente, `cesar(message, 26 - k)`.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 3</span> — Le chiffrement affine <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-12-3 }

Chaque lettre de rang $x$ devient $(a\,x+b)\bmod 26$. La clé est le couple $(a,b)$.

1.  Pourquoi $a$ doit-il être **premier avec $26$** ? Donner la liste de toutes les valeurs possibles de $a$.

    ??? pouce "Coup de pouce"

        Essayer $a=2$ : quelles lettres deviennent `A` ? Peut-on encore déchiffrer sans ambiguïté ?

2.  Chiffrer `NSI` avec la clé $(a,b)=(3,1)$.

3.  Pour déchiffrer, on a besoin de l’**inverse modulaire** de $a$. Vérifier que $9$ est l’inverse de $3$ modulo $26$ (c’est-à-dire $3\times 9\equiv 1\ [26]$).

4.  En déduire la formule de déchiffrement, puis déchiffrer `ODZ` chiffré avec $(3,1)$.

    ??? pouce "Coup de pouce"

        Partir de $y=(a\,x+b)\bmod 26$ et isoler $x$ : on ne divise pas par $a$ modulo $26$, on multiplie par son inverse.

??? corrige "Corrigé"

    1.  Si $a$ n’est pas premier avec $26$, la fonction $x\mapsto(ax+b)\bmod 26$ n’est pas une bijection : deux lettres différentes peuvent avoir le même chiffré, le déchiffrement devient impossible. Valeurs possibles : **$1,3,5,7,9,11,15,17,19,21,23,25$**.

    2.  `N`(13)$\to 3\times13+1=40\equiv14$ `O` ; `S`(18)$\to 3\times18+1=55\equiv3$ `D` ; `I`(8)$\to 3\times8+1=25$ `Z`. Résultat : **`ODZ`**.

    3.  $3\times 9 = 27 = 26 + 1$, donc $3\times 9\equiv 1\ [26]$ : $9$ est bien l’inverse de $3$.

    4.  Déchiffrement : $x = 9\,(y - 1)\bmod 26$. Sur `ODZ` : `O`(14)$\to 9(14-1)=117\equiv13$ `N` ; `D`(3)$\to 9(3-1)=18$ `S` ; `Z`(25)$\to 9(25-1)=216\equiv8$ `I`. On retrouve **`NSI`**.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 4</span> — Vigenère : la clé qui se répète <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-12-4 }

On chiffre en additionnant, modulo $26$, chaque lettre du message avec la lettre correspondante de la clé, **répétée** autant de fois que nécessaire.

1.  Chiffrer `ANANAS` avec la clé `NSI` (répétée en `NSINSI`).

2.  Dans le mot chiffré, une même lettre du clair (par exemple les trois `A`) donne-t-elle toujours la même lettre chiffrée ? Comparer avec César sur ce point.

3.  Le chiffre de Vigenère fut réputé « indéchiffrable » pendant trois siècles. Quelle propriété de la clé (le fait qu’elle se *répète*) a finalement permis de le casser ?

    ??? pouce "Coup de pouce"

        Avec une clé de $3$ lettres, comment sont chiffrées les lettres de rangs $1$, $4$, $7$, … du message ? Quel chiffrement déjà cassé retrouve-t-on ?

??? corrige "Corrigé"

    1.  `A`+`N`$=0+13=13$ `N` ; `N`+`S`$=13+18=31\equiv5$ `F` ; `A`+`I`$=0+8=8$ `I` ; `N`+`N`$=13+13=26\equiv0$ `A` ; `A`+`S`$=0+18=18$ `S` ; `S`+`I`$=18+8=26\equiv0$ `A`. Résultat : **`NFIASA`**.

    2.  **Non.** Les trois `A` du clair deviennent `N`, `I` et `S`, et les deux `N` deviennent `F` et `A` : une même lettre du clair donne des lettres chiffrées différentes selon sa position face à la clé. À l’inverse, deux lettres différentes du clair (`N` et `S`) donnent ici le même `A`. Avec César, une lettre est toujours chiffrée pareil. Cela rend l’analyse des fréquences bien plus difficile.

    3.  La clé se **répète** périodiquement : des groupes de lettres identiques dans le clair, espacés d’un multiple de la longueur de la clé, produisent les mêmes groupes chiffrés. Ces répétitions trahissent la longueur de la clé (méthode de Babbage-Kasiski), après quoi le chiffre se ramène à plusieurs César.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 5</span> — Le masque jetable et le XOR <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-12-5 }

En informatique, le masque jetable combine chaque caractère du message avec la clé par un **OU exclusif** (XOR, noté `^`).

```python
def chiffre(message, masque):
    resultat = ""
    for i in range(len(message)):
        code = ord(message[i]) ^ ord(masque[i])
        resultat = resultat + chr(code)
    return resultat
```

1.  On sait que $65\ \texttt{\^{}}\ 66 = 3$. Que vaut $3\ \texttt{\^{}}\ 66$ ? Qu’illustre ce calcul sur le XOR ?

2.  En déduire pourquoi la *même* fonction `chiffre` sert aussi à **déchiffrer**.

3.  À quelles conditions (longueur, hasard, réutilisation) le masque jetable est-il **inviolable** ? Citer le nom du chercheur qui l’a démontré.

4.  Pourquoi, malgré cette perfection théorique, n’utilise-t-on pas le masque jetable partout ?

??? corrige "Corrigé"

    1.  $3\ \texttt{\^{}}\ 66 = 65$ (car $65\ \texttt{\^{}}\ 66 = 3$, et appliquer $\texttt{\^{}}\,66$ de nouveau annule l’opération). Le XOR est son **propre inverse** : $(m\oplus k)\oplus k = m$.

    2.  Chiffrer une deuxième fois avec le même masque annule le premier XOR et redonne le message clair : `chiffre(chiffre(msg, masque), masque) == msg`. Une seule fonction suffit.

    3.  Il est inviolable si le masque est **aléatoire**, **aussi long que le message** et **utilisé une seule fois** (jetable). Démontré par **Claude Shannon** (1949).

    4.  Il faudrait une clé aussi longue que *tout* ce qu’on veut s’envoyer, vraiment aléatoire et jamais réutilisée : la production et surtout la **distribution** d’une telle clé sont impraticables au quotidien.

### Chiffrement asymétrique et RSA

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Symétrique ou asymétrique ? <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-12-6 }

1.  Expliquer en une phrase la différence entre un chiffrement **symétrique** et un chiffrement **asymétrique**.

2.  Citer le principal **défaut** du chiffrement symétrique, que l’asymétrique vient résoudre.

3.  Alice veut envoyer un message confidentiel à Bob. Avec *quelle* clé, et de *qui*, doit-elle chiffrer ? Avec quelle clé Bob déchiffre-t-il ?

    ??? pouce "Coup de pouce"

        Tout le monde doit pouvoir écrire à Bob, mais seul Bob doit pouvoir lire : laquelle de ses deux clés reste chez lui ?

4.  Alice veut maintenant **prouver** que c’est bien elle qui écrit (signature). Avec quelle clé chiffre-t-elle alors ?

??? corrige "Corrigé"

    1.  **Symétrique** : une *même* clé secrète chiffre et déchiffre. **Asymétrique** : *deux* clés distinctes, une publique pour chiffrer, une privée pour déchiffrer.

    2.  Le **problème de l’échange de la clé** : il faut avoir partagé la clé secrète *avant* de communiquer, ce qui est difficile sur un canal non sûr.

    3.  Alice chiffre avec la clé **publique de Bob** ; Bob déchiffre avec sa clé **privée**.

    4.  Pour signer, Alice chiffre avec sa **propre clé privée** : n’importe qui peut vérifier avec la clé publique d’Alice que le message vient bien d’elle.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — RSA à la main — fabriquer les clés (1) <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-12-7 }

Alice choisit les nombres premiers $p=3$ et $q=11$.

1.  Calculer $n=p\times q$, puis $\varphi=(p-1)(q-1)$.

2.  Alice choisit $e=3$. Vérifier que $e$ est bien premier avec $\varphi$. Donner la **clé publique**.

3.  Trouver $d$, l’inverse modulaire de $e$ (le nombre tel que $3d\equiv 1\ [20]$). Donner la **clé privée**.

    ??? pouce "Coup de pouce"

        Tester $d=1,2,3,\dots$ : calculer $3d$ et regarder le reste de sa division par $20$.

4.  Bob envoie le nombre $M=5$. Calculer le message chiffré $C=M^{e}\bmod n$.

5.  Vérifier que le déchiffrement redonne bien $5$ (on admettra le calcul de $26^{7}\bmod 33$, qui vaut $5$).

??? corrige "Corrigé"

    1.  $n = 3\times 11 = \mathbf{33}$ ; $\varphi = (3-1)(11-1) = 2\times 10 = \mathbf{20}$.

    2.  $\text{PGCD}(3,20)=1$ : $e=3$ convient. **Clé publique : $(3,\,33)$**.

    3.  On cherche $d$ tel que $3d\equiv 1\ [20]$ : $3\times 7 = 21 = 20+1$, donc $\mathbf{d=7}$. **Clé privée : $(7,\,33)$**.

    4.  $C = 5^{3}\bmod 33 = 125\bmod 33 = 125 - 3\times 33 = \mathbf{26}$.

    5.  $26^{7}\bmod 33 = 5$ : on retrouve bien le message $M=5$.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — RSA à la main — trouver $d$ (2) <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-8 }

Cette fois $p=7$ et $q=11$, et Alice choisit $e=7$.

1.  Calculer $n$ et $\varphi$.

2.  Pour trouver $d$ tel que $7d\equiv 1\ [60]$, on peut tester $d=1,2,3,\dots$ jusqu’à tomber sur un multiple de $60$ plus $1$. Montrer que $d=43$ convient (calculer $7\times 43$).

3.  Donner la clé publique et la clé privée.

4.  Bob envoie $M=2$. Calculer $C=2^{7}\bmod 77$.

    ??? pouce "Coup de pouce"

        Calculer d’abord $2^{7}$, puis le reste de sa division par $n$.

??? corrige "Corrigé"

    1.  $n = 7\times 11 = \mathbf{77}$ ; $\varphi = 6\times 10 = \mathbf{60}$.

    2.  $7\times 43 = 301 = 5\times 60 + 1$, donc $7\times 43\equiv 1\ [60]$ : $\mathbf{d = 43}$ convient.

    3.  **Clé publique : $(7,\,77)$** ; **clé privée : $(43,\,77)$**.

    4.  $C = 2^{7}\bmod 77 = 128\bmod 77 = 128 - 77 = \mathbf{51}$.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 9</span> — L’inverse modulaire en Python <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-9 }

En Python, on calcule $d$ par `d = pow(e, -1, phi)`.

1.  Que renvoie `pow(3, -1, 20)` ? `pow(7, -1, 60)` ?

2.  Que calcule l’appel `pow(M, e, n)` ? Pourquoi l’écrit-on ainsi plutôt que `(M ** e) % n` ?

    ??? pouce "Coup de pouce"

        Imaginer $M$ et $e$ de plusieurs centaines de chiffres : combien de chiffres aurait `M ** e` ?

3.  Compléter la fonction de génération de clés :

    ??? pouce "Coup de pouce"

        Reprendre les trois premières étapes de RSA du cours : une ligne par étape.

    ```python
    def generer_cles(p, q, e):
        n = ...
        phi = ...
        d = ...
        return (e, n), (d, n)   # (cle publique, cle privee)
    ```

??? corrige "Corrigé"

    1.  `pow(3, -1, 20)` renvoie `7` ; `pow(7, -1, 60)` renvoie `43`.

    2.  `pow(M, e, n)` calcule $M^{e}\bmod n$. On l’écrit ainsi car c’est une **exponentiation modulaire rapide** : elle réduit modulo $n$ à chaque étape et ne manipule jamais le nombre géant $M^{e}$ (contrairement à `(M ** e) % n`).

    3.  `n = p * q` ; `phi = (p - 1) * (q - 1)` ; `d = pow(e, -1, phi)`.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 10</span> — L’échange de clé de Diffie-Hellman <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-10 }

Alice et Bob veulent fabriquer une clé secrète commune *en public*. Ils conviennent publiquement de $p=23$ et $g=5$.

1.  Alice choisit en secret $a=4$ et publie $A=g^{a}\bmod p$. Calculer $A$.

    ??? pouce "Coup de pouce"

        Calculer $5^{4}$, puis lui retirer le plus grand multiple de $23$ possible.

2.  Bob choisit en secret $b=3$ et publie $B=g^{b}\bmod p$. Calculer $B$.

3.  Alice calcule $B^{a}\bmod p$ ; Bob calcule $A^{b}\bmod p$. Vérifier qu’ils obtiennent **le même** secret.

4.  Ève a intercepté $p$, $g$, $A$ et $B$. Pourquoi ne peut-elle pas retrouver le secret commun aussi facilement qu’Alice et Bob ?

    ??? pouce "Coup de pouce"

        Pour calculer le secret, il faut connaître $a$ ou $b$. Quelle opération Ève devrait-elle savoir « inverser » pour les retrouver à partir de $A$ ou $B$ ?

??? corrige "Corrigé"

    1.  $A = 5^{4}\bmod 23 = 625\bmod 23 = \mathbf{4}$.

    2.  $B = 5^{3}\bmod 23 = 125\bmod 23 = \mathbf{10}$.

    3.  Alice : $B^{a} = 10^{4}\bmod 23 = \mathbf{18}$. Bob : $A^{b} = 4^{3}\bmod 23 = 64\bmod 23 = \mathbf{18}$. Même secret **$18$**, jamais transmis.

    4.  Pour retrouver le secret, Ève devrait retrouver $a$ (ou $b$) à partir de $A=g^{a}\bmod p$ : c’est le **problème du logarithme discret**, qui n’a pas d’algorithme rapide connu. Alice et Bob, eux, connaissent leur exposant secret.

### HTTPS

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 11</span> — Le petit cadenas du navigateur <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-12-11 }

1.  HTTPS combine un chiffrement **asymétrique** et un chiffrement **symétrique**. Lequel sert à *échanger la clé*, lequel sert à chiffrer *les données* ? Pourquoi ce partage des rôles ?

2.  Remettre dans l’ordre les étapes de la poignée de main (*handshake*) TLS :

    - le client fabrique une clé symétrique, la chiffre avec la clé publique du serveur et l’envoie ;

    - le serveur envoie son certificat et sa clé publique ;

    - les deux échangent ensuite leurs données chiffrées en symétrique (AES) ;

    - le client vérifie le certificat auprès d’une autorité de certification.

3.  À quoi sert le **certificat** ? Que risquerait-on sans lui ?

??? corrige "Corrigé"

    1.  L’**asymétrique** sert à *échanger la clé* de session ; le **symétrique** (AES) chiffre ensuite *les données*. Raison : l’asymétrique résout l’échange de clé mais est lent ; le symétrique est rapide mais suppose une clé partagée — on combine leurs forces.

    2.  Ordre : **(1)** le serveur envoie son certificat et sa clé publique ; **(2)** le client vérifie le certificat auprès d’une autorité de certification ; **(3)** le client fabrique une clé symétrique, la chiffre avec la clé publique du serveur et l’envoie ; **(4)** les deux échangent leurs données chiffrées en symétrique (AES).

    3.  Le **certificat** authentifie le serveur (garantit que la clé publique est bien la sienne). Sans lui, un attaquant pourrait se placer au milieu (*man in the middle*) en présentant sa propre clé publique.

### Vers le bac

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 12</span> — Type bac — La méthode du masque jetable *(Métropole 2025, jour 2,* `25-NSIJ2ME1`*)* <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-12 }

**Partie A — Le masque jetable.** On attribue à chaque lettre son rang ($0$ à $25$). Pour chiffrer, on additionne le rang de chaque lettre du message avec celui de la lettre correspondante du masque ; si le résultat dépasse $25$, on retranche $26$ (calcul « modulo $26$ »). Exemple : `HELLO` avec le masque `WMCKL` donne `DQNVZ`.

1.  Chiffrer le message `LIBRE` à l’aide de la clé `EYQMT`.

On dispose de la variable `alphabet` (liste des $26$ lettres dans l’ordre) accessible partout.

1.  Écrire une fonction `indice(L, element)` qui renvoie l’indice de `element` dans la liste `L` (on suppose `element` présent une seule fois). Par exemple `indice(alphabet, ’K’)` renvoie `10`.

    ??? pouce "Coup de pouce"

        On veut l’*indice*, pas l’élément : quelle forme de boucle `for` donne accès aux indices ?

2.  Écrire `lettres_vers_indices(chaine)` qui renvoie la liste des indices des lettres. Par exemple `lettres_vers_indices(’HELLO’)` renvoie `[7, 4, 11, 11, 14]`.

    ??? pouce "Coup de pouce 2 (début de solution)"

        `def lettres_vers_indices(chaine):`  
        `resultat = []`  
        `for lettre in chaine:`  
        `...`

On dispose aussi de `indices_vers_lettres` (réciproque, non demandée). Voici la fonction `chiffrement`, incomplète :

```python
def chiffrement(msg, cle):
    assert len(cle) >= len(msg), "impossible"
    indices_msg = lettres_vers_indices(msg)
    indices_cle = lettres_vers_indices(cle)
    n = len(msg)
    indices_msg_chiffre = []
    for k in range(n):
        ind = ...              # (a)
        if ind >= 26:
            ind = ...           # (b)
        indices_msg_chiffre.append(ind)
    msg_chiffre = indices_vers_lettres(...)   # (c)
    return msg_chiffre
```

1.  Recopier et compléter les lignes `(a)`, `(b)` et `(c)`.

2.  Indiquer, en justifiant, ce que renvoie l’appel `chiffrement(’RESEAU’, ’GFTZ’)`.

    ??? pouce "Coup de pouce"

        Comparer les longueurs du message et de la clé, puis relire la première ligne de la fonction.

3.  Déchiffrer le message `GMEDH` avec la clé `FVEIT`. Expliquer la méthode de déchiffrement quand on connaît la clé.

    ??? pouce "Coup de pouce"

        On fait l’opération inverse : soustraire au lieu d’additionner. Si le résultat est négatif, comment revenir entre $0$ et $25$ ?

4.  Adapter la fonction `chiffrement` pour obtenir une fonction `dechiffrement` (indiquer les lignes à modifier).

**Partie B — Sécurisation des communications.**

1.  Expliquer la différence entre un algorithme de chiffrement symétrique et asymétrique.

2.  Bob envoie sa clé publique à Alice, qui chiffre son message avec cette clé et l’envoie à Bob. Indiquer comment Bob déchiffre le message reçu.

3.  Expliquer comment une tierce personne pourrait se faire passer pour Alice sans que Bob s’en aperçoive.

4.  Expliquer brièvement le fonctionnement du protocole **HTTPS**, et pourquoi on ne se contente pas d’un chiffrement asymétrique pour toute la communication.

??? corrige "Corrigé"

    **Partie A.**

    1.  `L`(11)+`E`(4)$=15$ `P` ; `I`(8)+`Y`(24)$=32\equiv6$ `G` ; `B`(1)+`Q`(16)$=17$ `R` ; `R`(17)+`M`(12)$=29\equiv3$ `D` ; `E`(4)+`T`(19)$=23$ `X`. Résultat : **`PGRDX`**.

    2.

        ```python
        def indice(L, element):
            for i in range(len(L)):
                if L[i] == element:
                    return i
        ```

    3.

        ```python
        def lettres_vers_indices(chaine):
            resultat = []
            for lettre in chaine:
                resultat.append(indice(alphabet, lettre))
            return resultat
        ```

        *Autre méthode :* on construit directement la liste des indices par compréhension.

        ```python
        def lettres_vers_indices(chaine):
            return [indice(alphabet, lettre) for lettre in chaine]
        ```

    4.  `(a)` `ind = indices_msg[k] + indices_cle[k]` ; `(b)` `ind = ind - 26` ; `(c)` `indices_vers_lettres(indices_msg_chiffre)`.

    5.  L’assertion `len(cle) >= len(msg)` est fausse (`len(’GFTZ’)`$=4 < 6=$`len(’RESEAU’)`) : l’appel **lève une `AssertionError` « impossible »**. Le masque doit être au moins aussi long que le message.

    6.  Déchiffrement : on *soustrait* le rang de la clé (et on ajoute $26$ si le résultat est négatif). `G`(6)$-$`F`(5)$=1$ `B` ; `M`(12)$-$`V`(21)$=-9\equiv17$ `R` ; `E`(4)$-$`E`(4)$=0$ `A` ; `D`(3)$-$`I`(8)$=-5\equiv21$ `V` ; `H`(7)$-$`T`(19)$=-12\equiv14$ `O`. Message : **`BRAVO`**.

    7.  Il suffit de remplacer l’addition par une **soustraction** et le test « $\ge 26$, on retranche $26$ » par « $< 0$, on ajoute $26$ » :

        ```python
        def dechiffrement(msg, cle):
            assert len(cle) >= len(msg), "impossible"
            indices_msg = lettres_vers_indices(msg)
            indices_cle = lettres_vers_indices(cle)
            n = len(msg)
            indices_msg_dechiffre = []
            for k in range(n):
                ind = indices_msg[k] - indices_cle[k]
                if ind < 0:
                    ind = ind + 26
                indices_msg_dechiffre.append(ind)
            return indices_vers_lettres(indices_msg_dechiffre)
        ```

    **Partie B.**

    1.  Symétrique : *une* clé commune chiffre et déchiffre. Asymétrique : *deux* clés (publique pour chiffrer, privée pour déchiffrer).

    2.  Bob déchiffre avec sa **clé privée** (le message a été chiffré avec sa clé publique).

    3.  Une tierce personne peut aussi récupérer la clé *publique* de Bob (elle est publique) et lui envoyer un message signé « Alice » : Bob ne peut pas vérifier l’expéditeur. Il manque l’**authentification** (une signature d’Alice avec *sa* clé privée).

    4.  **HTTPS** utilise un chiffrement **asymétrique** au début pour échanger de façon sûre une **clé symétrique** de session, puis chiffre toutes les données en **symétrique** (AES). On n’utilise pas que l’asymétrique car il est trop **lent** pour de gros volumes.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 13</span> — Type bac — Le chiffrement de Polybe *(Centres étrangers 2026, groupe 1, jour 1,* `26-NSIJ1G11`*)* <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-13 }

Le chiffrement de Polybe range les $26$ lettres et les $10$ chiffres dans une grille $6\times 6$. Chaque caractère est remplacé par le couple (numéro de ligne, numéro de colonne) de sa case. Exemple de grille :

|     |     |     |     |     |     |     |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|     |  1  |  2  |  3  |  4  |  5  |  6  |
|  1  |  Q  |  7  |  A  |  X  |  2  |  J  |
|  2  |  9  |  E  |  H  |  0  |  R  |  M  |
|  3  |  L  |  Z  |  4  |  W  |  D  |  O  |
|  4  |  6  |  V  |  N  |  B  |  8  |  K  |
|  5  |  P  |  Y  |  1  |  S  |  T  |  F  |
|  6  |  G  |  C  |  3  |  I  |  U  |  5  |

Ainsi `N` (ligne $4$, colonne $3$) donne $(4,3)$, et `NSI` se chiffre en $(4,3)\,(5,4)\,(6,4)$.

1.  Déchiffrer, avec la grille ci-dessus, le message $(6,2)\,(3,6)\,(3,5)\,(2,2)$.

Pour construire une grille, on choisit une **clé** (lettres toutes différentes), on l’écrit d’abord, puis on complète avec les lettres restantes dans l’ordre alphabétique, enfin les chiffres $0$ à $9$. Avec la clé `2048ALGORITHMES`, l’ordre d’insertion est `2048ALGORITHMESBCDFJKNPQUVWXYZ135679`.

1.  Chiffrer `BAC` avec la clé `SECURITY1024`.

    ??? pouce "Coup de pouce"

        Écrire d’abord l’ordre d’insertion complet, puis remplir la grille ligne par ligne, $6$ caractères par ligne.

2.  Pourquoi ce chiffrement est-il qualifié de **symétrique** ?

On donne la fonction `generer_ordre` :

```python
def generer_ordre(cle):
    ordre_insertion = cle
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    for lettre in alphabet:
        if lettre not in ordre_insertion:
            ordre_insertion = ordre_insertion + lettre
    return ordre_insertion
```

1.  Quel est le résultat de `generer_ordre(’AXU7’)` ?

2.  Écrire `grille_vide(n)` renvoyant un tableau de `n` lignes de `n` chaînes vides. Par exemple `grille_vide(3)` renvoie `[[’’,’’,’’], [’’,’’,’’], [’’,’’,’’]]`.

3.  Recopier et compléter les lignes `(a)`, `(b)`, `(c)` de `generer_grille` :

    ??? pouce "Coup de pouce"

        La variable `indice` avance de $1$ à chaque case : quel caractère de `ordre_insertion` placer en case `(i, j)` ?

    ```python
    def generer_grille(cle):
        ordre_insertion = generer_ordre(cle)
        grille = grille_vide(6)
        indice = 0
        for i in range(...):        # (a)
            for j in range(...):     # (b)
                grille[i][j] = ...    # (c)
                indice = indice + 1
        return grille
    ```

4.  Écrire la fonction `generer_dico(cle)` renvoyant le dictionnaire associant à chaque caractère sa position (un tuple) dans la grille. Puis écrire `chiffrer(cle, message)` renvoyant la liste des couples.

    ??? pouce "Coup de pouce 2 (début de solution)"

        `def generer_dico(cle):`  
        `grille = generer_grille(cle)`  
        `dico = {}`  
        `for i in range(6):`  
        `for j in range(6):`  
        Attention : les lignes et colonnes de la grille sont numérotées à partir de $1$.

5.  Alice et Bob changent de clé chaque jour et souhaitent se l’échanger par un chiffrement **asymétrique**. Expliquer la différence entre chiffrement symétrique et asymétrique.

??? corrige "Corrigé"

    1.  $(6,2)\to$`C`, $(3,6)\to$`O`, $(3,5)\to$`D`, $(2,2)\to$`E` : le message est **`CODE`**.

    2.  Avec la clé `SECURITY1024`, l’ordre d’insertion est  
        `SECURITY1024ABDFGHJKLMNOPQVWXZ356789`. La grille (remplie ligne par ligne) place `B` en $(3,2)$, `A` en $(3,1)$ et `C` en $(1,3)$. Donc `BAC` se chiffre en **$(3,2)\,(3,1)\,(1,3)$**.

    3.  C’est **symétrique** : la *même* grille (déterminée par la clé) sert à chiffrer *et* à déchiffrer. Qui connaît la clé peut faire les deux.

    4.  `generer_ordre(’AXU7’)` renvoie  
        `’AXU7BCDEFGHIJKLMNOPQRSTVWYZ012345689’` (on ajoute les lettres non présentes dans l’ordre alphabétique, puis les chiffres $\neq 7$).

    5.  Chaque ligne est une *nouvelle* liste de `n` chaînes vides, et la grille est la liste de ces `n` lignes : deux listes par compréhension imbriquées.

        ```python
        def grille_vide(n):
            return [["" for j in range(n)] for i in range(n)]
        ```

        *Autre méthode :* deux boucles imbriquées, une ligne après l’autre.

        ```python
        def grille_vide(n):
            grille = []
            for i in range(n):
                ligne = []
                for j in range(n):
                    ligne.append("")
                grille.append(ligne)
            return grille
        ```

    6.  `(a)` `range(6)` ; `(b)` `range(6)` ; `(c)` `ordre_insertion[indice]`.

    7.

        ```python
        def generer_dico(cle):
            grille = generer_grille(cle)
            dico = {}
            for i in range(6):
                for j in range(6):
                    dico[grille[i][j]] = (i + 1, j + 1)
            return dico

        def chiffrer(cle, message):
            dico = generer_dico(cle)
            return [dico[c] for c in message]    # le couple de chaque caractere
        ```

    8.  Symétrique : *une* clé partagée (ici la grille) ; le problème est de **se l’échanger** en sécurité. Asymétrique : *deux* clés (publique/privée), ce qui permet justement d’échanger la clé symétrique quotidienne sans l’avoir jamais transmise en clair.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 14</span> — Type bac — Transmettre une clé de session *(Métropole 2024, sujet 2,* `24-NSIJ2ME1`*)* <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-14 }

Bob a mis en place une base de données pour gérer sa collection de CD. Cette base est hébergée sur un serveur auquel il accède depuis un client installé sur son ordinateur personnel. Pour sécuriser la connexion, un algorithme de chiffrement **symétrique** est utilisé.

1.  Expliquer brièvement ce qu’est un algorithme de chiffrement symétrique.

La clé de chiffrement, notée $C$, est choisie aléatoirement par le serveur à chaque connexion d’un client. Pour que le chiffrement et le déchiffrement puissent se faire sans problème, le serveur doit envoyer au client la clé $C$ de façon sécurisée.

1.  Rappeler brièvement ce qu’est un algorithme de chiffrement asymétrique.

On suppose à présent que Bob possède une clé publique et une clé privée, et que sa clé publique est connue du serveur.

1.  Proposer une solution pour que le serveur envoie la clé $C$ à l’ordinateur de Bob de façon sécurisée, c’est-à-dire pour que **seul Bob** puisse déchiffrer la clé envoyée.

??? corrige "Corrigé"

    1.  Un algorithme de chiffrement **symétrique** utilise une **même clé**, partagée par l’émetteur et le destinataire, pour chiffrer et pour déchiffrer (exemple : AES).

    2.  Un algorithme de chiffrement **asymétrique** utilise une **paire de clés** : une clé **publique**, diffusée à tous, qui sert à chiffrer, et une clé **privée**, gardée secrète par son propriétaire, qui seule permet de déchiffrer (exemple : RSA).

    3.  Le serveur **chiffre la clé $C$ avec la clé publique de Bob** et envoie le résultat. Seul Bob possède la clé privée associée : lui seul peut déchiffrer et retrouver $C$. Ensuite, client et serveur échangent leurs données chiffrées en symétrique avec $C$ (plus rapide) — c’est le principe de HTTPS.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 15</span> — Type bac — Les mots de passe d’un hôpital *(Polynésie 2024, jour 2,* `24-NSIJ2PO1`*)* <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-15 }

Pour utiliser les ordinateurs d’un hôpital, tout le personnel doit saisir son identifiant puis son mot de passe. Pour davantage de sécurité, ce dernier doit être fort et changé régulièrement. On appelle « mot de passe fort » une chaîne de caractères composée : d’au minimum $12$ caractères ; d’au moins $2$ majuscules ; d’au moins $2$ chiffres ; d’au moins $2$ symboles parmi `#@!?%<>=€$+-*/&`. Par exemple, un médecin utilise le mot de passe fort `@20!HôPiTaL&24#`.

On dispose des méthodes `isalpha` (le caractère est-il une lettre ?), `isupper` (est-il une majuscule ?) et `isdigit` (est-il un chiffre ?) :

```console
>>> 'A'.isalpha()
True
>>> 'a'.isupper()
False
>>> '5'.isdigit()
True
```

Tous les symboles sont rangés dans une variable globale de type `str` :

```python
liste_symboles = '#@!?%<>=€$+-*/&'
```

1.  <span class="run" title="À programmer et tester sur machine">▶</span>  La fonction `mdp_fort` prend en paramètre une chaîne `mdp` et renvoie `True` si `mdp` est un mot de passe fort, `False` sinon. Compléter les lignes 2, 10, 12 et 14.

    ??? pouce "Coup de pouce"

        Ligne 2 : la longueur. Ligne 14 : il suffit qu’*une seule* des trois conditions de comptage échoue pour renvoyer `False`.

    ```python
    def mdp_fort(mdp):
        if ... :
            return False
        majuscules = 0
        chiffres = 0
        symboles = 0
        for caractere in mdp:
            if caractere.isupper():
                majuscules += 1
            if ... :
                chiffres += 1
            if ... :
                symboles += 1
        if ... :
            return False
        return True
    ```

Pour aider le personnel, le service informatique a écrit une fonction `creation_mdp` qui génère aléatoirement un mot de passe. Elle prend en paramètres quatre entiers : la longueur `n` du mot de passe, et les nombres minimaux `nbr_m` de majuscules, `nbr_c` de chiffres et `nbr_s` de symboles qu’il doit contenir. Elle renvoie une chaîne respectant ces conditions (la fonction `choice`, du module `random`, renvoie un élément choisi au hasard).

1.  <span class="run" title="À programmer et tester sur machine">▶</span>  Compléter la ligne 9 et les lignes 13 à 19.

    ```python
    def creation_mdp(n, nbr_m, nbr_c, nbr_s):
        mdp = ''
        caracteres = 'abcdefghijklmnopqrstuvwxyz' + \
                     'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' + \
                     '#@!?%<>=€$+-*/&'
        majuscules = 0
        chiffres = 0
        symboles = 0
        while ... :
            # la variable c contient un caractere
            # choisi aleatoirement dans la variable caracteres
            c = choice(caracteres)
            if ... :
                ...
            if ... :
                ...
            if ... :
                ...
            mdp = ...
        return mdp
    ```

Sans le générateur, le personnel a tendance à insérer des mots de la langue dans son mot de passe : `@20!HôPiTaL&24#` est fort, mais on y trouve le mot « hôpital ». Un mot de passe fort qui ne contient aucun mot de $4$ lettres ou plus de la langue française est dit « extra fort ». On dispose de la variable `dicoFR` (de type `list`), qui contient tous les mots de la langue française, et de la fonction `transforme`, qui renvoie une copie de la chaîne où toutes les majuscules sont devenues des minuscules (par exemple, `transforme(’@20!HôPiTaL&24#’)` renvoie `’@20!hôpital&24#’`).

On suppose que les mots présents dans un mot de passe sont entiers et séparés par des chiffres ou des symboles. La fonction `recherche_mot` prend en paramètre un mot de passe `mdp` et renvoie la liste des mots (en minuscules) qu’il contient :

```console
>>> recherche_mot('@20!NeUrO&24#')
['neuro']
>>> recherche_mot('Chef!14Neuro@85!')
['chef', 'neuro']
```

1.  <span class="run" title="À programmer et tester sur machine">▶</span>  Compléter les lignes 5, 6, 15, 16 et 18 de la fonction `recherche_mot`.

    ??? pouce "Coup de pouce"

        La boucle intérieure doit s’arrêter en fin de chaîne *ou* sur un chiffre ou un symbole : tester `i < len(mot)` en premier.

    ```python
    def recherche_mot(mdp):
        mot = transforme(mdp)
        trouve = []
        i = 0
        while ... :
            if ... :   # si le caractere est un chiffre
                i = i + 1
            elif mot[i] in liste_symboles:
                i = i + 1
            else:
                # si le caractere est une lettre, on prend les
                # lettres qui la suivent jusqu'au moment ou
                # on trouve un chiffre ou un symbole
                chaine = ''
                while ... :
                    chaine = ...
                    i = i + 1
                ...
        return trouve
    ```

2.  <span class="run" title="À programmer et tester sur machine">▶</span>  Écrire une fonction `mdp_extra_fort` qui prend en paramètre une chaîne `mdp` et renvoie `True` si `mdp` est un mot de passe extra fort, `False` sinon.

    ??? pouce "Coup de pouce"

        Réutiliser `mdp_fort` et `recherche_mot`, puis examiner chaque mot trouvé : sa longueur et sa présence dans `dicoFR`.

    ??? pouce "Coup de pouce 2 (début de solution)"

        `def mdp_extra_fort(mdp):`  
        `if not mdp_fort(mdp):`  
        `return False`  
        `for mot in recherche_mot(mdp):`

??? corrige "Corrigé"

    1.  Lignes 2, 10, 12 et 14 :

        ```python
        def mdp_fort(mdp):
            if len(mdp) < 12:
                return False
            majuscules = 0
            chiffres = 0
            symboles = 0
            for caractere in mdp:
                if caractere.isupper():
                    majuscules += 1
                if caractere.isdigit():
                    chiffres += 1
                if caractere in liste_symboles:
                    symboles += 1
            if majuscules < 2 or chiffres < 2 or symboles < 2:
                return False
            return True
        ```

    2.  On continue à tirer des caractères tant que la longueur voulue *ou* l’un des minimums n’est pas atteint (le mot de passe peut donc dépasser `n` caractères si le hasard tarde à fournir les majuscules, chiffres ou symboles demandés) :

        ```python
            while len(mdp) < n or majuscules < nbr_m or chiffres < nbr_c or symboles < nbr_s:
                # la variable c contient un caractere
                # choisi aleatoirement dans la variable caracteres
                c = choice(caracteres)
                if c.isupper():
                    majuscules += 1
                if c.isdigit():
                    chiffres += 1
                if c in liste_symboles:
                    symboles += 1
                mdp = mdp + c
        ```

        Par exemple, tout mot de passe renvoyé par `creation_mdp(12, 2, 2, 2)` est fort.

    3.  Lignes 5, 6, 15, 16 et 18 :

        ```python
        def recherche_mot(mdp):
            mot = transforme(mdp)
            trouve = []
            i = 0
            while i < len(mot):
                if mot[i].isdigit():   # si le caractere est un chiffre
                    i = i + 1
                elif mot[i] in liste_symboles:
                    i = i + 1
                else:
                    # si le caractere est une lettre, on prend les
                    # lettres qui la suivent jusqu'au moment ou
                    # on trouve un chiffre ou un symbole
                    chaine = ''
                    while i < len(mot) and not mot[i].isdigit() and mot[i] not in liste_symboles:
                        chaine = chaine + mot[i]
                        i = i + 1
                    trouve.append(chaine)
            return trouve
        ```

        La condition `i < len(mot)` doit être testée *en premier* (évaluation paresseuse du `and`) pour ne pas lire `mot[i]` hors de la chaîne quand le mot de passe se termine par une lettre.

    4.  Un mot de passe extra fort est d’abord fort, puis ne contient aucun mot d’au moins $4$ lettres présent dans `dicoFR` :

        ```python
        def mdp_extra_fort(mdp):
            if not mdp_fort(mdp):
                return False
            for m in recherche_mot(mdp):
                if len(m) >= 4 and m in dicoFR:
                    return False
            return True
        ```

        Ainsi `mdp_extra_fort(’@20!HôPiTaL&24#’)` renvoie `False` (il contient « hôpital »).

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 16</span> — Type bac — Les casiers connectés du lycée *(sujet maison, façon bac)* <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-12-16 }

*Cet exercice n’est pas un sujet officiel : il a été écrit au format du bac pour s’entraîner.*

Le lycée installe des casiers connectés. Pour ouvrir son casier, un élève utilise une application sur son téléphone, qui envoie au casier, par radio, un court message texte, par exemple `"OUVRE07"` pour le casier numéro $07$. Comme n’importe qui peut capter ces ondes, le message est chiffré.

**Partie A — Un XOR avec une clé courte.** Chaque caractère est remplacé par son code (`ord("O")` vaut $79$, `ord("U")` vaut $85$…). On combine ensuite chaque code avec un nombre de la clé par un **OU exclusif** (XOR, opérateur `^` en Python). Rappel : bit à bit, le XOR vaut $1$ si les deux bits sont différents, $0$ s’ils sont égaux. La clé, enregistrée une fois pour toutes dans l’application et dans le casier, est la liste `[23, 5, 42]` : elle est **répétée** autant que nécessaire.

1.  Écrire $79$ et $23$ en binaire sur $8$ bits, puis calculer $79\ \texttt{\^{}}\ 23$ bit à bit. Calculer ensuite $88\ \texttt{\^{}}\ 23$. Que constate-t-on ?

Un message est représenté par la liste de ses codes. On considère la fonction suivante, incomplète :

```python
def chiffrer_xor(codes, cle):
    resultat = []
    for i in range(len(codes)):
        k = cle[...]                  # (a) la cle est repetee
        resultat.append(...)          # (b)
    return resultat
```

1.  <span class="run" title="À programmer et tester sur machine">▶</span>  Recopier et compléter les lignes `(a)` et `(b)`. Pour un message de $7$ codes, donner l’indice de la clé utilisé pour chaque valeur de `i` de $0$ à $6$.

    ??? pouce "Coup de pouce"

        Pour faire « tourner » un indice sur une clé de longueur $3$, utiliser le reste de la division de `i` par `len(cle)`.

2.  Expliquer pourquoi la *même* fonction `chiffrer_xor`, avec la même clé, permet au casier de **déchiffrer**. Ce chiffrement est-il symétrique ou asymétrique ? Justifier.

Ève, une élève curieuse, capte le message chiffré `[88, 80, 124, 69, 64, 26, 32]`. Elle ne connaît pas la clé, mais elle sait que tous les messages commencent par `"OUVRE"` et que la clé contient trois nombres.

1.  Montrer que si $c = m\ \texttt{\^{}}\ k$, alors $k = c\ \texttt{\^{}}\ m$. En déduire, sachant que `"OUV"` a pour codes $79$, $85$, $86$, les trois nombres de la clé (détailler les calculs en binaire).

2.  <span class="run" title="À programmer et tester sur machine">▶</span>  Écrire une fonction `retrouver_cle(intercepte, debut_connu, n)` qui renvoie la liste des `n` premiers nombres de la clé, à partir de la liste `intercepte` des codes chiffrés et de la liste `debut_connu` des codes du début du message clair (on suppose qu’elles contiennent au moins `n` éléments). Quel appel permet ensuite à Ève de lire tout le message ?

    ??? pouce "Coup de pouce"

        Appliquer la question 4 à chaque position : le $i$-ième nombre de la clé s’obtient à partir de `intercepte[i]` et `debut_connu[i]`.

    ??? pouce "Coup de pouce 2 (début de solution)"

        `def retrouver_cle(intercepte, debut_connu, n):`  
        `cle = []`  
        `for i in range(n):`

3.  Le cours présente le masque jetable comme un chiffrement **inviolable**. Citer les conditions qu’il impose et expliquer lesquelles ne sont pas respectées ici.

**Partie B — Échanger une clé neuve avec RSA.** Pour corriger le défaut, l’application tire au hasard une **nouvelle clé** à chaque ouverture et l’envoie d’abord au casier, chiffrée avec RSA. Le casier possède une paire de clés fabriquée avec $p = 17$, $q = 19$ et $e = 5$.

1.  Calculer $n$ et $\varphi$. Vérifier que $e$ est premier avec $\varphi$, puis que $d = 173$ convient (calculer $5\times 173$). Donner la clé publique et la clé privée du casier.

2.  L’application doit transmettre le nombre $K = 42$ (un nombre de la nouvelle clé). Écrire l’instruction Python qui calcule le nombre chiffré $C$ ; on obtient $C = 264$. Écrire l’instruction que le casier exécute pour retrouver $K$.

3.  Avec ces petits nombres, Ève pourrait retrouver la clé privée. Expliquer comment, puis pourquoi c’est impossible en pratique avec un vrai RSA.

    ??? pouce "Coup de pouce"

        Avec $n=323$, combien de divisions faut-il essayer pour trouver $p$ et $q$ ? Et avec un $n$ de $600$ chiffres ?

**Partie C — Le faux casier.**

1.  Ève installe un émetteur qui se fait passer pour le casier et envoie à l’application *sa propre* clé publique. Expliquer ce qu’elle peut alors faire. Quel élément, utilisé par HTTPS lors de la poignée de main TLS, permettrait à l’application de déjouer cette attaque ?

??? corrige "Corrigé"

    **Partie A.**

    1.  $79 = \texttt{01001111}$ et $23 = \texttt{00010111}$. Bit à bit : $\texttt{01001111}\ \texttt{\^{}}\ \texttt{00010111} = \texttt{01011000} = \mathbf{88}$. Puis $88\ \texttt{\^{}}\ 23$ : $\texttt{01011000}\ \texttt{\^{}}\ \texttt{00010111} = \texttt{01001111} = \mathbf{79}$. On retrouve le nombre de départ : appliquer deux fois le XOR avec la même clé **annule** l’opération, $(m\ \texttt{\^{}}\ k)\ \texttt{\^{}}\ k = m$.

    2.  `(a)` `k = cle[i % len(cle)]` ; `(b)` `resultat.append(codes[i] ^ k)`.

        ```python
        def chiffrer_xor(codes, cle):
            resultat = []
            for i in range(len(codes)):
                k = cle[i % len(cle)]         # la cle est repetee
                resultat.append(codes[i] ^ k)
            return resultat
        ```

        Pour `i` $= 0, 1, 2, 3, 4, 5, 6$, l’indice `i % 3` vaut $0, 1, 2, 0, 1, 2, 0$ : la clé est reprise depuis le début tous les trois caractères.

    3.  Chaque code chiffré vaut `codes[i] ^ k` ; le casier calcule `(codes[i] ^ k) ^ k`, qui redonne `codes[i]` (question 1), avec le *même* `k` puisque l’indice `i % len(cle)` est le même. Donc `chiffrer_xor(chiffrer_xor(m, cle), cle)` vaut `m`. C’est un chiffrement **symétrique** : la **même** clé, partagée par l’application et le casier, sert à chiffrer et à déchiffrer.

    4.  Si $c = m\ \texttt{\^{}}\ k$, alors $c\ \texttt{\^{}}\ m = (m\ \texttt{\^{}}\ k)\ \texttt{\^{}}\ m = k$ (le XOR est commutatif, et $m$ s’annule avec lui-même). Ève fait donc le XOR entre le chiffré et le clair connu :

        - $88\ \texttt{\^{}}\ 79$ : $\texttt{01011000}\ \texttt{\^{}}\ \texttt{01001111} = \texttt{00010111} = 23$ ;

        - $80\ \texttt{\^{}}\ 85$ : $\texttt{01010000}\ \texttt{\^{}}\ \texttt{01010101} = \texttt{00000101} = 5$ ;

        - $124\ \texttt{\^{}}\ 86$ : $\texttt{01111100}\ \texttt{\^{}}\ \texttt{01010110} = \texttt{00101010} = 42$.

        Elle retrouve la clé `[23, 5, 42]`.

    5.  On applique la question 4 à chaque position : le nombre d’indice `i` de la clé vaut `intercepte[i] ^ debut_connu[i]`.

        ```python
        def retrouver_cle(intercepte, debut_connu, n):
            return [intercepte[i] ^ debut_connu[i] for i in range(n)]
        ```

        Avec `intercepte = [88, 80, 124, 69, 64, 26, 32]`, l’appel `retrouver_cle(intercepte, [79, 85, 86], 3)` renvoie `[23, 5, 42]`. Ève appelle ensuite `chiffrer_xor(intercepte, [23, 5, 42])`, qui renvoie `[79, 85, 86, 82, 69, 48, 55]`, c’est-à-dire `"OUVRE07"` (vérifié par exécution).

    6.  Le masque jetable exige une clé **aussi longue que le message**, **aléatoire** et **utilisée une seule fois**. Ici la clé est **courte** et **répétée** dans le message, et surtout **réutilisée** pour tous les messages : connaître un morceau du clair (le début `"OUVRE"`, toujours le même) suffit à retrouver la clé, donc à lire — et à fabriquer — tous les messages.

    **Partie B.**

    1.  $n = 17\times 19 = 323$ et $\varphi = 16\times 18 = 288$. Comme $288 = 2^{5}\times 3^{2}$ n’est pas divisible par le nombre premier $5$, $e = 5$ est bien premier avec $\varphi$. Enfin $5\times 173 = 865 = 3\times 288 + 1$, donc $5\times 173\equiv 1\ [288]$ : $d = 173$ est l’inverse modulaire de $e$ (en Python, `pow(5, -1, 288)` renvoie `173`). Clé publique : $\mathbf{(5,\,323)}$ ; clé privée : $\mathbf{(173,\,323)}$.

    2.  L’application chiffre avec la clé **publique** du casier : `C = pow(42, 5, 323)`, qui vaut $264$. Le casier déchiffre avec sa clé **privée** : `K = pow(264, 173, 323)`, qui redonne $42$ (vérifié par exécution).

    3.  Ève connaît la clé publique $(5, 323)$. Elle cherche un diviseur de $323$ en essayant $2, 3, 5, \dots$ : elle trouve vite $323 = 17\times 19$, calcule $\varphi = 288$, puis $d = 173$ comme le casier. Avec un vrai RSA, $n$ est le produit de deux nombres premiers de plus de $150$ chiffres : aucun algorithme connu ne sait **factoriser** un tel nombre en un temps raisonnable. La sécurité de RSA repose sur cette difficulté.

    **Partie C.**

    1.  L’application, croyant parler au casier, chiffre la nouvelle clé avec la clé publique d’**Ève** : Ève la déchiffre avec sa clé privée, peut lire les messages, et même les retransmettre au vrai casier en les rechiffrant avec la vraie clé publique (attaque de l’**homme du milieu**). Il manque l’**authentification** du casier. HTTPS la règle avec un **certificat** : le serveur présente sa clé publique dans un certificat signé par une **autorité de certification** de confiance, que le client vérifie avant d’envoyer la clé symétrique. Un faux casier ne pourrait pas présenter un certificat valide pour sa propre clé.

### Critiquer une réponse d’IA

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 17</span> — Des clés RSA fabriquées par un assistant d’IA <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> { #ex-12-17 }

Un élève demande à un assistant d’IA : « Écris un programme Python qui fabrique une paire de clés RSA à partir de deux nombres premiers `p` et `q`, puis qui chiffre et déchiffre un entier. » Voici la réponse obtenue :

```python
p, q = 5, 11
n = p * q                  # module public
e = 3                      # exposant public, premier avec (p-1)(q-1)
d = pow(e, -1, n)          # exposant prive : inverse modulaire de e

def chiffrer(M):
    return pow(M, e, n)    # C = M^e mod n

def dechiffrer(C):
    return pow(C, d, n)    # M = C^d mod n
```

*« La clé publique est `(e, n)`, la clé privée `(d, n)` ; `pow(e, -1, n)` calcule l’inverse modulaire de `e`, exactement comme dans le cours. »*

1.  La réponse est-elle correcte ? La vérifier à la main (ou en console) avec le message $M = 7$ : calculer $C =$ `chiffrer(7)`, puis `dechiffrer(C)`. Retrouve-t-on $7$ ?

2.  Localiser et corriger l’erreur (on donnera la valeur correcte de $d$).

    ??? pouce "Coup de pouce"

        Relire l’étape 3 de RSA dans le cours : modulo *quel* nombre calcule-t-on l’inverse de $e$ ?

3.  Quelle vérification simple, faite avant de faire confiance à la réponse, aurait suffi à détecter l’erreur ?

??? corrige "Corrigé"

    1.  **Non.** Avec $n = 55$ : `d = pow(3, -1, 55)` vaut $37$ (car $3 \times 37 = 111 = 2\times 55 + 1$). Puis `chiffrer(7)` $= 7^{3} \bmod 55 = 343 \bmod 55 = 13$, et `dechiffrer(13)` $= 13^{37} \bmod 55 = \mathbf{18}$ (sortie réelle), et non $7$ : le déchiffrement **ne redonne pas le message**.

    2.  L’erreur : l’inverse modulaire de $e$ doit être pris **modulo $\varphi = (p-1)(q-1)$**, pas modulo $n$ (cours : « *Calculer $d$, l’inverse modulaire de $e$ : le nombre tel que $e \times d \equiv 1\ [\varphi]$* »). Lignes corrigées :

        ```python
        phi = (p - 1) * (q - 1)    # 40
        d = pow(e, -1, phi)        # 27, car 3 * 27 = 81 = 2 * 40 + 1
        ```

        Avec $d = 27$ : `dechiffrer(13)` $= 13^{27} \bmod 55 = 7$. ✓

    3.  Faire un **aller-retour** sur un petit message : `dechiffrer(chiffrer(7))` doit renvoyer `7`. C’est un test d’une ligne, à faire systématiquement sur tout code de chiffrement — ici sur un exemple assez petit pour qu’on puisse vérifier la réponse à la main ($d = 27$, car $3 \times 27 = 81 = 2 \times 40 + 1$).

### S’entraîner à l’oral

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 18</span> — Expliquer en deux minutes <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-12-18 }

Au Grand Oral comme devant l’examinateur de l’épreuve pratique, il faut savoir **expliquer** une notion clairement, sans notes. Choisir l’un des sujets suivants (ou le tirer au sort) :

1.  Expliquer à un camarade de Première la différence entre chiffrement **symétrique** et chiffrement **asymétrique**.

2.  Expliquer comment **HTTPS** combine les deux types de chiffrement.

3.  Expliquer pourquoi **RSA** est considéré comme sûr alors que la clé publique est connue de tous.

**Préparation (5 min, seul).** Noter au brouillon **trois idées** et **un exemple**, rien de plus, puis retourner la feuille. **Exposé (2 min, chronométré).** Debout, face à un camarade, **sans lire de notes** : tout passe par la parole. **Retour (2 min).** Le camarade pose une question de relance (on peut alors s’aider d’un schéma), remplit la grille ci-dessous et donne un conseil ; puis on échange les rôles. Cette grille reprend les critères d’évaluation du Grand Oral.

??? pouce "Coup de pouce"

    Structurer chaque explication en trois temps : une **définition** en une phrase, un **exemple** petit et concret déroulé à voix haute, puis le **piège** (l’erreur que l’auditeur risque de faire). Finir par une phrase qui répond à la question posée. Une image aide beaucoup à l’oral (un coffre et sa clé, un cadenas ouvert que l’on distribue) ; dire ensuite précisément ce que représente chaque objet. Sujet 3 : qu’est-ce qui est facile à calculer, et qu’est-ce qui est difficile ?

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

    - **Symétrique** : une seule clé secrète, partagée, sert à chiffrer et à déchiffrer (César, XOR, AES) ; c’est rapide, mais il faut transmettre la clé sans qu’on l’intercepte.

    - **Asymétrique** : deux clés liées ; la clé **publique**, diffusée, sert à chiffrer ; la clé **privée**, gardée secrète, sert à déchiffrer.

    - Exemple : Alice publie sa clé publique ; Bob chiffre son message avec ; seule Alice peut le déchiffrer.

    - Piège : l’asymétrique est beaucoup plus lent ; on ne l’utilise pas pour chiffrer de gros volumes.

    **Sujet 2.**

    - Au début de la connexion (poignée de main TLS), le serveur envoie son **certificat** : sa clé publique, garantie par une autorité de certification.

    - Le navigateur s’en sert pour transmettre de façon sûre une **clé de session** (symétrique), que seul le serveur peut retrouver.

    - Toute la suite de l’échange est chiffrée en **symétrique** avec cette clé de session : c’est rapide.

    - Piège : sans vérification du certificat, une attaque de l’homme du milieu est possible ; HTTPS protège le transport, pas l’honnêteté du site.

    **Sujet 3.**

    - Clé publique $(e, n)$ avec $n = p \times q$, où $p$ et $q$ sont de grands nombres premiers gardés secrets.

    - Calculer la clé privée $d$ demande $\varphi = (p - 1)(q - 1)$, donc de connaître $p$ et $q$, donc de **factoriser** $n$.

    - Multiplier deux nombres est facile ; factoriser un nombre de plusieurs centaines de chiffres est hors de portée : on ne connaît pas d’algorithme efficace.

    - Exemple : $n = 55 = 5 \times 11$ se factorise de tête ; la sécurité repose sur la **taille** des clés, pas sur le secret de la méthode.
