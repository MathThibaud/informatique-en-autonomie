# Activités préparatoires

<p class="sous-titre">Programmation orientée objet et paradigmes</p>

## <span class="etiquette">Activité 1</span> La fiche d’identité d’un objet

*décrire ce qu’un objet sait et ce qu’il sait faire*

<p class="infos-activite">Durée : 20 min · Sans ordinateur, par deux</p>

!!! consignes "Consignes"

    - On n’écrit **aucun code** : on décrit des objets de la vie courante **en français**, sur des fiches à deux colonnes dessinées sur le cahier : à gauche, ce que l’objet **sait** (ses caractéristiques et leur valeur) ; à droite, ce que l’objet **sait faire** (ses actions).

    - Une **caractéristique** se note avec sa valeur actuelle (par exemple « couleur : verte ») ; une **action** se note par un verbe (par exemple « s’allumer »).

### <span class="exo-num">Exercice 1</span> — Deux lampes <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-programmation-orientee-objet-et-paradigm-act-1-1 }

Léa possède une lampe de bureau bleue, équipée d’une ampoule de $40$ W ; elle est éteinte. Tom possède une lampe du **même modèle**, mais rouge, avec une ampoule de $60$ W ; elle est allumée.

1.  Sur le cahier, dessiner et remplir la fiche de la lampe de Léa : au moins trois caractéristiques avec leur valeur, et au moins trois actions qu’on peut lui faire faire.

2.  Sans la dessiner, imaginer la fiche de la lampe de Tom. Qu’est-ce qui est **identique** sur les deux fiches ? Qu’est-ce qui **change** ?

??? corrige "Corrigé"

    1.  **Caractéristiques** : couleur : bleue ; puissance de l’ampoule : $40$ W ; allumée : non (on accepte aussi : marque, hauteur, position du bras…). **Actions** : appuyer sur l’interrupteur (allumer / éteindre), changer l’ampoule, orienter le bras, dire si elle éclaire.

    2.  **Identique** : la liste des caractéristiques (leurs *noms*) et la liste des actions. **Change** : les *valeurs* (bleue / rouge, $40$ / $60$ W, éteinte / allumée). Deux lampes du même modèle ont la même *forme* de fiche, mais pas le même contenu.

### <span class="exo-num">Exercice 2</span> — Le modèle commun <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-programmation-orientee-objet-et-paradigm-act-1-2 }

1.  Écrire une fiche « modèle » qui conviendrait à **toutes** les lampes de ce modèle. Qu’a-t-on gardé des fiches précédentes ? Qu’a-t-on enlevé ?

2.  À l’usine, on fabrique une nouvelle lampe. Quelles informations faut-il donner au moment de la fabrication ? Quelle caractéristique a toujours la **même** valeur à la sortie de l’usine ?

??? corrige "Corrigé"

    1.  On garde le titre « Lampe », les noms des caractéristiques et toutes les actions ; on enlève les valeurs, propres à chaque lampe. Cette fiche modèle ne décrit aucune lampe en particulier : elle sert à en fabriquer.

    2.  Il faut fournir la couleur et la puissance de l’ampoule (elles varient d’une lampe à l’autre). La caractéristique « allumée » vaut **toujours** « non » à la sortie de l’usine : inutile de la demander.

### <span class="exo-num">Exercice 3</span> — Les actions changent l’état <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-programmation-orientee-objet-et-paradigm-act-1-3 }

1.  La lampe de Léa est éteinte. On appuie **trois fois** sur son interrupteur. Quelle caractéristique a changé, et quelle est sa valeur finale ? Lesquelles n’ont pas bougé ?

2.  L’action « changer l’ampoule » ne peut pas se faire sans une **information supplémentaire**. Laquelle ?

3.  Classer les actions de votre fiche en deux groupes : celles qui **modifient** une caractéristique, et celles qui ne font que **donner une information** (par exemple « dire si elle éclaire »). Compléter la fiche si l’un des groupes est vide.

4.  Sur la fiche d’une carte de cantine, la caractéristique « solde » vaut $12$ €. Un camarade efface et écrit directement « solde : $-50$ ». Pourquoi est-ce gênant ? Comment l’éviter, si l’on n’a le droit de toucher au solde qu’à travers des actions ?

??? corrige "Corrigé"

    1.  Seule « allumée » a changé : éteinte $\to$ allumée $\to$ éteinte $\to$ **allumée**. Couleur et puissance n’ont pas bougé. L’état d’un objet est l’ensemble des valeurs de ses caractéristiques *à un instant donné*.

    2.  La **nouvelle puissance** (la nouvelle ampoule). Une action peut avoir besoin d’informations en plus de l’objet lui-même.

    3.  **Modifient** : appuyer sur l’interrupteur, changer l’ampoule, orienter le bras. **Informent** sans rien changer : dire si elle éclaire, dire sa puissance.

    4.  N’importe qui peut mettre l’objet dans un état **absurde** (un solde de $-50$ € alors qu’on ne peut pas dépenser ce qu’on n’a pas). Si le solde ne se modifie que par des actions (« recharger », « payer un repas »), ces actions peuvent **vérifier** la demande et refuser un paiement sans provision.

### <span class="exo-num">Exercice 4</span> — À vous <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-programmation-orientee-objet-et-paradigm-act-1-4 }

1.  Choisir un objet : un **réveil**, un **ascenseur** ou un **personnage de jeu vidéo**. Dessiner et remplir sur le cahier sa fiche modèle : trois caractéristiques, trois actions, dont **une** qui demande une information supplémentaire.

??? corrige "Corrigé"

    1.  Exemple (réveil) : heure affichée : 7 h 12 ; heure de l’alarme : 7 h 30 ; alarme activée : oui. Actions : avancer d’une minute, sonner, régler l’alarme *(information : la nouvelle heure)*, dire si l’alarme est activée. Exemple (ascenseur) : étage actuel, portes ouvertes, nombre de personnes ; actions : aller à un étage *(information : le numéro de l’étage)*, ouvrir les portes, dire l’étage.

### <span class="exo-num">Exercice 5</span> — Ce qu’on a découvert <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-programmation-orientee-objet-et-paradigm-act-1-5 }

1.  Recopier et compléter sur le cahier, avec vos mots.

    - Un objet est décrit à la fois par …

    - La fiche « modèle », commune à toutes les lampes, sert à …

    - La lampe de Léa et celle de Tom sont deux …

    - Une action peut … une caractéristique, ou seulement …

??? corrige "Corrigé"

    1.  Un objet est décrit à la fois par **ce qu’il sait** (ses caractéristiques et leurs valeurs : son état) et par **ce qu’il sait faire** (ses actions : son comportement). La fiche modèle sert à **fabriquer** autant de lampes qu’on veut, toutes construites sur le même plan. Les lampes de Léa et de Tom sont deux **exemplaires** du même modèle. Une action peut **modifier** une caractéristique, ou seulement **donner une information** sur l’objet.
