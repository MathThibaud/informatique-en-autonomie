# Exercices

<p class="sous-titre">Le Web : réseaux et interactions homme-machine</p>

!!! consignes "Mode d’emploi"

    -  Étoiles, <span class="essentiel">• essentiel</span>, coup de pouce, $\blacktriangleright$ et pastilles IA : voir le [mode d’emploi du chapitre 1](../01-les-bases-de-la-programmation-python/exercices.md#modeemploi).

    - <span class="run" title="À programmer et tester sur machine">▶</span> *À taper et tester* dans un navigateur (fichier `.html` ouvert localement, ou un éditeur en ligne).

    - Rôles à ne pas confondre : **HTML** $=$ le fond (structure) ; **CSS** $=$ la forme ; **JavaScript** $=$ le comportement.

### Réseaux : comment les machines se parlent

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 1</span> — Internet ou Web ? <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-10-1 }

<span class="essentiel">• essentiel</span>

Pour chaque phrase, dire si elle concerne **Internet** (le réseau) ou **le Web** (le service).

1.  consulter une page de cours avec des liens hypertextes ;

2.  envoyer un courriel ;

3.  l’ensemble des câbles, fibres et routeurs qui relient les machines ;

4.  cliquer d’article en article sur une encyclopédie en ligne.0

    ??? pouce "Coup de pouce"

        Internet est le réseau physique qui relie les machines ; le Web est *un* service qui l’utilise, fait de pages reliées par des liens hypertextes. Le courriel est un autre service.

??? corrige "Corrigé"

    !!! remarque "Remarque"

        On donne **une** version simple ; d’autres écritures sont possibles.

    Internet est le réseau (les machines et leurs liaisons) ; le Web est un service qui l’utilise (des pages reliées par des liens). a) **Web** ; b) **Internet** (le courriel est un service d’Internet, pas du Web) ; c) **Internet** ; d) **Web**.

    <span class="erreurfreq">▷ Erreur fréquente.</span> employer « Internet » et « le Web » comme synonymes : le courriel, les jeux en ligne ou la visioconférence utilisent Internet sans passer par le Web.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 2</span> — Le bon mot <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-10-2 }

Compléter avec : *protocole* / *adresse IP* / *paquet* / *routeur* / *DNS*.

1.  Le … traduit un nom de domaine en ….

2.  Un message est découpé en … avant de circuler.

3.  Un … aiguille ces morceaux vers leur destination.

4.  HTTP est un … : un ensemble de règles de communication.0

    ??? pouce "Coup de pouce"

        Le mot « adresse IP » complète la première phrase ; pour les autres, revoir le vocabulaire de la section sur le réseau du cours.

??? corrige "Corrigé"

    On suit le trajet d’un message : on trouve l’adresse, on découpe, on aiguille, en respectant des règles communes. a) le **DNS** traduit un nom de domaine en **adresse IP** ; b) **paquets** ; c) **routeur** ; d) **protocole**.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 3</span> — Client-serveur ou pair-à-pair ? <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-10-3 }

<span class="essentiel">• essentiel</span>

1.  Décrire, avec les mots *demande* et *fournit*, le modèle client-serveur.

2.  Dans un logiciel de partage de fichiers en *pair-à-pair*, quel(s) rôle(s) joue votre machine ?

3.  Quand vous consultez un site web, votre ordinateur est-il plutôt client ou serveur ? Pourquoi ?0

    ??? pouce "Coup de pouce"

        Le client est celui qui demande, le serveur celui qui fournit. En pair-à-pair, une même machine peut-elle faire les deux ?

??? corrige "Corrigé"

    **a)** Des machines **clientes** *demandent* des ressources ; une machine **serveur** les *fournit*. **b)** En pair-à-pair, votre machine est **à la fois cliente et serveur** (elle reçoit et fournit). **c)** **Client** : elle demande des pages aux serveurs web et ne fournit rien en retour.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 4</span> — Le voyage d’un paquet <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-4 }

Un paquet part de votre machine (IP `192.168.1.10`) vers un serveur (IP `193.51.208.14`).

1.  Quelles adresses le paquet doit-il porter pour arriver *et* pour qu’on puisse lui répondre ?

2.  Deux paquets d’un même message peuvent-ils suivre des chemins différents ? Que se passe-t-il si l’un se perd ?

    ??? pouce "Coup de pouce"

        Penser à une lettre postale : quelles adresses écrit-on sur l’enveloppe pour qu’elle arrive, et pour qu’on puisse y répondre ?

??? corrige "Corrigé"

    **a)** L’adresse IP de **destination** `193.51.208.14` *et* l’adresse IP **source** `192.168.1.10` (sans elle, le serveur ne saurait pas à qui répondre). *Précision* : `192.168.1.10` est une adresse **privée** ; en sortant vers Internet, la box la remplace par son adresse publique, et c’est à la box que le serveur répond, qui transmet ensuite la réponse à la machine (traduction d’adresses, NAT). **b)** Oui, deux paquets peuvent suivre des **chemins différents** ; un paquet perdu est simplement **renvoyé**.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 5</span> — Dérouler le protocole du bit alterné <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-5 }

<span class="essentiel">• essentiel</span>

Alice envoie à Bob quatre paquets, étiquetés successivement `0`, `1`, `0`, `1`. Après chaque paquet reçu, Bob renvoie un accusé de réception (ACK). Sans ACK au bout du délai, Alice renvoie le *même* paquet.

1.  Rappeler à quoi sert le bit `0`/`1` qui étiquette chaque paquet.

2.  **Scénario 1.** Tout arrive normalement. Combien de paquets et combien d’accusés circulent en tout ?

3.  **Scénario 2.** Le **2<sup>e</sup> paquet** (étiquette `1`) se perd en route. Décrire, étape par étape, ce que fait Alice, puis Bob. Combien de fois le 2<sup>e</sup> paquet est-il finalement envoyé ?

4.  **Scénario 3.** Cette fois le 2<sup>e</sup> paquet arrive bien, mais c’est son **accusé qui se perd**. Alice renvoie donc le 2<sup>e</sup> paquet (étiquette `1`). Comment Bob comprend-il que c’est un **doublon**, et que fait-il alors ?

    ??? pouce "Coup de pouce"

        Dessiner deux colonnes, Alice et Bob, et une flèche par message (paquet ou accusé), en notant l’étiquette `0` ou `1` de chaque paquet.

