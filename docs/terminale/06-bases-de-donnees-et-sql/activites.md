# Activités préparatoires

<p class="sous-titre">Bases de données et SQL</p>

## <span class="etiquette">Activité 1</span> Le grand tableau du secrétariat

*quand un seul tableau ne suffit plus*

<p class="infos-activite">Durée : 25 min · Sans ordinateur, par deux</p>

!!! consignes "Consignes"

    - On répond sur le cahier : on repère, on compte, on recopie. Aucun mot de vocabulaire n’est attendu avant l’exercice 4.

### <span class="exo-num">Exercice 1</span> — Le tableau tout-en-un <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-06-bases-de-donnees-et-sql-act-1-1 }

Le secrétariat d’un lycée note tout dans un seul tableau, partagé entre plusieurs personnes. Voici un extrait :

|  | **Nom** | **Prénom** | **Classe** | **Prof. principal** | **Salle** | **Matière** | **Note** | **Date** |
|:--:|:---|:---|:---|:---|:--:|:---|:--:|:---|
| 1 | Martin | Léa | TNSI1 | M. Rossi | B12 | NSI | 15 | 12/09 |
| 2 | Bianchi | Hugo | TNSI1 | M. Rossi | B12 | NSI | 11 | 12/09 |
| 3 | Martin | Léa | TNSI2 | Mme Costa | C04 | NSI | 17 | 12/09 |
| 4 | Martin | Léa | TNSI1 | M. Rosi | B12 | Maths | 13 | 15/09 |
| 5 | Bianci | Hugo | TNSI1 | M. Rossi | B21 | Maths | 9 | 15/09 |
| 6 | Durand | Noé | TNSI2 | Mme Costa | C04 | NSI | 23 | 12/09 |
| 7 | Durand | Noé | T NSI 2 | Mme Costa | C04 | Maths | abs | 2026-09-15 |
| 8 | Silva | Inès | TNSI2 | Mme Costa | C04 | NSI | 14 | 12/09 |

1.  Combien de fois le nom du professeur principal de la TNSI1 est-il écrit ? Et la salle de la TNSI1 ?

2.  Repérer dans le tableau **au moins cinq** anomalies (noter le numéro de ligne et la colonne), et les classer : faute de frappe, valeur impossible, même chose écrite de deux façons, information contradictoire.

3.  Les lignes 1 et 3 parlent-elles de la même élève ? Les lignes 1 et 4 ? Comment en être sûr ?

4.  La TNSI1 déménage en salle B15. Combien de cases faut-il modifier ? Que se passe-t-il si l’on en oublie une ?

5.  Zoé Petit arrive en TNSI1 ; elle n’a encore aucune note. Comment l’inscrire dans ce tableau ?

6.  On efface la ligne 8 (la note avait été saisie par erreur). Quelle autre information disparaît avec elle ?

??? corrige "Corrigé"

    1.  « M. Rossi » est écrit $4$ fois (lignes 1, 2, 4, 5 — dont une fois mal orthographié) ; la salle de la TNSI1, $4$ fois aussi (trois fois B12, une fois B21). L’information « la TNSI1 a M. Rossi en salle B12 » est **recopiée** sur chaque ligne d’élève de la classe : c’est la **redondance**.

    2.  Anomalies (on en attend au moins cinq) :

        - **fautes de frappe** : « M. Rosi » (ligne 4), « Bianci » (ligne 5) ;

        - **information contradictoire** : salle B21 pour la TNSI1 (ligne 5) alors que les autres lignes disent B12 ;

        - **valeur impossible** : la note $23$ (ligne 6) ;

        - **même chose écrite de deux façons** : « T NSI 2 » au lieu de « TNSI2 », la date « 2026-09-15 » au lieu de « 15/09 » (ligne 7) ;

        - **valeur d’une autre nature** : « abs » dans une colonne de nombres (ligne 7) — une absence n’est pas une note.

    3.  Lignes 1 et 3 : deux classes différentes, donc *probablement* deux élèves homonymes… mais rien ne le garantit (Léa a pu changer de classe). Lignes 1 et 4 : même classe, sans doute la même élève, mais là encore on **devine**. Pour en être sûr, il faudrait un **numéro unique** par élève.

    4.  $4$ cases (lignes 1, 2, 4, 5). Si l’on en oublie une, le tableau donne deux salles différentes pour la même classe : il devient **incohérent**. (Le nom savant, hors programme : *anomalie de mise à jour*.)

    5.  On ne peut l’inscrire qu’en laissant vides les cases Matière, Note et Date, ce qui n’a pas de sens pour une ligne « de note » — ou en inventant une fausse note. Le tableau mélange deux choses : « qui est l’élève » et « quelle note a-t-elle eue ».

    6.  En effaçant sa seule note, on efface aussi **l’existence** d’Inès Silva et le fait qu’elle est en TNSI2 : le secrétariat ne sait plus qu’elle est inscrite.

