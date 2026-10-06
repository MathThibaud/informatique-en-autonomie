# Présentation de l'année

Cette année prolonge et couronne ce que vous avez commencé en Première. On monte d’un cran : de nouvelles **structures de données** (arbres, graphes), des **méthodes algorithmiques** puissantes, les **bases de données**, le fonctionnement profond des **machines et des réseaux**… et même les **limites** de ce qu’un ordinateur peut calculer. Objectif : devenir autonome et rigoureux, et arriver prêt(e)s aux épreuves.

!!! encadre "L’esprit NSI, version Terminale"

    - **Autonomie** : concevoir une solution, la programmer, la tester, la corriger — par vous-même.

    - **Abstraction** : choisir la bonne *structure de données* et la bonne *méthode* pour chaque problème.

    - **Rigueur** : justifier qu’un programme *se termine*, qu’il est *correct*, et estimer son *coût*.

## La discipline, cette année

La NSI est une **spécialité scientifique** à part entière. En Terminale, c’est **6 heures par semaine**, dont une bonne partie **sur machine**. Elle s’articule autour des mêmes grands piliers qu’en Première, poussés plus loin :

- **programmer** — avec de nouveaux styles (objet, récursif, fonctionnel) ;

- **l’algorithmique** — des méthodes puissantes (diviser pour régner, programmation dynamique, algorithmes de graphes) ;

- **les structures de données** — listes chaînées, piles, files, arbres, graphes ;

- **les données** — les bases de données relationnelles et le langage SQL ;

- **les machines et les réseaux** — systèmes d’exploitation, processus, routage, sécurité.

Environ **un tiers de l’année** reste consacré à des **projets** et à la pratique sur machine : c’est là qu’on devient vraiment autonome.

## Ce que vous allez apprendre

*Le programme est dense et s’enchaîne : la **récursivité** (chapitre 1) est la clé qui ouvre les arbres, « diviser pour régner » et les graphes. On avance régulièrement tout au long de l’année.*

### De la rentrée aux vacances de Toussaint

**Chapitre 1 — La récursivité.** *Résoudre un problème en le ramenant à une version plus petite de lui-même : une fonction qui s’appelle elle-même. Élégant, et incontournable pour toute la suite.*

**Chapitre 2 — La programmation orientée objet.** *Concevoir vos propres « objets » (leurs données *et* leurs actions) pour organiser des programmes plus gros et plus clairs.*

**Chapitre 3 — Les structures de données linéaires.** *Construire vos propres boîtes à ranger l’information : listes chaînées, piles (« dernier arrivé, premier servi ») et files (comme une file d’attente).*

### De la Toussaint à Noël

**Chapitre 4 — Les arbres.** *Manipuler des structures « en arborescence » (comme un arbre généalogique) et y ranger ou rechercher une information très efficacement.*

**Chapitre 5 — Diviser pour régner.** *Couper un gros problème en deux moitiés, les résoudre séparément, puis recombiner : la recette des algorithmes rapides, comme le tri fusion.*

**Chapitre 6 — Bases de données et SQL.** *Interroger de vraies bases de données avec le langage SQL : retrouver, croiser et mettre à jour de très grandes quantités de données.*

### De janvier aux vacances d’hiver

**Chapitre 7 — Les graphes.** *Modéliser des réseaux (routes, amis, Internet) par des points reliés, et écrire des algorithmes pour s’y déplacer, détecter un cycle, trouver un chemin.*

**Chapitre 8 — La programmation dynamique.** *Rendre certains algorithmes récursifs spectaculairement plus rapides, en évitant de recalculer sans cesse la même chose.*

**Chapitre 9 — La recherche textuelle.** *Trouver efficacement un motif dans un grand texte (un roman, un génome) : de la méthode naïve à l’algorithme de Boyer-Moore.*

**Chapitre 10 — Processus et ordonnancement.** *Comprendre comment le système d’exploitation fait tourner plusieurs programmes « en même temps » et gère les ressources de la machine.*

### De l’hiver au printemps

**Chapitre 11 — Les réseaux.** *Suivre le voyage d’un message sur Internet : adressage, découpage en paquets, routage — comment les données trouvent leur chemin d’un bout à l’autre du monde.*

**Chapitre 12 — Cryptographie.** *Protéger ces échanges : le chiffrement (symétrique et asymétrique) qui rend un message illisible pour tout autre que son destinataire.*

**Chapitre 13 — Calculabilité et décidabilité.** *Toucher aux **limites** de l’informatique : existe-t-il des problèmes qu’*aucun* programme ne pourra jamais résoudre ? (Oui — et c’est vertigineux.)*

**Chapitre 14 — Systèmes sur puce et informatique embarquée.** *Découvrir comment un ordinateur entier tient sur une seule puce (dans votre téléphone, votre console, votre voiture) et ce que fait un microcontrôleur dans un système embarqué.*

