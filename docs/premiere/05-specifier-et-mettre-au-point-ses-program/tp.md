# TP et projets

<p class="sous-titre">Spécifier et mettre au point ses programmes</p>

## <span class="etiquette">TP</span> Le bulletin bogué

*spécifier, tester, déboguer et sécuriser un vrai module*

<p class="infos-activite">Durée : 2 à 3 h (deux séances) · Sur machine, par deux</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/05-tp-bulletin-bogue){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/premiere-05-tp-bulletin-bogue.zip){ .md-button }

!!! encadre "But du TP"

    Un programmeur pressé a écrit le module qui calcule les bulletins de notes du lycée. Il affirme : « j’ai testé, tout passe ». Pourtant, le bulletin qu’il affiche est faux de la première à la dernière ligne. Votre mission : **spécifier** ses sept fonctions, écrire des **jeux de tests** qui démasquent les bugs, **déboguer**, **sécuriser** le code par la programmation défensive, **prouver** une boucle par un invariant et un variant — puis comparer avec un autre langage. Produit final : un fichier `bulletin.py` correct, documenté et testé, et un **rapport de bugs**.

!!! consignes "Consignes"

    - Fichier à télécharger (lien ci-dessus) : `tp_mise_au_point_depart.py`. Le **copier** sous le nom `bulletin.py` et ne travailler que sur la copie.

    - Les réponses aux questions (sans <span class="run" title="À programmer et tester sur machine">▶</span> ) s’écrivent sur le cahier.

    - <span class="run" title="À programmer et tester sur machine">▶</span> signale ce qui est *à programmer et tester*. Garder **tous** les tests écrits au fil du TP en bas du fichier, et relancer le fichier après chaque modification.

    - Si le programme se fige, c’est une **boucle infinie** : l’interrompre avec `Ctrl + C` et le noter.

    - Niveau : ★ échauffement, ★★ classique (niveau bac), ★★★ défi ; les *coups de pouce* et les *corrigés* se déplient sous chaque exercice.

    - Usage de l’IA, indiqué sur chaque exercice : <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> aucune ; <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> en appui (déboguer, reformuler, vérifier ; la réponse finale est écrite et comprise par vous) ; <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> l’exercice s’appuie sur une réponse d’IA. Voir la [charte d’usage de l’IA](../charte.md).

## Prise en main : un bulletin qui a l’air juste

Voici les sept fonctions du fichier fourni (commentaires d’origine compris). Les notes sont sur 20 et rangées dans l’ordre chronologique des devoirs.

```python
def moyenne(notes):
    # moyenne des notes
    somme = 0
    for i in range(1, len(notes)):
        somme = somme + notes[i]
    return somme / len(notes)

def moyenne_ponderee(notes, coefs):
    # moyenne en tenant compte des coefficients
    somme = 0
    for i in range(len(notes)):
        somme = somme + notes[i] * coefs[i]
    return somme / len(notes)

def arrondi_demi(x):
    # arrondi au demi-point
    return int(x * 2) / 2

def nb_admis(notes):
    # combien de notes sont au moins egales a 10
    nb = 0
    for x in notes:
        if x > 10:
            nb = nb + 1
    return nb

def rang(moyennes, m):
    # rang de la moyenne m parmi les moyennes de la classe
    r = 0
    for x in moyennes:
        if x >= m:
            r = r + 1
    return r

def nb_progressions(notes):
    # combien de fois une note est meilleure que la precedente
    nb = 0
    for i in range(len(notes)):
        if notes[i] > notes[i - 1]:
            nb = nb + 1
    return nb

def premiere_sous(notes, seuil):
    # indice de la premiere note strictement inferieure au seuil
    i = 0
    while i < len(notes):
        if notes[i] < seuil:
            return i
    i = i + 1
    return None
```

Le fichier se termine par les tests du programmeur et par l’affichage du bulletin de Lina :

```python
assert moyenne([0, 10, 20]) == 10
assert moyenne_ponderee([12, 14], [1, 1]) == 13
assert arrondi_demi(12.5) == 12.5
assert nb_admis([8, 12, 15]) == 2
assert rang([12, 15, 9], 12) == 2
assert nb_progressions([8, 10, 12]) == 2
assert premiere_sous([5, 12, 14], 10) == 0
print("Tous les tests passent.")

bulletin("Lina", [15, 9, 12, 10], [1, 2, 1, 2], [13.5, 11.0, 15.0, 11.0, 8.5, 9.5])
```

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 1</span> — Le bulletin de Lina, à la main <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-tp-1-1 }

