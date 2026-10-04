# Exercices

<p class="sous-titre">Informatique embarquée et objets connectés</p>

!!! consignes "Mode d’emploi"

    - Niveau : ★ échauffement, ★★ classique (niveau bac), ★★★ défi ; les *coups de pouce* et les *corrigés* se déplient sous chaque exercice.

    - <span class="tag">sur papier</span> *à faire sur papier* ; <span class="tag">sur machine</span> *à programmer et tester* en Python.

    - Réflexe « objet embarqué » : **capteur** (mesure) $\to$ **programme** (décision) $\to$ **actionneur** (action) $\to$ on recommence.

    - Usage de l’IA, indiqué sur chaque exercice : <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> aucune ; <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> en appui (déboguer, reformuler, vérifier ; la réponse finale est écrite et comprise par vous) ; <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> l’exercice s’appuie sur une réponse d’IA. Voir la charte d’usage de l’IA.

### Systèmes embarqués

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 1</span> — Embarqué ou pas ? <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-08-1 }

<span class="tag">sur papier</span>  Pour chaque objet, dire s’il contient un **système embarqué**, et si oui, la tâche qu’il accomplit : un lave-linge ; un marteau ; un régulateur de vitesse de voiture ; une chaise ; une montre connectée ; un feu tricolore.

??? corrige "Corrigé"

    - **Oui** : lave-linge (piloter le cycle de lavage) ; régulateur de vitesse (maintenir la vitesse) ; montre connectée (afficher l’heure, mesurer l’activité) ; feu tricolore (gérer l’alternance des feux).

    - **Non** : le marteau et la chaise (aucun ordinateur).

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 2</span> — Pas tout à fait un ordinateur <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-08-2 }

<span class="tag">sur papier</span>  Citer **deux** différences entre un système embarqué (dans un objet) et un ordinateur de bureau.

??? corrige "Corrigé"

    Un système embarqué ne réalise **qu’une tâche** (au lieu d’être polyvalent), n’a en général **ni écran ni clavier** classiques, est **minuscule et sobre**, et doit souvent réagir **en temps réel**.

### Capteurs et actionneurs

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 3</span> — Qui mesure, qui agit ? <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-08-3 }

<span class="tag">sur papier</span>  Classer en deux colonnes (**capteur** / **actionneur**) : thermomètre, radiateur, détecteur de mouvement, haut-parleur, microphone, moteur de volet, capteur de luminosité, LED.

??? corrige "Corrigé"

    - **Capteurs** : thermomètre, détecteur de mouvement, microphone, capteur de luminosité.

    - **Actionneurs** : radiateur, haut-parleur, moteur de volet, LED.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 4</span> — Dans un objet du quotidien <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-4 }

<span class="tag">sur papier</span>  Pour un **portail automatique** de maison :

1.  Citer un **capteur** et un **actionneur** de ce système.

2.  Que se passe-t-il, dans l’ordre, entre le moment où une voiture arrive et celui où le portail s’ouvre ? (mesure $\to$ décision $\to$ action)

??? pouce "Coup de pouce"

    Que doit « sentir » le portail pour savoir qu’une voiture arrive ? Qu’est-ce qui le fait bouger ? Placez ensuite le programme entre les deux.

??? corrige "Corrigé"

    *(Portail automatique.)*

    1.  Capteur : détecteur de présence (ou récepteur de la télécommande/du badge). Actionneur : le **moteur** du portail.

    2.  Le capteur détecte la voiture (ou reçoit le signal) $\to$ le programme **décide** d’ouvrir $\to$ il commande le **moteur** (actionneur) $\to$ le portail s’ouvre.

### La boucle de commande

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 5</span> — Que fait ce programme ? <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-08-5 }

<span class="tag">sur papier</span>  On lit le programme d’un objet embarqué :

```python
while True:
    t = lire_temperature()
    if t > 25:
        allumer_ventilateur()
    else:
        eteindre_ventilateur()
    attendre(30)
```

1.  Quel est le **capteur** ? Quel est l’**actionneur** ?

2.  Décrire en une phrase ce que fait cet objet.

3.  Que se passe-t-il si la température mesurée est de $22\,^\circ$C ? de $28\,^\circ$C ?

