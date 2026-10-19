# Exercices

<p class="sous-titre">Les réseaux sociaux</p>

!!! consignes "Mode d’emploi"

    - Niveau : ★ échauffement, ★★ classique (niveau bac), ★★★ défi ; les *coups de pouce* et les *corrigés* se déplient sous chaque exercice.

    - <span class="tag">sur papier</span> *signale les exercices à faire sur papier* ; $\blacktriangleright$  *ceux qui demandent une petite recherche ou une manipulation.*

    - Vocabulaire du graphe : **sommet**, **arête**, **degré**, **distance**, **excentricité**, **diamètre**, **rayon**, **centre**.

    - Usage de l’IA, indiqué sur chaque exercice : <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> aucune ; <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> en appui (déboguer, reformuler, vérifier ; la réponse finale est écrite et comprise par vous) ; <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> l’exercice s’appuie sur une réponse d’IA. Voir la charte d’usage de l’IA.

### Reconnaître et comparer les réseaux

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 1</span> — Le bon réseau <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-1 }

<span class="essentiel">• essentiel</span>

<span class="tag">sur papier</span>  Associer chaque réseau à son contenu principal : *Instagram, TikTok, LinkedIn, WhatsApp, YouTube* $\;\leftrightarrow\;$ *vidéos, photos, vidéos courtes, messages privés, contacts professionnels*.

??? pouce "Coup de pouce"

    Relisez la colonne « Contenu principal » du tableau des ordres de grandeur, dans le cours.

??? corrige "Corrigé"

    *Réponses aux questions fermées ; pour les questions ouvertes ou de débat, des pistes attendues (d’autres formulations sont possibles).*

    Activité 1 — Dresser le portrait des réseaux

    1.  Facebook, WhatsApp et Instagram (environ $3$ milliards chacun) $>$ YouTube ($\sim 2{,}5$ milliards) $>$ TikTok ($\sim 1{,}6$ milliard) $>$ Snapchat (près de $1$ milliard) $>$ X (centaines de millions). LinkedIn ne se compare pas directement : il annonce ses *inscrits*, pas ses utilisateurs actifs. Les trois premiers ont le même ordre de grandeur et appartiennent à la même entreprise, **Meta**.

    2.  **YouTube** et **TikTok** (Instagram accepté pour ses vidéos courtes).

    3.  Le chiffre est publié par l’entreprise elle-même et change tous les jours ; il existe des **faux comptes**, des comptes **inactifs**, des personnes qui ont **plusieurs comptes**, et la définition d’« utilisateur actif » varie. On ne peut donc retenir qu’un **ordre de grandeur**.

    4.  Réponse personnelle. Exemples : TikTok, des vidéos courtes et divertissantes, surtout pour un public jeune ; LinkedIn, un réseau professionnel pour trouver un stage ou un emploi.

    Activité 2 — Régler sa confidentialité

    1.  Trois réglages exposent Léa (on en attend trois parmi ceux-ci) : le **compte public** $\to$ le passer en **privé** ; les **commentaires et messages ouverts à tous** $\to$ les limiter à ses **abonnés** ou amis ; la **position ajoutée aux publications** $\to$ **désactiver le partage de la position** ; les **abonnés visibles par tous** $\to$ masquer la liste de ses abonnés.

    2.  Réponse personnelle (ne jamais recopier un mot de passe donné en exemple : publié, il n’est plus secret). Méthode attendue : un mot de passe **long** (au moins $12$ caractères), par exemple une phrase de passe de plusieurs mots sans lien entre eux, avec majuscules, chiffres et symboles, sans **information personnelle** (prénom, date de naissance) et **différent** pour chaque site.

    3.  **Identification** : saisir son adresse e-mail ; taper son pseudo. **Authentification** : entrer un code reçu par SMS ; poser son doigt sur le capteur d’empreinte.

    4.  Débat, pistes attendues : il faut l’**accord** de la personne (droit à l’image, vie privée) ; une fois publiée, la photo **échappe** à son auteur (copies, captures) ; publier sans accord peut **blesser** et, selon les cas, être **puni par la loi**.

    Activité 3 — Suivre l’argent

    1.  La **publicité ciblée**.

    2.  On vend aux annonceurs notre **attention** et nos **données** (le profil qui permet de choisir la publicité la plus susceptible de nous intéresser).

    3.  $2$ milliards $\times\ 40~€ = \mathbf{80}$ **milliards d’euros par an** (ordre de grandeur).

    4.  Plus vous restez, plus l’application peut **afficher de publicités** et collecter de données : elle a donc intérêt à vous retenir (notifications, lecture automatique, fil infini).

    Activité 4 — Mesurer le réseau des amis

    1.  Degrés : Alice $2$, Bilal $3$, Chloé $3$, **David $4$**, Ella $2$, Farid $2$. L’influenceur est **David**.

    2.  Distance Alice–Farid $= \mathbf{3}$ (Alice–Bilal–David–Farid) ; distance Bilal–Ella $= \mathbf{2}$ (Bilal–David–Ella).

    3.  Excentricités : Alice $3$, Bilal $2$, Chloé $2$, David $2$, Ella $3$, Farid $3$.

    4.  **Diamètre $= 3$** (plus grande excentricité) ; **rayon $= 2$** (plus petite) ; **centre** $=$ {Bilal, Chloé, David}.

    5.  Avec les arêtes Alice–Ella et Alice–Farid, toutes les excentricités valent $2$ : le **diamètre passe de $3$ à $2$**.

    Activité 5 — Combien de degrés nous séparent ?

    1.  Réponse personnelle. Idée attendue : deux personnes prises au hasard sont reliées par une **courte chaîne de connaissances** (environ six), même si elles ne se connaissent pas.

    2.  La plus grande distance est le **diamètre**, soit $\mathbf{3}$ (par exemple Alice et Farid) : c’est **moins** que six, car le réseau est tout petit.

    3.  Chaque nouvelle amitié crée un **raccourci** entre deux parties du réseau : les chaînes raccourcissent, donc la distance moyenne **diminue**.

    Activité 6 — Enquêter sur son fil

    1.  Pistes attendues : un algorithme **classe** les contenus selon des signaux (temps passé, « j’aime », partages, comptes suivis…) et place en premier ce qui a le plus de chances de vous **retenir**.

    2.  Réponse personnelle (par exemple : ne plus voir que des vidéos d’un seul type après en avoir regardé quelques-unes).

    3.  Exemples : **suivre des comptes aux avis différents** ; **vérifier** une information avant de la partager ; couper la lecture automatique ; s’abonner à des médias fiables.

    Activité 7 — Ma charte des réseaux

    Production personnelle. Une charte réussie contient par exemple une règle sur la **vie privée** (régler sa confidentialité, ne pas publier d’informations personnelles), une sur l’**esprit critique** (vérifier avant de partager), une contre le **harcèlement** (ne pas insulter, garder les preuves, signaler, soutenir une victime), et par exemple le **respect des autres** (demander l’accord avant de publier une photo) et l’**équilibre** (limiter son temps d’écran).

    Activité 8 — Sobriété numérique

    1.  La vidéo est **stockée** en plusieurs définitions et en plusieurs copies dans des centres de données, tant qu’elle n’est pas supprimée ; surtout, elle est **retransmise à chaque visionnage** : vue un million de fois, elle traverse un million de fois les réseaux.

    2.  Presque toute l’empreinte du téléphone (environ $80$ kg CO<sub>2</sub>e) est émise à la **fabrication**, donc avant qu’on s’en serve. Le garder plus longtemps **répartit** cette empreinte sur plus d’années et **évite** d’en fabriquer un nouveau (par exemple $80$ kg sur $5$ ans au lieu de $2{,}5$ ans : deux fois moins par an).

    3.  Avec la lecture automatique, des vidéos sont téléchargées **sans avoir été choisies** ; en haute qualité, chaque seconde de vidéo contient **plus de données**. Réglages : désactiver la lecture automatique, réduire la qualité vidéo (surtout sur un petit écran).

    4.  Le réseau gagne de l’argent grâce au **temps passé** (plus de publicités vues) : le fil infini et la lecture automatique servent justement à **retenir l’attention**. Les désactiver irait contre son modèle économique ; c’est donc à l’utilisateur de le faire.

    Instagram $\leftrightarrow$ **photos** ; TikTok $\leftrightarrow$ **vidéos courtes** ; LinkedIn $\leftrightarrow$ **contacts professionnels** ; WhatsApp $\leftrightarrow$ **messages privés** ; YouTube $\leftrightarrow$ **vidéos**. *(Beaucoup de réseaux mélangent aujourd’hui plusieurs formats ; on retient ici leur usage *principal* d’origine.)*

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 2</span> — Ordres de grandeur <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-2 }