1.  <span class="run" title="À programmer et tester sur machine">▶</span> Lancer le fichier. Recopier ce qu’il affiche.

2.  Lina a eu `15` (coef. 1), `9` (coef. 2), `12` (coef. 1), `10` (coef. 2). Calculer **à la main** sa moyenne pondérée, puis l’arrondir au demi-point le plus proche. Combien de ses notes valent au moins 10 ? Combien de fois a-t-elle progressé d’un devoir au suivant ? Les moyennes de la classe (dont la sienne) sont `13.5, 11.0, 15.0, 11.0, 8.5, 9.5` : quel est son rang (les ex aequo partagent le même rang) ?

3.  Comparer avec l’affichage. Quelles lignes du bulletin sont fausses ? Quel résultat est même *impossible*, quelles que soient les notes ?

4.  « Tous les tests passent. » Que prouve cette phrase ? Que ne prouve-t-elle pas ?

??? corrige "Corrigé"

    !!! encadre "Les sept bugs du fichier de départ"

        Chaque test du programmeur évite précisément le cas qui révèle le bug (première note nulle, coefficients tous égaux à 1, `x` déjà multiple de 0,5, aucune note égale à 10, pas d’ex aequo, première note la plus basse, première note déjà sous le seuil).

        | **Fonction** | **Ligne fautive** | **Correction** |
        |:---|:---|:---|
        | `moyenne` | `range(1, len(notes))` oublie la 1<sup>re</sup> note | `range(len(notes))` |
        |  | et tableau vide : `ZeroDivisionError` | `if len(notes) == 0: return None` |
        | `moyenne_ponderee` | divise par `len(notes)` | divise par la somme des coefficients |
        | `arrondi_demi` | `int(x * 2) / 2` tronque | `int(x * 2 + 0.5) / 2` |
        | `nb_admis` | `x > 10` | `x >= 10` |
        | `rang` | `r = 0` et `x >= m` | `r = 1` et `x > m` |
        | `nb_progressions` | `range(len(notes))` : `notes[-1]` pour `i = 0` | `range(1, len(notes))` |
        | `premiere_sous` | `i = i + 1` hors de la boucle | l’indenter dans le `while` |

    - **1.** « Le succès d’un jeu de tests ne garantit pas la correction d’un programme ». Point commun des sept tests : un seul cas, le plus « gentil », jamais de valeur limite ni de cas particulier du cahier des charges.

    - **2.** Réponse personnelle ; attendus fréquents : les tests aux frontières (`nb_admis`, `rang`, `arrondi_demi`), l’affichage pour la boucle infinie, le variant pour l’expliquer.

    - **3.** Non : on a seulement vérifié un nombre fini de cas. Pour une boucle, l’invariant et le variant apportent une vraie **preuve** ; pour le reste, un bon jeu de tests rend un bug *peu probable*, pas impossible.

    **1.** Affichage obtenu :

    ```text
    Tous les tests passent.
    Bulletin de Lina
    Moyenne : 16.0 / 20
    Notes d'au moins 10 : 2 sur 4
    Progressions : 2
    Rang : 0 sur 6
    ```

    **2.** Moyenne pondérée : $\dfrac{15 \times 1 + 9 \times 2 + 12 \times 1 + 10 \times 2}{1 + 2 + 1 + 2} = \dfrac{65}{6} \approx 10{,}83$, arrondie au demi-point le plus proche : **11**. Notes d’au moins 10 : **3** (15, 12, 10). Progressions : **1** (de 9 à 12). Rang : deux moyennes sont strictement supérieures à 11 (13,5 et 15), donc rang **3** sur 6 (ex aequo avec l’autre 11).  
    **3.** Toutes les lignes sont fausses ; un rang `0` est impossible (le meilleur rang vaut 1).  
    **4.** Elle prouve seulement que le code donne le bon résultat *sur ces sept cas* ; elle ne prouve pas qu’il est correct en général (règle de Dijkstra : les tests montrent la présence de bugs, jamais leur absence).

## Spécifier : écrire le contrat

Le cahier des charges du lycée décrit ce que chaque fonction *doit* faire.

