# TP et projets

<p class="sous-titre">Les bases de la programmation Python</p>

## <span class="etiquette">TP</span> Le nombre mystère, édition de luxe

*un vrai petit jeu, construit fonction par fonction*

<p class="infos-activite">Durée : 2 à 3 h (deux séances) · Sur machine, seul ou par deux</p>

!!! encadre "But du TP"

    Programmer, étape par étape, un **jeu complet** dans la console : l’ordinateur choisit un nombre au hasard, le joueur doit le deviner en un nombre limité d’essais, avec des **indices** (« trop grand », « chaud », « froid »), trois **niveaux**, un **score** et la possibilité de **rejouer**. En défi, on renverse les rôles : c’est l’ordinateur qui devine, et on **prouve** qu’il gagne toujours. Le TP réinvestit tout le chapitre : séquence, affectation, conditionnelles, boucles `for` et `while`, fonctions spécifiées et testées.

!!! consignes "Consignes"

    - Tout le code s’écrit dans **un seul fichier** `nombre_mystere.py`, que l’on complète au fil des exercices et que l’on **lance après chaque fonction**.

    - Les réponses aux questions (sans <span class="run" title="À programmer et tester sur machine">▶</span> ) s’écrivent sur le cahier.

    - <span class="run" title="À programmer et tester sur machine">▶</span> signale ce qui est *à programmer et tester*. Chaque fonction reçoit une **docstring** (rôle, et s’il y a lieu précondition et postcondition). Les tests `assert` donnés sont recopiés **en bas du fichier** : s’ils passent, rien ne s’affiche.

    - **Pas de liste dans ce TP** : quand il y a plusieurs choses à montrer, on fait des `print` successifs.

    - Niveau : ★ échauffement, ★★ classique (niveau bac), ★★★ défi ; les *coups de pouce* et les *corrigés* se déplient sous chaque exercice.

    - Usage de l’IA, indiqué sur chaque exercice : <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> aucune ; <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> en appui (déboguer, reformuler, vérifier ; la réponse finale est écrite et comprise par vous) ; <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> l’exercice s’appuie sur une réponse d’IA. Voir la [charte d’usage de l’IA](../charte.md).

## Prise en main : comparer et contrôler

Une partie se joue ainsi : l’ordinateur pense à un nombre `secret` ; le joueur fait une `proposition` ; l’ordinateur répond `"trop petit"`, `"trop grand"` ou `"gagne"`. On commence par les deux briques les plus simples.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 1</span> — La réponse de l’ordinateur <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-01-les-bases-de-la-programmation-python-tp-1-1 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire la fonction `comparer(proposition, secret)` qui renvoie la chaîne `"trop petit"`, `"trop grand"` ou `"gagne"`. Elle **renvoie** la réponse (`return`), elle ne l’affiche pas.

```python
assert comparer(30, 42) == "trop petit"
assert comparer(50, 42) == "trop grand"
assert comparer(42, 42) == "gagne"
```

Pourquoi est-il préférable de *renvoyer* la réponse plutôt que de l’*afficher* ?