<span class="tag">sur papier</span>  On rappelle que la population mondiale est d’environ $8$ milliards d’humains.

1.  Un réseau annonce « $3$ milliards d’utilisateurs actifs ». Quelle proportion de l’humanité cela représente-t-il, environ ?

2.  Pourquoi parle-t-on d’un **ordre de grandeur** plutôt que d’un chiffre exact ?

??? pouce "Coup de pouce"

    Une proportion s’obtient en divisant la partie par le tout. Pour la question 2 : ce chiffre est-il le même d’un jour à l’autre, et qui le publie ?

??? corrige "Corrigé"

    **1.** $3$ milliards sur $8$ milliards, soit $\dfrac{3}{8} \approx 0{,}375$ : environ **37 %** de l’humanité (un peu plus d’un tiers).  
    **2.** Le nombre exact d’utilisateurs *change en permanence* (inscriptions, comptes inactifs ou multiples) et n’est pas vérifiable. Un **ordre de grandeur** (« quelques milliards ») suffit pour comparer et raisonner, sans prétendre à une précision illusoire.

### Identité numérique, sécurité

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 3</span> — Identifier ou authentifier ? <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-3 }

<span class="essentiel">• essentiel</span>

<span class="tag">sur papier</span>  Pour chaque action, dire s’il s’agit d’**identification** (annoncer qui l’on est) ou d’**authentification** (prouver que c’est bien soi) :

1.  saisir son identifiant de l’ENT (*prenom.nom*) ;

2.  taper son mot de passe ;

3.  déverrouiller son téléphone par reconnaissance du visage ;

4.  saisir son numéro de téléphone sur la page de connexion d’une messagerie ;

5.  valider, sur son téléphone, la notification « Est-ce bien vous qui essayez de vous connecter ? ».

??? pouce "Coup de pouce"

    Pour chaque action, demandez-vous : est-ce que je dis *qui* je suis, ou est-ce que je *prouve* que c’est bien moi (par quelque chose que je sais, que je possède ou que je suis) ?

