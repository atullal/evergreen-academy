#!/usr/bin/env python3
"""Render lessons/*.md into lessons/*.html wrapped in the site chrome.

Dependency-free on purpose (no pandoc/markdown lib on every machine).
Handles the narrow markdown subset our style guide allows: #/##/### headers,
paragraphs, **bold**, *italics*, ordered/unordered lists, and --- rules.
Run from the repo root: python3 build.py
"""
import html
import re
from pathlib import Path

CHROME = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Evergreen Digital Academy</title>
<meta name="description" content="Free, patient technology lessons for older adults.">
<link rel="stylesheet" href="../style.css">
</head>
<body>
<header class="site">
  <span class="textsize" id="textsize" hidden>
    <button class="b1" data-size="" aria-label="Normal text size">A</button>
    <button class="b2" data-size="size-lg" aria-label="Large text size">A</button>
    <button class="b3" data-size="size-xl" aria-label="Largest text size">A</button>
  </span>
  <div class="brand"><a href="../index.html">Evergreen Digital Academy</a></div>
  <p class="tagline">Free, patient technology lessons for older adults</p>
</header>
<nav class="crumbs"><a href="../index.html">&larr; All lessons</a></nav>
<main>
{body}
</main>
<footer class="site">
  <p>Evergreen Digital Academy · lessons are free to read, print, and share
  (CC BY-SA 4.0) · <span class="nolink"><a href="../about.html">about this project</a></span></p>
</footer>
<script>
(function () {{
  var box = document.getElementById('textsize');
  if (!box) return;
  box.hidden = false;
  var saved = localStorage.getItem('ega-size') || '';
  if (saved) document.documentElement.classList.add(saved);
  box.addEventListener('click', function (e) {{
    var b = e.target.closest('button'); if (!b) return;
    document.documentElement.classList.remove('size-lg', 'size-xl');
    if (b.dataset.size) document.documentElement.classList.add(b.dataset.size);
    localStorage.setItem('ega-size', b.dataset.size);
  }});
}})();
</script>
</body>
</html>
"""


def inline(text):
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    return text


def render(md):
    out, para, mode = [], [], None  # mode: None | 'ul' | 'ol'

    def flush_para():
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para.clear()

    def close_list():
        nonlocal mode
        if mode:
            out.append("</%s>" % mode)
            mode = None

    item = []

    def flush_item():
        if item:
            out.append("<li>" + inline(" ".join(item)) + "</li>")
            item.clear()

    for raw in md.splitlines():
        line = raw.rstrip()
        stripped = line.strip()
        m = re.match(r"^(#{1,3}) (.+)$", line)
        if m:
            flush_item(); close_list(); flush_para()
            level = len(m.group(1))
            out.append("<h%d>%s</h%d>" % (level, inline(m.group(2)), level))
        elif stripped == "---":
            flush_item(); close_list(); flush_para()
            out.append("<hr>")
        elif re.match(r"^\d+\. ", stripped):
            flush_para(); flush_item()
            if mode != "ol":
                close_list(); out.append('<ol class="steps">'); mode = "ol"
            item.append(re.sub(r"^\d+\. ", "", stripped))
        elif stripped.startswith("- "):
            flush_para(); flush_item()
            if mode != "ul":
                close_list(); out.append("<ul>"); mode = "ul"
            item.append(stripped[2:])
        elif stripped == "":
            flush_item(); close_list(); flush_para()
        elif mode and (raw.startswith("   ") or raw.startswith("  ")):
            item.append(stripped)  # continuation of a list item
        else:
            flush_item(); close_list()
            para.append(stripped)
    flush_item(); close_list(); flush_para()
    return "\n".join(out)


def main():
    for src in sorted(Path("lessons").glob("*.md")):
        md = src.read_text(encoding="utf-8")
        title_m = re.search(r"^# (.+)$", md, re.M)
        title = title_m.group(1) if title_m else src.stem
        body = render(md)
        dst = src.with_suffix(".html")
        dst.write_text(CHROME.format(title=html.escape(title), body=body),
                       encoding="utf-8")
        print("built", dst)


if __name__ == "__main__":
    main()
