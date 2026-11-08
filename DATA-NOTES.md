# Data notes

This repo publishes a working dataset, not a sourced measurement table. Two problems are open: the volume totals do not reconcile, and the volume and PCSA values have no textbook citations. This file records exactly what is in the tree and what is missing.

## Three volume totals

| Total | Where it comes from | What it covers |
| --- | --- | --- |
| 486.9 cm3 | `data/muscles.json`, field `totals.volume_cm3`; also the sum of the 20 `volume_cm3` values in that file | The 20-rank table. It is the basis for `volume_pct`, which divides each row by 486.9. |
| 438.7 cm3 | `forearm_mass_anatomy.html`: the page-header stat "Total Mean Forearm Muscle Volume", the text "384.5 of 438.7 cm3", and the simulator constant `B1=206.2,B2=137.3,B3=95.3,T=438.7` | The header figure and the three-band simulator. The three band values are styled weights, not a muscle-by-muscle sum. |
| 447.8 cm3 | Sum of the 12 `volume` values in `data/muscles_grouped.json` | The 12 grouped muscle records used by `scripts/generate_artifact.py`. Their `volume_pct` values sum to 102.2%, so the grouped percentages are also not on a 100% basis. |

The three totals differ by up to 48.2 cm3. Nothing in the repo defines which population, inclusion rule or rounding produced each one, so they cannot be reconciled from the current source. The 20-row `volume_pct` values sum to 99.8% because of per-row rounding. Do not present any of these totals as a measured forearm volume.

## Missing citations for volume and PCSA

Every `volume_cm3` and `pcsa_cm2` value in `data/muscles.json` and every `volume` and `pcsa` value in `data/muscles_grouped.json` is unsourced. No page, table, edition or dataset is recorded for any row.

The only citations in the tree are in `scripts/generate_segment.py`: Holzbaur et al., 2005 and Lieber et al., 1992. They appear as in-text names for forearm architectural data in a long-form section that is not part of the current trimmed HTML. The repo contains no journal, volume, page numbers or DOI for either paper, so those records are incomplete as well.

`REFERENCES.md` lists the same gap and the plate-provenance gap. This file does not add any new source or value.

## What would close these gaps

1. Pick one volume table and state its inclusion rule, then rebuild all three totals from that single table so the header, simulator and grouped records agree.
2. Cite a page or table in a standard anatomy source for each volume and PCSA value, and record the edition.
3. Either recover the full bibliographic records for Holzbaur et al., 2005 and Lieber et al., 1992, or remove the in-text names until they are verified.
