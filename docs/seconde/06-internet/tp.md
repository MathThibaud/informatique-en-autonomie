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

!!! encadre "Le vocabulaire du TP"

    - Un **switch** (ou *commutateur*) est le boîtier qui relie entre elles, par des câbles, les machines d’un **même réseau local** (une salle, une maison) : il fait suivre chaque paquet vers la machine à qui il est destiné.

    - Un **routeur** (vu en cours) relie **plusieurs réseaux** entre eux et aiguille les paquets de l’un à l’autre.

    - La **passerelle** d’une machine est l’adresse IP du routeur de *son* réseau local : c’est à lui qu’elle confie tout paquet destiné à une machine d’un **autre** réseau, comme on passe par la porte de sortie d’un bâtiment. On l’appelle aussi *routeur par défaut*.

    - Filius demande aussi un **masque** : recopiez simplement la valeur donnée (`255.255.255.0`), sans chercher à l’expliquer.

## Partie 1 — Un réseau local

### <span class="exo-num">Exercice 1</span> <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-internet-tp-1-1 }

<span class="run" title="À programmer et tester sur machine">▶</span>  En mode **construction**, poser **trois Ordinateurs** reliés à un même **Switch**. Double-cliquer sur chacun et saisir son **adresse IP** et le **masque** `255.255.255.0` (laisser la passerelle vide) :

![](../figures/fba3a781af3b3232.svg){ .tikz loading=lazy }

1.  Les trois machines ont des adresses `192.168.0._`. À quoi sert le **switch** ?

2.  Double-cliquer sur le switch : Filius propose-t-il de lui donner une adresse IP ? Qu’en déduire ?

??? corrige "Corrigé"

    0

    1.  Le **switch** relie entre elles les machines d’un *même* réseau local et aiguille les données vers la bonne machine. *(Toutes les IP commencent par `192.168.0` : même réseau local.)*

    2.  **Non**, Filius ne propose aucune adresse IP pour le switch : il n’en a pas besoin (il ne fait que distribuer dans le réseau local, il ne « raisonne » pas sur les adresses IP comme un routeur).

### <span class="exo-num">Exercice 2</span> <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-06-internet-tp-1-2 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Passer en **simulation**. Sur PC-A, installer la **Ligne de commande**, l’ouvrir et taper : `ping 192.168.0.2`. Ralentir la vitesse (curseur en haut) pour bien voir.

1.  Le `ping` réussit-il ? Décrire le trajet du paquet (quels composants traverse-t-il ?).

2.  <span class="run" title="À programmer et tester sur machine">▶</span>  Ouvrir « Afficher les échanges de données » sur PC-B : que voit-on arriver ?

3.  <span class="run" title="À programmer et tester sur machine">▶</span>  Taper `ping 192.168.0.9` (machine qui n’existe pas). Que se passe-t-il, et pourquoi ?

??? corrige "Corrigé"

    1.  Le `ping` **réussit**. Trajet : PC-A $\to$ Switch $\to$ PC-B, et la réponse revient par le même chemin.

    2.  On voit **arriver les paquets** (requête « echo » puis réponse). C’est l’échange « requête echo » / « réponse echo » du `ping`.

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

0

## <span class="etiquette">Débat</span> Les fournisseurs d’accès à Internet doivent-ils traiter tous les paquets de la même façon ?

*la neutralité du Net*

<p class="infos-activite">Durée : 50 min</p>

!!! consignes "Consignes"

    - En classe entière. Les rôles sont tirés au sort : vous défendrez peut-être une position qui n’est pas la vôtre, c’est un excellent entraînement.

    - Chaque argument s’appuie sur un **document** ci-dessous ou sur le **cours**. <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> Préparation sans IA ni recherche en ligne.

    - Avant de commencer, notez sur votre cahier votre position de départ : oui, non ou je ne sais pas.