??? corrige "Corrigé"

    **a.** identifiant de l’ENT $=$ **identification** (on annonce qui l’on est) ; **b.** mot de passe $=$ **authentification** (on prouve qu’on connaît un secret) ; **c.** reconnaissance du visage $=$ **authentification** (on prouve qui l’on est par ce que l’on est) ; **d.** numéro de téléphone saisi sur la page de connexion $=$ **identification** (il sert ici d’identifiant) ; **e.** validation de la notification $=$ **authentification** (on prouve qu’on possède le téléphone). *En résumé : l’identification *annonce*, l’authentification *prouve*.*

    <span class="erreurfreq">▷ Erreur fréquente.</span> Ranger la notification « Est-ce bien vous ? » (ou un code reçu par SMS) dans l’identification parce qu’on y « dit que c’est soi ». En la validant, on *prouve* qu’on a le téléphone en main : c’est de l’authentification.

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 4</span> — E-réputation <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-4 }

<span class="tag">sur papier</span>  « Rien ne s’efface vraiment sur Internet. » Expliquer cette phrase, puis donner un exemple de situation où votre e-réputation d’aujourd’hui pourrait vous suivre plus tard.

??? pouce "Coup de pouce"

    Une fois une photo ou un message publié, qui d’autre que vous peut y avoir accès ? Que peut-on en faire avant que vous ne le supprimiez ?

??? corrige "Corrigé"

    « Rien ne s’efface vraiment » : une photo, un message ou un commentaire mis en ligne peut être **copié, capturé (*screenshot*), partagé et archivé** par d’autres ; même supprimé de la source, il peut subsister ailleurs. *Exemple :* une publication gênante postée à 15 ans peut être retrouvée des années plus tard par un recruteur, une école ou un employeur, et nuire à une candidature.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 5</span> — Un bon mot de passe <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-5 }

$\blacktriangleright$  Proposer deux mots de passe : un **faible** et un **solide**. Expliquer, pour chacun, ce qui le rend facile ou difficile à deviner (longueur, variété des caractères, mot du dictionnaire, information personnelle…).

??? pouce "Coup de pouce"

    Pensez à ce qu’un pirate essaierait en premier : des mots courants, des prénoms, des dates. Qu’est-ce qui rend un mot de passe long à deviner, même pour un ordinateur ?

??? corrige "Corrigé"

    *Exemple.* Faible : `sofiane2010` — court, contient un **prénom** et une **date de naissance** (informations personnelles faciles à deviner), aucun caractère spécial. Solide : on ne recopie jamais un exemple imprimé (publié, il n’est plus secret), mais on suit une méthode — par exemple une **phrase de passe** de plusieurs mots sans lien entre eux, choisis au hasard, dans laquelle on glisse **majuscules, chiffres et symboles** : elle est **longue**, ne contient **aucune information personnelle** et reste facile à retenir. *Les deux leviers essentiels : la **longueur** et l’**imprévisibilité**.*

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 6</span> — Mes données, mes droits <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-6 }

<span class="essentiel">• essentiel</span>

<span class="tag">sur papier</span>  Inès, 16 ans, habite à Monaco. Elle a un compte sur une application de partage de photos.

1.  Citer trois **données personnelles** que cette application détient sans doute sur elle.

2.  Inès veut savoir quelles données l’application conserve sur elle, puis faire supprimer une ancienne photo. Quel droit exerce-t-elle dans chaque cas ?

3.  L’application ne lui répond pas. À quelle autorité peut-elle s’adresser ? Et si elle habitait à Nice ?

4.  Sa petite sœur, qui a $13$ ans, peut-elle ouvrir seule un compte sur cette application ?

??? pouce "Coup de pouce"

    Relisez dans le cours l’encadré « Vos droits sur vos données » et l’encadré « Et à Monaco ? » : on y trouve les droits, l’âge à partir duquel on décide seul, et l’autorité de chaque pays.

??? corrige "Corrigé"

    **1.** Par exemple : son **nom** ou son pseudo, son **adresse e-mail**, ses **photos**, sa **date de naissance**, sa **localisation**, la liste de ses abonnés.  
    **2.** Savoir quelles données sont conservées : **droit d’accès**. Faire supprimer une photo : **droit d’effacement**.  
    **3.** Résidant à Monaco, elle s’adresse à l’**APDP** (Autorité de protection des données personnelles, loi n° 1.565). Si elle habitait à Nice (France), ce serait la **CNIL** (RGPD et loi Informatique et libertés).  
    **4.** **Non** : en dessous de $15$ ans, il faut aussi l’accord des parents (titulaires de l’autorité parentale), à Monaco comme en France.

### Le modèle économique

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 7</span> — « Si c’est gratuit…» <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-7 }

<span class="essentiel">• essentiel</span>

<span class="tag">sur papier</span>  La plupart des réseaux sont gratuits mais très riches.

1.  Quelle est leur principale source de revenus ?

2.  Compléter : « Si c’est gratuit, c’est que le ……, c’est ……». Qu’est-ce qu’on vend réellement à l’annonceur ?

??? pouce "Coup de pouce"

    Relisez dans le cours la partie « Comment gagnent-ils de l’argent ? » : qui paie le réseau, et en échange de quoi ?

??? corrige "Corrigé"

    **1.** La principale source de revenus est la **publicité ciblée** (et la revente de l’espace publicitaire aux annonceurs).  
    **2.** « Si c’est gratuit, c’est que le **produit**, c’est **vous** ». Ce qu’on vend à l’annonceur, ce sont votre **attention** et vos **données personnelles** (centres d’intérêt, comportements), qui permettent de vous montrer des publicités très ciblées.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 8</span> — Suivre l’argent <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-8 }