### <span class="exo-num">Exercice 2</span> — Deux secrétaires, un seul fichier <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-06-bases-de-donnees-et-sql-act-1-2 }

Le fichier du tableau est rangé sur un disque partagé. À 10 h 00, Mme Leroy l’ouvre et ajoute la note de Zoé. À 10 h 01, M. Giraud ouvre **le même fichier** et corrige « Bianci » en « Bianchi ». Mme Leroy enregistre à 10 h 05, M. Giraud à 10 h 06.

1.  Que contient le fichier à 10 h 07 ? Quel travail a été perdu, et pourquoi ?

2.  Imaginer une règle que le logiciel devrait appliquer pour que cela n’arrive pas.

??? corrige "Corrigé"

    1.  Le fichier contient la version de M. Giraud : « Bianchi » est corrigé, mais la note de Zoé **a disparu**. Chacun a travaillé sur sa propre copie du fichier, ouverte avant que l’autre n’enregistre ; le dernier qui enregistre écrase le travail de l’autre.

    2.  Exemples de règles : bloquer le fichier (ou seulement la ligne) pendant qu’une personne le modifie ; enregistrer modification par modification au lieu du fichier entier ; prévenir la seconde personne qu’une autre version a été enregistrée entre-temps. C’est ce que fait un SGBD (gestion des **accès concurrents**, transactions).

### <span class="exo-num">Exercice 3</span> — Découper le tableau <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-06-bases-de-donnees-et-sql-act-1-3 }

On décide de ranger les informations dans **trois** tableaux plus petits, chacun ne parlant que d’une seule chose. Corriger les anomalies au passage.

1.  Sur le cahier, construire et remplir les trois tableaux suivants (une ligne par classe, une ligne par élève, une ligne par note) ; seules leurs colonnes sont données.

    <table>
    <thead>
    <tr>
    <th colspan="3" style="text-align: left;"><strong>CLASSE</strong></th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: left;"><strong>Code</strong></td>
    <td style="text-align: left;"><strong>Prof. princ.</strong></td>
    <td style="text-align: left;"><strong>Salle</strong></td>
    </tr>
    </tbody>
    </table>

    <table>
    <thead>
    <tr>
    <th colspan="4" style="text-align: left;"><strong>ÉLÈVE</strong></th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: left;"><strong>…</strong></td>
    <td style="text-align: left;"><strong>Nom</strong></td>
    <td style="text-align: left;"><strong>Prénom</strong></td>
    <td style="text-align: left;"><strong>Classe</strong></td>
    </tr>
    </tbody>
    </table>

    <table>
    <thead>
    <tr>
    <th colspan="4" style="text-align: left;"><strong>NOTE</strong></th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: left;"><strong>Élève</strong></td>
    <td style="text-align: left;"><strong>Matière</strong></td>
    <td style="text-align: left;"><strong>Note</strong></td>
    <td style="text-align: left;"><strong>Date</strong></td>
    </tr>
    </tbody>
    </table>

