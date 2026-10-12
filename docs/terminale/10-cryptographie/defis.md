# Défis Advent of Code

<p class="sous-titre">Cryptographie</p>

## <span class="etiquette">Défi 1</span> Combo Breaker

*la carte d’hôtel — Diffie-Hellman et exponentiation modulaire*

<p class="infos-activite">Jour 25</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/10-defi-aoc-2020-25){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-10-defi-aoc-2020-25.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/25 ](https://adventofcode.com/2020/day/25 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (lien ci-dessus) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

*Ce défi réinvestit l’échange de clés de Diffie-Hellman et l’exponentiation modulaire vus dans ce chapitre : la carte et la porte appliquent exactement ce protocole, et l’on joue ici le rôle de l’espion.*

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|  |  |  |  |
|:---|:---|:---|:---|
| handshake | poignée de main (échange initial) | subject number | nombre de départ (base) |
| loop size | nombre de tours de boucle (secret) | remainder | reste (de la division) |
| public key | clé publique | encryption key | clé de chiffrement (secrète) |
| eavesdrop | écouter en cachette | reverse-engineer | retrouver par analyse |
| trial and error | essais successifs | card / door | carte / porte |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Dernier jour : votre carte de chambre ne fonctionne pas, et l’accueil est fermé. La carte et la porte s’authentifient par un petit protocole cryptographique ; en écoutant ce qu’elles s’échangent, vous allez retrouver leur clé secrète. Le fichier contient les deux nombres que vous avez interceptés.

    **Ce qu’il faut faire.**

    - Transformer un nombre $s$ avec $n$ tours : partir de $1$ puis, $n$ fois, multiplier par $s$ et prendre le reste de la division par $20201227$. Autrement dit, calculer $s^n \bmod 20201227$.

    - La carte et la porte ont chacune un nombre de tours secret. Chacune publie la transformée de $7$ avec son secret : sa clé publique. Le fichier contient les deux clés publiques (carte, puis porte).

    - La clé de chiffrement est la transformée de la clé publique de la porte avec le secret de la carte ; c’est aussi la transformée de la clé publique de la carte avec le secret de la porte.

    - Réponse : la clé de chiffrement.

### <span class="exo-num">Exercice 1</span> — Vérifier sa compréhension <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-cryptographie-aoc-1-1 }

1.  Que vaut la transformée de $7$ avec $0$ tour ? avec $1$ tour ?

2.  Faut-il retrouver les deux secrets pour calculer la clé ?

3.  Pourquoi est-on sûr qu’une recherche « essayer $n = 1, 2, 3\dots$ » finira par trouver le secret ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-cryptographie-aoc-1-2 }

Transformer à la main le nombre `7` avec 1, 2 puis 3 tours de boucle (le modulo ne sert pas encore). À partir de combien de tours le reste de la division modifie-t-il le résultat ?

Dans un exemple inventé, la carte utilise `10` tours et la porte `17` tours. Avec la calculatrice ou Python, vérifier que les clés publiques sont `19859298` (carte) et `11869933` (porte), puis que la clé de chiffrement vaut `1455220`, qu’on la calcule du côté de la carte ou de la porte.

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Transformer <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-cryptographie-aoc-1-3 }

Écrire une fonction `transformer(sujet, nb_tours)` qui applique la transformation de l’énoncé. Vérifier les valeurs de l’exemple précédent.

??? pouce "Coup de pouce"

    Une boucle `for` de `nb_tours` tours, avec `valeur = valeur * sujet % 20201227`. Python fournit aussi `pow(sujet, nb_tours, 20201227)`, beaucoup plus rapide (lire l’encadré).

### <span class="exo-num">Exercice 4</span> — Retrouver un secret <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-cryptographie-aoc-1-4 }

Écrire une fonction `nb_tours(cle_publique)` qui retrouve le nombre de tours secret à partir d’une clé publique. Tester : `nb_tours(19859298)` doit renvoyer `10`. Calculer ensuite la clé de chiffrement de vos données.