!!! encadre "Cahier des charges"

    - `moyenne(notes)` : la moyenne des notes ; `None` si le tableau est vide.

    - `moyenne_ponderee(notes, coefs)` : somme des `note `$\times$` coef` divisée par la **somme des coefficients** ; autant de coefficients que de notes, tous strictement positifs ; au moins une note.

    - `arrondi_demi(x)` : pour un nombre positif `x`, le demi-point **le plus proche** (`12.2` donne `12.0`, `12.8` donne `13.0`) ; à égale distance, on arrondit vers le haut (`12.25` donne `12.5`).

    - `nb_admis(notes)` : le nombre de notes **supérieures ou égales** à 10.

    - `rang(moyennes, m)` : `m` est l’une des moyennes de la classe ; son rang vaut 1 + le nombre de moyennes **strictement** supérieures (deux ex aequo ont le même rang).

    - `nb_progressions(notes)` : le nombre de devoirs dont la note est strictement supérieure à celle du devoir **précédent** (le premier devoir n’a pas de précédent).

    - `premiere_sous(notes, seuil)` : l’indice de la première note strictement inférieure à `seuil`, ou `None` s’il n’y en a pas.

    - Dans toutes les fonctions, une note est un nombre entre 0 et 20.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 2</span> — Des docstrings à la place des commentaires <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-tp-1-2 }

1.  Pour chacune des sept fonctions, remplacer le commentaire par une **docstring** qui donne son rôle, ses **préconditions** (sur les arguments) et sa **postcondition** (sur le résultat). Vérifier le résultat avec `help(rang)` dans la console.

2.  Le nom `nb_admis` est-il bien choisi pour « nombre de notes d’au moins 10 » ? Proposer mieux, sans le changer dans le fichier (le reste du logiciel l’utilise).

3.  Pour `rang`, donner une postcondition qui encadre le résultat entre deux valeurs.

??? corrige "Corrigé"

    **1.** Voir les docstrings de la version corrigée (exercice 6). **2.** Le nom suggère des élèves « admis » alors qu’on compte des *notes* : `nb_notes_au_moins_10` est plus juste ; on garde l’ancien nom pour ne pas casser le reste du logiciel (la docstring lève l’ambiguïté). **3.** Postcondition : `1 <= rang(moyennes, m) <= len(moyennes)` — elle aurait suffi à rejeter le `0` du bulletin de Lina.

## Tester pour démasquer

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 3</span> — Un vrai jeu de tests <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-tp-1-3 }

1.  Pour chaque fonction, expliquer en une phrase pourquoi le test du programmeur est **trop faible** (par exemple : quel ingrédient de la check-list du cours lui manque-t-il ?).

2.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire pour chaque fonction un jeu de tests d’au moins **trois** `assert` : un cas normal, un cas limite, un cas particulier tiré du cahier des charges. **Ne rien corriger pour l’instant** : le but est de *faire échouer* le code.

3.  Commenter chaque test qui échoue (`# ECHOUE`) et continuer avec les suivants. Recopier sur le cahier (ou en commentaire dans `bulletin.py`) le tableau ci-dessous et le compléter (un bug par fonction, et un de plus : le cas du tableau vide pour `moyenne`).0

    ??? pouce "Coup de pouce"

        Penser aux valeurs *égales* à une frontière (une note de 10, deux moyennes égales, un `x` à égale distance), aux tableaux vides, à un tableau d’un seul élément, et à une première valeur qui joue un rôle particulier (la première note, le premier devoir).

| **Fonction**       | **Test qui échoue** | **Attendu** | **Obtenu** |
|:-------------------|:--------------------|:------------|:-----------|
| `moyenne`          |                     |             |            |
| `moyenne` (vide)   |                     |             |            |
| `moyenne_ponderee` |                     |             |            |
| `arrondi_demi`     |                     |             |            |
| `nb_admis`         |                     |             |            |
| `rang`             |                     |             |            |
| `nb_progressions`  |                     |             |            |
| `premiere_sous`    |                     |             |            |