<span class="tag">sur papier</span>  Un réseau de partage de vidéos compte $500$ millions d’utilisateurs et rapporte en moyenne $12$ € par utilisateur et par an.

1.  Estimer son **revenu annuel** (ordre de grandeur).

2.  L’application affiche une publicité toutes les $5$ minutes de visionnage. Combien de publicités voit un utilisateur qui la regarde $30$ minutes par jour ? Et $1$ heure par jour ? En déduire, avec l’idée d’« économie de l’attention », pourquoi l’application a intérêt à vous garder le plus longtemps possible.

??? pouce "Coup de pouce"

    Revenu total $=$ nombre d’utilisateurs $\times$ revenu moyen par utilisateur ; gardez le mot « millions » dans le calcul, puis rappelez-vous que $1\,000$ millions font $1$ milliard.

??? corrige "Corrigé"

    **1.** Revenu $\approx 500\,\text{millions} \times 12~\text{€} = 6\,000$ millions d’euros, soit **6 milliards d’euros par an** (ordre de grandeur).  
    **2.** $30 \div 5 = \mathbf{6}$ publicités par jour ; en $1$ heure, $60 \div 5 = \mathbf{12}$ publicités. Le nombre de publicités vues, donc ce que paient les annonceurs, est proportionnel au temps passé : l’application a intérêt à **capter votre attention** le plus longtemps possible (notifications, défilement infini, vidéos qui s’enchaînent). C’est l’**économie de l’attention**.

    <span class="erreurfreq">▷ Erreur fréquente.</span> Écrire « $500 \times 12 = 6\,000$ milliards » : on comptait en *millions*. $6\,000$ millions font $6$ milliards. Un contrôle de vraisemblance aide : un réseau quatre fois plus petit que celui de l’activité du cours, qui rapporte moins par utilisateur, ne peut pas gagner davantage.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 9</span> — Ce que la publicité sait de vous <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-9 }

<span class="tag">sur papier</span>  En une semaine, Hugo a aimé une douzaine de vidéos de football, cherché « crampons pas chers », publié une photo localisée au stade Louis-II et regardé jusqu’au bout trois vidéos de recettes de pâtes.

1.  Quelles informations le réseau peut-il en **déduire** sur Hugo ?

2.  Proposer deux publicités qu’il risque de voir dans son fil la semaine suivante.

3.  Expliquer pourquoi ces informations ont de la valeur pour le réseau.

??? pouce "Coup de pouce"

    Pour chaque action d’Hugo, demandez-vous ce qu’elle révèle : un goût, un besoin d’achat, un lieu de vie ?

??? corrige "Corrigé"

    **1.** Hugo **aime le football** (et le pratique sans doute : il cherche des crampons), il a un **petit budget** (« pas chers »), il fréquente le **stade Louis-II**, donc vit probablement **à Monaco ou à proximité**, et il s’intéresse à la **cuisine**.  
    **2.** Par exemple : des crampons en promotion dans un magasin de sport proche de Monaco ; des billets pour un match de l’AS Monaco ; une marque de pâtes ou un robot de cuisine.  
    **3.** Ces informations permettent de montrer à Hugo des publicités **ciblées**, qui ont plus de chances de le faire cliquer et acheter. Les annonceurs paient donc plus cher pour les afficher : ce qui est vendu, c’est l’**attention** et les **données** d’Hugo.

### Un réseau social, c’est un graphe

Pour les exercices 10 et 11, on étudie le réseau d’amitiés suivant, différent de celui du cours (une arête $=$ « est ami avec ») :

![](../figures/196c1c39eee4a51d.svg){ .tikz loading=lazy }

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 10</span> — Degrés et distances <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-10 }

<span class="essentiel">• essentiel</span>

<span class="tag">sur papier</span> 

1.  Donner le **degré** de chaque personne. Qui est le plus « connecté » ?

2.  Déterminer la **distance** entre Gabin et Kenza, puis entre Kenza et Maël (donner un plus court chemin).

??? pouce "Coup de pouce"

    Le degré d’un sommet est le nombre d’arêtes qui en partent. Pour une distance, cherchez le chemin qui emprunte le moins d’arêtes possible.

??? corrige "Corrigé"

    **1.** Degrés : Gabin $2$, Hana $3$, Ilyes $3$, **Jade $4$**, Kenza $2$, Lucas $3$, Maël $1$. La personne la plus « connectée » est **Jade** (degré $4$).  
    **2.** Distance **Gabin–Kenza** $= \mathbf{3}$ : un plus court chemin est **Gabin–Hana–Jade–Kenza** (ou Gabin–Ilyes–Jade–Kenza). Distance **Kenza–Maël** $= \mathbf{2}$ : chemin **Kenza–Lucas–Maël**.

    <span class="erreurfreq">▷ Erreur fréquente.</span> Compter les personnes du chemin au lieu des arêtes : Gabin–Hana–Jade–Kenza passe par $4$ personnes, mais n’emprunte que $3$ arêtes. La distance vaut $3$.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 11</span> — Diamètre, rayon, centre <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-11 }

<span class="duree">≈ 20 min</span>

<span class="tag">sur papier</span> 

1.  Rappeler ce qu’est l’**excentricité** d’un sommet, puis calculer celle de chaque personne.