??? pouce "Coup de pouce"

    Ne pas appeler `transformer(7, n)` pour `n = 1, 2, 3...` : chaque appel recommencerait tout depuis le début. Faire **une seule** boucle `while` qui multiplie la valeur par 7 à chaque tour et compte les tours, jusqu’à tomber sur la clé publique.

??? pouce "Coup de pouce 2 (début de solution)"

    Il suffit de retrouver le secret d’**un seul** des deux appareils : la clé vaut `transformer(cle_publique_porte, tours_carte)`. Le nombre de tours peut dépasser plusieurs millions : c’est normal.

## Partie 2

Il n’y a pas de deuxième énigme ce jour-là : la seconde étoile est offerte quand les 49 autres étoiles de l’année ont été obtenues.

!!! encadre "Outil Python : mesurer un temps (time.perf_counter)"

    `perf_counter()` renvoie un temps en secondes, très précis ; la différence entre deux appels donne la durée d’un calcul.

    ```python
    from time import perf_counter
    debut = perf_counter()
    n = nb_tours(19859298)                 # le calcul a chronometrer
    duree = perf_counter() - debut
    print(f"{n} tours en {duree:.6f} s")   # 6 chiffres apres la virgule
    ```

    **Intérêt.** En divisant le nombre de tours par la durée, on obtient une vitesse (tours par seconde) qui permet d’extrapoler. Question : chronométrer `nb_tours` sur vos deux clés publiques ; combien de tours par seconde votre programme fait-il ?

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 5</span> — Défi : pourquoi est-ce sûr ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-cryptographie-aoc-1-5 }

Les vrais protocoles utilisent un modulo de plus de 600 chiffres. Mesurer la vitesse de votre recherche du nombre de tours (encadré ci-dessus). Pour un modulo d’environ $2\times 10^7$, la recherche essaie au pire $2 \times 10^7$ valeurs ; estimer le temps qu’elle prendrait pour un modulo de l’ordre de $10^{20}$, puis $10^{600}$. Expliquer pourquoi l’espion est battu alors que la carte et la porte calculent vite.

??? pouce "Coup de pouce"

    La recherche essaie, au pire, toutes les valeurs du nombre de tours, jusqu’au modulo. La carte, elle, n’a qu’à calculer une puissance, ce que `pow` fait en un nombre d’étapes proportionnel au nombre de *chiffres* de l’exposant.

## Rappel : l’échange de clés de Diffie-Hellman

!!! encadre "Se mettre d’accord sur un secret en parlant en public (chapitre 10)"

    La transformation de l’énoncé calcule $\text{sujet}^{\,n} \bmod p$ avec $p = 20201227$. C’est le protocole de **Diffie et Hellman** (1976) vu en cours. Un autre exemple avec de petits nombres : $p = 29$ et $g = 2$, connus de tous.

    - Alice choisit en secret $a = 5$ et envoie $A = 2^5 \bmod 29 = 3$.

    - Bob choisit en secret $b = 11$ et envoie $B = 2^{11} \bmod 29 = 18$.

    - Alice calcule $B^a \bmod 29 = 18^5 \bmod 29 = 15$ ; Bob calcule $A^b \bmod 29 = 3^{11} \bmod 29 = 15$.

    Ils obtiennent le même secret car $(g^b)^a = (g^a)^b = g^{ab}$. Un espion qui a entendu $3$ et $18$ doit retrouver $a$ ou $b$ : c’est le problème du **logarithme discret**.

    **Pourquoi est-ce difficile ?** Les puissances successives de $2$ modulo $29$ semblent tirées au hasard : $2, 4, 8, 16, 3, 6, 12, 24, 19, 9, 18, 7\dots$ Aucune régularité ne permet de « remonter » d’un résultat à l’exposant : la méthode naïve essaie les exposants un à un, et même les meilleures méthodes connues deviennent beaucoup trop lentes quand $p$ est très grand. À l’inverse, calculer une puissance est rapide : en Python, `pow(a, b, m)` calcule $a^b \bmod m$ par exponentiation rapide, sans jamais manipuler le nombre géant $a^b$.

