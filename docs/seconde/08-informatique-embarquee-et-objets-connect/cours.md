# Cours

<p class="sous-titre">Informatique embarquée et objets connectés</p>

<span id="chap-08" class="ancre"></span>

|  |  |
|:---|:---|
| **Programme** | Systèmes informatiques **embarqués** ; **capteurs** et **actionneurs** ; **interface homme-machine** (IHM) ; **objets connectés** et réseaux d’objets (IoT) ; algorithme de **commande** d’un système physique ; enjeux de **sécurité** et de **vie privée**. |
| **Idée** | Des ordinateurs minuscules se cachent dans nos objets et pilotent le monde physique : ils *mesurent* (capteurs), *décident* (un programme), *agissent* (actionneurs). Reliés au réseau, ils deviennent **connectés** — pratiques, mais pas sans risques. |
| **Objectifs** | Reconnaître un système embarqué ; distinguer **capteur** et **actionneur** ; lire et écrire une **boucle de commande** simple ; décrire une **IHM** ; comprendre l’**Internet des objets** ; mesurer les enjeux de sécurité, de vie privée et d’environnement. |

!!! situation "Situation de départ"

    1.  Le chauffage de votre maison s’allume tout seul quand il fait froid, et s’éteint quand il fait assez chaud. Qui décide, et comment ?

    2.  Une caméra de surveillance connectée peut-elle être piratée, et se retourner contre vous ou contre d’autres ?

    3.  Votre téléphone pollue-t-il surtout quand vous l’utilisez, ou avant même votre premier appel ?

