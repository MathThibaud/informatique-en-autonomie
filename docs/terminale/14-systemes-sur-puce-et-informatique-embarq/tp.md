# TP et projets

<p class="sous-titre">Systèmes sur puce et informatique embarquée</p>

## <span class="etiquette">TP</span> Programmer un système embarqué

*capteurs, boucle temps réel et système sur puce avec le micro:bit*

<p class="infos-activite">Durée : 2 h 30 à 3 h (deux séances) · Sur machine, par deux</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/terminale/14-tp-soc){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/terminale-14-tp-soc.zip){ .md-button }

!!! consignes "Consignes"

    - Parties A et B : éditeur Python officiel du micro:bit , `python.microbit.org`, avec son **simulateur** (curseurs des capteurs sous la carte ; la sortie de `print` s’affiche dans la console série, sous l’éditeur). Si des cartes réelles sont disponibles, transférer le programme sur la carte avec le bouton « Send to micro:bit ».

    - Parties C et D : Python habituel sur l’ordinateur, avec le fichier à télécharger `tp_soc_depart.py`.

    - Niveau : ★ échauffement, ★★ classique (niveau bac), ★★★ défi ; les *coups de pouce* et les *corrigés* se déplient sous chaque exercice. Le symbole <span class="run" title="À programmer et tester sur machine">▶</span>  signale ce qui est à programmer et tester.

    - Usage de l’IA, indiqué sur chaque exercice : <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> aucune ; <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> en appui (déboguer, reformuler, vérifier ; la réponse finale est écrite et comprise par vous) ; <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> l’exercice s’appuie sur une réponse d’IA. Voir la [charte d’usage de l’IA](../charte.md).

!!! encadre "But du TP"

    Construire de vrais **systèmes embarqués** — une veilleuse, une alarme, un podomètre — sur le modèle **capteur $\to$ traitement $\to$ actionneur**, mesurer le **rythme** de leur boucle et leur **consommation**, **tester leur logique** sur ordinateur avec des capteurs simulés, puis **analyser la puce** qui les fait tourner et la comparer à celle d’un PC. *Produit final* : trois programmes embarqués qui fonctionnent, et une fiche d’analyse du système sur puce.

**Aide-mémoire micro:bit (MicroPython).** Toujours commencer par `from microbit import *`.

| **Instruction** | **Rôle** |
|:---|:---|
| `temperature()` | température en degrés (entier) |
| `display.read_light_level()` | lumière ambiante, de $0$ (noir) à $255$ (plein jour) |
| `accelerometer.get_values()` | triplet `(x, y, z)` d’accélérations en milli-$g$ |
| `button_a.was_pressed()` | `True` si A a été pressé depuis le dernier appel |
| `display.set_pixel(x, y, v)` | allume la LED de colonne `x`, ligne `y` (de $0$ à $4$), intensité `v` de $0$ à $9$ |
| `display.show(Image.HEART)`, `display.clear()` | affiche une image ; éteint l’écran |
| `display.scroll("texte")` | fait défiler un texte (et **attend** la fin du défilement) |
| `sleep(n)`, `running_time()` | attend `n` millisecondes ; temps écoulé depuis le démarrage, en ms |
| `import music` puis `music.pitch(880, 100)` | joue un son de $880$ Hz pendant $100$ ms |

## Partie A — La boucle et son rythme

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 1</span> — Combien de tours par seconde ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-14-systemes-sur-puce-et-informatique-embarq-tp-1-1 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Taper et lancer ce programme, puis ouvrir la console série.

```python
from microbit import *

n = 0
debut = running_time()
while True:
    n = n + 1
    if running_time() - debut >= 1000:    # une seconde s'est ecoulee
        print(n)
        n = 0
        debut = running_time()
```

1.  Que représente le nombre affiché chaque seconde ? Noter sa valeur (approximative).

2.  Ce programme a-t-il un capteur ? un actionneur ? Que fait-il de « utile » ?

3.  *(Si une carte réelle est disponible.)* Refaire la mesure sur la carte. Pourquoi la valeur peut-elle être différente de celle du simulateur ?

