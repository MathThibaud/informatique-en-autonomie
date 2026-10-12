# TP et projets

<p class="sous-titre">Les données structurées et leur traitement</p>

## <span class="etiquette">TP 1</span> Tableur 1 : notes, fréquences et graphiques

*Excel, le grand oublié des programmes — I*

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/seconde/05-tp-tableur-1){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/seconde-05-tp-tableur-1.zip){ .md-button }

Usage de l’IA, indiqué sur chaque exercice : <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> aucune ; <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> en appui (déboguer, reformuler, vérifier ; la réponse finale est écrite et comprise par vous) ; <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> l’exercice s’appuie sur une réponse d’IA. Voir la charte d’usage de l’IA.

!!! encadre "Pour commencer"

    Récupérer le fichier `tableur1.xlsx` (à télécharger : <https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/seconde/05-tp-tableur-1>). Il contient **quatre feuilles** nommées « `Exercice 1` », « `Exercice 2` », « `Exercice 3` » et « `Exercice 4` » (onglets en bas de la fenêtre). Les **données de départ** y sont déjà saisies ; les cellules sur **fond jaune** sont **à compléter**.

### <span class="exo-num">Exercice 1</span> — Notes d’un contrôle (feuille `Exercice 1`) <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-les-donnees-structurees-et-leur-traiteme-tp-1-1 }

On a relevé, dans l’ordre croissant, les notes obtenues à un contrôle de mathématiques par les élèves de la classe de 2<sup>de</sup> 11 (cellules `C2:O3`).

1.  **Moyenne d’une série de données.** En `B5`, saisir la formule `=MOYENNE(C2:O3)`. *(Utiliser le menu des fonctions, choisir `MOYENNE`, puis sélectionner la plage `C2` à `O3`.)*

2.  **Ligne des effectifs.** La ligne `8` donne les différentes notes. Compléter la ligne des **effectifs** (`C9:O9`) : pour chaque note, le nombre d’élèves l’ayant obtenue.

3.  **Fréquences (décimales, puis en pourcentage).**

    1.  En `P9`, calculer l’**effectif total** avec `=SOMME(C9:O9)`.

    2.  En `C10`, calculer la fréquence de la première note avec `=C9/$P9`.

    3.  Recopier `C10` vers `D10:O10` avec la **poignée de recopie** (la petite croix en bas à droite de la cellule). *Le symbole `$` **fixe** la colonne `P` lors de la recopie.*

    4.  En `C11`, saisir `=C10`. Puis, par un clic droit » « Format de cellule » » onglet `Nombre`, choisir **Pourcentage**, `0` décimale. Recopier vers `D11:O11`.

    5.  Compléter `P10` et `P11` avec `=SOMME(C10:O10)` et `=SOMME(C11:O11)`. Que doivent valoir ces totaux ?

4.  **Effectifs cumulés croissants (E.C.C.).**

    1.  En `C12`, saisir `=C9`.

    2.  En `D12`, saisir `=C12+D9`, puis recopier vers `E12:O12`.

5.  **Moyenne pondérée par les effectifs.** En `B14`, saisir la formule  
    `=SOMMEPROD(C8:O8;C9:O9)/P9`.  
    **Comparer** avec la moyenne trouvée à la question **1** : que remarque-t-on ?

### <span class="exo-num">Exercice 2</span> — Fréquences et F.C.C. (feuille `Exercice 2`) <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-les-donnees-structurees-et-leur-traiteme-tp-1-2 }

La feuille `Exercice 2` donne les effectifs du lycée par **année de naissance**. Compléter, à l’aide de formules, la ligne des **fréquences** et celle des **fréquences cumulées croissantes** (F.C.C.).

### <span class="exo-num">Exercice 3</span> — Graphiques (feuille `Exercice 3`) <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-les-donnees-structurees-et-leur-traiteme-tp-1-3 }

La feuille `Exercice 3` donne les effectifs du lycée par **niveau** et par **dominante**.