!!! curieux "Pour les curieux (facultatif) — Un peu d’histoire"

    L’un des tout premiers ordinateurs *embarqués* est l’**Apollo Guidance Computer** qui, en **1969**, a guidé les astronautes jusqu’à la Lune avec une puissance… ridicule face à un smartphone d’aujourd’hui. Le **premier objet connecté** de l’histoire serait un **grille-pain** branché à Internet, présenté pour s’amuser en **1990**. L’expression « **Internet des objets** » (*Internet of Things*) est lancée en **1999** par **Kevin Ashton** (Ashton, *RFID Journal*, 2009). On comptait fin 2024 **près de 20 milliards** d’objets connectés dans le monde (sans compter smartphones et ordinateurs) — plus de deux fois le nombre d’humains (IoT Analytics, 2024 ; ONU, 2022).

    ![](../img/08_hist_agc.jpg){ .photo loading=lazy style="width:100%" }  
    L’ordinateur de guidage d’Apollo

    ![](../img/08_hist_kevin_ashton.jpg){ .photo loading=lazy style="width:100%" }  
    Kevin Ashton (2015)

    Sources : K. Ashton, « That “Internet of Things” Thing », *RFID Journal*, 2009 ; IoT Analytics, *State of IoT – Summer 2024*, septembre 2024 (18,8 milliards d’objets connectés estimés fin 2024), `iot-analytics.com` ; ONU (Département des affaires économiques et sociales), *World Population Prospects 2022* (8 milliards d’humains en novembre 2022), `un.org`.

    [$\to$ frise chronologique](../frise-chronologique.md#frise)

## L’informatique invisible : les systèmes embarqués

L’ordinateur n’est plus seulement la machine posée sur un bureau. Il a **rétréci** et s’est glissé *dans les objets*.

!!! definition "Définition 1"

    Un <span id="lex-embarque08" class="ancre"></span>**système embarqué** est un ordinateur **intégré dans un objet**, dédié à **une tâche précise**. Il est le plus souvent minuscule, sobre en énergie, et invisible pour l’utilisateur. Le petit processeur qu’il contient s’appelle un <span id="lex-microcontroleur08" class="ancre"></span>**microcontrôleur**.

!!! exemple "Exemple"

    On en trouve partout : lave-linge, four à micro-ondes, ascenseur, distributeur de billets, montre connectée, régulateur de vitesse d’une voiture, box Internet, feu tricolore, drone, carte bancaire… Une voiture récente en contient à elle seule **plusieurs dizaines**.

!!! encadre "À retenir — Différence avec un ordinateur ordinaire"

    Un système embarqué ne fait **qu’une** chose (réguler une température, afficher l’heure…), n’a en général **pas d’écran ni de clavier** classiques, et doit souvent réagir **en temps réel** : un airbag ne peut pas « ramer ».

<span id="cours-08-1" class="ancre"></span>

<span class="afaire">▶ Exercices d'application :</span> exercices **[1](exercices.md#ex-08-1) et [2](exercices.md#ex-08-2)** (systèmes embarqués)

## Sentir et agir : capteurs et actionneurs

Pour interagir avec le monde physique, un système embarqué a besoin de deux sortes d’organes.

![](../img/08_hist_microbit.jpg){ .photo loading=lazy style="width:100%" }  
Une carte micro:bit : capteurs, boutons et LED

!!! definition "Définition 2"

    <span id="lex-capteur08" class="ancre"></span>Un **capteur** *mesure* une grandeur physique (température, lumière, mouvement, pression…) et la transforme en un **nombre** exploitable par la machine. C’est une **entrée**.  
    Un <span id="lex-actionneur08" class="ancre"></span>**actionneur** *agit* sur le monde physique (chauffer, éclairer, tourner, ouvrir, émettre un son…). C’est une **sortie**.

| **Capteurs (entrées)** | **Actionneurs (sorties)** |
|:---|:---|
| thermomètre (température) | radiateur, ventilateur |
| photorésistance (luminosité) | lampe, LED |
| détecteur de mouvement | moteur (volet, portail) |
| microphone (son) | haut-parleur |
| capteur d’image (chapitre *Photographie numérique*) | écran |

<span class="retouract">↺ Retour sur l'activité.</span> Dans « La carte qui réagit », le thermomètre de la carte, qui fournissait le nombre affiché, était un **capteur** ; l’écran de LED, qui montrait le cœur ou la coche, était un **actionneur**.

!!! activite "Activité — Capteurs ou actionneurs ?"

    Pour un **smartphone**, classer en deux colonnes : l’écran tactile, le haut-parleur, l’appareil photo, le vibreur, le micro, la lampe torche, le capteur de luminosité.

<span id="cours-08-3" class="ancre"></span>

<span class="afaire">▶ Exercices d'application :</span> exercices **[3](exercices.md#ex-08-3) et [4](exercices.md#ex-08-4)** (capteurs et actionneurs)

## La boucle de commande : mesurer, décider, agir

<span id="lex-boucledecommande08" class="ancre"></span>

Le cœur d’un objet embarqué est un **programme** qui répète sans fin le même cycle.

!!! regle "Règle 1 — Le cycle acquisition $to$ décision $to$ action"

    ![](../figures/f78396e72f5c447a.svg){ .tikz loading=lazy }

    Le système **acquiert** une mesure, **décide** (avec des conditions), **commande** un actionneur, puis **recommence**.

<span class="retouract">↺ Retour sur l'activité.</span> Le schéma complété à la fin de l’activité est exactement ce cycle : la carte *mesurait* la température, *décidait* avec le bloc *si… alors… sinon*, *agissait* en affichant une icône, et le bloc *toujours* la faisait recommencer sans fin.

!!! exemple "Exemple — Le thermostat d’une maison connectée"

    On veut maintenir une pièce à $19\,^\circ$C. On dispose d’un capteur `lire_temperature()` et d’un radiateur, que l’on commande avec `allumer_chauffage()` et `eteindre_chauffage()`.

    ```python
    while True:                       # boucle sans fin
        t = lire_temperature()        # ENTREE : le capteur -> un nombre
        if t < 19:
            allumer_chauffage()       # SORTIE : on commande un actionneur
        else:
            eteindre_chauffage()
        attendre(60)                  # on re-teste chaque minute
    ```

    On reconnaît le cycle : **lire** la température, **décider** (`if`), **agir** sur le radiateur, **recommencer**.

!!! encadre "À retenir — Deux nouveautés : while True et les fonctions de la carte"

    - La boucle `while True:` se répète « tant que `True` est vrai ». Or `True` est **toujours** vrai : la boucle ne s’arrête jamais. Au chapitre *Les bases de Python*, une boucle sans fin était un piège, car le programme ne se terminait pas. Ici, c’est **voulu** : un objet embarqué doit surveiller et réagir tant qu’il est allumé. Son microcontrôleur n’exécute que ce programme, de la mise sous tension jusqu’à ce qu’on coupe le courant ; il n’a rien d’autre à faire.

    - `lire_temperature()`, `allumer_chauffage()`, `attendre(60)`… ne sont pas des fonctions de Python : dans un vrai objet, elles sont fournies avec la carte électronique, et on les **appelle** comme `print` ou `input`, sans savoir comment elles fonctionnent à l’intérieur. Une fonction `lire_…()` renvoie la mesure du capteur ; `allumer_…()` ou `eteindre_…()` commande un actionneur ; `attendre(n)` met le programme en **pause** pendant `n` secondes. Comme aucune carte n’est branchée à votre ordinateur, ces programmes s’écrivent **sur papier**.

!!! encadre "À retenir — C’est un algorithme comme un autre"

    La « décision » n’est qu’une suite de **conditions** et de **boucles** — ce que vous savez déjà écrire (chapitre *Les bases de Python*), avec en plus la boucle sans fin `while True`. Un volet qui se ferme quand la nuit tombe, un arrosage qui se déclenche quand la terre est sèche : même boucle, autres capteurs et actionneurs.

!!! activite "Activité — Compléter une boucle de commande"

    Un **éclairage automatique** allume une LED quand la luminosité `lum` devient faible (en dessous de 30). Recopier et compléter :

    ```python
    while True:
        lum = lire_luminosite()
        if ... :                      # (a) condition
            allumer_led()             # (b)
        else:
            eteindre_led()
        attendre(1)
    ```

<span id="cours-08-5" class="ancre"></span>

<span class="afaire">▶ Exercices d'application :</span> exercices **[5](exercices.md#ex-08-5) à [10](exercices.md#ex-08-10)** (la boucle de commande : arrosage automatique, alarme, thermostat)

## L’interface homme-machine (IHM)

Comment un humain *dialogue*-t-il avec un objet ? Par son **interface**.

!!! definition "Définition 3"

    <span id="lex-ihm08" class="ancre"></span>L’**interface homme-machine** (IHM) est l’ensemble des moyens par lesquels l’utilisateur **commande** la machine et **reçoit** des informations d’elle :

    - **entrées** (l’humain vers la machine) : bouton, écran tactile, molette, voix, geste…

    - **sorties** (la machine vers l’humain) : écran, LED, son, vibration…

!!! regle "Règle 2 — Une bonne IHM"

    Une IHM réussie est **simple**, **compréhensible** et donne un **retour** : quand on appuie sur un bouton, un voyant, un bip ou un affichage confirme que l’action a été prise en compte. Une mauvaise IHM laisse l’utilisateur dans le doute (« a-t-il compris ? »).

!!! exemple "Exemple"

    Sur un **lave-linge** : la molette et les boutons sont l’**entrée**, l’écran et le bip de fin sont la **sortie**. Sur un **assistant vocal**, l’entrée est la **voix** et la sortie est… la voix aussi.

<span id="cours-08-11" class="ancre"></span>

<span class="afaire">▶ Exercices d'application :</span> exercices **[11](exercices.md#ex-08-11) à [13](exercices.md#ex-08-13)** (l’interface homme-machine)

## Les objets connectés et l’Internet des objets

Un système embarqué qui, en plus, se **relie au réseau** devient un **objet connecté**.

!!! definition "Définition 4"

    Un <span id="lex-objetconnecte08" class="ancre"></span>**objet connecté** est un objet équipé de capteurs et/ou d’actionneurs qui **échange des données** par un réseau (Wi-Fi, Bluetooth, 4G/5G…). L’ensemble de ces objets forme l’**Internet des objets** (*IoT*, *Internet of Things*).

!!! exemple "Exemple"

    Montre qui envoie votre rythme cardiaque au téléphone ; thermostat réglable à distance ; enceinte connectée ; caméra de surveillance ; capteurs de pollution d’une ville « intelligente » ; balance qui mémorise votre poids dans le nuage.

!!! curieux "Pour les curieux (facultatif) — Le nuage n’est jamais loin"

    Beaucoup d’objets connectés envoient leurs mesures vers des **serveurs** (le *cloud*, chapitre *Les données structurées et leur traitement*), où elles sont stockées et analysées. Ces montagnes de données alimentent des services (statistiques, recommandations) mais posent aussi la question : *qui* les détient ?

<span id="cours-08-14" class="ancre"></span>

<span class="afaire">▶ Exercices d'application :</span> exercice **[14](exercices.md#ex-08-14)** (objets connectés)

## Sécurité et vie privée

Un objet connecté est un petit ordinateur *relié à Internet* : il peut donc, comme tout ordinateur, être **attaqué**.

!!! etudedoc "Quand des caméras attaquent Internet (Mirai, 2016)"

    En **2016**, un logiciel malveillant nommé **Mirai** a pris le contrôle de **centaines de milliers** d’objets connectés (jusqu’à environ 600 000 à son pic ; Antonakakis et al., 2017) (caméras, magnétoscopes numériques…) dont les propriétaires n’avaient jamais changé le **mot de passe par défaut** (souvent `admin`/`admin`). Transformés en armée de « robots », ces objets ont **saturé** de grands sites (déni de service, chapitre *Internet*) et rendu inaccessibles, pendant des heures, Twitter, Netflix, Spotify… *La leçon : un objet mal sécurisé met en danger bien plus que son propriétaire.*

    Source : M. Antonakakis et al., « Understanding the Mirai Botnet », *USENIX Security Symposium*, 2017.

!!! regle "Règle 3 — Deux enjeux à retenir"

    - **Sécurité** : un objet connecté est une **porte d’entrée** sur le réseau (et sur votre maison). *Réflexes :* changer le mot de passe par défaut, faire les mises à jour.

    - **Vie privée** : un objet connecté est un **capteur** qui observe (caméra), écoute (micro) ou vous suit (montre, GPS). Ses données sont des **données personnelles** (chapitre *Les données structurées et leur traitement*), protégées dans l’Union européenne par le **RGPD**.

!!! encadre "À retenir — Et à Monaco ?"

    Les données d’un objet connecté y sont protégées par la loi n° 1.565 (2024), sous le contrôle de l’**APDP** : ce sont les mêmes grands droits qu’avec le RGPD (voir l’encadré « Et à Monaco ? » du chapitre *Les réseaux sociaux*).

!!! activite "Activité — Enquête sur un objet connecté"

    Choisir un objet connecté du quotidien (maison, lycée, sport…). **1.** Quels **capteurs** et **actionneurs** possède-t-il ? **2.** Quelles **données** envoie-t-il, et à qui ? **3.** Citer un risque de **sécurité** et un risque de **vie privée**, puis un geste pour s’en protéger.

<span id="cours-08-15" class="ancre"></span>

<span class="afaire">▶ Exercices d'application :</span> exercices **[15](exercices.md#ex-08-15) et [16](exercices.md#ex-08-16)** (sécurité : mots de passe par défaut ; vie privée)

## L’impact environnemental des objets connectés

<span id="lex-empreinte08" class="ancre"></span>

Un objet connecté consomme un peu d’électricité… mais c’est surtout sa **fabrication** qui pèse. Les chiffres ci-dessous sont des **ordres de grandeur**, tirés d’études publiques. C’est ici que l’on fait le calcul complet pour un smartphone ; les thèmes *Localisation* et *Réseaux sociaux* y renvoient.

!!! etudedoc "Le poids du numérique en France"

    - **Fabriquer avant d’utiliser.** La **fabrication** représente environ **80 %** des émissions de gaz à effet de serre de nos équipements numériques : avant même sa première utilisation, un appareil a déjà produit l’essentiel de son empreinte. *Source : ADEME–Arcep, étude publiée en 2022 (données 2020).*

    - **Un parc énorme.** En 2020, la France comptait environ **800 millions d’équipements numériques** (dont 70 millions de smartphones), et les usages numériques produisaient près de **300 kg de déchets par an et par personne**. *Source : ADEME–Arcep, 2022 (données 2020).*

    - **Une tendance à la hausse.** Si rien ne change, les émissions du numérique augmenteraient d’environ **45 %** d’ici 2030 et seraient **multipliées par 3** d’ici 2050 (par rapport à 2020), notamment à cause de la **multiplication des objets connectés**. *Source : ADEME–Arcep, 2022 (scénario tendanciel).*

    - **Aujourd’hui.** Le numérique représente **4,4 %** de l’empreinte carbone de la France (29,5 millions de tonnes de CO$_2$e) et **11 %** de sa consommation d’électricité. Répartition : **terminaux** (téléphones, ordinateurs, écrans, objets connectés…) **50 %**, **centres de données** **46 %**, **réseaux** 4 %. Ces chiffres ne tiennent pas encore compte de l’essor de l’IA générative. *Source : ADEME–Arcep, mise à jour publiée en janvier 2025 (données 2022).*

    - **Le cas du smartphone.** Un smartphone émet environ **80 kg de CO$_2$e** sur toute sa vie, dont **99 %** (environ 79 kg) lors de sa **fabrication** ; l’usage et la fin de vie ne pèsent qu’environ 1 % en France, où l’électricité est peu carbonée. Ce bilan suppose une durée d’utilisation de **2,5 ans**, soit environ **32 kg de CO$_2$e par année** d’utilisation. *Source : ADEME, outil Impact CO2 (`impactco2.fr`), fiche « smartphone » (données ADEME–Arcep 2025), consultée en 2026.*

    Sources : ADEME–Arcep, *Évaluation de l’impact environnemental du numérique en France et analyse prospective*, 2022 (données 2020 : part de la fabrication, parc d’équipements, déchets, scénario 2030–2050), `arcep.fr` ; ADEME–Arcep, *Évaluation de l’impact environnemental du numérique en France*, mise à jour de janvier 2025 (données 2022 : 4,4 %, 29,5 Mt CO$_2$e, 11 % de l’électricité, répartition 50/46/4 %), `ademe.fr` ; ADEME, outil *Impact CO2*, fiche « smartphone », consultée en 2026 (80 kg CO$_2$e, 99 % à la fabrication, 2,5 ans d’utilisation), `impactco2.fr`.

!!! activite "Activité — Un objet connecté, pour quoi faire ?"

    À partir du document ci-dessus :

    1.  À l’aide du cas du smartphone, expliquer pourquoi, pour limiter l’impact d’un objet connecté, il vaut mieux le **garder longtemps** plutôt que de chercher seulement à l’éteindre.

    2.  Choisir un objet connecté (ampoule, prise, montre, enceinte…). Est-il vraiment **utile** ? Quel objet non connecté pourrait rendre le même service ?

    3.  Citer trois raisons qui obligent à remplacer un objet connecté trop tôt (penser aux **mises à jour** qui s’arrêtent, à la **réparabilité**, à la batterie…).

    4.  Un objet connecté reste souvent en **veille**, relié au réseau jour et nuit. Proposer deux gestes de **sobriété** pour les objets et le smartphone (durée d’utilisation, qualité vidéo, lecture automatique, extinction…).

<span id="cours-08-17" class="ancre"></span>

<span class="afaire">▶ Exercices d'application :</span> exercice **[17](exercices.md#ex-08-17)** (l’empreinte d’un smartphone), exercice **[18](exercices.md#ex-08-18)** (critiquer une réponse d’IA), exercice **[19](exercices.md#ex-08-19)** (Python au service du thème)

!!! curieux "Pour les curieux (facultatif) — Liens avec d’autres chapitres"

    - **Déjà vu :** la boucle de commande s’écrit avec les `while` et `if` du chapitre *Les bases de Python*, et les données de l’objet voyagent en **paquets** sur **Internet**, grâce à une **adresse IP**.

    - **Tout se rejoint :** le capteur d’image d’un appareil photo et le récepteur **GPS** sont aussi des **capteurs**, et les mesures envoyées dans le **nuage** sont souvent des **données personnelles** (chapitre *Les données structurées et leur traitement*).

    - **Plus loin :** en spécialité NSI de Première, on programme soi-même capteurs, actionneurs et **IHM**.

## Bilan — la carte mémoire

Les mots importants du thème sont définis dans le lexique.

| **Notion** | **À retenir** |
|:---|:---|
| Système embarqué | ordinateur (microcontrôleur) intégré à un objet, pour **une** tâche. |
| Capteur | mesure une grandeur physique $\to$ un **nombre** (entrée). |
| Actionneur | **agit** sur le monde physique (sortie). |
| Boucle de commande | **acquisition** (capteur) $\to$ **décision** (programme) $\to$ **action** (actionneur) $\to$ recommencer. |
| IHM | moyens de **commander** la machine et d’en **recevoir** un retour. |
| Objet connecté | système embarqué relié au **réseau** ; ensemble $=$ **IoT**. |
| Nuage | les objets envoient souvent leurs données vers des serveurs distants. |
| Sécurité | objet $=$ porte d’entrée ; changer le mot de passe, mettre à jour. |
| Vie privée | objet $=$ capteur ; données personnelles ; RGPD (UE), loi n° 1.565 (Monaco). |
| Environnement | smartphone $\approx 80$ kg CO$_2$e, dont 99 % à la **fabrication** : garder, réparer, se passer du superflu. |

!!! situation "Retour à la situation de départ"

    1.  Un **système embarqué** (§ I) répète sans fin une **boucle de commande** : le **capteur** mesure la température, le programme décide (`if t < 19`), l’**actionneur**, le radiateur, agit, puis tout recommence (§ II et III).

    2.  Oui : un **objet connecté** est un petit ordinateur relié à Internet, donc une porte d’entrée. En 2016, Mirai a piraté des centaines de milliers d’objets restés avec leur **mot de passe par défaut** pour saturer de grands sites (§ VI). Réflexes : changer ce mot de passe, faire les mises à jour.

    3.  Avant : environ 99 % des 80 kg de CO$_2$e d’un smartphone sont émis à sa **fabrication** (§ VII). Le geste le plus efficace est donc de le garder longtemps.

!!! encadre "Débat argumenté"

    Un **débat**, proposé en fin de chapitre, accompagne ce thème : « Faut-il équiper sa maison de caméras et d’enceintes connectées ? » (documents, rôles, tableau d’arguments et trace écrite, environ 50 min).

## Savoir-faire à maîtriser

*À la fin du chapitre, je sais…*

!!! autopos "Savoir-faire : je me positionne"

    - reconnaître un **système embarqué** dans un objet du quotidien ;

    - distinguer un **capteur** d’un **actionneur** et donner des exemples de chacun ;

    - dérouler une **boucle de commande** « mesurer $\rightarrow$ décider $\rightarrow$ agir » (ex. thermostat) ;

    - décrire le rôle d’une **interface homme-machine** (IHM) ;

    - expliquer ce qu’est un **objet connecté** et l’**Internet des objets** ;

    - citer les risques de **sécurité** et de **vie privée** des objets connectés, et les textes qui protègent les données (RGPD, loi monégasque n° 1.565) ;

    - expliquer pourquoi la **fabrication** pèse le plus dans l’impact environnemental d’un objet connecté.