??? corrige "Corrigé"

    |  |  |
    |:---|:---|
    | **Ancrage BO (1re)** | constructions élémentaires (séquence, affectation, conditionnelles, boucles bornées et non bornées, appels de fonction) ; spécification (docstring, précondition par `assert`) ; jeux de tests ; terminaison par un variant. |
    | **Code** | tout le code ci-dessous forme **un seul fichier** `nombre_mystere.py`, exécuté avec `python3` : tous les `assert` passent, et une partie complète a été jouée en simulant les saisies (sorties reproduites telles quelles). |
    | **Contrainte** | aucune liste ni aucun tuple (non vus à ce stade) : les affichages multiples sont des `print` successifs, et chaque fonction renvoie **une seule** valeur (d’où `borne_max` et `essais_autorises` séparées). |

    - Testées par `assert` : `comparer`, `est_dans_intervalle`, `ecart`, `indice`, `points`, `borne_max`, `essais_autorises`, `essais_ordinateur`, `pire_cas`, `nb_moities`. Non testables ainsi : `partie`, `afficher_menu`, `demander_niveau`, `ordinateur_devine`, `jouer` (elles lisent le clavier ou affichent) : on les essaie à la main.

    - Test révélateur d’une erreur : réponse personnelle (exemples typiques : `assert points(1, 7) == 100` qui échoue quand le cas « premier coup » est placé après la formule générale ; `assert indice(39, 42) == "brulant"` qui révèle un écart négatif).

    - Pourquoi 7 essais suffisent : chaque essai raté élimine la proposition et **au moins la moitié** des candidats restants ; de 100 candidats on passe à au plus 50, 25, 12, 6, 3, 1 : après 6 essais ratés il reste au plus un nombre, que le 7<sup>e</sup> essai trouve.

    ```python
    import random

    def comparer(proposition, secret):
        """Renvoie "trop petit", "trop grand" ou "gagne"."""
        if proposition < secret:
            return "trop petit"
        elif proposition > secret:
            return "trop grand"
        else:
            return "gagne"
    ```

    Une réponse *renvoyée* est **réutilisable** (`partie`, puis `essais_ordinateur` s’en servent) et **testable** par `assert` ; une réponse affichée est perdue pour le programme.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 2</span> — Une proposition dans les clous <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-01-les-bases-de-la-programmation-python-tp-1-2 }

1.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire `est_dans_intervalle(n, mini, maxi)` qui renvoie `True` si `n` est compris entre `mini` et `maxi` (bornes **incluses**), `False` sinon.

2.  Écrire vous-même un **jeu de tests** d’au moins cinq `assert` pour `mini = 1` et `maxi = 100`. Quels cas **limites** ne faut-il surtout pas oublier ?

```text
>>> est_dans_intervalle(57, 1, 100)
True
>>> est_dans_intervalle(0, 1, 100)
False
```

??? corrige "Corrigé"

    ```python
    def est_dans_intervalle(n, mini, maxi):
        """Renvoie True si mini <= n <= maxi (bornes incluses), False sinon."""
        return n >= mini and n <= maxi

    assert est_dans_intervalle(57, 1, 100) == True
    assert est_dans_intervalle(1, 1, 100) == True      # borne basse
    assert est_dans_intervalle(100, 1, 100) == True    # borne haute
    assert est_dans_intervalle(0, 1, 100) == False     # juste en dessous
    assert est_dans_intervalle(101, 1, 100) == False   # juste au-dessus
    ```

    Les cas limites indispensables sont les **deux bornes** (`1`, `100`) et leurs **voisins extérieurs** (`0`, `101`) : ce sont eux qui distinguent `>=` de `>`. On accepte aussi la version avec `if …: return True else: return False`.

## Le cœur du jeu : la boucle de partie

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 3</span> — Une première partie <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-les-bases-de-la-programmation-python-tp-1-3 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire, **sans fonction** pour l’instant, un programme qui :

- tire un nombre `secret` entre 1 et 100 avec `random.randint(1, 100)` (ne pas oublier `import random`) ;

- demande une proposition au joueur, **tant qu’**il n’a pas trouvé, et affiche à chaque fois la réponse de `comparer` ;

- compte les essais et affiche à la fin `Bravo, trouve en 6 essai(s) !`

```text
Votre proposition : 50
trop grand
Votre proposition : 25
trop petit
...
```

1.  Pourquoi une boucle `while` et non une boucle `for` ?

2.  Le joueur tape `50` : que vaut `input(...)` ? Que faut-il écrire pour pouvoir le comparer à `secret` ?

3.  Cette boucle a-t-elle un **variant** ? Peut-elle ne jamais s’arrêter ?

??? corrige "Corrigé"

    ```python
    secret = random.randint(1, 100)
    essais = 0
    reponse = ""
    while reponse != "gagne":
        proposition = int(input("Votre proposition : "))
        essais = essais + 1
        reponse = comparer(proposition, secret)
        if reponse != "gagne":
            print(reponse)
    print("Bravo, trouve en", essais, "essai(s) !")
    ```

    **1.** On ne sait pas *à l’avance* combien d’essais seront nécessaires : c’est le cas typique du `while`.  
    **2.** `input` renvoie toujours une **chaîne** (`"50"`) ; il faut `int(input(…))`, sinon la comparaison avec un entier provoque une `TypeError`.  
    **3.** Non : aucune quantité ne décroît forcément, un joueur peut proposer `1` indéfiniment. La boucle ne s’arrête que si le joueur finit par trouver. *Initialiser `reponse = ""`* permet d’entrer une première fois dans la boucle.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 4</span> — Un nombre d’essais limité <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-les-bases-de-la-programmation-python-tp-1-4 }