2.  En déduire le **diamètre**, le **rayon** et le **centre** du réseau.

3.  Maël devient aussi ami avec Kenza. Le diamètre change-t-il ? Justifier.

??? pouce "Coup de pouce"

    L’excentricité d’une personne : calculez sa distance à chacune des six autres et gardez la plus grande.

??? pouce "Coup de pouce 2 (début de solution)"

    Excentricité de Gabin : distances à Hana $1$, à Ilyes $1$, à Jade $2$, à Kenza $3$, à Lucas $3$, à Maël $4$ ; la plus grande vaut $4$. Faites de même pour les six autres personnes, puis comparez les sept excentricités.

??? corrige "Corrigé"

    **1.** L’**excentricité** d’un sommet est la **plus grande distance** qui le sépare d’un autre sommet du réseau (« à quelle distance est la personne la plus éloignée de moi ? »). Ici :

    |              | Gabin | Hana | Ilyes | Jade | Kenza | Lucas | Maël |
    |:------------:|:-----:|:----:|:-----:|:----:|:-----:|:-----:|:----:|
    | excentricité |  $4$  | $3$  |  $3$  | $2$  |  $3$  |  $3$  | $4$  |

    **2.** Le **diamètre** (plus grande excentricité) vaut $\mathbf{4}$ (Gabin et Maël) ; le **rayon** (plus petite excentricité) vaut $\mathbf{2}$ ; le **centre** (le sommet d’excentricité minimale) est **Jade**.  
    **3.** **Non**, le diamètre reste égal à $\mathbf{4}$. Pour aller de Gabin à Maël, il faut passer par Hana ou Ilyes, puis forcément par Jade (le seul lien entre les deux groupes), puis par Kenza ou Lucas avant d’arriver à Maël : au moins $4$ arêtes, avec ou sans la nouvelle amitié. *Contrairement à l’activité du cours, une nouvelle amitié ne réduit pas toujours le diamètre : il faut qu’elle raccourcisse le chemin entre les deux personnes les plus éloignées.*

    <span class="erreurfreq">▷ Erreur fréquente.</span> Prendre comme excentricité la *plus petite* distance (qui vaut presque toujours $1$) : l’excentricité est la distance à la personne la *plus éloignée*.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 12</span> — Dessiner un réseau <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-12 }

<span class="essentiel">• essentiel</span>

<span class="tag">sur papier</span>  Dans un club, Léo est ami avec Mia et avec Noé ; Mia est aussi amie avec Noé et avec Paul ; Paul est ami avec Rose. Personne d’autre n’est ami.

1.  Dessiner le graphe de ce réseau.

2.  Donner le degré de chaque personne.

3.  Déterminer la distance entre Léo et Rose, puis entre Noé et Paul.

??? pouce "Coup de pouce"

    Placez d’abord les cinq sommets, puis tracez une arête pour chaque relation « est ami avec » de l’énoncé (attention, il y en a cinq).

??? corrige "Corrigé"

    **1.** Cinq sommets et cinq arêtes : Léo–Mia, Léo–Noé, Mia–Noé, Mia–Paul, Paul–Rose.

    ![](../figures/0b0c45e4f516f088.svg){ .tikz loading=lazy }

    **2.** Degrés : Léo $2$, **Mia $3$**, Noé $2$, Paul $2$, Rose $1$.  
    **3.** Distance **Léo–Rose** $= \mathbf{3}$ (Léo–Mia–Paul–Rose) ; distance **Noé–Paul** $= \mathbf{2}$ (Noé–Mia–Paul).

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 13</span> — Fabriquer un diamètre <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-13 }

<span class="duree">≈ 15 min</span>

<span class="tag">sur papier</span>  On dispose de cinq personnes. Dans chaque réseau demandé, on doit pouvoir aller de n’importe qui à n’importe qui en suivant les arêtes.

1.  Dessiner un réseau de ces cinq personnes dont le **diamètre** vaut $4$. Combien d’arêtes compte-t-il ?

2.  Dessiner un réseau de ces cinq personnes dont le diamètre vaut $1$. Combien d’arêtes compte-t-il ?

3.  Quel est le **centre** du réseau de la question 1 ?

??? pouce "Coup de pouce"

    Diamètre $4$ : deux personnes doivent être séparées par $4$ arêtes, avec seulement cinq personnes en tout. Diamètre $1$ : que signifie « être à distance $1$ de tout le monde » ?

??? pouce "Coup de pouce 2 (début de solution)"

    Question 1 : placez les cinq personnes « en file indienne », chacune amie seulement avec ses voisines. Question 2 : chacun est ami avec les quatre autres ; attention à ne pas compter deux fois la même arête.

??? corrige "Corrigé"

    **1.** On place les cinq personnes en « file indienne » : A–B–C–D–E. Les deux extrémités A et E sont à distance $4$, et aucune distance n’est plus grande : le diamètre vaut $\mathbf{4}$. Ce réseau compte $\mathbf{4}$ arêtes. (C’est d’ailleurs le seul dessin possible : avec cinq personnes, une distance de $4$ oblige à les aligner toutes.)

    ![](../figures/d00d4c0a341b4da9.svg){ .tikz loading=lazy }

    **2.** Diamètre $1$ : toutes les distances valent $1$, donc **chacun est ami avec tous les autres**. Chaque personne a $4$ amis, ce qui fait $5 \times 4 = 20$ « bouts » d’arêtes ; chaque arête ayant deux bouts, il y a $20 / 2 = \mathbf{10}$ arêtes.  
    **3.** Excentricités dans la file : A $4$, B $3$, **C $2$**, D $3$, E $4$. Le rayon vaut $2$ et le **centre** est la personne du milieu, **C**.

