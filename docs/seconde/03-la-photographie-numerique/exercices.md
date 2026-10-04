# Exercices

<p class="sous-titre">La photographie numérique</p>

!!! consignes "Mode d’emploi"

    - Niveau : ★ échauffement, ★★ classique (niveau bac), ★★★ défi ; les *coups de pouce* et les *corrigés* se déplient sous chaque exercice.

    - <span class="tag">sur papier</span> *signale les exercices à faire sur papier* ; <span class="run" title="À programmer et tester sur machine">▶</span> *ceux où l’on écrit et teste un vrai programme* (Spyder ou Basthon, avec la bibliothèque PIL).

    - Rappel utile : une couleur $=$ trois nombres **RVB** entre $0$ et $255$ ; le pixel $(0,0)$ est en **haut à gauche**.

    - Usage de l’IA, indiqué sur chaque exercice : <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> aucune ; <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> en appui (déboguer, reformuler, vérifier ; la réponse finale est écrite et comprise par vous) ; <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> l’exercice s’appuie sur une réponse d’IA. Voir la charte d’usage de l’IA.

### Le capteur et la formation de l’image

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 1</span> — Vrai ou faux <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-03-1 }

<span class="tag">sur papier</span>  Répondre par **vrai** ou **faux**, et corriger les phrases fausses.

1.  Un photosite mesure une couleur et la transforme directement en trois nombres.

2.  Il y a autant de filtres rouges que de filtres verts sur un capteur.

3.  Sans filtre de couleur, un capteur donnerait une image en niveaux de gris.

4.  Plus un photosite reçoit de lumière, plus le nombre qu’il produit est grand.

??? corrige "Corrigé"

    **a. Faux.** Un photosite ne mesure qu’**une seule** composante (une quantité de lumière derrière *un* filtre rouge, vert *ou* bleu) ; les trois nombres RVB d’un pixel sont **reconstitués** ensuite à partir des photosites voisins (dématriçage).  
    **b. Faux.** Dans le filtre de **Bayer**, il y a **deux fois plus de filtres verts** que de rouges ou de bleus (l’œil humain est plus sensible au vert).  
    **c. Vrai.** Sans filtre coloré, chaque photosite ne mesurerait qu’une intensité lumineuse : on obtiendrait une image en **niveaux de gris**.  
    **d. Vrai.** Plus un photosite reçoit de lumière, plus la valeur numérique produite est **grande** (proche de $255$).

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 2</span> — Expliquer à un camarade <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-2 }

<span class="tag">sur papier</span>  En trois ou quatre lignes, expliquer comment un capteur fabrique une image. Employer les mots : *photosite*, *lumière*, *nombre*, *filtre de Bayer*.

??? corrige "Corrigé"

    *Exemple.* Le capteur est quadrillé de millions de **photosites**. Chaque photosite reçoit de la **lumière** à travers un petit **filtre de couleur** (rouge, vert ou bleu, disposés selon le **filtre de Bayer**) et la transforme en un **nombre** d’autant plus grand que la lumière est intense. L’appareil combine ensuite ces mesures voisines pour reconstituer, en chaque **pixel**, ses trois valeurs R, V et B.

### Le pixel et le codage RVB

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 3</span> — Nommer la couleur <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-03-3 }

<span class="tag">sur papier</span>  Donner la couleur obtenue par chacun des codes RVB suivants :

$(255,0,0)$ $(0,0,0)$ $(255,255,255)$ $(0,255,0)$ $(255,255,0)$ $(40,40,40)$.

??? corrige "Corrigé"

    $(255,0,0)$ : **rouge** ; $(0,0,0)$ : **noir** ; $(255,255,255)$ : **blanc** ; $(0,255,0)$ : **vert** ; $(255,255,0)$ : **jaune** (rouge $+$ vert) ; $(40,40,40)$ : un **gris foncé** (les trois canaux égaux et faibles).

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 4</span> — Coder une couleur <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-03-4 }