On transforme ce programme en une fonction `partie(secret, maxi, essais_max)`. Le joueur propose des nombres entre `1` et `maxi` ; il a droit à `essais_max` essais. La fonction **renvoie** le nombre d’essais utilisés s’il a gagné, et `0` s’il a perdu (elle affiche alors le nombre mystère).

1.  <span class="run" title="À programmer et tester sur machine">▶</span> Compléter la fonction. La boucle doit s’arrêter dans **deux** cas : le joueur a trouvé, ou il n’a plus d’essai.0

    ??? pouce "Coup de pouce"

        Avec un booléen `trouve` : la boucle continue tant que `not trouve` *et* qu’il reste des essais. Après la boucle, c’est `trouve` qui dit ce qu’il faut renvoyer.

    ```python
    def partie(secret, maxi, essais_max):
        """Joue une partie. Renvoie le nombre d'essais utilises
        si le joueur gagne, 0 s'il perd."""
        essais = 0
        trouve = False
        while ... and ...:
            proposition = int(input("Votre proposition : "))
            ...
        ...
    ```

2.  <span class="run" title="À programmer et tester sur machine">▶</span> Une proposition **hors limites** (0, 150…) ne doit **pas** être comptée : afficher `Hors limites !` et redemander. Réutiliser `est_dans_intervalle`.

3.  Donner un **variant** de la boucle quand toutes les propositions sont dans les limites. Que devient la terminaison si un joueur tape `0` sans arrêt ? Est-ce grave ?

4.  Pourquoi ne peut-on pas tester `partie` avec des `assert`, comme `comparer` ? Qu’en déduire sur la façon de découper un programme ?

??? corrige "Corrigé"

    ```python
    def partie(secret, maxi, essais_max):
        """Joue une partie. Renvoie le nombre d'essais utilises
        si le joueur gagne, 0 s'il perd."""
        essais = 0
        trouve = False
        while not trouve and essais < essais_max:
            proposition = int(input("Votre proposition : "))
            if not est_dans_intervalle(proposition, 1, maxi):
                print("Hors limites ! Entre 1 et", maxi, "(essai non compte).")
            else:
                essais = essais + 1
                reponse = comparer(proposition, secret)
                if reponse == "gagne":
                    trouve = True
                    print("Bravo, trouve en", essais, "essai(s) !")
                else:
                    print(reponse, "-", indice(proposition, secret),
                          "- il reste", essais_max - essais, "essai(s)")
        if trouve:
            return essais
        print("Perdu ! Le nombre mystere etait", secret)
        return 0
    ```

    (Version finale, avec l’indice de l’exercice 5 ; à ce stade, la ligne `print(reponse)` suffit.)

    **3.** Variant : `essais_max - essais`, entier positif ou nul, qui diminue de 1 à chaque proposition comptée ; la boucle s’arrête au plus tard quand il atteint 0. Si le joueur tape `0` sans arrêt, `essais` ne bouge plus : il n’y a plus de variant et la boucle peut tourner sans fin. Ce n’est pas grave ici (c’est le joueur qui le décide, et `Ctrl + C` l’interrompt), mais il faut savoir le dire : la terminaison n’est garantie *que* si les saisies sont valides.  
    **4.** `partie` dépend de ce que tape l’utilisateur (`input`) et communique par `print` : un `assert` ne peut ni répondre à sa place ni lire l’écran. D’où la règle : **séparer le calcul** (petites fonctions qui renvoient une valeur, testables) **de l’interaction** (fonctions courtes qui ne font qu’enchaîner `input`, `print` et les appels).

## Indices et score

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 5</span> — Chaud ou froid ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-les-bases-de-la-programmation-python-tp-1-5 }

