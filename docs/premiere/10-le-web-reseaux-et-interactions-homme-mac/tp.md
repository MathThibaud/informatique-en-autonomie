# TP et projets

<p class="sous-titre">Le Web : réseaux et interactions homme-machine</p>

## <span class="etiquette">TP</span> Mon premier site, pas à pas

*le site du Club Astro : structurer, mettre en forme, rendre interactif*

<p class="infos-activite">Durée : 2 h (une séance) · Seul, sur machine</p>

!!! fichiers "Fichiers à télécharger"

    [:material-folder-open: dossier en ligne](https://github.com/MathThibaud/nsi-fichiers-eleves/tree/main/premiere/10-tp-site-web-guide){ .md-button } [:material-zip-box: archive .zip](https://github.com/MathThibaud/nsi-fichiers-eleves/raw/main/zips/premiere-10-tp-site-web-guide.zip){ .md-button }

!!! encadre "But du TP"

    Construire, à partir d’un squelette fourni, le petit site du club d’astronomie du lycée : deux pages reliées par une barre de navigation, mises en forme par une feuille de style commune, puis rendues interactives en JavaScript (un compteur de « j’aime », une inscription qui vérifie ce qu’on a saisi, un mode nuit). Les trois parties suivent les trois premiers jalons du **projet « Créer un site web interactif »** : ce sont exactement les gestes que vous referez ensuite, seul, sur votre propre site.

!!! consignes "Consignes"

    - Fichiers à télécharger (lien ci-dessus) : le dossier `monsite/`, qui contient `index.html` (la page d’accueil), `style.css` (la feuille de style) et `script.js` (le programme JavaScript). Ne pas renommer ces fichiers.

    - Outils : un éditeur de texte (pas un traitement de texte) et un navigateur. Après chaque modification, **enregistrer** le fichier, puis **actualiser** la page dans le navigateur (touche `F5`).

    - Les commentaires `TODO` du squelette indiquent où écrire. Chaque partie commence par le rappel des outils utiles, avec le paragraphe du cours où les retrouver. Les réponses aux questions (sans <span class="run" title="À programmer et tester sur machine">▶</span> ) s’écrivent sur le cahier.

    - <span class="run" title="À programmer et tester sur machine">▶</span> *À écrire et tester dans le navigateur.* Niveau : ★ échauffement, ★★ classique (niveau bac), ★★★ défi ; les *coups de pouce* et les *corrigés* se déplient sous chaque exercice.

    - Usage de l’IA, indiqué sur chaque exercice : <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> aucune ; <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> en appui (déboguer, reformuler, vérifier ; la réponse finale est écrite et comprise par vous) ; <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> l’exercice s’appuie sur une réponse d’IA. Voir la [charte d’usage de l’IA](../charte.md).

## La structure HTML (jalon J1)

Environ 40 minutes. On écrit le **fond** de la page : les titres, les textes, la liste, le tableau et les liens.

!!! encadre "Outils de la partie 1 — les balises (cours, § V « HTML : structurer la page »)"

    - `<head>` contient les informations *sur* la page (`<title>`, le titre de l’onglet) ; `<body>` contient ce qui s’affiche.

    - `<h1>`, `<h2>` : titres ; `<p>` : paragraphe ; `<strong>` : texte important ; `<ul>` : liste à puces, dont chaque élément est un `<li>`.

    - `<a href="…">texte</a>` : lien hypertexte. Pour une page du même dossier, le nom du fichier suffit (`infos.html` : c’est un chemin **relatif**, comme au chapitre précédent) ; pour un autre site, on écrit l’adresse complète, qui commence par `https://`.

    - `<div>` : conteneur qui regroupe des éléments ; attributs `id="…"` (identifiant *unique* dans la page) et `class="…"` (étiquette *partagée*).

    - Tableau : `<table>` contient des lignes `<tr>` ; chaque ligne contient des cases `<th>` (case de titre) ou `<td>` (case ordinaire). Le squelette en donne un modèle.

    - `<!-- … -->` : commentaire, ignoré par le navigateur. Les consignes `TODO` du squelette en sont.

    Chaque balise ouverte se referme, et les balises s’emboîtent sans se croiser (sauf les balises auto-fermantes comme `<meta>`, `<link>`, `<input>`).

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 1</span> — Découvrir le squelette <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-tp-1-1 }

1.  Ouvrir `index.html` dans le navigateur (double-clic), puis dans l’éditeur de texte. Quels textes le navigateur affiche-t-il ? Pourquoi les lignes `TODO` n’apparaissent-elles pas ?

2.  Combien de blocs `<div class="carte">` la page contient-elle ? Pourquoi est-ce une `class` et pas un `id` ?

3.  Repérer le tableau du planning : combien de lignes compte-t-il pour l’instant ? Combien de cases par ligne ?

