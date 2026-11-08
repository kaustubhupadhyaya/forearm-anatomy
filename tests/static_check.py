# -*- coding: utf-8 -*-
"""Static checks for the published artifact. No browser, no network.

    python tests/static_check.py

Verifies that the HTML, data files and image assets agree, and that no local
absolute paths or credential-looking strings are present.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from build_data import parse_muscles, slug  # noqa: E402

PLATES = ["palmar_sup", "palmar_deep", "dorsal_sup", "dorsal_deep"]
EXPECT = {"palmar_sup": 6, "palmar_deep": 3, "dorsal_sup": 10, "dorsal_deep": 7}
FAILS = []


def check(ok, name, detail=""):
    if not ok:
        FAILS.append((name, detail))
    print(("PASS " if ok else "FAIL ") + name + (("   [" + detail + "]") if detail and not ok else ""))


def main():
    html_path = ROOT / "forearm_mass_anatomy.html"
    html = html_path.read_text(encoding="utf-8")

    check(html_path.stat().st_size > 100_000, "HTML is present and non-trivial",
          "%d bytes" % html_path.stat().st_size)

    for plate in PLATES:
        img = ROOT / "images" / ("plate_%s.jpg" % plate)
        check(img.exists() and img.stat().st_size > 50_000, "image present: %s" % plate,
              str(img))
        check(('src="images/plate_%s.jpg"' % plate) in html,
              "HTML references image: %s" % plate)
        check(('href="images/plate_%s.jpg"' % plate) in html,
              "HTML reveal layer references image: %s" % plate)

    for plate, want in EXPECT.items():
        check(('id="view-%s"' % plate) in html, "view exists: %s" % plate)
        mg = len(re.findall(r'id="mg-%s-\d+"' % plate, html))
        tg = len(re.findall(r'id="tg-%s-\d+"' % plate, html))
        check(mg == want, "muscle groups: %s" % plate, "got %d want %d" % (mg, want))
        check(tg == want, "labels: %s" % plate, "got %d want %d" % (tg, want))

    rows = parse_muscles(html)
    check(len(rows) == 20, "HTML table has 20 muscles", "got %d" % len(rows))
    check([r["rank"] for r in rows] == list(range(1, 21)), "ranks are 1..20")
    check(len({r["name"] for r in rows}) == 20, "muscle names are unique")
    check(all(r["volume_cm3"] > 0 and r["pcsa_cm2"] > 0 for r in rows),
          "all volumes and PCSA values are positive")

    data = json.loads((ROOT / "data" / "muscles.json").read_text(encoding="utf-8"))
    check(data["count"] == 20 and len(data["muscles"]) == 20, "data/muscles.json has 20 rows")
    by_id = {m["id"]: m for m in data["muscles"]}
    for r in rows:
        m = by_id.get(slug(r["name"]))
        check(m is not None, "data row exists: %s" % r["name"])
        if m is None:
            continue
        same = (
            m["rank"] == r["rank"]
            and m["volume_cm3"] == r["volume_cm3"]
            and m["volume_pct"] == r["volume_pct"]
            and m["pcsa_cm2"] == r["pcsa_cm2"]
            and m["moment_arm"] == r["moment_arm"]
            and m["tier"] == r["tier"]
        )
        check(same, "data matches HTML: %s" % r["name"])

    vol = round(sum(r["volume_cm3"] for r in rows), 1)
    pct = round(sum(r["volume_pct"] for r in rows), 1)
    check(data["totals"]["volume_cm3"] == vol, "volume total matches table",
          "%s vs %s" % (data["totals"]["volume_cm3"], vol))
    check(data["totals"]["volume_pct"] == pct, "percentage total matches table",
          "%s vs %s" % (data["totals"]["volume_pct"], pct))

    ex = json.loads((ROOT / "data" / "exercises.json").read_text(encoding="utf-8"))
    check(ex["count"] == 8 and len(ex["exercises"]) == 8, "data/exercises.json has 8 records")
    need = {"id", "name", "category", "tier", "primary_muscles",
            "secondary_muscles", "biomechanics", "optimal_prescription"}
    check(all(need <= set(e) for e in ex["exercises"]), "exercise records have required fields")

    grouped = json.loads((ROOT / "data" / "muscles_grouped.json").read_text(encoding="utf-8"))
    check(grouped["count"] == len(grouped["muscles"]), "grouped muscle count is consistent")

    text_exts = {".html", ".py", ".json", ".md", ".yml", ".yaml", ".txt"}
    bad_paths = []
    bad_secrets = []
    for p in ROOT.rglob("*"):
        if not p.is_file() or p.suffix.lower() not in text_exts:
            continue
        if ".git" in p.parts:
            continue
        t = p.read_text(encoding="utf-8", errors="ignore")
        if re.search(r"C:[\\/]Users[\\/]", t):
            bad_paths.append(str(p.relative_to(ROOT)))
        if re.search(r"(ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[0-9A-Z]{16})", t):
            bad_secrets.append(str(p.relative_to(ROOT)))
    check(not bad_paths, "no local absolute user paths", ", ".join(bad_paths))
    check(not bad_secrets, "no credential-looking strings", ", ".join(bad_secrets))

    refs = re.findall(r'(?:src|href)="(https?://[^"]+)"', html)
    check(not refs, "HTML has no external asset references", ", ".join(refs))

    print("\n%d checks failed" % len(FAILS))
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
