# TP et projets

<p class="sous-titre">La photographie numérique</p>

## <span class="etiquette">Projet 1</span> Dessiner des drapeaux avec Python

|  |  |
|:---|:---|
| **Idée** | Jusqu’ici, on *modifiait* des images. Ici, on va en **fabriquer** à partir de rien : des drapeaux. |
| **Objectif** | Réinvestir le codage **RVB** en respectant les **proportions** et les **couleurs officielles** de chaque drapeau. |
| **Outil** | la bibliothèque `PIL` (`Image.new`), les **boucles** du cours, et le codage **RVB** des couleurs. |
| **IA** | <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> **Autorisé** : demander une explication (le rôle d’une fonction de `PIL`, le sens d’un message d’erreur). **Interdit** : faire écrire le programme par une IA. Vous devez pouvoir expliquer chaque ligne de votre code. |

## Créer une image et la remplir

On sait déjà *lire* et *modifier* les pixels d’une image avec `getpixel`, `putpixel` et une double boucle `for`. Pour dessiner un drapeau, il suffit en plus de créer une image **vierge** avec `Image.new`, puis de **colorier chaque pixel** en **RVB** :

```python
from PIL import Image

largeur, hauteur = 500, 400
img = Image.new("RGB", (largeur, hauteur))     # image vierge (noire) largeur x hauteur

for y in range(hauteur):
    for x in range(largeur):
        img.putpixel((x, y), (255, 0, 0))      # (R, V, B) : ici, tout en rouge
```

Toute l’idée est là : dans la boucle, on **teste la position** du pixel $(x, y)$ pour choisir sa couleur **RVB**. Rappel : le point $(0,0)$ est en **haut à gauche**, $x$ va vers la droite, $y$ vers le bas.

!!! remarque "Remarque"

    Les **dimensions** (proportions) et les **codes couleur** exacts (souvent en RVB) de chaque drapeau se trouvent sur la **Wikipédia anglaise** (*en.wikipedia.org*), aux rubriques « *Proportion* » et « *Colours* ». Prenez l’habitude d’aller les y chercher **dès** Monaco et la France — et pensez à **citer vos sources**.

## Exemple 1 : le drapeau de Monaco

Le drapeau monégasque a des **proportions 4:5** (4 de haut pour 5 de large) et se compose de **deux bandes horizontales** égales : **rouge** en haut, **blanc** en bas. On choisit donc une image de $500 \times 400$ (largeur $\times$ hauteur, soit bien $5:4$). Pour chaque pixel, on regarde s’il est dans la **moitié haute** ($y < \text{hauteur}/2$) ou basse :

```python
from PIL import Image

largeur, hauteur = 500, 400
img = Image.new("RGB", (largeur, hauteur))

rouge = (206, 17, 38)                       # rouge de Monaco
blanc = (255, 255, 255)

for y in range(hauteur):
    for x in range(largeur):
        if y < hauteur // 2:
            img.putpixel((x, y), rouge)     # bande du haut
        else:
            img.putpixel((x, y), blanc)     # bande du bas

img.save("monaco.png")
img.show()
```

\*(image manquante : 03t1_drapeau_monaco)\*

## Exemple 2 : le drapeau de la France

Le drapeau français a des **proportions 2:3** et se compose de **trois bandes verticales** égales : **bleu**, **blanc**, **rouge**. On prend une image de $600 \times 400$ (soit $3:2$). Cette fois, on teste la position `x` du pixel (trois zones) :

```python
from PIL import Image

largeur, hauteur = 600, 400
img = Image.new("RGB", (largeur, hauteur))

bleu  = (0, 85, 164)
blanc = (255, 255, 255)
rouge = (239, 65, 53)

for y in range(hauteur):
    for x in range(largeur):
        if x < largeur // 3:
            img.putpixel((x, y), bleu)      # bande de gauche
        elif x < 2 * largeur // 3:
            img.putpixel((x, y), blanc)     # bande du milieu
        else:
            img.putpixel((x, y), rouge)     # bande de droite

img.save("france.png")
img.show()
```

\*(image manquante : 03t1_drapeau_france)\*

