# Forearm anatomy and mass guide

Interactive single-page guide to forearm anatomy and hypertrophy. It ranks 20 forearm muscles by contractile volume, physiological cross-sectional area (PCSA) and moment arm, maps exercises to muscles, and shows four medical plates with per-muscle reveals. Open `forearm_mass_anatomy.html` in a browser. No build step or server is needed; the four images in `images/` are local.

## Repo layout

- `forearm_mass_anatomy.html` - the artifact. All plate geometry, clip paths, labels and JavaScript are inline.
- `images/plate_*.jpg` - the four plates used by the artifact: superficial palmar, deep palmar, superficial dorsal, deep dorsal.
- `data/muscles.json` - the 20-row table used by the HTML, with volume, PCSA, fascicle length, pennation, moment arm, tier, notes and exercise mapping.
- `data/muscles_grouped.json` - the 12 grouped muscle records from `scripts/generate_artifact.py`, including origin, insertion, action and mass notes.
- `data/exercises.json` - the 8 detailed exercise records from `scripts/generate_artifact.py`.
- `scripts/build_data.py` - rebuilds the three JSON files from the HTML and the reference dataset.
- `scripts/generate_artifact.py` - reference dataset module. It does not write the HTML.
- `scripts/generate_segment.py` - injects a long-form scientific section into an older HTML revision. It expects a marker that the current trimmed HTML does not contain, so it exits with `Target marker not found`. Keep it for provenance.
- `tests/static_check.py` - checks assets, image references, HTML table counts and JSON consistency. No browser needed.
- `tests/check.py` - Playwright regression suite. Opens the HTML and checks the four views, hover and click behaviour, labels, leader lines and artwork.

## Data fields

| Field | Unit | Meaning |
| --- | --- | --- |
| `volume_cm3` | cm3 | Contractile muscle volume used by the ranking |
| `volume_pct` | percent | Share of the 20-row table total (486.9 cm3) |
| `pcsa_cm2` | cm2 | Physiological cross-sectional area |
| `fiber_length_cm` | cm | Fascicle length |
| `pennation_deg` | degrees | Pennation angle |
| `moment_arm` | text | Moment arm range and the action it belongs to |
| `score` | 0-10 | Heuristic ranking score, not a measured quantity |
| `tier` | 1-3 | Training priority group |
| `exercises` | list | Exercise name and impact (Primary, High, Assist) |

`data/exercises.json` adds primary and secondary muscles, biomechanics, a third-party protocol note and a prescription string for each exercise.

## Regenerate the data

```sh
python scripts/build_data.py
python tests/static_check.py
```

`build_data.py` reads the `M`, `NOTES` and `EX` arrays in the HTML and the two lists in `scripts/generate_artifact.py`. It writes the three JSON files.

The HTML itself is the canonical built artifact. There is no full HTML builder in this repo; the plate coordinates, masks, clip paths and label positions are inline. Editing the HTML directly and then rerunning `build_data.py` and the checks is the supported path.

## Run the browser regression suite

```sh
python -m pip install -r requirements.txt
python -m playwright install chromium   # optional if Chrome is already installed
python tests/check.py
```

On Windows the script uses the installed Chrome channel by default. Set `PLAYWRIGHT_CHANNEL=chromium` to use Playwright's bundled Chromium instead.

CI runs both checks on every push and pull request.

## Data caveats

- The volume and PCSA figures still need textbook citations. They are provisional working values, not established measurements. Do not cite them as sourced facts until each value is tied to a page or table.
- Three volume totals appear in the source: 486.9 cm3 (sum of the 20-row table, and the basis for its percentages), 438.7 cm3 (page header and video cards), and 447.8 cm3 (sum of the 12 grouped records). They do not reconcile. The grouped percentages also sum to 102.2%. Treat all of these as provisional.
- Moment arms and pennation angles are rounded ranges or approximations.
- The Roger C protocol notes are a third-party anecdotal report. They are not medical advice.

## Sources

See `REFERENCES.md`. The current HTML has no formal citations. The long-form section in `scripts/generate_segment.py` cites Holzbaur et al., 2005 and Lieber et al., 1992, but that section is not present in the trimmed artifact. Full bibliographic records are not in the source tree.

## License

MIT. See `LICENSE`. Image provenance and the citation gap are covered in `REFERENCES.md`.