??? corrige "Corrigé"

    - Podomètre : **acquisition** (accéléromètre, $50$ mesures par seconde), **contrôle** (compter, afficher à l’écran), **temps** (la boucle doit tourner assez vite pour ne pas rater un pas : pas d’instruction bloquante).

    - Hystérésis : deux seuils écartés pour ignorer le bruit autour d’un seuil unique (15 basculements contre 1 ; 26 pas comptés au lieu de 20, 24 au lieu de 10).

    - Une veilleuse ou un podomètre n’a besoin ni de GHz, ni de Go : la puce consomme environ $1\,000$ fois moins qu’un PC (des mois sur deux piles en mode veille), coûte quelques euros et tient dans un objet de quelques centimètres.

    **1.** Le nombre de passages dans la boucle pendant une seconde, c’est-à-dire sa **fréquence** (de quelques milliers à quelques dizaines de milliers de tours par seconde ; valeur variable selon le simulateur et la carte).

    **2.** Aucun capteur au sens du cours (seulement l’horloge interne `running_time()`), aucun actionneur ; il ne fait rien d’utile : il mesure seulement la vitesse de la boucle.

    **3.** Le simulateur ne reproduit pas la vitesse réelle du processeur : il émule la carte dans le navigateur, avec la puissance de l’ordinateur. Sur la carte, la valeur dépend du processeur à $64$ MHz et de l’interpréteur MicroPython.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 2</span> — Ce qui ralentit la boucle <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-14-systemes-sur-puce-et-informatique-embarq-tp-1-2 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Ajouter successivement, dans la boucle (juste après `n = n + 1`), chacune des lignes suivantes, et relever le nombre de tours par seconde dans le tableau, recopié sur le cahier.

| **Ligne ajoutée**                      | **Tours par seconde** |
|:---------------------------------------|:---------------------:|
| (rien)                                 |                       |
| `x, y, z = accelerometer.get_values()` |                       |
| `sleep(20)`                            |                       |
| `display.scroll("Hi")`                 |                       |
| `display.scroll("Hi", wait=False)`     |                       |

1.  Avec `sleep(20)`, quel est le nombre **maximal** de tours par seconde ? Le comparer à la mesure.

2.  Avec `display.scroll("Hi")`, la carte lit-elle encore ses capteurs pendant le défilement ? Imaginer les conséquences pour un **airbag** ou un **podomètre**.

3.  Quel est l’effet de `wait=False` ? Énoncer une règle de programmation d’un système **temps réel**.

??? corrige "Corrigé"

    | **Ligne ajoutée** | **Tours par seconde (ordre de grandeur)** |
    |:---|:---|
    | (rien) | des milliers, voire des dizaines de milliers |
    | lecture de l’accéléromètre | moins (il faut interroger le capteur à chaque tour) |
    | `sleep(20)` | un peu moins de $50$ |
    | `display.scroll("Hi")` | $1$ affiché (chaque tour dure plus d’une seconde) |
    | `display.scroll("Hi", wait=False)` | de nouveau beaucoup (le défilement ne bloque plus) |

    **1.** Chaque tour dure au moins $20$ ms, donc au plus $1000 / 20 = 50$ tours par seconde ; on mesure un peu moins, car le reste du tour prend aussi du temps.

    **2.** Non : pendant le défilement, le programme est **bloqué** dans `scroll` et ne lit plus aucun capteur. Un airbag réagirait avec plus d’une seconde de retard ; un podomètre raterait les pas faits pendant l’affichage.

    **3.** Avec `wait=False`, le défilement se fait « en arrière-plan » et la boucle continue aussitôt (relancé à chaque tour, le texte n’a d’ailleurs pas le temps de défiler : on ne lance un affichage qu’en cas de besoin). Règle : **dans la boucle d’un système temps réel, aucune instruction ne doit bloquer longtemps** ; la durée d’un tour doit rester petite devant le temps de réaction exigé.

## Partie B — Trois systèmes embarqués

Pour chaque système, on identifie d’abord **capteur**, **traitement** et **actionneur**, puis on programme la boucle.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 3</span> — Une veilleuse qui s’allume avec la nuit <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-14-systemes-sur-puce-et-informatique-embarq-tp-1-3 }

