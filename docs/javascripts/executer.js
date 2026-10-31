// Exécuter le Python des pages dans le navigateur (Pyodide, chargé au premier clic seulement).
// Chaque bloc Python reçoit « ▶ Exécuter » et « ✎ Modifier » ; le bouton « Python » en bas à
// droite ouvre un éditeur libre pour programmer et tester les exercices.
(function () {
  const PYODIDE = "https://cdn.jsdelivr.net/pyodide/v0.26.4/full/";
  const DUREE_MAX = 5;   // secondes avant d'arrêter une boucle infinie
  // Blocs qui ne peuvent pas tourner ici : fenêtres graphiques, console interactive.
  const NON_EXECUTABLE = /^\s*(import|from)\s+(turtle|tkinter|matplotlib|pygame|micro(bit|python)?|machine)\b|^\s*>>>/m;

  const RUNNER = `
import sys, io, time, traceback

class TempsDepasse(BaseException):
    pass

def __executer(src):
    sortie = io.StringIO()
    anciens = sys.stdout, sys.stderr
    sys.stdout = sys.stderr = sortie
    limite = time.time() + ${DUREE_MAX}
    compte = [0]

    def trace(frame, evenement, arg):
        compte[0] += 1
        if compte[0] % 500 == 0 and time.time() > limite:
            raise TempsDepasse()
        return trace

    def saisie(invite=""):
        print(invite, end="")
        import js
        r = js.prompt(str(invite))
        if r is None:
            raise KeyboardInterrupt("saisie annulée")
        print(r)
        return r

    espace = {"__name__": "__main__", "input": saisie}
    sys.settrace(trace)
    try:
        exec(compile(src, "<programme>", "exec"), espace)
    except TempsDepasse:
        sys.settrace(None)
        print("\\n⏱ Programme arrêté au bout de ${DUREE_MAX} s : boucle infinie ?")
    except BaseException:
        sys.settrace(None)
        t, e, tb = sys.exc_info()
        traceback.print_exception(t, e, tb.tb_next)
    finally:
        sys.settrace(None)
        sys.stdout, sys.stderr = anciens
    return sortie.getvalue()
`;

  let chargement = null;
  function pyodide() {
    if (!chargement) {
      chargement = new Promise((ok, ko) => {
        const s = document.createElement("script");
        s.src = PYODIDE + "pyodide.js";
        s.onload = ok;
        s.onerror = () => ko(new Error("impossible de charger Python (connexion ?)"));
        document.head.appendChild(s);
      }).then(() => loadPyodide({ indexURL: PYODIDE }))
        .then(py => { py.runPython(RUNNER); return py; })
        .catch(e => { chargement = null; throw e; });
    }
    return chargement;
  }

  async function executer(code, zone) {
    zone.hidden = false;
    zone.classList.remove("erreur");
    zone.textContent = chargement ? "Exécution…" : "Chargement de Python (quelques secondes la première fois)…";
    try {
      const py = await pyodide();
      // laisse le navigateur afficher le message avant de bloquer pendant l'exécution
      await new Promise(r => setTimeout(r, 20));
      const res = py.globals.get("__executer")(code);
      zone.textContent = res.trim() ? res.replace(/\s+$/, "")
        : "(aucun affichage : le programme ne fait peut-être que définir des fonctions ; ✎ Modifier pour ajouter un appel)";
      zone.classList.toggle("erreur", /Traceback|⏱/.test(res));
    } catch (e) {
      zone.textContent = "Erreur : " + e.message;
      zone.classList.add("erreur");
    }
  }

  // ---------------------------------------------------------------- éditeur libre
  const BROUILLON = "nsi-editeur-python";
  function lireBrouillon() { try { return localStorage.getItem(BROUILLON) || ""; } catch (e) { return ""; } }
  function ecrireBrouillon(v) { try { localStorage.setItem(BROUILLON, v); } catch (e) { /* stockage refusé */ } }

  function editeur() {
    let p = document.getElementById("editeur-python");
    if (p) return p;
    p = document.createElement("section");
    p.id = "editeur-python";
    p.hidden = true;
    p.setAttribute("aria-label", "Éditeur Python");
    p.innerHTML =
      '<div class="ep-tete"><strong>Éditeur Python</strong>' +
      '<span class="ep-info">exécuté dans votre navigateur</span>' +
      '<button type="button" class="ep-fermer" aria-label="Fermer l\'éditeur">✕</button></div>' +
      '<textarea spellcheck="false" autocapitalize="off" aria-label="Code Python"' +
      ' placeholder="# Écrivez votre programme ici, puis ▶ Exécuter (Ctrl+Entrée)"></textarea>' +
      '<div class="ep-actions"><button type="button" class="ep-run">▶ Exécuter</button>' +
      '<button type="button" class="ep-vider">Effacer</button></div>' +
      '<pre class="sortie-python" hidden></pre>';
    const ta = p.querySelector("textarea"), zone = p.querySelector("pre");
    ta.value = lireBrouillon();
    ta.addEventListener("input", () => ecrireBrouillon(ta.value));
    ta.addEventListener("keydown", e => {
      if (e.key === "Tab" && !e.shiftKey) {
        e.preventDefault();
        ta.setRangeText("    ", ta.selectionStart, ta.selectionEnd, "end");
        ecrireBrouillon(ta.value);
      } else if (e.key === "Enter" && (e.ctrlKey || e.metaKey)) {
        e.preventDefault();
        executer(ta.value, zone);
      }
    });
    p.querySelector(".ep-run").onclick = () => executer(ta.value, zone);
    p.querySelector(".ep-vider").onclick = () => { ta.value = ""; ecrireBrouillon(""); zone.hidden = true; ta.focus(); };
    p.querySelector(".ep-fermer").onclick = () => { p.hidden = true; };
    document.body.appendChild(p);

    const b = document.createElement("button");
    b.id = "ouvrir-editeur";
    b.type = "button";
    b.textContent = "▶ Python";
    b.title = "Ouvrir l'éditeur Python";
    b.onclick = () => { p.hidden = !p.hidden; if (!p.hidden) ta.focus(); };
    document.body.appendChild(b);
    return p;
  }

  function ouvrirDans(code) {
    const p = editeur(), ta = p.querySelector("textarea");
    p.hidden = false;
    ta.value = code;
    ecrireBrouillon(code);
    p.querySelector("pre").hidden = true;
    ta.focus();
  }

  // ---------------------------------------------------------------- boutons des blocs
  function decorer() {
    editeur();
    document.querySelectorAll(".md-typeset div.language-python").forEach(bloc => {
      if (bloc.dataset.executable) return;
      bloc.dataset.executable = "1";
      const code = bloc.querySelector("code");
      if (!code) return;
      const src = code.innerText.replace(/\n$/, "");
      if (NON_EXECUTABLE.test(src)) return;
      const barre = document.createElement("div");
      barre.className = "barre-python";
      const run = document.createElement("button");
      run.type = "button";
      run.textContent = "▶ Exécuter";
      const mod = document.createElement("button");
      mod.type = "button";
      mod.textContent = "✎ Modifier";
      mod.title = "Ouvrir ce code dans l'éditeur Python";
      const zone = document.createElement("pre");
      zone.className = "sortie-python";
      zone.hidden = true;
      zone.setAttribute("aria-live", "polite");
      run.onclick = () => executer(src, zone);
      mod.onclick = () => ouvrirDans(src);
      barre.append(run, mod);
      bloc.after(barre, zone);
    });
  }

  if (typeof document$ !== "undefined") document$.subscribe(decorer);
  else document.addEventListener("DOMContentLoaded", decorer);
})();
