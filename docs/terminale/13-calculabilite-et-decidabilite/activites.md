# Activités préparatoires

<p class="sous-titre">Calculabilité et décidabilité</p>

## <span class="etiquette">Activité 1</span> Un programme peut en manger un autre

*recettes, programmes qui lisent des programmes, et un devin malheureux*

<p class="infos-activite">Durée : 25 min · Sans ordinateur, par deux</p>

!!! consignes "Consignes"

    - On lit, on prédit, on joue ; on répond sur le cahier. Aucun mot de vocabulaire n’est attendu avant l’exercice 4.

### <span class="exo-num">Exercice 1</span> — La recette de crêpes <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-13-calculabilite-et-decidabilite-act-1-1 }

Une fiche porte la recette des crêpes. Recopier et compléter sur le cahier le tableau suivant : pour chaque situation, dire **qui travaille** (la « machine »), **ce qu’il reçoit** (la « donnée ») et si la recette est **exécutée** (on obtient des crêpes) ou seulement **lue comme un texte**.

| **Situation** | **Qui travaille ?** | **Ce qu’il reçoit** | **Exécutée ou lue ?** |
|:---|:---|:---|:---|
| Un cuisinier suit la recette. |  |  |  |
| Une photocopieuse en tire dix exemplaires. |  |  |  |
| Un traducteur la met en anglais. |  |  |  |
| Un correcteur orthographique la relit. |  |  |  |
| Un éditeur compte le nombre de lignes de la recette pour la mise en page. |  |  |  |

1.  Un même texte peut-il être tantôt « des instructions à suivre », tantôt « une donnée à traiter » ?

??? corrige "Corrigé"

    | **Situation** | **Qui travaille ?** | **Ce qu’il reçoit** | **Exécutée ou lue ?** |
    |:---|:---|:---|:---|
    | cuisinier | le cuisinier | la recette | **exécutée** |
    | photocopieuse | la photocopieuse | la recette | lue (copiée) |
    | traducteur | le traducteur | la recette | lue (traduite) |
    | correcteur orthographique | le correcteur | la recette | lue (vérifiée) |
    | compter les lignes | l’éditeur | la recette | lue (mesurée) |

    1.  Oui : le **même** texte est une suite d’instructions pour le cuisinier, et une simple donnée pour tous les autres. Tout dépend de **qui** le reçoit et de ce qu’il en fait.

### <span class="exo-num">Exercice 2</span> — Python lit du Python <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-13-calculabilite-et-decidabilite-act-1-2 }

On considère la fonction suivante, enregistrée dans un fichier `test.py`, suivie de l’appel `accueil(3)` :

```python
def accueil(n):
    for k in range(n):
        print("bonjour")
```

1.  Dans un terminal, on tape `python3 test.py`. Qu’est-ce qui s’affiche ? Dans cette commande, quel est le programme qui travaille, et quelle est sa donnée ?

2.  On range maintenant le **texte** de la fonction dans une chaîne de caractères, et on écrit une autre fonction :

    ```python
    source = 'def accueil(n):\n    for k in range(n):\n        print("bonjour")\n'

    def compter_lignes(code):
        return code.count("\n")    # nombre de passages a la ligne
    ```

    Que renvoie `compter_lignes(source)` ? Un « bonjour » est-il affiché ?

3.  En Python, `exec(chaine)` exécute le programme écrit dans la chaîne. Qu’affiche l’instruction `exec(source + "accueil(2)\n")` ?

4.  La fonction `compter_lignes` a elle aussi un texte (deux lignes). Peut-on lui donner **son propre texte** en entrée ? Que renverrait-elle ?

??? corrige "Corrigé"

    1.  Il s’affiche trois fois `bonjour`. Le programme qui travaille est `python3` (l’**interpréteur**) ; sa donnée est le fichier `test.py`, c’est-à-dire le **texte** d’un programme. (Et `python3` est lui-même lancé par le terminal, qui tourne sur le système d’exploitation…)

    2.  `compter_lignes(source)` renvoie $3$ (trois passages à la ligne) ; aucun `bonjour` n’est affiché : le texte de `accueil` est **lu**, pas exécuté — comme la recette par la photocopieuse.

    3.  Deux `bonjour` : `exec` **exécute** le texte reçu (définition de `accueil`, puis appel `accueil(2)`) — comme le cuisinier. `exec` est un interpréteur Python *dans* Python.

    4.  Oui : le texte de `compter_lignes` est une chaîne comme une autre ; elle renverrait $2$. Un programme peut recevoir **son propre texte** en entrée : rien de magique, c’est une donnée. (Vérifié en Python : $3$, deux `bonjour`, $2$.)