## Approfondissement

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Approfondissement 1 : programmer l’exponentiation rapide <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-cryptographie-aoc-1-6 }

La fonction `pow(a, b, m)` de Python n’effectue pas $b$ multiplications : elle utilise l’**exponentiation rapide**, fondée sur $a^{b} = \left(a^{b/2}\right)^2$ si $b$ est pair et $a^{b} = \left(a^{(b-1)/2}\right)^2 \times a$ si $b$ est impair.

1.  À la main : calculer $2^{11} \bmod 29$ en n’utilisant que des carrés et des multiplications par $2$ (partir de $2^{11} = (2^{5})^{2} \times 2$). Combien de multiplications a-t-on faites ? Combien en fallait-il avec la méthode « une multiplication par tour » ?

2.  Écrire une fonction **récursive** `puissance_rapide(a, b, m)` qui renvoie $a^b \bmod m$. La comparer à `pow(a, b, m)` sur de nombreuses valeurs.

    ??? pouce "Coup de pouce"

        Cas de base : $b = 0$, le résultat est $1$. Sinon, calculer **une seule fois** `puissance_rapide(a, b // 2, m)`, l’élever au carré modulo `m`, puis multiplier par `a` si `b` est impair.

    ??? pouce "Coup de pouce 2 (début de solution)"

        Appeler deux fois la fonction sur `b // 2` (au lieu de stocker le résultat dans une variable) redonnerait une complexité linéaire : bien garder le résultat dans une variable `moitie`.

3.  Combien d’appels récursifs pour $b = 10^{600}$ ? Quelle est la complexité en fonction de $b$ ?

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 2 : le logarithme discret plus vite (pas de bébé, pas de géant) <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-cryptographie-aoc-1-7 }

On cherche $n$ tel que $g^n \bmod p = c$, avec $0 \leq n < p$. On pose $m$ un entier tel que $m^2 > p$ et on écrit $n = i \times m + j$ avec $0 \leq i, j < m$.

- **Pas de bébé** : on range dans un dictionnaire les $m$ valeurs $g^j \bmod p$ (clé) avec leur exposant $j$ (valeur).

- **Pas de géant** : on calcule $c$, puis $c \times g^{-m}$, $c \times g^{-2m}$… (modulo $p$), jusqu’à tomber sur une clé du dictionnaire. Si $c \times g^{-im} = g^j$, alors $c = g^{im + j}$.

On admet que, $p$ étant premier, $g^{p-1} \bmod p = 1$ (petit théorème de Fermat) : multiplier par $g^{-m}$ revient donc à multiplier par $g^{p-1-m} \bmod p$.

1.  À la main, avec $p = 29$, $g = 2$ et $m = 6$ : écrire le dictionnaire des pas de bébé. Retrouver le secret de Bob à partir de sa clé publique $18$, sachant que $2^{22} \bmod 29 = 5$.

2.  Écrire `log_discret(g, cible, p)` et vérifier qu’elle retrouve les nombres de tours de l’exemple du défi, puis de vos données.

    ??? pouce "Coup de pouce"

        `m = int(p ** 0.5) + 1` ; une boucle `for` remplit le dictionnaire `bebes` ; une boucle `while` fait les pas de géant tant que la valeur courante n’est pas une clé de `bebes` (et que `i < m`).

    ??? pouce "Coup de pouce 2 (début de solution)"

        Calculer une fois pour toutes `facteur = pow(g, p - 1 - m, p)` ; à chaque pas de géant, `geant = geant * facteur % p`. À la sortie, la réponse est `i * m + bebes[geant]`.