Pour aider le joueur, on ajoute un indice selon la distance entre la proposition et le secret : `"brulant"` si elle vaut au plus 3, `"chaud"` si elle vaut au plus 10, `"froid"` au-delà.

1.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire `ecart(a, b)` qui renvoie la distance entre `a` et `b`, toujours positive ou nulle (`ecart(3, 10)` et `ecart(10, 3)` valent `7`). Utiliser une conditionnelle.

2.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire `indice(proposition, secret)`, en réutilisant `ecart`.

3.  <span class="run" title="À programmer et tester sur machine">▶</span> Modifier `partie` pour afficher, à chaque essai raté, la réponse, l’indice et le nombre d’essais restants.

```python
assert ecart(3, 10) == 7
assert ecart(10, 3) == 7
assert ecart(5, 5) == 0
assert indice(45, 42) == "brulant"
assert indice(32, 42) == "chaud"
assert indice(31, 42) == "froid"
```

```text
Votre proposition : 50
trop grand - chaud - il reste 6 essai(s)
```

Ces six tests suffisent-ils ? Quel test ajouter pour vérifier la frontière entre `"brulant"` et `"chaud"` *de l’autre côté* du secret ?

??? corrige "Corrigé"

    ```python
    def ecart(a, b):
        """Renvoie la distance entre a et b (positive ou nulle)."""
        if a >= b:
            return a - b
        else:
            return b - a

    def indice(proposition, secret):
        """Renvoie "brulant" (ecart <= 3), "chaud" (ecart <= 10) ou "froid"."""
        d = ecart(proposition, secret)
        if d <= 3:
            return "brulant"
        elif d <= 10:
            return "chaud"
        else:
            return "froid"
    ```

    Les six tests donnés ne vérifient la frontière qu’*au-dessus* pour `"brulant"` et *en dessous* pour `"chaud"`/`"froid"`. Tests de frontière à ajouter, des deux côtés du secret :

    ```python
    assert indice(39, 42) == "brulant"   # ecart 3, sous le secret
    assert indice(38, 42) == "chaud"     # ecart 4
    assert indice(52, 42) == "chaud"     # ecart 10, au-dessus
    assert indice(53, 42) == "froid"     # ecart 11
    ```

    Erreur fréquente détectée ainsi : `d = proposition - secret` (sans `ecart`), négatif sous le secret, qui donne toujours `"brulant"`.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Compter les points <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-les-bases-de-la-programmation-python-tp-1-6 }

Règle du score : une partie perdue rapporte `0` point ; trouver du **premier coup** rapporte `100` points ; sinon, on gagne `10` points, plus `10` points par essai **non utilisé**.

1.  Combien de points pour une victoire en 2 essais sur 7 ? en 7 essais sur 7 ?

2.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire `points(essais, essais_max)`, où `essais` est la valeur renvoyée par `partie`. Écrire sa docstring avec la **précondition** sur `essais`, et la vérifier par un `assert` en première ligne.

3.  Compléter ce jeu de tests (au moins un test par cas de la règle).

```python
assert points(0, 7) == 0       # perdu
assert points(1, 7) == 100     # du premier coup
assert points(2, 7) == ...
assert points(7, 7) == ...
```

??? corrige "Corrigé"

    **1.** 2 essais sur 7 : $10 + 10 \times 5 = 60$ points ; 7 essais sur 7 : $10 + 10 \times 0 = 10$ points.

    ```python
    def points(essais, essais_max):
        """Renvoie les points d'une partie.
        Precondition : 0 <= essais <= essais_max (0 signifie : perdu)."""
        assert essais >= 0 and essais <= essais_max, "nombre d'essais impossible"
        if essais == 0:
            return 0
        elif essais == 1:
            return 100
        else:
            return 10 + 10 * (essais_max - essais)

    assert points(0, 7) == 0       # perdu
    assert points(1, 7) == 100     # du premier coup
    assert points(2, 7) == 60
    assert points(7, 7) == 10      # gagne au dernier essai
    ```

    L’ordre des tests compte : si l’on teste `essais == 1` *après* la formule générale, le cas « premier coup » n’est jamais atteint.

