"""Render every research markdown file to a styled PDF via pandoc + typst.

Usage: python3 pdfgen/build_pdfs.py [file.md ...]   (default: all root + output/*.md)
Output: output/pdf/<name>.pdf. Requires pandoc >= 3.1 and typst on PATH.
"""
import datetime
import pathlib
import re
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "output" / "pdf"
TEMPLATE = ROOT / "pdfgen" / "template.typ"
COMPACT = {"gonka_adi_partnership_onepager"}          # must stay one page
DATE_RE = re.compile(r"\*\*(?:Research |Analysis )?Date:\*\*\s*([^\n|]+)")


def split_front(text):
    """Pull the first H1 (and an immediately following H2) out of the body as title/subtitle."""
    lines = text.splitlines()
    title = subtitle = None
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i < len(lines) and lines[i].startswith("# "):
        title = lines[i][2:].strip()
        i += 1
        j = i
        while j < len(lines) and not lines[j].strip():
            j += 1
        if j < len(lines) and lines[j].startswith("## ") and j - i <= 1:
            subtitle = lines[j][3:].strip()
            i = j + 1
    return title, subtitle, "\n".join(lines[i:])


def doc_date(text, path):
    m = DATE_RE.search(text)
    if m:
        return re.sub(r"\s*\(.*", "", m.group(1)).strip().rstrip(".")
    mtime = datetime.date.fromtimestamp(path.stat().st_mtime)
    return mtime.strftime("%B %d, %Y")


def build(path):
    text = path.read_text()
    title, subtitle, body = split_front(text)
    title = title or path.stem.replace("_", " ")
    stem = path.stem
    header_title = re.sub(r"[*_`]", "", subtitle if subtitle and title.isupper() else title)
    if len(header_title) > 70:
        header_title = header_title[:67].rstrip() + "..."
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as tmp:
        tmp.write(body)
    pdf = OUT / f"{stem}.pdf"
    cmd = ["pandoc", tmp.name, "-f", "gfm+smart", "-t", "pdf", "--pdf-engine=typst",
           f"--template={TEMPLATE}", "-M", f"title={title}", "-M", f"header-title={header_title}",
           "-M", f"doc-date={doc_date(text, path)}", "-M", f"footer-left=gonka-tokenomics · {path.name}",
           "-o", str(pdf)]
    if subtitle:
        cmd += ["-M", f"subtitle={subtitle}"]
    if stem in COMPACT:
        cmd += ["-M", "compact=true"]
    r = subprocess.run(cmd, capture_output=True, text=True)
    pathlib.Path(tmp.name).unlink()
    if r.returncode:
        print(f"FAIL {path.name}\n{r.stderr[-1500:]}")
        return False
    pages = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
    n = re.search(r"Pages:\s+(\d+)", pages)
    warn = " (WARN)" if "warning" in r.stderr.lower() else ""
    print(f"ok   {pdf.name:50s} {n.group(1) if n else '?':>3} pages{warn}")
    return True


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    files = [pathlib.Path(a) for a in sys.argv[1:]] or sorted(
        p for p in list(ROOT.glob("*.md")) + list((ROOT / "output").glob("*.md")) if p.name != "README.md")
    ok = all([build(p) for p in files])
    sys.exit(0 if ok else 1)