<span class="tag">sur papier</span>  Donner un code RVB plausible pour : du **noir**, du **blanc**, un **gris moyen**, du **jaune** (rouge + vert), du **violet** (rouge + bleu), un **rouge très sombre**.

??? corrige "Corrigé"

    *Exemples plausibles.* Noir $(0,0,0)$ ; blanc $(255,255,255)$ ; gris moyen $(128,128,128)$ ; jaune $(255,255,0)$ ; violet $(200,0,200)$ (rouge $+$ bleu) ; rouge très sombre $(80,0,0)$.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 5</span> — Combien de couleurs ? <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-03-5 }

<span class="tag">sur papier</span>  Chaque canal (R, V, B) prend une valeur entière de $0$ à $255$, soit $256$ possibilités.

1.  Combien de couleurs différentes peut-on coder en tout ? Donner le calcul.

2.  Combien de nuances de **gris** peut-on coder (les trois canaux égaux) ?

??? pouce "Coup de pouce"

    Pour chaque valeur du rouge, on peut choisir n’importe quelle valeur du vert, puis n’importe quelle valeur du bleu : les possibilités se multiplient. Pour un gris, une fois le rouge choisi, reste-t-il un choix pour le vert et le bleu ?

??? corrige "Corrigé"

    **1.** Chaque canal a $256$ valeurs, et il y a trois canaux indépendants : $$256 \times 256 \times 256 = 256^3 = \mathbf{16\,777\,216} \text{ couleurs} \quad (\approx 16{,}7 \text{ millions}).$$ **2.** Un gris a ses trois canaux **égaux** : il n’y a donc autant de gris que de valeurs communes possibles, soit **256** nuances (du noir au blanc).

### Définition, résolution et poids

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Compter les pixels <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-03-6 }

<span class="tag">sur papier</span>  Une image a pour définition $1920 \times 1080$.

1.  Combien de pixels contient-elle ? Donner un ordre de grandeur en millions.

2.  Calculer son **poids brut** (3 octets par pixel), en méga-octets ($1$ Mo $\approx 10^6$ octets).

??? pouce "Coup de pouce"

    Nombre de pixels $=$ largeur $\times$ hauteur. Poids brut $=$ nombre de pixels $\times 3$ octets ; divisez ensuite par $10^6$ pour obtenir des Mo.

??? corrige "Corrigé"

    **1.** $1920 \times 1080 = \mathbf{2\,073\,600}$ pixels, soit environ **2 millions** (2 mégapixels).  
    **2.** Poids brut $= 3 \text{ octets} \times 2\,073\,600 = 6\,220\,800$ octets $\approx \mathbf{6{,}2}$ **Mo**.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — Doubler la définition <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-03-7 }

<span class="tag">sur papier</span>  L’image A a pour définition $800 \times 600$ ; l’image B, la même scène photographiée en « double définition », mesure $1600 \times 1200$.

1.  Combien de pixels contient chaque image ?

2.  Combien de fois plus de pixels l’image B contient-elle ? Est-ce « deux fois plus » ?

3.  Calculer le poids brut de l’image B en Mo ($3$ octets par pixel).

??? pouce "Coup de pouce"

    Calculez le nombre de pixels de chaque image (largeur $\times$ hauteur) *avant* de comparer : la largeur double, mais la hauteur aussi.

??? corrige "Corrigé"

    **1.** Image A : $800 \times 600 = \mathbf{480\,000}$ pixels. Image B : $1600 \times 1200 = \mathbf{1\,920\,000}$ pixels.  
    **2.** $1\,920\,000 \div 480\,000 = \mathbf{4}$ : B contient **quatre fois** plus de pixels, et non deux. La largeur *et* la hauteur ont doublé : $2 \times 2 = 4$.  
    **3.** Poids brut de B $= 1\,920\,000 \times 3 = 5\,760\,000$ octets $\approx \mathbf{5{,}8}$ **Mo** (quatre fois le poids brut de A, $1{,}44$ Mo).

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — Résolution d’une impression <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-03-8 }