## Niveaux et menu

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Trois niveaux de difficulté <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-les-bases-de-la-programmation-python-tp-1-7 }

| **Niveau** |  **Nom**  | **Nombre mystère** | **Essais autorisés** |
|:----------:|:---------:|:------------------:|:--------------------:|
|    `1`     |  facile   |   entre 1 et 10    |          4           |
|    `2`     |   moyen   |   entre 1 et 100   |          7           |
|    `3`     | difficile |  entre 1 et 1000   |          10          |

1.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire `afficher_menu()`, qui affiche les trois niveaux, **un par ligne** (trois `print`). Cette fonction ne renvoie rien.

2.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire `borne_max(niveau)` et `essais_autorises(niveau)`, qui renvoient la borne et le nombre d’essais du niveau. Précondition : `niveau` vaut `1`, `2` ou `3` — la garantir par un `assert` avec un message.

3.  Que se passe-t-il lors de l’appel `borne_max(4)` ? Pourquoi est-ce préférable à un résultat faux qui passerait inaperçu ?

??? corrige "Corrigé"

    ```python
    def afficher_menu():
        """Affiche les niveaux, un par ligne."""
        print("1 : facile    (entre 1 et 10,   4 essais)")
        print("2 : moyen     (entre 1 et 100,  7 essais)")
        print("3 : difficile (entre 1 et 1000, 10 essais)")
        print("4 : l'ordinateur devine (entre 1 et 100)")   # ajout de l'exercice 12

    def borne_max(niveau):
        """Renvoie la plus grande valeur possible du secret.
        Precondition : niveau vaut 1, 2 ou 3."""
        assert niveau >= 1 and niveau <= 3, "niveau inconnu"
        if niveau == 1:
            return 10
        elif niveau == 2:
            return 100
        else:
            return 1000

    def essais_autorises(niveau):
        """Renvoie le nombre d'essais du niveau.
        Precondition : niveau vaut 1, 2 ou 3."""
        assert niveau >= 1 and niveau <= 3, "niveau inconnu"
        if niveau == 1:
            return 4
        elif niveau == 2:
            return 7
        else:
            return 10
    ```

    **3.** `borne_max(4)` s’arrête net sur `AssertionError: niveau inconnu`. Sans l’`assert`, le `else` renverrait `1000` : un résultat faux, silencieux, découvert bien plus tard (ou jamais). Mieux vaut échouer tôt et clairement.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — Un menu à l’épreuve des fautes de frappe <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-les-bases-de-la-programmation-python-tp-1-8 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `demander_niveau()` qui affiche le menu, demande un niveau et **redemande tant que** la réponse n’est pas `"1"`, `"2"` ou `"3"`. Elle renvoie le niveau sous forme d’**entier**.

```text
1 : facile    (entre 1 et 10,   4 essais)
2 : moyen     (entre 1 et 100,  7 essais)
3 : difficile (entre 1 et 1000, 10 essais)
Votre niveau (1, 2 ou 3) : 4
Choix impossible.
Votre niveau (1, 2 ou 3) : 2
```

Pourquoi compare-t-on la saisie aux **chaînes** `"1"`, `"2"`, `"3"` *avant* de la convertir avec `int` ? Que ferait `int("deux")` ?

??? corrige "Corrigé"

    ```python
    def demander_niveau():
        """Affiche le menu et redemande jusqu'a un choix valide (entier renvoye)."""
        afficher_menu()
        choix = input("Votre niveau (1, 2, 3 ou 4) : ")
        while choix != "1" and choix != "2" and choix != "3" and choix != "4":
            print("Choix impossible.")
            choix = input("Votre niveau (1, 2, 3 ou 4) : ")
        return int(choix)
    ```

    (Sans l’exercice 12, la condition ne porte que sur `"1"`, `"2"`, `"3"`.) `int("deux")` provoque une `ValueError` qui arrête le programme : on vérifie donc la chaîne *avant* de la convertir. Piège classique : écrire `or` au lieu de `and` dans la condition (elle est alors toujours vraie : boucle infinie).

## Le jeu complet

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 9</span> — Rejouer et faire le bilan <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-les-bases-de-la-programmation-python-tp-1-9 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire la fonction principale `jouer()` qui :