??? corrige "Corrigé"

    |  |  |
    |:---|:---|
    | **Ancrage BO (1re)** | réaliser et analyser une page HTML/CSS simple ; rôles de HTML, CSS et JavaScript ; événements et modification du document ; distinguer ce qui relève du client et du serveur. |
    | **Code** | une version possible parmi d’autres : les textes, les couleurs et la disposition sont libres, pourvu que les balises, les sélecteurs et les fonctions demandés y soient. |

    Le fichier `script.js` terminé, bonus compris :

    ```text
    // Programme JavaScript du Club Astro

    // Le bouton "J'aime" : ajoute 1 au nombre affiche
    function aimer() {
      let zone = document.querySelector("#nbJaime");
      let n = parseInt(zone.textContent);
      zone.textContent = n + 1;
    }

    // L'inscription : refuse un champ vide, puis un club complet
    function inscrire() {
      let champ = document.querySelector("#nom");
      let nom = champ.value;
      let reponse = document.querySelector("#reponse");
      let zonePlaces = document.querySelector("#places");
      let places = parseInt(zonePlaces.textContent);
      if (nom === "") {
        reponse.textContent = "Veuillez écrire votre nom.";
        reponse.style.color = "red";
      } else if (places === 0) {
        reponse.textContent = "Désolé " + nom + ", c'est complet !";
        reponse.style.color = "red";
      } else {
        zonePlaces.textContent = places - 1;
        reponse.textContent = "Merci " + nom + ", à vendredi !";
        reponse.style.color = "green";
        champ.value = "";
      }
    }

    // Le mode nuit : ajoute la classe nuit au body si elle est absente, la retire sinon
    function basculerNuit() {
      document.body.classList.toggle("nuit");
    }

    let boutonNuit = document.querySelector("#boutonNuit");
    boutonNuit.addEventListener("click", basculerNuit);   // sans les parentheses

    // Bonus : le compte a rebours, construit avec une boucle while
    function compteARebours() {
      let texte = "";
      let i = 10;
      while (i > 0) {
        texte = texte + i + "... ";
        i = i - 1;
      }
      texte = texte + "Décollage !";
      document.querySelector("#decollage").textContent = texte;
    }
    ```

    **1.** Le navigateur affiche les cinq sous-titres (« Qui sommes-nous ? », « Ce que l’on observe », « Le planning », « Vous aimez le club ? », « S’inscrire à la nuit d’observation ») et le début du tableau, sans aucune mise en forme ; l’onglet porte le titre « Mon site ». Les lignes `TODO` sont écrites entre `<!--` et `-->` : ce sont des **commentaires**, que le navigateur ignore. **2.** Cinq blocs. C’est une `class` parce que plusieurs balises portent la même étiquette, pour recevoir le même style ; un `id` doit être unique dans la page. **3.** Deux lignes (la ligne de titres et celle du lundi), de trois cases chacune.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 2</span> — Titres, annonce et présentation <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-tp-1-2 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

1.  Remplacer le titre de l’onglet `Mon site` par `Club Astro - Accueil`. Où ce titre s’affiche-t-il ?

2.  Écrire le titre principal `<h1>` « Club Astro ».

3.  Juste en dessous, écrire un paragraphe d’identifiant `annonce` qui contient : « Prochaine nuit d’observation : vendredi à 21 h, sur le toit du lycée. »

4.  Dans la carte « Qui sommes-nous ? », écrire un paragraphe de deux ou trois phrases qui présente le club ; mettre quelques mots en valeur avec `<strong>`.

5.  Dans la carte « Ce que l’on observe », écrire une liste à puces d’au moins trois objets du ciel.

??? corrige "Corrigé"

    ```text
    <title>Club Astro - Accueil</title>
    ...
    <h1>Club Astro</h1>

    <p id="annonce">Prochaine nuit d'observation : vendredi à 21 h, sur le toit du lycée.</p>
    ...
    <div class="carte">
      <h2>Qui sommes-nous ?</h2>
      <p>Le Club Astro réunit les élèves curieux du ciel. On y apprend à
         <strong>reconnaître les constellations</strong> et à se servir d'un télescope.</p>
    </div>

    <div class="carte">
      <h2>Ce que l'on observe</h2>
      <ul>
        <li>la Lune et ses cratères</li>
        <li>les planètes Jupiter et Saturne</li>
        <li>les étoiles filantes du mois d'août</li>
      </ul>
    </div>
    ```

    Le titre de l’onglet s’affiche dans l’**onglet** du navigateur (et dans les favoris ou l’historique), pas dans la page.

    <span class="erreurfreq">▷ Erreur fréquente.</span> écrire les éléments de la liste directement dans `<ul>`, sans `<li>` : ils s’affichent alors à la suite, sans puces.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 3</span> — Compléter le planning <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-tp-1-3 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Ajouter au tableau, sur le modèle de la ligne du lundi, une ligne « Mercredi, 14 h, Fabriquer une lunette » et une ligne « Vendredi, 21 h, Nuit d’observation ». Pourquoi la première ligne utilise-t-elle des `<th>` et les autres des `<td>` ?

??? corrige "Corrigé"

    ```text
    <tr>
      <td>Mercredi</td>
      <td>14 h</td>
      <td>Fabriquer une lunette</td>
    </tr>
    <tr>
      <td>Vendredi</td>
      <td>21 h</td>
      <td>Nuit d'observation</td>
    </tr>
    ```

    La première ligne contient les **titres des colonnes** : ses cases sont des `<th>`, que le navigateur affiche en gras et centrées. Les lignes suivantes contiennent les données, dans des cases ordinaires `<td>`.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 4</span> — La barre de navigation et une deuxième page <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-tp-1-4 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

1.  À l’endroit indiqué, sous l’annonce, écrire un bloc `<div class="barre">` qui contient trois liens : « Accueil » vers `index.html`, « Infos pratiques » vers `infos.html`, « En savoir plus » vers `https://fr.wikipedia.org/ wiki/ Astronomie`.

    ??? pouce "Coup de pouce"

        Reprendre la forme du lien de l’exemple du cours (§ V) : la destination entre les guillemets de `href`, le texte cliquable entre les deux balises.

2.  Lesquels de ces liens utilisent un chemin relatif ? Lequel une adresse complète ? Pourquoi le lien « Infos pratiques » ne mène-t-il encore nulle part ?

3.  Créer la page `infos.html` : dans l’éditeur, enregistrer une copie de `index.html` sous ce nom, **dans le même dossier**. Dans cette copie, changer le titre de l’onglet en `Club Astro - Infos pratiques` ; garder le `<h1>`, la barre et la ligne `<script …>` de la fin ; remplacer l’annonce et toutes les cartes par une seule carte « Infos pratiques » (lieu du rendez-vous, matériel à apporter).