!!! activite "Activité — Prendre le programme en main"

    Saisir et tester les deux programmes ci-dessus. Puis répondre :

    1.  Dans le programme de la France, à quoi sert `largeur // 3` ? Pourquoi trois zones ?

    2.  Modifier le drapeau de Monaco pour que la bande du haut soit **bleue** au lieu de rouge.

    3.  Que faudrait-il changer pour obtenir un drapeau **deux fois plus grand** ?

## À vous de jouer !

!!! activite "Activité — Des drapeaux à trois bandes"

    En vous inspirant du drapeau français (trois bandes **verticales**) ou en passant à des bandes **horizontales**, dessiner les drapeaux suivants en **respectant proportions et couleurs** (dimensions et codes couleur exacts sur la **version anglaise de Wikipédia**).

    | **Drapeau** | **Description** | **Proportions** |
    |:---|:---|:---|
    | Italie | 3 bandes verticales : vert, blanc, rouge | 2:3 |
    | Belgique | 3 bandes verticales : noir, jaune, rouge | 13:15 |
    | Allemagne | 3 bandes horizontales : noir, rouge, or (jaune) | 3:5 |
    | Pays-Bas | 3 bandes horizontales : rouge, blanc, bleu | 2:3 |

    *Astuce* : pour des bandes **horizontales**, on teste la position `y` du pixel (`y < hauteur // 3`, etc.) au lieu de `x`.

### Défi 1 : le disque du Japon (à compléter)

Pour le Japon, **pas question** d’utiliser une fonction toute faite comme `ellipse` : ce serait tricher ! On va dessiner le disque **nous-mêmes**, avec l’**équation du cercle**. Un pixel $(x, y)$ se trouve **à l’intérieur** du disque de centre $(x_c, y_c)$ et de rayon $r$ lorsque : $$(x - x_c)^2 + (y - y_c)^2 \ \leqslant\ r^2.$$ Le drapeau du Japon a des proportions $2:3$, un fond blanc et un disque rouge **centré** dont le diamètre vaut $3/5$ de la hauteur. **Compléter** la ligne du `if` en traduisant l’équation ci-dessus en Python.

```python
from PIL import Image

largeur, hauteur = 600, 400              # proportions 2:3
img = Image.new("RGB", (largeur, hauteur), (255, 255, 255))

xc, yc = largeur // 2, hauteur // 2      # centre du drapeau
r = int(0.3 * hauteur)                   # rayon = 3/5 de la demi-hauteur
rouge = (188, 0, 45)

for y in range(hauteur):
    for x in range(largeur):
        if .......................................... :   # A COMPLETER : dans le disque ?
            img.putpixel((x, y), rouge)

img.save("japon.png")
img.show()
```

\*(image manquante : 03t1_drapeau_japon)\*  
Le résultat attendu.

!!! activite "Activité — Le disque du Japon"

    1.  Compléter puis tester le programme.

    2.  Expliquer avec vos mots ce que teste votre condition.

    3.  Modifier le rayon pour obtenir un disque **deux fois plus petit**.

\begin{attention}{L'axe des $y$ est à l'envers !}
L'origine $(0,0)$ est en \textbf{haut à gauche} et l'axe des $y$ est orienté \textbf{vers le bas} :
un $y$ \emph{plus grand} correspond à un point \emph{plus bas} sur l'image. C'est l'\textbf{inverse}
du repère habituel en mathématiques\,! Attention, donc, en écrivant vos \textbf{inégalités} :
« vers le haut » signifie un $y$ \textbf{plus petit}, « vers le bas » un $y$ \textbf{plus grand}.
Le mieux est de \textbf{tester} votre condition sur un pixel dont vous connaissez déjà la couleur
(par exemple un coin).
\end{attention}

### Défi 2 : une diagonale (à compléter)

Passons du cercle à une **droite**. On coupe le drapeau en deux triangles par la **diagonale** qui va du coin $(0,0)$ (haut-gauche) au coin $(\text{largeur}, \text{hauteur})$ (bas-droit). L’équation de cette droite est : $$y = \frac{\text{hauteur}}{\text{largeur}} \times x.$$ Un pixel est **en dessous** de la diagonale (donc dans le triangle du bas) lorsque son $y$ est *plus grand* que celui de la droite, c’est-à-dire lorsque $y > \dfrac{\text{hauteur}}{\text{largeur}} \times x$ (attention à l’axe des $y$ !). **Compléter** la condition.