??? corrige "Corrigé"

    **a)** Le bit `0`/`1` sert à **distinguer un nouveau paquet d’un paquet renvoyé** : si Bob reçoit deux fois de suite un paquet portant le même bit, le second est un **doublon**.

    **b) Scénario 1 (tout arrive).** 4 paquets partent, 4 accusés reviennent : **4 paquets et 4 accusés**, aucun renvoi.

    **c) Scénario 2 (le 2<sup>e</sup> paquet, étiquette `1`, se perd).** Alice envoie le paquet étiqueté `1` et attend son accusé. Comme le paquet n’arrive pas à Bob, aucun accusé n’est renvoyé ; au bout du délai, Alice **renvoie le même paquet `1`**. Cette fois il arrive, Bob le traite et renvoie l’accusé. Le 2<sup>e</sup> paquet a donc été envoyé **2 fois**. Alice passe ensuite au paquet `0` suivant.

    **d) Scénario 3 (l’accusé du 2<sup>e</sup> paquet se perd).** Bob a bien reçu et traité le 2<sup>e</sup> paquet (étiquette `1`), mais son accusé se perd. Faute d’accusé, Alice **renvoie le 2<sup>e</sup> paquet (étiquette `1`)**. Bob constate qu’il porte **le bit qu’il vient déjà de traiter** : c’est un doublon, il le **jette** (sans le traiter une deuxième fois) mais **renvoie quand même l’accusé**, pour qu’Alice puisse avancer.

### URL et protocole HTTP

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 6</span> — Décomposer une URL <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-10-6 }

<span class="essentiel">• essentiel</span>

On donne l’URL \; `https://www.lycee.mc/nsi/web/cours.html`

1.  Quel est le **protocole** ? La communication est-elle sécurisée ? À quoi le voit-on ?

2.  Quel est le **nom de domaine** du serveur ?

3.  Quel est le **chemin** de la ressource sur le serveur ?0

    ??? pouce "Coup de pouce"

        Une URL se lit de gauche à droite : le protocole avant `://`, puis le nom du serveur jusqu’au premier `/`, puis le chemin.

??? corrige "Corrigé"

    On lit l’URL de gauche à droite : protocole avant `://`, domaine jusqu’au premier `/`, puis chemin. a) protocole `https` : oui, **sécurisée** (chiffrée), on le voit au « s » de `https`. \; b) `www.lycee.mc`. \; c) `/nsi/web/cours.html`.

    <span class="erreurfreq">▷ Erreur fréquente.</span> inclure le protocole ou le chemin dans le nom de domaine : le domaine est seulement `www.lycee.mc`, entre `://` et le premier `/`.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 7</span> — Les codes de réponse HTTP <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-10-7 }

Associer chaque code à la situation correspondante : \; `200` \;/\; `304` \;/\; `403` \;/\; `404` \;/\; `500`.

1.  la page demandée existe et le serveur l’envoie ;

2.  l’adresse contient une faute de frappe : la page n’existe pas ;

3.  le programme du serveur a planté pendant la préparation de la page ;

4.  la page existe, mais vous n’avez pas le droit de la consulter ;

5.  l’image n’a pas changé depuis votre dernière visite : le navigateur garde sa copie.0

    ??? pouce "Coup de pouce"

        Les codes en `2..` signalent un succès, en `3..` une redirection ou une copie déjà à jour, en `4..` une erreur du client, en `5..` une erreur du serveur.

??? corrige "Corrigé"

    a\) `200` ; \; b) `404` ; \; c) `500` ; \; d) `403` ; \; e) `304`. Les codes en `4..` sont des erreurs du client (mauvaise adresse, accès refusé), ceux en `5..` des erreurs du serveur.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — Lire un échange HTTP <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-10-8 }

```html
GET /nsi/web/cours.html HTTP/1.1

HTTP/1.1 404 Not Found
Content-Type: text/html
```

1.  Qui envoie la première ligne ? Qui envoie les deux lignes suivantes ?

2.  Quelle est la **méthode** de la requête ?

3.  Que signifie le code **404** ? La ressource a-t-elle été trouvée ? Que renverrait le serveur en cas de succès ?

    ??? pouce "Coup de pouce"

        Une requête commence par une méthode ; une réponse commence par la version de HTTP, suivie d’un code.

??? corrige "Corrigé"

    **a)** La première ligne (`GET…`) est envoyée par le **client** ; les deux lignes suivantes (`HTTP/1.1 404…` et `Content-Type…`) forment la **réponse du serveur**. **b)** La méthode est `GET`. **c)** **404** signifie « ressource **introuvable** » : elle n’a pas été trouvée. En cas de succès, le serveur renverrait `200 OK` suivi du code HTML de la page.

    <span class="erreurfreq">▷ Erreur fréquente.</span> croire qu’un code `404` signale une panne du serveur : le serveur a bien répondu ; c’est la ressource demandée qui n’existe pas (les pannes du serveur sont les codes `5..`).

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 9</span> — `GET` ou `POST` ? <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-10-9 }

Pour chaque situation, choisir la méthode la plus adaptée et **justifier**.

1.  afficher la page d’accueil d’un site ;

2.  envoyer un identifiant et un mot de passe pour se connecter ;

3.  lancer une recherche « chat » qu’on aimerait pouvoir mettre en favori.

    ??? pouce "Coup de pouce"

        Pour chaque cas, se demander : les données peuvent-elles être visibles (et mémorisées) dans l’URL, ou doivent-elles rester cachées ?

??? corrige "Corrigé"

    **a)** `GET` : on *demande* une page. **b)** `POST` : un mot de passe est sensible, il ne doit **pas** apparaître dans l’URL. **c)** `GET` : la recherche apparaît dans l’URL (`...?q=chat`), donc partageable et gardable en favori.

### HTML et CSS

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 10</span> — À chaque balise son rôle <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-10-10 }

Associer chaque balise à son rôle : \; <code>&lt;h1&gt;</code> \;/\; <code>&lt;p&gt;</code> \;/\; <code>&lt;a&gt;</code> \;/\; <code>&lt;img&gt;</code> \;/\; <code>&lt;ul&gt;</code> \;/\; <code>&lt;li&gt;</code>.

1.  un lien hypertexte ;

2.  un élément d’une liste ;

3.  un titre principal ;

4.  une image ;

5.  un paragraphe ;

6.  une liste à puces.

Laquelle de ces balises s’écrit **sans** balise fermante ?0

??? pouce "Coup de pouce"

    `h` comme *heading* (titre), `p` comme paragraphe, `a` comme ancre, `ul` comme liste non ordonnée, `li` comme élément de liste. Quelle balise n’entoure aucun texte ?

??? corrige "Corrigé"

    a\) <code>&lt;a&gt;</code> ; \; b) <code>&lt;li&gt;</code> ; \; c) <code>&lt;h1&gt;</code> ; \; d) <code>&lt;img&gt;</code> ; \; e) <code>&lt;p&gt;</code> ; \; f) <code>&lt;ul&gt;</code>. La balise <code>&lt;img&gt;</code> n’a pas de balise fermante : elle n’entoure aucun contenu (<code>&lt;img src="logo.png" alt="logo"&gt;</code>).

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 11</span> — Lire du HTML <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-10-11 }