4.  Vérifier qu’on passe d’une page à l’autre, dans les deux sens, avec la barre.

**Point d’étape  ✓** La page d’accueil affiche son titre, l’annonce, la barre, la présentation, la liste et un planning de quatre lignes ; la barre permet de passer d’une page à l’autre. C’est le jalon J1 du projet : des pages qui existent et sont reliées.

??? corrige "Corrigé"

    **1.**

    ```text
    <div class="barre">
      <a href="index.html">Accueil</a>
      <a href="infos.html">Infos pratiques</a>
      <a href="https://fr.wikipedia.org/wiki/Astronomie">En savoir plus</a>
    </div>
    ```

    **2.** `index.html` et `infos.html` sont des chemins **relatifs** : le navigateur cherche ces fichiers dans le dossier de la page affichée. Le lien vers Wikipédia est une adresse complète (protocole, nom de domaine, chemin). Tant que le fichier `infos.html` n’existe pas, le navigateur ne le trouve pas et affiche une page d’erreur (sur un serveur, ce serait l’erreur 404).

    **3.** Le fichier `infos.html` :

    ```text
    <!doctype html>
    <html lang="fr">
    <head>
      <meta charset="utf-8">
      <title>Club Astro - Infos pratiques</title>
    </head>
    <body>

      <h1>Club Astro</h1>

      <div class="barre">
        <a href="index.html">Accueil</a>
        <a href="infos.html">Infos pratiques</a>
        <a href="https://fr.wikipedia.org/wiki/Astronomie">En savoir plus</a>
      </div>

      <div class="carte">
        <h2>Infos pratiques</h2>
        <p>Rendez-vous en salle 204, puis sur le toit du lycée pour les observations.</p>
        <p>À apporter : une lampe rouge et des vêtements chauds.</p>
      </div>

      <script src="script.js"></script>
    </body>
    </html>
    ```

    <span class="erreurfreq">▷ Erreur fréquente.</span> enregistrer `infos.html` dans un autre dossier (Téléchargements, Bureau…) : le chemin relatif `infos.html` ne le trouve plus. Autre erreur : écrire le lien externe sans `https://` ; le navigateur cherche alors un fichier `fr.wikipedia.org` dans le dossier du site.

## La mise en forme CSS (jalon J2)

Environ 35 minutes. On écrit maintenant la **forme**, dans un fichier à part : le HTML ne change presque plus.

!!! encadre "Outils de la partie 2 — les règles CSS (cours, § VI « CSS : mettre en forme »)"

    - Relier la feuille de style : `<link rel="stylesheet" href="style.css">`, dans le `<head>` de **chaque** page.

    - Une règle : `sélecteur { propriété: valeur; }`. Trois sélecteurs : par nom de balise (`h1`), par classe (`.barre`), par identifiant (`#annonce`).

    - Propriétés : `color`, `background-color`, `font-family`, `font-size`, `text-align`, `margin` (marge extérieure), `padding` (marge intérieure), `border` (par exemple `1px solid gray`). Tailles en `px` ; couleurs par leur nom anglais (`gold`, `white`, `midnightblue`, `aliceblue`…).

    - Flexbox (§ VI A) : `display: flex` sur le **conteneur** aligne ses enfants en ligne ; `gap` règle l’espace entre eux, `justify-content` leur répartition horizontale, `align-items` leur alignement vertical.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 5</span> — Relier la feuille de style <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-tp-1-5 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

1.  Ouvrir `style.css`. Une règle y est fournie comme modèle :

    ```text
    .carte {
      border: 2px solid gray;
      padding: 10px 20px;
      margin-bottom: 15px;
    }
    ```

    Quelles balises vise-t-elle ? Que fait chacune de ses trois propriétés ?

2.  Relier `style.css` à `index.html`, à l’endroit indiqué. Actualiser : qu’est-ce qui change ?

3.  Relier aussi `style.css` à `infos.html`. Quel est l’intérêt d’une seule feuille de style pour tout le site ?

??? corrige "Corrigé"

    **1.** La règle vise toutes les balises de classe `carte` (les cinq blocs de la page d’accueil). `border` les entoure d’un trait gris continu de 2 pixels ; `padding` laisse une marge *intérieure* entre ce trait et le contenu (avec deux valeurs : 10 pixels en haut et en bas, 20 à gauche et à droite) ; `margin-bottom` laisse une marge *extérieure* de 15 pixels sous chaque carte.

    **2.** Dans le `<head>`, à la place du commentaire :

    ```text
    <link rel="stylesheet" href="style.css">
    ```

    Après actualisation, les cartes sont encadrées et espacées : la règle `.carte` s’applique.

    **3.** Même ligne dans le `<head>` de `infos.html`. Une seule feuille pour tout le site : on écrit chaque règle une fois, toutes les pages ont la même apparence, et une modification du style s’applique partout d’un coup. C’est la séparation du fond (les pages HTML) et de la forme (la feuille CSS).

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Mettre en forme la page <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-tp-1-6 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Dans `style.css`, à la place des commentaires `TODO J2`, écrire les règles suivantes. Actualiser après chacune pour en voir l’effet.

1.  Pour `body` : une police sans empattement (`sans-serif`), une couleur de fond claire, une marge de `20px`.

    ??? pouce "Coup de pouce"

        Chaque règle a la forme de la règle `.carte` fournie : le sélecteur, puis, entre accolades, une propriété par ligne, terminée par un point-virgule. Le premier sélecteur s’écrit simplement `body`.

