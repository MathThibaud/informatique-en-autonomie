# TP et projets

<p class="sous-titre">Le Web : réseaux et interactions homme-machine</p>

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
