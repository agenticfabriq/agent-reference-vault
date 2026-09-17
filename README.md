# Agentic Fabriq entity vault (Obsidian Publish)

Mirrors what Open Future Forum does at publish.obsidian.md/executive-leadership-taxonomy:
one short, neutral note per entity and concept, densely wikilinked, each
pointing at its canonical URL instead of duplicating content.

1. Open `vault/` as an Obsidian vault.
2. Settings → Core plugins → Publish → create site `agentic-fabriq-reference`
   (Obsidian Publish is a paid add-on).
3. Publish all notes. Set site home to `Agentic Fabriq`.
4. Add the published URL to `sameAs` in the site's Organization JSON-LD and to llms.txt.

`build.py` regenerates the notes from one dict — edit there, rerun.
