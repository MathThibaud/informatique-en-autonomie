# Réussir l'épreuve pratique

!!! encadre "Le cadre"

    **1 heure**, **sur machine**, notée sur **8**. Avec la partie écrite (3 h 30, notée sur 12), elle forme l’épreuve de spécialité, de coefficient **16**. Le sujet est accompagné de fichiers Python (code de départ, données) déjà présents sur l’ordinateur. Il demande d’**écrire** du code, de le **tester** et de **corriger** un code fourni. Un examinateur est présent : il vient vous voir aux **appels professeur** indiqués dans le sujet, et peut intervenir à tout moment.

### S’entraîner pendant l’année

- Les **sujets 1 à 23** reprennent le format de la banque nationale ; ils sont disponibles sur la **plateforme de la classe**.

- Les **sujets 24 à 32**, écrits pour les chapitres de Terminale que les premiers travaillent peu, sont dans la **deuxième partie de ce livre** ; leurs corrigés sont en fin de livre.

- Traitez chaque sujet **en 1 heure chronométrée**, sans aide d’IA, puis seulement ensuite lisez le corrigé.

### Gérer l’heure

|  | **Lecture** | **Écrire et tester** | **Corriger un code fourni** | **Relecture** |
|:---|:--:|:--:|:--:|:--:|
| Durée indicative | 5 min | $\approx$ 25 min | $\approx$ 25 min | 5 min |

1.  **Lire tout le sujet**, puis **ouvrir les fichiers** fournis et les **exécuter** tels quels : on voit ce qui existe déjà et ce qui manque.

2.  **Repérer les appels professeur** : préparer, pour chacun, ce que l’on va montrer et dire.

3.  **Enregistrer souvent**, sous le nom de fichier demandé.

4.  **Bloqué plus de 5 minutes** ? Le dire à l’examinateur : une aide ponctuelle vaut mieux qu’une demi-heure perdue, et la suite du sujet reste accessible.

### Écrire, tester, corriger

- **Respecter la signature** imposée (nom de la fonction, paramètres, valeur renvoyée) : les tests de l’examinateur l’appellent telle quelle.

- **`return`, pas `print`** : une fonction renvoie son résultat ; un `print` sert seulement à tracer, et on le retire ensuite.

- **Tester** avec `assert` sur un cas courant *et* sur les cas limites (liste vide, un seul élément, élément absent, arbre vide `None`), en calculant le résultat attendu **à la main**.

- **Corriger un code fourni** : exécuter, lire le message d’erreur de bas en haut (type, puis ligne), trouver le plus petit exemple qui échoue, tracer les variables jusqu’à la première valeur inattendue, corriger **une seule chose**, puis relancer **tous** les tests.

!!! remarque "Remarque — À l’appel professeur"

    On montre le code qui s’exécute et on **explique** sa démarche : « j’attendais …, j’ai obtenu …; sur l’exemple …, la variable … vaut … au lieu de …; j’ai donc corrigé …». Une erreur bien localisée et bien expliquée est valorisée, même si la correction n’est pas terminée.

### Les erreurs qui coûtent des points

- Modifier le code fourni au-delà de ce qui est demandé, ou changer le nom d’une fonction.

- Rendre un fichier qui ne s’exécute plus (erreur de syntaxe laissée en fin d’épreuve) : mieux vaut une fonction incomplète mais un fichier qui tourne.

- Écrire des tests qui recopient le résultat obtenu au lieu du résultat attendu.

- Ne rien dire à l’appel professeur : l’explication orale fait partie de l’évaluation.