### Petit monde et recommandation

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 14</span> — Six degrés de séparation <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-14 }

<span class="tag">sur papier</span> 

1.  Expliquer, avec vos propres mots, l’expression « six degrés de séparation » (expérience de Milgram, 1967).

2.  Sur Facebook (vers 2016), la distance moyenne mesurée était d’environ $3{,}5$. Que peut-on en conclure sur l’évolution du « petit monde » ?

??? pouce "Coup de pouce"

    Comparez $3{,}5$ avec les « cinq ou six intermédiaires » de l’expérience de Milgram. Les chaînes de connaissances se sont-elles allongées ou raccourcies, et pourquoi ?

??? corrige "Corrigé"

    **1.** L’idée : deux personnes prises au hasard sur Terre seraient reliées par une **chaîne d’environ six connaissances** (« l’ami d’un ami d’un ami…»). C’est le phénomène du **petit monde**, suggéré par l’expérience de **Milgram** (1967).  
    **2.** Une distance moyenne d’environ $3{,}5$ sur Facebook montre que le monde numérique est devenu un « **petit monde** » *encore plus resserré* : les réseaux sociaux raccourcissent les chaînes de connaissances (bien en dessous de six).

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 15</span> — Qui choisit ce que je vois ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-15 }

<span class="essentiel">• essentiel</span>

<span class="tag">sur papier</span> 

1.  Qu’est-ce qu’un **algorithme de recommandation** ? Quel est son but ?

2.  Expliquer ce qu’est une **bulle de filtres**, et proposer un geste simple pour en sortir.

??? pouce "Coup de pouce"

    Relisez la partie du cours « Qui choisit ce que vous voyez ? ». Pour le but de l’algorithme, repensez au modèle économique : plus vous restez, plus…

??? corrige "Corrigé"

    **1.** Un **algorithme de recommandation** choisit et ordonne les contenus qui vous sont montrés (fil d’actualité, vidéos suggérées) à partir de vos actions passées. Son but : **maximiser votre engagement** (temps passé, clics, likes).  
    **2.** Une **bulle de filtres** : à force de vous montrer ce qui vous plaît déjà, l’algorithme vous enferme dans des contenus **similaires** et vous cache les autres points de vue. Geste simple pour en sortir : **s’abonner volontairement à des sources variées** (voire opposées), varier ses recherches, ou désactiver la personnalisation.

### <span class="stars" title="Niveau 3 sur 3">★★★</span> <span class="exo-num">Exercice 16</span> — Les amis de mes amis <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-02-16 }

<span class="duree">≈ 15 min</span>

<span class="tag">sur papier</span>  Un réseau propose à chacun des « amis suggérés » : les personnes situées à **distance $2$**, en commençant par celles avec qui l’on a le plus d’**amis en commun**. On reprend le graphe d’amitiés de la section IV du cours.

1.  Quelles personnes sont à distance $2$ d’Alice ? Combien d’amis en commun a-t-elle avec chacune ? Qui lui sera suggéré en premier ?

2.  Même question pour Ella.

3.  Expliquer pourquoi ce type de suggestion a tendance à refermer chaque groupe sur lui-même (faire le lien avec la bulle de filtres).

??? pouce "Coup de pouce"

    Être à distance $2$, c’est ne pas être ami direct, mais être ami d’un de ses amis. Pour les amis en commun, écrivez la liste des amis de chacun et cherchez les noms présents dans les deux listes.

??? pouce "Coup de pouce 2 (début de solution)"

    Amis d’Alice : Bilal et Chloé. Amis de Bilal : Alice, Chloé, David ; amis de Chloé : Alice, Bilal, David. Dans ces listes, qui n’est ni Alice, ni déjà son ami ?

??? corrige "Corrigé"

    **1.** Alice a pour amis Bilal et Chloé. Leurs autres amis : David seulement. La seule personne à distance $2$ d’Alice est donc **David**, avec qui elle a **deux** amis en commun (Bilal et Chloé) : David lui est suggéré en premier.  
    **2.** Ella a pour amis David et Farid. Les amis de David qui ne sont pas déjà amis d’Ella sont Bilal et Chloé (Farid, lui, n’a pas d’autre ami). À distance $2$ d’Ella : **Bilal** et **Chloé**, avec chacun **un seul** ami en commun (David) : ils sont à égalité. Alice est à distance $3$ d’Ella : elle n’est pas suggérée.  
    **3.** On vous propose surtout des personnes **déjà proches de vos amis**, qui fréquentent les mêmes groupes et partagent souvent les mêmes goûts et avis. Chaque groupe se resserre, on rencontre rarement des personnes vraiment différentes : comme la bulle de filtres, ce mécanisme rétrécit la variété de ce que l’on voit (ici, des *personnes*).

### <span class="stars" title="Niveau 1 sur 3">★</span> <span class="exo-num">Exercice 17</span> — Citoyen des réseaux <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-17 }

<span class="tag">sur papier</span>  Face à une situation de cyberharcèlement, citer trois bons réflexes et donner un numéro d’aide joignable à Monaco.

