#!/usr/bin/env python3
"""Einmaliger Download der Originalpakete ohne Node/npm (Python-Standardbibliothek)."""
from pathlib import Path
import io, tarfile, urllib.request, shutil, sys

BASE = Path(__file__).resolve().parent / "www" / "lib"
VERSIONS = {
    "ionic": ("https://registry.npmjs.org/@ionic/core/-/core-8.8.19.tgz", "8.8.19"),
    "sqljs": ("https://registry.npmjs.org/sql.js/-/sql.js-1.16.0.tgz", "1.16.0"),
}

def unpack_selected(tar_bytes, target, predicate):
    count = 0
    target.mkdir(parents=True, exist_ok=True)
    with tarfile.open(fileobj=io.BytesIO(tar_bytes), mode="r:gz") as archive:
        for member in archive:
            if not member.isfile() or not member.name.startswith("package/"):
                continue
            rel = Path(member.name.removeprefix("package/"))
            if not predicate(rel):
                continue
            if ".." in rel.parts or rel.is_absolute():
                raise ValueError("Ungueltiger Paketpfad")
            dest = target / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            with archive.extractfile(member) as source, dest.open("wb") as output:
                shutil.copyfileobj(source, output)
            count += 1
    return count

def main():
    for name, (url, version) in VERSIONS.items():
        print(f"Lade {name} {version} von npm Registry (nur statische Dateien) ...")
        req = urllib.request.Request(url, headers={"User-Agent": "mw-ionic-starter/1.0"})
        with urllib.request.urlopen(req, timeout=90) as response:
            data = response.read()
        if name == "ionic":
            selector = lambda p: (p.parts[:2] == ("dist", "ionic") or p == Path("css/ionic.bundle.css") or p == Path("LICENSE"))
        else:
            selector = lambda p: p in (Path("dist/sql-wasm.js"), Path("dist/sql-wasm.wasm"), Path("LICENSE"))
        count = unpack_selected(data, BASE / name, selector)
        print(f"  {count} Dateien gespeichert")
    # sql.js Dateien stehen im Paket unter dist/, verschieben sie in lib/sqljs/
    for filename in ("sql-wasm.js", "sql-wasm.wasm"):
        source = BASE / "sqljs" / "dist" / filename
        if not source.is_file():
            raise RuntimeError("Datei fehlt im Paket: " + str(source))
        source.replace(BASE / "sqljs" / filename)
    (BASE / "sqljs" / "dist").rmdir()
    for file in (BASE / "ionic" / "dist" / "ionic" / "ionic.esm.js", BASE / "ionic" / "css" / "ionic.bundle.css", BASE / "sqljs" / "sql-wasm.wasm"):
        if not file.is_file(): raise RuntimeError("Erwartete Datei fehlt: " + str(file))
    print("Fertig: Jetzt python -m http.server 8000 -d www ausfuehren.")

if __name__ == "__main__":
    try: main()
    except Exception as e:
        print("Download fehlgeschlagen:", e, file=sys.stderr)
        sys.exit(1)