<span class="essentiel">• essentiel</span>

```html
<body>
  <h1>Recettes</h1>
  <p>Voici ma recette <strong>preferee</strong>.</p>
  <a href="dessert.html">Voir les desserts</a>
</body>
```

1.  Nommer la balise du titre, celle du paragraphe, celle du lien.

2.  Vers quelle page mène le lien ? Est-ce un chemin relatif ou absolu ?

3.  Dessiner l’**arbre** (DOM) de ce fragment.0

    ??? pouce "Coup de pouce"

        Dans l’arbre, chaque balise est un nœud ; les balises placées *entre* l’ouverture et la fermeture d’une autre en sont les enfants.

??? corrige "Corrigé"

    **a)** Titre : <code>&lt;h1&gt;</code> ; paragraphe : <code>&lt;p&gt;</code> ; lien : <code>&lt;a&gt;</code>. **b)** Vers `dessert.html` ; c’est un chemin **relatif** (pas de `/` ni de domaine au début). **c)** Arbre (DOM) :

    ![](../figures/0b18c85f11bf99ae.svg){ .tikz loading=lazy }

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 12</span> — Corriger le HTML <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-12 }

Ce fragment contient deux erreurs de balises. Les repérer et les corriger.

```html
<p>Un paragraphe <strong>en gras</p></strong>
<h2>Un sous-titre
```

??? pouce "Coup de pouce"

    Vérifier que chaque balise ouverte est fermée, et que les balises s’emboîtent sans se croiser : la dernière ouverte est la première fermée.

??? corrige "Corrigé"

    Les balises <code>&lt;strong&gt;</code> et <code>&lt;p&gt;</code> sont **mal imbriquées**, et le <code>&lt;h2&gt;</code> n’est pas fermé :

    ```html
    <p>Un paragraphe <strong>en gras</strong></p>
    <h2>Un sous-titre</h2>
    ```

    <span class="erreurfreq">▷ Erreur fréquente.</span> fermer les balises dans l’ordre où on les a ouvertes : la dernière ouverte (<code>&lt;strong&gt;</code>) doit être la première fermée.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 13</span> — <span class="run" title="À programmer et tester sur machine">▶</span>  Ma première page <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-13 }

Écrire une page HTML complète (avec <code>&lt;!doctype html&gt;</code>, <code>&lt;head&gt;</code> et <code>&lt;body&gt;</code>) affichant un titre « Mon site NSI », un paragraphe de présentation, et un lien vers `eduscol.education.fr`. L’ouvrir dans un navigateur.

??? pouce "Coup de pouce"

    Repartir du squelette de page complète du cours. Un lien vers un autre site demande une adresse complète, qui commence par `https://`, dans `href`.

??? corrige "Corrigé"

    On part du squelette du cours (<code>&lt;!doctype html&gt;</code>, puis <code>&lt;head&gt;</code> pour les informations sur la page et <code>&lt;body&gt;</code> pour ce qui s’affiche) ; le lien vers un autre site prend une adresse complète dans `href`.

    ```html
    <!doctype html>
    <html lang="fr">
      <head>
        <meta charset="utf-8">
        <title>Mon site NSI</title>
      </head>
      <body>
        <h1>Mon site NSI</h1>
        <p>Bienvenue sur ma page de presentation.</p>
        <a href="https://eduscol.education.fr">Eduscol</a>
      </body>
    </html>
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 14</span> — Relier le CSS <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-10-14 }

<span class="essentiel">• essentiel</span>

On donne le CSS :

```css
h1 { color: darkblue; text-align: center; }
p  { font-size: 18px; }
#avertissement { color: red; }
```

1.  Quelle sera l’apparence des titres <code>&lt;h1&gt;</code> ?

2.  Quel élément de la page sera affiché en rouge ? (Sa balise peut-elle se déduire du CSS seul ?)

3.  On écrit ces règles dans un fichier `.css` à part plutôt que dans le HTML. Quel principe cela illustre-t-il, et quel en est l’intérêt pour un site de plusieurs pages ?

    ??? pouce "Coup de pouce"

        Le symbole `#` devant un nom désigne l’élément qui porte cet `id`. Pour c), relire les rôles des trois langages dans le mode d’emploi.

??? corrige "Corrigé"

    **a)** Les <code>&lt;h1&gt;</code> seront en **bleu foncé** et **centrés**. **b)** L’élément qui porte `id="avertissement"` sera en **rouge**, quelle que soit sa balise : le CSS seul ne permet pas de savoir s’il s’agit d’un <code>&lt;p&gt;</code>, d’un <code>&lt;div&gt;</code>… (il faut lire le HTML). **c)** La **séparation du fond (HTML) et de la forme (CSS)** : on change l’apparence sans toucher au contenu. Pour un site de plusieurs pages, toutes les pages se relient au même fichier `.css` : une seule modification change l’apparence de tout le site, et le style reste identique d’une page à l’autre.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 15</span> — `id` ou `class` ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-15 }

On donne ce fragment :

```html
<h1 id="titre">Menu</h1>
<p class="plat">Pizza</p>
<p class="plat">Salade</p>
```

1.  Pourquoi `titre` est-il un `id` et `plat` une `class` ? (penser à *unique* / *partagé*)

2.  Écrire le sélecteur CSS qui met **le titre** en bleu.

3.  Écrire le sélecteur CSS qui met **les deux plats** en vert, *d’un seul coup*.

    ??? pouce "Coup de pouce"

        Revoir les trois sortes de sélecteurs du cours : par balise, par `id`, par classe, et le symbole qui précède chacun.

??? corrige "Corrigé"

    **a)** `titre` est un `id` car il désigne **une seule** balise (unique) ; `plat` est une `class` car elle est **partagée** par plusieurs balises. **b)** et **c)** :

    ```css
    #titre { color: blue; }    /* # pour l'identifiant unique */
    .plat  { color: green; }   /* . pour la classe partagee : les deux plats */
    ```

    <span class="erreurfreq">▷ Erreur fréquente.</span> inverser les symboles : `#` désigne un `id`, `.` une classe. `#plat` ne désigne aucun élément ici.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 16</span> — <span class="run" title="À programmer et tester sur machine">▶</span>  Aligner avec Flexbox <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-16 }

<span class="horsprog">au-delà du programme</span> Écrire une page contenant une barre de navigation : un <code>&lt;div class="barre"&gt;</code> qui contient trois liens (<code>&lt;a&gt;</code>) « Accueil », « Cours », « Contact ».