**Rappel du cours.** Les routeurs acheminent les **paquets** de proche en proche. La **neutralité du Net** est le principe selon lequel ils transmettent **tous** les paquets de la même façon, sans favoriser un contenu ou un service. Techniquement, votre fournisseur d’accès à Internet (FAI : Monaco Telecom, Orange, Free…) pourrait ralentir certains paquets ou en accélérer d’autres. En a-t-il le droit ? Et serait-ce une bonne idée ?

!!! encadre "Les deux camps"

    **Groupe POUR** — oui : tous les paquets doivent être traités de la même façon (neutralité stricte).  
    **Groupe CONTRE** — non : un FAI doit pouvoir donner des priorités ou proposer des offres différentes selon les services.

Les documents

!!! encadre "Document 1 — La règle en Europe : un Internet ouvert"

    Depuis le 30 avril 2016, un règlement européen impose aux FAI de traiter tout le trafic **de façon égale**, sans discrimination, restriction ni interférence, quels que soient l’expéditeur, le destinataire, le contenu ou l’application. Une gestion « raisonnable » du trafic reste permise : un FAI peut traiter différemment des *catégories* de trafic qui ont des besoins techniques différents (un appel vidéo supporte mal le retard, un téléchargement peut attendre), ou faire face à une congestion temporaire, mais jamais pour des raisons commerciales. En France, c’est l’**Arcep** qui veille au respect de ces règles. Monaco n’étant pas membre de l’Union européenne, ce règlement ne s’y applique pas directement.

    Source : règlement (UE) 2015/2120 du 25 novembre 2015, article 3 ; Arcep, rapport annuel « L’état de l’internet en France ».

!!! encadre "Document 2 — L’« illimité »… sur certaines applications seulement"

    Certains forfaits mobiles ont proposé des options « tarif zéro » : le trafic de quelques applications partenaires (musique, vidéo, réseau social) n’était pas décompté du forfait, alors que celui des autres l’était, et pouvait même être ralenti une fois le forfait épuisé. Pour le client, c’est une bonne affaire ; pour une petite application concurrente, c’est un handicap. La Cour de justice de l’Union européenne a jugé, le 15 septembre 2020 (affaire Telenor, en Hongrie), que ralentir ou bloquer les autres applications était contraire au règlement européen, puis, le 2 septembre 2021, que ces options « tarif zéro » étaient elles-mêmes incompatibles avec l’égalité de traitement du trafic.

    Source : Cour de justice de l’Union européenne, arrêts du 15 septembre 2020 (Telenor Magyarország) et du 2 septembre 2021.

!!! encadre "Document 3 — Les opérateurs : « que les plus gros paient leur part »"

    Une poignée de grandes plateformes, surtout de vidéo en ligne, produit une part importante du trafic qui arrive chez les abonnés. Or ce sont les opérateurs qui paient les antennes, la fibre et les routeurs. Plusieurs grands opérateurs européens demandent donc que ces plateformes contribuent au financement des réseaux : c’est le débat de la « juste part » (*fair share*), sur lequel la Commission européenne a lancé une consultation publique en février 2023. Les plateformes répondent qu’elles investissent déjà (câbles sous-marins, serveurs installés au plus près des abonnés) et que ce sont les abonnés eux-mêmes qui demandent ces vidéos, et paient leur abonnement pour cela.

    Source : Commission européenne, consultation « L’avenir du secteur des communications électroniques et de ses infrastructures », février 2023.

!!! encadre "Document 4 — Aux États-Unis, la règle fait le yo-yo"

    Aux États-Unis, l’autorité fédérale des télécoms (FCC) a adopté des règles de neutralité du Net en 2015, les a supprimées fin 2017, puis rétablies en avril 2024 ; en janvier 2025, une cour d’appel fédérale les a annulées. Sans règle, un FAI peut en principe créer des « voies rapides » payantes, réservées aux services qui ont les moyens de payer. Les partisans de la suppression font valoir que l’Internet américain a continué à se développer pendant ces années ; leurs adversaires rappellent que plusieurs États, comme la Californie en 2018, ont voté leur propre loi de neutralité pour combler le vide.

    Source : FCC, décisions de 2015, 2017 et 2024 ; cour d’appel fédérale (6<sup>e</sup> circuit), 2 janvier 2025.

