# Activités préparatoires

<p class="sous-titre">Les données en tables</p>

## <span class="etiquette">Activité 1</span> Ouvrir un fichier CSV

*ce que contient vraiment un fichier de données*

<p class="infos-activite">Durée : 20 min · Seul ou en binôme, sur un poste</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/08-activite-fichiers-csv){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/premiere-08-activite-fichiers-csv.zip){ .md-button }

!!! consignes "Consignes"

    - Aucun programme à écrire ; les réponses se notent sur le cahier.

    - Fichiers à télécharger (lien ci-dessus) : `prenoms.csv` (les prénoms les plus donnés en France en 2023 et 2025, d’après l’INSEE), `communes.csv` et `departements.csv`.

    - Outils : un **éditeur de texte** (Bloc-notes, TextEdit, l’éditeur de Python…) et un **tableur** (LibreOffice Calc ou autre).

### <span class="exo-num">Exercice 1</span> — Dans un éditeur de texte <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-08-les-donnees-en-tables-act-1-1 }

Ouvrir `prenoms.csv` avec l’**éditeur de texte**.

1.  Combien le fichier compte-t-il de lignes ? En quoi la première ligne est-elle différente de toutes les autres ?

2.  Quel caractère sépare les valeurs sur une ligne ?

3.  Que signifie, à votre avis, la ligne `Jade,F,2025,2925` ? Donner le sens de chacune des quatre valeurs.

??? corrige "Corrigé"

    **1.** **41** lignes. La première, `prenom,sexe,annee,nombre`, ne décrit pas un prénom : elle donne le **nom des colonnes**.  
    **2.** La **virgule**.  
    **3.** En **2025**, le prénom **Jade** a été donné **2 925** fois à des **filles** (`F`). On devine sans peine `prenom`, `annee`, `nombre` ; `F`/`G` (fille/garçon) se déduit des prénoms.

### <span class="exo-num">Exercice 2</span> — Dans un tableur <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-08-les-donnees-en-tables-act-1-2 }

Ouvrir maintenant `prenoms.csv` avec le **tableur**. Une fenêtre d’import demande le séparateur : choisir la **virgule**.

1.  Combien y a-t-il de colonnes ? de lignes de données (sans compter la première) ?

2.  Rouvrir le fichier en choisissant cette fois le **point-virgule** comme séparateur. Que se passe-t-il ? Pourquoi ?

3.  Ouvrir `communes.csv` dans le tableur (séparateur : virgule). Comment s’affiche le code `dep` de Nice ? Et dans l’éditeur de texte ? Pourquoi cette différence peut-elle poser problème ?

??? corrige "Corrigé"

    **4.** **4** colonnes, **40** lignes de données.  
    **5.** Tout se retrouve dans **une seule colonne** : il n’y a aucun point-virgule dans le fichier, donc le tableur ne sait pas où couper. C’est exactement le piège du « fichier à la française » (séparateur `;`) lu avec la virgule, ou l’inverse.  
    **6.** Le tableur affiche en général **6** au lieu de `06` : il a « deviné » un nombre et supprimé le zéro. L’éditeur de texte montre bien `06`, car le fichier ne contient que du **texte**. Le problème : un code n’est pas un nombre (`2A` ne pourrait pas en être un), et si l’on réenregistre depuis le tableur, le fichier est modifié sans qu’on l’ait voulu. *À retenir pour Python : tout ce qu’on lit dans un CSV est une chaîne.*

### <span class="exo-num">Exercice 3</span> — Chercher une information à la main <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-08-les-donnees-en-tables-act-1-3 }

Répondre **sans formule ni tri automatique**, en lisant les lignes une à une (dans l’éditeur ou dans le tableur).

1.  Quel est le prénom de garçon le plus donné en 2025, et combien de fois ? Quelles lignes avez-vous dû regarder ? Lesquelles avez-vous ignorées ?

2.  Combien de filles, au total, ont reçu le prénom Louise en 2023 et en 2025 ?

3.  Dans quelle région se trouve Menton ? Quels fichiers a-t-il fallu consulter, et grâce à quelle colonne ? Peut-on répondre à la même question pour Ajaccio ?

??? corrige "Corrigé"

    **7.** **Gabriel**, **4 625** fois. On n’a regardé que les lignes où le sexe vaut `G` *et* l’année `2025` (10 lignes) ; on a ignoré les filles et l’année 2023. On a donc d’abord **filtré** les lignes, puis cherché le **maximum**.  
    **8.** $3\,177 + 3\,070 = \mathbf{6\,247}$ (deux lignes `Louise` à additionner).  
    **9.** Menton a pour code `06` dans `communes.csv` ; dans `departements.csv`, le code `06` correspond aux Alpes-Maritimes, région **Provence-Alpes-Cote d’Azur** (écrite sans accent dans le fichier). Il a fallu les **deux fichiers**, reliés par la colonne commune `dep`. Pour Ajaccio (code `2A`), c’est impossible : ce code n’apparaît pas dans `departements.csv`.

### <span class="exo-num">Exercice 4</span> — Ce qu’on a découvert <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-08-les-donnees-en-tables-act-1-4 }

1.  **Ce qu’on a découvert.** Recopier la phrase sur le cahier en complétant les trous **(a)** à **(e)** avec les mots : *texte*, *en-tête*, *enregistrement*, *séparateur*, *colonne*.

    « Un fichier CSV est un simple fichier … **(a)**. Sa première ligne, l’… **(b)**, donne le nom de chaque … **(c)**. Chaque ligne suivante est un … **(d)** : elle décrit un individu. Sur une ligne, les valeurs sont séparées par un … **(e)**, qu’il faut connaître pour bien lire le fichier. »

??? corrige "Corrigé"

    **10.** « Un fichier CSV est un simple fichier **texte**. Sa première ligne, l’**en-tête**, donne le nom de chaque **colonne**. Chaque ligne suivante est un **enregistrement** : elle décrit un individu. Sur une ligne, les valeurs sont séparées par un **séparateur**, qu’il faut connaître pour bien lire le fichier. »