1.  Dans le CSS, écrire la règle `.barre` qui aligne les trois liens **horizontalement** avec un espace de `15px` entre eux.

2.  Les répartir ensuite avec `justify-content: space-between`. Que change cette valeur ?

3.  *Piège :* faut-il mettre `display:flex` sur le <code>&lt;div&gt;</code> ou sur les <code>&lt;a&gt;</code> ? Pourquoi ?

    ??? pouce "Coup de pouce"

        Partir de l’exemple Flexbox du cours : quelles propriétés y figurent, et dans quelle règle sont-elles écrites ?

??? corrige "Corrigé"

    ```html
    <div class="barre">
      <a href="#">Accueil</a>
      <a href="#">Cours</a>
      <a href="#">Contact</a>
    </div>
    ```

    **a)** et **b)** :

    ```css
    .barre {
        display: flex;
        gap: 15px;                    /* a) espace entre les liens */
        justify-content: space-between;  /* b) pousse les liens aux extremites */
    }
    ```

    **b)** `space-between` **répartit** les liens sur toute la largeur, le premier collé à gauche, le dernier à droite, l’espace restant distribué entre eux. **c)** Sur le **<code>&lt;div&gt;</code>** (le **conteneur**) : c’est lui qui devient une boîte flexible, et ce sont *ses enfants* (les <code>&lt;a&gt;</code>) qui s’alignent.

### JavaScript : rendre la page vivante

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 17</span> — Prévoir l’effet <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-10-17 }

<span class="essentiel">• essentiel</span>

```html
<p id="message">Bonjour</p>
<button onclick="saluer()">Clique</button>
```

```javascript
function saluer() {
    let e = document.querySelector("#message");
    e.innerHTML = "Bonsoir !";
}
```

1.  Que se passe-t-il quand on clique sur le bouton ?

2.  À quel **événement** réagit-on ? Quel rôle joue `querySelector` ?

3.  Ce traitement s’exécute-t-il côté client ou côté serveur ?0

    ??? pouce "Coup de pouce"

        Repérer dans le HTML l’attribut qui relie le bouton à la fonction, puis lire la fonction ligne par ligne : quelle balise est sélectionnée, et que devient son contenu ?

??? corrige "Corrigé"

    **a)** Au clic, le paragraphe « Bonjour » devient « **Bonsoir !** ». **b)** On réagit à l’événement `click` (le clic sur le bouton), branché par l’attribut `onclick` ; `querySelector("#message")` **sélectionne** dans le DOM la balise d’`id message`. **c)** Ce traitement s’exécute **côté client** (dans le navigateur).

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 18</span> — <span class="run" title="À programmer et tester sur machine">▶</span>  Un compteur de clics <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-18 }

<span class="duree">≈ 15 min</span>

Sur une page contenant <code>&lt;p id="score"&gt;0&lt;/p&gt;</code> et un bouton, écrire une fonction JavaScript qui, à chaque clic, **augmente de 1** le nombre affiché.

??? pouce "Coup de pouce"

    Trois étapes : lire le nombre affiché, lui ajouter 1, réécrire le résultat dans le paragraphe. Le texte lu est une chaîne : `parseInt(e.innerHTML)` le transforme en entier.

??? pouce "Coup de pouce 2 (début de solution)"

    `function compter() {`  
    `let e = document.querySelector("#score");`  
    `let n = parseInt(e.innerHTML);`  
    …

??? corrige "Corrigé"

    ```html
    <p id="score">0</p>
    <button onclick="compter()">+1</button>
    <script src="script.js"></script>
    ```

    ```javascript
    function compter() {
        let e = document.querySelector("#score");
        let n = parseInt(e.innerHTML);
        e.innerHTML = n + 1;
    }
    ```

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 19</span> — <span class="run" title="À programmer et tester sur machine">▶</span>  Additionner deux nombres <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-19 }

Une page contient deux champs et un bouton :

```html
<input type="number" id="a">
<input type="number" id="b">
<button id="calc">Additionner</button>
<p id="resultat"></p>
```

1.  Écrire la fonction `additionner()` qui **lit** les deux champs avec `.value`, en fait la somme (`parseInt(...)`) et l’affiche dans le paragraphe `#resultat`.

2.  Au lieu de `onclick` dans le HTML, **brancher** le bouton depuis le JavaScript avec `addEventListener`.

3.  Ce calcul a-t-il besoin du serveur ?

    ??? pouce "Coup de pouce"

        `.value` donne le texte saisi dans un champ : le convertir avant d’additionner, sinon `+` colle les deux textes. Pour b), revoir la forme `bouton.addEventListener("click", …)` du cours.

    ??? pouce "Coup de pouce 2 (début de solution)"

        `function additionner() {`  
        `let a = parseInt(document.querySelector("#a").value);`  
        `let b = …`

??? corrige "Corrigé"

    **a)** et **b)** (version avec `addEventListener`) :

    ```javascript
    function additionner() {
        let a = parseInt(document.querySelector("#a").value);
        let b = parseInt(document.querySelector("#b").value);
        document.querySelector("#resultat").textContent = a + b;
    }
    // on branche le bouton depuis le JS (pas d'onclick dans le HTML)
    document.querySelector("#calc").addEventListener("click", additionner);
    ```

    **c)** **Non** : le calcul se fait entièrement **côté client**, dans le navigateur.

    <span class="erreurfreq">▷ Erreur fréquente.</span> additionner directement les `.value` : ce sont des chaînes, et `+` les colle (`"2" + "3"` donne `"23"`). On convertit d’abord avec `parseInt`.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 20</span> — <span class="run" title="À programmer et tester sur machine">▶</span>  Mini-projet : un thème clair/sombre <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-20 }

<span class="duree">≈ 30 min</span>

Construire une page **complète** (HTML $+$ CSS $+$ JS dans un seul fichier) avec un titre, un paragraphe, et un bouton « Changer de thème ».

1.  En CSS, définir une classe `.sombre` qui met le fond en noir et le texte en blanc (`background` et `color`).

2.  En JavaScript, au clic sur le bouton, **ajouter ou retirer** cette classe sur le <code>&lt;body&gt;</code>, avec l’instruction :  
    `document.body.classList.toggle("sombre")`

3.  *Bonus :* placer le bouton et un second bouton « À propos » dans une barre `display:flex` alignée à droite (`justify-content: flex-end`).

    ??? pouce "Coup de pouce"

        Construire dans l’ordre : la page HTML, puis la règle `.sombre` dans un <code>&lt;style&gt;</code> du <code>&lt;head&gt;</code>, puis une fonction appelée au clic.

    ??? pouce "Coup de pouce 2 (début de solution)"

        <code>&lt;button onclick="changer()"&gt;Changer de thème&lt;/button&gt;</code>  
        `function changer() {`  
        …