??? corrige "Corrigé"

    **1.** `moyenne` : la première note vaut 0, donc l’oublier ne change rien ; pas de cas vide. `moyenne_ponderee` : coefficients tous égaux à 1 (la somme des coefficients vaut alors `len(notes)`). `arrondi_demi` : `12.5` est déjà un multiple de 0,5. `nb_admis` : aucune note égale à la frontière 10. `rang` : pas d’ex aequo. `nb_progressions` : la première note est la plus petite. `premiere_sous` : la réponse est l’indice 0, la boucle ne fait jamais un deuxième tour.  
    **2–3.** Jeu de tests possible et résultat **réellement obtenu sur la version d’origine** :

    | **Test**                             | **Attendu** | **Obtenu (origine)** |
    |:-------------------------------------|:------------|:---------------------|
    | `moyenne([12, 8, 16])`               | `12`        | `8.0`                |
    | `moyenne([])`                        | `None`      | `ZeroDivisionError`  |
    | `moyenne_ponderee([10, 16], [1, 2])` | `14`        | `21.0`               |
    | `arrondi_demi(12.8)`                 | `13.0`      | `12.5`               |
    | `arrondi_demi(12.25)`                | `12.5`      | `12.0`               |
    | `nb_admis([10, 9.5, 20])`            | `2`         | `1`                  |
    | `rang([15, 12, 15], 15)`             | `1`         | `2`                  |
    | `nb_progressions([12, 8, 10])`       | `1`         | `2`                  |
    | `premiere_sous([12, 14, 5, 3], 10)`  | `2`         | boucle infinie       |
    | `premiere_sous([12, 14], 10)`        | `None`      | boucle infinie       |

    Tests qui passent sur la version d’origine et qu’on garde (cas normaux et limites) : `arrondi_demi(12.2) == 12.0`, `arrondi_demi(0) == 0`, `nb_admis([]) == 0`, `rang([15, 12, 15], 12) == 3`, `nb_progressions([14]) == 0`, `premiere_sous([], 10) is None`…

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 4</span> — Un bug sans message d’erreur <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-tp-1-4 }

L’appel `nb_progressions([12, 8, 10])` renvoie `2` au lieu de `1`, **sans aucune erreur**.

1.  Pour `i = 0`, quelles cases sont comparées ? Pourquoi Python ne signale-t-il pas d’`IndexError` ?

2.  Pourquoi le test du programmeur, `[8, 10, 12]`, ne pouvait-il pas voir ce bug ?

??? corrige "Corrigé"

    **1.** Pour `i = 0`, on compare `notes[0]` à `notes[-1]`, c’est-à-dire à la **dernière** note : un indice négatif est valide en Python (on compte depuis la fin), donc aucune erreur. Sur `[12, 8, 10]`, `12 > 10` compte une « progression » fantôme. **2.** Avec `[8, 10, 12]`, la première note est la plus petite : `8 > 12` est faux, la comparaison parasite ne compte rien. C’est le piège signalé dans le cours à propos de la convention `-1`.

## Déboguer et corriger

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 5</span> — Enquêter avec des affichages <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-tp-1-5 }

1.  <span class="run" title="À programmer et tester sur machine">▶</span> Dans `premiere_sous`, ajouter `print("i =", i)` comme première ligne du corps de la boucle, puis lancer `premiere_sous([12, 14, 5], 10)`. Qu’observe-t-on ? Quelle est la cause ?

2.  <span class="run" title="À programmer et tester sur machine">▶</span> Dans `moyenne_ponderee`, afficher `somme` après la boucle et la valeur par laquelle on divise, pour `[10, 16]` et `[1, 2]`. Quelle est la bonne valeur du diviseur ?

3.  Dérouler à la main `rang([15, 12, 15], 15)` : valeurs successives de `x` et de `r`. Pourquoi le résultat est-il juste quand il n’y a pas d’ex aequo ?

??? corrige "Corrigé"

    **1.** L’écran se remplit de `i = 0` sans fin (`Ctrl + C`) : `i = i + 1` est indenté au niveau du `while`, donc exécuté *après* la boucle, jamais pendant ; `notes[0] = 12` n’étant pas sous le seuil, la boucle ne progresse pas.  
    **2.** `somme` vaut `42` et l’on divise par `2` (le nombre de notes) : `21.0`. Il faut diviser par la somme des coefficients, `3`, ce qui donne `14`.  
    **3.** `x = 15` : `r = 1` ; `x = 12` : `r = 1` ; `x = 15` : `r = 2`. Résultat `2` au lieu de `1`. Avec `>=`, on compte `m` elle-même et ses ex aequo : sans ex aequo, cela fait exactement « 1 + nombre de moyennes strictement supérieures », d’où un résultat juste par hasard.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Tout corriger, tout relancer <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-tp-1-6 }

1.  <span class="run" title="À programmer et tester sur machine">▶</span> Corriger les sept fonctions, **une à la fois**, en relançant **tous** les tests après chaque correction. Retirer les affichages de débogage, garder les tests (et retirer les `# ECHOUE`).