2.  Pour `h1` : une couleur de texte, et le texte centré.

3.  Pour l’annonce : un fond doré, le texte centré, une marge intérieure de `8px`. Pourquoi faut-il ici un `#` et non un point ?

4.  Pour `th` : un fond foncé et un texte blanc ; pour `td` : une bordure fine et une marge intérieure de `5px`.

5.  Changer la couleur de fond dans la règle de `body`, puis ouvrir `infos.html`. Que constate-t-on ?

??? corrige "Corrigé"

    ```text
    body {
      font-family: sans-serif;
      background-color: aliceblue;
      margin: 20px;
    }

    h1 {
      color: royalblue;
      text-align: center;
    }

    #annonce {
      background-color: gold;
      color: black;
      text-align: center;
      padding: 8px;
    }

    th {
      background-color: midnightblue;
      color: white;
      padding: 5px;
    }

    td {
      border: 1px solid gray;
      padding: 5px;
    }
    ```

    **3.** `annonce` est un **identifiant** (`id="annonce"`) : le sélecteur commence par `#`. Le point est réservé aux classes. (La ligne `color: black;` garde l’annonce lisible en mode nuit, à l’exercice 10.) **5.** Le fond change aussi sur `infos.html` : les deux pages utilisent le même fichier `style.css`.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 7</span> — La barre de navigation avec Flexbox <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-tp-1-7 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

1.  Écrire la règle de la classe `barre` : ses liens en ligne, séparés de `10px`, sur un fond foncé, avec une marge intérieure de `10px`.

    ??? pouce "Coup de pouce"

        Revoir l’exemple `.barre` du cours (§ VI A) : `display: flex` et `gap` s’écrivent dans la règle du conteneur, pas dans celle des liens.

2.  Essayer successivement `justify-content: center`, puis `space-between`, puis `flex-end`. Décrire l’effet de chacune, et garder celle que vous préférez.

3.  Les liens bleus se lisent mal sur un fond foncé : écrire une règle qui met **tous** les liens en blanc. Quel sélecteur faut-il ?

**Point d’étape  ✓** Les deux pages utilisent le même `style.css`, la barre est en ligne, et vous avez écrit les trois sortes de sélecteurs : balise, classe, identifiant. C’est le jalon J2 du projet : le style s’applique, le fond et la forme sont séparés.

??? corrige "Corrigé"

    ```text
    .barre {
      display: flex;
      gap: 10px;
      justify-content: space-between;
      align-items: center;
      background-color: midnightblue;
      padding: 10px;
      margin-bottom: 15px;
    }

    a {
      color: white;
    }
    ```

    **2.** `center` regroupe les liens au milieu de la barre ; `space-between` place le premier à gauche, le dernier à droite, et répartit l’espace restant entre eux ; `flex-end` les regroupe à droite. **3.** Le sélecteur par nom de balise `a` vise tous les liens (ici, ce sont tous ceux de la barre).

    <span class="erreurfreq">▷ Erreur fréquente.</span> écrire `display: flex` dans la règle des liens `a` : ce sont les *enfants* ; c’est leur conteneur, `.barre`, qui doit devenir flexible.

## Les interactions JavaScript (jalon J3)

Environ 45 minutes. On écrit enfin le **comportement**, dans `script.js`. La ligne `<script src="script.js"></script>` est déjà à la fin du `<body>` : le programme est chargé après les balises qu’il utilise.

!!! encadre "Outils de la partie 3 — JavaScript (cours, § VII « JavaScript : rendre la page interactive »)"

    - Une fonction : `function aimer() { … }` ; une variable : `let n = 0;` ; chaque instruction finit par `;` et un commentaire commence par `//`.

    - Réagir à un clic : attribut `onclick="aimer()"` sur le bouton, ou, depuis le JavaScript, `bouton.addEventListener("click", aimer);` (sans parenthèses après `aimer`).

    - Sélectionner un élément : `document.querySelector("#nbJaime")` (ou `document. getElementById("nbJaime")`) ; le `<body>` s’obtient directement par `document.body`.

    - Modifier : `.textContent` (le contenu), `.style.color` (la couleur du texte), `.classList.toggle("nuit")` (ajoute la classe si elle est absente, la retire sinon), `.value` (le texte d’un champ). `parseInt(texte)` convertit un texte en entier (exercice 18 de la feuille).

    - `"Merci " + nom` colle deux textes ; un nombre collé à un texte devient du texte.

    - Si rien ne se passe : touche `F12`, onglet **Console** ; le message d’erreur indique le fichier et la ligne.

    La condition s’écrit comme en Python, avec des parenthèses autour du test et des accolades autour de chaque bloc ; on compare avec `===` (égal), `!==` (différent), `<`, `<=`, `>`, `>=`.

    ```text
    if (nom === "") {
        ...
    } else if (places === 0) {
        ...
    } else {
        ...
    }
    ```

    ```python
    if nom == "":
        ...
    elif places == 0:
        ...
    else:
        ...
    ```

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 8</span> — Le bouton « J’aime » <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-tp-1-8 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

1.  Dans la carte « Vous aimez le club ? », écrire un bouton « J’aime » qui appelle `aimer()` au clic, puis le paragraphe :

    ```text
    <p>Nombre de j'aime : <span id="nbJaime">0</span></p>
    ```

2.  Dans `script.js`, écrire la fonction `aimer()` : sélectionner le `<span>`, lire le nombre affiché, lui ajouter 1, réécrire le résultat.

    ??? pouce "Coup de pouce"

        C’est l’exercice 18 de la feuille : trois étapes, lire, ajouter 1, réécrire. Le texte lu est une chaîne : `parseInt` la transforme en entier.

3.  Dans `style.css`, écrire une règle qui affiche ce nombre en plus grand (`font-size`).

