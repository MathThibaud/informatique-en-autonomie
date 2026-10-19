# Cours

<p class="sous-titre">La photographie numérique</p>

<span id="chap-03" class="ancre"></span>

|  |  |
|:---|:---|
| **Programme** | Du capteur au pixel ; codage des couleurs (RVB) ; définition, résolution et taille d’un fichier ; traitement d’image *par programme* ; métadonnées EXIF ; rôle des algorithmes dans les appareils. |
| **Idée** | Une photo numérique n’est qu’un immense tableau de **nombres**. Comprendre ces nombres, c’est pouvoir *lire*, *fabriquer* et *transformer* une image **soi-même**, avec quelques lignes de Python. |
| **Objectifs** | Expliquer comment un capteur forme une image ; coder une couleur en RVB ; calculer définition, résolution et poids ; modifier une image pixel par pixel ; lire les métadonnées et en mesurer l’enjeu pour la vie privée. |

!!! situation "Situation de départ"

    1.  Votre téléphone prend des photos de « 12 millions de pixels ». Qu’est-ce qu’un pixel, et pourquoi une photo pèse-t-elle plusieurs mégaoctets ?

    2.  Vous publiez une photo prise dans votre chambre. Un inconnu peut-il savoir où et quand elle a été prise, alors que rien ne se voit sur l’image ?

    3.  Comment une application met-elle votre photo en noir et blanc en une fraction de seconde ?