1.  Sélectionner les cellules `A1:D2`, puis *Insertion » Graphique » Secteurs* pour construire un **diagramme circulaire** des élèves de Seconde par dominante.

2.  Sélectionner `A1:D4`, puis *Insertion » Graphique » Colonnes* pour construire un **histogramme** des effectifs par niveau et par dominante. Soigner le titre et la légende.

### <span class="exo-num">Exercice 4</span> — Moyennes (feuille `Exercice 4`) <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-les-donnees-structurees-et-leur-traiteme-tp-1-4 }

La feuille `Exercice 4` donne les salaires d’une entreprise (colonne `A`).

1.  En `D2`, faire calculer le **nombre d’employés** (fonction `NB`).

2.  En `D3`, faire calculer la **masse salariale**, c’est-à-dire le montant total des salaires (fonction `SOMME`).

3.  En `D4`, faire calculer le **salaire moyen** (fonction `MOYENNE`).

## <span class="etiquette">TP 2</span> Tableur 2 : suites de nombres et conjecture

*Excel, le grand oublié des programmes — II*

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/seconde/05-tp-tableur-2){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/seconde-05-tp-tableur-2.zip){ .md-button }

Usage de l’IA, indiqué sur chaque exercice : <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> aucune ; <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> en appui (déboguer, reformuler, vérifier ; la réponse finale est écrite et comprise par vous) ; <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> l’exercice s’appuie sur une réponse d’IA. Voir la charte d’usage de l’IA.

!!! encadre "Pour commencer"

    Récupérer le fichier `tableur2.xlsx` (à télécharger : <https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/seconde/05-tp-tableur-2>). Il contient les feuilles « `Exercice 1` » à « `Exercice 4` » et un « `Bonus` ». Les valeurs de départ y sont déjà en place (cellules sur fond jaune à compléter).

### <span class="exo-num">Exercice 1</span> — Une suite de nombres, pas de 1 (feuille `Exercice 1`) <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-les-donnees-structurees-et-leur-traiteme-tp-2-1 }

Pour créer une suite de 30 nombres consécutifs dans la colonne `A` : la cellule `A1` contient déjà le premier nombre, `5`. En `A2`, saisir la formule `=A1+1`, puis, à l’aide de la **poignée de recopie**, créer la suite de 30 nombres dans la colonne `A`. On dit que le **pas** entre deux nombres est de `1`.

### <span class="exo-num">Exercice 2</span> — Un pas réglable (feuille `Exercice 2`) <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-les-donnees-structurees-et-leur-traiteme-tp-2-2 }

On veut compter de `8` en `8` à partir de `5`. Le **pas** est en `C1` (`8`) et le premier nombre en `A1` (`5`). En `A2`, saisir `=A1+C$1`, puis recopier vers le bas. *Le symbole `$` **fixe** la ligne `1` lors de la recopie.*

### <span class="exo-num">Exercice 3</span> — Somme d’une suite : émettre une conjecture (feuille `Exercice 3`) <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-les-donnees-structurees-et-leur-traiteme-tp-2-3 }

On compte de `3` en `3` à partir de `5` (pas en `C1`, premier terme en `A1`). En `A2`, saisir `=A1+C$1` et recopier pour obtenir 30 termes.

1.  En `C4`, le **nombre de termes** : `=NB(A1:A30)`.

2.  En `C7`, la plus petite valeur : `=MIN(A1:A30)`. En `C8`, la plus grande : `=MAX(A1:A30)`.

3.  En `C9`, la **somme des deux valeurs extrêmes**. En `C12`, la **somme de tous les termes** : `=SOMME(A1:A30)`.

4.  **Conjecture.** En faisant varier les données, trouver la relation entre la **somme des termes**, le **nombre de termes** et les **valeurs extrêmes**. Noter votre idée.

### <span class="exo-num">Exercice 4</span> — Contrôler la conjecture : départ aléatoire (feuille `Exercice 4`) <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-les-donnees-structurees-et-leur-traiteme-tp-2-4 }

On fait varier automatiquement le premier terme.