3.  Combien d’opérations pour $p \approx 2 \times 10^7$ ? Et pour $p \approx 10^{600}$ ? Cela remet-il en cause la sécurité du protocole ? Quelle quantité de mémoire faut-il ?

## <span class="etiquette">Défi 2</span> Shuttle Search

*les navettes — modulo et efficacité*

<p class="infos-activite">Jour 13</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/10-defi-aoc-2020-13){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-10-defi-aoc-2020-13.zip){ .md-button }

!!! consignes "Consignes"

    - L’énoncé se lit sur le site (voir le QR code) : [https://adventofcode.com/2020/day/13 ](https://adventofcode.com/2020/day/13 ). On peut le lire en anglais ou le faire traduire par le navigateur (clic droit, *Traduire en français*).

    - Avec un compte (GitHub, Google…), le bouton *get your puzzle input* donne **votre** fichier de données, à enregistrer sous `input.txt` à côté de votre programme. Sans compte : le dossier du défi (lien ci-dessus) contient des **données maison** (`input.txt`) et le programme `verifier.py`, qui dit si vos réponses sont justes.

    - La partie 2 n’apparaît qu’une fois la partie 1 validée sur le site.

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> L’IA peut aider à comprendre un message d’erreur, jamais à écrire la solution.

*Ce défi réinvestit l’arithmétique modulaire de ce chapitre : le reste `%` dans la partie 1, puis, en approfondissement, l’inverse modulaire `pow(a, -1, m)` rencontré avec le chiffrement affine et RSA.*

## Lire l’énoncé

Vocabulaire utile pour lire le texte original :

|                |              |            |                      |
|:---------------|:-------------|:-----------|:---------------------|
| shuttle bus    | navette      | timestamp  | instant (en minutes) |
| depart         | partir       | earliest   | le plus tôt possible |
| out of service | hors service | ID         | identifiant (numéro) |
| offset         | décalage     | subsequent | suivant, consécutif  |

!!! encadre "Résumé de l’énoncé (partie 1)"

    **Contexte.** Arrivé au port, vous devez rejoindre l’aéroport en navette. Chaque navette fait une boucle de durée fixe et repasse donc régulièrement au port ; son numéro est justement la durée de sa boucle, en minutes. Le fichier contient vos notes : l’heure à laquelle vous serez prêt, et la liste des navettes de la compagnie.

    **Ce qu’il faut faire.**

    - Ligne 1 : l’instant $a$ (en minutes) à partir duquel vous pouvez partir. Ligne 2 : les numéros des navettes séparés par des virgules ; un `x` désigne une navette hors service, à ignorer.

    - Toutes les navettes sont parties ensemble à l’instant 0 : la navette numéro $b$ part donc aux instants $0$, $b$, $2b$, $3b$… autrement dit aux multiples de $b$.

    - Il faut trouver la navette qui part le plus tôt à partir de l’instant $a$ (un départ à l’instant $a$ lui-même convient). La réponse est son numéro multiplié par le nombre de minutes d’attente.

### <span class="exo-num">Exercice 1</span> — Comprendre ce qui est demandé <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-cryptographie-aoc-2-1 }

Questions de vérification, à traiter sur le cahier :

1.  Si $a$ est un multiple de $b$, combien de minutes attend-on la navette $b$ ?

2.  Avec $a = 30$, à quel instant part la navette 7, et combien attend-on ?

3.  Les `x` jouent-ils un rôle dans la partie 1 ?

### <span class="exo-num">Exercice 2</span> — À la main, sur un petit exemple <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-cryptographie-aoc-2-2 }

On considère le fichier (inventé) suivant :

```console
96
5,x,7,x,x,11
```

Pour chaque navette, calculer le premier départ à partir de l’instant 96 et l’attente correspondante. Vérification : la réponse est `14`.

## Programmer la partie 1

### <span class="exo-num">Exercice 3</span> — Lire le fichier <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-cryptographie-aoc-2-3 }

Écrire une fonction `lire_notes(nom_fichier)` qui renvoie l’instant d’arrivée et la liste des numéros des navettes en service (sans les `x`).

??? pouce "Coup de pouce"

    `ligne.split(",")` découpe la seconde ligne ; on ne garde que les morceaux différents de `"x"`.

### <span class="exo-num">Exercice 4</span> — L’attente, avec un modulo <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-cryptographie-aoc-2-4 }

Écrire une fonction `attente(arrivee, numero)` qui renvoie le nombre de minutes à attendre la navette `numero`, **sans boucle**. En déduire la réponse. Tester sur l’exemple du défi, puis sur vos données.

??? pouce "Coup de pouce"

    `arrivee % numero` donne le temps écoulé depuis le dernier départ. Attention au cas où il vaut `0` : on part tout de suite.

## Partie 2

Une fois la partie 1 validée, lire la suite de l’énoncé sur le site.

!!! encadre "Résumé de la partie 2 (à lire après avoir validé la partie 1)"

    La compagnie propose un concours : trouver le moment où les navettes partent les unes après les autres, minute après minute, dans l’ordre de la liste.

    - La première ligne ne sert plus. Les positions dans la liste sont numérotées à partir de 0, `x` compris ; un `x` n’impose aucune condition.

    - Trouver le plus petit instant $t$ tel que la navette en position $i$ parte exactement à l’instant $t + i$, pour toutes les navettes en service.

### <span class="exo-num">Exercice 5</span> — Comprendre la condition <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-cryptographie-aoc-2-5 }

Traduire la condition sur une navette de numéro $b$ placée en position $i$ par une égalité avec `%`. Sur l’exemple du défi, on doit trouver $t = 215$ : le vérifier pour chacune des trois navettes.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 6</span> — Défi : la partie 2 sur vos données <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-cryptographie-aoc-2-6 }