2.  Pour `arrondi_demi`, on peut ajouter `0.5` quelque part avant `int` : où exactement, et pourquoi cela transforme-t-il une troncature en arrondi ? Vérifier sur `12.2`, `12.25` et `12.8`.

3.  Relancer le bulletin de Lina et le comparer à votre calcul de l’exercice 1.

4.  Rédiger le **rapport de bugs** (sur le cahier ou en commentaire en tête de `bulletin.py`) : pour chaque fonction, le *symptôme* (le test qui échoue), la *cause* (la ligne fautive) et la *correction*.0

    ??? pouce "Coup de pouce"

        Pour `rang`, deux changements : la valeur initiale de `r` et la comparaison. Pour `nb_progressions`, c’est le `range` qui doit changer, pas la comparaison.

??? corrige "Corrigé"

    Version corrigée complète (avec la programmation défensive de l’exercice 7 et l’invariant de l’exercice 8) :

    ```python
    def notes_valides(notes):
        """Renvoie True si toutes les notes sont comprises entre 0 et 20."""
        for x in notes:
            if x < 0 or x > 20:
                return False
        return True

    def moyenne(notes):
        """Renvoie la moyenne des notes, ou None si le tableau est vide.
        Precondition : chaque note est entre 0 et 20.
        Postcondition : None si notes == [], sinon un nombre entre 0 et 20."""
        assert notes_valides(notes), "note hors de [0, 20]"
        if len(notes) == 0:
            return None
        somme = 0
        for i in range(len(notes)):
            somme = somme + notes[i]
        return somme / len(notes)

    def moyenne_ponderee(notes, coefs):
        """Renvoie la moyenne des notes ponderee par les coefficients.
        Preconditions : notes non vide, meme longueur que coefs,
        notes entre 0 et 20, coefficients strictement positifs.
        Postcondition : un nombre entre 0 et 20."""
        assert len(notes) > 0, "aucune note"
        assert len(notes) == len(coefs), "autant de coefficients que de notes"
        assert notes_valides(notes), "note hors de [0, 20]"
        somme = 0
        somme_coefs = 0
        for i in range(len(notes)):
            assert coefs[i] > 0, "coefficient nul ou negatif"
            somme = somme + notes[i] * coefs[i]
            somme_coefs = somme_coefs + coefs[i]
        return somme / somme_coefs

    def arrondi_demi(x):
        """Renvoie x arrondi au demi-point le plus proche
        (au demi-point superieur en cas d'egalite).
        Precondition : x >= 0."""
        assert x >= 0, "x doit etre positif"
        return int(x * 2 + 0.5) / 2

    def nb_admis(notes):
        """Renvoie le nombre de notes superieures ou egales a 10."""
        nb = 0
        for x in notes:
            if x >= 10:
                nb = nb + 1
        return nb

    def rang(moyennes, m):
        """Renvoie le rang de m : 1 + le nombre de moyennes strictement
        superieures a m (les ex aequo ont le meme rang).
        Precondition : m est l'une des moyennes du tableau.
        Postcondition : 1 <= resultat <= len(moyennes)."""
        assert m in moyennes, "m doit etre une moyenne de la classe"
        r = 1
        for x in moyennes:
            if x > m:
                r = r + 1
        return r

    def nb_progressions(notes):
        """Renvoie le nombre d'indices i >= 1 tels que notes[i] > notes[i - 1]."""
        nb = 0
        for i in range(1, len(notes)):
            if notes[i] > notes[i - 1]:
                nb = nb + 1
        return nb

    def premiere_sous(notes, seuil):
        """Renvoie l'indice de la premiere note strictement inferieure a seuil,
        ou None s'il n'y en a pas."""
        i = 0
        while i < len(notes):
            # invariant : les notes d'indices 0 a i - 1 sont toutes >= seuil
            for k in range(i):
                assert notes[k] >= seuil
            if notes[i] < seuil:
                return i
            i = i + 1
        return None

    def bulletin(nom, notes, coefs, moyennes_classe):
        """Affiche le bulletin de l'eleve nom."""
        m = arrondi_demi(moyenne_ponderee(notes, coefs))
        print("Bulletin de", nom)
        print("Moyenne :", m, "/ 20")
        print("Notes d'au moins 10 :", nb_admis(notes), "sur", len(notes))
        print("Progressions :", nb_progressions(notes))
        print("Rang :", rang(moyennes_classe, m), "sur", len(moyennes_classe))
        i = premiere_sous(notes, 10)
        if i is not None:
            print("Premiere note sous la moyenne : devoir numero", i + 1)
    ```

    Jeu de tests final (tous verts) :

    ```python
    assert moyenne([0, 10, 20]) == 10
    assert moyenne([12, 8, 16]) == 12        # la premiere note compte
    assert moyenne([15]) == 15
    assert moyenne([]) is None               # cas vide : sentinelle
    assert moyenne_ponderee([12, 14], [1, 1]) == 13
    assert moyenne_ponderee([10, 16], [1, 2]) == 14   # coefficients differents
    assert moyenne_ponderee([8], [3]) == 8
    assert arrondi_demi(12.5) == 12.5
    assert arrondi_demi(12.8) == 13.0        # arrondi vers le haut
    assert arrondi_demi(12.2) == 12.0
    assert arrondi_demi(12.25) == 12.5       # egalite : demi-point superieur
    assert arrondi_demi(0) == 0
    assert nb_admis([8, 12, 15]) == 2
    assert nb_admis([10, 9.5, 20]) == 2      # 10 compte
    assert nb_admis([]) == 0
    assert rang([12, 15, 9], 12) == 2
    assert rang([12, 15, 9], 15) == 1
    assert rang([15, 12, 15], 15) == 1       # ex aequo premiers
    assert rang([15, 12, 15], 12) == 3
    assert nb_progressions([8, 10, 12]) == 2
    assert nb_progressions([12, 8, 10]) == 1  # le 1er devoir n'a pas de precedent
    assert nb_progressions([14]) == 0
    assert nb_progressions([]) == 0
    assert premiere_sous([5, 12, 14], 10) == 0
    assert premiere_sous([12, 14, 5, 3], 10) == 2
    assert premiere_sous([12, 14], 10) is None
    assert premiere_sous([], 10) is None
    assert notes_valides([0, 20, 12.5]) == True
    assert notes_valides([-1, 12]) == False
    assert notes_valides([20.5]) == False
    assert notes_valides([]) == True
    ```

    **2.** On ajoute `0.5` **après** avoir multiplié par 2 et **avant** `int` : `int(x * 2 + 0.5)`. `int` tronque (garde la partie entière) ; décaler de 0,5 fait passer à l’entier suivant tout nombre dont la partie décimale est au moins 0,5 : c’est un arrondi à l’entier le plus proche de `2x`, donc au demi-point le plus proche de `x`. `12.2` $\to$ `int(24.9)/2 = 12.0` ; `12.25` $\to$ `int(25.0)/2 = 12.5` ; `12.8` $\to$ `int(26.1)/2 = 13.0`.  
    **3.** Le bulletin corrigé correspond au calcul de l’exercice 1 :

    ```text
    Bulletin de Lina
    Moyenne : 11.0 / 20
    Notes d'au moins 10 : 3 sur 4
    Progressions : 1
    Rang : 3 sur 6
    Premiere note sous la moyenne : devoir numero 2
    ```

    **4.** Le rapport de bugs reprend le tableau du début de ce corrigé (symptôme = test de l’exercice 3).