<span class="tag">sur papier</span>  On imprime une photo de définition $1500 \times 1000$ sur du papier de $12{,}7 \times 8{,}47$ cm.

1.  Convertir la largeur en **pouces** ($1$ pouce $=2{,}54$ cm).

2.  En déduire la **résolution** de l’impression en ppp. Le résultat convient-il pour une « belle » impression (environ $300$ ppp) ?

??? pouce "Coup de pouce"

    Largeur en pouces $=$ largeur en cm divisée par $2{,}54$. La résolution est un nombre de pixels *par pouce* : divisez le nombre de pixels de la largeur par la largeur en pouces.

??? corrige "Corrigé"

    **1.** $12{,}7~\text{cm} \div 2{,}54 = \mathbf{5}$ **pouces**.  
    **2.** Résolution $= \dfrac{1500 \text{ pixels}}{5 \text{ pouces}} = \mathbf{300}$ **ppp**. C’est exactement la valeur visée pour une « belle » impression : **le résultat convient**. *(En hauteur : $8{,}47~\text{cm} \approx 3{,}33$ pouces, et $1000 / 3{,}33 \approx 300$ ppp également.)*

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 9</span> — Imprimer en grand <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-03-9 }

<span class="tag">sur papier</span>  Un appareil photo donne des images de $4000 \times 3000$ pixels.

1.  Quelle est la plus grande taille d’impression (en cm) possible pour une « belle » impression à $300$ ppp ?

2.  On veut en faire une affiche de $60$ cm de large. Quelle sera la résolution de l’impression ? Est-ce une « belle » impression ? Pourquoi est-ce malgré tout acceptable pour une affiche ?

??? pouce "Coup de pouce"

    À $300$ ppp, chaque pouce imprimé utilise $300$ pixels : combien de pouces peut-on remplir avec les $4000$ pixels de la largeur ?

??? pouce "Coup de pouce 2 (début de solution)"

    Largeur : $4000 / 300 \approx 13{,}3$ pouces, à convertir en cm (multiplier par $2{,}54$). Faites de même pour la hauteur. Pour l’affiche, convertissez d’abord $60$ cm en pouces.

??? corrige "Corrigé"

    **1.** À $300$ ppp, chaque pouce imprimé utilise $300$ pixels. Largeur : $4000 \div 300 \approx 13{,}3$ pouces, soit $13{,}3 \times 2{,}54 \approx \mathbf{34}$ **cm**. Hauteur : $3000 \div 300 = 10$ pouces, soit $\mathbf{25{,}4}$ **cm**. La plus grande « belle » impression mesure donc environ $\mathbf{34 \times 25}$ **cm**.  
    **2.** $60$ cm $= 60 \div 2{,}54 \approx 23{,}6$ pouces, et $4000 \div 23{,}6 \approx \mathbf{170}$ **ppp**. C’est nettement moins que $300$ ppp : ce n’est pas une « belle » impression au sens strict. Mais une affiche se regarde **de loin** : à quelques mètres, l’œil ne distingue plus les pixels, et $170$ ppp suffisent largement.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 10</span> — Compression <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-10 }

<span class="tag">sur papier</span>  Une photo $4000 \times 3000$ pèse, en réalité, $4$ Mo sur la carte mémoire, alors que son poids « brut » est bien plus grand. Calculer le poids brut, puis expliquer d’où vient la différence.

??? pouce "Coup de pouce"

    Calculez le poids brut comme à l’exercice « Compter les pixels », puis comparez-le aux $4$ Mo. Quel traitement le format JPEG fait-il subir à l’image ?

??? corrige "Corrigé"

    Poids brut $= 4000 \times 3000 \times 3 = 36\,000\,000$ octets $= \mathbf{36}$ **Mo**. Sur la carte, la photo ne pèse que $4$ Mo, soit **9 fois moins** : c’est l’effet de la **compression** (format JPEG). Elle **supprime des détails peu perceptibles** par l’œil (compression *avec pertes*) pour réduire fortement la taille du fichier.