La veilleuse allume d’autant plus de LED qu’il fait sombre : $0$ LED en plein jour (lumière $255$), les $25$ dans le noir complet (lumière $0$). On calcule ce nombre avec `(255 - lumiere) * 25 // 255`.

1.  Combien de LED pour une lumière de $128$ ? de $200$ ?

2.  <span class="run" title="À programmer et tester sur machine">▶</span>  Compléter les pointillés dans l’éditeur et tester le programme (faire varier le curseur de lumière du simulateur). Les LED se remplissent ligne par ligne : la LED numéro `k` (de $0$ à $24$) est en colonne `k % 5` et en ligne `k // 5`.

    ```python
    from microbit import *

    while True:
        lumiere = ...............................
        nb = ....................................
        display.clear()
        for k in range(nb):
            display.set_pixel(.........., .........., 9)
        sleep(200)
    ```

3.  Identifier le capteur, le traitement et l’actionneur. Pourquoi `sleep(200)` est-il raisonnable ici, et ne le serait-il pas pour un frein ABS ?

??? corrige "Corrigé"

    **1.** $(255-128) \times 25 \,//\, 255 = 3175 \,//\, 255 = 12$ LED ; $(255-200) \times 25 \,//\, 255 = 1375 \,//\, 255 = 5$ LED.

    **2.**

    ```python
    from microbit import *

    while True:
        lumiere = display.read_light_level()
        nb = (255 - lumiere) * 25 // 255
        display.clear()
        for k in range(nb):
            display.set_pixel(k % 5, k // 5, 9)
        sleep(200)
    ```

    **3.** Capteur : le capteur de lumière (les LED elles-mêmes) ; traitement : le calcul de `nb` ; actionneur : les LED de l’écran. La lumière ambiante varie lentement : la regarder $5$ fois par seconde suffit largement. Un frein ABS doit réagir en quelques millisecondes : $200$ ms de pause serait beaucoup trop.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 4</span> — Une alarme de température qui ne panique pas <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-14-systemes-sur-puce-et-informatique-embarq-tp-1-4 }

Un local technique ne doit pas dépasser $30$ degrés. Cahier des charges :

- l’alarme **se déclenche** dès que la température atteint $30$ degrés : image `Image.NO` et un bip (`music.pitch(880, 100)`) à chaque tour ;

- elle ne **s’arrête** que lorsque la température est redescendue à $28$ degrés ou moins (entre $28$ et $30$, elle garde son état précédent) : c’est une **hystérésis** ;

- le bouton A **coupe le son** de l’alarme en cours (l’image reste) ; le son reviendra à la prochaine alarme ;

- le bouton B fait défiler la température **minimale** et **maximale** relevées depuis le démarrage, sous la forme `"22/31"`.

1.  Dresser sur le cahier un tableau donnant l’état de l’alarme (déclenchée ou non) pour la suite de températures : $26,\ 29,\ 30,\ 31,\ 29,\ 30,\ 29,\ 28,\ 27$.

2.  <span class="run" title="À programmer et tester sur machine">▶</span>  Écrire le programme complet. On utilisera trois variables : `en_alarme`, `son_coupe` et le couple `mini`, `maxi`.

3.  Pourquoi ne pas ranger *toutes* les températures dans une liste pour calculer le minimum et le maximum à la demande ? (Penser à la mémoire vive d’un microcontrôleur, et à une alarme qui fonctionne des mois.)

