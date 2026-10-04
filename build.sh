#!/bin/sh
# Régénère tout le site depuis les sources Overleaf : ./build.sh [niveaux...]
set -e
cd "$(dirname "$0")"
for d in Seconde Premiere Terminale; do git -C "$HOME/Documents/Overleaf/$d" pull -q || true; done
.venv/bin/python build/build.py "$@"
.venv/bin/python build/gen_css.py
.venv/bin/python build/gen_site.py
.venv/bin/mkdocs build -q 2>&1 | grep -v 'MkDocs 2.0\|│\|^.\[0m$' || true