1.  En `B1`, un décimal aléatoire entre 0 et 1 : `=ALEA()`. En `B2` : `=B1*100`. En `B3`, un **entier** aléatoire entre 0 et 99 : `=ENT(B2)` (partie entière).

2.  Le pas est en `E1` (`3`). En `C1`, recopier le nombre aléatoire : `=B3`. Créer dans la colonne `C` une suite de 30 termes de pas 3.

3.  Compléter `E4`, `E7`, `E8`, `E9` et `E12` (comme en `Exercice 3`, mais sur la colonne `C`). **Vérifier** la conjecture. On peut appuyer sur `F9` pour retirer un nouveau nombre aléatoire.

### <span class="exo-num">Exercice 5</span> — BONUS : départ *et* pas quelconques (feuille `Bonus`) <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-les-donnees-structurees-et-leur-traiteme-tp-2-5 }

Faire varier automatiquement le premier terme **et** le pas.

1.  Obtenir en `B3` un entier aléatoire entre 0 et 99. Choisir un pas entier quelconque en `E1`.

2.  Dans la colonne `C`, créer une suite d’autant de termes que voulu, de pas celui de `E1`, à partir de `B3`.

3.  Compléter `E2`, `E7`, `E8`, `E9` et `E12` en prenant pour plage la **colonne `C` entière** : `C:C`. Vérifier la conjecture.

## <span class="etiquette">TP 3</span> Tableur 3 : représenter et résumer une série

*Excel, le grand oublié des programmes — III*

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/seconde/05-tp-tableur-3){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/seconde-05-tp-tableur-3.zip){ .md-button }

Usage de l’IA, indiqué sur chaque exercice : <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> aucune ; <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> en appui (déboguer, reformuler, vérifier ; la réponse finale est écrite et comprise par vous) ; <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> l’exercice s’appuie sur une réponse d’IA. Voir la charte d’usage de l’IA.

!!! encadre "Pour commencer"

    Récupérer le fichier `tableur3.xlsx` (à télécharger : <https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/seconde/05-tp-tableur-3>). Il contient quatre feuilles (« `Exercice 1` » à « `Exercice 4` ») dont les données sont déjà saisies.

### <span class="exo-num">Exercice 1</span> — Représentation de séries statistiques (feuille `Exercice 1`) <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-les-donnees-structurees-et-leur-traiteme-tp-3-1 }

**1<sup>er</sup> cas : série statistique discrète.** Nombre de frères et sœurs parmi les 1240 élèves d’un lycée :

\begin{adjustbox}{max width=\textwidth}
\begin{tabular}{cccccccccc}
\hline
Nombre de frères et sœurs & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 \\
\hline
Effectifs & 311 & 586 & 215 & 59 & 31 & 19 & 11 & 6 & 2 \\
\hline
\end{tabular}
\end{adjustbox}

**Diagramme en barres :** via *Insertion » Graphique*, représenter cette série par un diagramme en barres (soigner le titre et la légende). Résultat attendu :

![](../figures/30aed9402f145174.svg){ .tikz loading=lazy }

**2<sup>e</sup> cas : série à classes.** Durée des interventions :

\begin{adjustbox}{max width=\textwidth}
\begin{tabular}{ccccccccc}
\hline
Durée (min) & $0 \leq t < 15$ & $15 \leq t < 30$ & $30 \leq t < 45$ & $45 \leq t < 60$ & $60 \leq t < 75$ & $75 \leq t < 90$ & $90 \leq t < 105$ & $105 \leq t < 120$ \\
\hline
Nombre d'interventions & 32 & 88 & 47 & 25 & 13 & 7 & 5 & 3 \\
\hline
\end{tabular}
\end{adjustbox}

**Histogramme**, puis **diagramme circulaire** de cette série (via *Insertion » Graphique*). Résultats attendus :

![](../figures/1dbb8d6f0baad63e.svg){ .tikz loading=lazy }

![](../figures/8377e301f4ef8de6.svg){ .tikz loading=lazy }

*Pourcentages arrondis à l’unité (total des effectifs : 220).*