??? corrige "Corrigé"

    **1.**

    | Température | 26  | 29  |   30    | 31  | 29  | 30  | 29  | 28  | 27  |
    |:------------|:---:|:---:|:-------:|:---:|:---:|:---:|:---:|:---:|:---:|
    | Alarme      | non | non | **oui** | oui | oui | oui | oui | non | non |

    À $29$ (entre $28$ et $30$), l’alarme garde son état : éteinte la première fois, allumée ensuite.

    **2.**

    ```python
    from microbit import *
    import music

    en_alarme = False
    son_coupe = False
    mini = temperature()
    maxi = mini
    while True:
        t = temperature()
        if t < mini:
            mini = t
        if t > maxi:
            maxi = t
        if t >= 30:
            en_alarme = True
        elif t <= 28:
            en_alarme = False
            son_coupe = False            # le son reviendra a la prochaine alarme
        if button_a.was_pressed() and en_alarme:
            son_coupe = True
        if button_b.was_pressed():
            display.scroll(str(mini) + "/" + str(maxi))
        if en_alarme:
            display.show(Image.NO)
            if not son_coupe:
                music.pitch(880, 100)
        else:
            display.clear()
        sleep(200)
    ```

    *À noter* : sans le test `and en_alarme`, un appui sur A hors alarme couperait par avance le son de la prochaine alarme ; `display.scroll` bloque la boucle environ deux secondes (acceptable ici : la température varie lentement).

    **3.** Une liste qui grandit à chaque tour ($5$ mesures par seconde, soit $432\,000$ par jour) saturerait vite les $128$ Ko de mémoire vive, et le programme planterait au bout de quelques heures. Deux variables `mini` et `maxi` suffisent et occupent une place constante, quelle que soit la durée de fonctionnement.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 5</span> — Un podomètre <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-14-systemes-sur-puce-et-informatique-embarq-tp-1-5 }

Quand on marche, la carte (à la ceinture) est secouée à chaque pas. On mesure la **norme** de l’accélération $\sqrt{x^2+y^2+z^2}$ : au repos, elle vaut environ $1000$ milli-$g$ (la pesanteur), et elle oscille au-dessus et au-dessous à chaque pas.

1.  Calculer la norme pour `(0, 0, -1024)` et pour `(300, -400, 1000)`.

2.  <span class="run" title="À programmer et tester sur machine">▶</span>  Écrire un programme qui, environ $50$ fois par seconde, calcule la norme (`import math`, puis `math.sqrt`) et compte un pas **quand la norme passe au-dessus de $1250$** ; pour compter le pas suivant, il faut d’abord que la norme soit **redescendue sous $1050$**. Une variable booléenne `en_haut` mémorise si l’on est déjà au-dessus. Le bouton A affiche le nombre de pas (sans bloquer la boucle), le bouton B le remet à zéro.

    ??? pouce "Coup de pouce"

        La boucle contient deux tests sur la norme : `if not en_haut and a > 1250:` (on vient de franchir le seuil haut : on compte un pas et on passe `en_haut` à `True`), et `elif en_haut and a < 1050:` (on est redescendu : `en_haut` repasse à `False`).

3.  <span class="run" title="À programmer et tester sur machine">▶</span>  Tester dans le simulateur en faisant varier le curseur de l’axe `z` (ou avec le geste « secouer »), puis, si possible, en marchant avec une vraie carte.

??? corrige "Corrigé"

    **1.** $\sqrt{0+0+1024^2} = 1024$ ; $\sqrt{300^2+400^2+1000^2} = \sqrt{1\,250\,000} \approx 1118$.

    **2.**

    ```python
    from microbit import *
    import math

    pas = 0
    en_haut = False
    while True:
        x, y, z = accelerometer.get_values()
        a = math.sqrt(x * x + y * y + z * z)
        if not en_haut and a > 1250:
            en_haut = True
            pas = pas + 1
        elif en_haut and a < 1050:
            en_haut = False
        if button_a.was_pressed():
            display.scroll(str(pas), wait=False)
        if button_b.was_pressed():
            pas = 0
            display.clear()
        sleep(20)                        # environ 50 mesures par seconde
    ```

    **3.** Dans le simulateur, chaque passage du curseur `z` au-delà de $1250$ (en valeur absolue) puis retour vers $1000$ compte un pas ; un aller-retour qui reste entre $1050$ et $1250$ n’en compte pas.

## Partie C — Tester la logique sans la carte

Tester un programme embarqué sur la carte est lent et peu reproductible (on ne marche pas deux fois de la même façon !). Une bonne pratique consiste à isoler la partie **traitement** dans des fonctions *sans capteur ni actionneur*, que l’on teste sur ordinateur avec des **capteurs simulés** : des listes de mesures. Ouvrir `tp_soc_depart.py` et le lancer : il affiche l’état des tests.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 6</span> — Les fonctions de traitement <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-14-systemes-sur-puce-et-informatique-embarq-tp-1-6 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Compléter, dans l’ordre, `veilleuse`, `nb_basculements`, `nb_led`, `alarme`, `mise_a_jour`, `norme`, `compter_pas_naif` et `compter_pas` (leur rôle est décrit dans le fichier), jusqu’à ce que tous les tests affichent `OK`. Ce sont exactement les décisions prises dans vos programmes de la partie B.