4.  Cliquer cinq fois, puis actualiser la page. Que devient le compteur ? Expliquer pourquoi.

??? corrige "Corrigé"

    Dans `index.html` :

    ```text
    <div class="carte">
      <h2>Vous aimez le club ?</h2>
      <button onclick="aimer()">J'aime</button>
      <p>Nombre de j'aime : <span id="nbJaime">0</span></p>
    </div>
    ```

    Dans `script.js` et dans `style.css` :

    ```text
    function aimer() {
      let zone = document.querySelector("#nbJaime");
      let n = parseInt(zone.textContent);
      zone.textContent = n + 1;
    }
    ```

    ```text
    #nbJaime {
      font-size: 24px;
    }
    ```

    **4.** Le compteur revient à 0 : actualiser recharge le fichier `index.html`, où le `<span>` contient 0. Le JavaScript n’a modifié que la page affichée, dans la mémoire du navigateur (le DOM) : rien n’a été enregistré, ni dans le fichier, ni sur un serveur.

    <span class="erreurfreq">▷ Erreur fréquente.</span> oublier `parseInt` : `zone.textContent` est une chaîne, et `"0" + 1` vaut `"01"`, puis `"011"`… Le compteur colle des 1 au lieu de compter.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 9</span> — Valider l’inscription <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-tp-1-9 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

1.  Dans la carte « S’inscrire à la nuit d’observation », écrire, dans cet ordre : un paragraphe « Places restantes : » suivi de `<span id="places">3</span>` ; un champ de texte d’identifiant `nom` ; un bouton « S’inscrire » qui appelle `inscrire()` au clic ; un paragraphe vide d’identifiant `reponse`.

    ??? pouce "Coup de pouce"

        L’exemple « Réagir à une saisie » du cours (§ VII B) contient déjà un champ, un bouton et un paragraphe vide.

2.  Écrire la fonction `inscrire()` : si le champ est vide, afficher en rouge, dans le paragraphe `reponse`, « Veuillez écrire votre nom. » ; sinon, afficher en vert un message qui reprend le nom saisi, par exemple « Merci Léa, à vendredi ! ». Tester les deux cas.

    ??? pouce "Coup de pouce"

        Lire le champ avec `.value` dans une variable `nom`, puis tester si elle est égale à la chaîne vide `""`. La couleur se règle avec `reponse.style.color = "red";`.

3.  Le club n’a que trois places. Améliorer `inscrire()` : à chaque inscription acceptée, le nombre de places affiché diminue de 1 ; quand il vaut 0, la fonction affiche en rouge « Désolé Tom, c’est complet ! » (avec le nom saisi) au lieu d’inscrire. Tester avec quatre inscriptions de suite.

    ??? pouce "Coup de pouce 2 (début de solution)"

        `let zonePlaces = document.querySelector("#places");`  
        `let places = parseInt(zonePlaces.textContent);`  
        `if (nom === "") { … }`  
        `else if (places === 0) { … }`  
        `else { zonePlaces.textContent = places - 1; … }`

4.  Après une inscription acceptée, vider le champ (comme dans la page complète de la fin du § VII).

5.  Un visiteur peut-il contourner cette limite de trois places ? Où faudrait-il faire la vérification pour qu’elle soit sûre ?

??? corrige "Corrigé"

    **1.**

    ```text
    <div class="carte">
      <h2>S'inscrire à la nuit d'observation</h2>
      <p>Places restantes : <span id="places">3</span></p>
      <input type="text" id="nom" placeholder="Votre nom">
      <button onclick="inscrire()">S'inscrire</button>
      <p id="reponse"></p>
    </div>
    ```

    **2.** Première version, sans les places :

    ```text
    function inscrire() {
      let nom = document.querySelector("#nom").value;
      let reponse = document.querySelector("#reponse");
      if (nom === "") {
        reponse.textContent = "Veuillez écrire votre nom.";
        reponse.style.color = "red";
      } else {
        reponse.textContent = "Merci " + nom + ", à vendredi !";
        reponse.style.color = "green";
      }
    }
    ```

    **3.** et **4.** Version finale. Avec Léa, Hugo, Inès puis Tom, les trois premiers sont inscrits (les places passent à 2, 1, 0) et Tom reçoit « Désolé Tom, c’est complet ! » ; un clic avec le champ vide donne toujours « Veuillez écrire votre nom. ».

    ```text
    function inscrire() {
      let champ = document.querySelector("#nom");
      let nom = champ.value;
      let reponse = document.querySelector("#reponse");
      let zonePlaces = document.querySelector("#places");
      let places = parseInt(zonePlaces.textContent);
      if (nom === "") {
        reponse.textContent = "Veuillez écrire votre nom.";
        reponse.style.color = "red";
      } else if (places === 0) {
        reponse.textContent = "Désolé " + nom + ", c'est complet !";
        reponse.style.color = "red";
      } else {
        zonePlaces.textContent = places - 1;
        reponse.textContent = "Merci " + nom + ", à vendredi !";
        reponse.style.color = "green";
        champ.value = "";
      }
    }
    ```

    **5.** Oui : il suffit d’actualiser la page pour retrouver 3 places, et les outils de développement (`F12`) permettent de modifier la page ou le programme. Cette vérification se fait **côté client**, sur la machine de l’utilisateur, qui la contrôle. Pour qu’elle soit sûre, il faut la faire **côté serveur** : c’est le serveur qui compterait les inscriptions reçues et refuserait la quatrième.

    <span class="erreurfreq">▷ Erreur fréquente.</span> écrire `if (nom = "")`, avec un seul `=` : c’est une affectation, pas une comparaison. La variable `nom` reçoit la chaîne vide, la condition est toujours fausse, et la page répond « Merci , à vendredi ! », sans le nom.

    <span class="erreurfreq">▷ Erreur fréquente.</span> oublier `parseInt` pour les places : `"0" === 0` est faux (une chaîne n’est pas un nombre) : le club n’est jamais complet, et les places affichées deviennent négatives.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 10</span> — Le mode nuit <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-tp-1-10 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