```python
from PIL import Image

largeur, hauteur = 600, 400
img = Image.new("RGB", (largeur, hauteur))

bleu  = (0, 85, 164)
jaune = (255, 205, 0)

for y in range(hauteur):
    for x in range(largeur):
        if ..........................................  :   # A COMPLETER : sous la diagonale ?
            img.putpixel((x, y), bleu)     # triangle du bas
        else:
            img.putpixel((x, y), jaune)    # triangle du haut

img.save("diagonale.png")
img.show()
```

\*(image manquante : 03t1_drapeau_diagonale)\*  
Le résultat attendu.

!!! activite "Activité — La diagonale"

    1.  Compléter puis tester le programme.

    2.  Échanger les deux triangles (bleu en haut, jaune en bas). Que faut-il changer ?

    3.  **Défi** : obtenir l’*autre* diagonale (du coin haut-droit au coin bas-gauche).

### Défi 3 : des drapeaux plus difficiles

Vous avez maintenant les deux outils : le **cercle** et la **droite**. On peut alors s’attaquer à des drapeaux qui mêlent bandes, triangles et bandes obliques. Le principe ne change pas : on parcourt tous les pixels et on teste une **condition**.

!!! activite "Activité — À vous de relever le défi"

    1.  **Le Bénin** : une bande **verticale** verte à gauche, et à droite **deux bandes horizontales** (jaune en haut, rouge en bas). Réalisable uniquement avec des *rectangles* : à vous de trouver comment les combiner.

    2.  **La Tchéquie** : moitié haute blanche, moitié basse rouge, et un **triangle bleu** à gauche pointant vers le centre. Le triangle se dessine en testant, pour chaque pixel, s’il est *du bon côté* de **deux** droites.

    3.  **Les Seychelles** : cinq **bandes obliques** (bleu, jaune, rouge, blanc, vert) qui partent toutes du coin **en bas à gauche**. Les droites de séparation visent les **tiers** des bords haut et droit (*pas* des angles égaux !) : pour un pixel, on compare sa *pente* $(\text{hauteur}-y)/x$ à celle de ces droites.

!!! activite "Activité — Votre drapeau"

    1.  Choisir un drapeau (pays, région, club…), rechercher ses **dimensions** et ses **couleurs** exactes, puis le reproduire le plus fidèlement possible.

    2.  **Bonus** : expliquer pourquoi certains drapeaux (avec une *étoile*, un *blason*…) sont presque impossibles à dessiner ainsi.

**Crédits.** Les images de drapeaux de ce projet sont produites par les programmes Python qui les accompagnent (bibliothèque `PIL`). Les drapeaux nationaux ne sont pas protégés par le droit d’auteur ; couleurs et proportions d’après la Wikipédia anglaise.

## <span class="etiquette">Projet 2</span> Retoucher un tableau célèbre en RVB

|  |  |
|:---|:---|
| **Idée** | Appliquer vos programmes de traitement d’image à de **vraies œuvres d’art**, pour les transformer comme un artiste numérique. |
| **Objectif** | Parcourir tous les pixels, **modifier les canaux** R, V, B, et recolorer une **zone choisie** avec une condition. |
| **Fichiers** | `nuit_etoilee.jpg` et `blue_boy.jpg` sont fournis (œuvres du **domaine public**). À placer dans le même dossier que vos programmes. |
| **IA** | <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> **Autorisé** : demander une explication (le rôle d’une fonction de `PIL`, le sens d’un message d’erreur). **Interdit** : faire écrire le programme par une IA. Vous devez pouvoir expliquer chaque ligne de votre code. |

!!! remarque "Remarque"

    Ces deux tableaux — *La Nuit étoilée* de Vincent **van Gogh** (1889) et *The Blue Boy* (*Le Garçon en bleu*) de Thomas **Gainsborough** (vers 1770) — sont dans le **domaine public** : on peut donc les utiliser et les modifier librement.

## Exemple 1 : recolorer tout un tableau

On parcourt **tous les pixels** et on **échange les canaux** rouge et bleu. Le ciel bleu de Van Gogh devient chaud, et les étoiles jaunes deviennent bleutées.