??? pouce "Coup de pouce"

    Repérez la fonction qui *lit* une valeur (le capteur) et celles qui *agissent* (l’actionneur). Pour $22\,^\circ$C, la condition `t > 25` est-elle vraie ou fausse ?

??? corrige "Corrigé"

    1.  Capteur : le thermomètre (`lire_temperature`). Actionneur : le ventilateur.

    2.  L’objet **rafraîchit** la pièce : il allume le ventilateur dès que la température dépasse $25\,^\circ$C, et l’éteint sinon.

    3.  À $22\,^\circ$C : $22>25$ est faux $\to$ ventilateur **éteint**. À $28\,^\circ$C : $28>25$ est vrai $\to$ ventilateur **allumé**.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Dérouler une boucle <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-08-6 }

<span class="tag">sur papier</span>  Une veilleuse exécute le programme suivant :

```python
while True:
    lum = lire_luminosite()
    if lum < 40:
        allumer_lampe()
    else:
        eteindre_lampe()
    attendre(60)
```

Le capteur renvoie successivement $70$, $30$, $10$ puis $50$. Recopier et compléter le tableau :

| **Tour** | **`lum`** | **`lum < 40` ?** | **État de la lampe** |
|:--------:|:---------:|:----------------:|:--------------------:|
|    1     |    70     |                  |                      |
|    2     |    30     |                  |                      |
|    3     |    10     |                  |                      |
|    4     |    50     |                  |                      |

Combien de temps s’est-il écoulé entre la première et la dernière mesure ?

??? pouce "Coup de pouce"

    À chaque tour, on lit une nouvelle valeur, on teste la condition (vraie ou fausse), puis on exécute *une seule* des deux branches. Le programme attend $60$ s à la fin de chaque tour.

??? corrige "Corrigé"

    | **Tour** | **`lum`** | **`lum < 40` ?** |  **État de la lampe**   |
    |:--------:|:---------:|:----------------:|:-----------------------:|
    |    1     |    70     |       faux       |         éteinte         |
    |    2     |    30     |       vrai       |         allumée         |
    |    3     |    10     |       vrai       | allumée (elle le reste) |
    |    4     |    50     |       faux       |         éteinte         |

    Entre la première et la dernière mesure, il y a trois attentes de $60$ s : **3 minutes**.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Compléter un arrosage automatique <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-7 }

<span class="tag">sur machine</span>  Un système arrose une plante dès que la terre est trop sèche : l’humidité `h` passe sous `40`. Recopier et compléter :

```python
while True:
    h = lire_humidite()
    if ... :                     # (a) condition
        ...                      # (b) ouvrir la pompe
    else:
        fermer_pompe()
    attendre(3600)               # on re-teste chaque heure
```

??? pouce "Coup de pouce"

    La condition (a) traduit « l’humidité passe sous $40$ » avec `<`. L’action (b) fait le contraire de celle écrite sous le `else`.

??? corrige "Corrigé"

    ```python
    while True:
        h = lire_humidite()
        if h < 40:                   # (a) la terre est trop seche
            ouvrir_pompe()           # (b)
        else:
            fermer_pompe()
        attendre(3600)
    ```

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 8</span> — Défi — une alarme <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-8 }

<span class="tag">sur machine</span>  Écrire une boucle de commande pour une **alarme** : tant qu’elle fonctionne, si le détecteur de mouvement renvoie `True` (`detecte()`), elle déclenche la sirène (`sonner()`) et allume une LED (`allumer_led()`) ; sinon elle éteint tout. On testera dix fois par seconde.

??? pouce "Coup de pouce"

    Même structure que l’arrosage : `while True`, une lecture du capteur dans un `if`, un `else`, puis une attente. Pour « éteindre tout », on dispose de `eteindre_sirene()` et `eteindre_led()`. Dix fois par seconde : combien de secondes attendre entre deux tests ?

??? pouce "Coup de pouce 2 (début de solution)"

    `while True:`  
    `if detecte():`  
    `sonner()`  
    `allumer_led()`  
    (il reste le `else` et l’attente.)

??? corrige "Corrigé"

    ```python
    while True:
        if detecte():                # mouvement detecte
            sonner()
            allumer_led()
        else:
            eteindre_sirene()
            eteindre_led()
        attendre(0.1)                # 10 fois par seconde
    ```

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 9</span> — Le thermostat à deux seuils <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-9 }