- enchaîne les parties **tant que** le joueur répond `o` à la question `Rejouer ? (o/n)` ;

- pour chaque partie : demande le niveau, tire le secret, lance `partie`, calcule et affiche les points gagnés et le total ;

- à la fin, affiche un bilan : nombre de parties jouées, nombre de parties gagnées, total des points.

```text
Points gagnes : 30 - total : 30
Rejouer ? (o/n) n
Bilan : 2 partie(s), 1 gagnee(s), 30 points.
```

Puis ajouter tout en bas du fichier la ligne `jouer()`, **après** les tests, et faire tester votre jeu par un voisin.

1.  Repérer dans votre programme une **séquence**, une **affectation**, une **conditionnelle**, une boucle **non bornée**, un **appel de fonction**. Où une boucle **bornée** serait-elle utile ? (Voir la partie suivante.)

2.  Quelles variables de `jouer` sont des **compteurs** ou des **accumulateurs** ? Avec quelle valeur faut-il les initialiser, et où (avant ou dans la boucle) ?0

    ??? pouce "Coup de pouce"

        Trois variables avant la boucle (`nb_parties`, `nb_gagnees`, `total`) et une variable `encore = "o"` pour pouvoir entrer une première fois dans le `while`.

??? corrige "Corrigé"

    ```python
    def jouer():
        """Enchaine les parties et affiche le bilan."""
        nb_parties = 0
        nb_gagnees = 0
        total = 0
        encore = "o"
        while encore == "o":
            niveau = demander_niveau()
            if niveau == 4:                      # ajout de l'exercice 12
                ordinateur_devine(100)
            else:
                maxi = borne_max(niveau)
                essais_max = essais_autorises(niveau)
                secret = random.randint(1, maxi)
                essais = partie(secret, maxi, essais_max)
                nb_parties = nb_parties + 1
                if essais > 0:
                    nb_gagnees = nb_gagnees + 1
                gain = points(essais, essais_max)
                total = total + gain
                print("Points gagnes :", gain, "- total :", total)
            encore = input("Rejouer ? (o/n) ")
        print("Bilan :", nb_parties, "partie(s),", nb_gagnees, "gagnee(s),",
              total, "points.")

    # ... les tests assert ...
    jouer()
    ```

    Exécution réelle (saisies simulées, secret `42` puis `3` ; le menu, affiché avant chaque choix de niveau, n’est pas reproduit) :

    ```text
    Votre niveau (1, 2, 3 ou 4) : 5
    Choix impossible.
    Votre niveau (1, 2, 3 ou 4) : 2
    Votre proposition : 50
    trop grand - chaud - il reste 6 essai(s)
    Votre proposition : 0
    Hors limites ! Entre 1 et 100 (essai non compte).
    Votre proposition : 25
    trop petit - froid - il reste 5 essai(s)
    Votre proposition : 37
    trop petit - chaud - il reste 4 essai(s)
    Votre proposition : 40
    trop petit - brulant - il reste 3 essai(s)
    Votre proposition : 42
    Bravo, trouve en 5 essai(s) !
    Points gagnes : 30 - total : 30
    Rejouer ? (o/n) o
       (niveau 1 : 5, 8, 9, 10 -> Perdu ! Le nombre mystere etait 3)
    Points gagnes : 0 - total : 30
    Rejouer ? (o/n) n
    Bilan : 2 partie(s), 1 gagnee(s), 30 points.
    ```

    **1.** Séquence : le corps de `jouer` ; affectations : `total = total + gain` ; conditionnelles : `comparer`, `indice`, `points` ; boucles non bornées : `partie`, `demander_niveau`, `jouer` ; appels de fonction : partout dans `jouer`. La boucle bornée sert dans `pire_cas` (parcourir *tous* les secrets).  
    **2.** Compteurs : `nb_parties`, `nb_gagnees` ; accumulateur : `total`. Tous initialisés à `0` **avant** la boucle : placés dedans, ils seraient remis à zéro à chaque partie (erreur la plus fréquente de l’exercice).

## Défi : l’ordinateur devine