### Modifier une image par programme (PIL)

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 11</span> — Lire un pixel <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-11 }

<span class="run" title="À programmer et tester sur machine">▶</span>  À l’aide de l’image `terre.jpg`, écrire un programme qui affiche les trois canaux R, V, B du pixel de coordonnées $(120, 200)$.

??? pouce "Coup de pouce"

    Repartez du premier programme du cours : `Image.open`, puis `getpixel((x, y))`, qui renvoie les trois canaux du pixel.

??? corrige "Corrigé"

    ```python
    from PIL import Image
    img = Image.open("terre.jpg")
    r, v, b = img.getpixel((120, 200))
    print("Rouge :", r, " Vert :", v, " Bleu :", b)
    ```

    *`getpixel((x, y))` renvoie le triplet RVB du pixel ; on l’affiche.*

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 12</span> — Que fait ce programme ? <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-03-12 }

<span class="tag">sur papier</span>  On considère le programme suivant, appliqué à une image de $500 \times 500$ :

```python
from PIL import Image
img = Image.open("terre.jpg")
for y in range(500):
    for x in range(500):
        r, v, b = img.getpixel((x, y))
        img.putpixel((x, y), (0, v, b))
img.show()
```

1.  Que fait ce programme pour chaque pixel ?

2.  Quel sera l’effet visible sur l’image ? Justifier.

??? pouce "Coup de pouce"

    Comparez le triplet lu, `(r, v, b)`, et le triplet écrit : quel canal a changé, et quelle valeur prend-il ?

??? corrige "Corrigé"

    **1.** Pour chaque pixel, il lit ses valeurs $(r, v, b)$ puis les réécrit en **mettant le rouge à $0$** : $(0, v, b)$. Il **supprime la composante rouge** de toute l’image.  
    **2.** L’image perd tout son rouge : elle **tire vers le cyan** (bleu-vert). Sur `terre.jpg`, les tons chauds disparaissent et l’image paraît plus froide et bleutée.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 13</span> — Le négatif <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-13 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Écrire un programme qui transforme `terre.jpg` en son **négatif** : chaque canal $c$ est remplacé par $255-c$. Tester, puis afficher le résultat.

??? pouce "Coup de pouce"

    Reprenez le programme à deux boucles du cours (celui qui décale les canaux) : seule la ligne `putpixel` change.

??? corrige "Corrigé"

    On remplace chaque canal $c$ par $255 - c$.

    ```python
    from PIL import Image
    img = Image.open("terre.jpg")
    largeur, hauteur = img.size
    for y in range(hauteur):
        for x in range(largeur):
            r, v, b = img.getpixel((x, y))
            img.putpixel((x, y), (255 - r, 255 - v, 255 - b))
    img.show()
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 14</span> — Éclaircir l’image <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-14 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Écrire un programme qui **éclaircit** `terre.jpg` en ajoutant $60$ à chacun des trois canaux de chaque pixel. Attention, un canal ne peut pas dépasser $255$ : on écrira par exemple `min(255, r + 60)`, qui vaut le plus petit des deux nombres. Que deviennent les zones déjà très claires ?

??? pouce "Coup de pouce"

    Même structure que le négatif : seul le calcul de la nouvelle couleur change, canal par canal.

??? corrige "Corrigé"

    On ajoute $60$ à chaque canal, sans dépasser $255$ grâce à `min`.

    ```python
    from PIL import Image
    img = Image.open("terre.jpg")
    largeur, hauteur = img.size
    for y in range(hauteur):
        for x in range(largeur):
            r, v, b = img.getpixel((x, y))
            img.putpixel((x, y), (min(255, r + 60), min(255, v + 60), min(255, b + 60)))
    img.show()
    ```

    *Les zones déjà très claires (canaux proches de $255$) sont bloquées à $255$ : elles deviennent blanches et leurs détails disparaissent (on dit que l’image est « brûlée »). Le fond noir de l’espace, lui, devient gris foncé (par exemple $(5, 3, 6)$ devient $(65, 63, 66)$).*

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 15</span> — Niveaux de gris <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-15 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Écrire un programme qui rend l’image **grise** : remplacer R, V et B par leur moyenne $m = (r+v+b)\ //\ 3$. Vérifier qu’une image grise a bien ses trois canaux égaux.

??? pouce "Coup de pouce"

    Deux boucles, comme pour le négatif. Dans la boucle, calculez d’abord `m`, puis écrivez un pixel dont les trois canaux valent `m`.

??? pouce "Coup de pouce 2 (début de solution)"

    Dans les deux boucles :  
    `r, v, b = img.getpixel((x, y))`  
    `m = (r + v + b) // 3`  
    (il reste à écrire le pixel gris avec `putpixel`.)