<span class="tag">sur machine</span>  Le thermostat du cours allume le chauffage sous $19\,^\circ$C et l’éteint sinon : autour de $19\,^\circ$C, le radiateur s’allume et s’éteint sans arrêt, ce qui l’use. On veut un thermostat plus malin : il **allume** le chauffage si la température passe sous $19\,^\circ$C, l’**éteint** si elle dépasse $21\,^\circ$C, et **ne change rien** entre les deux.

1.  Écrire cette boucle de commande (une mesure par minute).

2.  Le chauffage est éteint et la pièce est à $20\,^\circ$C. Que fait le programme ? Et si le chauffage était allumé ?

??? pouce "Coup de pouce"

    Il y a trois cas : sous $19$, au-dessus de $21$, et entre les deux. Pour « ne rien changer », il suffit de ne commander aucun actionneur : pas besoin de `else`.

??? pouce "Coup de pouce 2 (début de solution)"

    `while True:`  
    `t = lire_temperature()`  
    `if t < 19:`  
    `allumer_chauffage()`  
    `elif` …

??? corrige "Corrigé"

    1.  Trois cas ; entre $19$ et $21\,^\circ$C, on ne commande rien (pas de `else`) :

        ```python
        while True:
            t = lire_temperature()
            if t < 19:
                allumer_chauffage()      # trop froid
            elif t > 21:
                eteindre_chauffage()     # trop chaud
            attendre(60)                 # entre 19 et 21 : on ne change rien
        ```

    2.  À $20\,^\circ$C, aucune des deux conditions n’est vraie : le programme **ne change rien**. Le chauffage éteint **reste éteint** ; s’il était allumé, il **reste allumé** (jusqu’à dépasser $21\,^\circ$C). Le radiateur ne bascule donc plus sans arrêt autour d’un seul seuil.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 10</span> — Le compteur de passages <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-10 }

<span class="tag">sur machine</span>  À l’entrée d’une petite salle, un détecteur `detecte()` renvoie `True` quand quelqu’un passe. On veut **compter** les entrées, afficher le total sur un écran (`afficher(n)`) et déclencher un signal sonore (`sonner()`) dès que plus de $20$ personnes sont entrées.

1.  Écrire la boucle de commande (dix tests par seconde).

2.  Une personne reste une demi-seconde devant le détecteur. Quel problème cela pose-t-il ? Proposer une solution simple.

??? pouce "Coup de pouce"

    Il faut une variable qui garde le nombre d’entrées d’un tour de boucle à l’autre : où la créer, avant ou dans la boucle ?

??? pouce "Coup de pouce 2 (début de solution)"

    `nb = 0`  
    `while True:`  
    `if detecte():`  
    `nb = nb + 1`  
    (il reste l’affichage, le test des $20$ personnes et l’attente.)

??? corrige "Corrigé"

    1.  Le compteur `nb` est créé **avant** la boucle (sinon il repartirait de $0$ à chaque tour) :

        ```python
        nb = 0
        while True:
            if detecte():
                nb = nb + 1
                afficher(nb)
                if nb > 20:
                    sonner()
            attendre(0.1)                # 10 tests par seconde
        ```

    2.  En une demi-seconde, la boucle teste $5$ fois le détecteur : la même personne serait **comptée $5$ fois**. Solution simple : après une détection, attendre une seconde avant de reprendre les tests (ajouter `attendre(1)` juste après `afficher(nb)`) ; ou ne compter que lorsque le détecteur passe de `False` à `True`.

### L’interface homme-machine (IHM)

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 11</span> — Entrées et sorties <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-08-11 }

<span class="tag">sur papier</span>  Pour un **four à micro-ondes**, citer deux éléments d’**entrée** (l’humain vers la machine) et deux éléments de **sortie** (la machine vers l’humain).

??? corrige "Corrigé"

    *(Four à micro-ondes.)* **Entrées** : les boutons / la molette (durée, puissance), le bouton « départ ». **Sorties** : l’écran (temps restant), le **bip** de fin, la lumière intérieure.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 12</span> — Bonne ou mauvaise IHM ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-12 }

<span class="tag">sur papier</span>  On appuie sur le bouton d’un objet, mais *rien* ne semble se passer (ni voyant, ni son, ni affichage). Pourquoi est-ce une **mauvaise** IHM ? Que faudrait-il ajouter ?