??? pouce "Coup de pouce"

    Relisez la partie du cours « Bien vivre avec les réseaux sociaux » : elle décrit quoi faire (et ne pas faire) face au harcèlement.

??? corrige "Corrigé"

    Face au cyberharcèlement : **(1)** ne pas répondre ni « rendre les coups », **conserver les preuves** (captures d’écran) ; **(2)** **signaler** et bloquer l’auteur sur la plateforme ; **(3)** **en parler** à un adulte de confiance (parent, professeur, CPE). À Monaco, la ligne d’écoute du Gouvernement contre le harcèlement, y compris en ligne, est joignable au **98 98 96 96** (24 h/24) ; le service français **3018** (violences numériques, gratuit et anonyme) répond aussi par tchat avec son application.

### Impact environnemental

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 18</span> — Le coût d’un smartphone <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-18 }

<span class="tag">sur papier</span>  Sami filme beaucoup de vidéos en 4K pour les publier sur un réseau social. Son téléphone est presque plein : il ne lui reste que $20$ Go libres. On suppose qu’une minute de vidéo en 4K occupe environ $400$ Mo ($1$ Go $= 1\,000$ Mo).

1.  Combien de minutes de vidéo en 4K Sami peut-il encore filmer ?

2.  Sami pense acheter un téléphone neuf avec plus de mémoire. D’après le Document 6 du cours (on y reviendra au thème *Objets connectés*), un smartphone émet environ $80$ kg CO<sub>2</sub>e sur sa vie, presque tout à sa **fabrication**. Proposer deux solutions plutôt que d’acheter un téléphone neuf.

3.  Sami publie une vidéo de $50$ Mo, qui est vue $1$ million de fois. Quelle quantité de données le réseau social doit-il transporter pour ces visionnages ? Donner le résultat en téraoctets ($1$ To $= 10^{6}$ Mo).

4.  Même après avoir libéré son téléphone, Sami garde ses vidéos « dans le nuage ». Où sont-elles stockées en réalité, et pourquoi ce stockage a-t-il aussi un coût environnemental ?

??? pouce "Coup de pouce"

    Question 1 : convertissez d’abord les $20$ Go en mégaoctets. Question 3 : chaque visionnage renvoie toute la vidéo ; multipliez la taille du fichier par le nombre de vues.

??? corrige "Corrigé"

    **1.** $20$ Go $= 20\,000$ Mo, et $20\,000 \div 400 = \mathbf{50}$ **minutes** de vidéo en 4K.  
    **2.** Par exemple : **trier et supprimer** les vidéos ratées ou en double ; filmer en **définition plus basse** (1080p au lieu de 4K, bien suffisant sur un petit écran) ; transférer ses vidéos sur un ordinateur ou un disque dur ; si la mémoire manque vraiment, choisir un téléphone **reconditionné**. Acheter du neuf ajoute environ $80$ kg CO<sub>2</sub>e, émis presque entièrement à la fabrication.  
    **3.** $50 \times 1\,000\,000 = 50\,000\,000$ Mo $= 50 \times 10^{6}$ Mo, soit $\mathbf{50}$ **To** transportés par les réseaux — un million de fois la taille du fichier.  
    **4.** « Le nuage » est fait de **serveurs** rangés dans des **centres de données** : ils fonctionnent jour et nuit, doivent être fabriqués, alimentés en électricité et refroidis, et les fichiers y sont souvent conservés en plusieurs copies. Stocker des vidéos qu’on ne regarde plus a donc un coût, même si on ne le voit pas.

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 19</span> — Haute ou basse définition ? <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-19 }

<span class="tag">sur papier</span>  On admet qu’une heure de vidéo en ligne échange environ $3$ Go de données en **haute définition** et environ $1$ Go en **définition standard** (ordres de grandeur, voir le document du cours). Lina regarde $2$ heures de vidéos par jour sur son téléphone.

1.  Quelle quantité de données échange-t-elle en une semaine en haute définition ? En définition standard ?

2.  Combien de fois moins de données consomme-t-elle en définition standard ?

3.  Sur un petit écran de téléphone, la différence de qualité se voit peu. Quel conseil donner à Lina ? Pourquoi est-ce bon pour l’environnement ?

??? pouce "Coup de pouce"

    Calculez d’abord le nombre d’heures de vidéo regardées en une semaine, puis multipliez par la quantité de données échangée en une heure.

??? corrige "Corrigé"

    **1.** En une semaine : $2 \times 7 = 14$ heures de vidéo. Haute définition : $14 \times 3 = \mathbf{42}$ **Go** ; définition standard : $14 \times 1 = \mathbf{14}$ **Go**.  
    **2.** $42 \div 14 = 3$ : **trois fois moins** de données en définition standard.  
    **3.** Conseil : régler la qualité vidéo sur la **définition standard** (ou « économie de données ») et désactiver la lecture automatique. Moins de données échangées, c’est moins de sollicitation des **réseaux** et des **centres de données**, donc moins d’énergie consommée ; cela préserve aussi son forfait.