Les astronomes s’éclairent en rouge : cette lumière n’éblouit pas des yeux habitués à l’obscurité. On ajoute au site un mode nuit, fond noir et texte rouge.

1.  Dans `style.css`, écrire une règle pour la classe `nuit` : fond noir, texte rouge (`red`, ou `tomato`, plus doux).

2.  Dans la barre, **sur les deux pages**, ajouter le bouton `<button id="boutonNuit">Mode nuit</button>`, sans attribut `onclick`.

3.  Dans `script.js`, écrire une fonction `basculerNuit()` qui ajoute la classe `nuit` au `<body>` si elle est absente, et la retire sinon. Puis, en dehors de toute fonction, brancher le bouton `boutonNuit` sur cette fonction avec `addEventListener`.

    ??? pouce "Coup de pouce"

        L’exercice 20 de la feuille fait la même chose avec une classe `sombre`. Pour le branchement, revoir la remarque « Deux manières de brancher un événement » du cours (§ VII A).

4.  Passer en mode nuit, puis cliquer sur « Infos pratiques ». Le mode nuit est-il conservé ? Quel mécanisme du cours permet à un site de retenir une préférence d’une page à l’autre ?

**Point d’étape  ✓** Le compteur avance, l’inscription refuse un champ vide puis un club complet, le mode nuit fonctionne sur les deux pages. Votre fonction `inscrire` lit une saisie, utilise des variables et une condition, et modifie la page : c’est la « fonction algorithmique » demandée par le projet. C’est le jalon J3.

!!! encadre "Outil du bonus — la boucle while en JavaScript"

    Comme en Python, avec des parenthèses autour de la condition et des accolades autour du bloc répété :

    ```text
    let i = 10;
    while (i > 0) {
        ...
        i = i - 1;
    }
    ```

    ```python
    i = 10
    while i > 0:
        ...
        i = i - 1
    ```

??? corrige "Corrigé"

    Dans `style.css`, puis dans la barre de **chaque** page :

    ```text
    .nuit {
      background-color: black;
      color: tomato;
    }
    ```

    ```text
    <button id="boutonNuit">Mode nuit</button>
    ```

    Dans `script.js` :

    ```text
    function basculerNuit() {
      document.body.classList.toggle("nuit");
    }

    let boutonNuit = document.querySelector("#boutonNuit");
    boutonNuit.addEventListener("click", basculerNuit);   // sans les parentheses
    ```

    Le sélecteur de classe `.nuit` l’emporte sur le sélecteur de balise `body`, plus général : le fond devient noir même si la règle `body` en fixe un autre.

    **4.** Non : chaque page est chargée à nouveau, et la classe ajoutée au `<body>` de l’accueil n’existe pas dans `infos.html`. Pour s’en souvenir, le site pourrait faire retenir la préférence par le navigateur dans un **cookie** (cours, § VIII), comme on retient une langue.

    <span class="erreurfreq">▷ Erreur fréquente.</span> écrire `addEventListener("click", basculerNuit())`, avec des parenthèses : la fonction est exécutée une fois, tout de suite, au chargement (la page s’ouvre donc en mode nuit), et le clic ne fait plus rien.

    <span class="erreurfreq">▷ Erreur fréquente.</span> oublier le bouton dans la barre de `infos.html` : sur cette page, `querySelector` ne trouve aucune balise d’identifiant `boutonNuit` et renvoie `null` ; la console affiche une erreur sur la ligne de `addEventListener`.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 11</span> — Bonus : le compte à rebours <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-le-web-reseaux-et-interactions-homme-mac-tp-1-11 }

<span class="run" title="À programmer et tester sur machine">▶</span> 

1.  Ajouter à la page d’accueil une carte « Le décollage » avec un bouton « Lancer le compte à rebours » et un paragraphe vide d’identifiant `decollage`.

2.  Écrire une fonction `compteARebours()` qui construit, avec une boucle `while`, le texte `10... 9... 8... 7... 6... 5... 4... 3... 2... 1... Décollage !`, puis l’affiche dans le paragraphe.

    ??? pouce "Coup de pouce"

        Partir d’une variable `texte` qui vaut la chaîne vide `""` ; à chaque tour, lui coller le nombre suivi de `"... "` ; après la boucle, lui coller `"Décollage !"`.

3.  Le texte apparaît d’un seul coup, et non seconde après seconde. Pourquoi ?

??? corrige "Corrigé"

    ```text
    <div class="carte">
      <h2>Le décollage</h2>
      <button onclick="compteARebours()">Lancer le compte à rebours</button>
      <p id="decollage"></p>
    </div>
    ```

    ```text
    function compteARebours() {
      let texte = "";
      let i = 10;
      while (i > 0) {
        texte = texte + i + "... ";
        i = i - 1;
      }
      texte = texte + "Décollage !";
      document.querySelector("#decollage").textContent = texte;
    }
    ```

    Le paragraphe affiche `10... 9... 8... 7... 6... 5... 4... 3... 2... 1... Décollage !`. La boucle s’exécute en une fraction de milliseconde, et la page n’est affichée à nouveau qu’une fois la fonction terminée : tout apparaît d’un coup. Pour montrer un nombre par seconde, il faudrait programmer une attente entre deux étapes, ce qui dépasse le programme.

## Vers le projet