### <span class="exo-num">Exercice 2</span> — Caractéristiques de position d’une série en liste (feuille `Exercice 2`) <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-les-donnees-structurees-et-leur-traiteme-tp-3-2 }

Taille (cm) de 10 nourrissons (colonne `A`) : 49 ; 50,5 ; 50 ; 48,5 ; 52 ; 50 ; 49,5 ; 51 ; 49,5 ; 50,5.

- \(a\) Ordonner les tailles par ordre croissant (*Données » Trier*).

- \(b\) En `C1` : `=MEDIANE(A1:A10)`.

- \(c\) En `C2` : `=QUARTILE(A1:A10;1)`. En `C3` : `=QUARTILE(A1:A10;3)`.

- \(d\) En `C4` : `=MOYENNE(A1:A10)`.

- \(e\) En `C5` : calculer l’**étendue** (`=MAX(A1:A10)-MIN(A1:A10)`).

### <span class="exo-num">Exercice 3</span> — Caractéristiques de position dans un tableau (feuille `Exercice 3`) <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-les-donnees-structurees-et-leur-traiteme-tp-3-3 }

Tailles de 885 nourrissons :

\begin{adjustbox}{max width=\textwidth}
\begin{tabular}{clllllllllllll}
\hline Taille $t$ & 47,5 & 48 & 48,5 & 49 & 49,5 & 50 & 50,5 & 51 & 51,5 & 52 & 52,5 & 53 & TOTAL \\
\hline Effectif $n$ & 55 & 77 & 105 & 115 & 132 & 154 & 66 & 77 & 55 & 25 & 13 & 11 & \\
\hline $t \times n$ & & & & & & & & & & & & & \\
\hline E. C. C. & 55 & & & & & & & & & & & & \\
\hline
\end{tabular}
\end{adjustbox}

- \(a\) Compléter la ligne des produits $t \times n$ (par exemple `=B3*B4`, à recopier).

- \(b\) Calculer la moyenne à l’aide de $\dfrac{\sum (t \times n)}{\sum n}$.

- \(c\) Calculer l’étendue.

- \(d\) Trouver médiane, premier et troisième quartile par lecture de la ligne des E.C.C. *Méthode : avec un effectif total $N$, le premier quartile est la première valeur dont l’E.C.C. atteint (ou dépasse) $N/4$ ; la médiane, la première dont l’E.C.C. atteint $N/2$ ; le troisième quartile, la première dont l’E.C.C. atteint $3N/4$.*

### <span class="exo-num">Exercice 4</span> — Caractéristiques de position pour données groupées (feuille `Exercice 4`) <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-05-les-donnees-structurees-et-leur-traiteme-tp-3-4 }

Tailles de 640 nourrissons :

\begin{adjustbox}{max width=\textwidth}
\begin{tabular}{clllllllllll}
\hline Taille $t$ & [45;46[ & [46;47[ & [47;48[ & [48;49[ & [49;50[ & [50;51[ & [51;52[ & [52;53[ & [53;54[ & [54;55[ & TOTAL \\
\hline Effectif $n$ & 10 & 25 & 35 & 65 & 128 & 190 & 95 & 45 & 32 & 15 & \\
\hline Fréquence & 1,56\% & & & & & & & & & & \\
\hline F. C. C. & 1,56\% & & & & & & & & & & \\
\hline Centre de classe & 45,5 & & & & & & & & & & \\
\hline
\end{tabular}
\end{adjustbox}

- \(a\) Compléter les fréquences, les centres de classe et les F.C.C.

- \(b\) Localiser médiane, premier et troisième quartile *(même méthode, avec les F.C.C. : première classe dont la F.C.C. atteint $25\,\%$, $50\,\%$, puis $75\,\%$)*.

- \(c\) Calculer la moyenne avec `=SOMMEPROD(centres;effectifs)/total`.

!!! danger "Conversion impossible"
    Ce passage n'a pas pu être converti.

## Corrigé

??? corrige "Corrigé"

    !!! danger "Conversion impossible"
        Ce passage n'a pas pu être converti.