On renverse les rôles. Stratégie de l’ordinateur pour un nombre entre `mini` et `maxi` : proposer le **milieu** `(mini + maxi) // 2` ; si c’est trop petit, le secret est entre `milieu + 1` et `maxi` ; si c’est trop grand, entre `mini` et `milieu - 1`. On recommence avec le nouvel intervalle.

Cette stratégie, qui coupe l’intervalle en deux à chaque essai, est l’un des grands classiques de l’algorithmique. Nous l’étudierons en détail au chapitre *La recherche dichotomique* : elle y recevra son nom, nous prouverons qu’elle se termine toujours et nous calculerons précisément son coût.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 10</span> — Jouer la stratégie à la main <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-01-les-bases-de-la-programmation-python-tp-1-10 }

Le secret est `37`, entre 1 et 100. Recopier sur le cahier le tableau suivant et le compléter jusqu’à la victoire.

| **Essai** | `mini` | `maxi` | **proposition** | **réponse** |
|:---------:|:------:|:------:|:---------------:|:-----------:|
|     1     |   1    |  100   |       50        | trop grand  |
|     2     |        |        |                 |             |
|     3     |        |        |                 |             |
|     …     |        |        |                 |             |

??? corrige "Corrigé"

    | **Essai** | `mini` | `maxi` | **proposition** | **réponse** |
    |:---------:|:------:|:------:|:---------------:|:-----------:|
    |     1     |   1    |  100   |       50        | trop grand  |
    |     2     |   1    |   49   |       25        | trop petit  |
    |     3     |   26   |   49   |       37        |    gagné    |

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 11</span> — Le pire des cas <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-les-bases-de-la-programmation-python-tp-1-11 }

1.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire `essais_ordinateur(secret, maxi)` qui **simule** cette stratégie (le secret est connu de la fonction, qui utilise `comparer` pour obtenir la réponse) et renvoie le nombre d’essais nécessaires.0

    ??? pouce "Coup de pouce"

        La boucle de `essais_ordinateur` ressemble à celle de `partie` : un booléen `trouve`, un compteur d’essais ; seuls `mini` et `maxi` changent selon la réponse de `comparer`.

    ```python
    assert essais_ordinateur(50, 100) == 1
    assert essais_ordinateur(25, 100) == 2
    assert essais_ordinateur(100, 100) == 7
    ```

2.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire `pire_cas(maxi)` qui essaie **tous** les secrets possibles de 1 à `maxi` (boucle `for`) et renvoie le plus grand nombre d’essais rencontré. Calculer `pire_cas(10)`, `pire_cas(100)`, `pire_cas(1000)`. Que remarquez-vous en comparant avec le tableau des niveaux ?0

    ??? pouce "Coup de pouce 2 (début de solution)"

        `def pire_cas(maxi):`  
        `pire = 0`  
        `for secret in range(1, maxi + 1):`  
        `e = essais_ordinateur(secret, maxi)`  
        …

3.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire `nb_moities(n)` qui compte combien de fois on peut diviser `n` par 2 (division entière `//`) avant d’arriver à `0`. Vérifier par une boucle d’`assert` que `pire_cas(m) == nb_moities(m)` pour tous les `m` de 1 à 200. Combien d’essais suffiraient pour un nombre entre 1 et un million ?