??? pouce "Coup de pouce"

    Relisez la règle « Une bonne IHM » du cours : que doit-il se passer juste après un appui sur un bouton ?

??? corrige "Corrigé"

    Sans aucun **retour**, l’utilisateur ne sait pas si son appui a été pris en compte : il doute, ré-appuie, se trompe. Il faudrait ajouter un **retour** : un voyant/une LED, un bip, ou un message à l’écran confirmant l’action.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 13</span> — Concevoir une IHM <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-08-13 }

<span class="tag">sur papier</span>  On conçoit un **pot de fleurs connecté** qui mesure l’humidité de la terre et peut arroser tout seul.

1.  Proposer une **entrée** (pour que l’utilisateur commande le pot) et deux **sorties** (pour qu’il soit informé). Justifier chaque choix en une phrase.

2.  L’utilisateur lance un arrosage à la main. Quel **retour** le pot doit-il lui donner ?

??? pouce "Coup de pouce"

    Entrées : par quoi l’humain agit-il sur un objet (bouton, écran tactile, application, voix…) ? Sorties : comment l’objet informe-t-il (voyant, son, écran, notification) ? Pensez à ce que l’utilisateur a besoin de savoir : la terre est-elle sèche ? l’arrosage a-t-il commencé ?

??? corrige "Corrigé"

    1.  Par exemple. **Entrée** : un bouton « arroser maintenant » (ou une application sur le téléphone), pour déclencher l’arrosage à la main. **Sorties** : un voyant qui passe au rouge quand la terre est sèche (on voit d’un coup d’œil l’état de la plante) ; une notification sur le téléphone quand le réservoir d’eau est vide (on est prévenu même absent).

    2.  Un **retour** immédiat : un voyant qui clignote ou un bip au début de l’arrosage, puis un signal à la fin. Sans retour, l’utilisateur ne sait pas si son appui a été pris en compte.

### Objets connectés, sécurité et vie privée

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 14</span> — Objet connecté <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-08-14 }

<span class="tag">sur papier</span> 

1.  Qu’est-ce qui distingue un **objet connecté** d’un simple objet embarqué ?

2.  Citer deux objets connectés et, pour chacun, une donnée qu’il transmet.

??? corrige "Corrigé"

    1.  Un objet connecté est **relié au réseau** et **échange des données** ; un objet seulement embarqué ne communique pas.

    2.  Exemples : montre connectée $\to$ rythme cardiaque / nombre de pas ; caméra $\to$ images ; thermostat $\to$ température (au choix).

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 15</span> — Le danger des mots de passe par défaut <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-15 }

<span class="tag">sur papier</span>  En 2016, le logiciel **Mirai** a détourné des centaines de milliers de caméras connectées pour saturer de grands sites.

1.  Quelle négligence des propriétaires a rendu l’attaque possible ?

2.  En quoi un objet connecté mal sécurisé met-il en danger **plus** que son seul propriétaire ?

3.  Citer deux gestes simples pour sécuriser un objet connecté.

??? pouce "Coup de pouce"

    Que font la plupart des gens du mot de passe écrit dans la notice ? Et des centaines de milliers d’objets piratés, que peuvent-ils faire *ensemble* ?

??? corrige "Corrigé"

    *(Mirai.)*

    1.  Les propriétaires n’avaient jamais **changé le mot de passe par défaut** (souvent `admin`/`admin`).

    2.  L’objet piraté devient un « robot » qui participe à une **attaque** (déni de service) contre d’autres sites : il nuit à *tout* Internet, pas seulement à son propriétaire.

    3.  Changer le mot de passe par défaut ; installer les **mises à jour** (et couper l’objet quand il ne sert pas).

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 16</span> — Vie privée <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-16 }

<span class="tag">sur papier</span>  Une enceinte connectée « écoute » pour réagir à la voix de ses utilisateurs. Expliquer, en deux phrases, en quoi cela pose une question de **vie privée**, et quel texte protège les données personnelles en France (et dans l’UE) ; et à Monaco ?

??? corrige "Corrigé"

    Une enceinte qui « écoute » en permanence peut enregistrer des conversations privées et les envoyer vers un serveur : ce sont des **données personnelles**, dont l’usage est encadré en France (et dans l’UE) par le **RGPD** (autorité : CNIL). Monaco n’étant pas dans l’UE, c’est la **loi n° 1.565 du 3 décembre 2024** qui s’y applique (autorité : APDP).