??? corrige "Corrigé"

    Une page complète possible :

    ```html
    <!doctype html>
    <html lang="fr">
    <head>
      <meta charset="utf-8">
      <title>Theme</title>
      <style>
        body        { font-family: sans-serif; margin: 20px; }
        .barre      { display: flex; justify-content: flex-end; gap: 8px; }
        .sombre     { background: black; color: white; }
      </style>
    </head>
    <body>
      <div class="barre">
        <button onclick="basculer()">Changer de theme</button>
        <button>A propos</button>
      </div>
      <h1>Mon site</h1>
      <p>Clique sur le bouton pour changer l'apparence.</p>

      <script>
        function basculer() {
            document.body.classList.toggle("sombre");
        }
      </script>
    </body>
    </html>
    ```

    Au clic, `classList.toggle("sombre")` **ajoute** la classe si elle est absente, la **retire** sinon : le fond bascule du clair au sombre. La barre de boutons est alignée à droite grâce à `display:flex` $+$ `justify-content: flex-end`.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 21</span> — Client ou serveur ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-21 }

1.  Pour chaque tâche, dire si elle est plutôt exécutée **côté client** (dans le navigateur, en JavaScript) ou **côté serveur** (sur la machine distante) :

    1.  afficher ou masquer un menu quand on clique dessus ;

    2.  changer la couleur d’un bouton au survol de la souris ;

    3.  vérifier qu’un champ contient bien un « @ » *avant* d’envoyer un formulaire ;

    4.  vérifier qu’un mot de passe est correct pour connecter l’utilisateur ;

    5.  consulter une base de données pour afficher les résultats d’une recherche ;

    6.  enregistrer définitivement une commande d’achat.

2.  Un site vérifie **en JavaScript** qu’un code promo est valide avant d’accorder une réduction. Un élève affirme : « puisque c’est vérifié, le prix payé est forcément juste. » Expliquer **pourquoi le serveur doit refaire la vérification** de son côté.

    ??? pouce "Coup de pouce"

        Qui peut voir et modifier le JavaScript d’une page ?

3.  Le traitement côté serveur s’écrit dans un *autre* langage que celui de l’interaction dans la page. Citer un exemple de langage côté serveur, et le langage utilisé côté client.

??? corrige "Corrigé"

    **a)**

    1.  afficher/masquer un menu : **client** (réaction immédiate d’affichage, aucun besoin du serveur) ;

    2.  couleur au survol : **client** (souvent même en CSS seul) ;

    3.  vérifier la présence d’un « @ » avant l’envoi : **client** (confort : prévenir tout de suite), *mais* le serveur devra revérifier ;

    4.  vérifier un mot de passe : **serveur** (le client ne doit pas connaître les mots de passe enregistrés) ;

    5.  consulter une base de données : **serveur** (c’est lui qui détient et interroge la base) ;

    6.  enregistrer une commande : **serveur** (donnée durable et sensible).

    **b)** Le JavaScript s’exécute **sur la machine de l’utilisateur** : celui-ci peut le **lire et le modifier** (outils de développement), ou même envoyer la requête sans passer par la page. Une vérification faite *seulement* côté client est donc **contournable** : le serveur, hors de portée de l’utilisateur, doit **refaire** la vérification avant d’accorder la réduction. *Règle générale : tout contrôle sensible se refait côté serveur.*

    **c)** Côté client : **JavaScript**. Côté serveur : par exemple **PHP** (ou Python) — il n’est pas demandé d’en développer une expertise, seulement de savoir *qui fait quoi*.

### Les formulaires

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 22</span> — Lire un formulaire <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-10-22 }

<span class="essentiel">• essentiel</span>

```html
<form action="/inscription" method="post">
    <input type="text" name="prenom">
    <input type="email" name="courriel">
    <button type="submit">Envoyer</button>
</form>
```

1.  Vers quelle adresse les données sont-elles envoyées ? Avec quelle méthode ?

2.  Sous quels noms les deux valeurs arriveront-elles au serveur ?

3.  Avec cette méthode, les données apparaissent-elles dans l’URL ?

    ??? pouce "Coup de pouce"

        Les attributs `action`, `method` et `name` répondent chacun à l’une des questions.

??? corrige "Corrigé"

    **a)** Vers `/inscription`, avec la méthode `post`. **b)** Sous les noms `prenom` et `courriel` (les attributs `name`). **c)** **Non** : avec `POST`, les données ne figurent pas dans l’URL.

    <span class="erreurfreq">▷ Erreur fréquente.</span> chercher le nom d’envoi dans `type` ou dans le texte affiché : c’est l’attribut `name` qui donne l’étiquette sous laquelle la valeur arrive au serveur.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 23</span> — <span class="run" title="À programmer et tester sur machine">▶</span>  Un formulaire de recherche <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-23 }

<span class="duree">≈ 20 min</span>

Le site `https://www.recettes.mc` veut un formulaire de recherche, envoyé à l’adresse `/recherche`.

1.  Écrire ce formulaire : un champ texte nommé `q` (le mot cherché), un champ texte nommé `tri`, et un bouton d’envoi. Choisir la méthode, sachant qu’on veut pouvoir mettre une recherche en favori.

2.  Un visiteur tape « tarte » dans `q` et « prix » dans `tri`, puis envoie. Écrire l’URL complète demandée au serveur.

3.  On lit dans l’historique : `https://www.recettes.mc/recherche?q=soupe&tri=date`. Qu’avait-on saisi dans chaque champ ?

4.  Le site ajoute un formulaire de connexion avec un mot de passe. Peut-on reprendre la même méthode ? Pourquoi ?

??? pouce "Coup de pouce"

    Revoir dans le cours la forme d’une URL avec `GET` : un `?`, puis des paires `clef=valeur` séparées par `&`.

??? pouce "Coup de pouce 2 (début de solution)"

    <code>&lt;form action="/recherche" method="…"&gt;</code>  
    <code>&lt;input type="text" name="q"&gt;</code>  
    …

??? corrige "Corrigé"

    **a)** Méthode `get`, pour que la recherche figure dans l’URL et puisse être gardée en favori :

    ```html
    <form action="/recherche" method="get">
        <input type="text" name="q">
        <input type="text" name="tri">
        <button type="submit">Chercher</button>
    </form>
    ```

    **b)** `https://www.recettes.mc/recherche?q=tarte&tri=prix` : l’adresse `action`, puis `?`, puis les paires `name=valeur` séparées par `&`. **c)** « soupe » dans le champ `q`, « date » dans le champ `tri`. **d)** **Non** : avec `get`, le mot de passe apparaîtrait dans l’URL, donc à l’écran et dans l’historique. On utilise `post` (et une page en `https`).

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 24</span> — Ce que retient le navigateur : les cookies <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-10-24 }

