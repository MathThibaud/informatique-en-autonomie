# Activités préparatoires

<p class="sous-titre">Architecture des ordinateurs et systèmes d'exploitation</p>

## <span class="etiquette">Activité 1</span> Perdu dans le terminal

*explorer un vrai Linux, sans souris*

<p class="infos-activite">Durée : 20 min · Par deux, sur un ordinateur</p>

!!! consignes "Consignes"

    - Ni installation, ni compte à créer. Les réponses se notent sur le cahier.

    - Ouvrir `https://bellard.org/jslinux/` et cliquer sur *click here* sur la ligne **x86 – Alpine Linux 3.12.0 – Console**. Attendre l’invite `localhost:~#`, puis cliquer dans la fenêtre noire.

    - On tape une commande, puis la touche **Entrée**. Les espaces comptent (on écrit `cd ..` avec une espace, jamais `cd..`), les majuscules aussi.

    - Ce Linux tourne *dans votre navigateur* : vous ne pouvez rien casser. En cas de doute, rechargez la page : tout revient à l’état de départ.

    - Le but n’est pas d’apprendre des commandes par cœur, mais de **deviner ce qu’elles font** en observant ce qu’elles affichent.

### <span class="exo-num">Exercice 1</span> — Où suis-je ? <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-09-architecture-des-ordinateurs-et-systemes-act-1-1 }

1.  Taper `pwd`. Qu’affiche le terminal ? Est-ce un nom de fichier, un nom de dossier, ou autre chose ?

2.  Taper `ls`. Combien d’éléments sont affichés ? Recopier leurs noms.

3.  Taper `cat readme.txt`. Que fait, d’après vous, la commande `cat` ?

??? corrige "Corrigé"

    **1.** Le terminal affiche `/root`. Ce n’est ni un simple nom de fichier ni un simple nom de dossier, mais un **chemin** : l’adresse du dossier où l’on se trouve (le répertoire courant).

    **2.** Quatre éléments : `bench.py`, `hello.c`, `hello.js`, `readme.txt`.

    **3.** `cat` affiche le **contenu** d’un fichier texte (ici un petit mode d’emploi en anglais qui commence par *Some tests*).

### <span class="exo-num">Exercice 2</span> — Se déplacer <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-09-architecture-des-ordinateurs-et-systemes-act-1-2 }

1.  Taper `cd /`, puis `pwd`, puis `ls`. Le dossier `/` contient-il le dossier où vous étiez au départ ? Pourquoi, à votre avis, appelle-t-on `/` la **racine** ?

2.  Taper `cd root`, puis `pwd`. Taper ensuite `cd ..`, puis `pwd`. Que désigne `..` ?

3.  Depuis n’importe où, taper `cd` tout seul, puis `pwd`. Où arrive-t-on ?

4.  Depuis votre point de départ, on peut atteindre `bin` par `cd /bin` ou par `cd ../bin`. Essayer les deux. Quelle est la différence d’écriture entre ces deux *chemins* ?

??? corrige "Corrigé"

    **4.** `pwd` affiche `/` ; `ls` affiche `bin dev etc home lib media mnt opt proc root run sbin srv sys tmp usr var`. Le dossier `root` du départ est bien dedans : tous les dossiers partent de `/`, comme les branches d’un arbre partent de sa racine.

    **5.** Après `cd root` : `/root`. Après `cd ..` : `/`. Le symbole `..` désigne le dossier **parent**, un cran au-dessus.

    **6.** On revient dans `/root`, le **répertoire personnel** de l’utilisateur.

    **7.** Les deux mènent à `/bin`. `/bin` commence par `/` : on part de la racine (chemin **absolu**, valable de partout). `../bin` part de l’endroit où l’on est (chemin **relatif**, qui ne marche que depuis `/root` ou un autre dossier situé juste sous la racine).

### <span class="exo-num">Exercice 3</span> — Créer <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-09-architecture-des-ordinateurs-et-systemes-act-1-3 }

1.  Revenir au point de départ. `mkdir` veut dire *make directory*. Créer un dossier `nsi`, entrer dedans, puis y créer un fichier vide avec `touch essai.txt`. Écrire les commandes tapées, dans l’ordre.

2.  Dessiner sur le cahier l’arbre des dossiers et fichiers à partir de `/root` (sans les éléments cachés).

??? corrige "Corrigé"

    **8.** `cd` (ou `cd /root`), `mkdir nsi`, `cd nsi`, `touch essai.txt` ; `ls` affiche `essai.txt`. Autre solution correcte : `mkdir nsi` puis `touch nsi/essai.txt` sans se déplacer.

    **9.**

    ```text
    /root/
    |-- bench.py
    |-- hello.c
    |-- hello.js
    |-- nsi/
    |   |-- essai.txt
    |-- readme.txt
    ```

### <span class="exo-num">Exercice 4</span> — Le fichier caché <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-09-architecture-des-ordinateurs-et-systemes-act-1-4 }

1.  Revenir au point de départ et taper `ls -a`. Quels noms nouveaux apparaissent ? Qu’ont-ils en commun ?

2.  L’un de ces dossiers cachés contient un dossier `firefox`, qui contient lui-même un fichier `profiles.ini`. Le retrouver (les dossiers s’affichent en bleu), puis l’afficher. Écrire le **chemin complet** de ce fichier, depuis la racine.

??? corrige "Corrigé"

    **10.** Apparaissent `.`, `..`, `.ash_history`, `.cache`, `.mozilla` et `.wine` : leur nom **commence par un point**. Ce sont des éléments **cachés**, que `ls` n’affiche pas sans l’option `-a` (souvent des réglages de programmes). `.` et `..` sont le dossier courant et le dossier parent. `.ash_history` est un fichier qui garde l’historique des commandes (son contenu varie).

    **11.** Par exemple : `cd .mozilla`, `ls` (on voit `extensions` et `firefox`), `cd firefox`, `ls`, `cat profiles.ini`. Le fichier contient des lignes comme `[Profile0]`, `Name=default-default`. Chemin complet :

    `/root/.mozilla/firefox/profiles.ini`

    On peut aussi faire, sans se déplacer, `cat .mozilla/firefox/profiles.ini`.

### <span class="exo-num">Exercice 5</span> — Ce qu’on a découvert <span class="ia ia-rouge" title="Sans IA : le but est l'automatisme lui-même"></span> { #ex-09-architecture-des-ordinateurs-et-systemes-act-1-5 }

1.  Recopier sur le cahier et compléter avec vos mots.

    - `pwd` affiche … ; `ls` …

    - `cd` … ; `..` désigne …

    - un chemin qui commence par `/` part … ; sinon, il part …

    - un nom qui commence par un point est …

??? corrige "Corrigé"

    **12.** Réponse possible :

    - `pwd` affiche le dossier où l’on est (le **répertoire courant**) ; `ls` affiche son contenu ;

    - `cd` change de dossier ; `..` désigne le dossier **parent** ;

    - un chemin qui commence par `/` part de la **racine** (chemin **absolu**) ; sinon il part du répertoire courant (chemin **relatif**) ;

    - un nom qui commence par un point est **caché** (visible avec `ls -a`).