2.  Dans ÉLÈVE, deux élèves ont les mêmes nom et prénom. Inventer une **première colonne** (titre « …») qui permette de les distinguer à coup sûr. Que met-on alors dans la colonne « Élève » de NOTE, et pourquoi pas le nom ?

3.  Reprendre les questions 4, 5 et 6 avec ces trois tableaux : que deviennent les problèmes ?

4.  Écrire deux **règles** qu’un logiciel pourrait vérifier tout seul à chaque saisie, pour refuser les anomalies de l’exercice 1.

??? corrige "Corrigé"

    1.  Un découpage possible (les anomalies sont corrigées ; la note 23 est à vérifier auprès du professeur, l’absence n’est pas une note) :

        <table>
        <thead>
        <tr>
        <th colspan="3" style="text-align: left;"><strong>CLASSE</strong></th>
        </tr>
        </thead>
        <tbody>
        <tr>
        <td style="text-align: center;"><strong>Code</strong></td>
        <td style="text-align: left;"><strong>Prof. princ.</strong></td>
        <td style="text-align: center;"><strong>Salle</strong></td>
        </tr>
        <tr>
        <td style="text-align: center;">TNSI1</td>
        <td style="text-align: left;">M. Rossi</td>
        <td style="text-align: center;">B12</td>
        </tr>
        <tr>
        <td style="text-align: center;">TNSI2</td>
        <td style="text-align: left;">Mme Costa</td>
        <td style="text-align: center;">C04</td>
        </tr>
        </tbody>
        </table>

        <table>
        <thead>
        <tr>
        <th colspan="4" style="text-align: left;"><strong>ÉLÈVE</strong></th>
        </tr>
        </thead>
        <tbody>
        <tr>
        <td style="text-align: center;"><strong>Num.</strong></td>
        <td style="text-align: left;"><strong>Nom</strong></td>
        <td style="text-align: left;"><strong>Prénom</strong></td>
        <td style="text-align: center;"><strong>Classe</strong></td>
        </tr>
        <tr>
        <td style="text-align: center;">1</td>
        <td style="text-align: left;">Martin</td>
        <td style="text-align: left;">Léa</td>
        <td style="text-align: center;">TNSI1</td>
        </tr>
        <tr>
        <td style="text-align: center;">2</td>
        <td style="text-align: left;">Bianchi</td>
        <td style="text-align: left;">Hugo</td>
        <td style="text-align: center;">TNSI1</td>
        </tr>
        <tr>
        <td style="text-align: center;">3</td>
        <td style="text-align: left;">Martin</td>
        <td style="text-align: left;">Léa</td>
        <td style="text-align: center;">TNSI2</td>
        </tr>
        <tr>
        <td style="text-align: center;">4</td>
        <td style="text-align: left;">Durand</td>
        <td style="text-align: left;">Noé</td>
        <td style="text-align: center;">TNSI2</td>
        </tr>
        <tr>
        <td style="text-align: center;">5</td>
        <td style="text-align: left;">Silva</td>
        <td style="text-align: left;">Inès</td>
        <td style="text-align: center;">TNSI2</td>
        </tr>
        <tr>
        <td style="text-align: center;">6</td>
        <td style="text-align: left;">Petit</td>
        <td style="text-align: left;">Zoé</td>
        <td style="text-align: center;">TNSI1</td>
        </tr>
        </tbody>
        </table>

        <table>
        <thead>
        <tr>
        <th colspan="4" style="text-align: left;"><strong>NOTE</strong></th>
        </tr>
        </thead>
        <tbody>
        <tr>
        <td style="text-align: center;"><strong>Élève</strong></td>
        <td style="text-align: left;"><strong>Matière</strong></td>
        <td style="text-align: center;"><strong>Note</strong></td>
        <td style="text-align: center;"><strong>Date</strong></td>
        </tr>
        <tr>
        <td style="text-align: center;">1</td>
        <td style="text-align: left;">NSI</td>
        <td style="text-align: center;">15</td>
        <td style="text-align: center;">12/09</td>
        </tr>
        <tr>
        <td style="text-align: center;">2</td>
        <td style="text-align: left;">NSI</td>
        <td style="text-align: center;">11</td>
        <td style="text-align: center;">12/09</td>
        </tr>
        <tr>
        <td style="text-align: center;">3</td>
        <td style="text-align: left;">NSI</td>
        <td style="text-align: center;">17</td>
        <td style="text-align: center;">12/09</td>
        </tr>
        <tr>
        <td style="text-align: center;">1</td>
        <td style="text-align: left;">Maths</td>
        <td style="text-align: center;">13</td>
        <td style="text-align: center;">15/09</td>
        </tr>
        <tr>
        <td style="text-align: center;">2</td>
        <td style="text-align: left;">Maths</td>
        <td style="text-align: center;">9</td>
        <td style="text-align: center;">15/09</td>
        </tr>
        <tr>
        <td style="text-align: center;">4</td>
        <td style="text-align: left;">NSI</td>
        <td style="text-align: center;">?</td>
        <td style="text-align: center;">12/09</td>
        </tr>
        <tr>
        <td style="text-align: center;">5</td>
        <td style="text-align: left;">NSI</td>
        <td style="text-align: center;">14</td>
        <td style="text-align: center;">12/09</td>
        </tr>
        </tbody>
        </table>

        La ligne « abs » de Noé disparaît des notes (ou va dans un futur tableau ABSENCE).

    2.  Le **numéro** de l’élève. Dans NOTE, on écrit ce numéro et non le nom : le nom n’est pas unique (deux Léa Martin) et peut être mal orthographié ; le numéro désigne **une seule** ligne d’ÉLÈVE, où le nom n’est écrit qu’une fois.

    3.  Déménagement : **une seule** case à changer (dans CLASSE). Zoé : une ligne dans ÉLÈVE, aucune dans NOTE. Supprimer la note d’Inès : elle reste dans ÉLÈVE. Les trois problèmes disparaissent parce que chaque information n’est écrite **qu’une fois**, dans le tableau qui la concerne.

    4.  Exemples : « une note est un nombre compris entre $0$ et $20$ » ; « la classe d’un élève doit exister dans CLASSE » ; « le numéro d’élève de NOTE doit exister dans ÉLÈVE » ; « deux élèves n’ont jamais le même numéro » ; « la date s’écrit toujours sous la même forme ».

