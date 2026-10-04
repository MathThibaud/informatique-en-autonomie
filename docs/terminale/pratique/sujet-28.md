# Sujet 28 — Ordonnancement de tâches : le tourniquet

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/pratique-28-tourniquet){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-pratique-28-tourniquet.zip){ .md-button }

??? corrige "Corrigé"

    !!! remarque "Remarque"

        On donne une version simple ; d’autres réponses sont possibles. Le fichier complet, `corrige_sujet_28.py`, est en ligne : [`github.com/MathThibaud/nsi-fichiers-eleves/tree/main/corriges/terminale/pratique-28`](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/corriges/terminale/pratique-28).

    Question 1

    *Tourniquet de quantum 2 sur `[("A", 3), ("B", 1), ("C", 4)]` : frise, file, instants de fin.*

    (tête de file à gauche)

    | **Intervalle** | **Tâche** | **Ce qui se passe** | **File ensuite** |
    |:--:|:--:|:---|:---|
    | $[0 ; 2]$ | A | A s’exécute 2, il reste 1 : réenfilée | `B, C, A(1)` |
    | $[2 ; 3]$ | B | B s’exécute 1 : **finie à 3** | `C, A(1)` |
    | $[3 ; 5]$ | C | C s’exécute 2, il reste 2 : réenfilée | `A(1), C(2)` |
    | $[5 ; 6]$ | A | A s’exécute 1 : **finie à 6** | `C(2)` |
    | $[6 ; 8]$ | C | C s’exécute 2 : **finie à 8** | (vide) |

    On obtient `[("B", 3), ("A", 6), ("C", 8)]`.

    $\blacktriangleright$ Appel professeur. dérouler la frise en montrant qu’une tâche non terminée repart en **fin** de file.

    Question 2

    *Écrire `tourniquet(taches, quantum)` avec une `File`.*

    ```python
    def tourniquet(taches, quantum):
        f = File()
        for tache in taches:
            f.enfiler(tache)
        instant = 0
        fins = []
        while not f.est_vide():
            nom, reste = f.defiler()
            execution = min(quantum, reste)   # au plus quantum unites de temps
            instant = instant + execution
            reste = reste - execution
            if reste > 0:
                f.enfiler((nom, reste))       # pas finie : retour en fin de file
            else:
                fins.append((nom, instant))
        return fins
    ```

    On enfile un **nouveau** couple `(nom, reste)` : la liste `taches` de départ n’est pas modifiée.

    ```python
        assert tourniquet(taches, 1) == [("B", 2), ("A", 6), ("C", 8)]
        assert tourniquet(taches, 10) == premier_arrive(taches)
        assert tourniquet([], 2) == []
    ```

    Question 3

    *Écrire `temps_moyen(fins)`.*

    ```python
    def temps_moyen(fins):
        total = 0
        for nom, instant in fins:
            total = total + instant
        return total / len(fins)
    ```

    Pour l’exemple : premier arrivé donne $(3+4+8)/3 = 5$, le tourniquet de quantum 2 donne $(3+6+8)/3 \approx 5{,}67$.

    $\blacktriangleright$ Appel professeur. présenter `tourniquet` et le rôle de la file, puis vérifier les tests.

    Question 4

    *Exécuter `comparer("taches.csv")` et interpréter.*

    ```console
    >>> comparer("taches.csv")
    premier arrivé : 62.375
    tourniquet, quantum 1 : 27.0
    tourniquet, quantum 2 : 27.75
    tourniquet, quantum 5 : 30.0
    tourniquet, quantum 10 : 36.875
    tourniquet, quantum 100 : 62.375
    ```

    - En premier arrivé, premier servi, la `sauvegarde` (40 unités), placée en tête, fait attendre toutes les autres : même la `calculatrice` (durée 1) ne se termine qu’à l’instant 78. Le tourniquet fait passer les **tâches courtes** rapidement (quantum 5 : `navigateur` finie à 8 au lieu de 43) ; les longues (`sauvegarde`, `antivirus`) finissent un peu plus tard, mais le temps moyen est divisé par plus de deux.

    - Quand le quantum dépasse la durée de toutes les tâches (ici 100), aucune tâche n’est interrompue : on retrouve exactement premier arrivé, premier servi.

    - En pratique, chaque changement de tâche (**commutation de contexte**) a un coût pour le processeur : sauvegarder et restaurer l’état de la tâche. Un quantum trop petit multiplie ces commutations et fait perdre du temps ; on choisit un compromis.

    $\blacktriangleright$ Appel professeur. interpréter les résultats et faire le lien avec l’ordonnancement des processus vu en cours (interactivité, coût des commutations).