- Ce site n’est qu’un exemple : dans le projet, le thème, les pages et les interactions sont les vôtres. Vous pouvez repartir de ce dossier, en le réorganisant selon l’**arborescence imposée** : la feuille de style va dans `styles/`, le programme dans `scripts/`, les autres pages dans `contenus/`. Les chemins changent alors : depuis `index.html`, on écrit `styles/style.css` ; depuis une page de `contenus/`, `../styles/style.css` (on remonte d’un cran avec `..`, comme dans le terminal).

- Le projet demande aussi des images (`<img src="…" alt="…">`, cours § V), un formulaire avec un attribut `method` (cours § VIII, jalon J4) et au moins quatre interactions : ce TP en compte déjà trois.

## <span class="etiquette">Projet</span> Créer un site web interactif

!!! remarque "Remarque — De quoi s’agit-il ?"

    Vous allez concevoir, **seul**, un petit site web **interactif** en HTML, CSS et JavaScript, sur le thème de votre choix. Ce projet est le **couronnement** du chapitre sur le Web : il réunit tout ce que vous avez appris (structure, mise en forme, interactions, formulaire).  
    **Ce qui est noté n’est pas seulement le site fini**, mais surtout ce que *vous* savez faire et expliquer : votre **soutenance orale**, un **contrôle individuel sur machine**, et votre **carnet de bord**. Lisez bien la partie « Comment vous serez évalué ».

## Le cahier des charges

**Outils :** un simple **éditeur de texte** (et un navigateur pour tester). **Pas de framework** (React, Bootstrap…), pas de générateur de site : uniquement du **HTML, CSS et JavaScript** écrits par vous.

Votre site doit comporter :

- **3 à 4 pages** reliées par une **navigation claire** (un menu présent sur chaque page) ;

- des **liens hypertextes**, avec au moins un **chemin absolu** et un **chemin relatif** ;

- des **images** (libres de droit, sources citées) et au moins un **tableau** ;

- une **feuille de style CSS séparée** : le fond (HTML) et la forme (CSS) dans des fichiers distincts ;

- au moins **quatre interactions JavaScript** réagissant à des **événements** (clic, survol…) et modifiant la page (le DOM) ;

- **au moins une fonction JavaScript « algorithmique »** que vous avez écrite : elle doit contenir une **variable** et une **condition** ou une **boucle** (un mini-quiz qui compte les points, un compteur avec un seuil, une vérification de formulaire…) — pas seulement un `innerHTML = "…"` ;

- un **formulaire** (avec un attribut `method`).

!!! encadre "Aide-mémoire JavaScript : boucle et hasard (en plus du cours)"

    Le cours montre la condition `if (…) { …}`. Pour une boucle ou un tirage au hasard :

    - `for (let i = 1; i <= 10; i++) { …}` répète le bloc pour `i` allant de 1 à 10 (comme `for i in range(1, 11):` en Python) ;

    - `while (n > 0) { …}` répète tant que la condition est vraie ;

    - `Math.floor(Math.random() * 6) + 1` donne un entier au hasard entre 1 et 6 (comme `randint(1, 6)`).

!!! encadre "Arborescence imposée"

    Tout le site tient dans un dossier `monsite/` organisé ainsi :

    |                      |                                         |
    |:---------------------|:----------------------------------------|
    | `monsite/index.html` | la page d’accueil (nom **obligatoire**) |
    | `monsite/contenus/`  | les autres pages `.html`                |
    | `monsite/styles/`    | les feuilles de style `.css`            |
    | `monsite/scripts/`   | les fichiers JavaScript `.js`           |
    | `monsite/medias/`    | les images et autres médias             |

## Choisir un thème

Choisissez **un** thème dans le menu ci-dessous (ou proposez le vôtre, à faire valider). Chaque thème suggère des interactions ; à vous de les enrichir.

| **Thème** | **Interactions JavaScript possibles** |
|:---|:---|
| Site *utile* (convertisseur, minuteur, *to-do*) | calcul en direct, ajout/suppression d’éléments, compte à rebours |
| Mini-*quiz* sur un sujet | score qui se met à jour, correction, message selon le résultat |
| Mini-*jeu* (devine le nombre, pierre-feuille-ciseaux) | tirage aléatoire, test de la réponse, compteur de parties |
| *Portfolio* / page personnelle | galerie d’images, mode clair/sombre, afficher/masquer des sections |
| Site d’un *club* ou d’une *association* | formulaire d’adhésion, agenda interactif, bouton « j’aime » |

*Contrainte de bon sens :* un thème **correct et respectueux**, sans contenu personnel sensible (le site pourra être montré en classe).

## L’intelligence artificielle : mode d’emploi

!!! encadre "L’IA est autorisée — mais déclarée, et elle ne pense pas à votre place"

    Vous **pouvez** utiliser une IA (comme le web, pour chercher une technique ou débloquer un bug). **Mais** :

    - vous devez **comprendre et pouvoir expliquer chaque ligne** de votre site. *Ce que vous ne savez pas expliquer à l’oral ne comptera pas* — pire, cela se retournera contre vous ;

    - vous **déclarez** votre usage de l’IA dans votre **carnet de bord** : quels prompts, ce que vous avez **gardé, modifié ou rejeté**, et **pourquoi** ;

    - une IA se **trompe** souvent : à vous de repérer et corriger. Une suggestion d’IA n’est pas une vérité.

    En résumé : <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> IA **en appui** pendant le projet (chercher, déboguer, vérifier ; le code final est écrit et compris par vous) ; <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> **sans IA** pour le contrôle sur machine et la soutenance. Voir la charte d’usage de l’IA.

    **L’essentiel de votre note vient de ce que *vous* savez faire seul** (voir plus bas). Un site parfait que vous ne savez pas expliquer vaut moins qu’un site modeste que vous maîtrisez.

