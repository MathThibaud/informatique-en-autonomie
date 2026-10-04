# Activités préparatoires

<p class="sous-titre">Systèmes sur puce et informatique embarquée</p>

## <span class="etiquette">Activité 1</span> Un ordinateur dans une carte de 5 cm

*percevoir, décider, agir avec un micro:bit simulé*

<p class="infos-activite">Durée : 20 min · Par deux, sur un ordinateur</p>

!!! consignes "Consignes"

    - Ouvrir l’éditeur Python officiel du micro:bit : `python.microbit.org` (gratuit, sans compte). À droite de l’écran se trouve un **simulateur** : la carte, ses deux boutons A et B, son écran de $5 \times 5$ LED et, en dessous, des curseurs qui simulent ses capteurs (dont la **température**).

    - Effacer le programme d’exemple, taper le programme demandé, puis lancer le simulateur (bouton de lecture sous la carte). Après chaque modification, relancer.

    - Le micro:bit est une vraie carte, utilisée dans les collèges du monde entier ; tout ce que vous écrivez ici fonctionnerait tel quel sur la carte réelle.

### <span class="exo-num">Exercice 1</span> — Un bouton, une lumière <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-14-systemes-sur-puce-et-informatique-embarq-act-1-1 }

Programme 1 :

```python
from microbit import *

while True:
    if button_a.is_pressed():
        display.show(Image.HEART)
    else:
        display.clear()
    sleep(100)
```

1.  Lancer le programme, puis appuyer sur le bouton A du simulateur (et le relâcher). Décrire ce qui se passe.

2.  Dans ce programme, quelle ligne **perçoit** le monde extérieur ? quelle ligne **décide** ? quelles lignes **agissent** ?

3.  Supprimer la ligne `while True:` (et décaler le reste vers la gauche), relancer, appuyer sur A. Que se passe-t-il ? Pourquoi la boucle sans fin est-elle indispensable ?

4.  Remettre la boucle. Modifier le programme pour que le cœur ne s’affiche que si l’on appuie **en même temps** sur A et sur B (le bouton B s’appelle `button_b`). Recopier sur le cahier la ligne modifiée.

??? corrige "Corrigé"

    **1.** Tant que A est enfoncé, un cœur s’affiche ; dès qu’on le relâche, l’écran s’éteint (au plus $0{,}1$ s plus tard).

    **2.** **Percevoir** : `button_a.is_pressed()` (ligne 4, on lit l’état du bouton). **Décider** : le `if` / `else` (lignes 4 et 6). **Agir** : `display.show(Image.HEART)` et `display.clear()` (lignes 5 et 7).

    **3.** Le programme s’exécute **une seule fois**, au lancement : le bouton n’est pas enfoncé à cet instant, l’écran est effacé, puis le programme se termine. Appuyer ensuite sur A ne fait plus rien. Un système embarqué doit surveiller le monde **en permanence** : d’où la boucle sans fin.

    **4.** `if button_a.is_pressed() and button_b.is_pressed():`

### <span class="exo-num">Exercice 2</span> — Un thermomètre <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-14-systemes-sur-puce-et-informatique-embarq-act-1-2 }

Programme 2 :

```python
from microbit import *

while True:
    t = temperature()
    display.scroll(str(t))
    sleep(500)
```

1.  Lancer le programme et faire glisser le curseur de température du simulateur. Qu’affiche la carte ? Quel est le type de la valeur renvoyée par `temperature()` ?

2.  Ici, quel composant joue le rôle de **capteur** ? Lequel joue le rôle d’**actionneur** ?

??? corrige "Corrigé"

    **5.** La carte fait défiler la température choisie avec le curseur (dans le simulateur, le curseur va d’environ $-5$ à $50$ degrés). `temperature()` renvoie un **entier** (`int`), en degrés Celsius ; `str(t)` le transforme en texte pour l’afficher.

    **6.** **Capteur** : le capteur de température de la carte (il mesure, c’est une **entrée**). **Actionneur** : l’écran de LED (il agit, c’est une **sortie**).

### <span class="exo-num">Exercice 3</span> — Un thermostat <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-14-systemes-sur-puce-et-informatique-embarq-act-1-3 }

On veut chauffer une pièce à $19$ degrés : la LED du centre de l’écran (colonne $2$, ligne $2$) représente le **radiateur**. L’instruction `display.set_pixel(2, 2, 9)` l’allume au maximum ; `display.clear()` éteint tout l’écran.

Programme 3, à compléter :

```python
from microbit import *

consigne = 19
while True:
    t = temperature()
    if ...:
        display.set_pixel(2, 2, 9)    # radiateur allume
    else:
        display.clear()               # radiateur eteint
    sleep(1000)
```

1.  Compléter la condition, puis vérifier avec le curseur à $15$ degrés et à $25$ degrés. Recopier la condition sur le cahier.

2.  Le programme ne regarde la température qu’une fois par seconde. Que pourrait-il se passer si l’on remplaçait `sleep(1000)` par `sleep(600000)` (dix minutes) ? Et si ce programme pilotait un **airbag** au lieu d’un radiateur ?

??? corrige "Corrigé"

    **7.** Condition : `t < consigne`. À $15$ degrés, la LED centrale s’allume (radiateur en marche) ; à $25$ degrés, elle s’éteint.

    ```python
    from microbit import *

    consigne = 19
    while True:
        t = temperature()
        if t < consigne:
            display.set_pixel(2, 2, 9)    # radiateur allume
        else:
            display.clear()               # radiateur eteint
        sleep(1000)
    ```

    **8.** Avec dix minutes d’attente, le programme ne verrait un changement de température qu’avec jusqu’à dix minutes de retard : la pièce pourrait refroidir longtemps avant que le radiateur ne s’allume. Pour un radiateur, c’est inconfortable mais sans danger. Pour un **airbag**, un retard de quelques millisecondes est déjà inacceptable : la réponse doit arriver **à temps**, c’est une **contrainte de temps réel**.

### <span class="exo-num">Exercice 4</span> — Ce qu’on a découvert <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-14-systemes-sur-puce-et-informatique-embarq-act-1-4 }

1.  Recopier et compléter sur le cahier, avec vos mots.

    - Les trois programmes ont la même forme : une boucle qui, sans fin,…

    - Un **capteur** sert à… ; un **actionneur** sert à…

    - Sur cette carte, on n’a lancé ni Windows, ni Android : dès qu’elle est alimentée, elle…

      Pourtant, il y a bien un processeur et de la mémoire. Où sont-ils, d’après vous ?

??? corrige "Corrigé"

    **9.**

    - … **lit un capteur, décide, puis commande un actionneur** (percevoir $\to$ décider $\to$ agir).

    - … **mesurer** une grandeur physique (entrée) ; … **agir** sur le monde physique (sortie).

    - … **exécute directement son programme**, sans système d’exploitation. Le processeur et la mémoire sont **tous dans la petite puce noire** de la carte.