## Programmation défensive

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Des garde-fous <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-tp-1-7 }

1.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire `notes_valides(notes)` qui renvoie `True` si toutes les notes sont entre 0 et 20, `False` sinon. La tester (penser à `0`, `20`, `-1`, `20.5` et au tableau vide).

2.  <span class="run" title="À programmer et tester sur machine">▶</span> Ajouter des `assert` avec message pour **toutes** les préconditions du cahier des charges : notes valides, même longueur pour `notes` et `coefs`, coefficients strictement positifs, `x` positif, `m` présente dans `moyennes`… Vérifier que `moyenne_ponderee([12, 25], [1, 1])` s’arrête avec un message clair.

3.  Pour `moyenne`, le cahier des charges impose la valeur **sentinelle** `None` pour le tableau vide, et non un `assert`. Quel est alors le devoir de celui qui appelle `moyenne` ?

4.  <span class="run" title="À programmer et tester sur machine">▶</span> Ajouter au bulletin une dernière ligne `Premiere note sous la moyenne : devoir numero 2` (le numéro est l’indice + 1), affichée **seulement** si `premiere_sous(notes, 10)` ne renvoie pas `None`.

??? corrige "Corrigé"

    **1–2.** Voir le code ci-dessus. Messages obtenus :

    ```text
    moyenne_ponderee([12, 25], [1, 1]) -> AssertionError: note hors de [0, 20]
    moyenne_ponderee([12, 14], [1])    -> AssertionError: autant de coefficients que de notes
    moyenne_ponderee([12, 14], [1, 0]) -> AssertionError: coefficient nul ou negatif
    arrondi_demi(-3)                   -> AssertionError: x doit etre positif
    rang([12, 15], 13)                 -> AssertionError: m doit etre une moyenne de la classe
    ```

    **3.** Celui qui appelle doit **tester le résultat** (`if r is not None:`) avant de l’utiliser dans un calcul ou un affichage ; sinon l’erreur surgit plus loin (`TypeError` sur `None`).  
    **4.** Voir les deux dernières lignes de `bulletin`. Pour Lina, la première note sous 10 est le 9 du devoir d’indice 1, d’où « devoir numero 2 ».