Organisation du débat

| **Rôle** | **Préparation (15 min), puis débat** |
|:---|:---|
| Groupe POUR ($\approx$ 1/3) | Défend **oui** : au moins trois arguments, chacun appuyé sur un document ou le cours ; prévoit la réponse à deux arguments adverses ; choisit qui ouvre et qui conclut. |
| Groupe CONTRE ($\approx$ 1/3) | Défend **non** : même travail que le groupe POUR. |
| Modérateur (1 ou 2) | Prépare deux questions de relance ; donne la parole en alternant les camps, tient le temps, recentre. Ne donne **pas** son avis. |
| Secrétaire (1 ou 2) | Note au tableau, en deux colonnes POUR / CONTRE, chaque argument et le numéro du document cité. |
| Observateurs (les autres) | Suivent deux ou trois élèves (citent-ils un document ? répondent-ils à l’argument précédent ?) et notent le meilleur argument de chaque camp. |

| **Min.** | **Étape** | **Min.** | **Étape** |
|---:|:---|---:|:---|
| 0–3 | **Mise en place** : tirage des rôles, groupes face à face. | 26–38 | **Échanges** : 12 min, parole alternée entre les camps. |
| 3–18 | **Préparation** en groupes, tableau d’arguments ci-dessous. | 38–42 | **Observateurs** : meilleur argument de chaque camp. |
| 18–20 | **Ouverture** : le modérateur lit la question et les règles. | 42–44 | **Conclusions** : 1 min par groupe. |
| 20–26 | **Prises de position** : 3 min POUR, puis 3 min CONTRE. | 44–50 | **Bilan** : trace écrite individuelle, puis vote. |

!!! encadre "Règles de prise de parole"

    - On lève la main, le modérateur donne la parole ; une seule personne à la fois, une minute au plus.

    - On **argumente** (« je pense que… **parce que**… ») et on **cite** un document ou le cours (« d’après le document 2… »).

    - On **répond à l’argument précédent** avant d’en avancer un nouveau : « vous dites que…, mais… ».

    - On **respecte** : on critique une idée, jamais une personne ; pas de moquerie ; on ne raconte pas la vie privée de quelqu’un.

Tableau d’arguments

Recopier ce tableau sur le cahier et le compléter pendant le débat.

| **Argument POUR (oui)** | **Doc.** | **Argument CONTRE (non)** | **Doc.** |
|:------------------------|:---------|:--------------------------|:---------|
| …                       |          | …                         |          |

Trace écrite finale (individuelle)

Sur le cahier, notez votre position après le débat (oui, non, je ne sais toujours pas) et si vous avez changé d’avis. Puis, en trois à cinq lignes, justifiez-la avec vos **deux meilleurs arguments**, dont **un argument de l’autre camp** que vous trouvez solide (avec le document qui l’appuie).