??? corrige "Corrigé"

    On remplace R, V, B par leur moyenne $m$ ; les trois canaux deviennent égaux, donc le pixel est gris.

    ```python
    from PIL import Image
    img = Image.open("terre.jpg")
    largeur, hauteur = img.size
    for y in range(hauteur):
        for x in range(largeur):
            r, v, b = img.getpixel((x, y))
            m = (r + v + b) // 3
            img.putpixel((x, y), (m, m, m))
    img.show()
    ```

    *Vérification : après ce traitement, tout pixel vaut $(m, m, m)$ — ses trois canaux sont bien **égaux**, ce qui caractérise un gris.*

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 16</span> — Le miroir <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-16 }

<span class="run" title="À programmer et tester sur machine">▶</span>  Écrire un programme qui retourne `terre.jpg` comme dans un **miroir** : la colonne de gauche passe à droite, et inversement. On ne crée pas de nouvelle image : on **échange** les pixels deux à deux.

??? pouce "Coup de pouce"

    Le pixel de la colonne `x` échange sa place avec celui de la colonne `largeur - 1 - x`, sur la même ligne. Ne parcourez que la moitié gauche de l’image, sinon chaque échange serait aussitôt défait.

??? pouce "Coup de pouce 2 (début de solution)"

    `for y in range(hauteur):`  
    `for x in range(largeur // 2):`  
    `gauche = img.getpixel((x, y))`  
    `droite = img.getpixel((largeur - 1 - x, y))`

??? corrige "Corrigé"

    Sur chaque ligne, le pixel de la colonne `x` échange sa place avec celui de la colonne symétrique `largeur - 1 - x` (la colonne $0$ avec la dernière, la colonne $1$ avec l’avant-dernière, etc.). On ne parcourt que la **moitié gauche** : si l’on allait jusqu’au bout, chaque paire serait échangée deux fois et l’image reviendrait à l’identique.

    ```python
    from PIL import Image
    img = Image.open("terre.jpg")
    largeur, hauteur = img.size
    for y in range(hauteur):
        for x in range(largeur // 2):
            gauche = img.getpixel((x, y))
            droite = img.getpixel((largeur - 1 - x, y))
            img.putpixel((x, y), droite)                  # on echange
            img.putpixel((largeur - 1 - x, y), gauche)    # les deux pixels
    img.show()
    ```

    *Les deux valeurs sont lues **avant** d’écrire : si l’on écrivait d’abord à gauche, la couleur d’origine de ce pixel serait perdue.*

### Métadonnées et vie privée

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 17</span> — Les données cachées <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-17 }

<span class="tag">sur papier</span> 

1.  Qu’appelle-t-on les **métadonnées EXIF** d’une photo ? Citer trois informations qu’elles peuvent contenir.

2.  En quoi la présence de coordonnées **GPS** dans une photo publiée peut-elle poser un problème de vie privée ?

3.  Proposer une précaution simple avant de partager une photo prise au smartphone.