À la première visite d’un internaute, le serveur `https://www.recettes.mc` répond :

```text
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Set-Cookie: theme=sombre; Max-Age=604800
Set-Cookie: panier=tarte-citron
```

1.  Ces deux informations sont-elles mémorisées dans le client ou sur le serveur ?

2.  L’internaute clique ensuite sur un lien vers la page `/desserts.html` du même site. Écrire la première ligne de la requête envoyée, puis l’en-tête qui retransmet les cookies.

3.  Combien de temps chaque cookie est-il conservé ?

4.  L’internaute se rend ensuite sur `https://www.meteo.mc`. Le navigateur envoie-t-il ces cookies à ce site ?

5.  Un autre site marchand range le prix à payer dans un cookie `prix=45`, et son serveur facture le prix qu’il lit dans ce cookie. Pourquoi est-ce une mauvaise idée ?

??? pouce "Coup de pouce"

    `Max-Age` est une durée en secondes ; une journée compte $24 \times 3600$ secondes.

??? pouce "Coup de pouce 2 (début de solution)"

    Où le cookie est-il rangé, et qui peut donc le lire et le modifier ?

??? corrige "Corrigé"

    **a)** Dans le **client** : l’en-tête `Set-Cookie` demande au navigateur de les garder. **b)** Le navigateur retransmet de lui-même les deux cookies, séparés par `;` :

    ```text
    GET /desserts.html HTTP/1.1
    Cookie: theme=sombre; panier=tarte-citron
    ```

    **c)** `theme` : $604\,800$ secondes, soit $604\,800 / (24 \times 3600) = 7$ jours. `panier` n’a pas de durée : il est effacé à la fermeture du navigateur. **d)** **Non** : un cookie n’est renvoyé qu’au site qui l’a déposé (`www.recettes.mc`). **e)** Le cookie est stocké chez le client : l’utilisateur peut le lire et le **modifier** (par exemple avec les outils de développement) et payer `prix=1`. Le prix doit être calculé et vérifié **sur le serveur** ; un cookie ne doit contenir que des informations sans risque (préférence, identifiant de session).

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 25</span> — Le voyage d’un clic (synthèse) <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-10-25 }

Remettre dans l’ordre les étapes qui vont de la saisie d’une URL à l’affichage de la page.

1.  le navigateur affiche la page en assemblant HTML, CSS et JavaScript ;

2.  le serveur renvoie une réponse HTTP contenant le HTML ;

3.  le DNS traduit le nom de domaine en adresse IP ;

4.  le navigateur envoie une requête HTTP `GET` au serveur ;

5.  les paquets traversent des routeurs jusqu’au serveur.

    ??? pouce "Coup de pouce"

        Avant de pouvoir contacter le serveur, le navigateur doit connaître son adresse IP.

??? corrige "Corrigé"

    Ordre : **3** (le DNS traduit le nom en IP) $\to$ **4** (requête HTTP `GET`) $\to$ **5** (les paquets traversent les routeurs) $\to$ **2** (réponse HTTP avec le HTML) $\to$ **1** (le navigateur assemble et affiche).

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 26</span> — `GET` et `POST` selon un assistant d’IA <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> { #ex-10-26 }

Un élève demande à un assistant d’IA : « Quelle est la différence entre les méthodes `GET` et `POST` ? » Voici la réponse obtenue.

« Ce sont les deux méthodes principales du protocole HTTP. `GET` sert à **demander** une ressource, par exemple afficher une page : c’est la méthode utilisée quand on tape une URL dans le navigateur. `POST` sert à **envoyer** des données au serveur pour qu’il les traite, typiquement celles d’un formulaire. Dans les deux cas, le navigateur (le client) envoie une requête et le serveur répond avec un code de statut (`200`, `404`, etc.). La différence concrète pour un formulaire : avec `GET`, les données sont placées dans le corps de la requête et n’apparaissent pas dans l’URL ; avec `POST`, elles sont ajoutées à la fin de l’URL après un `?`. »

1.  La réponse est-elle correcte ? Vérifier avec le cours, puis en soumettant un formulaire `method="get"` (par exemple une recherche sur un moteur de recherche) et en observant l’URL obtenue.

2.  Localiser et corriger l’erreur.

3.  Quelle vérification simple, faite avant de faire confiance à la réponse, aurait suffi à détecter l’erreur ?

    ??? pouce "Coup de pouce"

        Confronter chaque phrase à la partie « Les formulaires » du cours, en particulier ce qui est dit de l’URL.

??? corrige "Corrigé"

    **a)** Non. Le cours dit : « `GET` : les éventuels paramètres sont **visibles dans l’URL** » et « `POST` : les données ne sont **pas** dans l’URL ». En pratique, après une recherche sur un moteur (formulaire en `get`), l’URL contient bien les mots cherchés après le `?` (par exemple `...?q=lycee+monaco`). **b)** L’erreur est l’**inversion** de la dernière phrase. Correction : avec `GET`, les données sont ajoutées à la fin de l’URL après un `?` ; avec `POST`, elles voyagent dans le **corps** de la requête et n’apparaissent pas dans l’URL. Le reste (rôles de `GET` et `POST`, client-serveur, codes de statut) est juste. **c)** Un test d’une minute : soumettre un formulaire en `get` et regarder la barre d’adresse, ou ouvrir l’onglet Réseau des outils de développement (`F12`) et lire la méthode et l’URL de la requête. Le ton assuré ne prouve rien : l’inversion est l’erreur la plus facile à commettre sur deux notions symétriques.

### Entraînement

*Exercices courts pour s’entraîner aux gestes de base, chacun avec plusieurs données. Ils font tous partie du parcours essentiel.*

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 27</span> — Lire des URL <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-10-27 }

<span class="essentiel">• essentiel</span>

Pour chaque URL, donner le **protocole**, le **nom de domaine**, le **chemin** et, s’il y en a, les **paramètres** (noms et valeurs).

1.  `http://www.lycee.mc/index.html`

2.  `https://fr.wikipedia.org/wiki/Alan_Turing`

3.  `https://www.recettes.mc/recherche?q=soupe&tri=date`

??? pouce "Coup de pouce"

    Lire de gauche à droite : avant `://`, le protocole ; jusqu’au premier `/`, le domaine ; puis le chemin, jusqu’à un éventuel `?`. Après le `?`, des paires `nom=valeur` séparées par `&`.