### <span class="exo-num">Exercice 4</span> — Mettre des mots <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-06-bases-de-donnees-et-sql-act-1-4 }

1.  Sur le cahier, proposer un nom pour chacune des notions suivantes.

    1.  un des trois petits tableaux (CLASSE, ÉLÈVE, NOTE) ;

    2.  une colonne / une ligne d’un de ces tableaux ;

    3.  la colonne inventée qui distingue chaque élève à coup sûr ;

    4.  la colonne « Élève » de NOTE, qui renvoie vers une ligne d’ÉLÈVE ;

    5.  une règle comme « une note est comprise entre 0 et 20 » ;

    6.  le logiciel qui range les tableaux, vérifie les règles et gère les modifications simultanées.

2.  Recopier et compléter : « Un simple fichier partagé ne sait pas garantir que les données restent …, ni que plusieurs personnes puissent …»

??? corrige "Corrigé"

    1.  Propositions fréquentes, puis mots du cours :

        | **Notion** | **Propositions fréquentes** | **Mot du cours** |
        |:---|:---|:---|
        | un des petits tableaux | tableau, feuille, fiche | **relation** (ou **table**) |
        | une colonne / une ligne | champ / fiche | **attribut** / **enregistrement** |
        | la colonne qui distingue chaque élève | numéro, identifiant, matricule | **clé primaire** |
        | la colonne qui renvoie vers ÉLÈVE | lien, renvoi, pointeur | **clé étrangère** |
        | « une note est entre 0 et 20 » | règle, condition | **contrainte** (d’intégrité) |
        | le logiciel qui gère tout | gestionnaire, serveur | **SGBD** |

    2.  … restent **cohérentes** ; … puissent les **modifier en même temps** sans se gêner (accès concurrents).