*Durée de l’épreuve : 1 heure.*

!!! encadre "Déroulement de l’épreuve"

    - Cette situation d’évaluation comporte ce document ainsi que des fichiers de codes et de données présents sur l’ordinateur. Le candidat doit **agir en autonomie** et faire preuve d’initiative tout au long de l’épreuve.

    - En cas de difficulté, le candidat peut solliciter l’examinateur. Des moments privilégiés sont indiqués sous la forme d’**appels professeur**. L’examinateur peut intervenir à tout moment s’il le juge utile.

Un système d’exploitation doit partager le processeur entre plusieurs tâches. On suppose ici que toutes les tâches sont prêtes à l’instant `0`, dans un ordre donné, et qu’une tâche est décrite par un couple `(nom, duree)`, la durée étant un nombre entier d’unités de temps.

On compare deux façons de choisir la tâche à exécuter, toutes deux fondées sur une **file** de tâches en attente :

- **premier arrivé, premier servi** : on défile une tâche et on l’exécute **jusqu’au bout**, puis on passe à la suivante ;

- **tourniquet** de quantum `q` : on défile une tâche et on l’exécute pendant **au plus** `q` unités de temps. Si elle n’est pas terminée, elle est **enfilée de nouveau**, en fin de file, avec sa durée restante.

Chaque ordonnancement est résumé par la liste des couples `(nom, instant de fin)`, dans l’ordre où les tâches se terminent. Par exemple, pour les tâches `[("A", 3), ("B", 1), ("C", 4)]`, l’ordonnancement premier arrivé, premier servi donne `[("A", 3), ("B", 4), ("C", 8)]`.

Le fichier `ordonnanceur.py` fournit la classe `File` vue en cours (méthodes `est_vide`, `enfiler`, `defiler`, `tete` et `taille`), la fonction `lire_taches` qui lit les tâches d’un fichier CSV et la fonction `premier_arrive`.

Question 1

Pour les tâches `[("A", 3), ("B", 1), ("C", 4)]` et un tourniquet de quantum `2`, représenter sur une frise l’exécution des tâches au cours du temps ainsi que le contenu de la file, puis donner la liste des couples `(nom, instant de fin)`.

**$\blacktriangleright$ Appel professeur.** Appeler le professeur pour lui présenter votre réponse ou en cas de difficulté.

Question 2

Écrire le corps de la fonction `tourniquet(taches, quantum)` qui renvoie la liste des couples `(nom, instant de fin)` obtenue avec un tourniquet de quantum `quantum`, en utilisant un objet de la classe `File`. On pourra s’inspirer de la fonction `premier_arrive`. Tester avec la fonction `test_tourniquet`.

Question 3

Écrire le corps de la fonction `temps_moyen(fins)` qui renvoie la moyenne des instants de fin d’une liste de couples `(nom, instant de fin)`. Tester avec la fonction `test_temps_moyen`.

**$\blacktriangleright$ Appel professeur.** Appeler le professeur pour lui présenter votre réponse ou en cas de difficulté.

Question 4

Exécuter `comparer("taches.csv")`, qui affiche le temps moyen de fin des tâches du fichier pour l’ordonnancement premier arrivé, premier servi et pour plusieurs quantums. Interpréter les résultats : quelles tâches profitent du tourniquet ? Que se passe-t-il quand le quantum devient grand ? Pourquoi, en pratique, ne choisit-on pas un quantum aussi petit que possible ?

**$\blacktriangleright$ Appel professeur.** Appeler le professeur pour lui présenter votre réponse ou en cas de difficulté.

### Description du dossier

Le dossier fourni au candidat comporte les éléments suivants :

- une version PDF de l’énoncé ;

- un code source de départ `ordonnanceur.py` ;

- un fichier de données `taches.csv` (colonnes `nom` et `duree`).

