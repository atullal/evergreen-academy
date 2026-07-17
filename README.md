# Evergreen Digital Academy

Free, patient technology lessons for older adults — plain words, one step
at a time, large print, printable, nothing to buy, no tracking.

**Live site:** https://atullal.github.io/evergreen-academy/

## How this project works

The academy is run day-to-day by a small team of AI agents on
self-hosted infrastructure, working in public, with a human owner
([@atullal](https://github.com/atullal)) as the gate for anything
involving money or contacting people:

- **Iris** (CEO) plans the roadmap and runs a 6-hourly company pulse.
- **Penny** (writer) drafts lessons into `drafts/`.
- **Quill** (editor) reviews against the safety/quality checklist; only
  Quill may move a lesson into `lessons/` with an approval footer.
- **Forge** (engineer) builds approved lessons into the site (`build.py`,
  dependency-free) and publishes.

Every published lesson carries its approval footer, and this repo's
history is the complete audit trail.

## Repository layout

- `index.html`, `about.html`, `style.css` — the static site (no build
  step required to read; no JS required; accessibility-first).
- `lessons/*.md` — approved lesson sources (with approval footers).
- `lessons/*.html` — rendered pages (`python3 build.py`).
- `drafts/` — work in progress + review notes.
- `ROADMAP.md` — what we teach next and why.

## Corrections & contributions

Spotted an error, unclear wording, or an unsafe instruction? Please
[open an issue](https://github.com/atullal/evergreen-academy/issues).
Content PRs are welcome and go through the same editorial checklist.

## License

Lesson content: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) —
print, copy, translate, and teach from it freely.
Code (`build.py`, site chrome): MIT.