L’énoncé prévient que la réponse dépasse $10^{14}$ : tester tous les instants un par un prendrait des années. Lire la section suivante, puis écrire une fonction `premier_instant(navettes)` qui suit cette méthode. Vérifier sur l’exemple du défi et sur ceux de l’énoncé avant vos données.

??? pouce "Coup de pouce"

    On traite les navettes une par une. Une fois une navette satisfaite, on ne regarde plus que des instants qui la satisfont encore.

??? pouce "Coup de pouce 2 (début de solution)"

    Deux variables suffisent : `t` (candidat actuel) et `pas`. Pour chaque navette, on ajoute `pas` à `t` tant que la condition n’est pas vérifiée, puis on met à jour `pas`.

## Pour y arriver : synchroniser des périodes <span class="horsprog">au-delà du programme</span>

!!! encadre "Recherche à pas croissant"

    On cherche $t$ tel que $t \,\%\, 5 = 0$, $(t+2) \,\%\, 7 = 0$ et $(t+5) \,\%\, 11 = 0$ (exemple du défi).

    **Idée.** Si $t$ convient pour la navette 5, alors $t + 5$, $t + 10$… conviennent aussi : la condition est *périodique*. Si $t$ convient pour 5 *et* 7, alors $t + 35$, $t + 70$… conviennent encore pour les deux, puisque 35 est un multiple de 5 et de 7.

    **Méthode.** On part de $t = 0$ avec un pas de 1. Pour chaque navette, on avance de *pas* en *pas* jusqu’à ce qu’elle soit satisfaite, puis on multiplie le pas par son numéro : le pas est toujours le produit des périodes déjà satisfaites.

    - navette 5 : $t = 0$ convient tout de suite ; le pas devient $5$ ;

    - navette 7 : on teste $0$, puis $5$ ; $5 + 2 = 7$ est divisible par 7 ; le pas devient $5 \times 7 = 35$ ;

    - navette 11 : on teste $5, 40, 75, 110, 145, 180, 215$ ; $215 + 5 = 220 = 11 \times 20$. Donc $t = 215$.

    Il a suffi de 7 essais au lieu de 215. Pour chaque navette, on fait au plus « numéro » essais : quelques centaines en tout, même si $t$ dépasse $10^{14}$.

    **Pourquoi ça marche.** Les numéros des navettes sont premiers entre eux (ici ce sont même des nombres premiers) : en avançant de pas en pas, on finit toujours par satisfaire la nouvelle navette en moins de « numéro » essais. Si les numéros avaient un diviseur commun, il faudrait prendre leur PPCM.

    **Pour aller plus loin.** En mathématiques, ce problème est résolu par le *théorème des restes chinois* : si $n_1, \dots, n_k$ sont premiers entre eux deux à deux, il existe une unique solution $t$ entre $0$ et $n_1 \times \dots \times n_k - 1$ à un système de conditions $t \,\%\, n_j = r_j$. La méthode ci-dessus est une façon simple de la calculer.

