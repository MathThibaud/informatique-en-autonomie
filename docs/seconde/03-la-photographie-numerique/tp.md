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
r = int(0.3 * hauteur)                   # rayon = 3/5 de la demi-hauteur ; int garde la partie entiere
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

!!! encadre "$triangle$ L’axe des $y$ est à l’envers !"

    L’origine $(0,0)$ est en **haut à gauche** et l’axe des $y$ est orienté **vers le bas** : un $y$ *plus grand* correspond à un point *plus bas* sur l’image. C’est l’**inverse** du repère habituel en mathématiques ! Attention, donc, en écrivant vos **inégalités** : « vers le haut » signifie un $y$ **plus petit**, « vers le bas » un $y$ **plus grand**. Le mieux est de **tester** votre condition sur un pixel dont vous connaissez déjà la couleur (par exemple un coin).

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

    3.  **Les Seychelles** : cinq **bandes obliques** (bleu, jaune, rouge, blanc, vert) qui partent toutes du coin **en bas à gauche**. Les droites de séparation visent les **tiers** des bords haut et droit (*pas* des angles égaux !) : pour un pixel, on compare sa *pente* $(\text{hauteur}-y)/x$ à celle de ces droites (attention : sur le bord gauche, $x = 0$ et on ne peut pas diviser par $0$ : traiter ces pixels à part).

!!! activite "Activité — Votre drapeau"

    1.  Choisir un drapeau (pays, région, club…), rechercher ses **dimensions** et ses **couleurs** exactes, puis le reproduire le plus fidèlement possible.

    2.  **Bonus** : expliquer pourquoi certains drapeaux (avec une *étoile*, un *blason*…) sont presque impossibles à dessiner ainsi.

## Grille d’évaluation

La **moitié des points** récompense vos **initiatives** : allez au-delà de ce qui est demandé, et gardez une trace de ce que vous avez cherché et essayé.

<table>
<thead>
<tr>
<th style="text-align: left;"><strong>Critère</strong></th>
<th style="text-align: center;"><strong>Points</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" style="text-align: left;"><strong>Le socle</strong></td>
</tr>
<tr>
<td style="text-align: left;">Les quatre drapeaux à trois bandes sont dessinés, avec les proportions et les couleurs de la Wikipédia anglaise</td>
<td style="text-align: center;"> /3</td>
</tr>
<tr>
<td style="text-align: left;">Le drapeau du Japon est complet : disque centré, de la bonne taille, condition expliquée</td>
<td style="text-align: center;"> /2</td>
</tr>
<tr>
<td style="text-align: left;">La diagonale est obtenue, et vous savez échanger les deux triangles</td>
<td style="text-align: center;"> /2</td>
</tr>
<tr>
<td style="text-align: left;">Votre code est lisible : noms de variables parlants, commentaires sur les lignes importantes</td>
<td style="text-align: center;"> /1</td>
</tr>
<tr>
<td style="text-align: left;">Vous expliquez (à l’oral ou par écrit) le rôle de chaque ligne d’un de vos programmes</td>
<td style="text-align: center;"> /2</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Vos initiatives</strong></td>
</tr>
<tr>
<td style="text-align: left;">Vous avez dessiné des drapeaux supplémentaires de votre choix, sources (dimensions, couleurs) citées</td>
<td style="text-align: center;"> /3</td>
</tr>
<tr>
<td style="text-align: left;">Vous avez réussi un ou plusieurs défis : autre diagonale, Bénin, Tchéquie, Seychelles…</td>
<td style="text-align: center;"> /2</td>
</tr>
<tr>
<td style="text-align: left;">Vous avez inventé un effet ou une variante (dégradé, contour, drapeau « délavé », mélange de formes…)</td>
<td style="text-align: center;"> /2</td>
</tr>
<tr>
<td style="text-align: left;">Vous avez cherché par vous-même une fonction ou une notion (documentation, tutoriel) et vous savez l’expliquer ; les formes demandées restent dessinées pixel par pixel</td>
<td style="text-align: center;"> /2</td>
</tr>
<tr>
<td style="text-align: left;">Soin et originalité de l’ensemble (rendu, présentation des images)</td>
<td style="text-align: center;"> /1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Total</strong></td>
<td style="text-align: center;"><strong> /20</strong></td>
</tr>
</tbody>
</table>

**Crédits.** Les images de drapeaux de ce projet sont produites par les programmes Python qui les accompagnent (bibliothèque `PIL`). Les drapeaux nationaux ne sont pas protégés par le droit d’auteur ; couleurs et proportions d’après la Wikipédia anglaise.