??? corrige "Corrigé"

    ```python
    def essais_ordinateur(secret, maxi):
        """Simule la strategie du milieu ; renvoie le nombre d'essais.
        Precondition : 1 <= secret <= maxi."""
        assert secret >= 1 and secret <= maxi
        mini = 1
        essais = 0
        trouve = False
        while not trouve:
            proposition = (mini + maxi) // 2
            essais = essais + 1
            reponse = comparer(proposition, secret)
            if reponse == "trop petit":
                mini = proposition + 1
            elif reponse == "trop grand":
                maxi = proposition - 1
            else:
                trouve = True
        return essais

    def pire_cas(maxi):
        """Renvoie le plus grand nombre d'essais sur tous les secrets de 1 a maxi."""
        pire = 0
        for secret in range(1, maxi + 1):
            e = essais_ordinateur(secret, maxi)
            if e > pire:
                pire = e
        return pire

    def nb_moities(n):
        """Nombre de divisions entieres par 2 pour passer de n a 0."""
        k = 0
        while n > 0:
            n = n // 2
            k = k + 1
        return k

    assert pire_cas(10) == 4 and pire_cas(100) == 7 and pire_cas(1000) == 10
    for m in range(1, 201):
        assert pire_cas(m) == nb_moities(m)
    ```

    **2.** `pire_cas(10)`, `pire_cas(100)`, `pire_cas(1000)` valent **4, 7 et 10** : exactement les essais autorisés. Chaque niveau est donc « juste » : un joueur qui applique la bonne stratégie gagne *toujours*, de justesse dans le pire des cas. (Entre 1 et 100, la moyenne est de 5,8 essais ; 37 secrets sur 100 demandent les 7 essais.)  
    **3.** Les 200 `assert` passent. `nb_moities(1000000)` vaut **20** : 20 essais suffisent pour un nombre entre 1 et un million.  
    *Terminaison de `essais_ordinateur`* : variant `maxi - mini + 1` (le nombre de candidats), qui diminue strictement à chaque essai raté ; comme le secret reste toujours entre `mini` et `maxi`, on finit par le proposer.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 12</span> — À vous de penser, à lui de deviner <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-01-les-bases-de-la-programmation-python-tp-1-12 }

<span class="run" title="À programmer et tester sur machine">▶</span> Écrire `ordinateur_devine(maxi)` : le joueur pense à un nombre ; l’ordinateur propose, le joueur répond `+` (c’est plus), `-` (c’est moins) ou `=`. Une réponse inattendue est redemandée sans compter d’essai. Si le joueur **triche** (ses réponses se contredisent), l’intervalle devient vide (`mini > maxi`) : l’ordinateur l’annonce et s’arrête.

```text
Je propose 50 (+, - ou =) : +
Je propose 75 (+, - ou =) : -
Je propose 62 (+, - ou =) : +
Je propose 68 (+, - ou =) : =
Trouve en 4 essai(s) !
```

Ajouter ce mode au menu de `jouer()` (par exemple, niveau `4`). Quelles fonctions faut-il modifier ? Lesquelles restent intactes ?

??? corrige "Corrigé"

    ```python
    def ordinateur_devine(maxi):
        """Le joueur pense a un nombre entre 1 et maxi ; l'ordinateur le devine."""
        mini = 1
        essais = 0
        fini = False
        while not fini:
            if mini > maxi:
                print("Tricheur ! Aucun nombre ne convient.")
                fini = True
            else:
                proposition = (mini + maxi) // 2
                essais = essais + 1
                reponse = input("Je propose " + str(proposition) + " (+, - ou =) : ")
                if reponse == "+":
                    mini = proposition + 1
                elif reponse == "-":
                    maxi = proposition - 1
                elif reponse == "=":
                    print("Trouve en", essais, "essai(s) !")
                    fini = True
                else:
                    print("Repondre par +, - ou =.")
                    essais = essais - 1
    ```

    Testé : la séquence `+ - + =` donne bien l’affichage de l’énoncé ; répondre `+` à chaque fois affiche `Tricheur !` juste après la 7<sup>e</sup> proposition (`100`). Pour l’ajouter au jeu, on modifie `afficher_menu`, `demander_niveau` et `jouer` (voir plus haut) ; `comparer`, `indice`, `points`, `partie`, `borne_max` et `essais_autorises` restent **intactes** — c’est tout l’intérêt du découpage en fonctions. Attention : `borne_max(4)` déclencherait l’`assert`, d’où le `if niveau == 4` placé *avant* son appel.

## Bilan à rédiger

Sur une demi-page du cahier (ou dans un commentaire en tête du fichier `nombre_mystere.py`) :

1.  Lister les fonctions écrites, avec pour chacune : ce qu’elle reçoit, ce qu’elle renvoie (ou affiche), et si elle est testée par des `assert`. Lesquelles ne peuvent pas l’être, et pourquoi ?

2.  Citer un test qui vous a fait trouver une erreur dans votre code. Quelle était l’erreur ?

3.  Expliquer en deux phrases pourquoi 7 essais suffisent toujours entre 1 et 100 quand on joue « au milieu ».