??? corrige "Corrigé de l'activité"

    Notions du cours mobilisées

    - **Paquet**, **routeur**, **routage** de proche en proche, sans chef d’orchestre central.

    - **IP** achemine, **TCP** fiabilise mais *sans garantie de temps* : d’où les saccades du streaming (argument pour la priorité au temps réel).

    - **Ordres de grandeur du trafic** (zetta-octets par an) : la congestion est un vrai problème.

    - **Neutralité du Net** et **déni de service** (cadre « Deux enjeux de société »).

    - Indépendance d’Internet vis-à-vis du réseau physique : qui paie la fibre, les antennes 4G/5G ?

    - **Internet $\neq$ Web** : la neutralité concerne le réseau, pas le contenu des sites.

    Arguments attendus

    <table>
    <thead>
    <tr>
    <th style="text-align: left;"><strong>POUR (oui) : neutralité stricte</strong></th>
    <th style="text-align: left;"><strong>CONTRE (non) : priorités ou offres différenciées</strong></th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: left;"><ul>
    <li><p><strong>Égalité des chances</strong> : une petite application ou un site naissant doit arriver aussi vite qu’un géant (doc. 2).</p></li>
    <li><p><strong>Concurrence et innovation</strong> : Internet s’est développé sans « péage » ; les « voies rapides » payantes favoriseraient ceux qui ont déjà de l’argent (doc. 4).</p></li>
    <li><p><strong>Liberté d’accès à l’information</strong> : le FAI ne doit pas choisir ce que l’abonné voit ou utilise.</p></li>
    <li><p><strong>C’est la loi en Europe</strong>, confirmée par la justice (doc. 1 et 2) ; la Californie a recréé une règle quand la règle fédérale a disparu (doc. 4).</p></li>
    <li><p><strong>Le client paie déjà</strong> son abonnement pour accéder à tout Internet (doc. 3).</p></li>
    <li><p>La gestion technique « raisonnable » est <em>déjà</em> permise sans casser la neutralité (doc. 1).</p></li>
    </ul></td>
    <td style="text-align: left;"><ul>
    <li><p><strong>Tous les paquets n’ont pas les mêmes besoins</strong> : appel vidéo, téléconsultation, jeu en ligne supportent mal le retard ; TCP ne garantit pas le temps (cours, doc. 1).</p></li>
    <li><p><strong>Congestion</strong> : le trafic explose (cours) ; donner la priorité permet de mieux utiliser le réseau.</p></li>
    <li><p><strong>Qui paie les réseaux ?</strong> Les grandes plateformes produisent beaucoup de trafic sans financer les antennes et la fibre (doc. 3).</p></li>
    <li><p><strong>Offres moins chères</strong> pour le client : le « tarif zéro » était une bonne affaire pour certains abonnés (doc. 2).</p></li>
    <li><p><strong>L’exemple américain</strong> : l’Internet a continué à se développer sans règle fédérale (doc. 4).</p></li>
    <li><p>La neutralité est un <strong>principe européen</strong> : Monaco n’est pas tenu par ce règlement (doc. 1), chaque pays peut faire un autre choix.</p></li>
    </ul></td>
    </tr>
    </tbody>
    </table>

    *Arguments de l’autre camp souvent jugés solides dans la trace écrite :* un élève POUR retient souvent « certains usages (appel vidéo, secours) ont vraiment besoin de passer vite » ; un élève CONTRE, « une petite application n’a aucune chance si les géants achètent la priorité ».

    Questions de relance (pour le modérateur)

    1.  Si un hôpital fait une consultation à distance, doit-elle passer avant une vidéo de divertissement ? Est-ce contraire à la neutralité (doc. 1) ?

    2.  Qui devrait payer les nouvelles antennes et la fibre : l’abonné, les plateformes, l’État ?

    3.  Une option « réseau social illimité » à 2 € : bonne affaire pour vous, mais pour l’application concurrente ?

    4.  Que se passerait-il si votre FAI ralentissait le site d’un concurrent de son propre service de vidéo ?

    !!! encadre "Synthèse possible"

        La **neutralité du Net** est le principe selon lequel les FAI traitent tous les paquets de la même façon, sans favoriser un contenu, un service ou une entreprise. Dans l’Union européenne, c’est une **obligation légale** depuis 2016 (règlement 2015/2120), contrôlée en France par l’Arcep, avec des exceptions techniques limitées (congestion, catégories de trafic aux besoins différents). Le débat porte sur deux questions : **qui paie** les réseaux dont le trafic explose, et **qui décide** de ce qui passe en premier. Les choix diffèrent selon les pays (États-Unis, Monaco hors UE).