```python
from PIL import Image

img = Image.open("nuit_etoilee.jpg")
largeur, hauteur = img.size          # recupere la taille automatiquement !

for y in range(hauteur):
    for x in range(largeur):
        r, v, b = img.getpixel((x, y))
        img.putpixel((x, y), (b, v, r))   # on echange R et B
img.save("nuit_modifiee.jpg")
img.show()
```

*(Le parcours de tous les pixels peut prendre quelques secondes : c’est normal.)*

|  |  |
|:--:|:--:|
| \*(image manquante : 03t2_nuit_etoilee)\* | \*(image manquante : 03t2_nuit_etoilee_modif)\* |
|  Original |  Canaux R et B échangés |

!!! activite "Activité — Premiers essais sur La Nuit étoilée"

    1.  Saisir et tester le programme ci-dessus. Que remarque-t-on pour le ciel ? pour les étoiles ?

    2.  À quoi sert la ligne `largeur, hauteur = img.size` ?

    3.  Écrire un programme qui donne le **négatif** du tableau (remplacer chaque canal $c$ par $255 - c$).

    4.  Écrire un programme qui transforme le tableau en **niveaux de gris** (chaque canal remplacé par la moyenne $(r+v+b)//3$).

## Exemple 2 : changer la couleur d’un vêtement

Ici, on ne modifie **qu’une partie** de l’image, grâce à une condition `if`. Objectif : transformer le **costume bleu** du garçon en **costume rouge**, sans toucher au visage ni au décor. On repère les pixels où le **bleu domine**.

```python
from PIL import Image

img = Image.open("blue_boy.jpg")
largeur, hauteur = img.size

for y in range(hauteur):
    for x in range(largeur):
        r, v, b = img.getpixel((x, y))
        # le bleu domine (le costume) -> on repeint en rouge
        if b > r + 15 and b > v + 5 and b > 60:
            gris = (r + v + b) // 3          # on garde la luminosite (les plis)
            img.putpixel((x, y), (min(255, gris + 50), gris // 3, gris // 4))
img.save("garcon_modifie.jpg")
img.show()
```

|  |  |
|:--:|:--:|
| \*(image manquante : 03t2_blue_boy)\* | \*(image manquante : 03t2_blue_boy_modif)\* |
|  Original |  Costume recoloré |

!!! activite "Activité — Améliorer et personnaliser"

    1.  Le repérage est **imparfait** (certaines zones d’ombre sont oubliées). Modifier les valeurs de la condition pour **mieux** recolorer le costume.

    2.  Changer la couleur finale : essayer un costume **vert**, puis **violet**.

    3.  En gardant la luminosité `gris`, expliquer pourquoi les **plis** du tissu restent visibles après recoloration.

## Le projet

!!! activite "Activité — Votre œuvre numérique"

    Choisir **une œuvre du domaine public** (l’une des deux fournies, ou une autre trouvée sur un site d’images libres de droit) et réaliser une **transformation personnelle** qui combine au moins :

    - une transformation **globale** (négatif, niveaux de gris, échange de canaux…) ;

    - une modification **localisée** (changer la couleur d’un objet, d’un ciel, d’un vêtement).

    Vous rendrez : l’**image de départ**, votre **image transformée**, votre **programme Python**, et **deux ou trois phrases** expliquant ce que fait votre programme et d’où vient l’œuvre (**source** et licence).

## Grille d’évaluation

| **Critère**                                              | **Points** |
|:---------------------------------------------------------|:----------:|
| Le programme fonctionne et parcourt correctement l’image |     /6     |
| Transformation globale réussie                           |     /4     |
| Modification localisée (avec condition `if`) réussie     |     /5     |
| Explications claires + source de l’œuvre citée           |     /3     |
| Originalité et soin du rendu                             |     /2     |
| **Total**                                                |  ** /20**  |

Les versions modifiées des deux tableaux sont produites par les programmes Python de ce projet.

!!! danger "Conversion impossible"
    Ce passage n'a pas pu être converti.

## Corrigé

??? corrige "Corrigé"

    !!! danger "Conversion impossible"
        Ce passage n'a pas pu être converti.