??? corrige "Corrigé"

    a) protocole `http` (non sécurisé), domaine `www.lycee.mc`, chemin `/index.html`, pas de paramètre. b) `https`, `fr.wikipedia.org`, chemin `/wiki/Alan_Turing`, pas de paramètre. c) `https`, `www.recettes.mc`, chemin `/recherche`, paramètres `q` (valeur `soupe`) et `tri` (valeur `date`).

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 28</span> — Formulaires : `GET`, `POST` et l’URL <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-10-28 }

<span class="essentiel">• essentiel</span>

Les formulaires ci-dessous sont sur le site `https://www.site.mc`. Pour chacun, l’utilisateur remplit les champs comme indiqué, puis envoie. Donner la méthode, l’URL demandée au serveur, et dire si les valeurs saisies sont visibles dans cette URL.

a\) on saisit « Nice » :

```html
<form action="/meteo" method="get">
  <input type="text" name="ville">
  <button type="submit">OK</button>
</form>
```

b\) on saisit « ada » et « 1815 » :

```html
<form action="/connexion" method="post">
  <input type="text" name="login">
  <input type="password" name="mdp">
  <button type="submit">OK</button>
</form>
```

c\) on saisit « velo » et « 100 » :

```html
<form action="/annonces" method="get">
  <input type="text" name="cat">
  <input type="number" name="prix_max">
  <button type="submit">OK</button>
</form>
```

d\) Dans l’autre sens : après l’envoi d’un formulaire, la barre d’adresse affiche

`https://www.site.mc/films?genre=comedie&annee=2024`

Quelles étaient la méthode, l’adresse `action`, les noms des champs et les valeurs saisies ?

??? pouce "Coup de pouce"

    Avec `get`, l’URL est l’adresse `action`, suivie d’un `?` puis des paires `name=valeur` séparées par `&`. Avec `post`, l’URL est seulement l’adresse `action` : les valeurs voyagent dans le corps de la requête.

??? corrige "Corrigé"

    a) `GET` : `https://www.site.mc/meteo?ville=Nice`, la valeur est visible dans l’URL. b) `POST` : `https://www.site.mc/connexion` ; `login` et `mdp` voyagent dans le corps de la requête, ils n’apparaissent pas dans l’URL (c’est la bonne méthode pour un mot de passe). c) `GET` : `https://www.site.mc/annonces?cat=velo&prix_max=100`, valeurs visibles. d) Méthode `get` (les valeurs sont dans l’URL), `action="/films"`, deux champs nommés `genre` et `annee`, où l’on avait saisi `comedie` et `2024`.

    <span class="erreurfreq">▷ Erreur fréquente.</span> croire que `POST` rend les données secrètes : elles ne sont pas dans l’URL, mais restent lisibles dans la requête ; seul `https` les chiffre pendant le transport.

### Réseau : encapsulation et réseau local

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 29</span> — Des enveloppes dans des enveloppes <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-10-29 }

Le portable d’Inès (adresse IP `192.168.1.23`) demande la page `/horaires.html` au serveur web `51.75.20.30`, en `https` (port `443`). Sa carte Wi-Fi a l’adresse MAC `3C:22:FB:10:4A:01` ; la box, première étape du trajet, a l’adresse MAC `F4:CA:E5:81:02:9B`.

1.  Dessiner la trame envoyée par le portable sous forme de quatre cases emboîtées (comme le schéma de l’encapsulation du cours) et écrire dans chaque case les informations qu’elle contient : données HTTP, en-tête TCP, en-tête IP, en-tête MAC.

2.  Un routeur, au milieu du trajet, reçoit cette trame. Quelle information doit-il lire pour décider où envoyer le paquet ? Dans quel en-tête la trouve-t-il ?

3.  Au-delà de la box, d’un routeur à l’autre, l’en-tête MAC change à chaque saut, mais pas les adresses IP. Pourquoi ? (Qu’arrive-t-il à l’adresse source en passant par la box ?)

4.  Inès passe du Wi-Fi au réseau 4G de son téléphone. Le navigateur et le serveur doivent-ils changer leur façon d’écrire la requête HTTP ? Quel avantage de l’encapsulation cela illustre-t-il ?

??? pouce "Coup de pouce"

    Chaque couche n’ajoute que ce dont elle a besoin : l’application, la requête ; le transport, les ports ; le réseau, les adresses IP ; la liaison, les adresses MAC du « saut » en cours. Revoir la règle « L’encapsulation » du cours.

??? corrige "Corrigé"

    **a)** De l’extérieur vers l’intérieur :

    | **en-tête MAC** : source `3C:22:FB:10:4A:01`, destination `F4:CA:E5:81:02:9B` (la box) | **en-tête IP** : source `192.168.1.23`, destination `51.75.20.30` | **en-tête TCP** : port destination `443`, numéro d’ordre | **données HTTP** : `GET /horaires.html` (chiffrées, car `https`) |
    |:---|:---|:---|:---|

    **b)** L’**adresse IP de destination** (`51.75.20.30`), dans l’**en-tête IP** : le routeur ouvre la trame jusqu’à cet en-tête, sans avoir besoin de lire TCP ni HTTP. **c)** Les adresses MAC ne servent qu’à un « saut », d’une machine à la suivante sur un même réseau local : chaque routeur reconstruit une nouvelle trame vers son voisin. Les adresses IP désignent la source et la destination **finales** : elles restent les mêmes de bout en bout (sauf la traduction de l’adresse privée par la box, à la sortie du réseau local). **d)** Non : seule la couche liaison change (4G au lieu du Wi-Fi). La requête HTTP, l’en-tête TCP et l’en-tête IP s’écrivent de la même façon. Chaque couche fait son travail **sans connaître les autres** : c’est l’intérêt de l’encapsulation.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 30</span> — Le réseau d’un lycée <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-10-30 }

Voici les constituants d’un réseau d’établissement : un **commutateur** par salle, des **points d’accès Wi-Fi**, un **serveur** de fichiers et de comptes, un **pare-feu**, un **routeur d’accès** relié à Internet.

1.  Associer à chaque constituant l’un de ces rôles : (1) relier sans fil les tablettes au réseau ; (2) relier par câble les postes d’une même salle ; (3) filtrer les échanges entre le lycée et l’extérieur ; (4) relier le réseau du lycée à Internet ; (5) stocker les documents des élèves et vérifier les mots de passe.

2.  Un poste de la salle NSI ouvre `fr.wikipedia.org`. Citer, dans l’ordre, les constituants du lycée traversés par la requête avant qu’elle n’atteigne Internet.

3.  Les postes du lycée ont des adresses `10.0.x.x`. Le serveur de Wikipédia voit-il cette adresse ? Expliquer.

4.  Un site de jeux en ligne est inaccessible depuis le lycée, alors qu’il fonctionne à la maison. Quel constituant en est très probablement la cause ?

??? pouce "Coup de pouce"

    Revoir l’encadré « Le réseau du lycée » et la remarque sur les adresses privées et publiques.