??? corrige "Corrigé"

    **1.** Les **métadonnées EXIF** sont des informations **enregistrées automatiquement** dans le fichier photo, en plus des pixels. Exemples : **date et heure** de la prise, **modèle d’appareil** (ou de smartphone), **réglages** (ouverture, temps de pose, ISO), et souvent les **coordonnées GPS**.  
    **2.** Si une photo publiée contient les **coordonnées GPS**, n’importe qui peut savoir **où** (et quand) elle a été prise : domicile, école, lieux fréquentés. C’est une atteinte à la **vie privée** et à la sécurité.  
    **3.** Précaution : **désactiver la géolocalisation** de l’appareil photo, ou **supprimer les métadonnées** (EXIF) de la photo avant de la partager.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 18</span> — Une photo est-elle une preuve ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-03-18 }

<span class="tag">sur papier</span>  « Puisque c’est une photo, c’est forcément vrai. » Discuter cette affirmation en une ou deux phrases (on pourra parler de retouche, de filtres et d’images générées par IA).

??? corrige "Corrigé"

    **Non**, pas à elle seule. Une image peut être **retouchée**, passée par des **filtres**, sortie de son contexte, ou entièrement **générée par une IA**. Une photo est un indice, pas une preuve absolue : il faut la **recouper** avec d’autres sources.

### Critiquer une réponse d’IA

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 19</span> — Poids et résolution selon un assistant <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> { #ex-03-19 }

<span class="tag">sur papier</span>  Un élève a demandé à un assistant d’IA : « Mon téléphone prend des photos de $6000 \times 4000$ pixels. Combien pèsent-elles, et puis-je les imprimer en $30 \times 20$ cm ? » Voici la réponse obtenue :

> Votre photo contient $6000 \times 4000 = 24\,000\,000$ pixels, soit 24 mégapixels. Chaque pixel est codé par trois nombres (rouge, vert, bleu) sur un octet chacun, donc 3 octets par pixel : le poids brut est $24\,000\,000 \times 3 = 72\,000\,000$ octets, soit 72 Mo. En pratique, le fichier JPEG est compressé et pèse plutôt 5 à 10 Mo. Pour l’impression, aucune inquiétude : sur une largeur de 30 cm, la résolution de votre photo est de 6000 ppp, bien au-dessus des 300 ppp recommandés.

1.  La réponse est-elle correcte ? Refaites chaque calcul (rappel : $1$ pouce $=2{,}54$ cm).

2.  Localiser l’erreur, nommer la notion confondue et donner la valeur juste.

    ??? pouce "Coup de pouce"

        Relisez la définition de la résolution dans le cours : en quelle unité s’exprime-t-elle ? Convertissez $30$ cm en pouces.

3.  Quelle vérification simple, faite *avant* de faire confiance à cette réponse, aurait suffi à détecter l’erreur ?

**Crédits.** Image `terre.jpg` : « The Blue Marble », NASA, équipage d’Apollo 17, 7 décembre 1972, domaine public.

??? corrige "Corrigé"

    **1.** Le début est juste : $6000 \times 4000 = 24\,000\,000$ pixels (24 Mpx), $3$ octets par pixel, donc $72\,000\,000$ octets $\approx 72$ Mo brut, réduits par la compression JPEG. En revanche, $30$ cm $= 30 / 2{,}54 \approx 11{,}8$ pouces, et $6000 / 11{,}8 \approx \mathbf{508}$ ppp, pas $6000$.  
    **2.** L’assistant a confondu la **définition** (le nombre de pixels : $6000$ en largeur) et la **résolution** (le nombre de pixels *par pouce*) ; le cours précise : « la résolution est le nombre de pixels par unité de longueur ». La valeur juste est environ $508$ ppp — la conclusion (impression de bonne qualité) reste vraie, mais le nombre est faux.  
    **3.** Un ordre de grandeur suffisait : $6000$ ppp sur $11{,}8$ pouces exigerait $6000 \times 11{,}8 \approx 71\,000$ pixels de large, six fois plus que la photo n’en possède. Dès qu’une réponse annonce une résolution, vérifier l’unité (pixels *par pouce*) et refaire la division.