### Critiquer une réponse d’IA

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 20</span> — Une distance calculée par un assistant <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> { #ex-02-20 }

<span class="tag">sur papier</span>  Un élève a décrit à un assistant d’IA le graphe d’amitiés de la section IV du cours et lui a demandé : « Quelle est la distance entre Alice et Farid ? » Voici la réponse obtenue :

> Alice et Farid ne sont pas amis directement. Pour aller de l’un à l’autre, il faut passer par David, le sommet le plus connecté du réseau (degré 4). Un plus court chemin est Alice – Bilal – David – Farid (on peut aussi passer par Chloé à la place de Bilal). Ce chemin passe par quatre personnes : la distance entre Alice et Farid est donc de 4. À titre de comparaison, Ella et Farid sont amis, donc à distance 1.

1.  La réponse est-elle correcte ? Vérifier sur le graphe et relire la définition de la distance dans le cours.

2.  Localiser et corriger l’erreur.

    ??? pouce "Coup de pouce"

        Recomptez sur le graphe en suivant mot à mot la définition de la longueur d’une chaîne donnée dans le cours.

3.  Quelle vérification simple, faite *avant* de faire confiance à cette réponse, aurait suffi à détecter l’erreur ?

??? corrige "Corrigé"

    **1.** Non. Le chemin proposé (Alice–Bilal–David–Farid) est bien un plus court chemin, David a bien le degré $4$ et Ella–Farid sont bien à distance $1$. Mais, d’après le cours, la longueur d’un chemin est « le nombre d’**arêtes** empruntées », et la distance est la longueur du plus court chemin : ce chemin compte $\mathbf{3}$ arêtes, pas $4$.  
    **2.** L’assistant a compté les **personnes** (sommets) au lieu des **liens** (arêtes) : un chemin qui passe par $4$ sommets comporte $3$ arêtes. La distance Alice–Farid vaut $\mathbf{3}$.  
    **3.** Tester la règle sur un cas évident : Ella et Farid, amis directs, sont « à distance 1 » alors que leur chemin passe par *deux* personnes. La façon de compter de l’assistant se contredit donc elle-même en deux phrases.

### Python au service du thème

### <span class="stars" title="Niveau 2 sur 3">★★</span> <span class="exo-num">Exercice 21</span> — Python au service du thème — l’économie de l’attention <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> { #ex-02-21 }

$\blacktriangleright$  En Python (Spyder ou Basthon). Un réseau social affiche une publicité toutes les $4$ minutes de visionnage : un utilisateur qui regarde $10$ minutes voit donc $2$ publicités (la troisième n’arrive qu’au bout de $12$ minutes).

1.  Écrire une fonction `revenu(utilisateurs, revenu_par_utilisateur)` qui renvoie le revenu annuel du réseau, en euros. La tester avec les données de l’exercice « Suivre l’argent » : on doit retrouver $6$ milliards d’euros.

2.  Écrire une fonction `nb_pubs(minutes)` qui renvoie le nombre de publicités vues en `minutes` minutes de visionnage. Que doivent renvoyer `nb_pubs(10)`, `nb_pubs(30)` et `nb_pubs(60)` ? Vérifier sur machine.

3.  À l’aide d’une boucle `for`, afficher le nombre de publicités vues **en un an** ($365$ jours) par un utilisateur qui regarde $30$, $60$, $90$, puis $120$ minutes par jour. Expliquer, avec l’économie de l’attention, pourquoi le réseau cherche à vous garder le plus longtemps possible.

??? pouce "Coup de pouce"

    Question 2 : combien de « tranches » complètes de $4$ minutes y a-t-il dans `minutes` ? Cherchez, dans le chapitre *Les bases de Python*, l’opérateur qui donne le quotient d’une division entière.

??? pouce "Coup de pouce 2 (début de solution)"

    Question 3 : avec `for i in range(1, 5):`, la variable `i` prend les valeurs $1$, $2$, $3$, $4$ ; la durée quotidienne vaut alors `30 * i`. Il reste à multiplier le nombre de publicités d’une journée par $365$.

??? corrige "Corrigé"

    **1.** Le revenu annuel est le produit du nombre d’utilisateurs par le revenu moyen de chacun :

    ```python
    def revenu(utilisateurs, revenu_par_utilisateur):
        return utilisateurs * revenu_par_utilisateur

    print(revenu(500000000, 12))   # 6000000000
    ```

    On retrouve $6\,000\,000\,000$ €, soit $6$ milliards d’euros, comme à l’exercice « Suivre l’argent ».  
    **2.** Le nombre de publicités est le nombre de tranches *complètes* de $4$ minutes : c’est le quotient de la division entière par $4$, `minutes // 4`.

    ```python
    def nb_pubs(minutes):
        return minutes // 4

    print(nb_pubs(10))   # 2
    print(nb_pubs(30))   # 7
    print(nb_pubs(60))   # 15
    ```

    **3.** La variable `i` prend les valeurs $1$ à $4$ et la durée quotidienne vaut `30 * i` :

    ```python
    for i in range(1, 5):
        minutes = 30 * i
        print(f"{minutes} min par jour : {nb_pubs(minutes) * 365} publicites par an")
    ```

    Le programme affiche :

    ```text
    30 min par jour : 2555 publicites par an
    60 min par jour : 5475 publicites par an
    90 min par jour : 8030 publicites par an
    120 min par jour : 10950 publicites par an
    ```

    Chaque publicité affichée est payée par un annonceur : plus vous restez, plus le réseau affiche de publicités et plus il gagne d’argent. C’est l’**économie de l’attention** : vidéos qui s’enchaînent, défilement infini et notifications servent à allonger ce temps.

    <span class="erreurfreq">▷ Erreur fréquente.</span> Écrire `minutes / 4` : la division `/` donne `7.5` publicités pour $30$ minutes, un nombre qui n’a pas de sens ici. La division entière `//` ne compte que les tranches de $4$ minutes *terminées*.
