# TP et projets

<p class="sous-titre">Internet</p>

## <span class="etiquette">TP</span> Construire un réseau et faire circuler un paquet

*sur le simulateur Filius, gratuit et en français*

Usage de l’IA, indiqué sur chaque exercice : <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> aucune ; <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> en appui (déboguer, reformuler, vérifier ; la réponse finale est écrite et comprise par vous) ; <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> l’exercice s’appuie sur une réponse d’IA. Voir la charte d’usage de l’IA.

!!! encadre "But du TP"

    Avec le logiciel gratuit **Filius**, on va **construire** un petit réseau, donner une **adresse IP** à chaque machine, puis envoyer un paquet avec la commande `ping` et l’**observer voyager**. On ira du réseau local le plus simple jusqu’à **deux réseaux reliés par un routeur**.

**Prise en main.** Filius a deux modes (en haut) : le mode **construction** (le marteau) pour poser et relier les composants avec le **Câble**, et le mode **simulation** (la flèche verte) pour lancer les échanges. Les composants (barre de gauche) sont l’**Ordinateur**, le **Switch**, le **Routeur** et le **Câble** :

![](../figures/a5337ec15a2df869.svg){ .tikz loading=lazy }

Un **double-clic** sur une machine ouvre sa configuration (adresse IP, masque, passerelle). En mode simulation, un double-clic permet d’installer la « **Ligne de commande** » : on y tape `ping`, `ipconfig`, `traceroute`. Le clic droit « **Afficher les échanges de données** » montre les paquets qui passent.

## Partie 1 — Un réseau local

### <span class="exo-num">Exercice 1</span> <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-internet-tp-1-1 }

<span class="run" title="À programmer et tester sur machine">▶</span>  En mode **construction**, poser **trois Ordinateurs** reliés à un même **Switch**. Double-cliquer sur chacun et saisir son **adresse IP** et le **masque** `255.255.255.0` (laisser la passerelle vide) :

![](../figures/fba3a781af3b3232.svg){ .tikz loading=lazy }

1.  Les trois machines ont des adresses `192.168.0._`. À quoi sert le **switch** ?

2.  Le switch a-t-il besoin d’une adresse IP, lui ?

??? corrige "Corrigé"

    !!! danger "Conversion impossible"
        Ce passage n'a pas pu être converti.

    1.  Le **switch** relie entre elles les machines d’un *même* réseau local et aiguille les données vers la bonne machine. *(Toutes les IP commencent par `192.168.0` : même réseau local.)*

    2.  **Non** : un switch n’a pas besoin d’adresse IP (il ne fait que distribuer dans le réseau local, il ne « raisonne » pas sur les adresses IP comme un routeur).

### <span class="exo-num">Exercice 2</span> <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-internet-tp-1-2 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Passer en **simulation**. Sur PC-A, installer la **Ligne de commande**, l’ouvrir et taper : `ping 192.168.0.2`. Ralentir la vitesse (curseur en haut) pour bien voir.

1.  Le `ping` réussit-il ? Décrire le trajet du paquet (quels composants traverse-t-il ?).

2.  <span class="run" title="À programmer et tester sur machine">▶</span>  Ouvrir « Afficher les échanges de données » sur PC-B : que voit-on arriver ?

3.  <span class="run" title="À programmer et tester sur machine">▶</span>  Taper `ping 192.168.0.9` (machine qui n’existe pas). Que se passe-t-il, et pourquoi ?

??? corrige "Corrigé"

    1.  Le `ping` **réussit**. Trajet : PC-A $\to$ Switch $\to$ PC-B, et la réponse revient par le même chemin.

    2.  On voit **arriver les paquets** (requête « echo » puis réponse). C’est l’échange `ping` / `pong`.

    3.  `ping 192.168.0.9` : **échec** (« délai dépassé » / pas de réponse) car aucune machine ne porte cette adresse dans le réseau.

## Partie 2 — Deux réseaux reliés par un routeur

### <span class="exo-num">Exercice 3</span> <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-internet-tp-1-3 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Construire **deux** réseaux locaux reliés par **un Routeur**. À la création du routeur, Filius demande le **nombre d’interfaces** : en mettre **2**.

![](../figures/9b1f1288be07d9fc.svg){ .tikz loading=lazy }

Interface du routeur côté réseau 0 : `192.168.0.254` ; côté réseau 1 : `192.168.1.254` (masque `255.255.255.0` partout).

??? corrige "Corrigé"

    Construction conforme au schéma de l’énoncé : PC-A et S1 dans le réseau `192.168.0.0`, PC-B et S2 dans le réseau `192.168.1.0`, et le routeur avec ses deux interfaces `192.168.0.254` et `192.168.1.254`.

### <span class="exo-num">Exercice 4</span> <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-internet-tp-1-4 }

<span class="run" title="À programmer et tester sur machine">▶</span>  En simulation, sur PC-A, taper `ping 192.168.1.1`.

1.  Sans passerelle, Filius répond « `destination non joignable` ». Pourquoi ? *(Le paquet doit **quitter** le réseau local.)*

2.  <span class="run" title="À programmer et tester sur machine">▶</span>  Régler la **passerelle** de PC-A sur `192.168.0.254` (l’interface du routeur de *son* côté), et celle de PC-B sur `192.168.1.254`. Relancer le `ping` : il doit réussir. Décrire le trajet complet du paquet.

3.  <span class="run" title="À programmer et tester sur machine">▶</span>  Taper `traceroute 192.168.1.1` sur PC-A. Combien d’étapes ? Que représente l’étape intermédiaire ?

!!! encadre "Bilan du TP"

    Dans un **réseau local**, un **switch** suffit pour relier les machines (mêmes adresses `192.168.0._`). Pour **changer de réseau**, il faut un **routeur**, et chaque machine doit connaître sa **passerelle** (la porte de sortie vers les autres réseaux). Le paquet avance ensuite **de proche en proche**.

??? corrige "Corrigé"

    1.  PC-A (`192.168.0.1`) et PC-B (`192.168.1.1`) ne sont **pas dans le même réseau** (`.0.` vs `.1.`). Sans passerelle, PC-A ne sait pas *par où sortir* de son réseau local $\to$ « destination non joignable ».

    2.  Avec les passerelles réglées, le `ping` réussit. Trajet : **PC-A $\to$ S1 $\to$ Routeur $\to$ S2 $\to$ PC-B** (et retour). Le routeur fait le lien entre les deux réseaux.

    3.  `traceroute` montre **deux étapes** : d’abord le **routeur** (`192.168.0.254`), puis **PC-B**. L’étape intermédiaire est le routeur (la passerelle).

    *Pour aller plus loin : couper le câble PC-B–S2 en pleine simulation et relancer le ping $\to$ échec ; le rebrancher $\to$ succès. Illustre pannes et robustesse.*

!!! danger "Conversion impossible"
    Ce passage n'a pas pu être converti.