### Critiquer une réponse d’IA

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 17</span> — Le volet automatique d’un assistant <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> { #ex-08-17 }

<span class="tag">sur papier</span>  Un élève a demandé à un assistant d’IA : « Écris la boucle de commande d’un volet roulant qui se ferme quand la nuit tombe et s’ouvre quand il fait jour. Le capteur `lire_luminosite()` renvoie un nombre de `0` (nuit noire) à `100` (plein soleil). » Voici la réponse obtenue :

```python
while True:
    lum = lire_luminosite()      # ENTREE : le capteur -> un nombre
    if lum < 20:                 # il fait nuit
        ouvrir_volet()
    else:
        fermer_volet()
    attendre(60)                 # on re-teste chaque minute
```

1.  La réponse est-elle correcte ? Dérouler la boucle pour une mesure de nuit (`lum` $= 5$) puis de jour (`lum` $= 80$), et dire ce que fait le volet dans chaque cas.

2.  Localiser et corriger l’erreur.

    ??? pouce "Coup de pouce"

        Après avoir déroulé la boucle, comparez avec la demande de l’élève : de nuit, que doit faire le volet ?

3.  Quelle vérification simple, faite *avant* de faire confiance à cette réponse, aurait suffi à détecter l’erreur ?

??? corrige "Corrigé"

    1.  Non. La structure est la bonne (acquisition $\to$ décision $\to$ action $\to$ attente, comme le thermostat du cours), mais le déroulé donne : `lum` $= 5$ $\to$ condition vraie $\to$ `ouvrir_volet()` ; `lum` $= 80$ $\to$ condition fausse $\to$ `fermer_volet()`. Le volet s’**ouvre** la nuit et se **ferme** le jour : l’inverse de la demande.

    2.  L’erreur : les deux **actions** sont inversées dans le `if` / `else` (le commentaire « il fait nuit » est juste, l’action qui le suit ne l’est pas). Correction : `fermer_volet()` sous `if lum < 20:` et `ouvrir_volet()` sous `else:`.

    3.  Dérouler la boucle « à la main » avec **une valeur de chaque côté du seuil** (une mesure de nuit, une de jour) avant d’accepter le programme : c’est exactement la vérification de l’exercice 5.

### Impact environnemental

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 18</span> — L’empreinte d’un smartphone <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-08-18 }

<span class="tag">sur papier</span>  D’après l’outil *Impact CO2* de l’ADEME (données ADEME–Arcep 2025, consulté en 2026 ; voir le document du cours), un smartphone émet environ `80` kg de CO$_2$e sur toute sa vie, dont `99` % lors de sa **fabrication** ; le calcul suppose qu’il est gardé `2,5` ans. On néglige ici l’usage et la fin de vie.

1.  Calculer les émissions **par année d’utilisation** si le téléphone est gardé 2,5 ans.

2.  Même question s’il est gardé **5 ans**. Conclure.

3.  Pourquoi éteindre son téléphone la nuit a-t-il un effet bien plus faible que de le garder plus longtemps ?

4.  Citer deux raisons qui poussent à changer de téléphone ou d’objet connecté trop tôt, et un moyen d’y remédier.

??? pouce "Coup de pouce"

    Divisez les $80$ kg par le nombre d’années. Où sont émis $99\,\%$ des gaz : pendant l’usage ou à la fabrication ?

??? corrige "Corrigé"

    1.  $80 \div 2{,}5 = 32$ : environ **32 kg de CO$_2$e par an**.

    2.  $80 \div 5 = 16$ : environ **16 kg de CO$_2$e par an**. Garder le téléphone deux fois plus longtemps divise environ **par deux** son empreinte annuelle, car la fabrication (99 %) est « amortie » sur plus d’années.

    3.  Éteindre le téléphone ne réduit que la part « usage », qui ne pèse qu’environ 1 % ici ; garder le téléphone plus longtemps agit sur la fabrication, qui pèse environ 99 %.

    4.  Raisons : batterie usée, écran cassé difficile à réparer, **mises à jour** de sécurité qui s’arrêtent, mode, stockage plein… Remèdes : faire réparer (changer la batterie ou l’écran), choisir un modèle réparable et suivi longtemps, acheter reconditionné.