### <span class="exo-num">Exercice 3</span> — Le devin et le contrariant <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-13-calculabilite-et-decidabilite-act-1-3 }

**Le jeu** (à deux). Le **devin** écrit en secret sur un papier une prédiction : « tu vas lever la main » ou « tu ne vas pas lever la main », puis tend le papier au **contrariant**. Le contrariant lit la prédiction et fait **exactement le contraire**. Jouer trois manches en échangeant les rôles.

1.  Combien de fois le devin a-t-il eu raison ? Existe-t-il une prédiction gagnante pour le devin ? Pourquoi ?

2.  Que changerait la règle si le contrariant n’avait **pas le droit de lire** la prédiction ?

3.  **Le menteur.** La phrase « *Cette phrase est fausse.* » est-elle vraie ? fausse ?

4.  **Le barbier.** Dans un village, le barbier rase tous les hommes qui ne se rasent pas eux-mêmes, et seulement ceux-là. Le barbier se rase-t-il lui-même ?

5.  Qu’ont en commun le contrariant, la phrase du menteur et le barbier ?

??? corrige "Corrigé"

    1.  Le devin a eu raison **zéro** fois. Aucune prédiction n’est gagnante : quelle que soit celle qu’il écrit, le contrariant la lit et fait l’inverse. Le devin n’est pas « mauvais » : sa tâche est **impossible** dès que sa prédiction est lue par celui qu’elle concerne.

    2.  Le contrariant ne pourrait plus contredire : le devin aurait raison une fois sur deux au hasard, et la contradiction disparaîtrait. Tout le piège vient de ce que la prédiction **porte sur** celui qui la lit et lui est **donnée**.

    3.  Ni l’un ni l’autre : si elle est vraie, ce qu’elle dit est vrai, donc elle est fausse ; si elle est fausse, ce qu’elle dit est faux, donc elle est vraie (**paradoxe du menteur**).

    4.  S’il se rase, il fait partie de ceux qui se rasent eux-mêmes, donc il ne devrait pas se raser ; s’il ne se rase pas, il devrait se raser. Aucune réponse ne tient : un tel barbier **ne peut pas exister**.

    5.  Les trois parlent **d’eux-mêmes** (ou reçoivent un énoncé sur eux-mêmes) et le **contredisent** : c’est l’**auto-référence**.

### <span class="exo-num">Exercice 4</span> — Mettre des mots <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-13-calculabilite-et-decidabilite-act-1-4 }

1.  Recopier et compléter sur le cahier, avec vos mots.

    - Pour l’ordinateur, le texte d’un programme est avant tout …

    - Un programme qui lit le texte d’un autre programme et l’exécute s’appelle …

    - Un programme peut même recevoir en entrée …

    - Le contrariant est imbattable parce qu’il …

2.  **Une question pour la suite.** On rêve d’un programme « devin » qui lirait le texte de **n’importe quel** programme et prédirait, sans l’exécuter, s’il finira par s’arrêter ou s’il tournera pour toujours. Un tel devin peut-il exister ? Donner votre intuition, en pensant au contrariant.

??? corrige "Corrigé"

    1.  Mots attendus : **une donnée** (une chaîne de caractères) ; un **interpréteur** ; **son propre texte** (le programme peut se prendre lui-même en entrée) ; **lit la prédiction qui le concerne et fait le contraire**.

    2.  Intuition attendue : non. Si un tel devin existait, on pourrait écrire un programme « contrariant » qui demande au devin ce qu’il va faire lui-même, puis fait l’inverse (boucler si le devin prédit l’arrêt, s’arrêter sinon). C’est exactement la preuve du cours. On laisse la question ouverte : le cours y répond.