## Approfondissement

!!! encadre "Rappel du cours : puissance modulaire et inverse (pow(a, b, m))"

    Comme dans le cours (chiffrement affine, RSA), `pow(a, b, m)` calcule $a^b \bmod m$ sans jamais former le très grand nombre $a^b$. Avec l’exposant $-1$, `pow(a, -1, m)` renvoie l’**inverse de $a$ modulo $m$**, c’est-à-dire l’entier $y$ entre $0$ et $m-1$ tel que $a \times y \bmod m = 1$ (Python 3.8 ou plus récent). Il n’existe que si $a$ et $m$ sont premiers entre eux.

    ```python
    print(pow(3, 4))               # 81 : comme 3 ** 4
    print(pow(3, 4, 7))            # 4 : 81 % 7, sans jamais former de tres grand nombre
    print(pow(6, -1, 7))           # 6 : inverse de 6 modulo 7 (6 * 6 = 36 = 5 * 7 + 1)
    print(6 * pow(6, -1, 7) % 7)   # 1
    ```

    **Intérêt.** L’inverse modulaire se calcule en un nombre d’étapes proportionnel au nombre de chiffres (algorithme d’Euclide étendu), même pour des nombres immenses ; le chercher en essayant $y = 1, 2, 3\dots$ prendrait jusqu’à $m$ essais.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 7</span> — Approfondissement 1 : la formule des restes chinois <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-cryptographie-aoc-2-7 }

La section précédente cite le théorème des restes chinois. Il donne aussi une **formule** : pour le système $t \,\%\, n_m = r_m$ ($m = 1, \dots, k$), avec des $n_m$ premiers entre eux deux à deux, on pose $N = n_1 \times \dots \times n_k$, $N_m = N / n_m$ et $y_m$ l’inverse de $N_m$ modulo $n_m$. Alors $$t = \Big(\sum_{m} r_m \, N_m \, y_m\Big) \bmod N.$$

1.  Recopier et exécuter le code de l’encadré. Que se passe-t-il avec `pow(4, -1, 6)` ? Pourquoi ?

2.  Pour une navette de numéro $b$ en position $i$, quel reste $r$ doit avoir $t$ modulo $b$ ? Sur l’exemple du défi (`5,x,7,x,x,11`), calculer pour chaque navette $r_m$, $N_m$ et $y_m$, puis $t$. On doit retrouver `215`.

3.  Vérifier sur l’exemple que le terme associé à la navette 7 est un multiple de 5 et de 11, et qu’il a le bon reste modulo 7. En déduire pourquoi la formule fonctionne.

4.  Écrire une fonction `restes_chinois(navettes)` et la comparer à `premier_instant` : nombre d’opérations, lisibilité.

    ??? pouce "Coup de pouce"

        `(-i) % b` donne un reste compris entre 0 et `b - 1`, même quand `-i` est négatif.

    ??? pouce "Coup de pouce 2 (début de solution)"

        Une première boucle calcule le produit $N$ ; une seconde ajoute `r * (N // b) * pow(N // b, -1, b)` pour chaque navette ; on renvoie le total modulo $N$.