!!! remarque "Remarque — Un peu d’histoire"

    En **1936**, le mathématicien britannique **Alan Turing** imagine une machine abstraite capable d’exécuter *n’importe quel* algorithme — l’ancêtre théorique de tous nos ordinateurs. Il démontre aussi qu’un programme ne peut pas, en général, décider si un autre programme *s’arrêtera* un jour : c’est le fameux « problème de l’arrêt », que vous rencontrerez au chapitre 13. L’architecture concrète de nos machines, elle, doit beaucoup à **John von Neumann** (1945), dont vous croiserez le modèle au chapitre 14.

## Comment est organisé ce livre

!!! encadre "Comment est organisé un chapitre"

    Chaque chapitre de ce livre suit le même parcours :

    - **Activités préparatoires** : courtes, souvent sans ordinateur, à faire *avant* le cours pour se poser les bonnes questions ;

    - **Cours** : les notions, des exemples corrigés et un bilan ;

    - **Exercices** : du plus simple au niveau du bac, avec des coups de pouce en fin de rubrique ; leurs corrigés sont en fin de livre ;

    - **TP et projets** : un travail plus long sur machine qui réinvestit tout le chapitre ;

    - **Défis Advent of Code** : des énigmes de programmation tirées d’*Advent of Code* (`adventofcode.com`), un concours en ligne créé et animé depuis 2015 par le développeur **Eric Wastl**, qui publie chaque année, du 1<sup>er</sup> au 25 décembre, une énigme en deux parties. L’énoncé, en anglais, se lit sur le site (QR code sur chaque fiche ; le navigateur peut le traduire) ; la fiche fournit un lexique, un résumé, un petit exemple pour se tester et des coups de pouce. Ces défis sont **facultatifs** et n’utilisent que des notions déjà vues dans l’année.

    **Les défis n’ont volontairement pas de corrigé** dans ce livre : tout le plaisir d’une énigme est de la résoudre soi-même. Le site indique si votre réponse est juste (avec un compte gratuit) ; en cas de blocage, lisez les coups de pouce, puis venez en parler en classe.

## Le cap : le baccalauréat

!!! encadre "Les épreuves"

    - **l’écrit de spécialité** (en **juin**, coefficient **16**) : une épreuve écrite portant sur l’ensemble du programme ;

    - **le Grand Oral** (en juin également, coefficient **8**) : vous préparez **deux questions**, dont **au moins une doit s’appuyer sur la NSI**.

Comme les épreuves ont lieu **en fin d’année**, on dispose de **toute l’année** pour construire le programme. Le **troisième trimestre** sert à le **terminer et le consolider**, à s’entraîner en conditions (**bacs blancs**, pratique sur machine) et à préparer le **Grand Oral**.

## Comment vous êtes évalué

- à chaque chapitre : un ou deux courts **tests rapides** (/10) puis un **contrôle** (/20) — sauf pour la calculabilité, évaluée par ses seuls tests rapides ;

- des **bacs blancs** pour s’entraîner en conditions ;

- des **projets et travaux sur machine**, qui comptent aussi.

!!! encadre "L’intelligence artificielle : une charte, trois pastilles"

    Les assistants d’IA savent écrire du code et des explications ; le but de ce cours est que **vous** sachiez le faire, le vérifier et l’expliquer. Une [**charte d’usage de l’IA**](charte.md), reproduite juste après cette présentation, fixe ce qui est permis. L’usage est décidé **exercice par exercice** et signalé par une pastille à côté du titre :

    - <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> **sans IA** : tests, contrôles, sujets d’épreuve, exercices d’automatisme (lecture de code, questions de cours) ;

    - <span class="ia ia-orange" title="IA en appui : déboguer, reformuler, vérifier ; la réponse finale est la vôtre"></span> **IA en appui** : pour déboguer, reformuler ou vérifier, à condition d’écrire soi-même la réponse finale ;

    - <span class="ia ia-vert" title="IA intégrée : l'exercice s'appuie sur une réponse d'IA"></span> **IA intégrée** : l’exercice consiste à critiquer, tester ou améliorer une réponse d’assistant.

    Dans tous les cas : vous restez responsable de ce que vous rendez, vous devez pouvoir l’expliquer à l’oral, et vous dites quand l’IA a été utilisée. La complétion automatique de code dans l’éditeur compte comme un assistant.

!!! remarque "Remarque — Une ressource pour réviser à la maison"

    Deux sites tenus par des professeurs de NSI sont d’excellentes ressources pour la terminale : claires, complètes et conformes au programme. Ils ont été une **source d’inspiration** pour la préparation de nos cours, et je vous encourage à les consulter pour réviser ou approfondir, notamment en vue de l’épreuve écrite :

    - le site de **Gilles Lassus** : `glassus.github.io` ;

    - le site de **David Roche** : `pixees.fr/informatiquelycee`.

*Une année exigeante, mais passionnante. À la fin, vous saurez vraiment programmer — et penser comme un informaticien.*