## Prouver une boucle : invariant et variant

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 8</span> — La boucle de `premiere_sous`, version corrigée <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-tp-1-8 }

1.  Compléter l’invariant : « au début de chaque tour, les notes d’indices `0` à `i - 1` sont toutes … ». Recopier et compléter cette phrase.

2.  Montrer qu’il est vrai avant le premier tour, puis qu’il reste vrai d’un tour au suivant.

3.  Si la fonction renvoie `None`, que vaut `i` à la sortie de la boucle ? En déduire, grâce à l’invariant, que la postcondition est respectée.

4.  <span class="run" title="À programmer et tester sur machine">▶</span> Traduire l’invariant en `assert` placé en tête du corps de la boucle (une petite boucle `for` sur les indices déjà vus), et relancer les tests.

5.  Donner un **variant** qui prouve que la boucle corrigée se termine. Pourquoi la version d’origine n’en avait-elle pas ?0

    ??? pouce "Coup de pouce"

        Avant le premier tour, `i` vaut `0` : de quelles notes parle l’invariant ? Pour le variant, chercher une quantité entière, positive, qui diminue de 1 à chaque tour.

??? corrige "Corrigé"

    **1.** « … sont toutes **supérieures ou égales à `seuil`** ».  
    **2.** Avant le premier tour, `i = 0` : il n’y a aucune note d’indice 0 à $-1$, la propriété est vraie (rien à vérifier). Si elle est vraie au début d’un tour et qu’on ne sort pas par le `return`, c’est que `notes[i] >= seuil` ; après `i = i + 1`, les notes d’indices 0 à `i - 1` (l’ancien `i` compris) sont toutes au moins égales au seuil.  
    **3.** On sort de la boucle sans `return` quand `i < len(notes)` devient faux, c’est-à-dire `i == len(notes)`. L’invariant dit alors que *toutes* les notes sont au moins égales au seuil : renvoyer `None` est bien correct. (Si l’on sort par `return i`, l’invariant garantit que c’est la *première* note sous le seuil.)  
    **4.** Voir la petite boucle `for k in range(i)` du code corrigé (à retirer une fois la mise au point finie : elle rend la fonction plus lente).  
    **5.** Variant : `len(notes) - i`, entier positif tant qu’on est dans la boucle, qui diminue de 1 à chaque tour. Dans la version d’origine, `i` ne change jamais pendant la boucle : la quantité reste constante, ce n’est pas un variant — et la boucle est effectivement infinie dès que `notes[0] >= seuil`.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 9</span> — Un invariant pour un compteur <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-tp-1-9 }

Énoncer l’invariant de la boucle `for` de `nb_admis` corrigée (que vaut `nb` après avoir parcouru une partie des notes ?), et en déduire que la fonction renvoie le bon résultat.

??? corrige "Corrigé"

    Invariant : « après avoir parcouru les `k` premières notes, `nb` est le nombre de notes supérieures ou égales à 10 parmi elles ». Vrai au départ (`k = 0`, `nb = 0`), préservé car on ajoute 1 exactement quand la note examinée est au moins 10. À la fin, toutes les notes ont été parcourues : `nb` est le résultat attendu.

## Défi : au-delà de Python

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 10</span> — Le même calcul en C <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-tp-1-10 }

Le lycée voisin calcule ses moyennes avec ce programme en langage C.

```text
float moyenne(int notes[], int n) {
    int somme = 0;
    for (int i = 0; i < n; i++) {
        somme = somme + notes[i];
    }
    return somme / n;
}
```

1.  Repérer ce qui est **commun** avec Python (constructions) et ce qui est **particulier** au C (syntaxe, déclarations).

