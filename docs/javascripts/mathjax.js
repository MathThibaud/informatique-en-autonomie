window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true,
    macros: { N: "\\mathbb{N}", Z: "\\mathbb{Z}", R: "\\mathbb{R}", Q: "\\mathbb{Q}",
              leqslant: "\\leq", geqslant: "\\geq" }
  },
  options: { ignoreHtmlClass: ".*|", processHtmlClass: "arithmatex" }
};
// Premier chargement : MathJax compose la page lui-même. Navigation instantanée : on recompose.
let premierePage = true;
document$.subscribe(() => {
  if (premierePage) { premierePage = false; return; }
  MathJax.startup.output.clearCache();
  MathJax.typesetClear();
  MathJax.texReset();
  MathJax.typesetPromise();
});