??? corrige "Corrigé de l'activité"

    Notions du cours mobilisées

    - **Pixel**, codage **RVB** (trois nombres de 0 à 255), **définition** et **résolution**.

    - **Modifier une image par programme** (Python + PIL) : éclaircir, changer une couleur, c’est changer les valeurs des pixels.

    - **Algorithmes des appareils** : HDR, débruitage, accentuation, embellissement automatique.

    - **Une photo n’est plus une preuve** en soi : esprit critique (d’où vient l’image ? qui l’a publiée ?).

    - **Métadonnées EXIF** : le fichier peut garder la trace du logiciel, mais elles s’effacent.

    Arguments attendus

    <table>
    <thead>
    <tr>
    <th style="text-align: left;"><strong>POUR (oui) : toujours signaler</strong></th>
    <th style="text-align: left;"><strong>CONTRE (non) : pas d’obligation générale</strong></th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: left;"><ul>
    <li><p><strong>Santé publique</strong> : des corps impossibles à atteindre abîment l’image de soi (doc. 1).</p></li>
    <li><p><strong>Droit d’être informé</strong> : une retouche est souvent invisible, celui qui regarde doit savoir (cours).</p></li>
    <li><p><strong>La loi le fait déjà</strong> pour la publicité et l’influence commerciale ; il suffit d’aller plus loin (doc. 1 et 2).</p></li>
    <li><p><strong>Les filtres sont partout</strong> sur les réseaux, or la loi ne vise que l’influence commerciale : une photo personnelle retouchée échappe à toute mention (doc. 2). Les jeunes se comparent pourtant à ces images.</p></li>
    <li><p><strong>Confiance</strong> : la presse montre qu’on peut fixer une règle claire (doc. 4).</p></li>
    <li><p><strong>C’est techniquement simple</strong> : une mention, ou une trace dans les métadonnées (doc. 4).</p></li>
    </ul></td>
    <td style="text-align: left;"><ul>
    <li><p><strong>Toute photo est déjà calculée</strong> par le smartphone (doc. 3, cours) : où placer la limite ?</p></li>
    <li><p><strong>Mention inutile si elle est partout</strong> : on ne la lit plus (doc. 3).</p></li>
    <li><p><strong>Liberté artistique</strong> : la retouche fait partie du travail du photographe depuis toujours (doc. 3).</p></li>
    <li><p><strong>Impossible à contrôler</strong> pour des milliards de photos personnelles ; les métadonnées s’effacent (doc. 4).</p></li>
    <li><p><strong>Distinguer les cas</strong> : la loi vise déjà ce qui trompe dans un but commercial (silhouette, visage) (doc. 1 et 2).</p></li>
    <li><p><strong>Retouche légère <span class="math inline">≠</span> tromperie</strong> : corriger la lumière ne change pas ce que montre l’image (doc. 1 et 4).</p></li>
    </ul></td>
    </tr>
    </tbody>
    </table>

    *Arguments de l’autre camp souvent jugés solides dans la trace écrite :* un élève POUR retient souvent « une mention mise sur toutes les photos finirait par ne plus être lue » ; un élève CONTRE, « une silhouette affinée dans une publicité trompe vraiment celui qui regarde ».

    Questions de relance (pour le modérateur)

    1.  Éclaircir une photo et affiner une silhouette : est-ce la même chose ? (pensez aux pixels et à ce que montre l’image)

    2.  La retouche automatique du smartphone (doc. 3) doit-elle être signalée ?

    3.  Pourquoi la loi vise-t-elle la publicité et les influenceurs, et pas vos photos de vacances (doc. 1 et 2) ?

    4.  La règle de la presse (doc. 4) pourrait-elle s’appliquer aux réseaux sociaux ?

    !!! encadre "Synthèse possible"

        Retoucher une photo numérique, c’est **modifier les valeurs de ses pixels** : c’est facile, et le résultat peut être invisible. Toute photo de smartphone est déjà transformée par des algorithmes (HDR, débruitage). La loi française n’impose pas de signaler toute retouche, mais celles qui **trompent dans un but commercial** : la silhouette dans la publicité (« Photographie retouchée », 2017), la silhouette ou le visage dans l’influence commerciale (« Image retouchée », 2023). La presse s’impose des règles plus strictes encore : on ne touche pas au contenu. Face à une image, l’esprit critique reste indispensable : d’où vient-elle, qui l’a publiée, dans quel but ?