2.  Le typage du C est-il statique ou dynamique ? Qu’est-ce qui le montre dans le code ? Que se passerait-il, et *quand*, si l’on écrivait `somme = somme + "a";` ?

3.  En C, la division de deux `int` est une division **entière** (comme `//` en Python). Que renvoie ce programme pour les notes `12` et `13` ? Quel test aurait démasqué le bug ? La correction consiste à écrire `(float) somme / n` : que fait, d’après vous, `(float)` ?

4.  Le programme C est **compilé**, `bulletin.py` est **interprété**. Le compilateur aurait-il signalé le bug de la question 3 ? Et le bug d’indentation de `premiere_sous` ?

??? corrige "Corrigé"

    **1.** Commun : une fonction, une affectation `somme = somme + notes[i]`, une boucle bornée, un accumulateur initialisé à 0, un `return`. Particulier au C : types déclarés (`float`, `int`), accolades à la place de l’indentation, points-virgules, boucle `for (init; condition; pas)`, la taille `n` du tableau passée en paramètre.  
    **2.** Statique : chaque variable a un type **déclaré** (`int somme`). `somme = somme + "a";` est refusé **à la compilation**, avant toute exécution (le compilateur signale par exemple *incompatible pointer to integer conversion*). En Python, la même faute ne se verrait qu’à l’exécution de la ligne.  
    **3.** `somme / n` = `25 / 2` = `12` en division entière : le programme affiche `12.000000` au lieu de `12.5`. Tout test dont la somme n’est pas un multiple du nombre de notes le démasque ; les tests « ronds » comme `{10, 10}` ou `{0, 10, 20}` le laissent passer. `(float)` **convertit** `somme` en flottant avant la division, qui devient alors décimale (affichage corrigé : `12.500000`).  
    **4.** Non dans les deux cas : ce sont des erreurs de **logique**, pas de langage ; le programme est bien formé et bien typé. Un compilateur attrape les fautes de syntaxe et de type, pas les erreurs d’algorithme : les tests restent indispensables, quel que soit le langage.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 11</span> — Mille tests au hasard <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-specifier-et-mettre-au-point-ses-program-tp-1-11 }

<span class="horsprog">au-delà du programme</span> On ne connaît pas à l’avance le bon arrondi d’un nombre tiré au hasard, mais on sait le **vérifier** : le résultat doit être un multiple de `0.5`, à au plus `0.25` de `x`.

1.  <span class="run" title="À programmer et tester sur machine">▶</span> Écrire l’**oracle** `verifie_arrondi(r, x)`, qui renvoie `True` si `r` est un arrondi acceptable de `x`. (`r` est un multiple de `0.5` si `r * 2` est un entier, c’est-à-dire si `int(r * 2) == r * 2`.)

2.  <span class="run" title="À programmer et tester sur machine">▶</span> Tirer 1 000 nombres `x = random.randint(0, 2000) / 100` et vérifier `arrondi_demi(x)` avec l’oracle, par un `assert`. Faire de même avec la version d’origine (copiée sous un autre nom) : combien de tirages la démasquent ?

??? corrige "Corrigé"

    <span class="horsprog">au-delà du programme</span>

    ```python
    import random

    def verifie_arrondi(r, x):
        """Renvoie True si r est un multiple de 0.5 a au plus 0.25 de x."""
        return int(r * 2) == r * 2 and r - x <= 0.25 and x - r <= 0.25

    for i in range(1000):
        x = random.randint(0, 2000) / 100
        assert verifie_arrondi(arrondi_demi(x), x)
    ```

    La version corrigée passe les 1 000 tirages. La version d’origine échoue sur **environ la moitié** des tirages (de 476 à 509 sur 1 000 lors de cinq essais ; 48 % en moyenne) : tous les `x` dont la partie décimale, comptée à partir du dernier demi-point, dépasse 0,25. Un seul tirage malchanceux suffit à la démasquer ; l’oracle juge sans connaître la réponse exacte.

## Bilan à rédiger

Sur le cahier, en une demi-page :

1.  Les sept tests du programmeur passaient alors que les sept fonctions étaient fausses. Quelle règle du cours cette situation illustre-t-elle ? Quel point commun avaient ses tests ?

2.  Parmi les outils du TP (docstring, jeu de tests, affichages, `assert` de précondition, invariant, variant), lequel vous a été le plus utile, et pour quel bug ?

3.  Vos tests passent maintenant tous. Le module est-il pour autant *certainement* correct ? Justifier.
