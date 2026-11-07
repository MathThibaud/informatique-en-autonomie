# Lexique

*Les définitions sont résumées ; le renvoi (chapitre et page, cliquable) mène à la définition complète dans le cours. Les mots du langage Python sont regroupés à part, en fin de lexique.*

### A

**Accumulateur** — Variable initialisée avant une boucle puis mise à jour à chaque tour (somme, compteur…) ; motif de base de tout parcours. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-accumulateur01))*

**Accusé de réception** — Petit message de confirmation (ACK) renvoyé par le récepteur ; sans accusé au bout d’un délai, l’émetteur considère le paquet perdu et le renvoie. *(ch. 10, [voir le cours](10-le-web-reseaux-et-interactions-homme-mac/cours.md#lex-ack10))*

**Actionneur** — Dispositif qui reçoit un ordre numérique et agit sur le monde physique (une sortie) : moteur, lampe, haut-parleur…*(ch. 9, [voir le cours](09-architecture-des-ordinateurs-et-systemes/cours.md#lex-actionneur09))*

**Adresse IP** — Numéro d’une machine sur le réseau ; en IPv4, quatre nombres de 0 à 255, comme `193.51.208.14`. L’équivalent d’une adresse postale. *(ch. 10, [voir le cours](10-le-web-reseaux-et-interactions-homme-mac/cours.md#lex-ip10))*

**Affectation** — Instruction `nom = expression` (« reçoit ») : Python évalue d’abord la partie droite, puis range cette valeur dans la variable nommée à gauche. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-affectation01))*

**Algorithme** — Méthode : suite finie et non ambiguë d’étapes qui, à partir de données, produit un résultat. Le mot vient du savant persan al-Khwârizmî. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-algorithme01))*

**Algorithme glouton** — Stratégie qui construit la solution morceau par morceau, en faisant à chaque étape le choix qui paraît le meilleur sur le moment, sans jamais revenir en arrière. *(ch. 11, [voir le cours](11-les-algorithmes-gloutons/cours.md#lex-glouton11))*

**Alias** — Deux noms qui désignent le même objet : après `b = a`, modifier le tableau via `b` se voit via `a`. Affecter un tableau ne le copie pas. *(ch. 3, [voir le cours](03-les-types-construits/cours.md#lex-alias03))*

**Apprentissage automatique** — Plutôt que de programmer toutes les règles, on montre des exemples à la machine pour qu’elle apprenne à généraliser (*machine learning*). *(ch. 12, [voir le cours](12-les-k-plus-proches-voisins/cours.md#lex-apprentissage12))*

**Arborescence, racine** — Organisation des fichiers et répertoires en arbre ; sous Linux, tout part de la racine, notée `/`. *(ch. 9, [voir le cours](09-architecture-des-ordinateurs-et-systemes/cours.md#lex-arborescence09))*

**Argument** — Valeur fournie en entrée à une fonction lors de son appel, par exemple `3` et `4` dans `aire_rectangle(3, 4)`. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-argument01))*

**ASCII** — Table de 1963 qui associe à chaque caractère un numéro de 0 à 127 ; chaque caractère tient sur 7 bits, sans lettres accentuées. *(ch. 2, [voir le cours](02-le-binaire-et-l-ecriture-des-nombres/cours.md#lex-ascii02))*

**Assembleur** — Écriture du langage machine avec des abréviations lisibles (`LDA`, `ADD`…) : une instruction assembleur correspond à une instruction machine. *(ch. 9, [voir le cours](09-architecture-des-ordinateurs-et-systemes/cours.md#lex-assembleur09))*

### B

**Balise** — Marque qui encadre un contenu HTML : une balise ouvrante `<p>` et une balise fermante `</p>` ; certaines, comme `<img>`, n’ont pas de fermante. *(ch. 10, [voir le cours](10-le-web-reseaux-et-interactions-homme-mac/cours.md#lex-balise10))*

**Bibliothèque (module)** — Ensemble de fonctions déjà écrites et testées, que l’on charge avec `import` ; on apprend à lire sa documentation plutôt qu’à la connaître par cœur. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-bibliotheque01))*

**Binaire (base 2)** — Écriture des nombres avec deux chiffres, `0` et `1`, chaque rang pesant une puissance de 2 : c’est ainsi que la machine représente toute information. *(ch. 2, [voir le cours](02-le-binaire-et-l-ecriture-des-nombres/cours.md#lex-binaire02))*

**Bit** — Plus petite information (*binary digit*) : un `0` ou un `1`, deux états physiques faciles à distinguer pour un transistor. *(ch. 2, [voir le cours](02-le-binaire-et-l-ecriture-des-nombres/cours.md#lex-bit02))*

**Boucle bornée** — Boucle `for`, utilisée quand on connaît à l’avance le nombre de répétitions. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-bouclebornee01))*

**Boucle non bornée** — Boucle `while`, qui répète son bloc tant qu’une condition reste vraie, quand on ne sait pas à l’avance combien de tours il faudra. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-bouclenonbornee01))*

### C

**Capteur** — Dispositif qui mesure une grandeur du monde physique et la transforme en valeur numérique entrant dans la machine (une entrée). *(ch. 9, [voir le cours](09-architecture-des-ordinateurs-et-systemes/cours.md#lex-capteur09))*

**Chaîne de caractères** — Texte (type `str`) : suite de caractères numérotés à partir de 0, écrite entre guillemets. Une chaîne est immuable. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-chaine01))*

**Champion (maximum, minimum)** — Recherche du maximum : on initialise `m` avec `t[0]` puis on le remplace dès qu’un élément est plus grand ; `m` reste le maximum des éléments déjà vus. *(ch. 4, [voir le cours](04-algorithmique-le-parcours-sequentiel/cours.md#lex-champion04))*

**Charabia (mojibake)** — Texte illisible (« cafÃ© ») obtenu quand on relit un fichier avec un autre encodage que celui qui a servi à l’écrire. *(ch. 2, [voir le cours](02-le-binaire-et-l-ecriture-des-nombres/cours.md#lex-mojibake02))*

**Chemin absolu, chemin relatif** — Emplacement d’un fichier : un chemin absolu part de la racine et commence par `/` ; un chemin relatif part du répertoire courant (`../Images/logo.png`). *(ch. 9, [voir le cours](09-architecture-des-ordinateurs-et-systemes/cours.md#lex-chemin09))*

**`chmod`** — Commande qui modifie les droits d’un fichier, par lettres (`chmod o-r`) ou en chiffres : `chmod 754 fichier`, chaque chiffre codant en binaire les trois droits. *(ch. 9, [voir le cours](09-architecture-des-ordinateurs-et-systemes/cours.md#lex-chmod09))*

**Classe (étiquette)** — Catégorie à laquelle appartient un individu (par exemple l’espèce d’une fleur), connue pour les exemples et à prédire pour un nouvel individu. *(ch. 12, [voir le cours](12-les-k-plus-proches-voisins/cours.md#lex-classe12))*

**Classification supervisée** — À partir d’exemples déjà étiquetés (descripteurs et classe connus), prédire la classe d’un nouvel individu dont on ne connaît que les descripteurs. *(ch. 12, [voir le cours](12-les-k-plus-proches-voisins/cours.md#lex-supervise12))*

**Clé (de dictionnaire)** — Étiquette choisie qui donne accès à une valeur d’un dictionnaire. Les clés sont uniques et immuables (souvent `str`, `int` ou `tuple`). *(ch. 3, [voir le cours](03-les-types-construits/cours.md#lex-cle03))*

**Client-serveur** — Organisation des échanges où des machines clientes demandent des ressources à une machine serveur qui les fournit : c’est le modèle du Web. *(ch. 10, [voir le cours](10-le-web-reseaux-et-interactions-homme-mac/cours.md#lex-clientserveur10))*

**Compilateur, langage compilé** — Un langage compilé (comme C) est traduit une fois pour toutes, avant l’exécution, par un compilateur, qui produit un fichier exécutable. *(ch. 5, [voir le cours](05-specifier-et-mettre-au-point-ses-program/cours.md#lex-compilateur05))*

**Complément à deux** — Codage des entiers relatifs sur $n$ bits : pour coder $-x$, on écrit $x$ en binaire, on inverse tous les bits et on ajoute 1. L’addition ordinaire reste juste. *(ch. 2, [voir le cours](02-le-binaire-et-l-ecriture-des-nombres/cours.md#lex-complement02))*

**Compteur de programme** — Registre qui contient l’adresse de la prochaine instruction ; il avance d’un cran à chaque cycle, sauf si une instruction de saut le modifie. *(ch. 9, [voir le cours](09-architecture-des-ordinateurs-et-systemes/cours.md#lex-compteurprog09))*

**Concaténation** — Mise bout à bout de deux chaînes ou de deux tableaux avec `+` ; elle crée un nouvel objet sans modifier l’original. *(ch. 3, [voir le cours](03-les-types-construits/cours.md#lex-concatenation03))*

**Condition** — Expression dont la valeur est un booléen (`True` ou `False`), construite avec des opérateurs de comparaison et combinée avec `and`, `or`, `not`. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-condition01))*

**Construction par compréhension** — Écriture concise qui fabrique un tableau à partir d’un itérable : `[expression for x in itérable if condition]`, le filtre `if` étant facultatif. *(ch. 3, [voir le cours](03-les-types-construits/cours.md#lex-comprehension03))*

**Cookie** — Petite information que le serveur demande au navigateur de garder ; le navigateur la mémorise et la retransmet automatiquement à chaque requête vers le même site. *(ch. 10, [voir le cours](10-le-web-reseaux-et-interactions-homme-mac/cours.md#lex-cookie10))*

**Copie (d’un tableau)** — Nouvel objet indépendant, obtenu en reconstruisant le tableau : `[x for x in a]` ou `a[:]`. Pour un tableau de tableaux, il faut recopier chaque ligne. *(ch. 3, [voir le cours](03-les-types-construits/cours.md#lex-copie03))*

**Correction (d’un algorithme)** — Propriété d’un algorithme qui donne le résultat attendu ; on la prouve par un invariant de boucle (alors que le variant prouve la terminaison). *(ch. 4, [voir le cours](04-algorithmique-le-parcours-sequentiel/cours.md#lex-correction04))*

**Côté client, côté serveur** — Côté client, le code (JavaScript) s’exécute sur la machine de l’utilisateur après réception de la page ; côté serveur, sur la machine distante (PHP, Python…). *(ch. 10, [voir le cours](10-le-web-reseaux-et-interactions-homme-mac/cours.md#lex-client10))*

**Coût d’un algorithme** — Nombre d’opérations élémentaires qu’effectue un algorithme, exprimé en fonction de la taille `n` des données. *(ch. 4, [voir le cours](04-algorithmique-le-parcours-sequentiel/cours.md#lex-cout04))*

**Coût linéaire** — Coût proportionnel à la taille `n` des données : c’est celui d’un parcours simple. Doubler `n` double le temps. *(ch. 4, [voir le cours](04-algorithmique-le-parcours-sequentiel/cours.md#lex-lineaire04))*

**Coût logarithmique** — Coût de l’ordre de $\log_2 n$ : celui de la dichotomie, qui fait au plus $\lfloor \log_2 n \rfloor + 1$ tours. Doubler `n` n’ajoute qu’une étape. *(ch. 7, [voir le cours](07-la-recherche-dichotomique/cours.md#lex-logarithmique07))*

**Coût quadratique** — Coût proportionnel à $n^2$, typique d’une boucle dans une boucle : doubler `n` multiplie le temps par 4. C’est le coût des tris par sélection et par insertion. *(ch. 4, [voir le cours](04-algorithmique-le-parcours-sequentiel/cours.md#lex-quadratique04) ; ch. 6, [voir le cours](06-les-algorithmes-de-tri/cours.md#lex-quadratique06))*

**`cp`, `mv`, `rm` (Linux)** — Commandes : `cp` copie un fichier, `mv` le déplace ou le renomme, `rm` le supprime définitivement (`rm -r` : un répertoire et son contenu). *(ch. 9, [voir le cours](09-architecture-des-ordinateurs-et-systemes/cours.md#lex-cp09))*

**CSS** — Langage qui décrit la présentation d’une page (couleurs, tailles, polices, disposition) ; il sépare la forme (CSS) du fond (HTML). *(ch. 10, [voir le cours](10-le-web-reseaux-et-interactions-homme-mac/cours.md#lex-css10))*

**CSV** — Fichier texte (*Comma-Separated Values*) qui représente une table : la première ligne donne les descripteurs, chaque ligne suivante un enregistrement, les valeurs étant séparées par un séparateur (virgule, point-virgule). *(ch. 8, [voir le cours](08-les-donnees-en-tables/cours.md#lex-csv08))*

**Cycle d’exécution** — Boucle que répète sans fin le processeur : chercher l’instruction en mémoire, la décoder, l’exécuter. *(ch. 9, [voir le cours](09-architecture-des-ordinateurs-et-systemes/cours.md#lex-cycle09))*

### D

**Déboguer** — Localiser et corriger une erreur : dérouler le programme à la main, placer des affichages (`print`), puis les retirer en gardant les tests. *(ch. 5, [voir le cours](05-specifier-et-mettre-au-point-ses-program/cours.md#lex-deboguer05))*

**Demi-additionneur** — Circuit qui additionne deux bits : la somme vaut $a$ xor $b$, la retenue vaut $a$ et $b$. *(ch. 2, [voir le cours](02-le-binaire-et-l-ecriture-des-nombres/cours.md#lex-demiadd02))*

**Dépassement de capacité** — Résultat trop grand pour le nombre de bits disponibles : il « déborde » et l’on obtient une valeur fausse (en Python, les entiers n’ont pas cette limite). *(ch. 2, [voir le cours](02-le-binaire-et-l-ecriture-des-nombres/cours.md#lex-depassement02))*

**Descripteur** — Nom d’une colonne d’une table (on dit aussi attribut) : ce qu’on renseigne pour chaque individu, comme `prenom` ou `annee`. *(ch. 8, [voir le cours](08-les-donnees-en-tables/cours.md#lex-descripteur08) ; ch. 12, [voir le cours](12-les-k-plus-proches-voisins/cours.md#lex-descripteur12))*

**Dictionnaire (`dict`)** — Ensemble de couples clé $\to$ valeur, écrit entre accolades ; on accède à une valeur par sa clé, et non par un indice. *(ch. 3, [voir le cours](03-les-types-construits/cours.md#lex-dictionnaire03))*

**Distance euclidienne** — Entre deux individus décrits par $p$ descripteurs : racine carrée de la somme des carrés des écarts, descripteur par descripteur (généralisation de Pythagore). *(ch. 12, [voir le cours](12-les-k-plus-proches-voisins/cours.md#lex-distance12))*

**DNS** — Annuaire du réseau (*Domain Name System*) : il traduit un nom de domaine, comme `www.lycee.mc`, en adresse IP. *(ch. 10, [voir le cours](10-le-web-reseaux-et-interactions-homme-mac/cours.md#lex-dns10))*

**DOM** — Arbre formé par les balises emboîtées d’une page (*Document Object Model*), construit en mémoire par le navigateur et modifiable en JavaScript. *(ch. 10, [voir le cours](10-le-web-reseaux-et-interactions-homme-mac/cours.md#lex-dom10))*

**Domaine de valeurs** — Ensemble des valeurs que peut prendre un descripteur ; pour une jointure, les deux descripteurs doivent prendre leurs valeurs dans le même domaine. *(ch. 8, [voir le cours](08-les-donnees-en-tables/cours.md#lex-domaine08))*

**Doublon** — Même fiche présente deux fois dans une table, erreur de saisie fréquente ; on la repère par un parcours qui mémorise les identifiants déjà rencontrés. *(ch. 8, [voir le cours](08-les-donnees-en-tables/cours.md#lex-doublon08))*

**Droits d’accès** — Permissions d’un fichier : lecture (`r`), écriture (`w`), exécution (`x`), pour trois catégories : propriétaire (`u`), groupe (`g`), autres (`o`). *(ch. 9, [voir le cours](09-architecture-des-ordinateurs-et-systemes/cours.md#lex-droits09))*

### E

**Élément neutre** — Valeur d’initialisation d’un accumulateur qui ne change pas le résultat : `0` pour une somme, `1` pour un produit, `""` pour du texte, `[]` pour un tableau. *(ch. 4, [voir le cours](04-algorithmique-le-parcours-sequentiel/cours.md#lex-neutre04))*

**Encapsulation** — À l’envoi, chaque couche de protocoles (application, transport, réseau, liaison) ajoute son en-tête devant les données, comme des enveloppes dans des enveloppes. *(ch. 10, [voir le cours](10-le-web-reseaux-et-interactions-homme-mac/cours.md#lex-encapsulation10))*

**Encodage** — Règle qui fait correspondre caractères et octets (ASCII, Latin-1, UTF-8…). Encoder : caractères vers octets ; décoder : octets vers caractères. *(ch. 2, [voir le cours](02-le-binaire-et-l-ecriture-des-nombres/cours.md#lex-encodage02) ; ch. 8, [voir le cours](08-les-donnees-en-tables/cours.md#lex-encodage08))*

**Enregistrement** — Ligne d’une table (une fiche) : une valeur pour chaque descripteur, c’est-à-dire un p-uplet nommé ; en Python, un dictionnaire. *(ch. 8, [voir le cours](08-les-donnees-en-tables/cours.md#lex-enregistrement08))*

**Entrées-sorties** — Organes qui font communiquer la machine avec le monde : clavier, écran, disque, réseau, capteurs et actionneurs. *(ch. 9, [voir le cours](09-architecture-des-ordinateurs-et-systemes/cours.md#lex-es09))*

**Événement** — Ce qui se produit dans la page, souvent une action de l’utilisateur (clic, survol, touche, envoi d’un formulaire) ; on y réagit en exécutant une fonction JavaScript. *(ch. 10, [voir le cours](10-le-web-reseaux-et-interactions-homme-mac/cours.md#lex-evenement10))*

**Expression** — Écriture formée de valeurs, de variables et d’opérateurs (`n + 1`, `a > b`…) que Python évalue pour obtenir une valeur ; c’est la partie droite d’une affectation. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-expression01))*

### F

**Filtrer une table** — Parcourir la table et garder dans une nouvelle liste les enregistrements qui vérifient un critère, par une boucle ou par compréhension. *(ch. 8, [voir le cours](08-les-donnees-en-tables/cours.md#lex-filtrer08))*

**Flottant** — Nombre à virgule stocké sur un nombre fini de bits (type `float`) ; sa valeur est le plus souvent approchée : on ne teste jamais l’égalité de deux flottants. *(ch. 2, [voir le cours](02-le-binaire-et-l-ecriture-des-nombres/cours.md#lex-flottant02))*

**Fonction** — Bloc d’instructions nommé, défini une fois (`def`) puis appelé autant de fois qu’on veut ; il reçoit des paramètres et peut renvoyer un résultat (`return`). *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-fonction01))*

**Formulaire** — Partie d’une page (`<form>`) qui envoie des données au serveur : `action` donne l’adresse qui les reçoit, `method` la méthode (`get` ou `post`). *(ch. 10, [voir le cours](10-le-web-reseaux-et-interactions-homme-mac/cours.md#lex-formulaire10))*

**Frontière de décision** — Ligne qui sépare les régions du plan coloriées selon la classe prédite ; elle colle aux exemples pour $k$ petit, devient plus lisse quand $k$ grandit. *(ch. 12, [voir le cours](12-les-k-plus-proches-voisins/cours.md#lex-frontiere12))*

### G

**`GET`** — Méthode HTTP qui demande une ressource (afficher une page) ; les éventuels paramètres sont visibles dans l’URL, après un `?`. *(ch. 10, [voir le cours](10-le-web-reseaux-et-interactions-homme-mac/cours.md#lex-get10))*

### H

**Hexadécimal (base 16)** — Base à 16 chiffres (`0` à `9`, puis `A` à `F`) ; un chiffre hexadécimal représente exactement 4 bits, un octet tient en deux chiffres. *(ch. 2, [voir le cours](02-le-binaire-et-l-ecriture-des-nombres/cours.md#lex-hexadecimal02))*

**HTML** — Langage de balisage (*HyperText Markup Language*), et non de programmation, qui décrit la structure du contenu d’une page : titres, paragraphes, images, liens. *(ch. 10, [voir le cours](10-le-web-reseaux-et-interactions-homme-mac/cours.md#lex-html10))*

**HTTP** — Protocole du Web : le client envoie une requête (méthode, chemin), le serveur renvoie une réponse (code de statut comme 200 ou 404, en-têtes, corps). HTTP est sans mémoire. *(ch. 10, [voir le cours](10-le-web-reseaux-et-interactions-homme-mac/cours.md#lex-http10))*

**HTTPS** — Version sécurisée de HTTP : la communication est chiffrée. Le cadenas prouve que la liaison est chiffrée, pas que le site est honnête. *(ch. 10, [voir le cours](10-le-web-reseaux-et-interactions-homme-mac/cours.md#lex-https10))*

### I

**`id`, `class`** — Attributs qui étiquettent une balise pour la retrouver en CSS ou en JavaScript : `id` est unique dans la page, `class` peut être partagée par plusieurs balises. *(ch. 10, [voir le cours](10-le-web-reseaux-et-interactions-homme-mac/cours.md#lex-idclass10))*

**Indentation** — Décalage vers la droite (4 espaces) des lignes qui forment un bloc. En Python, l’indentation est la structure ; on ne mélange jamais espaces et tabulations. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-indentation01))*

**Indice** — Position d’un élément dans une chaîne, un p-uplet ou un tableau, comptée à partir de 0 : de `0` à `len(t) - 1`. *(ch. 3, [voir le cours](03-les-types-construits/cours.md#lex-indice03))*

**Instruction conditionnelle** — Construction qui choisit entre plusieurs comportements selon une condition : `if`, `elif`, `else`. Seul le premier bloc dont la condition est vraie est exécuté. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-conditionnelle01))*

**Instructions du LMC** — `INP`/`OUT` : lire/afficher ; `LDA n`/`STA n` : charger la case `n` dans l’accumulateur ACC/l’y ranger ; `ADD`, `SUB` ; sauts `BRA`, `BRZ`, `BRP` ; `HLT` ; `DAT`. *(ch. 9, [voir le cours](09-architecture-des-ordinateurs-et-systemes/cours.md#lex-lmcio09))*

**Internet** — Réseau mondial : l’infrastructure de câbles, fibres, antennes et machines (routeurs) qui relient les ordinateurs entre eux. *(ch. 10, [voir le cours](10-le-web-reseaux-et-interactions-homme-mac/cours.md#lex-internet10))*

**Interpréteur, langage interprété** — Un langage interprété (comme Python) est traduit au fur et à mesure, pendant l’exécution, par un interpréteur nécessaire à chaque exécution. *(ch. 5, [voir le cours](05-specifier-et-mettre-au-point-ses-program/cours.md#lex-interpreteur05))*

**Invariant de boucle** — Propriété vraie avant la boucle et préservée à chaque tour ; à la sortie, elle prouve que le résultat est correct. *(ch. 4, [voir le cours](04-algorithmique-le-parcours-sequentiel/cours.md#lex-invariant04) ; ch. 5, [voir le cours](05-specifier-et-mettre-au-point-ses-program/cours.md#lex-invariant05))*

### J

**JavaScript** — Langage de programmation exécuté dans le navigateur (côté client) qui rend la page interactive : réagir à un clic, modifier le contenu, vérifier un formulaire. *(ch. 10, [voir le cours](10-le-web-reseaux-et-interactions-homme-mac/cours.md#lex-javascript10))*

**Jeu d’entraînement, jeu de test** — On sépare les exemples étiquetés : le jeu d’entraînement sert au vote, le jeu de test, jamais vu, mesure le taux de réussite. *(ch. 12, [voir le cours](12-les-k-plus-proches-voisins/cours.md#lex-entrainement12))*

**Jeu de tests** — Ensemble de cas dont on connaît le résultat attendu (cas normaux, cas limites, cas particuliers). Son succès ne prouve pas la correction : seulement sur les cas testés. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-jeutests01))*

**Jointure (fusion de tables)** — Production d’une table où chaque enregistrement de la première est complété par les informations de la seconde ayant la même valeur pour un descripteur commun. *(ch. 8, [voir le cours](08-les-donnees-en-tables/cours.md#lex-jointure08))*

### K

**$k$ plus proches voisins ($k$-NN)** — Méthode de classification : on calcule la distance du nouvel individu à chaque exemple, on garde les $k$ plus proches et on lui attribue leur classe majoritaire. *(ch. 12, [voir le cours](12-les-k-plus-proches-voisins/cours.md#lex-knn12))*

### L

**Langage machine** — Jeu réduit d’instructions très simples (charger, additionner, comparer, sauter…), codées en binaire : le seul langage que le processeur exécute. *(ch. 9, [voir le cours](09-architecture-des-ordinateurs-et-systemes/cours.md#lex-langagemachine09))*

**Ligne de commande (terminal)** — Interface où l’on tape des commandes au clavier, après une invite qui rappelle qui l’on est et où l’on est ; plus rapide et automatisable que l’interface graphique. *(ch. 9, [voir le cours](09-architecture-des-ordinateurs-et-systemes/cours.md#lex-lignecommande09))*

**Liste de dictionnaires** — Représentation d’une table en Python : chaque enregistrement est un dictionnaire `{descripteur: valeur}`, la table est la liste de ces dictionnaires. *(ch. 8, [voir le cours](08-les-donnees-en-tables/cours.md#lex-listedict08))*

**Little Man Computer (LMC)** — Machine-modèle de von Neumann à 100 cases mémoire, un accumulateur et un compteur de programme, programmée en assembleur et simulable en ligne. *(ch. 9, [voir le cours](09-architecture-des-ordinateurs-et-systemes/cours.md#lex-lmc09))*

**Logarithme de base 2 ($\log_2$)** — Nombre $a$ de divisions par 2 qui ramènent $n$ à 1, soit $n = 2^a$ : $\log_2$ est la réciproque de la puissance de 2. *(ch. 7, [voir le cours](07-la-recherche-dichotomique/cours.md#lex-logarithme07))*

### M

**Matrice** — Tableau de tableaux de même longueur : $n$ lignes et $p$ colonnes. `M[i][j]` est la case ligne `i`, colonne `j` ; on la parcourt avec deux boucles imbriquées. *(ch. 3, [voir le cours](03-les-types-construits/cours.md#lex-matrice03))*

**Meilleur cas, pire cas** — Situations la plus favorable et la plus défavorable pour le coût : pour une recherche séquentielle, élément en tête (1 comparaison) ou absent (`n` comparaisons). *(ch. 4, [voir le cours](04-algorithmique-le-parcours-sequentiel/cours.md#lex-pirecas04))*

**Mémoire** — Organe qui range à la fois le programme et les données, dans des cases numérotées par une adresse. *(ch. 9, [voir le cours](09-architecture-des-ordinateurs-et-systemes/cours.md#lex-memoire09))*

**Mémoire vive (RAM)** — Mémoire de quelques giga-octets, rapide mais volatile : tout s’efface à l’extinction. Enregistrer, c’est recopier de la RAM vers le disque, permanent. *(ch. 9, [voir le cours](09-architecture-des-ordinateurs-et-systemes/cours.md#lex-ram09))*

**`mkdir`, `touch`, `cat` (Linux)** — Commandes : `mkdir` crée un répertoire, `touch` crée un fichier vide, `cat` affiche le contenu d’un fichier. *(ch. 9, [voir le cours](09-architecture-des-ordinateurs-et-systemes/cours.md#lex-mkdir09))*

**Modèle de von Neumann** — Organisation de quasiment tous les ordinateurs (1945) : unité de commande, UAL, mémoire et entrées-sorties ; le programme est rangé dans la même mémoire que les données. *(ch. 9, [voir le cours](09-architecture-des-ordinateurs-et-systemes/cours.md#lex-vonneumann09))*

**Mutable, immuable** — Un objet est mutable si l’on peut changer son contenu sans en créer un nouveau (`list`, `dict`) ; immuable sinon (nombres, `str`, `tuple`). *(ch. 3, [voir le cours](03-les-types-construits/cours.md#lex-mutable03))*

### N

**Normaliser des descripteurs** — Ramener des descripteurs d’échelles différentes (âge, revenu) à une même échelle, pour qu’aucun n’écrase les autres dans la distance. *(ch. 12, [voir le cours](12-les-k-plus-proches-voisins/cours.md#lex-normaliser12))*

### O

**Octet** — Paquet de 8 bits (*byte*) ; il permet $2^8 = 256$ valeurs différentes. *(ch. 2, [voir le cours](02-le-binaire-et-l-ecriture-des-nombres/cours.md#lex-octet02))*

**Opérateur booléen (non, et, ou)** — Opérateur qui combine des valeurs booléennes : non $a$ inverse ; $a$ et $b$ vaut 1 seulement si les deux valent 1 ; $a$ ou $b$ vaut 1 dès qu’au moins un vaut 1. *(ch. 2, [voir le cours](02-le-binaire-et-l-ecriture-des-nombres/cours.md#lex-opbooleen02))*

**Oracle** — Fonction, en général plus simple que le programme testé, qui juge si un résultat est juste ; elle permet de vérifier des tests générés au hasard. *(ch. 5, [voir le cours](05-specifier-et-mettre-au-point-ses-program/cours.md#lex-oracle05))*

**Ou exclusif (xor)** — $a$ xor $b$ vaut 1 lorsque exactement un des deux bits vaut 1, c’est-à-dire lorsque $a$ et $b$ sont différents. *(ch. 2, [voir le cours](02-le-binaire-et-l-ecriture-des-nombres/cours.md#lex-xor02))*

### P

**p-uplet nommé (tableau associatif)** — Regroupement de valeurs repérées chacune par un nom de champ plutôt que par une position ; en Python, on l’écrit avec un dictionnaire. C’est une fiche, un enregistrement. *(ch. 3, [voir le cours](03-les-types-construits/cours.md#lex-pupletnomme03))*

**p-uplet (`tuple`)** — Suite ordonnée de $p$ éléments, de types éventuellement différents, qu’on ne peut pas modifier après création ; on sépare les éléments par des virgules : `(3, 4)`. *(ch. 3, [voir le cours](03-les-types-construits/cours.md#lex-puplet03))*

**Pair-à-pair** — Organisation où chaque machine est à la fois cliente et serveur et échange directement avec les autres, sans serveur central. *(ch. 10, [voir le cours](10-le-web-reseaux-et-interactions-homme-mac/cours.md#lex-p2p10))*

**Paquet** — Petit morceau d’un message découpé pour voyager sur le réseau ; il porte les adresses IP de départ et d’arrivée, et les paquets sont réassemblés à l’arrivée. *(ch. 10, [voir le cours](10-le-web-reseaux-et-interactions-homme-mac/cours.md#lex-paquet10))*

**Paradigme (style de programmation)** — Style d’un langage : impératif (des ordres qui modifient des variables, comme en Python cette année), fonctionnel, objet, logique, événementiel. *(ch. 5, [voir le cours](05-specifier-et-mettre-au-point-ses-program/cours.md#lex-paradigme05))*

**Paramètre** — Nom, placé entre parenthèses dans la ligne `def`, qui désigne une entrée de la fonction ; il reçoit la valeur de l’argument lors de l’appel. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-parametre01))*

**Parcours séquentiel** — Examen des éléments d’un tableau un par un, du premier au dernier, par élément ou par indice ; on dit aussi parcours linéaire. *(ch. 4, [voir le cours](04-algorithmique-le-parcours-sequentiel/cours.md#lex-parcours04))*

**Polygone régulier (tortue)** — Pour tracer un polygone régulier à $n$ côtés, la tortue avance puis tourne de $360/n$ degrés, $n$ fois. *(compl., [voir le cours](dessiner-avec-la-tortue/cours.md#lex-polygoneT))*

**Porte logique** — Petit circuit de quelques transistors qui reçoit un ou deux bits et en produit un, en réalisant un opérateur booléen (ET, OU, NON…). *(ch. 2, [voir le cours](02-le-binaire-et-l-ecriture-des-nombres/cours.md#lex-porte02))*

**Portée, variable locale** — Les paramètres et variables créés à l’intérieur d’une fonction sont locaux : ils naissent à l’appel, disparaissent au `return` et sont invisibles de l’extérieur. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-portee01))*

**`POST`** — Méthode HTTP qui envoie des données au serveur pour qu’il les traite (typiquement un formulaire) ; les données ne sont pas dans l’URL. *(ch. 10, [voir le cours](10-le-web-reseaux-et-interactions-homme-mac/cours.md#lex-post10))*

**Postcondition** — Garantie sur le résultat d’une fonction, valable si les préconditions sont respectées (ex. : « renvoie un nombre positif »). *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-postcondition01) ; ch. 5, [voir le cours](05-specifier-et-mettre-au-point-ses-program/cours.md#lex-postcondition05))*

**Précondition** — Hypothèse sur les arguments, à la charge de l’appelant, qui doit être vraie pour qu’on ait le droit d’appeler la fonction (ex. : `x >= 0`). *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-precondition01) ; ch. 5, [voir le cours](05-specifier-et-mettre-au-point-ses-program/cours.md#lex-precondition05))*

**Problème d’optimisation** — Problème qui demande, parmi de nombreuses solutions valides, d’en trouver une la meilleure possible selon une mesure de qualité à minimiser ou maximiser. *(ch. 11, [voir le cours](11-les-algorithmes-gloutons/cours.md#lex-optimisation11))*

**Problème du sac à dos** — Remplir un sac de capacité limitée en emportant le plus de valeur possible ; le glouton par rapport valeur/poids est rapide mais pas toujours optimal. *(ch. 11, [voir le cours](11-les-algorithmes-gloutons/cours.md#lex-sacados11))*

**Processeur (CPU)** — Réunion de l’unité de commande, de l’UAL et de quelques registres : il exécute les instructions du langage machine. *(ch. 9, [voir le cours](09-architecture-des-ordinateurs-et-systemes/cours.md#lex-processeur09))*

**Programmation défensive** — Façon de programmer qui teste la précondition à l’entrée d’une fonction (`assert`) ou renvoie une valeur sentinelle, pour échouer tôt et clairement. *(ch. 5, [voir le cours](05-specifier-et-mettre-au-point-ses-program/cours.md#lex-defensive05))*

**Programme** — Traduction d’un algorithme dans un langage que la machine peut exécuter : une suite d’instructions qu’un ordinateur exécute pour accomplir une tâche. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-programme01))*

**Protocole** — Ensemble de règles précises que deux machines respectent pour communiquer (IP, TCP, HTTP…). *(ch. 10, [voir le cours](10-le-web-reseaux-et-interactions-homme-mac/cours.md#lex-protocole10))*

**Protocole du bit alterné** — Chaque paquet porte un seul bit, alternativement 0 et 1 ; il suffit au récepteur pour distinguer un nouveau paquet d’un paquet renvoyé (doublon). *(ch. 10, [voir le cours](10-le-web-reseaux-et-interactions-homme-mac/cours.md#lex-bitalterne10))*

**Prototype** — Annonce du nom d’une fonction, de ses paramètres et de ce qu’elle renvoie, par exemple `racine(x)`. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-prototype01))*

**`pwd`, `ls`, `cd` (Linux)** — Commandes pour se repérer : `pwd` affiche le répertoire courant, `ls` liste un répertoire (`ls -l` en détail, avec les droits), `cd` change de répertoire. *(ch. 9, [voir le cours](09-architecture-des-ordinateurs-et-systemes/cours.md#lex-pwd09))*

### R

**Recherche dichotomique** — Recherche dans un tableau trié : on compare à l’élément du milieu et on divise par deux la zone de recherche `[deb ; fin]` à chaque étape. *(ch. 7, [voir le cours](07-la-recherche-dichotomique/cours.md#lex-dichotomie07))*

**Recherche séquentielle** — Parcours qui cherche si un élément est présent (ou où il est) et s’arrête dès qu’il le trouve ; s’il est absent, on renvoie `-1` ou `None` selon l’énoncé. *(ch. 4, [voir le cours](04-algorithmique-le-parcours-sequentiel/cours.md#lex-rechseq04))*

**Référence (modèle mémoire)** — Une variable ne contient pas l’objet : elle le désigne, comme une flèche du nom vers l’objet rangé en mémoire. Ce modèle explique alias et copies. *(ch. 3, [voir le cours](03-les-types-construits/cours.md#lex-reference03))*

**Rendu de monnaie** — Rendre une somme avec le moins de pièces possible ; le glouton prend à chaque fois la plus grande coupure qui ne dépasse pas la somme restante. *(ch. 11, [voir le cours](11-les-algorithmes-gloutons/cours.md#lex-monnaie11))*

**Répertoire courant, répertoire parent** — Le répertoire courant est celui où l’on se trouve, noté `.` ; le répertoire parent, un cran au-dessus, est noté `..`. *(ch. 9, [voir le cours](09-architecture-des-ordinateurs-et-systemes/cours.md#lex-courant09))*

**Rosace** — Figure obtenue en répétant un même motif tout en tournant un peu à chaque fois : une fonction, une boucle et un petit tour. *(compl., [voir le cours](dessiner-avec-la-tortue/cours.md#lex-rosaceT))*

**Routeur** — Machine qui aiguille les paquets : elle lit l’adresse IP de destination et choisit vers quel voisin renvoyer le paquet ; les routeurs interconnectés forment Internet. *(ch. 10, [voir le cours](10-le-web-reseaux-et-interactions-homme-mac/cours.md#lex-routeur10))*

### S

**Sélecteur (CSS)** — Partie d’une règle CSS qui vise des balises : par nom (`h1`), par identifiant (`#menu`) ou par classe (`.bouton`). *(ch. 10, [voir le cours](10-le-web-reseaux-et-interactions-homme-mac/cours.md#lex-selecteur10))*

**Séquence** — Construction la plus simple : des instructions écrites les unes sous les autres, exécutées dans l’ordre, de haut en bas, une à la fois. L’ordre détermine le résultat. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-sequence01))*

**Solution optimale, solution approchée** — Une solution optimale est une meilleure solution ; une solution approchée est une bonne solution, pas forcément la meilleure. *(ch. 11, [voir le cours](11-les-algorithmes-gloutons/cours.md#lex-optimale11))*

**Spécification** — Description du contrat d’une fonction, sans dire comment elle s’y prend : son prototype, ses préconditions et ses postconditions. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-specification01) ; ch. 5, [voir le cours](05-specifier-et-mettre-au-point-ses-program/cours.md#lex-specification05))*

**Système canonique** — Système de pièces (comme les euros) pour lequel le rendu de monnaie glouton donne toujours la solution optimale ; ce n’est pas le cas de tous. *(ch. 11, [voir le cours](11-les-algorithmes-gloutons/cours.md#lex-canonique11))*

**Système d’exploitation (OS)** — Ensemble de programmes qui gèrent le matériel (processeur, mémoire, fichiers, périphériques, utilisateurs) et le mettent à disposition des applications : Windows, macOS, Linux…*(ch. 9, [voir le cours](09-architecture-des-ordinateurs-et-systemes/cours.md#lex-os09))*

### T

**Table de données** — Organisation de l’information en lignes (les enregistrements) et colonnes (les descripteurs) ; en Python, une liste de dictionnaires. *(ch. 8, [voir le cours](08-les-donnees-en-tables/cours.md#lex-table08))*

**Table de vérité** — Tableau qui donne la valeur d’un opérateur ou d’une expression booléenne pour chaque combinaison possible des entrées, une ligne par combinaison. *(ch. 2, [voir le cours](02-le-binaire-et-l-ecriture-des-nombres/cours.md#lex-tableverite02))*

**Tableau (`list`)** — Suite ordonnée et modifiable d’éléments, écrite entre crochets : `[12, 8, 15]`. On lit et modifie chaque élément par son indice. *(ch. 3, [voir le cours](03-les-types-construits/cours.md#lex-tableau03))*

**TCP** — Protocole de transport d’Internet qui, par accusés de réception et renvois, garantit qu’aucune donnée n’est perdue ni dupliquée. *(ch. 10, [voir le cours](10-le-web-reseaux-et-interactions-homme-mac/cours.md#lex-tcp10))*

**Terminaison** — Propriété d’un algorithme qui s’arrête toujours. Pour une boucle non bornée, on la justifie avec un variant. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-terminaison01))*

**Trace d’exécution** — Tableau qui suit l’évolution des variables tour après tour ; la dresser à la main est un réflexe essentiel pour comprendre ou déboguer un programme. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-trace01))*

**Transistor** — Minuscule interrupteur commandé électriquement, sans pièce mécanique, qui bascule des milliards de fois par seconde ; brique de base des portes logiques. *(ch. 9, [voir le cours](09-architecture-des-ordinateurs-et-systemes/cours.md#lex-transistor09))*

**Tri** — Réorganisation des éléments d’un tableau dans l’ordre croissant, `t[0]` $\leq$ `t[1]` $\leq \cdots$, en comparant et en échangeant des éléments. *(ch. 6, [voir le cours](06-les-algorithmes-de-tri/cours.md#lex-tri06))*

**Tri en place** — Tri qui réarrange le tableau donné lui-même, sans en créer un nouveau. *(ch. 6, [voir le cours](06-les-algorithmes-de-tri/cours.md#lex-enplace06))*

**Tri par insertion** — On prend les éléments un par un et on insère chacun à sa place dans la partie gauche déjà triée, en décalant les plus grands. Linéaire si le tableau est déjà trié. *(ch. 6, [voir le cours](06-les-algorithmes-de-tri/cours.md#lex-triinsertion06))*

**Tri par sélection** — À chaque étape, on cherche le minimum de la partie non triée et on l’échange avec son premier élément ; la partie gauche est triée et définitive. *(ch. 6, [voir le cours](06-les-algorithmes-de-tri/cours.md#lex-triselection06))*

**Typage dynamique** — Le type n’est connu que pendant l’exécution, quand la ligne est atteinte (c’est le cas de Python) : une erreur de type ne se manifeste qu’à ce moment-là. *(ch. 5, [voir le cours](05-specifier-et-mettre-au-point-ses-program/cours.md#lex-typagedyn05))*

**Typage statique** — Le type de chaque variable est fixé et vérifié avant l’exécution : une opération entre types incompatibles est refusée sans même lancer le programme. *(ch. 5, [voir le cours](05-specifier-et-mettre-au-point-ses-program/cours.md#lex-typagestatique05))*

**Type** — Nature d’une valeur, qui décide des opérations permises : entier (`int`), flottant (`float`), chaîne (`str`), booléen (`bool`)…*(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-type01))*

**Type construit** — Type dont chaque valeur regroupe plusieurs valeurs en un seul objet : p-uplet, tableau, dictionnaire. Par opposition, `int`, `float`, `bool`, `str` sont simples. *(ch. 3, [voir le cours](03-les-types-construits/cours.md#lex-typeconstruit03))*

### U

**UAL (unité arithmétique et logique)** — Organe du processeur qui calcule : additions, comparaisons, ET/OU logiques…*(ch. 9, [voir le cours](09-architecture-des-ordinateurs-et-systemes/cours.md#lex-ual09))*

**Unicode, point de code** — Catalogue universel qui attribue un numéro unique, le point de code (noté `U+`…), à tous les caractères de toutes les écritures. *(ch. 2, [voir le cours](02-le-binaire-et-l-ecriture-des-nombres/cours.md#lex-unicode02))*

**Unité de commande** — Organe du processeur qui lit les instructions du programme, les décode et ordonne leur exécution. *(ch. 9, [voir le cours](09-architecture-des-ordinateurs-et-systemes/cours.md#lex-commande09))*

**URL** — Adresse d’une ressource sur le Web : protocole (`https`), nom de domaine du serveur (`www.lycee.mc`) et chemin de la ressource (`/nsi/cours.html`). *(ch. 10, [voir le cours](10-le-web-reseaux-et-interactions-homme-mac/cours.md#lex-url10))*

**UTF-8** — Façon la plus répandue d’écrire les points de code Unicode en octets : 1 octet pour les caractères ASCII, 2 à 4 octets pour les autres. *(ch. 2, [voir le cours](02-le-binaire-et-l-ecriture-des-nombres/cours.md#lex-utf802))*

### V

**Valeur booléenne** — Valeur qui ne peut être que `1` (vrai) ou `0` (faux) ; en Python, `True` ou `False` (type `bool`). *(ch. 2, [voir le cours](02-le-binaire-et-l-ecriture-des-nombres/cours.md#lex-booleen02))*

**Valeur renvoyée** — Résultat qu’une fonction rend au programme avec `return`, pour être réutilisé dans un calcul ; une fonction sans `return` renvoie `None`. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-valeurrenvoyee01))*

**Valeur sentinelle** — Valeur renvoyée qui ne peut pas être confondue avec un résultat valide (en Python, `None`) ; celui qui appelle teste alors le résultat. *(ch. 5, [voir le cours](05-specifier-et-mettre-au-point-ses-program/cours.md#lex-sentinelle05))*

**Variable** — Nom qui désigne une valeur rangée en mémoire ; on peut lire cette valeur et la modifier. Plus précisément, une étiquette qui pointe vers un objet. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-variable01) ; ch. 3, [voir le cours](03-les-types-construits/cours.md#lex-variable03))*

**Variant de boucle** — Quantité entière positive qui décroît strictement à chaque tour de boucle ; s’il en existe un, la boucle finit par s’arrêter (terminaison). *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-variant01) ; ch. 7, [voir le cours](07-la-recherche-dichotomique/cours.md#lex-variant07))*

**Voyageur de commerce** — Visiter toutes les villes et revenir au départ en parcourant le moins de kilomètres ; le glouton « ville la plus proche » donne une bonne solution, rarement la meilleure. *(ch. 11, [voir le cours](11-les-algorithmes-gloutons/cours.md#lex-voyageur11))*

### W

**Web** — Service d’Internet (*World Wide Web*) : ensemble des pages reliées par des liens hypertextes, consultées avec un navigateur. Ne pas le confondre avec Internet. *(ch. 10, [voir le cours](10-le-web-reseaux-et-interactions-homme-mac/cours.md#lex-web10))*

## Python : mots-clés, fonctions et syntaxe

<span id="lexique-python" class="ancre"></span>

**`%` (modulo)** — Reste de la division entière : `7 % 2` vaut `1`. Un entier `a` est divisible par `b` lorsque `a % b == 0`. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-modulo01))*

**`+`, `-`, `*`, `/`, `**`** — Opérations sur les nombres : addition, soustraction, multiplication, division (`7 / 2` vaut le flottant `3.5`), puissance (`7 ** 2` vaut `49`). *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-operations01))*

**`//` (quotient entier)** — Quotient de la division entière : `7 // 2` vaut `3`. Il sert par exemple à calculer le milieu `(deb + fin) // 2`. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-quotient01))*

**`0b`, `bin`** — Préfixe d’un littéral binaire : `0b10111001` vaut 185 ; `bin(185)` donne la chaîne `’0b10111001’` et `int("10111001", 2)` fait l’inverse. *(ch. 2, [voir le cours](02-le-binaire-et-l-ecriture-des-nombres/cours.md#lex-binlit02))*

**`=` et `==`** — `=` affecte une valeur (« reçoit ») ; `==` teste l’égalité et renvoie un booléen. Les confondre est une erreur très fréquente. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-egal01))*

**`[0] * n`** — Répétition : tableau de `n` zéros. Piège : `[[0] * p] * n` répète la même ligne ; on écrit `[[0] * p for i in range(n)]`. *(ch. 3, [voir le cours](03-les-types-construits/cours.md#lex-repetition03))*

**`abs`** — Valeur absolue ; on compare deux flottants par un écart minuscule : `abs(a - b) < 1e-9`, jamais par `==`. *(ch. 2, [voir le cours](02-le-binaire-et-l-ecriture-des-nombres/cours.md#lex-abs02))*

**Affectation multiple `a, b = b, a`** — Déballe un p-uplet dans plusieurs variables ; Python évalue d’abord tout le membre de droite, ce qui permet d’échanger deux variables en une ligne. *(ch. 3, [voir le cours](03-les-types-construits/cours.md#lex-affmult03))*

**`and`, `or`, `not`** — Opérateurs booléens qui combinent des conditions. `and` et `or` sont séquentiels : évalués de gauche à droite, ils s’arrêtent dès que le résultat est connu. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-andor01))*

**`append`** — Méthode `t.append(x)` : ajoute `x` à la fin du tableau, sur place, et renvoie `None` (ne jamais écrire `t = t.append(x)`). *(ch. 3, [voir le cours](03-les-types-construits/cours.md#lex-append03))*

**`assert`** — Instruction qui vérifie une condition et arrête le programme avec un message si elle est fausse ; sert de garde-fou sur une précondition et à écrire les tests. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-assert01))*

**`begin_fill`, `end_fill`** — Ordres de la tortue qui encadrent le tracé d’une figure pour la remplir de couleur. *(compl., [voir le cours](dessiner-avec-la-tortue/cours.md#lex-fillT))*

**`bool`, `True`, `False`** — Type booléen et ses deux seules valeurs, vrai et faux ; c’est la valeur d’une condition. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-truefalse01))*

**`circle`, `color`** — Ordres de la tortue : `circle(r)` trace un cercle de rayon `r`, `color("red")` choisit la couleur du trait. *(compl., [voir le cours](dessiner-avec-la-tortue/cours.md#lex-circleT))*

**`csv.DictReader`** — Lecteur du module `csv` qui lit l’en-tête puis transforme chaque ligne en dictionnaire ; toutes les valeurs sont des chaînes ; `delimiter` précise le séparateur. *(ch. 8, [voir le cours](08-les-donnees-en-tables/cours.md#lex-dictreader08))*

**`d[cle]`, `del`** — `d[cle]` lit la valeur associée à une clé ; `d[cle] = v` crée ou remplace un couple ; `del d[cle]` le supprime. *(ch. 3, [voir le cours](03-les-types-construits/cours.md#lex-dcle03))*

**`def`** — Mot-clé qui définit une fonction : `def nom(param1, param2):` suivi du bloc indenté. La définition seule n’exécute rien. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-def01))*

**Deux-points `:`** — Signe obligatoire en fin de ligne `if`, `elif`, `else`, `for`, `while`, `def` ; les lignes du bloc qui suit sont indentées. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-deuxpoints01))*

**Docstring** — Texte entre triples guillemets placé juste après la ligne `def` : rôle, précondition, postcondition. On la consulte avec `help`. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-docstring01) ; ch. 5, [voir le cours](05-specifier-et-mettre-au-point-ses-program/cours.md#lex-docstring05))*

**`elif`** — Contraction de *else if* : enchaîne plusieurs tests ; Python exécute le premier bloc dont la condition est vraie et ignore les autres. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-elif01))*

**`encode`, `decode`** — Méthodes qui convertissent un texte en octets (`"é".encode("utf-8")`) et des octets en texte, selon un encodage. *(ch. 2, [voir le cours](02-le-binaire-et-l-ecriture-des-nombres/cours.md#lex-encode02))*

**`float`** — Type des nombres à virgule (flottants), aux valeurs approchées ; `float(...)` convertit en flottant : `float("12.5")`. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-float01))*

**`for`** — Boucle bornée : `for i in range(n):` répète le bloc pour chaque valeur ; `for x in t:` parcourt directement les éléments d’une chaîne ou d’un tableau. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-for01))*

**`for x in t`, `for i in range(len(t))`** — Les deux parcours d’un tableau : par élément, quand seules les valeurs comptent ; par indice, quand on a besoin de la position ou qu’on veut modifier. *(ch. 3, [voir le cours](03-les-types-construits/cours.md#lex-forin03))*

**`forward`, `backward`** — Ordres de la tortue : `forward(d)` avance de `d` pas, `backward(d)` recule ; le trait n’apparaît qu’avec ces ordres. *(compl., [voir le cours](dessiner-avec-la-tortue/cours.md#lex-forwardT))*

**`goto`** — Ordre de la tortue : `goto(x, y)` va au point de coordonnées `(x, y)`. *(compl., [voir le cours](dessiner-avec-la-tortue/cours.md#lex-gotoT))*

**`help`** — Fonction qui affiche la docstring d’une fonction, sans voir son code. *(ch. 5, [voir le cours](05-specifier-et-mettre-au-point-ses-program/cours.md#lex-help05))*

**`if`, `else`** — `if condition:` exécute le bloc indenté si la condition est vraie ; le bloc de `else:` est exécuté sinon. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-ifelse01))*

**`import`** — Instruction qui charge une bibliothèque (un module) : `import random`, `import turtle as t`, `import csv`. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-import01))*

**`in`** — Test d’appartenance (`x in t`) ; sur un dictionnaire, `cle in d` porte sur les clés, pas sur les valeurs. Dans `for x in t`, il introduit le parcours. *(ch. 3, [voir le cours](03-les-types-construits/cours.md#lex-in03))*

**`IndentationError`** — Erreur provoquée par une indentation incohérente des lignes d’un bloc. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-indenterror01))*

**Indices négatifs `t[-1]`** — Indices comptés depuis la fin : `t[-1]` est le dernier élément, `t[-2]` l’avant-dernier ; `t[-k]` désigne `t[len(t) - k]`. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-negatif01) ; ch. 3, [voir le cours](03-les-types-construits/cours.md#lex-negatif03))*

**`input`** — Fonction qui affiche un message, attend une saisie au clavier et renvoie ce qui a été tapé, toujours sous forme de chaîne. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-input01))*

**`int`** — Type des entiers (de taille arbitraire en Python) ; `int(...)` convertit en entier : `int("17")` vaut `17`. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-int01))*

**`KeyError`** — Erreur provoquée par `d[cle]` quand la clé est absente du dictionnaire ; tester `cle in d` avant l’évite. *(ch. 3, [voir le cours](03-les-types-construits/cours.md#lex-keyerror03))*

**`keys`, `values`, `items`** — Méthodes d’un dictionnaire : `d.keys()` les clés, `d.values()` les valeurs, `d.items()` les couples `(clé, valeur)` ; `for k in d` parcourt les clés. *(ch. 3, [voir le cours](03-les-types-construits/cours.md#lex-items03))*

**`lambda`** — Petite fonction anonyme utilisée comme clé de tri : `lambda ligne: int(ligne["nombre"])` associe à une fiche sa clé de tri. *(ch. 8, [voir le cours](08-les-donnees-en-tables/cours.md#lex-lambda08))*

**`left`, `right`** — Ordres de la tortue : `left(a)` et `right(a)` tournent de `a` degrés à gauche ou à droite ; ils ne changent que le cap. *(compl., [voir le cours](dessiner-avec-la-tortue/cours.md#lex-leftT))*

**`len`** — Fonction qui renvoie le nombre d’éléments d’une chaîne, d’un p-uplet, d’un tableau ou d’un dictionnaire. *(ch. 3, [voir le cours](03-les-types-construits/cours.md#lex-len03))*

**`M[i][j]`** — Case ligne `i`, colonne `j` d’une matrice ; `len(M)` est le nombre de lignes, `len(M[0])` le nombre de colonnes. *(ch. 3, [voir le cours](03-les-types-construits/cours.md#lex-mij03))*

**`NameError`** — Erreur provoquée par l’utilisation d’un nom qui n’existe pas, souvent une faute de frappe. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-nameerror01))*

**`None`** — Valeur spéciale « rien » : renvoyée par une fonction sans `return`, ou comme valeur sentinelle ; on la teste avec `r is None`. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-none01) ; ch. 5, [voir le cours](05-specifier-et-mettre-au-point-ses-program/cours.md#lex-none05))*

**`open`, `with`** — `open(...)` ouvre un fichier (ici avec `encoding="utf-8"`) ; dans un bloc `with`, le fichier est refermé tout seul à la fin. *(ch. 8, [voir le cours](08-les-donnees-en-tables/cours.md#lex-open08))*

**`ord`, `chr`** — `ord` donne le code (point de code) d’un caractère, `chr` fait l’inverse : `ord(’A’)` vaut 65, `chr(65)` vaut `’A’`. *(ch. 2, [voir le cours](02-le-binaire-et-l-ecriture-des-nombres/cours.md#lex-ordchr02))*

**`penup`, `pendown`** — Ordres de la tortue : lever et baisser le stylo, pour se déplacer sans tracer. *(compl., [voir le cours](dessiner-avec-la-tortue/cours.md#lex-penupT))*

**`pop`** — Méthode `t.pop()` : retire et renvoie le dernier élément ; `t.pop(i)` retire et renvoie l’élément d’indice `i`. *(ch. 3, [voir le cours](03-les-types-construits/cours.md#lex-pop03))*

**`print`** — Fonction qui affiche à l’écran ce qu’on lui donne entre parenthèses ; `end=""` évite le retour à la ligne. Afficher n’est pas renvoyer. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-print01))*

**`random.randint`** — Fonction du module `random` : `random.randint(1, 6)` renvoie un entier au hasard entre 1 et 6 (bornes comprises). *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-random01))*

**`range`** — `range(n)` : les entiers de `0` à `n-1` ; `range(a, b)` : de `a` à `b-1` ; `range(a, b, pas)` : de `pas` en `pas`. La borne `b` est exclue. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-range01))*

**`return`** — Instruction qui renvoie une valeur au programme et sort immédiatement de la fonction ; les lignes situées après ne sont pas exécutées. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-return01))*

**`return a, b`** — Une fonction renvoie plusieurs résultats sous forme de p-uplet, récupérés par affectation multiple : `q, r = division(17, 5)`. *(ch. 3, [voir le cours](03-les-types-construits/cours.md#lex-renvoiplusieurs03))*

**`sort`, `sorted`** — Tris tout faits de Python (Timsort) : `t.sort()` trie en place, `sorted(t)` renvoie un nouveau tableau trié. Le chapitre programme d’abord, à la main, le tri par sélection et le tri par insertion. *(ch. 6, [voir le cours](06-les-algorithmes-de-tri/cours.md#lex-sort06))*

**`sorted(..., key=...)`** — Trie une table selon un descripteur : `key` donne la valeur à comparer pour chaque fiche, `reverse=True` trie du plus grand au plus petit. *(ch. 8, [voir le cours](08-les-donnees-en-tables/cours.md#lex-key08))*

**`str`** — Type des chaînes de caractères ; `str(...)` convertit en chaîne : `str(17)` vaut `"17"`. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-str01))*

**`SyntaxError`** — Erreur de syntaxe (`:` ou parenthèse oubliés…), détectée avant l’exécution : Python refuse le programme sans exécuter la moindre ligne. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-syntaxerror01))*

**`t[i]` (accès par indice)** — Élément d’indice `i` d’une chaîne, d’un p-uplet ou d’un tableau, de `0` à `len(t) - 1` ; dans un tableau, `t[i] = x` le remplace. *(ch. 3, [voir le cours](03-les-types-construits/cours.md#lex-crochets03))*

**`Traceback`** — Message d’erreur affiché quand le programme s’arrête : fichier, numéro de ligne, ligne fautive, puis, en dernière ligne, le type d’erreur et son message. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-traceback01))*

**Tranche `t[a:b]`** — Nouveau tableau (ou chaîne) formé des éléments d’indices `a` à `b - 1` ; `a` omis : depuis le début ; `b` omis : jusqu’à la fin. *(ch. 3, [voir le cours](03-les-types-construits/cours.md#lex-tranche03))*

**`turtle`** — Module de dessin : on l’importe (`import turtle as t`), on donne des ordres à la tortue, et `turtle.done()` garde la fenêtre ouverte. *(compl., [voir le cours](dessiner-avec-la-tortue/cours.md#lex-turtleT))*

**`type`** — Fonction qui renvoie le type d’une valeur : `type(12.5)` donne `<class ’float’>`. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-typef01))*

**`TypeError`** — Erreur provoquée par une opération entre types incompatibles, comme `"a" + 1`. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-typeerror01))*

**`while`** — Boucle non bornée : `while condition:` répète le bloc tant que la condition est vraie, testée avant chaque tour. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-while01))*

**`ZeroDivisionError`** — Erreur provoquée par une division par zéro. *(ch. 1, [voir le cours](01-les-bases-de-la-programmation-python/cours.md#lex-zerodiv01))*