??? corrige "Corrigé"

    **a)** Point d’accès Wi-Fi : (1) ; commutateur : (2) ; pare-feu : (3) ; routeur d’accès : (4) ; serveur : (5). **b)** Le **commutateur** de la salle, (éventuellement un commutateur central), le **pare-feu**, puis le **routeur d’accès**, qui envoie la requête vers Internet. **c)** Non. `10.0.x.x` est une adresse **privée**, valable seulement dans le réseau du lycée. Le routeur d’accès la remplace par l’adresse **publique** du lycée (traduction d’adresses, NAT) : Wikipédia ne voit que cette adresse publique, commune à tous les postes du lycée. **d)** Le **pare-feu** : il bloque les échanges que l’établissement n’autorise pas.

### Programmer une interface d’après un cahier des charges

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 31</span> — <span class="run" title="À programmer et tester sur machine">▶</span>  Une inscription à l’atelier robotique <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-10-31 }

<span class="duree">≈ 40 min</span>

Le club du lycée veut une petite page pour s’inscrire à l’atelier robotique. Programmer cette **interface homme-machine** (IHM) en respectant le **cahier des charges** suivant :

1.  La page affiche le titre « Inscription à l’atelier robotique ».

2.  Elle contient deux champs de saisie de texte : le **prénom** (`id="prenom"`) et la **classe** (`id="classe"`), chacun avec un texte indicatif (`placeholder`).

3.  Un bouton « S’inscrire » appelle, au clic, la fonction `inscrire()`.

4.  Si l’un des deux champs est vide, le paragraphe `id="message"` affiche « Remplir les deux champs. » en **rouge**, et rien d’autre ne change.

5.  Sinon, le message affiche, en **vert**, « Inscription enregistrée : » suivi du prénom ; une ligne « prénom (classe) », par exemple « Léa (1G2) », s’ajoute à la liste <code>&lt;ul id="inscrits"&gt;</code> ; les deux champs sont vidés.

6.  Tout se passe sans recharger la page.

Rappel de syntaxe : comme en Python, mais avec des accolades, on écrit `if (condition) { … } else { … }` ; l’égalité se teste avec `===`, la différence avec `!==` (comme dans le cours), et le « ou » logique s’écrit `||`.

1.  Lister les **composants graphiques** de cette interface et, pour chacun, l’**événement** qu’il traite (s’il en traite un).

2.  Écrire le code HTML du corps de la page (exigences C1 à C3).

3.  Écrire la fonction JavaScript `inscrire()` (exigences C4 à C6).

4.  Proposer **trois essais** qui vérifient les exigences C4 et C5 (ce qu’on saisit, ce qu’on doit observer), puis les réaliser dans le navigateur.

5.  On recharge la page : la liste des inscrits est de nouveau vide. Pourquoi ? Que faudrait-il ajouter pour que le professeur retrouve toutes les inscriptions ?

??? pouce "Coup de pouce"

    Repartir de la page « Ma liste de courses » du cours : un champ, un bouton, une liste <code>&lt;ul&gt;</code> que l’on complète avec `innerHTML`. Il y a ici deux champs à lire, et la couleur du message se change avec `.style.color`.

??? pouce "Coup de pouce 2 (début de solution)"

    `function inscrire() {`  
    `let prenom = document.querySelector("#prenom").value;`  
    `let classe = …`  
    `let message = document.querySelector("#message");`  
    `if (prenom === "" || classe === "") {`  
    …

??? corrige "Corrigé"

    **a)** Le titre <code>&lt;h1&gt;</code>, le paragraphe `#message` et la liste `#inscrits` servent seulement à **afficher** : ils ne traitent aucun événement. Les deux **champs de saisie** reçoivent la frappe au clavier ; leur contenu est lu par `.value` (ils ne déclenchent pas de fonction ici). Le **bouton** traite l’événement `click` : il appelle `inscrire()`.

    **b)**

    ```html
    <h1>Inscription à l'atelier robotique</h1>
    <input type="text" id="prenom" placeholder="Prénom">
    <input type="text" id="classe" placeholder="Classe (ex. 1G2)">
    <button onclick="inscrire()">S'inscrire</button>
    <p id="message"></p>
    <ul id="inscrits"></ul>
    <script src="script.js"></script>
    ```

    **c)**

    ```javascript
    function inscrire() {
        let prenom = document.querySelector("#prenom").value;
        let classe = document.querySelector("#classe").value;
        let message = document.querySelector("#message");
        if (prenom === "" || classe === "") {          // C4
            message.textContent = "Remplir les deux champs.";
            message.style.color = "red";
        } else {                                       // C5
            message.textContent = "Inscription enregistrée : " + prenom;
            message.style.color = "green";
            let liste = document.querySelector("#inscrits");
            liste.innerHTML += "<li>" + prenom + " (" + classe + ")</li>";
            document.querySelector("#prenom").value = "";
            document.querySelector("#classe").value = "";
        }
    }
    ```

    C6 est respectée : aucune requête n’est envoyée, tout se passe **côté client**.

    **d)** Trois essais possibles :

    | **prénom** | **classe** | **ce qu’on doit observer** |
    |:---|:---|:---|
    | `Léa` | `1G2` | message vert « Inscription enregistrée : Léa » ; la ligne « Léa (1G2) » s’ajoute à la liste ; les deux champs sont vidés (C5) |
    | (vide) | `1G2` | message rouge « Remplir les deux champs. » ; liste inchangée ; `1G2` reste dans son champ (C4) |
    | `Hugo` | (vide) | message rouge ; liste inchangée ; `Hugo` reste dans son champ (C4) |

    Un quatrième essai utile : deux inscriptions valides de suite, pour vérifier que la seconde s’**ajoute** à la première au lieu de la remplacer (d’où le `+=`).

    **e)** La liste n’existe que dans la page affichée, dans la mémoire du **navigateur** (côté client) : rien n’a été envoyé au serveur. Recharger la page la redemande au serveur, qui renvoie la page d’origine, avec une liste vide. Pour conserver les inscriptions, il faut les **envoyer au serveur** : un formulaire <code>&lt;form action="/inscription" method="post"&gt;</code> dont les champs ont un `name` (`prenom`, `classe`), et, côté serveur, un programme qui les enregistre (dans un fichier ou une base de données) et fabrique la page des inscrits. On choisit `POST` : on envoie des données à enregistrer, qui n’ont pas à apparaître dans l’URL.

    <span class="erreurfreq">▷ Erreur fréquente.</span> ne tester que le cas où les *deux* champs sont vides : la condition doit être « l’un *ou* l’autre est vide », sinon une inscription sans prénom (ou sans classe) serait acceptée.