??? corrige "Corrigé de l'activité"

    Notions du cours mobilisées

    - **Pixel**, codage **RVB** (trois nombres de 0 à 255), **définition** et **résolution**.

    - **Modifier une image par programme** (Python + PIL) : éclaircir, changer une couleur, c’est changer les valeurs des pixels.

    - **Algorithmes des appareils** : HDR, débruitage, accentuation, embellissement automatique.

    - **Une photo n’est plus une preuve** en soi : esprit critique (d’où vient l’image ? qui l’a publiée ?).

    - **Métadonnées EXIF** : le fichier peut garder la trace du logiciel, mais elles s’effacent.

    Arguments attendus

    <table>
    <thead>
    <tr>
    <th style="text-align: left;"><strong>POUR (oui) : toujours signaler</strong></th>
    <th style="text-align: left;"><strong>CONTRE (non) : pas d’obligation générale</strong></th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: left;"><ul>
    <li><p><strong>Santé publique</strong> : des corps impossibles à atteindre abîment l’image de soi (doc. 1).</p></li>
    <li><p><strong>Droit d’être informé</strong> : une retouche est souvent invisible, celui qui regarde doit savoir (cours).</p></li>
    <li><p><strong>La loi le fait déjà</strong> pour la publicité et l’influence commerciale ; il suffit d’aller plus loin (doc. 1 et 2).</p></li>
    <li><p><strong>Les filtres sont partout</strong> sur les réseaux, or la loi ne vise que l’influence commerciale : une photo personnelle retouchée échappe à toute mention (doc. 2). Les jeunes se comparent pourtant à ces images.</p></li>
    <li><p><strong>Confiance</strong> : la presse montre qu’on peut fixer une règle claire (doc. 4).</p></li>
    <li><p><strong>C’est techniquement simple</strong> : une mention, ou une trace dans les métadonnées (doc. 4).</p></li>
    </ul></td>
    <td style="text-align: left;"><ul>
    <li><p><strong>Toute photo est déjà calculée</strong> par le smartphone (doc. 3, cours) : où placer la limite ?</p></li>
    <li><p><strong>Mention inutile si elle est partout</strong> : on ne la lit plus (doc. 3).</p></li>
    <li><p><strong>Liberté artistique</strong> : la retouche fait partie du travail du photographe depuis toujours (doc. 3).</p></li>
    <li><p><strong>Impossible à contrôler</strong> pour des milliards de photos personnelles ; les métadonnées s’effacent (doc. 4).</p></li>
    <li><p><strong>Distinguer les cas</strong> : la loi vise déjà ce qui trompe dans un but commercial (silhouette, visage) (doc. 1 et 2).</p></li>
    <li><p><strong>Retouche légère <span class="math inline">≠</span> tromperie</strong> : corriger la lumière ne change pas ce que montre l’image (doc. 1 et 4).</p></li>
    </ul></td>
    </tr>
    </tbody>
    </table>

    *Arguments de l’autre camp souvent jugés solides dans la trace écrite :* un élève POUR retient souvent « une mention mise sur toutes les photos finirait par ne plus être lue » ; un élève CONTRE, « une silhouette affinée dans une publicité trompe vraiment celui qui regarde ».

    Questions de relance (pour le modérateur)

    1.  Éclaircir une photo et affiner une silhouette : est-ce la même chose ? (pensez aux pixels et à ce que montre l’image)

    2.  La retouche automatique du smartphone (doc. 3) doit-elle être signalée ?

    3.  Pourquoi la loi vise-t-elle la publicité et les influenceurs, et pas vos photos de vacances (doc. 1 et 2) ?

    4.  La règle de la presse (doc. 4) pourrait-elle s’appliquer aux réseaux sociaux ?

    !!! encadre "Synthèse possible"

        Retoucher une photo numérique, c’est **modifier les valeurs de ses pixels** : c’est facile, et le résultat peut être invisible. Toute photo de smartphone est déjà transformée par des algorithmes (HDR, débruitage). La loi française n’impose pas de signaler toute retouche, mais celles qui **trompent dans un but commercial** : la silhouette dans la publicité (« Photographie retouchée », 2017), la silhouette ou le visage dans l’influence commerciale (« Image retouchée », 2023). La presse s’impose des règles plus strictes encore : on ne touche pas au contenu. Face à une image, l’esprit critique reste indispensable : d’où vient-elle, qui l’a publiée, dans quel but ?