!!! curieux "Pour les curieux (facultatif) — Un peu d’histoire"

    La toute première photographie est prise vers **1826** par le Français **Nicéphore Niépce** (« Point de vue du Gras ») : il a fallu *plusieurs heures* de pose ! En **1888**, **George Eastman** lance l’appareil **Kodak** avec un slogan resté célèbre : « *Vous appuyez sur le bouton, nous faisons le reste.* » Mais la vraie révolution est de **1975** : l’ingénieur **Steven Sasson**, chez Kodak, construit le **premier appareil photo numérique**. Il pesait environ 3,6 kg, enregistrait sur une cassette en **23 secondes**… une image de $100 \times 100$ pixels en noir et blanc ! (IEEE, 2022) Aujourd’hui, le capteur qui tient dans votre téléphone compte plus de **mille fois** plus de pixels (souvent 12 millions ou davantage, contre 10 000), en couleurs.

    ![](../img/03_hist_niepce.jpg){ .photo loading=lazy style="width:100%" }  
    « Point de vue du Gras » (Niépce, vers 1826)

    ![](../img/03_hist_sasson.jpg){ .photo loading=lazy style="width:100%" }  
    Le premier appareil numérique (Sasson, 1975)

    Sources : Harry Ransom Center (université du Texas à Austin), qui conserve le « Point de vue du Gras » de Nicéphore Niépce (vers 1826–1827), `hrc.utexas.edu` ; George Eastman Museum (Rochester), histoire de l’appareil Kodak de 1888 et de son slogan ; IEEE, *Milestone* « Handheld Digital Camera, 1975 » (appareil de Steven Sasson : environ 3,6 kg, image de $100 \times 100$ pixels enregistrée en 23 s), inaugurée en 2022, `ethw.org`.

    [$\to$ frise chronologique](../methode-debattre.md#frise)

## De la lumière à l’image : le capteur

Autrefois, l’appareil photo contenait une **pellicule** : une surface sensible à la lumière, qu’il fallait ensuite développer chimiquement en laboratoire. Aujourd’hui, la pellicule est remplacée par un **capteur** électronique.

!!! definition "Définition 1"

    Un <span id="lex-capteurphoto03" class="ancre"></span>**capteur** est une surface couverte de millions de petites cellules, les <span id="lex-photosite03" class="ancre"></span>**photosites**. Chaque photosite mesure la **quantité de lumière** qu’il reçoit et la transforme en un **nombre** (c’est la *numérisation*) : plus il reçoit de lumière, plus le nombre est grand.

![](../img/03_capteur_cmos_sony_a7riii.jpg){ .photo loading=lazy style="width:306px" }

Le capteur d’un appareil photo hybride, démonté (un capteur « CMOS », du nom de la technologie de fabrication utilisée par presque tous les appareils actuels) : la surface rectangulaire centrale porte des dizaines de millions de photosites.

Seul, un photosite ne distingue pas les couleurs : on obtiendrait une image en **niveaux de gris**. Pour capter la couleur, on place devant les photosites un <span id="lex-bayer03" class="ancre"></span>**filtre de Bayer** : des petits filtres rouges, verts et bleus. Fait amusant, il y a **deux fois plus de filtres verts** que de rouges ou de bleus, car notre œil est plus sensible au vert.

![](../img/03_hist_capteur_macro.jpg){ .photo loading=lazy style="width:100%" }  
Un capteur vu de très près : la mosaïque du filtre coloré

![](../figures/3764d33196c1492a.svg){ .tikz loading=lazy }  
Filtre de Bayer : 1 photosite rouge, 1 bleu et *2 verts* par groupe de quatre.

!!! activite "Activité — Expliquer le capteur"

    Rédiger, en quelques lignes, un résumé qui explique à un camarade comment un capteur d’appareil photo fabrique une image (mots à réutiliser : *photosite*, *lumière*, *nombre*, *filtre de Bayer*).

<span id="cours-03-1" class="ancre"></span>

<span class="afaire">▶ Exercices d'application :</span> exercices **[1](exercices.md#ex-03-1) et [2](exercices.md#ex-03-2)** (le capteur et la formation de l’image)

## Le pixel et le codage des couleurs (RVB)

L’image finale est un quadrillage de points colorés : les **pixels** (de l’anglais *picture element*).

!!! definition "Définition 2"

    Chaque <span id="lex-pixel03" class="ancre"></span>**pixel** porte une couleur codée par **trois nombres** entre **0 et 255** : la quantité de **R**ouge, de **V**ert et de **B**leu (système **RVB**, ou *RGB* en anglais). Exemple : $(247,\ 56,\ 98)$. C’est la <span id="lex-rvb03" class="ancre"></span>**synthèse additive** : en mélangeant de la lumière rouge, verte et bleue, on obtient toutes les autres couleurs.

![](../figures/95de1664973d2705.svg){ .tikz loading=lazy }

!!! exemple "Exemple"

    Quelques couleurs utiles : rouge $=(255,0,0)$ vert $=(0,255,0)$ bleu $=(0,0,255)$ **noir** $=(0,0,0)$ **blanc** $=(255,255,255)$ jaune $=(255,255,0)$. Quand les trois canaux sont *égaux*, on obtient un **gris**.

![](../figures/075dfbdd050d5368.svg){ .tikz loading=lazy }  
La synthèse additive : rouge + vert $=$ jaune, les trois ensemble $=$ blanc.

!!! activite "Activité — Jouer avec les couleurs"

    1.  Avec 256 valeurs possibles par canal (de 0 à 255) et 3 canaux, calculer le nombre total de couleurs différentes.

    2.  Donner le code RVB pour obtenir : du **noir**, du **blanc**, du **jaune** (rouge + vert), du **violet** (rouge + bleu).

    3.  Que voit-on à l’écran avec le code $(125,125,125)$ ? Et avec $(30,30,30)$ ?

!!! projet "Projet — Dessiner des drapeaux avec Python"

    Maintenant que vous savez coder une couleur, vous allez **fabriquer** des images de zéro : des drapeaux (Monaco, France, puis d’autres), en respectant les **proportions** et les **couleurs officielles**.  
    $\to$ voir le projet *« Dessiner des drapeaux avec Python »*, en fin de chapitre.

<span id="cours-03-3" class="ancre"></span>

<span class="afaire">▶ Exercices d'application :</span> exercices **[3](exercices.md#ex-03-3) à [5](exercices.md#ex-03-5)** (le pixel et le codage RVB)

## Définition, résolution et poids d’une image

!!! definition "Définition 3"

    La <span id="lex-definition03" class="ancre"></span>**définition** d’une image est son nombre de pixels : largeur $\times$ hauteur. Une image $800 \times 600$ contient $800 \times 600 = 480\,000$ pixels.  
    La <span id="lex-resolution03" class="ancre"></span>**résolution** est le nombre de pixels par unité de longueur, souvent en **ppp** (pixels par pouce, ou *dpi*). Un pouce vaut $2{,}54$ cm. Plus la résolution est élevée, plus l’image est nette à l’impression.

!!! regle "Règle 1"

    Une image en couleurs « brute » stocke 3 nombres par pixel (R, V, B), chacun sur **1 octet** (un **octet** est la petite unité de mémoire qui permet de ranger un nombre entier de $0$ à $255$). <span id="lex-poids03" class="ancre"></span>Son **poids** vaut donc environ : $$\text{poids} = \text{largeur} \times \text{hauteur} \times 3 \ \text{octets}.$$ (Les formats comme le JPEG *compressent* ensuite l’image pour réduire ce poids.)

!!! activite "Activité — Calculer sur les images"

    1.  Une photo de définition $1200 \times 900$ est tirée au format $20 \times 15$ (en cm). Calculer sa résolution en ppp (rappel : $1$ pouce $=2{,}54$ cm).

    2.  Pour une belle impression, il faut environ $300$ ppp. Calculer la définition minimale d’une photo imprimée en $15 \times 10$ cm.

    3.  Calculer le poids « brut » d’une photo de définition $4000 \times 3000$ (en méga-octets ; $1$ Mo $\approx 10^{6}$ octets).

<span id="cours-03-6" class="ancre"></span>

<span class="afaire">▶ Exercices d'application :</span> exercices **[6](exercices.md#ex-03-6) à [10](exercices.md#ex-03-10)** (définition, résolution, poids)

## Modifier une image par programme (Python + PIL)

Une image étant un tableau de nombres, on peut la **transformer** avec un programme. On utilise la bibliothèque **PIL**. Chaque pixel est repéré par des coordonnées $(x, y)$ : $(0,0)$ est en **haut à gauche**.

![](../figures/44921f2c19c5fc9e.svg){ .tikz loading=lazy }  
Le pixel $(0,0)$ est en haut à gauche ; $x$ va vers la droite, $y$ vers le bas.

Les programmes de ce chapitre utilisent l’image `terre.jpg` ($500 \times 500$ pixels) : c’est la célèbre photo de la Terre « *The Blue Marble* » prise par l’équipage d’Apollo 17 en 1972, dans le domaine public. Elle est à télécharger ici : <https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/seconde/03-photo-image-terre> ; à défaut, n’importe quelle photo `.jpg` renommée `terre.jpg` convient. Elle doit être rangée dans le même dossier que le programme.

La ligne `from PIL import Image` charge l’outil `Image` de la bibliothèque **PIL**, un peu comme `import turtle as t` chargeait la tortue ; on écrit ensuite `Image.open(...)` pour ouvrir une image.

**Lire** un pixel avec `getpixel`, le **modifier** avec `putpixel` :

```python
from PIL import Image
img = Image.open("terre.jpg")        # l'image doit etre dans le meme dossier
img = img.convert("RGB")             # 3 canaux R, V, B (utile pour un PNG)

r, v, b = img.getpixel((100, 250))   # lire le pixel (100, 250)
print("rouge :", r, "vert :", v, "bleu :", b)

img.putpixel((250, 250), (255, 0, 0)) # colorier ce pixel en rouge
img.show()                            # afficher l'image
```

Pour parcourir *toute* l’image, on utilise **deux boucles `for`** imbriquées :

```python
from PIL import Image
img = Image.open("terre.jpg").convert("RGB")
largeur, hauteur = img.size          # taille de l'image, en pixels

for y in range(hauteur):
    for x in range(largeur):
        r, v, b = img.getpixel((x, y))
        img.putpixel((x, y), (v, b, r))   # on decale les canaux
img.show()
```

!!! activite "Activité — Ses premières retouches"

    Saisir et tester les programmes ci-dessus dans Spyder (ou Basthon), avec l’image `terre.jpg`. Puis :

    1.  Modifier le premier programme pour afficher les canaux du pixel $(250,300)$.

    2.  Expliquer, en une phrase, l’effet du programme à deux boucles (le décalage des canaux).

    3.  Après une petite recherche sur le **négatif** d’une image, écrire un programme qui *inverse* chaque canal (indice : remplacer $r$ par $255-r$, etc.).

    4.  Après une recherche sur les **niveaux de gris**, écrire un programme qui rend l’image grise (indice : remplacer R, V et B par leur *moyenne* $(r+v+b)//3$).

Avec un `if`, on peut ne modifier *que certains* pixels (par exemple selon leur position ou leur couleur) : c’est la base de la retouche « localisée ».

!!! projet "Projet — Retoucher un tableau célèbre"

    Vous appliquerez ces techniques à de vraies œuvres d’art (du domaine public) : changer la couleur du ciel de *La Nuit étoilée* de Van Gogh, ou celle d’un vêtement dans un portrait.  
    $\to$ voir le projet *« Retoucher un tableau célèbre en RVB »*, en fin de chapitre.

<span id="cours-03-11" class="ancre"></span>

<span class="afaire">▶ Exercices d'application :</span> exercices **[11](exercices.md#ex-03-11) à [16](exercices.md#ex-03-16)** (modifier une image en Python)

## Les métadonnées (EXIF) et la vie privée

Un fichier photo ne contient pas *que* l’image. Il embarque aussi des informations sur la prise de vue : ce sont les **métadonnées EXIF**.

!!! definition "Définition 4"

    Les <span id="lex-exif03" class="ancre"></span>**métadonnées EXIF** sont des données *cachées* rangées dans le fichier : date et heure, marque et modèle de l’appareil, réglages, définition… et, si l’appareil possède un GPS (tous les smartphones), les **coordonnées du lieu** de la prise de vue.

On peut les lire avec un petit programme Python :

```python
from PIL import Image, ExifTags
img = Image.open("photo.jpg")
print("definition :", img.size)              # (largeur, hauteur)
exif = img.getexif()                         # metadonnees : numero -> valeur
for numero in exif:
    nom = ExifTags.TAGS.get(numero, numero)  # nom lisible de la metadonnee
    print(nom, ":", exif[numero])
```

Ce programme s’utilise tel quel, sans chercher à en comprendre chaque ligne (la ligne `ExifTags.TAGS.get(...)` va chercher le nom de la métadonnée dans une table fournie par PIL). Pour le GPS, il n’affiche qu’un simple nombre (par exemple `GPSInfo : 70`) : les coordonnées sont rangées à part, dans un sous-dossier des métadonnées ; les logiciels de photo et les sites de lecture EXIF les affichent en clair, comme dans le tableau ci-dessous.

Chaque métadonnée est rangée sous un **numéro** (par exemple 271 pour le fabricant, 272 pour le modèle, 306 pour la date) ; `ExifTags.TAGS` donne le **nom** qui correspond à chaque numéro (`Make`, `Model`, `DateTime`…).

| **Métadonnée EXIF**              | **Valeur (exemple fictif)**    |
|:---------------------------------|:-------------------------------|
| Date et heure de la prise de vue | `2026:05:14 16:42:07`          |
| Fabricant / modèle               | Smartphone (modèle quelconque) |
| Définition                       | $4032 \times 3024$             |
| Temps de pose / sensibilité      | 1/120 s / ISO 100              |
| Latitude GPS                     | $43^\circ\,43'\,50''$ N        |
| Longitude GPS                    | $7^\circ\,25'\,31''$ E         |
| Altitude GPS                     | 12 m                           |

Extrait de métadonnées EXIF (valeurs fictives). En rouge : les coordonnées GPS, qui suffisent à situer la prise de vue sur une carte.

!!! regle "Règle 2"

    Publier une photo prise au smartphone peut **révéler sans le vouloir** où et quand elle a été prise (domicile, école…). Beaucoup de réseaux sociaux retirent l’EXIF à la publication, mais **pas tous** : dans le doute, on peut *effacer les métadonnées* avant de partager.

!!! activite "Activité — Enquêter sur une photo"

    1.  Sur une photo fournie par le professeur, retrouver à l’aide du programme : la **date** de prise de vue, le **fabricant** de l’appareil, la **définition**.

    2.  Expliquer en quoi la présence de coordonnées GPS dans une photo peut poser un **problème de vie privée**.

<span id="cours-03-17" class="ancre"></span>

<span class="afaire">▶ Exercices d'application :</span> exercices **[17](exercices.md#ex-03-17) et [18](exercices.md#ex-03-18)** (métadonnées EXIF et vie privée), exercice **[19](exercices.md#ex-03-19)** (critiquer une réponse d’IA)

## Les algorithmes dans nos appareils

La photo « parfaite » du smartphone n’est pas seulement captée : elle est **calculée**. Des algorithmes interviennent après la prise de vue :

- **mise au point** et **exposition** automatiques ;

- **HDR** : combinaison de plusieurs clichés pour équilibrer ombres et lumières ;

- **débruitage**, accentuation, **filtres** et embellissement automatique ;

- détection de visages, *portraits* avec flou d’arrière-plan.

!!! regle "Règle 3"

    Une image numérique est **facile à modifier** : une retouche peut être invisible. Une photo n’est donc plus une **preuve** en soi. Avec l’IA (images générées, *deepfakes*), il faut plus que jamais garder un **esprit critique** : d’où vient l’image ? qui l’a publiée ?

!!! curieux "Pour les curieux (facultatif) — Liens avec d’autres chapitres"

    - **Déjà vu :** une photo est un tableau de nombres, que l’on parcourt et modifie avec les **boucles** et les **conditions** du chapitre *Les bases de Python*.

    - **À venir :** les coordonnées des métadonnées viennent du récepteur **GPS** (chapitre *Localisation*), et le capteur d’image rejoindra les autres **capteurs** au chapitre *Informatique embarquée et objets connectés*.

    - **Plus loin :** chaque valeur de 0 à 255 tient sur un octet, soit 8 **bits** (des 0 et des 1) ; l’écriture binaire s’étudie en spécialité NSI de Première.

## Bilan — la carte mémoire

Les mots importants du thème sont définis dans le lexique.

| **Notion** | **À retenir** |
|:---|:---|
| Capteur / photosite | mesure la lumière $\to$ un nombre ; filtre de Bayer (2$\times$ plus de vert). |
| Pixel | un point de l’image, codé en **RVB** : 3 nombres de 0 à 255. |
| Synthèse additive | R + V + B $\to$ toutes les couleurs ; 3 canaux égaux $=$ gris. |
| Définition | nombre de pixels $=$ largeur $\times$ hauteur. |
| Résolution | pixels par pouce (ppp / dpi) ; $1$ pouce $=2{,}54$ cm. |
| Poids brut | largeur $\times$ hauteur $\times 3$ octets (le JPEG compresse). |
| Coordonnées | pixel $(x,y)$ ; $(0,0)$ en haut à gauche. |
| PIL | `getpixel` (lire), `putpixel` (écrire), 2 boucles `for` pour tout parcourir. |
| Négatif / gris | $255-c$ pour chaque canal ; moyenne $(r+v+b)//3$ pour le gris. |
| EXIF | métadonnées cachées (date, appareil, **GPS**) $\to$ enjeu de vie privée. |
| Algorithmes | HDR, filtres, retouche ; une photo n’est plus une preuve $\to$ esprit critique. |

!!! situation "Retour à la situation de départ"

    1.  Un **pixel** est un point de l’image, codé par 3 nombres **RVB** de 0 à 255 (§ II). À un octet par nombre, 12 millions de pixels (la **définition**) font environ 36 Mo « bruts », que le JPEG **compresse** en quelques Mo (§ III).

    2.  Oui, souvent : les **métadonnées EXIF** cachées dans le fichier donnent la date, l’appareil et, sur un smartphone, les **coordonnées GPS** du lieu (§ V). Tous les réseaux ne les retirent pas : dans le doute, on les efface avant de partager.

    3.  Une image est un tableau de nombres : un programme parcourt chaque pixel avec deux boucles `for` et remplace R, V et B par leur moyenne $(r+v+b)//3$ (§ IV) ; trois canaux égaux donnent un **gris** (§ II).

!!! encadre "Débat argumenté"

    Un **débat**, proposé en fin de chapitre, accompagne ce thème : « Faut-il obliger à signaler toute photo retouchée, dans la publicité comme sur les réseaux sociaux ? » (documents, rôles, tableau d’arguments et trace écrite, environ 50 min).

## Savoir-faire à maîtriser

*À la fin du chapitre, je sais…*

!!! autopos "Savoir-faire : je me positionne"

    - expliquer comment un **capteur** transforme la lumière en image numérique ;

    - décrire une image par ses **pixels** et coder une couleur en **RVB** (3 valeurs de 0 à 255) ;

    - distinguer **définition**, **résolution** et **poids** d’une image, et estimer un poids ;

    - modifier une image par un programme **Python** (parcourir et changer les pixels avec la bibliothèque PIL) ;

    - expliquer ce que sont les métadonnées **EXIF** et le risque qu’elles posent pour la vie privée ;

    - citer des traitements automatiques (algorithmes) réalisés par un appareil photo ou un smartphone.