??? corrige "Corrigé"

    ```python
    def veilleuse(lumiere, allumee, seuil_bas=40, seuil_haut=80):
        if lumiere < seuil_bas:
            return True
        if lumiere > seuil_haut:
            return False
        return allumee

    def nb_basculements(etats):
        c = 0
        for i in range(1, len(etats)):
            if etats[i] != etats[i - 1]:
                c += 1
        return c

    def nb_led(lumiere):
        return (255 - lumiere) * 25 // 255

    def alarme(temp, en_alarme, seuil=30, retour=28):
        if temp >= seuil:
            return True
        if temp <= retour:
            return False
        return en_alarme

    def mise_a_jour(mini, maxi, temp):
        if temp < mini:
            mini = temp
        if temp > maxi:
            maxi = temp
        return (mini, maxi)

    def norme(x, y, z):
        return math.sqrt(x * x + y * y + z * z)

    def compter_pas_naif(normes, seuil=1200):
        pas = 0
        for i in range(1, len(normes)):
            if normes[i - 1] <= seuil < normes[i]:
                pas += 1
        return pas

    def compter_pas(normes, haut=1250, bas=1050):
        pas = 0
        en_haut = False
        for a in normes:
            if not en_haut and a > haut:
                en_haut = True
                pas += 1
            elif en_haut and a < bas:
                en_haut = False
        return pas
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Pourquoi deux seuils ? Les mesures parlent <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-14-systemes-sur-puce-et-informatique-embarq-tp-1-7 }

1.  <span class="run" title="À programmer et tester sur machine">▶</span>  La fonction fournie `lumiere_simulee()` renvoie $70$ niveaux de lumière relevés en fin de journée. Afficher le nombre de basculements de la veilleuse **naïve** (un seul seuil à $60$) et de la veilleuse **à hystérésis** :  
    `nb_basculements(simuler_veilleuse(niveaux, False))`, puis avec `True`. Pourquoi la veilleuse naïve « clignote »-t-elle ?

2.  <span class="run" title="À programmer et tester sur machine">▶</span>  `marche_simulee()` simule $10$ secondes de marche à $2$ pas par seconde. Comparer les nombres de pas trouvés par `compter_pas_naif` et par `compter_pas`. Lequel a raison ?

3.  <span class="run" title="À programmer et tester sur machine">▶</span>  Recommencer avec une marche lente, d’un pas par seconde, obtenue par `marche_simulee(cadence=1,` `graine=3)`. Combien de pas devrait-on trouver ? Qu’est-ce qui, dans le signal, trompe le compteur naïf ?

4.  <span class="run" title="À programmer et tester sur machine">▶</span>  Vérifier qu’au repos (une liste de $500$ valeurs tirées entre $940$ et $1060$) aucun des deux compteurs ne compte de pas.

??? corrige "Corrigé"

    **1.** Veilleuse naïve : **15** basculements ; à hystérésis : **1** seul. Au crépuscule, la lumière mesurée hésite autour de $60$ (entre $45$ et $75$ avec le bruit) : avec un seul seuil, chaque petite variation fait changer d’état. Avec deux seuils écartés ($40$ et $80$), il faut une vraie variation pour basculer.

    **2.** Naïf : **26** pas ; à hystérésis : **20** pas. La marche dure $10$ s à $2$ pas par seconde : il y a $20$ pas, c’est `compter_pas` qui a raison. (Avec les graines $1$ à $10$, le naïf trouve entre $21$ et $28$ pas, l’autre toujours $20$.)

    **3.** On attend $10$ pas ; le naïf en compte **24**, `compter_pas` exactement **10**. Quand le signal monte lentement, il passe longtemps près du seuil, et le **bruit** le fait franchir le seuil plusieurs fois au cours d’un même pas : chaque franchissement est compté.

    **4.**

    ```python
    repos = [random.randint(940, 1060) for i in range(500)]
    print(compter_pas_naif(repos), compter_pas(repos))      # 0 0
    ```

## Partie D — Consommation : combien de temps sur deux piles ?

On travaille avec des **ordres de grandeur** (hypothèses de l’exercice) : la carte est alimentée par deux piles AAA de capacité $1\,000$ mAh (elles peuvent fournir $1\,000$ mA pendant $1$ h, ou $10$ mA pendant $100$ h…) ; en fonctionnement, la carte consomme environ $30$ mA ; en **veille**, un microcontrôleur peut descendre vers $0{,}01$ mA.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — Faire durer les piles <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-14-systemes-sur-puce-et-informatique-embarq-tp-1-8 }

1.  Combien de temps (en heures, puis en jours) la carte tourne-t-elle si elle reste toujours active ?

2.  La veilleuse n’a pas besoin de regarder la lumière $5$ fois par seconde. On suppose qu’elle est active $1\,\%$ du temps et en veille le reste. Calculer le courant moyen $I = 0{,}01 \times 30 + 0{,}99 \times 0{,}01$, puis l’autonomie. Quel facteur a-t-on gagné ?

3.  Un smartphone a une batterie d’environ $4\,000$ mAh qui tient à peu près une journée d’utilisation. Quel est son courant moyen ? Combien de fois plus que la carte active ?

4.  <span class="run" title="À programmer et tester sur machine">▶</span>  Sur l’ordinateur, mesurer le nombre de tours par seconde d’une boucle vide semblable à celle de l’exercice 1 :

    ```python
    import time
    n = 0
    debut = time.time()
    while time.time() - debut < 1:
        n = n + 1
    print(n)
    ```

    Comparer avec la mesure de l’exercice 1. Qu’est-ce qui explique l’écart ? Qu’est-ce que l’on paie, en échange de cette vitesse ?

??? corrige "Corrigé"

    **1.** $1\,000 / 30 \approx 33$ h, soit environ **1,4 jour**.

    **2.** $I = 0{,}3 + 0{,}0099 = 0{,}3099$ mA ; autonomie $1\,000 / 0{,}3099 \approx 3\,227$ h, soit environ **134 jours**. On a gagné un facteur de l’ordre de **100** : un objet embarqué passe l’essentiel de son temps à *dormir*.

    **3.** $4\,000 / 24 \approx 167$ mA, environ $5{,}5$ fois le courant de la carte active (et environ $500$ fois celui de la veilleuse économe).

    **4.** Sur l’ordinateur de préparation (Python 3), la boucle vide fait environ **8 millions** de tours par seconde, bien plus que la carte. Écart : processeur à plusieurs GHz contre $64$ MHz, architecture plus performante (caches, plusieurs instructions par cycle). En échange : une consommation des milliers de fois plus grande, un prix et un encombrement bien supérieurs, un ventilateur…

## Partie E — Analyse : la puce du micro:bit face à un PC

La carte micro:bit (version 2) est construite autour d’une seule puce, le **nRF52833** (Nordic Semiconductor), qui contient : un cœur de processeur ARM Cortex-M4 à $64$ MHz, $512$ Ko de mémoire Flash, $128$ Ko de mémoire vive, une radio Bluetooth, un convertisseur analogique-numérique et des minuteries. Il n’y a **aucun système d’exploitation** : au démarrage, la puce exécute directement l’interpréteur MicroPython rangé en Flash, qui exécute à son tour votre programme.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 9</span> — Fiche d’analyse <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-14-systemes-sur-puce-et-informatique-embarq-tp-1-9 }

1.  Recopier et compléter le tableau (pour le PC, prendre un ordinateur de bureau typique : processeur à $8$ cœurs à $3{,}5$ GHz, $16$ Go de mémoire vive, consommation de l’ordre de $100$ W).

|  | **nRF52833 (micro:bit )** | **PC de bureau** | **Rapport PC / micro:bit** |
|:---|:--:|:--:|:--:|
| Fréquence | $64$ MHz |  |  |
| Nombre de cœurs |  |  |  |
| Mémoire vive | $128$ Ko |  |  |
| Puissance électrique | $\approx 0{,}1$ W ($3$ V $\times$ $30$ mA) |  |  |
| Système d’exploitation |  |  | — |
| Composants | une seule puce |  | — |

1.  Parmi les composants du nRF52833, lesquels jouent le rôle de **processeur**, de **mémoire**, d’**entrées-sorties** ? En quoi est-ce un **système sur puce** ? Est-ce plutôt un microcontrôleur ou un SoC de téléphone ? Justifier avec deux critères du cours.

2.  Le programme est en Flash, les variables en mémoire vive, et le processeur lit instruction et donnée par deux bus distincts. Quel nom porte cette architecture ? Quel avantage apporte-t-elle ?

3.  Pourquoi un système d’exploitation n’est-il ni nécessaire, ni même souhaitable pour l’alarme de la partie B ? Quel est l’inconvénient de MicroPython (un **interpréteur**) par rapport à un programme compilé en langage machine ?

4.  Si la radio Bluetooth de la puce tombe en panne, que faut-il changer ? Et sur un PC, si la carte Wi-Fi tombe en panne ? Relier à un intérêt et une limite de l’intégration.

??? corrige "Corrigé"

    **1.**

    |  | **nRF52833 (micro:bit )** | **PC de bureau** | **Rapport PC / micro:bit** |
    |:---|:--:|:--:|:--:|
    | Fréquence | $64$ MHz | $3{,}5$ GHz $= 3\,500$ MHz | $\approx 55$ |
    | Nombre de cœurs | $1$ | $8$ | $8$ |
    | Mémoire vive | $128$ Ko | $16$ Go | $131\,072$ |
    | Puissance électrique | $\approx 0{,}1$ W | $\approx 100$ W | $\approx 1\,000$ |
    | Système d’exploitation | aucun | Windows, Linux, macOS | — |
    | Composants | une seule puce | pièces séparées | — |

    Mémoire : $16$ Go $= 16 \times 1024 \times 1024$ Ko $= 16\,777\,216$ Ko, et $16\,777\,216 / 128 = 131\,072$. Composants du PC : carte mère, processeur, barrettes de mémoire, disque, carte graphique…

    **2.** Processeur : le cœur Cortex-M4 ; mémoire : la Flash (programme) et la mémoire vive (données) ; entrées-sorties : la radio Bluetooth, le convertisseur analogique-numérique (capteurs), les minuteries. Tout est gravé sur **un seul circuit intégré** : c’est un système sur puce. Il s’agit d’un **microcontrôleur** : fréquence de quelques dizaines de MHz, mémoire de quelques dizaines de Ko, aucun système d’exploitation, très faible consommation, une tâche embarquée.

    **3.** L’**architecture de Harvard** (programme et données dans deux mémoires, deux bus) : le processeur peut lire une instruction et une donnée **en même temps**.

    **4.** L’alarme n’a qu’**une** tâche : un OS (ordonnanceur, gestion de plusieurs processus) consommerait mémoire et énergie, et rendrait le temps de réaction moins prévisible. MicroPython est **interprété** : chaque instruction est analysée à l’exécution, ce qui est bien plus lent qu’un programme compilé (en C par exemple) et occupe de la mémoire pour l’interpréteur ; les produits industriels sont programmés en C ou en assembleur.

    **5.** Sur le micro:bit , la radio est *dans* la puce : il faut changer toute la puce, en pratique toute la carte. Sur un PC, on change seulement la carte Wi-Fi. Intérêt de l’intégration : taille, consommation, coût ; limite : **non réparable**, non évolutif.

## Bilan du TP

!!! encadre "À rédiger (une dizaine de lignes)"

    1.  Décrire, sur l’exemple du podomètre, les trois caractéristiques d’un système embarqué : acquisition, contrôle, contraintes de temps.

    2.  Expliquer à quoi sert une hystérésis (deux seuils), en citant vos mesures de la partie C.

    3.  Pourquoi une puce bien moins puissante qu’un PC est-elle le bon choix pour une veilleuse ou un podomètre ? Donner deux arguments chiffrés.
