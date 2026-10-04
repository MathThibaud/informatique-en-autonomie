# Activités préparatoires

<p class="sous-titre">Structures linéaires : piles, files, listes chaînées</p>

## <span class="etiquette">Activité 1</span> Par où entre-t-on, par où sort-on ?

*un tas, une rangée, et le bouton « Annuler »*

<p class="infos-activite">Durée : 20 min · Sans ordinateur, par deux</p>

!!! consignes "Consignes"

    - Matériel : huit cartes numérotées de `1` à `8` (ou huit post-it).

    - On **joue** chaque question avec les cartes, **puis** on note le résultat sur le cahier. Un joueur lit les instructions, l’autre manipule ; on échange les rôles à chaque partie.

    - « Poser $x$ » : ajouter la carte $x$ ; « prendre » : retirer une carte en respectant la règle, et noter son numéro.

### <span class="exo-num">Exercice 1</span> — Règle du tas <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-03-structures-lineaires-piles-files-listes-act-1-1 }

Les cartes forment un **tas** posé sur la table, comme des assiettes : on ne peut poser une carte que **sur le dessus**, et on ne peut prendre que **celle du dessus**.

1.  Poser `1`, `2`, `3`, `4` dans cet ordre, puis tout reprendre une par une. Dans quel ordre les cartes sortent-elles ?

2.  Repartir d’un tas vide et jouer : *poser 5, poser 2, prendre, poser 7, poser 4, prendre, prendre*. Noter sur le cahier les cartes prises, dans l’ordre, puis dessiner le tas final (vertical, le dessus en haut).

3.  Avec un tas de huit cartes, combien de cartes faut-il retirer avant de pouvoir prendre celle du **fond** ?

??? corrige "Corrigé"

    1.  `4`, `3`, `2`, `1` : l’ordre est **inversé**.

    2.  Cartes prises : `2`, puis `4`, puis `7`. Tas final : la seule carte `5`, qui est à la fois au fond et au dessus.

    3.  Il faut retirer les **sept** cartes posées par-dessus : seul le dessus est accessible.

### <span class="exo-num">Exercice 2</span> — Règle de la rangée <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-03-structures-lineaires-piles-files-listes-act-1-2 }

Les cartes sont maintenant posées en **rangée** : on pose toujours une nouvelle carte **à gauche**, et l’on prend toujours la carte **la plus à droite**.

1.  Poser `1`, `2`, `3`, `4`, puis tout reprendre. Dans quel ordre les cartes sortent-elles ?

2.  Rejouer la séquence de la question 2 : *poser 5, poser 2, prendre, poser 7, poser 4, prendre, prendre*. Noter les cartes prises, dans l’ordre, puis dessiner la rangée finale (horizontale : on pose à gauche, on prend à droite).

3.  Laquelle des deux règles **renverse** l’ordre des cartes ? Laquelle le **conserve** ? Citer une situation de la vie courante pour chacune.

??? corrige "Corrigé"

    1.  `1`, `2`, `3`, `4` : l’ordre est **conservé**.

    2.  Cartes prises : `5`, puis `2`, puis `7`. Rangée finale : la seule carte `4`. Même séquence qu’à la question 2, mais pas les mêmes cartes prises : seule la règle a changé.

    3.  Le tas renverse l’ordre (pile d’assiettes, pile de copies à corriger, bouton « page précédente ») ; la rangée le conserve (file d’attente à la cantine, documents envoyés à une imprimante, caisse d’un magasin).

### <span class="exo-num">Exercice 3</span> — Le bouton « Annuler » <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-03-structures-lineaires-piles-files-listes-act-1-3 }

Dans un éditeur de texte, on tape successivement les mots `Le`, `chat`, `dort`, `bien` : chaque mot tapé est une carte. Le raccourci `Ctrl+Z` **annule** le dernier mot tapé ; `Ctrl+Y` **refait** le dernier mot annulé.

1.  On appuie deux fois sur `Ctrl+Z`. Quel texte reste-t-il ? Quels mots ont été annulés, et dans quel ordre ?

2.  On appuie ensuite une fois sur `Ctrl+Y`. Quel mot revient ? Pour ranger les mots annulés, faut-il un tas ou une rangée ? Combien de paquets de cartes l’éditeur doit-il tenir en tout ?

3.  Repartir du texte `Le chat dort bien`, appuyer deux fois sur `Ctrl+Z`, puis taper le mot `mal`. Serait-il logique de pouvoir encore « refaire » `bien` ? Que doit-il arriver au paquet des mots annulés ?

??? corrige "Corrigé"

    1.  Il reste `Le chat`. Ont été annulés `bien`, puis `dort` : la **dernière** action est annulée la première.

    2.  `dort` revient : c’est le dernier mot annulé. Les mots annulés se rangent donc en **tas** (le dernier annulé est le premier refait). L’éditeur tient **deux tas** : celui des actions faites (pour annuler) et celui des actions annulées (pour refaire). Annuler fait passer une carte du premier tas au second ; refaire fait l’inverse.

    3.  Non : `bien` suivait `dort`, qui n’est plus dans le texte ; le refaire après `mal` donnerait un texte qui n’a jamais existé. La plupart des éditeurs **vident** le tas des actions annulées dès qu’une nouvelle action est faite.

### <span class="exo-num">Exercice 4</span> — Ce qu’on a découvert <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-03-structures-lineaires-piles-files-listes-act-1-4 }

1.  Recopier et compléter sur le cahier, avec vos mots.

    - Avec la règle du tas, la carte qui sort est toujours …

    - Avec la règle de la rangée, la carte qui sort est toujours …

    - Les deux paquets contiennent les mêmes cartes ; ce qui les distingue, c’est …

??? corrige "Corrigé"

    1.  Avec la règle du tas, la carte qui sort est toujours **la dernière entrée**. Avec la règle de la rangée, c’est toujours **la première entrée** (la plus ancienne). Ce qui distingue les deux paquets, ce n’est pas leur contenu mais **la façon d’ajouter et de retirer** : par où on entre, par où on sort.