??? corrige "Corrigé"

    !!! remarque "Remarque"

        On donne une version simple ; d’autres réponses sont possibles. Le fichier complet, `corrige_sujet_28.py`, est en ligne : [`github.com/MathThibaud/nsi-fichiers-eleves/tree/main/corriges/terminale/pratique-28`](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/corriges/terminale/pratique-28).

    Question 1

    *Tourniquet de quantum 2 sur `[("A", 3), ("B", 1), ("C", 4)]` : frise, file, instants de fin.*

    (tête de file à gauche)

    | **Intervalle** | **Tâche** | **Ce qui se passe** | **File ensuite** |
    |:--:|:--:|:---|:---|
    | $[0 ; 2]$ | A | A s’exécute 2, il reste 1 : réenfilée | `B, C, A(1)` |
    | $[2 ; 3]$ | B | B s’exécute 1 : **finie à 3** | `C, A(1)` |
    | $[3 ; 5]$ | C | C s’exécute 2, il reste 2 : réenfilée | `A(1), C(2)` |
    | $[5 ; 6]$ | A | A s’exécute 1 : **finie à 6** | `C(2)` |
    | $[6 ; 8]$ | C | C s’exécute 2 : **finie à 8** | (vide) |

    On obtient `[("B", 3), ("A", 6), ("C", 8)]`.

    $\blacktriangleright$ Appel professeur. dérouler la frise en montrant qu’une tâche non terminée repart en **fin** de file.

    Question 2

    *Écrire `tourniquet(taches, quantum)` avec une `File`.*

    ```python
    def tourniquet(taches, quantum):
        f = File()
        for tache in taches:
            f.enfiler(tache)
        instant = 0
        fins = []
        while not f.est_vide():
            nom, reste = f.defiler()
            execution = min(quantum, reste)   # au plus quantum unites de temps
            instant = instant + execution
            reste = reste - execution
            if reste > 0:
                f.enfiler((nom, reste))       # pas finie : retour en fin de file
            else:
                fins.append((nom, instant))
        return fins
    ```

    On enfile un **nouveau** couple `(nom, reste)` : la liste `taches` de départ n’est pas modifiée.

    ```python
        assert tourniquet(taches, 1) == [("B", 2), ("A", 6), ("C", 8)]
        assert tourniquet(taches, 10) == premier_arrive(taches)
        assert tourniquet([], 2) == []
    ```

    Question 3

    *Écrire `temps_moyen(fins)`.*

    ```python
    def temps_moyen(fins):
        total = 0
        for nom, instant in fins:
            total = total + instant
        return total / len(fins)
    ```

    Pour l’exemple : premier arrivé donne $(3+4+8)/3 = 5$, le tourniquet de quantum 2 donne $(3+6+8)/3 \approx 5{,}67$.

    $\blacktriangleright$ Appel professeur. présenter `tourniquet` et le rôle de la file, puis vérifier les tests.

    Question 4

    *Exécuter `comparer("taches.csv")` et interpréter.*

    ```console
    >>> comparer("taches.csv")
    premier arrivé : 62.375
    tourniquet, quantum 1 : 27.0
    tourniquet, quantum 2 : 27.75
    tourniquet, quantum 5 : 30.0
    tourniquet, quantum 10 : 36.875
    tourniquet, quantum 100 : 62.375
    ```

    - En premier arrivé, premier servi, la `sauvegarde` (40 unités), placée en tête, fait attendre toutes les autres : même la `calculatrice` (durée 1) ne se termine qu’à l’instant 78. Le tourniquet fait passer les **tâches courtes** rapidement (quantum 5 : `navigateur` finie à 8 au lieu de 43) ; les longues (`sauvegarde`, `antivirus`) finissent un peu plus tard, mais le temps moyen est divisé par plus de deux.

    - Quand le quantum dépasse la durée de toutes les tâches (ici 100), aucune tâche n’est interrompue : on retrouve exactement premier arrivé, premier servi.

    - En pratique, chaque changement de tâche (**commutation de contexte**) a un coût pour le processeur : sauvegarder et restaurer l’état de la tâche. Un quantum trop petit multiplie ces commutations et fait perdre du temps ; on choisit un compromis.

    $\blacktriangleright$ Appel professeur. interpréter les résultats et faire le lien avec l’ordonnancement des processus vu en cours (interactivité, coût des commutations).
