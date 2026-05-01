#!/usr/bin/env python3
"""
Genera páginas Hugo de publicaciones a partir de GRAFO.bib.

Uso:
    python3 scripts/bib_to_publications.py

- Solo procesa entradas donde aparece "Isaac Lozano-Osorio" como autor.
- Salta publicaciones cuyo slug ya existe en content/publication/.
- Para forzar sobreescritura: python3 scripts/bib_to_publications.py --overwrite
"""

import re, os, sys

ISAAC_NAMES = ['Lozano-Osorio, Isaac', 'Isaac Lozano-Osorio', 'I. Lozano-Osorio']
BIB_FILE = 'GRAFO.bib'
DEST_DIR = 'content/publication'
OVERWRITE = '--overwrite' in sys.argv

def unescape_latex(s):
    s = re.sub(r"\{\\'([aeiouAEIOU])\}", r'\1', s)
    s = re.sub(r"\\'\{?([aeiouAEIOU])\}?", r'\1', s)
    s = re.sub(r'\{\\"([aeiouAEIOU])\}', r'\1', s)
    s = re.sub(r'\\"([aeiouAEIOU])', r'\1', s)
    s = re.sub(r'\{\\~([nN])\}', r'\1', s)
    s = re.sub(r'\\~([nN])', r'\1', s)
    s = re.sub(r'\{\\c\{([cC])\}\}', r'\1', s)
    s = re.sub(r'\{\\ss\}', 'ss', s)
    s = re.sub(r"\\`\{?([aeiouAEIOU])\}?", r'\1', s)
    s = re.sub(r'\{([^{}]+)\}', r'\1', s)
    s = re.sub(r'\{([^{}]+)\}', r'\1', s)
    s = re.sub(r'[{}\\]', '', s)
    return s.strip()

def parse_field(entry, field):
    m = re.search(rf'^\s+{field}\s*=\s*\{{(.*?)\}}[,\n]', entry,
                  re.DOTALL | re.MULTILINE | re.IGNORECASE)
    if m:
        return unescape_latex(re.sub(r'\s+', ' ', m.group(1)).strip())
    m2 = re.search(rf'^\s+{field}\s*=\s*"(.*?)"[,\n]', entry,
                   re.DOTALL | re.MULTILINE | re.IGNORECASE)
    if m2:
        return unescape_latex(re.sub(r'\s+', ' ', m2.group(1)).strip())
    return ''

def format_authors(raw):
    parts = re.split(r'\s+and\s+', raw, flags=re.IGNORECASE)
    result = []
    for p in parts:
        p = p.strip()
        if ',' in p:
            last, first = p.split(',', 1)
            result.append(f"{first.strip()} {last.strip()}")
        else:
            result.append(p)
    return result

def pub_type(etype):
    return {'article': '2', 'inproceedings': '1', 'proceedings': '1',
            'phdthesis': '7', 'incollection': '6'}.get(etype, '1')

def make_slug(key):
    return key.lower().replace('_', '-')

def safe_yaml_str(s):
    return s.replace('"', "'").replace('\\', '')

def make_md(key, entry):
    etype = (re.match(r'@(\w+)\{', entry) or [None, 'misc'])[1].lower()
    title   = parse_field(entry, 'title')
    authors = format_authors(parse_field(entry, 'author'))
    year    = parse_field(entry, 'year') or '2020'
    abstract= parse_field(entry, 'abstract')
    doi     = parse_field(entry, 'doi')
    journal = parse_field(entry, 'journal')
    booktitle = parse_field(entry, 'booktitle')
    url     = parse_field(entry, 'url')

    venue    = journal or booktitle or ''
    doi_url  = f'https://doi.org/{doi}' if doi else ''
    pub_url  = url or doi_url
    featured = 'true' if authors and any(n in authors[0] for n in ['Lozano-Osorio', 'Isaac']) else 'false'
    authors_yaml = '\n'.join(f'  - {a}' for a in authors)

    return f"""---
title: "{safe_yaml_str(title)}"
authors:
{authors_yaml}
date: {year}-01-01
doi: "{doi}"
publication_types: ["{pub_type(etype)}"]
publication: "*{safe_yaml_str(venue)}*"
abstract: "{safe_yaml_str(abstract)}"
featured: {featured}
url_pdf: "{pub_url}"
---
"""

def main():
    with open(BIB_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    raw_entries = re.split(r'\n(?=@)', content)
    isaac = {}
    for e in raw_entries:
        if any(n in e for n in ISAAC_NAMES):
            m = re.match(r'@\w+\{(\S+),', e)
            if m:
                isaac[m.group(1)] = e

    print(f"Encontradas {len(isaac)} publicaciones de Isaac Lozano-Osorio")
    created, skipped = 0, 0

    for key, entry in isaac.items():
        slug = make_slug(key)
        dest = os.path.join(DEST_DIR, slug)
        if os.path.exists(dest) and not OVERWRITE:
            print(f"  · Saltando {slug} (ya existe)")
            skipped += 1
            continue
        os.makedirs(dest, exist_ok=True)
        with open(os.path.join(dest, 'index.md'), 'w', encoding='utf-8') as f:
            f.write(make_md(key, entry))
        title = parse_field(entry, 'title')[:55]
        print(f"  ✓ {slug}: {title}...")
        created += 1

    print(f"\nCreadas: {created}  |  Saltadas: {skipped}")
    print("Ahora ejecuta: hugo server")

if __name__ == '__main__':
    main()
