# -*- coding: utf-8 -*-
"""Rebuild the JSON data files from the artifact and the reference dataset.

    python scripts/build_data.py

Writes:
    data/muscles.json         20-row table used by forearm_mass_anatomy.html
    data/muscles_grouped.json 13 grouped muscle records from generate_artifact.py
    data/exercises.json       8 detailed exercise records from generate_artifact.py
"""
import ast
import contextlib
import io
import json
import pathlib
import re
import runpy

ROOT = pathlib.Path(__file__).resolve().parent.parent
HTML = ROOT / "forearm_mass_anatomy.html"
DATA = ROOT / "data"


def block(text, start, end):
    a = text.index(start) + len(start)
    b = text.index(end, a)
    return text[a:b]


def parse_muscles(html):
    raw = block(html, "const M = [", "];")
    rows = []
    for line in raw.splitlines():
        line = line.strip().rstrip(",")
        if not line.startswith("["):
            continue
        r = ast.literal_eval(line)
        rows.append({
            "rank": int(r[0]),
            "name": r[1],
            "compartment": r[2],
            "volume_cm3": float(r[3]),
            "volume_pct": float(r[4]),
            "pcsa_cm2": float(r[5]),
            "fiber_length_cm": float(r[6]),
            "pennation_deg": float(r[7]),
            "moment_arm": r[8],
            "score": float(r[9]),
            "tier": int(r[10]),
            "color": r[11],
        })
    return rows


def parse_notes(html):
    raw = block(html, "const NOTES = {", "};")
    notes = {}
    for line in raw.splitlines():
        m = re.match(r"\s*(\d+)\s*:\s*'(.*)',?\s*$", line)
        if m:
            notes[int(m.group(1))] = m.group(2)
    return notes


def parse_exercises_map(html):
    raw = block(html, "const EX = {", "};")
    ex = {}
    for line in raw.splitlines():
        m = re.match(r"\s*(\d+)\s*:\s*(.*?),?\s*$", line)
        if m:
            ex[int(m.group(1))] = ast.literal_eval(m.group(2))
    return ex


def slug(name):
    return re.sub(r"[^a-z]+", "_", name.lower()).strip("_")


def main():
    html = HTML.read_text(encoding="utf-8")
    notes = parse_notes(html)
    exmap = parse_exercises_map(html)
    muscles = []
    for r in parse_muscles(html):
        r["id"] = slug(r["name"])
        r["notes"] = notes.get(r["rank"], "")
        r["exercises"] = [{"name": n, "impact": i} for n, i in exmap.get(r["rank"], [])]
        muscles.append(r)

    volume = round(sum(m["volume_cm3"] for m in muscles), 1)
    pct = round(sum(m["volume_pct"] for m in muscles), 1)
    pcsa = round(sum(m["pcsa_cm2"] for m in muscles), 1)
    payload = {
        "title": "Forearm muscles used by forearm_mass_anatomy.html",
        "source": "forearm_mass_anatomy.html (M, NOTES and EX arrays)",
        "units": {
            "volume": "cm3",
            "volume_pct": "percent of the 20-row table total",
            "pcsa": "cm2",
            "fiber_length": "cm",
            "pennation": "degrees",
            "moment_arm": "cm",
        },
        "count": len(muscles),
        "totals": {
            "volume_cm3": volume,
            "volume_pct": pct,
            "pcsa_cm2": pcsa,
            "volume_percent_basis_cm3": volume,
        },
        "muscles": muscles,
    }
    DATA.mkdir(exist_ok=True)
    (DATA / "muscles.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    with contextlib.redirect_stdout(io.StringIO()):
        ref = runpy.run_path(str(ROOT / "scripts" / "generate_artifact.py"))
    grouped = {
        "title": "Grouped forearm muscle records from generate_artifact.py",
        "source": "scripts/generate_artifact.py (muscles_data)",
        "count": len(ref["muscles_data"]),
        "muscles": ref["muscles_data"],
    }
    (DATA / "muscles_grouped.json").write_text(
        json.dumps(grouped, indent=2) + "\n", encoding="utf-8")
    exercises = {
        "title": "Detailed exercise mapping from generate_artifact.py",
        "source": "scripts/generate_artifact.py (exercises_master)",
        "count": len(ref["exercises_master"]),
        "exercises": ref["exercises_master"],
    }
    (DATA / "exercises.json").write_text(
        json.dumps(exercises, indent=2) + "\n", encoding="utf-8")

    print("wrote data/muscles.json (%d muscles, %.1f cm3)" % (len(muscles), volume))
    print("wrote data/muscles_grouped.json (%d records)" % len(ref["muscles_data"]))
    print("wrote data/exercises.json (%d exercises)" % len(ref["exercises_master"]))


if __name__ == "__main__":
    main()