## Le déroulé : les jalons

Le projet se fait **en classe**, par étapes. À la fin de chaque séance, un point rapide avec le professeur valide votre avancée (et nourrit votre carnet de bord).

| **Jalon** | **Objectif de la séance** | **Validé si…** |
|:--:|:---|:---|
| J1 | structure HTML des pages $+$ navigation | les pages existent et sont reliées |
| J2 | mise en forme CSS (fichier séparé) | le style s’applique, fond/forme séparés |
| J3 | interactions JavaScript | au moins 4 interactions fonctionnent |
| J4 | formulaire, finitions, carnet de bord | le cahier des charges est complet |

## Comment vous serez évalué

L’évaluation récompense d’abord votre **compréhension**, pas seulement le résultat. Elle porte sur quatre éléments :

- la **soutenance orale** (individuelle) : expliquer votre code *et modifier une interaction en direct* ;

- un **contrôle sur machine, sans IA** : refaire seul, en classe, les gestes du projet ;

- le **carnet de bord** (dont l’usage de l’IA) : sérieux de la démarche et transparence ;

- **le site** (cahier des charges, code, navigation) : le produit fini et sa qualité.

!!! remarque "Remarque — Deux points d’attention"

    **La soutenance** (5 à 10 min) : vous présentez le site, on vous demande d’**expliquer** une fonction, de **prévoir** l’effet d’une modification, et d’**ajouter une petite interaction devant le professeur**.  
    **Le contrôle sans IA** : en classe, sans internet ni IA, à partir d’une page fournie, vous ajouterez quelques interactions et corrigerez un bug. C’est la preuve que *vous* savez faire.

## Le rendu

- Vérifiez que le site s’ouvre en double-cliquant sur `index.html`, et que **toute** la navigation fonctionne.

- **Compressez** le dossier `monsite/` (fichier `.zip`) et remettez-le selon les consignes de votre professeur, avant la date indiquée.

- Joignez votre **carnet de bord** complété.

- Citez vos **sources** (images, techniques) et n’utilisez que des médias **libres de droit**.

## Critères d’évaluation

La grille détaille, critère par critère, les quatre éléments de l’évaluation présentés plus haut. Les critères du site reprennent les jalons J1 à J4 : le TP qui précède (« Mon premier site, pas à pas ») vous a fait franchir les trois premiers sur un exemple ; il s’agit maintenant de refaire ces gestes sur votre propre site.

<table>
<thead>
<tr>
<th style="text-align: left;"><strong>Critère</strong></th>
<th style="text-align: left;"><strong>Ce qui est attendu</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" style="text-align: left;"><strong>Le site</strong></td>
</tr>
<tr>
<td style="text-align: left;">Structure et navigation (J1)</td>
<td style="text-align: left;">3 à 4 pages aux balises bien fermées et bien emboîtées ; un menu sur chaque page ; au moins un chemin relatif et un chemin absolu ; l’arborescence imposée respectée</td>
</tr>
<tr>
<td style="text-align: left;">Mise en forme (J2)</td>
<td style="text-align: left;">une feuille CSS séparée, reliée à chaque page ; des sélecteurs de balise, de classe et d’identifiant ; une disposition avec Flexbox</td>
</tr>
<tr>
<td style="text-align: left;">Interactions (J3)</td>
<td style="text-align: left;">au moins quatre interactions qui réagissent à un événement et modifient la page ; une fonction écrite par vous, avec une variable et une condition ou une boucle</td>
</tr>
<tr>
<td style="text-align: left;">Contenus et formulaire (J4)</td>
<td style="text-align: left;">des images libres de droit, sources citées ; un tableau ; un formulaire avec un attribut <code>method</code> ; le site s’ouvre depuis <code>index.html</code></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Soutenance orale</strong></td>
</tr>
<tr>
<td style="text-align: left;">Démonstration</td>
<td style="text-align: left;">le site fonctionne et respecte le cahier des charges</td>
</tr>
<tr>
<td style="text-align: left;">HTML et CSS</td>
<td style="text-align: left;">expliquer la structure des pages et la séparation du fond et de la forme</td>
</tr>
<tr>
<td style="text-align: left;">Une fonction JavaScript</td>
<td style="text-align: left;">l’expliquer ligne par ligne : l’événement, la sélection dans la page, la logique (condition ou boucle)</td>
</tr>
<tr>
<td style="text-align: left;">Modification en direct</td>
<td style="text-align: left;">réaliser devant le professeur la petite modification demandée</td>
</tr>
<tr>
<td style="text-align: left;">Recul</td>
<td style="text-align: left;">justifier un choix ; parler honnêtement de son usage de l’IA</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Contrôle sur machine, sans IA</strong></td>
</tr>
<tr>
<td style="text-align: left;">Ajouter des interactions</td>
<td style="text-align: left;">sur une page fournie : brancher un événement, sélectionner un élément, modifier la page</td>
</tr>
<tr>
<td style="text-align: left;">Corriger un bug</td>
<td style="text-align: left;">repérer l’erreur (console de <code>F12</code>, relecture) et la corriger</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Carnet de bord</strong></td>
</tr>
<tr>
<td style="text-align: left;">Suivi des séances</td>
<td style="text-align: left;">une entrée par séance : ce qui a été fait, les difficultés, les solutions trouvées</td>
</tr>
<tr>
<td style="text-align: left;">Usage de l’IA</td>
<td style="text-align: left;">chaque usage déclaré (la demande, la réponse, ce qui a été gardé, modifié ou rejeté, et pourquoi) ; le bilan final</td>
</tr>
</tbody>
</table>