??? corrige "Corrigé de l'activité"

    Notions du cours mobilisées

    - **Pixel**, codage **RVB** (trois nombres de 0 à 255), **définition** et **résolution**.

    - **Modifier une image par programme** (Python + PIL) : éclaircir, changer une couleur, c’est changer les valeurs des pixels.

    - **Algorithmes des appareils** : HDR, débruitage, accentuation, embellissement automatique.

    - **Une photo n’est plus une preuve** en soi : esprit critique (d’où vient l’image ? qui l’a publiée ?).

    - **Métadonnées EXIF** : le fichier peut garder la trace du logiciel, mais elles s’effacent.

    Arguments attendus

    <table>
    <thead>
    <tr>
    <th style="text-align: left;"><strong>POUR (oui) : toujours signaler</strong></th>
    <th style="text-align: left;"><strong>CONTRE (non) : pas d’obligation générale</strong></th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: left;"><ul>
    <li><p><strong>Santé publique</strong> : des corps impossibles à atteindre abîment l’image de soi (doc. 1).</p></li>
    <li><p><strong>Droit d’être informé</strong> : une retouche est souvent invisible, celui qui regarde doit savoir (cours).</p></li>
    <li><p><strong>La loi le fait déjà</strong> pour la publicité et l’influence commerciale ; il suffit d’aller plus loin (doc. 1 et 2).</p></li>
    <li><p><strong>Les filtres sont partout</strong> sur les réseaux, or la loi ne vise que l’influence commerciale : une photo personnelle retouchée échappe à toute mention (doc. 2). Les jeunes se comparent pourtant à ces images.</p></li>
    <li><p><strong>Confiance</strong> : la presse montre qu’on peut fixer une règle claire (doc. 4).</p></li>
    <li><p><strong>C’est techniquement simple</strong> : une mention, ou une trace dans les métadonnées (doc. 4).</p></li>
    </ul></td>
    <td style="text-align: left;"><ul>
    <li><p><strong>Toute photo est déjà calculée</strong> par le smartphone (doc. 3, cours) : où placer la limite ?</p></li>
    <li><p><strong>Mention inutile si elle est partout</strong> : on ne la lit plus (doc. 3).</p></li>
    <li><p><strong>Liberté artistique</strong> : la retouche fait partie du travail du photographe depuis toujours (doc. 3).</p></li>
    <li><p><strong>Impossible à contrôler</strong> pour des milliards de photos personnelles ; les métadonnées s’effacent (doc. 4).</p></li>
    <li><p><strong>Distinguer les cas</strong> : la loi vise déjà ce qui trompe dans un but commercial (silhouette, visage) (doc. 1 et 2).</p></li>
    <li><p><strong>Retouche légère <span class="math inline">≠</span> tromperie</strong> : corriger la lumière ne change pas ce que montre l’image (doc. 1 et 4).</p></li>
    </ul></td>
    </tr>
    </tbody>
    </table>

    *Arguments de l’autre camp souvent jugés solides dans la trace écrite :* un élève POUR retient souvent « une mention mise sur toutes les photos finirait par ne plus être lue » ; un élève CONTRE, « une silhouette affinée dans une publicité trompe vraiment celui qui regarde ».

    Questions de relance (pour le modérateur)

    1.  Éclaircir une photo et affiner une silhouette : est-ce la même chose ? (pensez aux pixels et à ce que montre l’image)

    2.  La retouche automatique du smartphone (doc. 3) doit-elle être signalée ?

    3.  Pourquoi la loi vise-t-elle la publicité et les influenceurs, et pas vos photos de vacances (doc. 1 et 2) ?

    4.  La règle de la presse (doc. 4) pourrait-elle s’appliquer aux réseaux sociaux ?

    !!! encadre "Synthèse possible"

        Retoucher une photo numérique, c’est **modifier les valeurs de ses pixels** : c’est facile, et le résultat peut être invisible. Toute photo de smartphone est déjà transformée par des algorithmes (HDR, débruitage). La loi française n’impose pas de signaler toute retouche, mais celles qui **trompent dans un but commercial** : la silhouette dans la publicité (« Photographie retouchée », 2017), la silhouette ou le visage dans l’influence commerciale (« Image retouchée », 2023). La presse s’impose des règles plus strictes encore : on ne touche pas au contenu. Face à une image, l’esprit critique reste indispensable : d’où vient-elle, qui l’a publiée, dans quel but ?

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
            rouge = gris + 50
            if rouge > 255:                  # on ne depasse pas 255
                rouge = 255
            img.putpixel((x, y), (rouge, gris // 3, gris // 4))
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

0

## <span class="etiquette">Débat</span> Faut-il obliger à signaler toute photo retouchée, dans la publicité comme sur les réseaux sociaux ?

*retouche et transparence*

<p class="infos-activite">Durée : 50 min</p>

!!! consignes "Consignes"

    - En classe entière. Les rôles sont tirés au sort : vous défendrez peut-être une position qui n’est pas la vôtre, c’est un excellent entraînement.

    - Chaque argument s’appuie sur un **document** ci-dessous ou sur le **cours**. <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> Préparation sans IA ni recherche en ligne.

    - Avant de commencer, notez sur votre cahier votre position de départ : oui, non ou je ne sais pas.

**Rappel du cours.** Une image numérique est un tableau de **pixels**, chacun codé par trois nombres (**RVB**) : la modifier, c’est changer ces nombres, et quelques lignes de Python y suffisent. Les smartphones eux-mêmes retouchent chaque photo grâce à des **algorithmes** (HDR, débruitage, embellissement). Une retouche peut être invisible : une photo n’est donc plus une **preuve** en soi. Faut-il prévenir celui qui regarde ?

!!! encadre "Les deux camps"

    **Groupe POUR** — oui : toute photo retouchée diffusée en public (publicité, réseaux sociaux) doit être signalée.  
    **Groupe CONTRE** — non : une telle obligation générale serait inutile ou impossible ; on peut la limiter à certains cas.

Les documents

!!! encadre "Document 1 — La mention « Photographie retouchée » (2017)"

    Depuis le 1<sup>er</sup> octobre 2017, en France, les photographies à usage commercial (publicités, affiches, catalogues…) sur lesquelles la **silhouette** d’un mannequin a été modifiée par un logiciel, pour l’affiner ou l’épaissir, doivent porter la mention **« Photographie retouchée »**. L’annonceur qui l’oublie risque une amende de 37 500 €, pouvant aller jusqu’à 30 % des dépenses consacrées à la publicité. Le but affiché est la **santé publique** : limiter la diffusion d’images de corps impossibles à atteindre. Une retouche de la lumière, des couleurs ou de la peau n’est pas concernée.

    Source : code de la santé publique, article L2133-2 ; décret n° 2017-738 du 4 mai 2017.

!!! encadre "Document 2 — Les influenceurs aussi (2023)"

    La loi française du 9 juin 2023 sur l’influence commerciale a étendu l’obligation aux **influenceurs** : lorsqu’ils font la promotion d’un produit ou d’un service, leurs photos et vidéos doivent porter la mention **« Image retouchée »** si un procédé de traitement d’image a affiné ou épaissi leur silhouette ou modifié l’apparence de leur visage ; un filtre qui transforme le visage est concerné. En revanche, une photo personnelle publiée sans aucun partenariat commercial n’est soumise à aucune obligation.

    Source : loi n° 2023-451 du 9 juin 2023 visant à encadrer l’influence commerciale et à lutter contre les dérives des influenceurs sur les réseaux sociaux.

!!! encadre "Document 3 — Toute photo est déjà retouchée ?"

    Avant même que vous touchiez à une photo, votre smartphone l’a transformée : il combine plusieurs clichés (HDR), réduit le bruit, accentue les contours, parfois lisse la peau automatiquement. Les photographes, eux, ont toujours ajusté la lumière, le contraste ou le cadrage, déjà dans la chambre noire à l’époque de la pellicule. Pour beaucoup de photographes et d’artistes, imposer une mention sur toute image modifiée n’aurait pas de sens : il faudrait la mettre sur presque toutes les photos, et elle finirait par ne plus être lue. La vraie question serait alors : **à partir de quand une retouche trompe-t-elle** celui qui regarde ?

    Source : d’après le cours (« Les algorithmes dans nos appareils »).

!!! encadre "Document 4 — Photo de presse : interdit de toucher au contenu"

    Pour une photo de presse, l’enjeu est la **confiance**. Le grand concours international de photojournalisme World Press Photo interdit d’ajouter, de retirer ou de déplacer un élément de l’image ; seuls des réglages raisonnables de lumière, de contraste et de couleur sont admis, et les photographes sélectionnés doivent fournir leurs fichiers d’origine. Des photos sélectionnées ont déjà été disqualifiées pour avoir enfreint ces règles. Les **métadonnées EXIF** d’un fichier peuvent indiquer le logiciel utilisé pour le modifier… mais elles s’effacent facilement.

    Source : World Press Photo, règles d’inscription et code éthique du concours.

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

\newgeometry{inner=1.8cm,outer=1.6cm,top=2.2cm,bottom=1.9cm,headheight=16pt,headsep=0.5cm,footskip=0.9cm}

## Corrigé

??? corrige "Corrigé"

    0
